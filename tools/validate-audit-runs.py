#!/usr/bin/env python3
"""Read-only validation of current Markdown audit runs, with readable output."""
import argparse
import importlib.util
from pathlib import Path
import sys
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'skills/evidence-to-proof-review/scripts'))
import markdown_audit

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--runs', type=Path, default=ROOT / 'tmp/audit-runs')
args = parser.parse_args()
root = args.runs.resolve()
if not root.is_relative_to(ROOT / 'tmp'):
    parser.error('Run inspection must stay inside this repository tmp directory')
print('# Audit run validation\n')
failed = 0
for run in sorted(root.iterdir()):
    if not run.is_dir() or not (run / 'run.md').is_file():
        continue
    print(f'## {run.name}\n')
    workspaces = list((run / 'work').glob('markdown-audit-*'))
    if len(workspaces) != 1:
        print('No single audit workspace exists. Execution may still be pending.\n')
        failed += 1
        continue
    try:
        import json  # Transient transport only; no JSON file is written.
        result = json.loads(markdown_audit.inspect(SimpleNamespace(workspace=workspaces[0], machine=True)))
        current = result.get('proof_results', {}) or {}
        ready = result['trace_complete'] and current.get('integrity') == 'current' and result['report_fresh']
        print(f"- Validated report: {'Yes' if ready else 'No'}\n- Findings: {len(result['findings'])}\n- Recorded individual steps: {len(result['phases'])}\n")
        for finding in result['findings']:
            print(f"### {finding['claim_id']}\n\n{finding['executive_summary']['conclusion']}\n")
        for error in result['errors']:
            print(f'Validation limitation: {error}\n')
        failed += not ready
    except (OSError, ValueError) as error:
        print(f'Inspection failed: {error}\n')
        failed += 1
raise SystemExit(1 if failed else 0)
