"""Behavioral checks for explicit registration and independent argument audit."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / 'skills/evidence-to-proof-review/scripts/contracts.py'
spec = importlib.util.spec_from_file_location('contracts', MODULE)
contracts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(contracts)
TEST_ROOT = MODULE.parents[3] / 'tmp'
TEST_ROOT.mkdir(exist_ok=True)
TEST_RUN = Path(tempfile.mkdtemp(prefix='contracts-tests-', dir=TEST_ROOT))


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix=self._testMethodName + '-', dir=TEST_RUN))
        (self.root / 'input').mkdir()
        self.write('input/report-ledger.json', {'R0': '# Report', 'R1': 'The total is three. One plus two is three.'})
        self.write('input/source-ledger.json', {'input/sources/ledger.md': {'L1': 'The amounts are one and two.'}})
        self.registry = contracts.initialize(self.root)
        for row in self.registry['anchors']:
            row['classification'] = 'claims' if row['report_anchor'] == 'R1' else 'non_claim'
            row['reason'] = 'Contains an arithmetic assertion.' if row['report_anchor'] == 'R1' else 'Document title only.'
        self.registry['claims'] = [{'claim_id': 'C1', 'report_anchor': 'R1', 'report_quote': 'The total is three.', 'disposition': 'audited'},
                                   {'claim_id': 'C2', 'report_anchor': 'R1', 'report_quote': 'One plus two is three.',
                                    'disposition': 'deferred', 'reason': 'The second assertion is explicitly outside this batch.'}]
        self.save_registry()
        self.finding = {
            'claim_id': 'C1', 'report_anchor': 'R1', 'report_quote': 'The total is three.',
            'argument_status': 'sufficient', 'semantic_state': 'supported', 'formal_status': 'not_attempted',
            'evidence': [{'path': 'input/sources/ledger.md', 'anchor': 'L1', 'quote': 'The amounts are one and two.'}],
            'proofs': [],
            'criteria': {'origin': 'inferred', 'operational_question': 'Is the stated total the sum of the recorded amounts?',
                         'decision_criteria': ['Add each recorded amount once and compare with three.'], 'scope': 'Two recorded amounts only.',
                         'missing_definitions': [], 'alternatives': []},
            'argument_audit': {'outcome': 'sufficient', 'report_items': [
                {'kind': 'inference', 'report_anchor': 'R1', 'report_quote': 'One plus two is three.', 'assessment': 'verified',
                 'reasoning': 'The stated arithmetic agrees with the supplied ledger.', 'evidence_refs': [0], 'proof_refs': []}],
                'independent_reasoning': ['The source records one and two, whose sum is three.'],
                'evidence_refs': [0], 'proof_refs': [], 'claim_dependencies': []},
            'formalization': {'rationale': 'Documentary test fixture; no execution is claimed.', 'correspondence': []}}

    def write(self, name, data):
        (self.root / name).write_text(json.dumps(data), encoding='utf-8')

    def save_registry(self):
        self.write('claims.json', self.registry)

    def validate(self, findings=None):
        return contracts.validate(self.root, [self.finding] if findings is None else findings)

    def make_gap(self):
        self.finding['argument_status'] = 'insufficient_support'
        self.finding['argument_audit'].update(outcome='not_provided', report_items=[])
        self.finding['support_search'] = {
            'scope': 'Supplied ledger passage L1.', 'queries': ['total', 'sum'],
            'inspected': [{'path': 'input/sources/ledger.md', 'anchor': 'L1'}],
            'limitations': ['No materials outside the supplied dossier were searched.'],
            'conclusion': 'This report conclusion does not provide an explicit source citation.'}

    def test_partial_coverage_counts_deferred_claims(self):
        result = self.validate()
        self.assertEqual(result['coverage'], 'partial')
        self.assertEqual((result['audited_claims'], result['deferred_claims']), (1, 1))
        rendered = '\n'.join(contracts.render(self.root, [self.finding]))
        self.assertIn('Deferred `C2`', rendered)
        self.assertIn('does not establish semantic completeness', rendered)

    def test_missing_anchor_classification_is_rejected(self):
        self.registry['anchors'].pop(0)
        self.save_registry()
        with self.assertRaisesRegex(ValueError, 'Every report anchor'):
            self.validate()

    def test_pending_anchor_is_rejected(self):
        self.registry['anchors'][0]['classification'] = 'pending'
        self.save_registry()
        with self.assertRaisesRegex(ValueError, 'pending'):
            self.validate()

    def test_non_claim_requires_reason(self):
        self.registry['anchors'][0]['reason'] = ''
        self.save_registry()
        with self.assertRaisesRegex(ValueError, 'reason'):
            self.validate()

    def test_claim_classification_requires_registered_claim(self):
        self.registry['anchors'][0]['classification'] = 'claims'
        self.save_registry()
        with self.assertRaisesRegex(ValueError, 'no registered claims'):
            self.validate()

    def test_registered_claim_cannot_be_silently_omitted(self):
        with self.assertRaisesRegex(ValueError, 'missing findings'):
            self.validate([])

    def test_duplicate_finding_id_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate finding'):
            self.validate([self.finding, copy.deepcopy(self.finding)])

    def test_unknown_finding_id_rejected(self):
        self.finding['claim_id'] = 'UNREGISTERED'
        with self.assertRaisesRegex(ValueError, 'Unknown finding'):
            self.validate()

    def test_quote_cannot_change_even_to_other_true_report_substring(self):
        self.finding['report_quote'] = 'One plus two is three.'
        with self.assertRaisesRegex(ValueError, 'altered registered'):
            self.validate()

    def test_fabricated_report_premise_rejected(self):
        self.finding['argument_audit']['report_items'][0]['report_quote'] = 'An independent auditor certified the total.'
        with self.assertRaisesRegex(ValueError, 'report quote does not match'):
            self.validate()

    def test_missing_criteria_rejected(self):
        del self.finding['criteria']
        with self.assertRaisesRegex(ValueError, 'criteria'):
            self.validate()

    def test_empty_evidence_valid_with_bounded_search(self):
        self.make_gap()
        self.finding['evidence'] = []
        self.finding['argument_audit']['evidence_refs'] = []
        self.finding['semantic_state'] = 'undetermined'
        self.finding['support_search']['conclusion'] = 'The inspected passage supplies no independent evidence about authentication.'
        self.validate()

    def test_gap_without_search_rejected(self):
        self.make_gap()
        self.finding['support_search'] = {}
        with self.assertRaisesRegex(ValueError, 'support_search.scope'):
            self.validate()

    def test_zero_inspections_requires_explicit_reason(self):
        self.make_gap()
        self.finding['support_search']['inspected'] = []
        with self.assertRaisesRegex(ValueError, 'uninspected_reason'):
            self.validate()
        self.finding['support_search']['uninspected_reason'] = 'No extracted source passages were accessible in this batch.'
        self.validate()

    def test_search_cannot_invent_inspected_anchor(self):
        self.make_gap()
        self.finding['support_search']['inspected'][0]['anchor'] = 'MISSING'
        with self.assertRaisesRegex(ValueError, 'unknown source passage'):
            self.validate()

    def test_justification_and_semantic_support_are_separate(self):
        self.make_gap()
        self.validate()
        self.assertEqual(self.finding['semantic_state'], 'supported')
        self.finding['argument_status'] = 'sufficient'
        with self.assertRaisesRegex(ValueError, 'disagrees'):
            self.validate()

    def test_report_cannot_be_independent_evidence(self):
        self.finding['evidence'][0].update(path='input/report.md', anchor='R1', quote='The total is three.')
        with self.assertRaisesRegex(ValueError, 'independent source'):
            self.validate()

    def test_brief_cannot_be_used_as_independent_search_material(self):
        self.make_gap()
        self.finding['support_search']['inspected'][0].update(path='input/brief.md')
        with self.assertRaisesRegex(ValueError, 'independent source'):
            self.validate()

    def test_malformed_enum_produces_validation_error(self):
        self.finding['criteria']['origin'] = ['inferred']
        with self.assertRaisesRegex(ValueError, 'criteria origin'):
            self.validate()

    def test_self_support_dependency_rejected(self):
        self.finding['argument_audit']['claim_dependencies'] = ['C1']
        with self.assertRaisesRegex(ValueError, 'Circular'):
            self.validate()

    def test_circular_support_dependency_rejected(self):
        self.registry['claims'][1]['disposition'] = 'audited'
        self.save_registry()
        second = copy.deepcopy(self.finding)
        second.update(claim_id='C2', report_quote='One plus two is three.')
        second['argument_audit']['claim_dependencies'] = ['C1']
        self.finding['argument_audit']['claim_dependencies'] = ['C2']
        with self.assertRaisesRegex(ValueError, 'Circular'):
            self.validate([self.finding, second])

    def test_deferred_dependency_cannot_be_used_as_audited_support(self):
        self.finding['argument_audit']['claim_dependencies'] = ['C2']
        with self.assertRaisesRegex(ValueError, 'distinct audited'):
            self.validate()

    def test_long_dependency_chain_does_not_use_python_recursion(self):
        # A graph stress fixture, not a claim of faithful semantic decomposition.
        findings, claims = [], []
        for index in range(1100):
            ident = f'CHAIN{index}'
            finding = copy.deepcopy(self.finding)
            finding['claim_id'] = ident
            finding['argument_audit']['claim_dependencies'] = [f'CHAIN{index + 1}'] if index < 1099 else []
            findings.append(finding)
            claims.append({'claim_id': ident, 'report_anchor': 'R1', 'report_quote': finding['report_quote'], 'disposition': 'audited'})
        self.registry['claims'] = claims
        self.save_registry()
        self.assertEqual(self.validate(findings)['audited_claims'], 1100)
        findings[-1]['argument_audit']['claim_dependencies'] = ['CHAIN0']
        with self.assertRaisesRegex(ValueError, 'Circular'):
            self.validate(findings)

    def test_every_proof_requires_correspondence(self):
        self.finding['proofs'] = [{'module': 'Audit', 'theorem': 'total', 'target': '(1+2:Nat)=3', 'relation': 'supports'}]
        with self.assertRaisesRegex(ValueError, 'source-to-target correspondence'):
            self.validate()
        self.finding['formalization']['correspondence'] = [{'proof_ref': 0, 'explanation': 'The two supplied ledger amounts map to natural numbers one and two, added once.'}]
        self.validate()

    def test_evidence_reference_must_exist(self):
        self.finding['argument_audit']['evidence_refs'] = [8]
        with self.assertRaisesRegex(ValueError, 'invalid or duplicate reference'):
            self.validate()

    def test_initialize_preserves_unchanged_and_invalidates_changed_anchors(self):
        self.assertEqual(contracts.initialize(self.root), self.registry)
        self.write('input/report-ledger.json', {'R0': '# Report', 'R1': 'The total is four.', 'R2': 'New claim.'})
        updated = contracts.initialize(self.root)
        self.assertEqual(updated['anchors'][0]['classification'], 'non_claim')
        self.assertEqual(updated['anchors'][1]['classification'], 'pending')
        self.assertEqual(updated['anchors'][1]['previous_review']['classification'], 'claims')
        self.assertEqual(updated['anchors'][2]['classification'], 'pending')
        self.assertEqual(updated['claims'], self.registry['claims'])
        with self.assertRaisesRegex(ValueError, 'pending'):
            self.validate()

    def test_changed_anchor_without_initialize_is_rejected(self):
        self.write('input/report-ledger.json', {'R0': '# Report', 'R1': 'The total is three. A new extra assertion.'})
        with self.assertRaisesRegex(ValueError, 'report changed'):
            self.validate()

    def test_removed_anchor_review_is_retained(self):
        self.write('input/report-ledger.json', {'R1': 'The total is three. One plus two is three.'})
        updated = contracts.initialize(self.root)
        self.assertEqual(updated['retired_anchors'][0]['report_anchor'], 'R0')
        self.validate()

    def test_all_non_claim_report_has_valid_empty_registration(self):
        self.registry['anchors'][1].update(classification='non_claim', reason='Reviewer classifies this text as outside the audited report scope.')
        self.registry['claims'] = []
        self.save_registry()
        self.assertEqual(self.validate([])['coverage'], 'complete_registration')

    def test_source_lookup_callback(self):
        self.assertEqual(contracts.validate(self.root, [self.finding],
            source_lookup=lambda path, anchor: {'quote': 'The amounts are one and two.'})['audited_claims'], 1)


if __name__ == '__main__':
    unittest.main()
