from pathlib import Path
import os,sys,unittest,tempfile,json
REPO=Path('/home/salboaie/work/lean_documents');BASE=REPO/'tmp/extension-code-review'
LEAN=Path.home()/'.local/share/evidence-to-proof/toolchains/lean-4.24.0-linux/bin/lean'
os.environ['AUDIT_TEST_LEAN']=str(LEAN)
sys.path.insert(0,str(REPO/'tests'))
import test_corpus,test_extractors,test_corrections,test_audit
# Tests retain all artifacts. Move only newly allocated test roots under this review.
test_audit.TEST_RUN=Path(tempfile.mkdtemp(prefix='audit-regressions-',dir=BASE))
def corpus_setup(cls):
 cls.retained_root=Path(tempfile.mkdtemp(prefix='corpus-regressions-',dir=BASE))
def extractor_setup(cls):
 cls.run_root=Path(tempfile.mkdtemp(prefix='extractor-regressions-',dir=BASE))
def correction_setup(cls):
 cls.run_root=Path(tempfile.mkdtemp(prefix='correction-regressions-',dir=BASE))
test_corpus.CorpusTests.setUpClass=classmethod(corpus_setup)
test_extractors.ExtractorTests.setUpClass=classmethod(extractor_setup)
test_corrections.CorrectionTests.setUpClass=classmethod(correction_setup)
selection={test_corpus.CorpusTests:[
 'test_bounded_ingestion_resumes_all_documents','test_tampered_extraction_blocks_audit_integration','test_missing_extraction_lock_cannot_disable_integrity','test_incomplete_ingestion_requires_explicit_accounting','test_uncertain_source_formal_gate_bound_to_original_hash','test_uncertain_report_claim_requires_original_review','test_refresh_missing_dependency_map_invalidates_all_claims','test_dependency_map_omitting_explicit_evidence_falls_back'],
 test_extractors.ExtractorTests:['test_docx_tracked_changes_and_objects_mark_partial','test_synthetic_low_confidence_tsv_is_partial','test_real_pdf_page_limit_is_partial'],
 test_corrections.CorrectionTests:['test_prior_check_archived_and_stale_results_rejected','test_report_correction_retains_original_claim_and_parent_link'],
 test_audit.AuditTests:['test_failed_optional_replay_is_recorded_as_failed_and_blocks_delivery','test_real_lean_check_render_export_and_stale_proof']}
suite=unittest.TestSuite(cls(name) for cls,names in selection.items() for name in names)
with (BASE/'selected-tests.log').open('w') as log:
 result=unittest.TextTestRunner(stream=log,verbosity=2).run(suite)
summary={'run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'skips':len(result.skipped),'lean':str(LEAN)}
(BASE/'selected-tests-result.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
sys.exit(not result.wasSuccessful())
