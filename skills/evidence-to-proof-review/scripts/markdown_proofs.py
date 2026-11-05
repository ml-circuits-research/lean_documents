"""Execute inspected Lean models with retained Markdown logs and no data manifests.

Source filtering is defense in depth, not a sandbox. Results establish encoded
propositions only; callers remain responsible for documentary correspondence.
"""
from __future__ import annotations

from datetime import datetime, timezone
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import tempfile

import audit

_ALLOWED_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}


def _block(text):
    text = str(text)
    fence = '`' * max(3, 1 + max((len(x) for x in re.findall(r'`+', text)), default=0))
    return f'{fence}\n{text}\n{fence}\n'


def _execute(command, cwd, log, env, timeout):
    started = datetime.now(timezone.utc).isoformat()
    status, stdout, stderr = None, '', ''
    failure = None
    try:
        process = subprocess.run(command, cwd=cwd, env=env, capture_output=True,
                                 text=True, timeout=timeout, check=False)
        status, stdout, stderr = process.returncode, process.stdout, process.stderr
        if status:
            failure = f'Lean exited with code {status}; see {log}'
    except subprocess.TimeoutExpired as exc:
        def decode(value):
            return value.decode('utf-8', errors='replace') if isinstance(value, bytes) else value or ''
        stdout, stderr = decode(exc.stdout), decode(exc.stderr)
        failure = f'Lean timed out after {timeout} seconds; see {log}'
    except OSError as exc:
        stderr = str(exc)
        failure = f'Could not execute Lean; see {log}'
    log.write_text('# Lean execution\n\n'
                   f'Started (UTC): {started}\n\nWorking directory: {cwd}\n\n'
                   f'Exit code: {status if status is not None else "not available"}\n\n'
                   f'LEAN_PATH: {env["LEAN_PATH"]}\n\nCommand:\n\n{_block(shlex.join(command))}\n'
                   f'Stdout:\n\n{_block(stdout)}\nStderr:\n\n{_block(stderr)}\n'
                   + (f'Failure: {failure}\n' if failure else ''), encoding='utf-8')
    if failure:
        raise ValueError(failure)
    return stdout + '\n' + stderr


def _proofs(proofs, declarations):
    for proof in proofs:
        if not isinstance(proof, dict) or any(not isinstance(proof.get(k), str) or not proof[k].strip()
                                            for k in ('module', 'theorem', 'target', 'relation', 'claim_id')):
            raise ValueError('Each proof needs module, theorem, target, relation and claim_id strings')
        if proof['module'] not in declarations or proof['theorem'] not in declarations[proof['module']]:
            raise ValueError(f'Missing declared theorem: {proof["module"]}.{proof["theorem"]}')
        if proof['relation'] not in {'supports', 'refutes', 'auxiliary'}:
            raise ValueError('Unknown proof relation')
        raw = proof['target']
        target = audit.lean_code(raw, reject_comments=True)
        if '\n' in raw or '\r' in raw or '#' in target or re.search(
            r'\b(theorem|lemma|def|example|import|axiom|by|where|end|namespace|section|set_option|attribute|elab|macro|initialize)\b|:=|[;`]', target
        ):
            raise ValueError('Target must be one proposition without commands, tactics or comments')
        stack, pairs = [], {')': '(', ']': '[', '}': '{'}
        for char in target:
            if char in '([{':
                stack.append(char)
            elif char in pairs and (not stack or stack.pop() != pairs[char]):
                raise ValueError('Unbalanced target delimiters')
        if stack:
            raise ValueError('Unbalanced target delimiters')


def _order(models):
    dependencies = {}
    for module, path in models.items():
        code = audit.lean_code(path.read_text(encoding='utf-8'))
        dependencies[module] = set(re.findall(r'\bimport\s+(?:all\s+)?(' + audit.MODULE_NAME + ')', code)) & models.keys()
    ordered, visiting = [], set()
    def visit(module):
        if module in visiting:
            raise ValueError(f'Local import cycle involving {module}')
        if module in ordered:
            return
        visiting.add(module)
        for dependency in sorted(dependencies[module]):
            visit(dependency)
        visiting.remove(module)
        ordered.append(module)
    for module in models:
        visit(module)
    return ordered


def check_models(workspace, lean, proofs, lean_version='4.24.0', timeout=60):
    """Return all declaration and requested-target checks, retaining every attempt.

    Each result has module, theorem, target, relation, claim_id, status, log,
    check_file and axioms. Declaration checks have None for target/relation/
    claim_id; requested checks preserve the caller's values. Paths are relative
    to workspace. A failure raises ValueError and leaves its Markdown records.
    """
    root = Path(workspace).resolve()
    if not root.is_dir():
        raise ValueError('Workspace does not exist')
    if not isinstance(timeout, (int, float)) or timeout <= 0:
        raise ValueError('Timeout must be positive')
    history = root / 'proof-attempts'
    if history.is_symlink():
        raise ValueError('proof-attempts cannot be a symlink')
    history.mkdir(exist_ok=True)
    attempt = Path(tempfile.mkdtemp(prefix=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ-'), dir=history))
    try:
        audit.validate_lean_version(lean_version)
        models = audit.model_inventory(root)
        snapshot = attempt / 'models'
        snapshot.mkdir()
        for module, path in models.items():
            destination = snapshot / path.relative_to(root / 'models')
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, destination)
        # Inspect the retained snapshot that will actually be compiled.
        models = {m: snapshot / p.relative_to(root / 'models') for m, p in models.items()}
        declarations = {m: audit.inspect_model(p, models) for m, p in models.items()}
        proofs = list(proofs)
        _proofs(proofs, declarations)
        ordered = _order(models)
        build = attempt / 'build'
        checks = attempt / 'checks'
        logs = attempt / 'logs'
        for directory in (build, checks, logs):
            directory.mkdir()
        executable = shutil.which(str(lean)) or str(Path(lean).resolve())
        env = dict(os.environ)
        for key in ('LEAN_PATH', 'LEAN_SRC_PATH', 'LEAN_SYSROOT', 'LAKE_HOME'):
            env.pop(key, None)
        env['LEAN_PATH'] = str(build)
        version = _execute([executable, '--version'], snapshot, logs / 'version.md', env, timeout)
        observed = re.search(r'\bversion ([^\s,;()]+)', version)
        if observed is None or observed.group(1) != lean_version:
            raise ValueError(f'Lean {lean_version} required; observed {version.strip()}')
        for index, module in enumerate(ordered, 1):
            output = build / (module.replace('.', '/') + '.olean')
            output.parent.mkdir(parents=True, exist_ok=True)
            _execute([executable, '-o', str(output), str(models[module].relative_to(snapshot))],
                     snapshot, logs / f'build-{index:03d}.md', env, timeout)
            if not output.is_file():
                raise ValueError(f'Compilation produced no object for {module}')
        requests = [dict(module=m, theorem=t, target=None, relation=None, claim_id=None)
                    for m, names in declarations.items() for t in names] + proofs
        results = []
        for index, proof in enumerate(requests, 1):
            module, theorem = proof['module'], proof['theorem']
            check = checks / f'Target{index:03d}.lean'
            content = f'import {module}\n#check @{theorem}\n#print axioms {theorem}\n'
            if proof['target'] is not None:
                content += f'example : ({proof["target"]}) := {theorem}\n'
            check.write_text(content, encoding='utf-8')
            log = logs / f'target-{index:03d}.md'
            output = _execute([executable, str(check)], checks, log, env, timeout)
            groups = re.findall(r'depends on axioms:\s*\[([^\]]*)\]', output, re.S)
            axioms = sorted({a.strip() for group in groups for a in group.split(',') if a.strip()})
            if set(axioms) - _ALLOWED_AXIOMS:
                raise ValueError(f'Unapproved axioms in {theorem}: {axioms}')
            if not groups and 'does not depend on any axioms' not in output:
                raise ValueError(f'No axiom inspection result for {theorem}')
            results.append({k: proof[k] for k in ('module', 'theorem', 'target', 'relation', 'claim_id')} |
                           {'status': 'passed', 'log': log.relative_to(root).as_posix(),
                            'check_file': check.relative_to(root).as_posix(), 'axioms': axioms})
        (attempt / 'result.md').write_text(f'# Proof attempt\n\nCompleted {len(results)} declaration and target checks.\n\n'
                                         'Lean checks the encoded propositions; documentary correspondence needs separate review.\n', encoding='utf-8')
        return results
    except (audit.AuditError, ValueError, OSError, TypeError) as exc:
        (attempt / 'failure.md').write_text('# Proof attempt failed\n\n' + _block(str(exc)), encoding='utf-8')
        raise ValueError(f'{exc} (retained attempt: {attempt.relative_to(root)})') from exc
