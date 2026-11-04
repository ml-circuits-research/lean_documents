#!/usr/bin/env python3
"""Verify preserved study exports and fixture identity; does not rerun Lean."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'skills/evidence-to-proof-review/scripts'))
import audit


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def verify(record, published):
    folder = ROOT / record['published_bundle' if published else 'source']
    fixture = ROOT / 'examples' / record['dossier']
    selected = fixture / ('report-correct.md' if record['variant'] == 'correct' else 'report.md')
    if not selected.exists():
        selected = fixture / 'report-mixed.md'
    checked_files = 0
    for name in ('export-manifest.json', 'bundle-manifest.json'):
        if (folder / name).exists():
            for relative, expected in read(folder / name)['files'].items():
                path = folder / relative
                assert path.resolve().is_relative_to(folder.resolve()), relative
                assert sha(path) == expected, f'Changed export artifact: {record["id"]}/{relative}'
                checked_files += 1
    if record['profile'] == 'v2':
        findings, proof = audit.verified(folder)
        assert proof['status'] == 'passed'
        assert len(findings) == record['conclusions']
        catalog = folder / 'input/catalog.json'
        if catalog.exists():
            docs = read(catalog)
            assert sum(d['role'] == 'report' for d in docs) == 1
            for doc in docs:
                if doc['role'] == 'report':
                    expected = selected
                elif doc['role'] == 'source':
                    expected = fixture / 'sources' / Path(doc['external']).name
                    if record['stage'] == 'revised' and expected.name in {'02-ledger.pdf', '02-ledger-r2.pdf'}:
                        expected = fixture / 'revisions/02-ledger-r2.pdf'
                else:
                    raise AssertionError('No brief was supplied for these demonstrations')
                assert sha(folder / doc['original']) == sha(expected), (record['id'], str(expected))
        else:
            assert sha(folder / 'input/report.md') == sha(selected)
            for original in (fixture / 'sources').rglob('*'):
                if original.is_file():
                    assert sha(folder / 'input/sources' / original.relative_to(fixture / 'sources')) == sha(original)
        if record['stage'] == 'revised':
            invalidation = read(folder / 'invalidation.json')
            assert invalidation['technical_results'] == 'all invalidated'
            assert set(invalidation['affected_claims']) == {'R1', 'R2', 'R5', 'R6', 'R7'}
            r1 = next(f for f in findings if f['claim_id'] == 'R1')
            assert r1['semantic_state'] == 'refuted'
    else:
        run = read(folder / 'run.json')
        assert run['execution_mode'] == 'agent-native'
        assert run['checks']['python_v2_validator'] == 'not_attempted'
        assert (folder / 'lean-exit-status.txt').read_text().strip() == '0'
        assert sha(folder / run['selected_report']) == sha(selected)
        for source in run['sources']:
            assert sha(folder / source) == sha(fixture / 'sources' / Path(source).name)
        assert 'sorryAx' not in (folder / 'lean.log').read_text()
        # Preserve the distinction: these are recorded native checks, not Python-v2 validation.
    assert (folder / 'independent-review.md').is_file()
    return dict(id=record['id'], profile=record['profile'], status='verified', export_hashes=checked_files)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--published', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    suite = read(ROOT / 'validation/tutorial-suite/suite-summary.json')
    results = [verify(r, args.published) for r in suite['runs']]
    rejected = read(ROOT / 'validation/tutorial-suite/stale-rejections.json')
    assert len(rejected) == 4 and all(r['exit_code'] != 0 for r in rejected)
    value = dict(status='passed', scope='Export integrity, exact-input identity and recorded final verification; no new Lean execution',
                 published=args.published, runs=results, stale_rejections=len(rejected))
    text = json.dumps(value, indent=2) + '\n'
    if args.output:
        args.output.write_text(text)
    print(text)
