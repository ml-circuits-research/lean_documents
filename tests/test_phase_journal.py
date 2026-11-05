"""Behavioral checks for honest, append-only phase chronology."""
import importlib.util
import json
import contextlib
import io
import shlex
import sys
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('phase_journal', ROOT / 'skills/evidence-to-proof-review/scripts/journal.py')
journal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(journal)
RUN = ROOT / 'tmp'
RUN.mkdir(exist_ok=True)


class JournalTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix='phase-journal-tests-', dir=RUN))
        self.workspace = self.root / 'workspace'
        self.workspace.mkdir()
        (self.workspace / 'claims.json').write_text('original claims')

    def append(self, **kwargs):
        return journal.append(self.workspace, phase='claims', status='completed',
            title='Registered claims', description='Reviewed report and registered claims.',
            claim_ids=['C1'], inputs=['claims.json'], **kwargs)

    def test_real_snapshot_and_append_only_history(self):
        event = self.append()
        path = self.workspace / 'phases.jsonl'
        original = path.read_bytes()
        (self.workspace / 'claims.json').write_text('revised claims')
        self.append()
        self.assertTrue(path.read_bytes().startswith(original))
        result = journal.validate(self.workspace)
        self.assertEqual(result['status'], 'valid')
        self.assertEqual(result['events'], 2)
        self.assertEqual((self.workspace / event['inputs'][0]['snapshot']).read_text(), 'original claims')
        self.assertEqual(result['artifact_changes'][0]['recorded_sha256'], event['inputs'][0]['sha256'])

    def test_parent_root_paths_and_missing_history(self):
        self.assertEqual(journal.validate(self.workspace)['status'], 'legacy_unknown')
        event = self.append(journal_root=self.root)
        self.assertEqual(event['inputs'][0]['path'], 'workspace/claims.json')
        self.assertEqual(journal.validate(self.workspace, self.root)['artifact_changes'], [])
        self.assertFalse((self.workspace / 'phases.jsonl').exists())

    def test_missing_and_external_artifacts_do_not_create_events(self):
        for value in ('missing', '../outside.txt'):
            (self.root / 'outside.txt').write_text('external')
            with self.assertRaises((ValueError, OSError)):
                journal.append(self.workspace, phase='review', status='started', title='Review',
                    description='Actual review', inputs=[value])
        self.assertFalse((self.workspace / 'phases.jsonl').exists())

    def test_corrupt_history_cannot_be_extended(self):
        event = self.append()
        path = self.workspace / 'phases.jsonl'
        with path.open('a') as stream:
            stream.write(json.dumps(event) + '\n')
        before = path.read_bytes()
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            self.append()
        self.assertEqual(before, path.read_bytes())

    def test_unterminated_history_is_not_concatenated_or_rewritten(self):
        self.append()
        path = self.workspace / 'phases.jsonl'
        before = path.read_bytes().rstrip(b'\n')
        path.write_bytes(before)
        with self.assertRaisesRegex(ValueError, 'final newline'):
            self.append()
        self.assertEqual(path.read_bytes(), before)

    def test_symbolic_link_journal_is_rejected(self):
        target = self.root / 'other-journal.jsonl'
        target.write_text('')
        (self.workspace / 'phases.jsonl').symlink_to(target)
        with self.assertRaisesRegex(ValueError, 'symbolic link'):
            self.append()
        self.assertEqual(target.read_text(), '')

    def test_corrupt_snapshot_blocks_validation_and_append(self):
        event = self.append()
        snapshot = self.workspace / event['inputs'][0]['snapshot']
        snapshot.write_text('tampered')
        with self.assertRaisesRegex(ValueError, 'snapshot hash mismatch'):
            journal.validate(self.workspace)
        with self.assertRaises(ValueError):
            self.append()

    def test_old_events_without_snapshot_remain_valid_and_disclosed(self):
        event = self.append()
        del event['inputs'][0]['snapshot']
        (self.workspace / 'phases.jsonl').write_text(json.dumps(event) + '\n')
        result = journal.validate(self.workspace)
        self.assertEqual(result['status'], 'valid')
        self.assertEqual(len(result['unavailable_snapshots']), 1)

    def test_snapshot_symlink_cannot_write_outside_root(self):
        (self.workspace / 'phase-artifacts').symlink_to(self.root, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'symbolic link'):
            self.append()
        self.assertFalse((self.workspace / 'phases.jsonl').exists())

    def test_check_cli_links_generated_files_and_exact_invocation(self):
        spec = importlib.util.spec_from_file_location('phase_audit', ROOT / 'skills/evidence-to-proof-review/scripts/audit.py')
        audit = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(audit)
        def execute_check(args):
            for name, content in {
                'checks/Target001.lean': 'example : True := True.intro',
                'logs/target-001.log': 'Executed test check output',
                'logs/nested/build.log': 'Nested executed log',
                'proof-results.json': '{"status":"passed"}',
                'environment.lock': '{}',
                '.lake/cache.log': 'Excluded build cache',
            }.items():
                path = self.workspace / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
            return {'status': 'passed'}
        argv = ['check', '--workspace', str(self.workspace), '--lean', '/test tool/lean', '--journal-root', str(self.root)]
        with patch.object(audit, 'check', side_effect=execute_check), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(audit.main(argv), 0)
        events = [json.loads(line) for line in (self.root / 'phases.jsonl').read_text().splitlines()]
        expected = [sys.executable, str(Path(audit.__file__).resolve()), *argv]
        self.assertEqual([shlex.split(event['command']) for event in events], [expected, expected])
        outputs = {item['path']: item for item in events[-1]['outputs']}
        self.assertEqual(set(outputs), {'workspace/checks/Target001.lean', 'workspace/logs/target-001.log',
            'workspace/logs/nested/build.log', 'workspace/proof-results.json', 'workspace/environment.lock'})
        log = outputs['workspace/logs/target-001.log']
        self.assertEqual((self.root / log['snapshot']).read_text(), 'Executed test check output')

    def test_invalid_status_and_timezone_rejected(self):
        event = self.append()
        event['status'] = 'assumed_complete'
        with self.assertRaises(ValueError):
            journal.validate_event(event)
        event['status'] = 'note'
        event['timestamp'] = '2026-11-05T09:00:00'
        with self.assertRaises(ValueError):
            journal.validate_event(event)


class IndividualTraceTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix='claim-trace-tests-', dir=RUN))
        self.workspace = self.root / 'workspace'
        (self.workspace / 'input').mkdir(parents=True)
        (self.workspace / 'input/audit-policy.json').write_text(json.dumps({'require_claim_traces': True}))
        (self.workspace / 'source.txt').write_text('Supplied source evidence.')
        self.findings = [{'claim_id': 'C1', 'proofs': [], 'executive_summary': {
            'conclusion': 'The supplied record does not establish the claim.',
            'how_verified': 'Inspected the supplied record and checked the argument.',
            'limits': 'No completeness assumption is justified.'}}]

    def step(self, step, ident='C1', **kwargs):
        artifact = self.workspace / ident / (step + '.md')
        artifact.parent.mkdir(exist_ok=True)
        artifact.write_text(f'{ident}: actual {step} analysis and limitations.')
        return journal.append(self.workspace, journal_root=self.root, phase='evidence',
            status=kwargs.pop('status', 'completed'), title=step, description='Individual recorded work.',
            claim_ids=[ident], claim_step=step, inputs=['source.txt'],
            outputs=[artifact], result='Documentary assessment completed; source coverage remains limited.', **kwargs)

    def complete(self):
        for step in journal.CLAIM_STEPS:
            self.step(step)

    def validate(self):
        return journal.validate_claim_traces(self.workspace, self.findings, self.root)

    def test_individual_nonformal_trace_passes_without_lean_proof(self):
        self.complete()
        self.assertEqual(self.validate()['profile'], 'individual_claim_traces_v1')

    def test_shared_event_does_not_satisfy_individual_steps(self):
        journal.append(self.workspace, journal_root=self.root, phase='evidence', status='completed',
            title='Shared inspection', description='Shared inspection of all claims.', claim_ids=['C1', 'C2'])
        with self.assertRaisesRegex(ValueError, 'missing individually recorded registration'):
            self.validate()
        with self.assertRaisesRegex(ValueError, 'exactly one'):
            journal.append(self.workspace, phase='claims', status='started', title='Registration',
                description='Shared registration', claim_ids=['C1', 'C2'], claim_step='registration')

    def test_completed_step_requires_real_artifacts(self):
        with self.assertRaisesRegex(ValueError, 'snapshotted inputs and outputs'):
            journal.append(self.workspace, phase='claims', status='completed', title='Registration',
                description='No evidence provided', claim_ids=['C1'], claim_step='registration', result='Claimed success')

    def test_summary_and_changed_stage_recheck_enforced(self):
        self.complete()
        del self.findings[0]['executive_summary']
        with self.assertRaisesRegex(ValueError, 'executive_summary'):
            self.validate()
        self.findings[0]['executive_summary'] = {key: 'Explicit account.' for key in ('conclusion', 'how_verified', 'limits')}
        self.step('evidence')
        with self.assertRaisesRegex(ValueError, 'execution order'):
            self.validate()

    def test_blocked_documentary_step_is_disclosed_without_formal_success(self):
        for step in journal.CLAIM_STEPS:
            self.step(step, status='blocked' if step == 'verification' else 'completed')
        self.assertEqual(self.validate()['limitations'][0]['step'], 'verification')
        self.findings[0]['proofs'] = [{'theorem': 'Example'}]
        with self.assertRaisesRegex(ValueError, 'actual command and log'):
            self.validate()

    def test_formal_verification_requires_command_and_log(self):
        self.complete()
        self.findings[0]['proofs'] = [{'theorem': 'Example'}]
        with self.assertRaisesRegex(ValueError, 'actual command and log'):
            self.validate()

    def test_legacy_is_explicit_and_not_upgraded(self):
        (self.workspace / 'input/audit-policy.json').write_text('{}')
        self.assertEqual(self.validate()['profile'], 'legacy_unenforced')


if __name__ == '__main__':
    unittest.main()
