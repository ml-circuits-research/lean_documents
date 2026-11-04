"""Manual transcription provenance tests; all fixtures/logs are retained in tmp/."""
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
from types import SimpleNamespace
import unittest

REPO=Path(__file__).resolve().parents[1]
SCRIPTS=REPO/'skills/evidence-to-proof-review/scripts'
if str(SCRIPTS) not in sys.path:sys.path.insert(0,str(SCRIPTS))
import audit
import corpus
import corrections
from test_extractors import write_pdf
from contract_fixture import annotate_synthetic_finding, register_synthetic_report


class CorrectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        (REPO/'tmp').mkdir(exist_ok=True)
        cls.run_root=Path(tempfile.mkdtemp(prefix='correction-tests-',dir=REPO/'tmp'))
        print('\nCorrection test artifacts retained at '+str(cls.run_root),flush=True)

    def setUp(self):
        self.case=self.run_root/self._testMethodName;self.case.mkdir()
        self.brief=self.case/'brief.md';self.brief.write_text('Review the supplied time statement.\n')
        self.report=self.case/'report.md';self.report.write_text('<a id="R1"></a>\nThe recorded time is 14:38.\n')
        self.source=self.case/'source.md';self.source.write_text('<a id="S1"></a>\nThe machine transcription is 14:38.\n')
        self.manual=self.case/'manual.txt';self.manual.write_text('The reviewed transcription is 14:30.\n')
        self.root=Path(corpus.prepare(SimpleNamespace(brief=self.brief,report=self.report,sources=[self.source],temp_root=self.case/'runs',
            ocr_language='eng',extract_timeout=60,max_pages=None,max_documents=None,max_seconds=None))['workspace'])
        self.path='input/sources/source.md'
        self.reason='Synthetic unit fixture: test caller-attested correction provenance, not real-world source accuracy.'

    def apply(self,**updates):
        kwargs=dict(root=self.root,path=self.path,anchor='S1',text_file=self.manual,reviewer='Fixture reviewer',reason=self.reason)
        kwargs.update(updates);return corrections.transcribe(**kwargs)

    def finding(self,path=None,anchor='S1',quote='The machine transcription is 14:38.',formal=False):
        return dict(claim_id='C1',report_anchor='R1',report_quote='The recorded time is 14:38.',question='What time was transcribed?',
            evidence=[dict(path=path or self.path,anchor=anchor,quote=quote)],rules=['Compare source and report text.'],assumptions=[],
            reasoning=['This test exercises provenance, not the historical correctness of the timestamp.'],semantic_state='undetermined' if not formal else 'supported',
            argument_status='insufficient_support' if not formal else 'sufficient',formal_status='not_attempted' if not formal else 'proved',proofs=[],
            limits=['Synthetic fixture; no actual-world assurance.'],recommendation='Inspect the original before relying on the time.')

    def test_preserves_old_quote_source_bytes_and_raw_artifacts(self):
        old=corpus.passage(self.root,self.path,'S1')
        original=self.root/old['locator']['original'];original_bytes=original.read_bytes()
        artifact_lock=(self.root/'extraction-lock.json').read_bytes()
        derived_before=(self.root/self.path).read_bytes()
        result=self.apply()
        self.assertEqual(result['anchor'],'S1-reviewed-0001')
        self.assertEqual(corpus.passage(self.root,self.path,'S1'),old)
        corrected=corpus.passage(self.root,self.path,result['anchor'])
        self.assertEqual(corrected['quote'],'The reviewed transcription is 14:30.')
        self.assertEqual(corrected['method'],'manual-transcription')
        self.assertEqual(corrected['locator']['source_anchor'],'S1')
        self.assertEqual(corrected['locator']['start_line'],old['locator']['start_line'])
        self.assertEqual(original.read_bytes(),original_bytes)
        self.assertEqual((self.root/'extraction-lock.json').read_bytes(),artifact_lock)
        self.assertTrue((self.root/self.path).read_bytes().startswith(derived_before))
        self.assertEqual((self.root/result['transcription_snapshot']).read_bytes(),self.manual.read_bytes())
        corpus.verify(self.root)

    def test_new_literal_passage_is_indexed_and_review_gate_accepts_only_it(self):
        result=self.apply();new_anchor=result['anchor']
        matches=corpus.search(self.root,'reviewed')['results']
        self.assertTrue(any(m['anchor']==new_anchor for m in matches))
        segment=corpus.passage(self.root,self.path,new_anchor)
        f=self.finding(anchor=new_anchor,quote=segment['quote'],formal=True)
        corpus.assert_reviewable(self.root,[f])
        reviews=corpus.read(self.root/'extraction-review.json')['reviews']
        self.assertEqual(len(reviews),1)
        self.assertEqual(reviews[0]['anchor'],new_anchor)
        self.assertEqual(reviews[0]['source_sha256'],segment['locator']['original_sha256'])
        self.assertEqual(reviews[0]['segment_sha256'],hashlib.sha256(segment['quote'].encode()).hexdigest())
        self.assertEqual(result['proof_check_status'],'not_run')
        self.assertTrue(segment['uncertainty'])

    def test_multiple_transcriptions_get_distinct_stable_anchors(self):
        first=self.apply();self.manual.write_text('Second reviewed wording: 14:30.\n');second=self.apply()
        self.assertEqual(first['anchor'],'S1-reviewed-0001');self.assertEqual(second['anchor'],'S1-reviewed-0002')
        self.assertNotEqual(first['transcription_snapshot'],second['transcription_snapshot'])
        self.assertIn('The reviewed transcription',corpus.passage(self.root,self.path,first['anchor'])['quote'])
        actions=[json.loads(line) for line in (self.root/'manual-transcriptions.jsonl').read_text().splitlines()]
        self.assertEqual(len(actions),2)

    def test_prior_check_archived_and_stale_results_rejected(self):
        finding = annotate_synthetic_finding(self.finding())
        register_synthetic_report(self.root, [finding])
        corpus.save(self.root/'findings.json',[finding])
        audit.check(SimpleNamespace(workspace=self.root,lean='/unneeded/lean',timeout=60))
        old_proof=(self.root/'proof-results.json').read_bytes()
        old_manifest=corpus.sha(self.root/'manifest.json')
        result=self.apply()
        self.assertNotEqual(corpus.sha(self.root/'manifest.json'),old_manifest)
        self.assertFalse((self.root/'proof-results.json').exists())
        archived=self.root/result['history']/'proof-results.json'
        self.assertEqual(archived.read_bytes(),old_proof)
        # Even if the old result were placed back, its input fingerprint is stale.
        (self.root/'proof-results.json').write_bytes(old_proof)
        with self.assertRaises(audit.AuditError):audit.verified(self.root)

    def test_report_correction_retains_original_claim_and_parent_link(self):
        self.manual.write_text('The recorded time is 14:30.\n')
        result=self.apply(path='input/report.md',anchor='R1')
        ledger=corpus.read(self.root/'input/report-ledger.json')
        self.assertEqual(ledger['R1'],'The recorded time is 14:38.')
        self.assertEqual(ledger[result['anchor']],'The recorded time is 14:30.')
        segment=corpus.passage(self.root,'input/report.md',result['anchor'])
        self.assertEqual(segment['locator']['parent_report_anchor'],'R1')
        f=self.finding();f.update(report_anchor=result['anchor'],report_quote='The recorded time is 14:30.')
        annotate_synthetic_finding(f)
        register_synthetic_report(self.root, [f], deferred=[{
            'claim_id': 'C-original', 'report_anchor': 'R1', 'report_quote': 'The recorded time is 14:38.',
            'reason': 'The retained original statement is superseded by the reviewed transcription in this fixture.'}])
        corpus.save(self.root/'findings.json',[f])
        self.assertEqual(audit.findings(self.root)[0]['report_anchor'],result['anchor'])

    def test_empty_text_and_missing_attribution_fail_without_input_changes(self):
        original_manifest=corpus.sha(self.root/'manifest.json')
        for updates in ({'reason':''},{'reviewer':' '},{'anchor':'missing'},{'path':'../outside'}):
            with self.subTest(updates=updates),self.assertRaises(ValueError):self.apply(**updates)
            self.assertEqual(corpus.sha(self.root/'manifest.json'),original_manifest)
        self.manual.write_text(' \n\t')
        with self.assertRaisesRegex(ValueError,'must not be empty'):self.apply()
        self.assertEqual(corpus.sha(self.root/'manifest.json'),original_manifest)

    def test_missing_and_non_utf8_manual_files_rejected(self):
        with self.assertRaisesRegex(ValueError,'existing UTF-8'):self.apply(text_file=self.case/'missing.txt')
        self.manual.write_bytes(b'\xff\xfe')
        with self.assertRaisesRegex(ValueError,'valid UTF-8'):self.apply()

    def test_modified_corpus_cannot_be_blessed_by_transcription(self):
        (self.root/self.path).write_text('tampered derived text')
        with self.assertRaises(ValueError):self.apply()
        self.assertFalse((self.root/'manual-transcriptions.jsonl').exists())

    def test_pending_ingestion_is_not_implicitly_processed(self):
        pending=Path(corpus.prepare(SimpleNamespace(brief=self.brief,report=self.report,sources=[self.source],temp_root=self.case/'pending-runs',
            ocr_language='eng',extract_timeout=60,max_pages=None,max_documents=2,max_seconds=None))['workspace'])
        with self.assertRaisesRegex(ValueError,'Finish pending ingestion'):
            self.apply(root=pending,path='input/report.md',anchor='R1')
        self.assertEqual(corpus.inventory(pending)[-1]['status'],'pending')

    @unittest.skipUnless(shutil.which('pdftotext') and shutil.which('pdfinfo'),'Real PDF converters unavailable')
    def test_pdf_page_coordinates_retained_and_partial_status_not_promoted(self):
        pdf=self.case/'native.pdf';write_pdf(pdf,['The event time is 14:30.','Unprocessed second page.'])
        root=Path(corpus.prepare(SimpleNamespace(brief=self.brief,report=self.report,sources=[pdf],temp_root=self.case/'pdf-runs',
            ocr_language='eng',extract_timeout=60,max_pages=1,max_documents=None,max_seconds=None))['workspace'])
        path='input/sources/native.pdf.md';old=corpus.passage(root,path,'pdf-page-0001')
        self.manual.write_text('The event time is 14:30.\n')
        result=self.apply(root=root,path=path,anchor='pdf-page-0001',reason='Reviewed the generated fixture PDF; retained its accurate time wording.')
        new=corpus.passage(root,path,result['anchor'])
        self.assertEqual(new['locator']['page'],1)
        self.assertEqual(new['locator']['words'],old['locator']['words'])
        self.assertEqual(result['document_status'],'partial')
        doc=next(d for d in corpus.inventory(root) if d['logical']==path)
        self.assertEqual(doc['status'],'partial')
        f=self.finding(path=path,anchor=result['anchor'],quote=new['quote'],formal=True)
        with self.assertRaisesRegex(ValueError,'Incomplete ingestion'):corpus.assert_reviewable(root,[f])
        corpus.save(root/'coverage-acknowledgement.json',{'documents':[{'document_id':doc['id'],'reason':'Second page remains outside this test batch.','impact':'No claim about second-page contents is made.'}]})
        corpus.assert_reviewable(root,[f])


if __name__=='__main__':unittest.main()
