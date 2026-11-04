"""Regression checks for fixture provenance and evaluator location mapping."""
import importlib.util
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('evaluate', ROOT / 'validation/evaluate.py')
evaluate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evaluate)


class ValidationTests(unittest.TestCase):
    def test_extended_report_coverage_and_native_originals(self):
        result = evaluate.evaluate(ROOT / 'validation/runs', 'extended')
        self.assertEqual(result['missing_runs'], [])
        self.assertEqual(result['total_expected_claims'], 156)
        self.assertEqual(result['total_matched_claims'], 156)
        self.assertTrue(all(not run['extra_anchors'] for run in result['runs']))
        for item in result['runs']:
            run = ROOT / 'validation/runs' / item['run_id']
            dossier, variant = item['run_id'].rsplit('-', 1)
            fixture = ROOT / 'examples' / dossier
            catalog = json.loads((run / 'input/catalog.json').read_text())
            self.assertEqual(len(catalog), 2 + sum(p.is_file() for p in (fixture / 'sources').rglob('*')))
            for document in catalog:
                if document['role'] == 'source':
                    relative = document['external'].split('/sources/', 1)[1]
                    source = fixture / 'sources' / relative
                else:
                    source = fixture / ('brief.md' if document['role'] == 'brief' else 'report-correct.md' if variant == 'correct' else 'report.md')
                self.assertEqual((run / document['original']).read_bytes(), source.read_bytes())
                self.assertEqual(document['original_sha'], hashlib.sha256(source.read_bytes()).hexdigest())

    def test_all_report_findings_are_accounted_for(self):
        result = evaluate.evaluate(ROOT / 'validation/runs', 'baseline')
        self.assertEqual(result['missing_runs'], [])
        self.assertEqual(result['total_expected_claims'], 81)
        self.assertEqual(result['total_matched_claims'], 81)
        self.assertTrue(all(not run['extra_anchors'] for run in result['runs']))

    def test_visible_claim_ids_resolve_distinct_html_anchors(self):
        result = evaluate.evaluate(ROOT / 'validation/runs', 'baseline')
        run = next(r for r in result['runs'] if r['run_id'] == '05-conflicting-evidence-mixed')
        first = next(c for c in run['comparisons'] if c['claim_id'] == 'CE-01')
        self.assertEqual(first['report_anchor'], 'report-ce01')
        self.assertTrue(first['matches'])

    def test_audited_snapshots_equal_original_selected_fixture_inputs(self):
        for run in (ROOT / 'validation/runs').iterdir():
            if int(run.name.split('-', 1)[0]) > 5:
                continue  # Native originals have an independent indexed-ingestion test suite.
            dossier, variant = run.name.rsplit('-', 1)
            fixture = ROOT / 'examples' / dossier
            report = 'report-correct.md' if variant == 'correct' else 'report.md'
            self.assertEqual((run / 'input/report.md').read_bytes(), (fixture / report).read_bytes())
            self.assertEqual((run / 'input/brief.md').read_bytes(), (fixture / 'brief.md').read_bytes())
            expected = {p.relative_to(fixture / 'sources') for p in (fixture / 'sources').rglob('*') if p.is_file()}
            observed = {p.relative_to(run / 'input/sources') for p in (run / 'input/sources').rglob('*') if p.is_file()}
            self.assertEqual(expected, observed)
            for rel in expected:
                self.assertEqual((run / 'input/sources' / rel).read_bytes(), (fixture / 'sources' / rel).read_bytes())


if __name__ == '__main__': unittest.main()
