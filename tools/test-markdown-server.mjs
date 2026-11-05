/** Isolated integration checks; all inputs, logs and runs stay under tmp/. */
import assert from 'node:assert/strict';
import { test } from 'node:test';
import { spawn, execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { once } from 'node:events';
import net from 'node:net';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { readExample } from './markdown-store.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
await fs.mkdir(path.join(root, 'tmp/markdown-server-tests'), { recursive: true });
const suite = await fs.mkdtemp(path.join(root, 'tmp/markdown-server-tests/run-'));
console.log(`Retained isolated server checks: ${suite}`);
const pause = ms => new Promise(resolve => setTimeout(resolve, ms));

async function startServer(name, mode, pilot = false) {
  const directory = path.join(suite, name), examples = path.join(directory, 'examples'), runs = path.join(directory, 'runs');
  await fs.mkdir(examples, { recursive: true });
  await fs.mkdir(path.join(examples, 'builder-without-metadata'));
  let executable = path.join(directory, 'missing-codex');
  if (mode !== 'missing') {
    executable = path.join(directory, 'stub-codex.mjs');
    await fs.writeFile(executable, `#!${process.execPath}\n// Explicit simulation: this process never performs an audit.\nprocess.stdin.resume();\nprocess.stdin.on('end',()=>{console.log(JSON.stringify({type:'test.stub',item:{text:'Simulated executor; no audit was performed.'}}));console.error('Intentional test diagnostic');process.exit(${mode === 'failure' ? 7 : 0});});\n`, { mode: 0o700 });
  }
  const probe = net.createServer();
  probe.listen(0, '127.0.0.1'); await once(probe, 'listening');
  const port = probe.address().port; await new Promise(resolve => probe.close(resolve));
  const child = spawn(process.execPath, [path.join(root, 'tools/audit-ui.mjs')], {
    cwd: root, env: { ...process.env, PORT: String(port), AUDIT_RUNS_ROOT: runs, AUDIT_EXAMPLES_ROOT: examples, CODEX_BIN: executable, AUDIT_TEST_MODE: '1', AUDIT_DOCUMENT_PILOT: pilot ? '1' : '0' },
    stdio: ['ignore', 'pipe', 'pipe'],
  });
  let output = '';
  child.stdout.on('data', bytes => { output += bytes; });
  child.stderr.on('data', bytes => { output += bytes; });
  const origin = `http://127.0.0.1:${port}`;
  async function request(route, data, expected = 200) {
    const response = await fetch(origin + route, data === undefined ? {} : { method: 'POST', headers: { 'Content-Type': 'application/json', Origin: origin }, body: JSON.stringify(data) });
    const body = await response.json();
    assert.equal(response.status, expected, `${route}: ${JSON.stringify(body)}`);
    return body;
  }
  for (let index = 0; index < 100 && !output.includes('Audit laboratory:'); index++) {
    if (child.exitCode !== null) throw Error(`Server exited before startup: ${output}`);
    await pause(30);
  }
  assert.match(output, /Audit laboratory:/, 'isolated server started');
  return { directory, examples, runs, child, request, origin,
    async stop() {
      if (child.exitCode === null && child.signalCode === null) { child.kill('SIGTERM'); await once(child, 'exit'); }
      await fs.writeFile(path.join(directory, 'server-output.md'), '# Isolated server output\n\n```text\n' + output + '\n```\n');
    },
    async terminal(id) {
      for (let index = 0; index < 160; index++) {
        if (child.exitCode !== null || child.signalCode !== null) throw Error(`Server crashed while recording executor failure:\n${output}`);
        const result = await request(`/api/runs/${id}`);
        if (!['queued', 'running', 'finalizing'].includes(result.status)) return result;
        await pause(30);
      }
      throw Error('Run never reached a terminal state');
    },
  };
}

async function seed(server) {
  const { id } = await server.request('/api/examples', { title: 'Household bill', description: '' });
  const catalog = await server.request('/api/examples');
  assert.equal(catalog.length, 1, 'directories without metadata are skipped');
  assert.deepEqual(catalog[0].reports, []);
  const metadata = await readExample(path.join(server.examples, id, 'example.md'));
  assert.equal(metadata.description, ''); assert.equal(metadata.question, ''); assert.deepEqual(metadata.reports, []);
  const bytes = Buffer.from('# Supplied report\r\n\r\n[R1] Total is 9.\r\n', 'utf8');
  const uploaded = await server.request(`/api/examples/${id}/files`, { role: 'report', files: [{ name: 'Original report.md', data: bytes.toString('base64') }] });
  const report = uploaded.reports[0];
  assert.deepEqual(await fs.readFile(path.join(server.examples, id, report.path)), bytes);
  return { id, report, bytes };
}

async function noDataDocuments(directory) {
  for (const entry of await fs.readdir(directory, { withFileTypes: true })) {
    const file = path.join(directory, entry.name);
    if (entry.isDirectory()) await noDataDocuments(file);
    else assert.ok(!/\.(json|jsonl|log)$/i.test(entry.name), `Unexpected persisted data/log document: ${file}`);
  }
}

await test('Markdown uploads preserve bytes, support concurrent catalog reads, protect paths, and record failed executor honestly', { timeout: 30000 }, async () => {
  const server = await startServer('uploads-and-failure', 'failure');
  try {
    const { id, report, bytes } = await seed(server);
    let reading = true, reads = 0;
    const reader = (async () => { while (reading) { const catalog = await server.request('/api/examples'); assert.equal(catalog.length, 1); reads++; await pause(2); } })();
    const sources = Array.from({ length: 12 }, (_, i) => ({ name: i === 0 ? '../Original | bill.md' : `Document ${i}.md`, bytes: Buffer.from(`Source ${i}\r\nexact bytes: ș €\n`) }));
    try {
      await Promise.all(sources.map(source => server.request(`/api/examples/${id}/files`, { role: 'source', files: [{ name: source.name, data: source.bytes.toString('base64') }] })));
    } finally { reading = false; }
    await reader; assert.ok(reads > 0);
    const [example] = await server.request('/api/examples');
    assert.equal(example.files.filter(file => file.role === 'source').length, sources.length);
    const metadata = await readExample(path.join(server.examples, id, 'example.md'));
    for (const source of sources) {
      const relative = Object.keys(metadata.file_names).find(file => metadata.file_names[file] === source.name);
      assert.ok(relative?.startsWith('sources/document-'));
      assert.deepEqual(await fs.readFile(path.join(server.examples, id, relative)), source.bytes);
      const download = await fetch(server.origin + '/api/file?' + new URLSearchParams({ example: id, path: relative, download: '1' }));
      assert.equal(download.status, 200); assert.deepEqual(Buffer.from(await download.arrayBuffer()), source.bytes);
    }
    const outside = path.join(server.directory, 'outside.md'); await fs.writeFile(outside, 'Outside selected example');
    await fs.symlink(outside, path.join(server.examples, id, 'outside-link.md'));
    await fs.mkdir(path.join(server.examples, id, 'evaluator')); await fs.writeFile(path.join(server.examples, id, 'evaluator/expected.md'), 'Withheld');
    for (const relative of ['../outside.md', '/etc/passwd', 'evaluator/expected.md', 'outside-link.md']) {
      await server.request('/api/file?' + new URLSearchParams({ example: id, path: relative }), undefined, 400);
    }
    await server.request('/api/file?' + new URLSearchParams({ example: '../bad', path: 'example.md' }), undefined, 400);
    const invalidOrigin = await fetch(server.origin + '/api/examples', { method: 'POST', headers: { 'Content-Type': 'application/json', Origin: 'https://untrusted.invalid' }, body: '{}' });
    assert.equal(invalidOrigin.status, 400);
    const run = await server.request('/api/runs', { exampleId: id, reportPath: report.path });
    const result = await server.terminal(run.id);
    assert.equal(result.status, 'failed'); assert.equal(result.exitCode, 7); assert.equal(result.reportAvailability.status, 'unavailable');
    assert.equal(result.auditReportPath, null); assert.deepEqual(result.findings, []);
    const runDirectory = path.join(server.runs, run.id);
    assert.deepEqual(await fs.readFile(path.join(runDirectory, 'inputs/report.md')), bytes);
    const snapshots = await fs.readdir(path.join(runDirectory, 'inputs/sources'));
    assert.equal(snapshots.length, sources.length);
    const saved = await Promise.all(snapshots.map(file => fs.readFile(path.join(runDirectory, 'inputs/sources', file))));
    for (const source of sources) assert.ok(saved.some(value => value.equals(source.bytes)));
    assert.match(await fs.readFile(path.join(runDirectory, 'run.md'), 'utf8'), /## Status\n\nfailed/);
    assert.match(await fs.readFile(path.join(runDirectory, 'execution.md'), 'utf8'), /Simulated executor/);
    await noDataDocuments(server.directory);
  } finally { await server.stop(); }
});

await test('missing executor becomes a failed run without crashing the server', { timeout: 15000 }, async () => {
  const server = await startServer('missing-executor', 'missing');
  try {
    const { id, report } = await seed(server);
    const run = await server.request('/api/runs', { exampleId: id, reportPath: report.path });
    const result = await server.terminal(run.id);
    assert.equal(result.status, 'failed'); assert.match(result.error, /ENOENT|spawn/);
    assert.equal(result.reportAvailability.status, 'unavailable');
    assert.equal((await server.request('/api/examples')).length, 1);
    await noDataDocuments(server.directory);
  } finally { await server.stop(); }
});

await test('zero executor exit without an audit is incomplete, never verified', { timeout: 15000 }, async () => {
  const server = await startServer('empty-success', 'success');
  try {
    const { id, report } = await seed(server);
    const run = await server.request('/api/runs', { exampleId: id, reportPath: report.path });
    const result = await server.terminal(run.id);
    assert.equal(result.status, 'incomplete'); assert.equal(result.exitCode, 0);
    assert.equal(result.reportAvailability.status, 'unavailable'); assert.equal(result.auditReportPath, null);
    assert.match(result.error, /did not pass/);
    await noDataDocuments(server.directory);
  } finally { await server.stop(); }
});

await test('fresh controlled Lean audit exposes links, detects tampering, and repairs rendered reports', { timeout: 60000 }, async () => {
  // Build an explicit synthetic helper fixture now; no user audit or deleted
  // historical run is read, restored or required. Lean really executes here.
  const fixtureRoot = path.join(suite, 'controlled-fixture');
  await fs.mkdir(fixtureRoot);
  const exercise = path.join(fixtureRoot, 'exercise.py');
  await fs.writeFile(exercise, `from pathlib import Path
import sys
sys.path.insert(0, str(Path(sys.argv[1]) / 'tests'))
import test_document_audit as fixture
fixture.TEST_ROOT = Path(sys.argv[2])
workspace = fixture.completed_fixture()
print('CONTROLLED_WORKSPACE=' + str(workspace))
`);
  let execution;
  try {
    execution = await promisify(execFile)('python3', [exercise, root, fixtureRoot], { cwd: root, timeout: 45000, maxBuffer: 4 * 1024 * 1024 });
  } catch (error) {
    await fs.writeFile(path.join(fixtureRoot, 'execution.md'), '# Controlled fixture execution failed\n\n```text\n' + (error.stdout || '') + '\n' + (error.stderr || error.message) + '\n```\n');
    throw error;
  }
  await fs.writeFile(path.join(fixtureRoot, 'execution.md'), '# Controlled fixture execution\n\nThe retained Python script called the real helper and Lean checks. No Codex process or user audit was reused. Exit code: 0.\n\n```text\n' + execution.stdout + '\n' + execution.stderr + '\n```\n');
  const originalWorkspace = /^CONTROLLED_WORKSPACE=(.+)$/m.exec(execution.stdout)?.[1];
  assert.ok(originalWorkspace && originalWorkspace.startsWith(fixtureRoot + path.sep));
  const originalReport = await fs.readFile(path.join(originalWorkspace, 'audit-report.md'));
  const originalValidation = await fs.readFile(path.join(originalWorkspace, 'validation.md'));
  const server = await startServer('controlled-document-audit', 'missing', true);
  try {
    const id = 'controlled-proof-fixture', runDirectory = path.join(server.runs, id);
    const workspace = path.join(runDirectory, 'work', path.basename(originalWorkspace));
    await fs.mkdir(path.dirname(workspace), { recursive: true });
    await fs.cp(originalWorkspace, workspace, { recursive: true, force: false, errorOnExist: true });
    await fs.mkdir(path.join(runDirectory, 'internal'));
    const state = { schema_version: 2, id, exampleId: 'controlled-fixture', exampleTitle: 'Fresh synthetic helper fixture', created: new Date().toISOString(), status: 'finished', test: true, language: 'en' };
    await fs.writeFile(path.join(runDirectory, 'internal/run.json'), JSON.stringify(state, null, 2) + '\n');
    await fs.writeFile(path.join(runDirectory, 'run.md'), '# Controlled helper fixture\n\nThis test generated a new synthetic audit and executed real Lean checks. It did not run Codex or restore a previous user audit. The source workspace is retained separately for comparison.\n');
    await fs.writeFile(path.join(runDirectory, 'fixture-provenance.md'), `# Controlled regression fixture\n\nFreshly generated by ${exercise}, then copied without modifying workspace bytes from ${originalWorkspace}.\n\nActual Lean target and axiom checks ran during fixture creation. The API checks below inspect their retained results; the copy does not claim an additional proof execution or independent semantic review.\n`);
    let result = await server.request(`/api/runs/${id}`);
    assert.equal(result.reportAvailability.status, 'ready', JSON.stringify(result));
    assert.equal(result.proofIntegrity.status, 'matches'); assert.equal(result.reportBinding.status, 'matches');
    assert.ok(result.findings.length > 0); assert.ok(result.proofResults.targets.length > 0);
    const links = new Set([result.auditReportPath, result.findingsPath]);
    for (const finding of result.findings) {
      links.add(finding.path);
      for (const evidence of finding.evidence) links.add(evidence.path);
      for (const proof of finding.proofs) links.add(proof.path);
    }
    for (const target of result.proofResults.targets) { links.add(target.check_file); links.add(target.log); }
    for (const relative of links) {
      assert.ok(relative, 'returned artifact link must be present');
      const value = await server.request('/api/file?' + new URLSearchParams({ run: id, path: relative }));
      assert.ok(value.size > 0, relative);
      if (relative.endsWith('.lean')) assert.equal(typeof value.text, 'string');
    }
    const reportPath = path.join(runDirectory, result.auditReportPath);
    await fs.appendFile(reportPath, '\nThis line is a test modification of rendered prose only.\n');
    result = await server.request(`/api/runs/${id}`);
    assert.equal(result.reportAvailability.status, 'stale'); assert.equal(result.reportAvailability.canRender, true);
    assert.equal(result.proofIntegrity.status, 'matches');
    result = await server.request(`/api/runs/${id}/render`, {});
    assert.equal(result.reportAvailability.status, 'ready');
    assert.deepEqual(await fs.readFile(reportPath), originalReport);
    await fs.unlink(reportPath);
    result = await server.request(`/api/runs/${id}`);
    assert.equal(result.reportAvailability.status, 'renderable'); assert.equal(result.reportAvailability.canRender, true);
    result = await server.request(`/api/runs/${id}/render`, {});
    assert.equal(result.reportAvailability.status, 'ready'); assert.deepEqual(await fs.readFile(reportPath), originalReport);
    const findingPath = path.join(workspace, 'findings', result.findings[0].claim_id + '.json');
    const finding = JSON.parse(await fs.readFile(findingPath, 'utf8'));
    finding.reasoning += ' Unvalidated test modification of the canonical finding.';
    await fs.writeFile(findingPath, JSON.stringify(finding, null, 2) + '\n');
    result = await server.request(`/api/runs/${id}`);
    assert.equal(result.reportAvailability.status, 'stale'); assert.equal(result.proofIntegrity.status, 'changed');
    assert.equal(result.reportAvailability.canRender, false);
    const rejection = await server.request(`/api/runs/${id}/render`, {}, 400);
    assert.match(rejection.error, /validation failed|changed|stale|check/i);
    assert.deepEqual(await fs.readFile(reportPath), originalReport, 'failed rendering must not replace the previous report');
    assert.ok(result.files.every(file => !file.path.startsWith('internal/') && !/\.jsonl?$/.test(file.path)), 'internal persistence must stay out of human artifact listings');
    assert.deepEqual(await fs.readFile(path.join(originalWorkspace, 'audit-report.md')), originalReport, 'freshly generated fixture report is untouched');
    assert.deepEqual(await fs.readFile(path.join(originalWorkspace, 'validation.md')), originalValidation, 'freshly generated fixture validation is untouched');
  } finally { await server.stop(); }
});

await test('Example language persists and controls the audit while uploaded bytes remain unchanged', {timeout: 30000}, async()=>{
  const server = await startServer('romanian-pilot-language','success',true);
  try {
    await server.request('/api/examples',{title:'Invalid language',language:'fr'},400);
    const created = await server.request('/api/examples',{title:'Aprobarea investiției',description:'Exemplu de test izolat.',language:'ro'});
    const reportBytes=Buffer.from('# Raport\n\nAfirmație în limba română.\n','utf8');
    const sourceBytes=Buffer.from('# Document sursă\n\nValoarea propusă este 8 milioane EUR.\n','utf8');
    const uploaded=await server.request(`/api/examples/${created.id}/files`,{role:'report',files:[{name:'raport.md',data:reportBytes.toString('base64')}]});
    await server.request(`/api/examples/${created.id}/files`,{role:'source',files:[{name:'termeni.md',data:sourceBytes.toString('base64')}]});
    const [example]=await server.request('/api/examples');
    assert.equal(example.language,'ro');
    assert.equal((await readExample(path.join(server.examples,created.id,'example.md'))).language,'ro');
    const started=await server.request('/api/runs',{exampleId:created.id,reportPath:uploaded.reports[0].path});
    const completed=await server.terminal(started.id);
    assert.equal(completed.language,'ro');assert.equal(completed.test,true);assert.equal(completed.status,'incomplete');
    assert(completed.files.every(file=>!file.path.startsWith('internal/')&&!/\.jsonl?$/.test(file.path)));
    const instructions=await fs.readFile(path.join(server.runs,started.id,'instructions.md'),'utf8');
    assert.match(instructions,/--language ro/);assert.match(instructions,/human documents in Romanian/);
    assert.deepEqual(await fs.readFile(path.join(server.runs,started.id,'inputs/report.md')),reportBytes);
    const names=await fs.readdir(path.join(server.runs,started.id,'inputs/sources'));
    assert.equal(names.length,1);assert.deepEqual(await fs.readFile(path.join(server.runs,started.id,'inputs/sources',names[0])),sourceBytes);
  } finally {await server.stop();}
});
