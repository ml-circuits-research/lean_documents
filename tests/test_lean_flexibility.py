"""Executed coverage for version pins, reviewed reusable modules, and Lean literals."""
from pathlib import Path
import shutil
from types import SimpleNamespace
import unittest

import test_audit as fixture

audit = fixture.audit
LEAN = fixture.LEAN


class LeanFlexibilityTests(unittest.TestCase):
    setUp = fixture.AuditTests.setUp
    save = fixture.AuditTests.save
    check = fixture.AuditTests.check

    def selected_workspace(self, version):
        previous = self.root
        self.root = Path(audit.prepare(SimpleNamespace(
            report=self.base / 'report.md', sources=[self.base / 'sources'],
            temp_root=self.base, lean_version=version))['workspace'])
        for name in ('claims.json', 'findings.json', 'review-plan.md', 'semantic-review.md', 'model-notes.md'):
            shutil.copyfile(previous / name, self.root / name)
        shutil.copyfile(previous / 'models/Audit.lean', self.root / 'models/Audit.lean')

    def test_selected_version_is_manifest_bound(self):
        self.selected_workspace('4.25.0')
        policy_path = self.root / 'input/audit-policy.json'
        policy = audit.read_json(policy_path)
        self.assertEqual(policy['lean_version'], '4.25.0')
        self.assertEqual(audit.read_json(self.root / 'run.json')['lean_version'], '4.25.0')
        self.assertEqual(audit.required_lean_version(self.root), '4.25.0')
        policy['lean_version'] = '4.24.0'
        audit.write_json(policy_path, policy)
        with self.assertRaisesRegex(audit.AuditError, 'hash mismatch'):
            self.check()

    def test_stable_lean4_versions_only(self):
        for version in ('3.51.1', '4.24.0-rc1', 'nightly', '4.24', '4.024.0', '4.24.0\n', '../4.24.0', None):
            with self.subTest(version=version), self.assertRaises(audit.AuditError):
                audit.validate_lean_version(version)
        self.assertEqual(audit.validate_lean_version('4.0.0'), '4.0.0')

    def test_legacy_policy_defaults_to_existing_version(self):
        policy_path = self.root / 'input/audit-policy.json'
        policy = audit.read_json(policy_path)
        policy.pop('lean_version')
        audit.write_json(policy_path, policy)
        self.assertEqual(audit.required_lean_version(self.root), '4.24.0')
        policy_path.unlink()
        self.assertEqual(audit.required_lean_version(self.root), '4.24.0')

    @unittest.skipUnless(Path(LEAN).is_file(), 'Lean executable unavailable')
    def test_real_version_mismatch_records_both_versions(self):
        self.selected_workspace('4.25.0')
        with self.assertRaisesRegex(audit.AuditError, 'Lean 4.25.0 required'):
            self.check()
        result = audit.read_json(self.root / 'proof-results.json')
        lock = audit.read_json(self.root / 'environment.lock')
        for record in (result, lock):
            self.assertEqual(record['lean_version_required'], '4.25.0')
            self.assertIn('4.24.0', record['lean_version_observed'])
            self.assertEqual(record['execution_status'], 'version_mismatch')
        self.assertFalse((self.root / 'logs/lake-build.log').exists())

    def reusable_models(self):
        (self.root / 'models/Audit.lean').unlink()
        (self.root / 'models/domain').mkdir()
        (self.root / 'models/Helpers.lean').write_text(
            'import Std\nnamespace Helpers\ntheorem one : (1 : Nat) = 1 := rfl\nend Helpers\n')
        (self.root / 'models/domain/Data.lean').write_text('def secondAmount : Nat := 2\n')
        (self.root / 'models/domain/Totals.lean').write_text(
            'import\n  Helpers\nimport domain.Data\nnamespace Audit\n'
            'theorem total : (1 + secondAmount : Nat) = 3 := by decide\nend Audit\n')
        self.finding['proofs'][0]['module'] = 'domain.Totals'
        self.save()

    @unittest.skipUnless(Path(LEAN).is_file(), 'Lean executable unavailable')
    def test_reused_nested_modules_build_and_every_theorem_is_audited(self):
        self.reusable_models()
        result = self.check()
        self.assertEqual(result['status'], 'passed')
        self.assertEqual(len(result['targets']), 3)
        self.assertTrue(any(t['module'] == 'Helpers' and t['target'] is None for t in result['targets']))
        self.assertIn('models/domain/Data.lean', result['input_hashes'])
        self.assertIn('models/domain/Totals.lean', result['input_hashes'])
        audit.render(SimpleNamespace(workspace=self.root))
        self.assertIn('(models/domain/Totals.lean)', (self.root / 'audit-report.md').read_text())
        (self.root / 'models/domain/Data.lean').write_text('def secondAmount : Nat := 7\n')
        with self.assertRaisesRegex(audit.AuditError, 'No successful proof check'):
            audit.render(SimpleNamespace(workspace=self.root))

    @unittest.skipUnless(Path(LEAN).is_file(), 'Lean executable unavailable')
    def test_reused_module_wrong_target_still_fails(self):
        self.reusable_models()
        self.finding['proofs'][0]['target'] = '(1 + 2 : Nat) = 4'
        self.save()
        with self.assertRaisesRegex(audit.AuditError, 'Lean command failed'):
            self.check()
        self.assertIn('type mismatch', (self.root / 'logs/target-003.log').read_text().lower())

    @unittest.skipUnless(Path(LEAN).is_file(), 'Lean executable unavailable')
    def test_unreferenced_nested_theorem_still_gets_actual_axiom_audit(self):
        (self.root / 'models/Hidden').mkdir()
        (self.root / 'models/Hidden/Bypass.lean').write_text(
            'theorem fabricated : False := sorryAx False true\n')
        with self.assertRaisesRegex(audit.AuditError, 'Unapproved axioms.*sorryAx'):
            self.check()
        result = audit.read_json(self.root / 'proof-results.json')
        self.assertEqual(result['status'], 'failed')
        self.assertIn('sorryAx', (self.root / 'logs/target-002.log').read_text())
        with self.assertRaises(audit.AuditError):
            audit.render(SimpleNamespace(workspace=self.root))

    def test_recursive_unreferenced_dangerous_model_is_rejected(self):
        (self.root / 'models/Hidden').mkdir()
        (self.root / 'models/Hidden/Bad.lean').write_text('axiom unreviewed : False\n')
        with self.assertRaisesRegex(audit.AuditError, 'Forbidden'):
            self.check('/missing/lean')

    def test_escaping_symlinks_and_unreviewed_objects_are_rejected(self):
        external = self.base / 'Outside.lean'
        external.write_text('theorem hidden : True := by trivial\n')
        symlink = self.root / 'models/Outside.lean'
        symlink.symlink_to(external)
        with self.assertRaisesRegex(audit.AuditError, 'symlink escapes'):
            self.check('/missing/lean')
        symlink.unlink()
        (self.root / 'models/Cache.olean').write_bytes(b'unreviewed')
        with self.assertRaisesRegex(audit.AuditError, 'Unreviewed compiled'):
            self.check('/missing/lean')

    def test_external_multiline_import_and_reserved_shadow_rejected(self):
        (self.root / 'models/Audit.lean').write_text('import\nMathlib\n')
        with self.assertRaisesRegex(audit.AuditError, 'Only Init/Std'):
            self.check('/missing/lean')
        (self.root / 'models/Std.lean').write_text('def forged := 1\n')
        with self.assertRaisesRegex(audit.AuditError, 'shadow'):
            self.check('/missing/lean')

    @unittest.skipUnless(Path(LEAN).is_file(), 'Lean executable unavailable')
    def test_string_character_and_raw_literals_are_data(self):
        target = '(1 + 2 : Nat) = 3 ∧ "opaque # /- -- := by axiom" = "opaque # /- -- := by axiom"'
        self.finding['proofs'][0]['target'] = target
        self.save()
        (self.root / 'models/Audit.lean').write_text(
            'import Std\n/- Outer /- nested sorry -/ comment -/\n'
            'def quoted : String := "opaque # -- /- \\" sorry \\""\n'
            'def rawQuoted : String := r#"opaque # -- /- \\" sorry"#\n'
            "def character : Char := '#'\n"
            'namespace Audit\ntheorem total : ' + target + ' := by constructor <;> decide\nend Audit\n')
        result = self.check()
        self.assertEqual(result['status'], 'passed')
        self.assertEqual(result['lean_version_required'], '4.24.0')

    def test_dangerous_tokens_after_string_and_nested_comment_remain_rejected(self):
        for literal in ('"/-"', '"--"', '"#"', 'r#"/-"#'):
            with self.subTest(literal=literal):
                (self.root / 'models/Audit.lean').write_text(
                    f'def text : String := {literal}\n/- Outer /- inner -/ outer -/\naxiom hidden : False\n')
                with self.assertRaisesRegex(audit.AuditError, 'Forbidden'):
                    self.check('/missing/lean')


if __name__ == '__main__':
    unittest.main()
