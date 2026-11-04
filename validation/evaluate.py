#!/usr/bin/env python3
"""Compare completed claim audits with editorial expectations after blind work.

This evaluator does not create, repair, or supply audit findings. It reports
mismatches for human adjudication. It never treats prospective proofs as actual
Lean checks.
"""
import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import re


def aggregate(rows):
    states = {row['semantic_state'] for row in rows}
    for state in ('refuted', 'both', 'undetermined'):
        if state in states:
            return state
    if states == {'not_applicable'}:
        return 'not_applicable'
    if states == {'supported'}:
        return 'supported'
    return 'undetermined'


def evaluate(root, suite='all'):
    repo = Path(__file__).resolve().parents[1]
    results, missing = [], []
    for expectation_file in sorted((repo / 'examples/evaluator').glob('*.json')):
        extended = int(expectation_file.name.split('-', 1)[0]) > 5
        if (suite == 'baseline' and extended) or (suite == 'extended' and not extended):
            continue
        expectations = json.loads(expectation_file.read_text())['expectations']
        for variant, filename in [('mixed', 'report.md'), ('correct', 'report-correct.md')]:
            run_id = expectation_file.stem + '-' + variant
            run = root / run_id
            if not (run / 'findings.json').is_file():
                missing.append(run_id)
                continue
            findings = json.loads((run / 'findings.json').read_text())
            proof_results = json.loads((run / 'proof-results.json').read_text())
            grouped = defaultdict(list)
            for finding in findings:
                grouped[finding['report_anchor']].append(finding)
            # Visible claim IDs and HTML anchor IDs need not be equal. Resolve
            # IDs from the immutable selected report, not from expected verdicts.
            report_ledger = json.loads((run / 'input/report-ledger.json').read_text())
            claim_anchors = {}
            for anchor, paragraph in report_ledger.items():
                heading = re.match(r'\*\*([A-Za-z0-9-]+)\.\*\*', paragraph.strip())
                if heading:
                    if heading[1] in claim_anchors:
                        raise ValueError(f'Duplicate report claim ID: {heading[1]}')
                    claim_anchors[heading[1]] = anchor
            wanted = [row for row in expectations if row['report_path'] == filename]
            comparisons = []
            for expected in wanted:
                anchor = claim_anchors.get(expected['claim_id'])
                rows = grouped.get(anchor, [])
                actual = aggregate(rows) if rows else 'missing'
                comparisons.append({'claim_id': expected['claim_id'], 'expected': expected['semantic_state'],
                    'observed': actual, 'matches': actual == expected['semantic_state'],
                    'report_anchor': anchor, 'atomic_findings': [row['claim_id'] for row in rows]})
            extra = sorted(set(grouped) - {claim_anchors.get(row['claim_id']) for row in wanted})
            results.append({'run_id': run_id, 'expected_claims': len(wanted),
                'audited_atomic_findings': len(findings), 'matched_claims': sum(c['matches'] for c in comparisons),
                'mismatches': [c for c in comparisons if not c['matches']], 'extra_anchors': extra,
                'semantic_counts': dict(Counter(f['semantic_state'] for f in findings)),
                'argument_counts': dict(Counter(f['argument_status'] for f in findings)),
                'formal_counts': dict(Counter(f['formal_status'] for f in findings)),
                'technical_status': proof_results['status'],
                'checked_theorems': len({(p['module'],p['theorem']) for p in proof_results.get('targets',[]) if p['status']=='passed'}),
                'comparisons': comparisons})
    return {'scope': f'{suite} synthetic dossiers, each supplied report audited separately',
        'expectation_limit': 'Editorial expectations, not independently certified domain truth',
        'aggregation': 'Atomic findings grouped by original report anchor; refuted, then both, then undetermined take precedence. Mixed supported/nonformal maps to undetermined. Review ambiguous aggregation manually.',
        'runs': results, 'missing_runs': missing,
        'total_expected_claims': sum(r['expected_claims'] for r in results),
        'total_matched_claims': sum(r['matched_claims'] for r in results),
        'total_atomic_findings': sum(r['audited_atomic_findings'] for r in results),
        'total_checked_theorems': sum(r['checked_theorems'] for r in results)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--runs', type=Path, default=Path(__file__).parent / 'runs')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--suite', choices=['all', 'baseline', 'extended'], default='all')
    args = parser.parse_args()
    result = evaluate(args.runs.resolve(), args.suite)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'runs'}, indent=2))
    raise SystemExit(1 if result['missing_runs'] or any(r['mismatches'] or r['extra_anchors'] for r in result['runs']) else 0)
