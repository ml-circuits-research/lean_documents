#!/usr/bin/env python3
"""Append and validate factual phase events; never infer historical execution."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
import os
import tempfile
import uuid

PHASES = ('intake', 'extraction', 'claims', 'evidence', 'modeling', 'verification', 'review', 'reporting')
CLAIM_STEPS = ('registration', 'evidence', 'analysis', 'verification', 'verdict')
STATUSES = ('started', 'completed', 'failed', 'blocked', 'note')


def journal_path(workspace, journal_root=None):
    workspace = Path(workspace).resolve(strict=True)
    root = Path(journal_root).resolve(strict=True) if journal_root else workspace
    if not workspace.is_dir() or not root.is_dir() or not workspace.is_relative_to(root):
        raise ValueError('Journal root must be the workspace or an ancestor directory')
    path = root / 'phases.jsonl'
    if path.is_symlink():
        raise ValueError('The phase journal must not be a symbolic link')
    return path


def artifact(workspace, value, capture=False):
    root = Path(workspace).resolve(strict=True)
    path = Path(value)
    path = (root / path).resolve(strict=True) if not path.is_absolute() else path.resolve(strict=True)
    if not path.is_relative_to(root) or not path.is_file():
        raise ValueError('Artifacts must be files inside the workspace')
    hasher = hashlib.sha256()
    temporary = None
    snapshot_root = root / 'phase-artifacts'
    if capture:
        if snapshot_root.is_symlink():
            raise ValueError('Snapshot directory must not be a symbolic link')
        snapshot_root.mkdir(exist_ok=True)
        temporary = tempfile.NamedTemporaryFile(prefix='.capture-', dir=snapshot_root, delete=False)
    try:
        with path.open('rb') as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b''):
                hasher.update(chunk)
                if temporary:
                    temporary.write(chunk)
        digest = hasher.hexdigest()
        ref = {'path': path.relative_to(root).as_posix(), 'sha256': digest}
        if temporary:
            temporary.close()
            directory = snapshot_root / digest
            if directory.is_symlink():
                raise ValueError('Snapshot hash directory must not be a symbolic link')
            directory.mkdir(exist_ok=True)
            destination = directory / path.name
            if destination.is_symlink():
                raise ValueError('Snapshot file must not be a symbolic link')
            if destination.exists():
                if artifact(root, destination)['sha256'] != digest:
                    raise ValueError('Existing content-addressed snapshot is corrupt')
                Path(temporary.name).unlink()
            else:
                os.replace(temporary.name, destination)
            ref['snapshot'] = destination.relative_to(root).as_posix()
        return ref
    finally:
        if temporary:
            temporary.close()
            Path(temporary.name).unlink(missing_ok=True)



def validate_event(event):
    required = {'schema_version', 'event_id', 'timestamp', 'phase', 'status', 'title',
                'description', 'claim_ids', 'inputs', 'outputs'}
    if not isinstance(event, dict) or not required <= event.keys():
        raise ValueError('Event is missing required fields')
    if set(event) - required - {'command', 'result', 'claim_step'}:
        raise ValueError('Unknown event fields')
    if type(event['schema_version']) is not int or event['schema_version'] != 1:
        raise ValueError('Unsupported phase journal schema')
    for name in ('event_id', 'timestamp', 'title', 'description'):
        if not isinstance(event[name], str) or not event[name].strip():
            raise ValueError(f'{name} must be a nonempty string')
    stamp = datetime.fromisoformat(event['timestamp'].replace('Z', '+00:00'))
    if stamp.utcoffset() is None or stamp.utcoffset().total_seconds() != 0:
        raise ValueError('timestamp must have a UTC offset')
    if event['phase'] not in PHASES or event['status'] not in STATUSES:
        raise ValueError('Invalid phase or status')
    if not isinstance(event['claim_ids'], list) or any(not isinstance(x, str) or not x.strip() for x in event['claim_ids']):
        raise ValueError('claim_ids must be an array of nonempty strings')
    if len(set(event['claim_ids'])) != len(event['claim_ids']):
        raise ValueError('Duplicate claim IDs')
    for name in ('inputs', 'outputs'):
        if not isinstance(event[name], list):
            raise ValueError(f'{name} must be an array')
        for ref in event[name]:
            if not isinstance(ref, dict) or not {'path', 'sha256'} <= set(ref) or set(ref) - {'path', 'sha256', 'snapshot'}:
                raise ValueError('Artifact references require path and sha256')
            for key in ('path', 'snapshot'):
                if key not in ref:
                    continue
                path = ref[key]
                if not isinstance(path, str) or not path or '\\' in path or Path(path).is_absolute() or any(p in ('', '.', '..') for p in path.split('/')):
                    raise ValueError('Artifact paths must be normalized journal-relative paths')
            if not isinstance(ref['sha256'], str) or not re.fullmatch('[0-9a-f]{64}', ref['sha256']):
                raise ValueError('Artifact sha256 must be a lowercase SHA-256 digest')
    if 'claim_step' in event:
        if event['claim_step'] not in CLAIM_STEPS or len(event['claim_ids']) != 1:
            raise ValueError('claim_step requires a supported step and exactly one claim ID')
        if event['status'] == 'completed':
            if not event['inputs'] or not event['outputs'] or any('snapshot' not in ref for ref in event['inputs'] + event['outputs']):
                raise ValueError('Completed claim steps require snapshotted inputs and outputs')
        if event['status'] in ('completed', 'blocked', 'failed') and not str(event.get('result', '')).strip():
            raise ValueError('Terminal claim steps require an explicit result or limitation')
    for name in ('command', 'result'):
        if name in event and not isinstance(event[name], str):
            raise ValueError(f'{name} must be a string')


def validate(workspace, journal_root=None):
    path = journal_path(workspace, journal_root)
    if not path.exists():
        return {'status': 'legacy_unknown', 'events': 0, 'artifact_changes': [],
                'reason': 'No phase journal exists; historical execution is not recorded.'}
    seen = set()
    changes = []
    unavailable = []
    previous = None
    with path.open(encoding='utf-8') as stream:
        for number, line in enumerate(stream, 1):
            try:
                event = json.loads(line)
                validate_event(event)
                if event['event_id'] in seen:
                    raise ValueError('Duplicate event ID')
                stamp = datetime.fromisoformat(event['timestamp'].replace('Z', '+00:00'))
                if previous and stamp < previous:
                    raise ValueError('Timestamps must be chronological')
                previous = stamp
                seen.add(event['event_id'])
                for ref in event['inputs'] + event['outputs']:
                    if 'snapshot' in ref:
                        if artifact(path.parent, ref['snapshot'])['sha256'] != ref['sha256']:
                            raise ValueError('Historical snapshot hash mismatch')
                    else:
                        unavailable.append({'event_id': event['event_id'], 'path': ref['path'], 'reason': 'No historical snapshot was recorded.'})
                    try:
                        current = artifact(path.parent, ref['path'])['sha256']
                    except (OSError, ValueError):
                        current = None
                    if current != ref['sha256']:
                        changes.append({'event_id': event['event_id'], 'path': ref['path'],
                                        'recorded_sha256': ref['sha256'], 'current_sha256': current})
            except (ValueError, TypeError, KeyError) as exc:
                raise ValueError(f'Invalid phase event at line {number}: {exc}') from exc
    return {'status': 'valid', 'events': len(seen), 'artifact_changes': changes, 'unavailable_snapshots': unavailable}


def append(workspace, *, phase, status, title, description, claim_ids=(), inputs=(), outputs=(),
           command=None, result=None, journal_root=None, claim_step=None):
    path = journal_path(workspace, journal_root)
    # Validate the existing history before appending. Historical hashes need not
    # match current bytes: mutable artifacts legitimately evolve between events.
    validate(workspace, journal_root)
    event = {'schema_version': 1, 'event_id': str(uuid.uuid4()),
             'timestamp': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
             'phase': phase, 'status': status, 'title': title, 'description': description,
             'claim_ids': list(claim_ids),
             'inputs': [artifact(path.parent, Path(workspace).resolve() / item, capture=True) for item in inputs],
             'outputs': [artifact(path.parent, Path(workspace).resolve() / item, capture=True) for item in outputs]}
    for name, value in (('command', command), ('result', result), ('claim_step', claim_step)):
        if value is not None:
            event[name] = value
    validate_event(event)
    if path.exists():
        lines = path.read_text(encoding='utf-8').splitlines()
        if lines:
            previous = datetime.fromisoformat(json.loads(lines[-1])['timestamp'].replace('Z', '+00:00'))
            current = datetime.fromisoformat(event['timestamp'].replace('Z', '+00:00'))
            if current < previous:
                raise ValueError('Clock precedes the last recorded event; history was not modified')
    if path.exists() and path.stat().st_size:
        with path.open('rb') as stream:
            stream.seek(-1, 2)
            if stream.read(1) != b'\n':
                raise ValueError('Existing journal lacks a final newline; preserve and repair the interrupted record before appending')
    with path.open('a', encoding='utf-8') as stream:
        stream.write(json.dumps(event, ensure_ascii=False) + '\n')
        stream.flush()
    return event


def validate_claim_traces(workspace, findings, journal_root=None):
    """Enforce the opt-in individual trace profile without upgrading old bundles."""
    workspace = Path(workspace).resolve()
    policy_path = workspace / 'input/audit-policy.json'
    policy = json.loads(policy_path.read_text()) if policy_path.is_file() else {}
    if not policy.get('require_claim_traces', False):
        return {'profile': 'legacy_unenforced', 'limitation': 'Individual claim chronology and executive summaries were not required for this bundle.'}
    path = journal_path(workspace, journal_root)
    validation = validate(workspace, journal_root)
    if validation['status'] != 'valid':
        raise ValueError('Individual claim traces require a recorded phase journal')
    events = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]
    known = {finding['claim_id'] for finding in findings}
    latest = {}
    owners = {}
    for index, event in enumerate(events):
        if 'claim_step' not in event:
            continue
        ident = event['claim_ids'][0]
        if ident not in known:
            raise ValueError(f'Unknown claim in individual trace: {ident}')
        latest[(ident, event['claim_step'])] = (index, event)
        for ref in event['outputs']:
            owners.setdefault(ref['path'], set()).add(ident)
    blocked = []
    for finding in findings:
        ident = finding['claim_id']
        summary = finding.get('executive_summary')
        if not isinstance(summary, dict) or any(not isinstance(summary.get(key), str) or not summary[key].strip() for key in ('conclusion', 'how_verified', 'limits')):
            raise ValueError(f'{ident}: executive_summary requires conclusion, how_verified, and limits')
        previous = -1
        for step in CLAIM_STEPS:
            pair = latest.get((ident, step))
            if not pair:
                raise ValueError(f'{ident}: missing individually recorded {step} step')
            index, event = pair
            if index <= previous:
                raise ValueError(f'{ident}: claim steps must be recorded in execution order; repeat downstream steps after revisions')
            previous = index
            if event['status'] not in ('completed', 'blocked', 'failed'):
                raise ValueError(f'{ident}: {step} has no terminal result')
            if not event['outputs'] or any('snapshot' not in ref for ref in event['outputs']):
                raise ValueError(f'{ident}: {step} requires a retained per-claim output artifact')
            if not any(owners[ref['path']] == {ident} for ref in event['outputs']):
                raise ValueError(f'{ident}: {step} has only shared outputs, not an individual intermediate artifact')
            if event['status'] != 'completed':
                blocked.append({'claim_id': ident, 'step': step, 'status': event['status'], 'limitation': event['result']})
            if step == 'verification' and finding.get('proofs'):
                if event['status'] != 'completed' or not event.get('command', '').strip() or not any(ref['path'].endswith('.log') for ref in event['outputs']):
                    raise ValueError(f'{ident}: formal proof findings require completed individual verification with actual command and log')
    return {'profile': 'individual_claim_traces_v1', 'claims': len(findings), 'steps_per_claim': list(CLAIM_STEPS), 'limitations': blocked,
            'assurance_limit': 'Recorded artifacts and chronology are checked mechanically; semantic adequacy and summary fidelity require review.'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='operation', required=True)
    for name in ('append', 'validate'):
        sub = commands.add_parser(name)
        sub.add_argument('--workspace', required=True)
        sub.add_argument('--journal-root', help='Containing audit directory; default is workspace')
        if name == 'append':
            sub.add_argument('--claim-step', choices=CLAIM_STEPS)
            sub.add_argument('--phase', choices=PHASES, required=True)
            sub.add_argument('--status', choices=STATUSES, required=True)
            sub.add_argument('--title', required=True)
            sub.add_argument('--description', required=True)
            for flag in ('claim-id', 'input', 'output'):
                sub.add_argument('--' + flag, action='append', default=[])
            sub.add_argument('--command')
            sub.add_argument('--result')
    args = vars(parser.parse_args(argv))
    operation = args.pop('operation')
    if operation == 'append':
        args['claim_ids'] = args.pop('claim_id')
        args['inputs'] = args.pop('input')
        args['outputs'] = args.pop('output')
    try:
        value = globals()[operation](**args)
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({'error': str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps(value, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
