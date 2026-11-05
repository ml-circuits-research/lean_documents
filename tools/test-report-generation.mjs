/** Isolated report-writer integration tests. The explicit stub never runs Codex. */
import assert from 'node:assert/strict';
import { test } from 'node:test';
import { spawn } from 'node:child_process';
import { once } from 'node:events';
import { createHash } from 'node:crypto';
import fs from 'node:fs/promises';
import net from 'node:net';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { writeExample, readExample } from './markdown-store.mjs';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
await fs.mkdir(path.join(ROOT, 'tmp/report-generation-tests'), { recursive: true });
const suite = await fs.mkdtemp(path.join(ROOT, 'tmp/report-generation-tests/run-'));
console.log(`Explicit simulated executor; retained test artifacts: ${suite}`);
const pause = ms => new Promise(resolve => setTimeout(resolve, ms));
const digest = value => createHash('sha256').update(value).digest('hex');
const sourceBytes = Buffer.from('# Investment terms\r\n\r\n## S01 — Subscription\r\n\r\nThe proposed subscription is EUR 8 million for 20% of equity after issuance. All amounts are exact.\r\n');

const stub = `#!${process.execPath}
import fs from 'node:fs/promises';
import path from 'node:path';
let prompt=''; process.stdin.setEncoding('utf8');
process.stdin.on('data',chunk=>prompt+=chunk);
process.stdin.on('end',async()=>{
  const cwd=process.cwd();
  await fs.writeFile(path.join(cwd,'stub-input.md'),'# Simulated executor input\\n\\n'+prompt);
  if(prompt.includes('Audit ONLY')) {
    if(process.env.STUB_AUDIT_WAIT==='1') {await fs.writeFile('stub-waiting.md','# Simulated waiting audit\\n');setInterval(()=>{},1000);return;}
    console.error('Explicit simulated audit failure: no audit or proof was performed.');process.exitCode=7;return;
  }
  if(prompt.includes('Requested title: WAIT')) {
    await fs.writeFile('stub-waiting.md','# Simulated waiting writer\\n');
    while(true){try{await fs.access('stub-release.md');break;}catch{}await new Promise(r=>setTimeout(r,20));}
  }
  const names=await fs.readdir('sources');const source='sources/'+names[0];
  const ro=prompt.includes('Language: Romanian');
  const report=prompt.includes('Requested title: INVALID')?'# Invalid draft\\n\\nThis deliberately invalid structural fixture has no anchored finding or required source citation. It must never be published.\\n':
    '# '+(ro?'Raport de investiție':'Investment report')+'\\n\\n## R01 — '+(ro?'Subscriere':'Subscription')+'\\n\\n'+(ro?'Subscrierea propusă este de 8 milioane EUR.':'The proposed subscription is EUR 8 million.')+'\\n\\n'+(ro?'Condițiile consemnate indică suma propusă și participația aferentă.':'The recorded transaction terms state the proposed amount and the corresponding ownership interest.')+' ['+(ro?'Condițiile tranzacției S01':'Transaction terms S01')+']('+source+'#s01--subscription).\\n';
  await fs.writeFile('report.md',report);
  await fs.writeFile('generation-notes.md','# Simulated generation notes\\n\\nThis document comes from an explicit test stub, not Codex. It tests publication boundaries only. Mode: '+(prompt.includes('Mode: with_errors')?'with_errors':'grounded')+'. No audit, semantic validation or proof was performed.\\n');
  if(prompt.includes('Requested title: MUTATE'))await fs.appendFile(source,'\\nChanged by simulated writer.\\n');
  console.log(JSON.stringify({type:'stub.completed',item:{text:'Explicit simulated draft created; no real generation occurred.'}}));
});
`;

async function start(name, { missing = false, auditWait = false } = {}) {
  const directory = path.join(suite, name), examples = path.join(directory, 'examples'), runs = path.join(directory, 'runs'), jobs = path.join(directory, 'report-jobs');
  await fs.mkdir(examples, { recursive: true });
  const executable = path.join(directory, missing ? 'missing-executor' : 'stub-executor.mjs');
  if (!missing) await fs.writeFile(executable, stub, { mode: 0o700 });
  const probe = net.createServer(); probe.listen(0, '127.0.0.1'); await once(probe, 'listening');
  const port = probe.address().port; await new Promise(resolve => probe.close(resolve));
  const child = spawn(process.execPath, [path.join(ROOT, 'tools/audit-ui.mjs')], { cwd: ROOT,
    env: { ...process.env, PORT: String(port), AUDIT_RUNS_ROOT: runs, AUDIT_EXAMPLES_ROOT: examples, AUDIT_DOCUMENT_PILOT: '1', AUDIT_TEST_MODE: '1', AUDIT_CONCURRENCY: '1', CODEX_BIN: executable, STUB_AUDIT_WAIT: auditWait ? '1' : '0' }, stdio: ['ignore', 'pipe', 'pipe'] });
  let output = ''; child.stdout.on('data', b => output += b); child.stderr.on('data', b => output += b);
  for (let n = 0; n < 100 && !output.includes('Audit laboratory:'); n++) { if (child.exitCode !== null) throw Error(output); await pause(20); }
  assert.match(output, /Audit laboratory:/);
  const origin = `http://127.0.0.1:${port}`;
  async function request(route, data, status = 200) {
    const response = await fetch(origin + route, data === undefined ? {} : { method: 'POST', headers: { 'Content-Type': 'application/json', Origin: origin }, body: JSON.stringify(data) });
    const value = await response.json(); assert.equal(response.status, status, `${route}: ${JSON.stringify(value)}`); return value;
  }
  async function waitFor(route, predicate) {
    for (let n = 0; n < 200; n++) { assert.equal(child.exitCode, null, output); const value = await request(route); if (predicate(value)) return value; await pause(25); }
    throw Error(`Timed out waiting for ${route}`);
  }
  return { directory, examples, runs, jobs, request,
    terminal: id => waitFor(`/api/report-jobs/${id}`, v => ['finished', 'failed', 'stopped'].includes(v.status)),
    auditTerminal: id => waitFor(`/api/runs/${id}`, v => !['queued', 'running', 'finalizing'].includes(v.status)),
    async waitMarker(base) { for (let n = 0; n < 150; n++) { try { await fs.access(path.join(base, 'stub-waiting.md')); return; } catch {} await pause(20); } throw Error('Waiting stub did not start'); },
    async close() { if (child.exitCode === null && child.signalCode === null) { child.kill('SIGTERM'); await once(child, 'exit'); } await fs.writeFile(path.join(directory, 'server-output.md'), '# Isolated server output\n\n```text\n' + output + '\n```\n'); },
  };
}

async function example(server, { id = 'investment', language = 'en', sources = true } = {}) {
  const base = path.join(server.examples, id); await fs.mkdir(path.join(base, 'sources'), { recursive: true });
  if (sources) await fs.writeFile(path.join(base, 'sources/terms.md'), sourceBytes);
  await fs.writeFile(path.join(base, 'report.md'), '# Existing report\n\n## R01 — Subscription\n\nThe proposed subscription is EUR 8 million.\n');
  await writeExample(path.join(base, 'example.md'), { schema_version: 1, title: 'Investment terms', description: '', question: '', source_directory: 'sources', language, reports: [{ path: 'report.md', label: 'Existing report' }] });
  return { id, base };
}
const generate = (server, id, title = 'Investment draft', mode = 'grounded') => server.request(`/api/examples/${id}/reports/generate`, { title, mode });

await test('drafts preserve sources, honor mode/language and publish only the report; later audits exclude writer notes and replace old runs', { timeout: 25000 }, async () => {
  const server = await start('publication');
  try {
    for (const [language, mode] of [['en', 'grounded'], ['ro', 'with_errors']]) {
      const { id, base } = await example(server, { id: `investment-${language}`, language });
      const queued = await generate(server, id, 'Investment draft', mode);
      const job = await server.terminal(queued.id); assert.equal(job.status, 'finished', job.error);
      const directory = path.join(server.jobs, job.id);
      assert.deepEqual(await fs.readFile(path.join(directory, 'sources/terms.md')), sourceBytes);
      const records = JSON.parse(await fs.readFile(path.join(directory, 'internal/sources.json'), 'utf8'));
      assert.equal(records[0].sha256, digest(sourceBytes));
      const instructions = await fs.readFile(path.join(directory, 'instructions.md'), 'utf8');
      assert.ok(instructions.includes(`Language: ${language === 'ro' ? 'Romanian' : 'English'}`)); assert.ok(instructions.includes(`Mode: ${mode}`));
      assert.ok(instructions.includes('investment-report-writer/SKILL.md'));
      assert.equal(path.dirname(job.reportPath), '.');
      const metadata = await readExample(path.join(base, 'example.md'));
      assert.equal(metadata.reports.length, 2); assert.equal(metadata.reports[1].path, job.reportPath);
      const published = await fs.readFile(path.join(base, job.reportPath)); assert.equal(digest(published), job.reportSha256);
      assert.deepEqual((await fs.readdir(base)).sort(), ['example.md', 'report.md', job.reportPath, 'sources'].sort());
      const catalog = await server.request('/api/examples');
      assert.ok(catalog.find(v => v.id === id).generationJobs.some(v => v.id === job.id));
      assert.ok(job.files.every(file => !file.path.startsWith('internal/') && !file.path.endsWith('.json')));
      const notes = await server.request('/api/file?' + new URLSearchParams({ job: job.id, path: 'generation-notes.md' })); assert.match(notes.text, /explicit test stub/);
      await server.request('/api/file?' + new URLSearchParams({ job: job.id, path: '../outside.md' }), undefined, 400);
      const first = await server.request('/api/runs', { exampleId: id, reportPath: job.reportPath });
      assert.equal((await server.auditTerminal(first.id)).status, 'failed');
      assert.deepEqual(await fs.readFile(path.join(server.runs, first.id, 'inputs/report.md')), published);
      assert.deepEqual(await fs.readFile(path.join(server.runs, first.id, 'inputs/sources/terms.md')), sourceBytes);
      assert.deepEqual((await fs.readdir(path.join(server.runs, first.id, 'inputs'))).sort(), ['report.md', 'sources']);
      assert.deepEqual(await fs.readdir(path.join(server.runs, first.id, 'inputs/sources')), ['terms.md']);
      const next = await server.request('/api/runs', { exampleId: id, reportPath: job.reportPath }); await server.auditTerminal(next.id);
      await assert.rejects(fs.stat(path.join(server.runs, first.id)), { code: 'ENOENT' });
      const refreshed = (await server.request('/api/examples')).find(v => v.id === id);
      assert.deepEqual(refreshed.runs.map(v => v.id), [next.id]);
    }
  } finally { await server.close(); }
});

await test('invalid mode and missing sources are rejected before a job starts', { timeout: 10000 }, async () => {
  const server = await start('invalid-requests');
  try {
    const one = await example(server), empty = await example(server, { id: 'empty', sources: false });
    await server.request(`/api/examples/${one.id}/reports/generate`, { title: 'Draft', mode: 'unsupported' }, 400);
    await server.request(`/api/examples/${empty.id}/reports/generate`, { title: 'Draft', mode: 'grounded' }, 400);
    assert.deepEqual(await fs.readdir(server.jobs), []);
  } finally { await server.close(); }
});

await test('missing executor and structurally invalid drafts fail without publication', { timeout: 15000 }, async () => {
  for (const missing of [true, false]) {
    const server = await start(missing ? 'missing-executor' : 'invalid-draft', { missing });
    try {
      const { id, base } = await example(server);
      const queued = await generate(server, id, missing ? 'Draft' : 'INVALID draft');
      const job = await server.terminal(queued.id); assert.equal(job.status, 'failed');
      assert.match(job.error, missing ? /ENOENT|spawn/ : /validation|anchor/i);
      assert.equal((await readExample(path.join(base, 'example.md'))).reports.length, 1);
      assert.ok(!(await fs.readdir(base)).some(file => file.startsWith('report-generated-')));
    } finally { await server.close(); }
  }
});

await test('changing original or retained source bytes blocks draft publication', { timeout: 15000 }, async () => {
  const server = await start('source-changes');
  try {
    for (const retained of [false, true]) {
      const { id, base } = await example(server, { id: retained ? 'retained-change' : 'original-change' });
      const queued = await generate(server, id, retained ? 'MUTATE draft' : 'WAIT draft');
      if (!retained) {
        const directory = path.join(server.jobs, queued.id); await server.waitMarker(directory);
        await fs.appendFile(path.join(base, 'sources/terms.md'), '\nA later source amendment.\n');
        await fs.writeFile(path.join(directory, 'stub-release.md'), '# Release simulated writer\n');
      }
      const job = await server.terminal(queued.id); assert.equal(job.status, 'failed'); assert.match(job.error, /source.*changed/i);
      assert.equal((await readExample(path.join(base, 'example.md'))).reports.length, 1);
    }
  } finally { await server.close(); }
});

await test('example stop cancels both an executing process and its queued sibling job', { timeout: 20000 }, async () => {
  for (const auditFirst of [true, false]) {
    const server = await start(auditFirst ? 'stop-audit-first' : 'stop-writer-first', { auditWait: true });
    try {
      const { id } = await example(server);
      let audit, job;
      if (auditFirst) {
        audit = await server.request('/api/runs', { exampleId: id, reportPath: 'report.md' }); await server.waitMarker(path.join(server.runs, audit.id));
        job = await generate(server, id, 'WAIT draft'); assert.equal((await server.request(`/api/report-jobs/${job.id}`)).status, 'queued');
      } else {
        job = await generate(server, id, 'WAIT draft'); await server.waitMarker(path.join(server.jobs, job.id));
        audit = await server.request('/api/runs', { exampleId: id, reportPath: 'report.md' }); assert.equal((await server.request(`/api/runs/${audit.id}`)).status, 'queued');
      }
      const stopped = await server.request(`/api/examples/${id}/stop`, {});
      assert.deepEqual(new Set(stopped.jobs), new Set([audit.id, job.id]));
      assert.equal((await server.terminal(job.id)).status, 'stopped');
      assert.equal((await server.auditTerminal(audit.id)).status, 'stopped');
      assert.ok(!(await fs.readdir(path.join(server.examples, id))).some(name => name.startsWith('report-generated-')));
    } finally { await server.close(); }
  }
});
