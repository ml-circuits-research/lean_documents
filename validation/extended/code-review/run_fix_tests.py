from pathlib import Path
import sys,unittest,tempfile,json
REPO=Path('/home/salboaie/work/lean_documents');BASE=REPO/'tmp/extension-code-review'
sys.path.insert(0,str(REPO/'tests'))
import test_corpus
names=['test_pdf_retry_preserves_reviewed_overlays_and_invalidates_old_check','test_retry_rejects_manual_anchor_collision_without_overwriting_passage','test_refresh_changed_original_does_not_reapply_manual_overlay','test_page_limited_pdf_retry_retains_old_attempt_and_original','test_noop_resume_preserves_successful_proof_fingerprint','test_refresh_archives_actual_proofs_and_stale_quote_cannot_pass','test_interrupted_derived_state_requires_explicit_recovery']
def setup(cls):cls.retained_root=Path(tempfile.mkdtemp(prefix='fix-regressions-',dir=BASE))
test_corpus.CorpusTests.setUpClass=classmethod(setup)
with (BASE/'fix-tests.log').open('w') as log:
 result=unittest.TextTestRunner(stream=log,verbosity=2).run(unittest.TestSuite(test_corpus.CorpusTests(n) for n in names))
summary={'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'skips':len(result.skipped)}
(BASE/'fix-tests-result.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
sys.exit(not result.wasSuccessful())
