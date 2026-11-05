#!/usr/bin/env python3
"""Create, verify, render, and export evidence-backed report audit workspaces.

Source filtering is defense in depth, not a sandbox for hostile Lean programs.
Only review trusted, inspected Lean source. Truth and model adequacy still require
independent semantic review; a checked theorem establishes its encoded proposition.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import shlex
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus
import corrections
import contracts
import journal

VERSION = '4.24.0'
MODULE_NAME = r'[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*'
MODULE_POLICY = 'Init/Std and recursively inspected local models only'
REQUIRED = {'claim_id', 'report_quote', 'report_anchor', 'question', 'evidence', 'rules',
            'assumptions', 'reasoning', 'semantic_state', 'argument_status',
            'formal_status', 'proofs', 'limits', 'recommendation'}
STATES = {
    'semantic_state': {'supported', 'refuted', 'both', 'undetermined', 'not_applicable'},
    'argument_status': {'sufficient', 'insufficient_support', 'invalid_inference', 'unsound_argument', 'disputed', 'nonformal'},
    'formal_status': {'proved', 'refuted', 'auxiliary', 'not_attempted', 'blocked'},
}
CAVEAT = ('Lean checks the encoded propositions, not source authenticity, extraction accuracy, '
          'completeness, legal authority, or the adequacy of the model. Source filters are '
          'defensive checks, not a sandbox for hostile Lean code.')


class AuditError(Exception):
    pass


def now():
    return datetime.now(timezone.utc).isoformat()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def read_json(path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        raise AuditError(f'Cannot read JSON {path}: {exc}') from exc


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def paragraphs(text):
    explicit = list(re.finditer(r'<a\s+id=[\"\']([^\"\']+)[\"\']\s*>\s*</a>', text))
    if explicit:
        result = {}
        prefix = text[:explicit[0].start()].strip()
        if prefix:
            anchor = 'document-preamble'
            while anchor in {m.group(1) for m in explicit}: anchor += '-preamble'
            result[anchor] = prefix
        for index, match in enumerate(explicit):
            anchor = match.group(1)
            if anchor in result:
                raise AuditError(f'Duplicate explicit anchor: {anchor}')
            end = explicit[index+1].start() if index+1 < len(explicit) else len(text)
            result[anchor] = text[match.end():end].strip()
        return result
    return {f'P{i:02d}': part.strip() for i, part in enumerate(
        (p for p in re.split(r'\n\s*\n', text.replace('\r\n', '\n')) if p.strip()), 1)}


def safe_path(root, relative):
    if not isinstance(relative, str) or Path(relative).is_absolute():
        raise AuditError(f'Expected relative path: {relative}')
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise AuditError(f'Path escapes workspace: {relative}')
    return path


def verify_manifest(root):
    manifest = read_json(root / 'input/manifest.json')
    if manifest.get('schema_version') == 2:
        return corpus.verify(root)
    expected = manifest.get('files', {})
    if read_json(root / 'manifest.json') != manifest:
        raise AuditError('Root and input manifest copies differ')
    actual = {p.relative_to(root).as_posix() for p in (root / 'input').rglob('*') if p.is_file()
              and p != root / 'input/manifest.json'}
    if actual != set(expected):
        raise AuditError('Input file inventory changed since preparation')
    for rel, record in expected.items():
        path = safe_path(root, rel)
        if not path.is_file() or digest(path) != record['sha256']:
            raise AuditError(f'Input hash mismatch: {rel}')
    return manifest


def validate_lean_version(value):
    if not isinstance(value, str) or not re.fullmatch(r'4\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)', value):
        raise AuditError('Lean version must be a stable Lean 4 release such as 4.24.0')
    return value


def required_lean_version(root):
    policy = root / 'input/audit-policy.json'
    return validate_lean_version(read_json(policy).get('lean_version', VERSION) if policy.is_file() else VERSION)


def module_path(module):
    if not re.fullmatch(MODULE_NAME, module):
        raise AuditError('Module must use plain dotted identifiers')
    return 'models/' + module.replace('.', '/') + '.lean'


def model_inventory(root):
    directory = root / 'models'
    if directory.is_symlink():
        raise AuditError('The models directory cannot be a symlink')
    modules = {}
    for path in sorted(directory.rglob('*')):
        if path.is_symlink():
            if not path.resolve().is_relative_to(directory.resolve()):
                raise AuditError(f'Model symlink escapes models directory: {path.name}')
            if path.is_dir():
                raise AuditError('Model directory symlinks are not supported; use ordinary directories')
        if path.suffix in {'.olean', '.ilean', '.so', '.o', '.a', '.bc'}:
            raise AuditError(f'Unreviewed compiled model artifact: {path.name}')
        if path.suffix != '.lean' or not path.is_file():
            continue
        module = '.'.join(path.relative_to(directory).with_suffix('').parts)
        if not re.fullmatch(MODULE_NAME, module) or path.relative_to(root).as_posix() != module_path(module):
            raise AuditError('Model paths must use plain dotted module identifiers')
        if module.split('.')[0] in {'Init', 'Std', 'Lean', 'Lake'}:
            raise AuditError('Local models cannot shadow toolchain module names')
        modules[module] = path
    return modules


def prepare(args):
    result = _prepare(args)
    root = Path(result['workspace'])
    journal.append(root, phase='intake', status='completed', title='Workspace prepared',
        description='The preparation helper preserved inputs and initialized the workspace. This event does not record agent analysis or semantic review.',
        outputs=[p for p in ('run.json', 'manifest.json', 'claims.json') if (root / p).is_file()],
        command=getattr(args, '_journal_command', None), result='Workspace preparation returned successfully.')
    return result


def _prepare(args):
    lean_version = validate_lean_version(getattr(args, 'lean_version', VERSION))
    proposed_temp = Path(args.temp_root or Path.cwd() / 'tmp').resolve()
    if any(Path(p).is_dir() and proposed_temp.is_relative_to(Path(p).resolve()) for p in args.sources):
        raise AuditError('Temporary root must be outside supplied source directories')
    text_extensions = {'.md', '.markdown', '.txt', '.text', '.csv'}
    brief_arg = getattr(args, 'brief', None)
    candidates = [Path(args.report)] + ([Path(brief_arg)] if brief_arg else [])
    for supplied in args.sources:
        p = Path(supplied)
        candidates.extend(x for x in p.rglob('*') if x.is_file()) if p.is_dir() else candidates.append(p)
    if getattr(args, 'indexed', False) or any(p.suffix.lower() not in text_extensions for p in candidates):
        return corpus.prepare(args)
    brief = Path(brief_arg).resolve() if brief_arg else None
    report = Path(args.report).resolve()
    if (brief is not None and not brief.is_file()) or not report.is_file():
        raise AuditError('Report and any supplied brief must be existing files')
    sources = [Path(p).resolve() for p in args.sources]
    if any(not p.exists() for p in sources):
        raise AuditError('A supplied source does not exist')
    temp_root = Path(args.temp_root) if args.temp_root else Path.cwd() / 'tmp'
    temp_root.mkdir(parents=True, exist_ok=True)
    root = Path(tempfile.mkdtemp(prefix='claim-audit-', dir=temp_root))
    (root / 'input/sources').mkdir(parents=True)
    (root / 'models').mkdir()
    shutil.copyfile(report, root / 'input/report.md')
    originals = {'input/report.md': str(report)}
    if brief is not None:
        shutil.copyfile(brief, root / 'input/brief.md')
        originals['input/brief.md'] = str(brief)
    used = set()
    for index, source in enumerate(sources, 1):
        files = sorted(p for p in source.rglob('*') if p.is_file()) if source.is_dir() else [source]
        for path in files:
            rel = path.relative_to(source).as_posix() if source.is_dir() else path.name
            candidate = rel
            suffix = 1
            while any(candidate == prior or candidate.startswith(prior + '/') or prior.startswith(candidate + '/') for prior in used):
                candidate = f'source-{index}-{suffix}/{rel}'
                suffix += 1
            used.add(candidate)
            destination = root / 'input/sources' / candidate
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, destination)
            originals[destination.relative_to(root).as_posix()] = str(path)
    source_ledger = {}
    for rel in originals:
        try:
            source_ledger[rel] = paragraphs((root / rel).read_text(encoding='utf-8'))
        except UnicodeError as exc:
            raise AuditError(f'Source must be extracted UTF-8 text: {rel}') from exc
    write_json(root / 'input/source-ledger.json', source_ledger)
    ledger_rows = []
    for rel, anchors in source_ledger.items():
        original = (root / rel).read_text(encoding='utf-8')
        cursor = 0
        for anchor, quote in anchors.items():
            offset = original.find(quote, cursor)
            if offset < 0: offset = original.find(quote)
            cursor = max(cursor, offset + len(quote))
            ledger_rows.append({'path': rel, 'anchor': anchor, 'quote': quote,
                'start_line': original.count('\n', 0, offset) + 1,
                'end_line': original.count('\n', 0, offset + len(quote)) + 1})
    (root / 'source-ledger.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in ledger_rows), encoding='utf-8')
    write_json(root / 'input/report-ledger.json', paragraphs((root / 'input/report.md').read_text(encoding='utf-8')))
    write_json(root / 'input/audit-policy.json', {'contract_version': 2,
        'require_claim_traces': bool(getattr(args, 'require_claim_traces', False)),
        'brief_origin': 'provided' if brief else 'inferred', 'lean_version': lean_version,
        'default_mandate': 'Audit every material report claim and its justification against the supplied sources; derive and disclose criteria without assuming the claim.'})
    contracts.initialize(root)
    files = {p.relative_to(root).as_posix(): {'sha256': digest(p), 'bytes': p.stat().st_size,
             'original_path': originals.get(p.relative_to(root).as_posix())}
             for p in sorted((root / 'input').rglob('*')) if p.is_file()}
    write_json(root / 'input/manifest.json', {'algorithm': 'sha256', 'files': files})
    write_json(root / 'manifest.json', {'algorithm': 'sha256', 'files': files})
    write_json(root / 'run.json', {'created_at': now(), 'workspace': str(root),
               'lean_version': lean_version, 'purpose': 'Audit the supplied report against supplied sources',
               'limitations': CAVEAT})
    return {'workspace': str(root), 'source_ledger': 'input/source-ledger.json', 'report_ledger': 'input/report-ledger.json'}


def nonempty_string(value, label):
    if not isinstance(value, str) or not value.strip():
        raise AuditError(f'{label} must be a nonempty string')


def findings(root):
    verify_manifest(root)
    data = read_json(root / 'findings.json')
    strict = (root / 'input/audit-policy.json').is_file()
    if strict and read_json(root / 'input/audit-policy.json').get('contract_version') != 2:
        raise AuditError('Unsupported audit contract version')
    if not isinstance(data, list) or (not data and not strict):
        raise AuditError('findings.json must be an array (legacy audits require at least one finding)')
    indexed = (root / 'input/index.sqlite3').is_file()
    sources = None if indexed else read_json(root / 'input/source-ledger.json')
    report = read_json(root / 'input/report-ledger.json')
    seen = set()
    for finding in data:
        if not isinstance(finding, dict) or not REQUIRED <= finding.keys():
            raise AuditError(f'Finding missing required fields: {REQUIRED - finding.keys() if isinstance(finding, dict) else REQUIRED}')
        ident = finding['claim_id']
        for field in ('claim_id', 'report_quote', 'report_anchor', 'question', 'recommendation'):
            nonempty_string(finding[field], field)
        if ident in seen:
            raise AuditError(f'Duplicate claim_id: {ident}')
        seen.add(ident)
        if finding['report_quote'] not in report.get(finding['report_anchor'], ''):
            raise AuditError(f'{ident}: report quote does not match its anchored paragraph')
        for field, choices in STATES.items():
            if finding[field] not in choices:
                raise AuditError(f'{ident}: invalid {field}')
        for field in ('evidence', 'rules', 'assumptions', 'reasoning', 'proofs', 'limits'):
            if not isinstance(finding[field], list) or (not finding[field] and field not in ({'assumptions', 'proofs', 'evidence'} if strict else {'assumptions', 'proofs'})):
                raise AuditError(f'{ident}: {field} must be a list and cannot be empty here')
        for field in ('rules', 'assumptions', 'reasoning', 'limits'):
            for item in finding[field]:
                nonempty_string(item, f'{ident}.{field}')
        for evidence in finding['evidence']:
            if not isinstance(evidence, dict) or not {'path', 'anchor', 'quote'} <= evidence.keys():
                raise AuditError(f'{ident}: malformed evidence')
            for field in ('path', 'anchor', 'quote'):
                nonempty_string(evidence[field], f'{ident}.evidence.{field}')
            if strict and not evidence['path'].startswith('input/sources/'):
                raise AuditError(f'{ident}: independent evidence must come from sources, not the report or brief')
            segment = corpus.passage(root, evidence['path'], evidence['anchor']) if indexed else None
            paragraph = (segment or {}).get('quote', '') if indexed else sources.get(evidence['path'], {}).get(evidence['anchor'], '')
            if evidence['quote'] not in paragraph:
                raise AuditError(f'{ident}: evidence quote does not match its anchored source paragraph')
        relations = set()
        for proof in finding['proofs']:
            if not isinstance(proof, dict) or not {'module', 'theorem', 'relation', 'target'} <= proof.keys():
                raise AuditError(f'{ident}: malformed proof reference')
            for field in ('module', 'theorem', 'relation', 'target'):
                nonempty_string(proof[field], f'{ident}.proof.{field}')
            if not re.fullmatch(MODULE_NAME, proof['module']):
                raise AuditError(f'{ident}: module must use plain dotted identifiers')
            if not re.fullmatch(r'[A-Za-z_][A-Za-z0-9_\'.]*', proof['theorem']):
                raise AuditError(f'{ident}: invalid theorem name')
            if proof['relation'] not in {'supports', 'refutes', 'auxiliary'}:
                raise AuditError(f'{ident}: invalid proof relation')
            target = lean_code(proof['target'], reject_comments=True)
            if '\n' in proof['target'] or '#' in target:
                raise AuditError(f'{ident}: target must be a single proposition without commands/comments')
            if re.search(r'\b(theorem|lemma|def|example|import|axiom|by|where|end|namespace|section|set_option|attribute|elab|macro|initialize)\b|:=|[;`]', target):
                raise AuditError(f'{ident}: target contains unsupported command or tactic syntax')
            stack = []
            pairs = {')': '(', ']': '[', '}': '{'}
            for char in target:
                if char in '([{': stack.append(char)
                elif char in pairs and (not stack or stack.pop() != pairs[char]):
                    raise AuditError(f'{ident}: unbalanced target delimiters')
            if stack: raise AuditError(f'{ident}: unbalanced target delimiters')
            relations.add(proof['relation'])
        if finding['formal_status'] in {'not_attempted', 'blocked'} and finding['proofs']:
            raise AuditError(f'{ident}: not_attempted/blocked findings cannot contain proof references')
        expected_semantic = {'proved': 'supported', 'refuted': 'refuted'}.get(finding['formal_status'])
        if expected_semantic and finding['semantic_state'] != expected_semantic:
            raise AuditError(f'{ident}: formal and semantic statuses are inconsistent')
        needed = {'proved': 'supports', 'refuted': 'refutes', 'auxiliary': 'auxiliary'}.get(finding['formal_status'])
        if needed and needed not in relations:
            raise AuditError(f'{ident}: formal status requires a corresponding checked theorem reference')
    if indexed:
        corpus.assert_reviewable(root, data)
    if strict:
        try:
            contracts.validate(root, data)
        except ValueError as exc:
            raise AuditError(str(exc)) from exc
    return data


def lean_code(text, *, reject_comments=False, mask_strings=True):
    """Mask literal/comment contents while preserving positions and newlines.

    This lexical gate is defense in depth for reviewed source, not a Lean parser.
    Interpolated strings are rejected because their embedded terms need parsing.
    """
    out, i, depth = [], 0, 0
    def masked(value):
        return ''.join('\n' if c == '\n' else ' ' for c in value)
    while i < len(text):
        if depth:
            if text.startswith('/-', i):
                depth += 1; out.append('  '); i += 2
            elif text.startswith('-/', i):
                depth -= 1; out.append('  '); i += 2
            else:
                out.append('\n' if text[i] == '\n' else ' '); i += 1
            continue
        if text.startswith('/-', i) or text.startswith('--', i):
            if reject_comments:
                raise AuditError('Target must be a single proposition without commands/comments')
            if text.startswith('/-', i):
                depth = 1; out.append('  '); i += 2
            else:
                end = text.find('\n', i)
                if end < 0: end = len(text)
                out.append(masked(text[i:end])); i = end
            continue
        raw = re.match(r'r(#+)?"', text[i:]) if i == 0 or not (text[i-1].isalnum() or text[i-1] in "_'") else None
        if text[i] == '"' or raw:
            if i and text[i-1] == '!':
                raise AuditError('Interpolated Lean strings require unsupported embedded-term inspection')
            start = i
            if raw:
                closing = '"' + (raw.group(1) or '')
                end = text.find(closing, i + len(raw.group()))
                if end < 0: raise AuditError('Unclosed Lean string')
                i = end + len(closing)
            else:
                i += 1
                while i < len(text) and text[i] != '"':
                    i += 2 if text[i] == '\\' else 1
                if i >= len(text): raise AuditError('Unclosed Lean string')
                i += 1
            value = text[start:i]
            out.append(masked(value) if mask_strings else value)
            continue
        # Apostrophes may also occur in identifiers; only mask complete character literals.
        char = re.match(r"'(?:\\(?:u[0-9A-Fa-f]{4}|x[0-9A-Fa-f]{2}|.)|[^'\\\n])'", text[i:]) if text[i] == "'" else None
        if char and (i == 0 or not (text[i-1].isalnum() or text[i-1] in "_'")):
            value = char.group(); out.append(masked(value) if mask_strings else value); i += len(value)
            continue
        out.append(text[i]); i += 1
    if depth: raise AuditError('Unclosed Lean comment')
    return ''.join(out)


def strip_comments(text):
    return lean_code(text, mask_strings=False)


def inspect_model(path, local_modules=()):
    source = lean_code(path.read_text(encoding='utf-8'))
    forbidden = r'\b(sorry|admit|axiom|axioms|native_decide|unsafe|meta|run_tac|elab|elab_rules|macro|macro_rules|syntax|initialize|builtin_initialize|implemented_by|extern|opaque)\b|#|\bset_option\b'
    if re.search(forbidden, source):
        raise AuditError(f'Forbidden or unauditable Lean construct in {path.name}')
    # A Lean import command takes one module identifier; comments and whitespace
    # may separate it from the keyword. Inspect tokens rather than physical lines.
    tokens = re.findall(MODULE_NAME + r'|[^\s]', source)
    for index, token in enumerate(tokens):
        if token != 'import':
            continue
        next_index = index + 1
        if next_index < len(tokens) and tokens[next_index] == 'all':
            next_index += 1
        module = tokens[next_index] if next_index < len(tokens) else ''
        if not re.fullmatch(MODULE_NAME, module):
            raise AuditError('Import must name an allowed module')
        if module not in local_modules and not re.fullmatch(r'(Init|Std)(\.[A-Za-z_][A-Za-z0-9_]*)*', module):
            raise AuditError(f'Only Init/Std or reviewed local model imports are permitted: {module}')
    declarations, namespaces = [], []
    for line in source.splitlines():
        ns = re.match(r'\s*namespace\s+([\w.]+)\s*$', line)
        end = re.match(r'\s*end(?:\s+([\w.]+))?\s*$', line)
        dec = re.match(r"\s*(?:(?:private|protected|noncomputable)\s+)*(theorem|lemma)\s+([\w.']+)", line)
        if ns:
            namespaces.append(ns.group(1))
        elif end and namespaces and (end.group(1) is None or end.group(1) == namespaces[-1]):
            namespaces.pop()
        elif dec:
            if re.match(r'\s*private\b', line):
                raise AuditError('Private theorem declarations cannot be audited by external name')
            declarations.append('.'.join(namespaces + [dec.group(2)]))
    if len(re.findall(r"\b(?:theorem|lemma)\s+[\w.']+", source)) != len(declarations):
        raise AuditError('Each theorem must start on its own line with a conventional declaration')
    return declarations


def snapshot(root):
    paths = [root / 'findings.json', root / 'input/manifest.json'] + list(model_inventory(root).values())
    paths += [root / name for name in ('extraction-review.json', 'coverage-acknowledgement.json', 'revision-review.json', 'invalidation.json', 'manual-transcriptions.jsonl')]
    paths += [root / 'extraction-lock.json']
    if (root / 'input/audit-policy.json').is_file():
        paths += [root / name for name in ('claims.json', 'review-plan.md', 'model-notes.md', 'semantic-review.md', 'independent-review.md')]
    return {p.relative_to(root).as_posix(): digest(p) for p in paths if p.is_file()}


def execute(command, root, logfile, timeout, env):
    started = time.monotonic()
    invocation = '$ ' + ' '.join(map(str, command)) + '\n'
    try:
        result = subprocess.run(command, cwd=root, env=env, text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, timeout=timeout)
        logfile.write_text(invocation + result.stdout + f'\n[exit_code={result.returncode}; elapsed_seconds={time.monotonic()-started:.3f}]\n', encoding='utf-8')
    except subprocess.TimeoutExpired as exc:
        output = exc.stdout or b''
        if isinstance(output, bytes): output = output.decode('utf-8', errors='replace')
        logfile.write_text(invocation + output + f'\nTIMEOUT [elapsed_seconds={time.monotonic()-started:.3f}]\n', encoding='utf-8')
        raise AuditError(f'Lean command timed out; see {logfile.name}') from exc
    except OSError as exc:
        logfile.write_text(invocation + str(exc) + '\n[execution_unavailable]\n', encoding='utf-8')
        raise AuditError(f'Cannot execute Lean tool: {exc}') from exc
    if result.returncode:
        raise AuditError(f'Lean command failed ({result.returncode}); see {logfile.name}')
    return result.stdout


def check(args):
    root = Path(args.workspace).resolve()
    if not root.is_dir(): raise AuditError('Workspace does not exist')
    # Retain previous executed results before replacing the current check.
    # Their source fingerprints remain in proof-results.json; do not attach
    # possibly edited current models to an older attempt.
    if (root / 'proof-results.json').exists():
        history = root / 'attempts'
        history.mkdir(exist_ok=True)
        number = 1
        while (history / f'{number:04d}').exists(): number += 1
        previous = history / f'{number:04d}'
        previous.mkdir()
        for name in ('proof-results.json', 'logs', 'checks', 'environment.lock'):
            path = root / name
            if path.is_dir(): shutil.copytree(path, previous / name)
            elif path.is_file(): shutil.copyfile(path, previous / name)
    logs = root / 'logs'
    if logs.exists(): shutil.rmtree(logs)
    logs.mkdir()
    if (root / 'checks').exists(): shutil.rmtree(root / 'checks')
    (root / 'environment.lock').unlink(missing_ok=True)
    results = {'checked_at': now(), 'status': 'failed', 'lean_version_required': None,
               'independent_checker': {'status': 'not_run', 'reason': 'No external checker is configured; no independent-kernel assurance is claimed.'},
               'targets': [], 'limitations': CAVEAT}
    if getattr(args, 'checker', None):
        results['independent_checker'] = {'status': 'not_run', 'path': str(Path(args.checker).resolve()),
            'reason': 'Requested replay has not been reached; earlier gates and model checks must succeed first.'}
    write_json(root / 'proof-results.json', results)
    try:
        verify_manifest(root)
        required_version = required_lean_version(root)
        results['lean_version_required'] = required_version
        data = findings(root)
        results['claim_trace_contract'] = journal.validate_claim_traces(root, data, getattr(args, 'journal_root', None))
        results['audit_contract'] = (contracts.validate(root, data) if (root / 'input/audit-policy.json').is_file() else
            {'version': 1, 'coverage': 'legacy_unreconciled', 'limitation': 'This older bundle has no enforced claim register or structured argument audit.'})
        if (root / 'lakefile.lean').exists():
            raise AuditError('Unreviewed lakefile.lean overrides the controlled configuration')
        models = model_inventory(root)
        declarations = {module: inspect_model(path, models) for module, path in models.items()}
        proofs = [p for f in data for p in f['proofs']]
        for proof in proofs:
            if proof['module'] not in declarations or proof['theorem'] not in declarations[proof['module']]:
                raise AuditError(f'Missing declared theorem target: {proof["module"]}.{proof["theorem"]}')
        results['input_hashes'] = snapshot(root)
        if not models and not proofs:
            results.update(status='not_run', execution_status='not_run',
                reason='No formal models or proof references; documentary audit only.')
            write_json(root / 'environment.lock', {'lean_version_required': required_version, 'execution_status': 'not_run',
                'module_policy': MODULE_POLICY, 'reason': results['reason']})
            results['artifact_hashes'] = artifact_hashes(root)
            write_json(root / 'proof-results.json', results)
            return results
        lean = Path(args.lean).resolve()
        lake = lean.with_name('lake')
        env = dict(os.environ, PATH=str(lean.parent) + os.pathsep + os.environ.get('PATH', ''))
        # Do not inherit arbitrary user Lean search paths or module directories.
        for key in ('LEAN_PATH', 'LEAN_SRC_PATH', 'LEAN_SYSROOT', 'LAKE_HOME'):
            env.pop(key, None)
        version = execute([str(lean), '--version'], root, logs / 'lean-version.log', args.timeout, env)
        results['lean_version_observed'] = version.strip()
        observed = re.search(r'\bversion ([^\s,;()]+)', version)
        if observed is None or observed.group(1) != required_version:
            results['execution_status'] = 'version_mismatch'
            write_json(root / 'environment.lock', {'lean_version_required': required_version,
                'lean_version_observed': version.strip(), 'execution_status': 'version_mismatch',
                'module_policy': MODULE_POLICY})
            raise AuditError(f'Lean {required_version} required; observed {version.strip()}')
        results['execution_status'] = 'executed'
        write_json(root / 'environment.lock', {'lean_version_required': required_version, 'lean_version_observed': version.strip(),
            'execution_status': 'executed', 'module_policy': MODULE_POLICY,
            'executables': {str(p): digest(p) for p in (lean, lake)}})
        (root / 'lean-toolchain').write_text(f'leanprover/lean4:v{required_version}\n')
        config = 'name = "claim_audit"\nversion = "0.1.0"\n'
        # A single controlled library owns every reviewed module, including helpers.
        # Explicit roots/globs avoid overlapping-library resolution for nested modules.
        config += '\n[[lean_lib]]\nname = "AuditReviewedSources"\nsrcDir = "models"\n'
        config += 'roots = ' + json.dumps(list(declarations)) + '\n'
        config += 'globs = ' + json.dumps(list(declarations)) + '\n'
        (root / 'lakefile.toml').write_text(config, encoding='utf-8')
        # Rebuild in a clean controlled build tree, without cached unreviewed objects.
        if (root / '.lake').exists(): shutil.rmtree(root / '.lake')
        if (root / 'lake-manifest.json').exists(): (root / 'lake-manifest.json').unlink()
        if models:
            execute([str(lake), 'build', 'AuditReviewedSources'], root, logs / 'lake-build.log', args.timeout, env)
        checks = root / 'checks'; checks.mkdir(exist_ok=True)
        # Every declared theorem is audited even if no finding references it.
        requests = [(module, theorem, None) for module, names in declarations.items() for theorem in names]
        requests += [(p['module'], p['theorem'], p['target']) for p in proofs]
        for index, (module, theorem, target) in enumerate(requests, 1):
            checkfile = checks / f'Target{index:03d}.lean'
            content = f'import {module}\n#check @{theorem}\n#print axioms {theorem}\n'
            if target: content += f'example : ({target}) := {theorem}\n'
            checkfile.write_text(content, encoding='utf-8')
            log = logs / f'target-{index:03d}.log'
            output = execute([str(lake), 'env', 'lean', str(checkfile.relative_to(root))], root, log, args.timeout, env)
            axiom_lists = re.findall(r'depends on axioms:\s*\[([^\]]*)\]', output, re.S)
            axioms = sorted({a.strip() for group in axiom_lists for a in group.split(',') if a.strip()})
            if set(axioms) - {'propext', 'Classical.choice', 'Quot.sound'}:
                raise AuditError(f'Unapproved axioms in {theorem}: {axioms}')
            if not axiom_lists and 'does not depend on any axioms' not in output:
                raise AuditError(f'No axiom inspection result for {theorem}')
            results['targets'].append({'module': module, 'theorem': theorem, 'target': target,
                'status': 'passed', 'axioms': axioms, 'log': log.relative_to(root).as_posix(),
                'check_file': checkfile.relative_to(root).as_posix(), 'model_sha256': digest(models[module])})
        if getattr(args, 'checker', None):
            checker = Path(args.checker).resolve()
            replay_logs = []
            replay = {'status': 'running', 'path': str(checker), 'logs': replay_logs,
                'method': 'fresh environment replay through the same Lean kernel; not an independent kernel implementation'}
            results['independent_checker'] = replay
            try:
                replay['sha256'] = digest(checker)
                for module in declarations:
                    log = logs / f'checker-{module}.log'
                    replay_logs.append(log.relative_to(root).as_posix())
                    execute([str(lake), 'env', str(checker), '--fresh', module], root, log, getattr(args, 'checker_timeout', 300), env)
                replay['status'] = 'passed'
            except (AuditError, OSError) as exc:
                replay.update(status='timeout' if 'timed out' in str(exc) else 'failed', error=str(exc))
                raise
        results['status'] = 'passed'
    except (AuditError, OSError, ValueError) as exc:
        results['error'] = str(exc)
        results.setdefault('execution_status', 'unavailable' if 'Cannot execute' in str(exc) else 'failed')
        if not (root / 'environment.lock').is_file():
            write_json(root / 'environment.lock', {'lean_version_required': results['lean_version_required'],
                'execution_status': results['execution_status'],
                'module_policy': MODULE_POLICY, 'error': str(exc)})
        results['artifact_hashes'] = artifact_hashes(root)
        write_json(root / 'proof-results.json', results)
        raise AuditError(str(exc)) from exc
    results['artifact_hashes'] = artifact_hashes(root)
    write_json(root / 'proof-results.json', results)
    return results


def artifact_hashes(root):
    paths = [root / 'environment.lock', root / 'lakefile.toml', root / 'lean-toolchain', root / 'source-ledger.jsonl']
    paths += sorted((root / 'logs').glob('*')) + sorted((root / 'checks').glob('*'))
    return {p.relative_to(root).as_posix(): digest(p) for p in paths if p.is_file()}


def verified(root):
    data = findings(root)
    results = read_json(root / 'proof-results.json')
    if results.get('status') not in {'passed', 'not_run'} or results.get('input_hashes') != snapshot(root):
        raise AuditError('No successful proof check for the current findings, models, and input manifest')
    if results.get('artifact_hashes') != artifact_hashes(root):
        raise AuditError('Verification logs, checks, or environment artifacts changed since checking')
    if results['status'] == 'not_run' and (any(f['proofs'] for f in data) or model_inventory(root)):
        raise AuditError('Formal artifacts cannot be delivered as a documentary-only audit')
    for finding in data:
        for proof in finding['proofs']:
            if not any(all(t.get(k) == proof[k] for k in ('module', 'theorem', 'target')) and t.get('status') == 'passed'
                       for t in results['targets']):
                raise AuditError(f'Missing checked proposition: {proof["theorem"]}')
    return data, results


def render(args):
    root = Path(args.workspace).resolve()
    data, results = verified(root)
    traces = journal.validate_claim_traces(root, data, getattr(args, 'journal_root', None))
    lines = ['# Evidence-backed claim audit', '', CAVEAT, '',
             ('Technical verification: executed successfully using ' + results['lean_version_observed']
              if results['status'] == 'passed' else 'Formal verification: not run. Documentary audit only.'), '',
             '[Proof results](proof-results.json) · [Input manifest](input/manifest.json)', '']
    lines += ['Individual trace profile: ' + traces['profile'] + '.', '']
    coverage = ['# Claim coverage', '']
    if (root / 'input/audit-policy.json').is_file():
        contract_lines = contracts.render_coverage(root, data)
        lines += contract_lines
        coverage += contract_lines
    else:
        legacy = 'Legacy audit: registered-claim coverage and structured report-argument checks were not enforced for this bundle.'
        lines += [legacy, '']
        coverage += [legacy, '']
    if (root / 'semantic-review.md').is_file():
        lines += ['[Semantic correspondence review](semantic-review.md)', '']
    else:
        lines += ['Semantic correspondence review: pending; technical success alone does not validate source fidelity.', '']
    if (root / 'input/index.sqlite3').is_file():
        documents = corpus.inventory(root)
        gaps = [d for d in documents if d['status'] != 'ready']
        lines += [f'Extraction inventory: {len(documents)} documents; {len(gaps)} pending, partial or blocked. See [ingestion details](ingestion.json) and [coverage](coverage.md).', '']
        coverage += ['', '## Document extraction coverage', '', '| Document | Source | State |', '|---|---|---|']
        coverage += [f'| {d["id"]} | {d["logical"]} | {d["status"]} |' for d in documents]
        ack = read_json(root / 'coverage-acknowledgement.json') if (root / 'coverage-acknowledgement.json').exists() else {}
        for d in gaps:
            coverage += ['', f'### {d["id"]}: {d["status"]}', '', d['warnings'], '']
            for item in ack.get('documents', []):
                if item.get('document_id') == d['id']:
                    coverage += ['Reason: ' + item['reason'], '', 'Impact: ' + item['impact'], '']
    coverage += ['', '## Claim outcomes', '', '| Claim | Semantic state | Argument status | Formal status |', '|---|---|---|---|']
    for f in data:
        if 'executive_summary' in f:
            summary = f['executive_summary']
            lines += [f'## {f["claim_id"]}: Executive summary', '', summary['conclusion'], '', 'How verified: ' + summary['how_verified'], '', 'Limits: ' + summary['limits'], '']
        lines += [f'## {f["claim_id"]}', '', '### Exact report claim', '',
                  f'`input/report.md#{f["report_anchor"]}`', '', '> ' + f['report_quote'].replace('\n', '\n> '), '',
                  '### Verification question', '', f['question'], '', '### Source evidence', '']
        if not f['evidence']:
            lines += ['No source evidence attached; see the bounded search record and its limits.', '']
        for e in f['evidence']:
            lines += [f'- [{e["path"]}]({e["path"]}) — `{e["anchor"]}`', '', '> ' + e['quote'].replace('\n', '\n> '), '']
            if (root / 'input/index.sqlite3').is_file():
                seg = corpus.passage(root, e['path'], e['anchor'])
                locator = seg['locator']
                compact = {k:v for k,v in locator.items() if k != 'words'}
                lines += [f'Original: [{locator["original"]}]({locator["original"]}); extraction: {seg["method"]}.',
                          'Coordinates: `' + json.dumps(compact, ensure_ascii=False) + '`.', '']
                if seg['uncertainty']:
                    lines += ['Extraction uncertainty: ' + '; '.join(seg['uncertainty']), '']
        if (root / 'input/audit-policy.json').is_file():
            lines += contracts.render_finding(f)
        for key in ('rules', 'assumptions', 'reasoning', 'limits'):
            lines += ['### ' + key.capitalize(), '']
            lines += ['- ' + item for item in f[key]] if f[key] else ['None stated.']
            lines += ['']
        lines += ['### Result', '', f'Semantic state: **{f["semantic_state"]}**; argument status: **{f["argument_status"]}**; formal status: **{f["formal_status"]}**.', '', '### Formal evidence', '']
        if not f['proofs']: lines += ['No formal proof was checked for this finding; see its formalization rationale where provided.', '']
        for p in f['proofs']:
            target = next(t for t in results['targets'] if all(t.get(k) == p[k] for k in ('module', 'theorem', 'target')))
            lines += [f'- `{p["theorem"]}` in module `{p["module"]}` ({p["relation"]}): `{p["target"]}`.',
                      f'  [Model]({module_path(p["module"])}) · [Executed check]({target["check_file"]}) · [Actual proof log]({target["log"]})', '']
        lines += ['### Recommendation', '', f['recommendation'], '']
        coverage += [f'| {f["claim_id"]} | {f["semantic_state"]} | {f["argument_status"]} | {f["formal_status"]} |']
    coverage += ['', 'Coverage enumerates submitted findings; it does not establish that every report claim was identified.', '']
    (root / 'audit-report.md').write_text('\n'.join(lines), encoding='utf-8')
    (root / 'coverage.md').write_text('\n'.join(coverage), encoding='utf-8')
    return {'report': str(root / 'audit-report.md'), 'coverage': str(root / 'coverage.md')}


def export(args):
    root = Path(args.workspace).resolve()
    if (root / 'input/audit-policy.json').is_file():
        required = ['review-plan.md', 'semantic-review.md']
        if model_inventory(root): required.append('model-notes.md')
        for name in required:
            if not (root / name).is_file() or not (root / name).read_text(encoding='utf-8').strip():
                raise AuditError(f'Export requires completed {name}; record limitations honestly')
    render(args)
    destination = Path(args.destination).resolve()
    if destination == root or destination.is_relative_to(root) or root.is_relative_to(destination):
        raise AuditError('Export destination must be separate from workspace')
    if destination.exists():
        raise AuditError('Export destination already exists; choose a new path')
    shutil.copytree(root, destination, ignore=shutil.ignore_patterns('.lake', '__pycache__', 'export-manifest.json'))
    files = {p.relative_to(destination).as_posix(): digest(p) for p in sorted(destination.rglob('*')) if p.is_file()}
    write_json(destination / 'export-manifest.json', {'exported_at': now(), 'algorithm': 'sha256', 'files': files})
    return {'destination': str(destination), 'files': len(files)}


def resume(args):
    return corpus.resume(args.workspace, max_documents=args.max_documents, max_seconds=args.max_seconds,
                         retry=args.retry, max_pages=args.max_pages, recover=args.recover)


def search(args):
    return corpus.search(args.workspace, args.query, args.limit, args.offset)


def show(args):
    corpus.verify(Path(args.workspace).resolve())
    value = corpus.passage(args.workspace, args.path, args.anchor)
    if value is None: raise AuditError('Passage not found')
    return value


def inventory(args):
    corpus.verify(Path(args.workspace).resolve())
    return {'documents': corpus.inventory(args.workspace)}


def refresh(args):
    return corpus.refresh(args.workspace, args.document_id, args.replacement, temp_root=args.temp_root)


def transcribe(args):
    return corrections.transcribe(args.workspace, args.path, args.anchor, args.text_file, args.reviewer, args.reason)


def import_extraction(args):
    import agent_extraction
    return agent_extraction.import_extraction(args.workspace, args.document_id, args.bundle)


def doctor(args):
    result = {'python': sys.version, 'sqlite': corpus.sqlite3.sqlite_version,
              'stdlib_only_runtime': True, 'lean_version_default': VERSION,
              'lean_version_policy': 'Each audit pins a stable Lean 4 version in its immutable input policy; older bundles default to ' + VERSION,
              'module_policy': MODULE_POLICY, 'tools': {}}
    try:
        with corpus.sqlite3.connect(':memory:') as probe:
            probe.execute('CREATE VIRTUAL TABLE probe USING fts5(text)')
        probe.close(); result['sqlite_fts5'] = True
    except corpus.sqlite3.Error:
        result['sqlite_fts5'] = False
    for name in ('lean', 'lake', 'pdfinfo', 'pdftotext', 'pdfimages', 'pdftoppm', 'tesseract', 'lean4checker'):
        path = (args.lean if name == 'lean' else str(Path(args.lean).with_name('lake')) if name == 'lake' and args.lean else shutil.which(name))
        if not path:
            result['tools'][name] = {'available': False}; continue
        if name == 'lean4checker':
            result['tools'][name] = {'available': Path(path).is_file(), 'path': path,
                                    'note': 'No version flag is assumed; use pinned build metadata.'}
            continue
        flag = '--version' if name in {'lean', 'lake', 'tesseract', 'lean4checker'} else '-v'
        try:
            run = subprocess.run([path, flag], capture_output=True, text=True, timeout=15)
            result['tools'][name] = {'available': run.returncode == 0, 'path': path,
                'version_output': (run.stdout + run.stderr).strip().splitlines()[:2]}
        except (OSError, subprocess.TimeoutExpired) as exc:
            result['tools'][name] = {'available': False, 'error': str(exc)}
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    prep = commands.add_parser('prepare')
    prep.add_argument('--brief', help='Optional review instructions; otherwise derive criteria from the report and sources'); prep.add_argument('--report', required=True)
    prep.add_argument('--sources', required=True, nargs='+'); prep.add_argument('--temp-root', default=None)
    prep.add_argument('--require-claim-traces', action='store_true', help='Require individually recorded claim steps and executive summaries')
    prep.add_argument('--indexed', action='store_true', help='Use coordinate-preserving adapters and the disk-backed corpus index')
    prep.add_argument('--lean-version', default=VERSION, help='Stable Lean 4 release pinned into this audit input policy')
    prep.add_argument('--ocr-language', default='eng')
    prep.add_argument('--extract-timeout', type=float, default=60)
    prep.add_argument('--max-pages', type=int)
    prep.add_argument('--max-documents', type=int)
    prep.add_argument('--max-seconds', type=float)
    sub = commands.add_parser('resume'); sub.add_argument('--workspace', required=True)
    sub.add_argument('--max-documents', type=int); sub.add_argument('--max-seconds', type=float)
    sub.add_argument('--retry', action='store_true'); sub.add_argument('--max-pages', type=int)
    sub.add_argument('--recover', action='store_true', help='Rebuild interrupted derived state from verified original snapshots; invalidate prior results')
    sub = commands.add_parser('search'); sub.add_argument('--workspace', required=True); sub.add_argument('--query', required=True)
    sub.add_argument('--limit', type=int, default=20); sub.add_argument('--offset', type=int, default=0)
    sub = commands.add_parser('show'); sub.add_argument('--workspace', required=True); sub.add_argument('--path', required=True); sub.add_argument('--anchor', required=True)
    sub = commands.add_parser('refresh'); sub.add_argument('--workspace', required=True); sub.add_argument('--document-id', required=True)
    sub.add_argument('--replacement', required=True); sub.add_argument('--temp-root')
    sub = commands.add_parser('inventory'); sub.add_argument('--workspace', required=True)
    sub = commands.add_parser('transcribe'); sub.add_argument('--workspace', required=True)
    sub.add_argument('--path', required=True); sub.add_argument('--anchor', required=True)
    sub.add_argument('--text-file', required=True); sub.add_argument('--reviewer', required=True); sub.add_argument('--reason', required=True)
    sub = commands.add_parser('import-extraction'); sub.add_argument('--workspace', required=True)
    sub.add_argument('--document-id', required=True); sub.add_argument('--bundle', required=True)
    sub = commands.add_parser('doctor'); sub.add_argument('--lean')
    for name in ('check', 'render', 'export'):
        sub = commands.add_parser(name); sub.add_argument('--workspace', required=True)
        sub.add_argument('--journal-root', help='Containing audit root for phases.jsonl')
        if name == 'check':
            sub.add_argument('--lean', required=True); sub.add_argument('--timeout', type=float, default=60)
            sub.add_argument('--checker', help='Optional compatible lean4checker binary for fresh environment replay')
            sub.add_argument('--checker-timeout', type=float, default=300)
        if name == 'export': sub.add_argument('--destination', required=True)
    args = parser.parse_args(argv)
    invocation = shlex.join([sys.executable, str(Path(__file__).resolve()), *(sys.argv[1:] if argv is None else argv)])
    args._journal_command = invocation
    try:
        operation = globals()[args.command.replace('-', '_')]
        if args.command in ('check', 'render'):
            root = Path(args.workspace)
            phase = 'verification' if args.command == 'check' else 'reporting'
            journal_root = getattr(args, 'journal_root', None)
            journal.append(root, journal_root=journal_root, phase=phase, status='started',
                title=f'{args.command} helper started', description='Automated helper execution; semantic phases are recorded separately by the agent.',
                inputs=[p for p in ('findings.json', 'claims.json') if (root / p).is_file()], command=invocation)
            try:
                result = operation(args)
            except (AuditError, OSError, UnicodeError, ValueError, corpus.sqlite3.Error) as exc:
                journal.append(root, journal_root=journal_root, phase=phase, status='failed',
                    title=f'{args.command} helper failed', description=str(exc), command=invocation, result='Helper failed; no success is asserted.')
                raise
            names = ('proof-results.json', 'environment.lock') if args.command == 'check' else ('audit-report.md', 'coverage.md')
            outputs = [p for p in names if (root / p).is_file()]
            if args.command == 'check':
                for directory, pattern in (('checks', '*.lean'), ('logs', '*.log')):
                    outputs.extend(p.relative_to(root).as_posix() for p in sorted((root / directory).rglob(pattern)) if p.is_file())
            journal.append(root, journal_root=journal_root, phase=phase, status='completed',
                title=f'{args.command} helper completed', description='The helper returned successfully; its output defines the scope of this result.',
                outputs=outputs, command=invocation, result='Helper returned successfully.')
        else:
            result = operation(args)
    except (AuditError, OSError, UnicodeError, ValueError, corpus.sqlite3.Error) as exc:
        print(json.dumps({'error': str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
