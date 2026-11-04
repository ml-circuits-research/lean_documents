#!/usr/bin/env python3
"""Recheck exported audit bundles in new temporary workspaces without answer keys."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lean', required=True)
    parser.add_argument('--checker', help='Optional compatible checker; replay through the same Lean kernel')
    parser.add_argument('--only', help='Reproduce only this exact run ID')
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    if args.only and (Path(args.only).name != args.only or args.only in {'.', '..'}):
        parser.error('--only must be a single run directory name')
    summary_path = base / ('reproduction-' + args.only + '.json' if args.only else 'reproduction.json')
    helper = base.parent / 'skills/evidence-to-proof-review/scripts/audit.py'
    outputs = base / ('reproduction-checker' if args.checker else 'reproduction')
    outputs.mkdir(exist_ok=True)
    summary = []
    for run in sorted((base / 'runs').iterdir()):
        if not run.is_dir(): continue
        if args.only and run.name != args.only: continue
        manifest = json.loads((run / 'export-manifest.json').read_text())
        for rel, expected in manifest['files'].items():
            if sha(run / rel) != expected:
                raise ValueError(f'Export integrity mismatch: {run.name}/{rel}')
        temp_root = base.parent / 'tmp'
        temp_root.mkdir(exist_ok=True)
        work = Path(tempfile.mkdtemp(prefix='reproduction-' + run.name + '-', dir=temp_root))
        shutil.copytree(run, work, dirs_exist_ok=True, ignore=shutil.ignore_patterns('.lake', 'attempts'))
        command = ['python3', str(helper), 'check', '--workspace', str(work), '--lean', str(Path(args.lean).resolve())]
        if args.checker:
            command += ['--checker', str(Path(args.checker).resolve())]
        module_count = max(1, len(list((work / 'models').glob('*.lean'))))
        result = subprocess.run(command, capture_output=True, text=True, timeout=300 + (module_count * 330 if args.checker else 0))
        target = outputs / run.name
        target.mkdir(exist_ok=True)
        (target / 'command.log').write_text('$ ' + ' '.join(command) + '\n' + result.stdout + result.stderr)
        if (work / 'proof-results.json').exists():
            shutil.copyfile(work / 'proof-results.json', target / 'proof-results.json')
        for name in ('logs', 'checks'):
            if (work / name).exists(): shutil.copytree(work / name, target / name, dirs_exist_ok=True)
        summary.append({'run_id': run.name, 'exit_code': result.returncode,
            'workspace': str(work), 'original_export_manifest_sha256': sha(run / 'export-manifest.json'),
            'proof_results': str((target / 'proof-results.json').relative_to(base)),
            'command_log': str((target / 'command.log').relative_to(base))})
        if result.returncode:
            summary_path.write_text(json.dumps(summary, indent=2) + '\n')
            raise SystemExit(f'Reproduction failed: {run.name}; see {target}')
    if not summary:
        raise SystemExit('No matching audit bundle was found')
    summary_path.write_text(json.dumps(summary, indent=2) + '\n')
    print(f'Reproduced {len(summary)} audit bundles in fresh temporary workspaces.')


if __name__ == '__main__': main()
