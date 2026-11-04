"""Behavioral tests for controlled agent extraction; artifacts retained in tmp/."""
import hashlib
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest import mock

REPO=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'skills/evidence-to-proof-review/scripts'))
import agent_extraction
import corpus


class AgentExtractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        (REPO/'tmp').mkdir(exist_ok=True)
        cls.retained=Path(tempfile.mkdtemp(prefix='agent-extraction-tests-',dir=REPO/'tmp'))
        print('\nAgent extraction test artifacts retained at '+str(cls.retained),flush=True)

    def setUp(self):
        self.case=self.retained/self._testMethodName;self.case.mkdir()
        self.report=self.case/'report.html';self.report.write_text('<p>Total is 3.</p>')
        self.source=self.case/'source.unknown';self.source.write_text('<p>Amount: 3.</p>')
        with mock.patch('extractors.shutil.which',return_value=None):
            self.root=Path(corpus.prepare(SimpleNamespace(report=self.report,sources=[self.source],
                temp_root=self.case/'runs',lean_version='4.25.1'))['workspace'])
        self.docs={d['role']:d for d in corpus.inventory(self.root)}

    def bundle(self,role='source',**changes):
        value={'schema_version':1,'original_sha256':self.docs[role]['original_sha'],
            'method':{'name':'agent-transcription','description':'Fixture declares visible paragraph transcription.'},
            'tool':{'name':'fixture-reader','version':'1'},'reviewer':'Fixture extraction author',
            'coverage':{'status':'complete','scope':'The single supplied paragraph.',
                        'limitations':['Synthetic fixture; no real source authenticity established.']},
            'segments':[{'anchor':'R1' if role=='report' else 'S1',
                         'quote':'Total is 3.' if role=='report' else 'Amount: 3.',
                         'locator':{'kind':'section','section':'First paragraph'},'uncertainty':[]}]}
        value.update(changes);return value

    def apply(self,role='source',value=None):
        path=self.case/('bundle-'+role+'.json');corpus.save(path,value or self.bundle(role))
        return agent_extraction.import_extraction(self.root,self.docs[role]['id'],path)

    def ready(self):
        self.apply();self.apply('report')
        corpus.save(self.root/'revision-review.json',{'revision_manifest_sha256':corpus.sha(self.root/'manifest.json'),
                    'reviewed_claims':[]})

    def finding(self):
        return {'claim_id':'C1','report_anchor':'R1','formal_status':'proved',
                'evidence':[{'path':self.docs['source']['logical'],'anchor':'S1'}]}

    def accept(self,role,anchor):
        seg=corpus.passage(self.root,self.docs[role]['logical'],anchor)
        path=self.root/'extraction-review.json'
        reviews=corpus.read(path) if path.exists() else {'reviews':[]}
        reviews['reviews'].append({'path':self.docs[role]['logical'],'anchor':anchor,'decision':'accepted',
            'reviewer':'Fixture material reviewer','reason':'Fixture attestation of original paragraph inspection.',
            'source_sha256':seg['locator']['original_sha256'],
            'segment_sha256':hashlib.sha256(seg['quote'].encode()).hexdigest()})
        corpus.save(path,reviews)

    def test_blocked_source_and_report_import_preserves_originals_and_attempts(self):
        self.assertTrue(all(d['status']=='blocked' for d in self.docs.values()))
        originals={d['original']:(self.root/d['original']).read_bytes() for d in self.docs.values()}
        prior=corpus.read(self.root/'extraction-lock.json')['files']
        self.ready()
        for path,raw in originals.items():self.assertEqual((self.root/path).read_bytes(),raw)
        for path,digest in prior.items():self.assertEqual(corpus.sha(self.root/path),digest)
        self.assertEqual(corpus.read(self.root/'input/report-ledger.json'),{'R1':'Total is 3.'})
        self.assertEqual(corpus.read(self.root/'claims.json')['anchors'][0]['classification'],'pending')
        self.assertTrue(corpus.search(self.root,'Amount')['results'])
        self.assertTrue(corpus.read(self.root/'ingestion.json')['complete'])
        corpus.verify(self.root)

    def test_sha_duplicate_anchors_unsafe_paths_and_coordinates_rejected_without_mutation(self):
        baseline=corpus.sha(self.root/'manifest.json')
        bad=[]
        value=self.bundle();value['original_sha256']='0'*64;bad.append(value)
        value=self.bundle();value['segments']*=2;bad.append(value)
        value=self.bundle();value['segments'][0]['anchor']='../../escape';bad.append(value)
        value=self.bundle();value['segments'][0]['locator']={'kind':'page','page':0};bad.append(value)
        value=self.bundle();value['segments'][0]['locator']={'kind':'section','section':''};bad.append(value)
        value=self.bundle();value['tool']['command']='touch /tmp/never';bad.append(value)
        value=self.bundle();value['segments'][0]['quote']=' ';bad.append(value)
        for value in bad:
            with self.subTest(value=value),self.assertRaises(ValueError):self.apply(value=value)
            self.assertEqual(corpus.sha(self.root/'manifest.json'),baseline)
            corpus.verify(self.root)

    def test_uncertainty_requires_both_report_and_source_material_review(self):
        self.ready();finding=self.finding()
        with self.assertRaisesRegex(ValueError,'uncertain extraction'):corpus.assert_reviewable(self.root,[finding])
        self.accept('source','S1')
        with self.assertRaisesRegex(ValueError,'uncertain extraction'):corpus.assert_reviewable(self.root,[finding])
        self.accept('report','R1');corpus.assert_reviewable(self.root,[finding])
        seg=corpus.passage(self.root,self.docs['source']['logical'],'S1')
        self.assertTrue(seg['uncertainty'])

    def test_uncertain_argument_items_and_auxiliary_evidence_require_review(self):
        self.ready();self.accept('source','S1')
        finding=self.finding();finding.update(formal_status='auxiliary',proofs=[{'proof':'fixture'}],
            argument_audit={'report_items':[{'report_anchor':'R1','proof_refs':[0]}]})
        with self.assertRaisesRegex(ValueError,'uncertain extraction'):corpus.assert_reviewable(self.root,[finding])
        self.accept('report','R1');corpus.assert_reviewable(self.root,[finding])
        (self.root/'extraction-review.json').unlink()
        finding['argument_audit']['report_items']=[]
        with self.assertRaisesRegex(ValueError,'uncertain extraction'):corpus.assert_reviewable(self.root,[finding])

    def test_import_does_not_process_other_pending_documents(self):
        with corpus.connection(self.root,True) as db:
            db.execute("UPDATE documents SET status='pending' WHERE role='report'")
        corpus.manifest(self.root)
        result=self.apply()
        self.assertEqual(result['coverage']['processed_this_batch'],[self.docs['source']['id']])
        self.assertEqual(next(d for d in corpus.inventory(self.root) if d['role']=='report')['status'],'pending')
        corpus.verify(self.root)

    def test_partial_coverage_persists_through_retry_and_identical_import_is_noop(self):
        value=self.bundle();value['coverage']['status']='partial'
        first=self.apply(value=value);manifest=corpus.sha(self.root/'manifest.json')
        lock=corpus.sha(self.root/'extraction-lock.json')
        result=self.apply(value=value)
        self.assertFalse(result['changed'])
        self.assertEqual(corpus.sha(self.root/'manifest.json'),manifest)
        self.assertEqual(corpus.sha(self.root/'extraction-lock.json'),lock)
        corpus.resume(self.root,retry=True)
        self.assertEqual(corpus.passage(self.root,self.docs['source']['logical'],'S1')['quote'],'Amount: 3.')
        imported=next(d for d in corpus.inventory(self.root) if d['role']=='source')
        self.assertEqual(imported['status'],'partial')
        self.assertTrue((self.root/first['extraction_bundle']).exists())
        corpus.verify(self.root)

    def test_changed_report_invalidates_claims_reviews_and_proofs_keeps_history(self):
        self.ready();self.accept('source','S1');self.accept('report','R1')
        registry=corpus.read(self.root/'claims.json');registry['anchors'][0].update(classification='claims',reason='Fixture review')
        corpus.save(self.root/'claims.json',registry)
        corpus.save(self.root/'findings.json',[self.finding(),{'claim_id':'C2'}])
        for name in ('proof-results.json','semantic-review.md','environment.lock'):(self.root/name).write_text('old result')
        value=self.bundle('report');value['segments'][0]['quote']='Total is 4.'
        result=self.apply('report',value)
        self.assertEqual(corpus.read(self.root/'claims.json')['anchors'][0]['classification'],'pending')
        self.assertEqual(corpus.read(self.root/'invalidation.json')['affected_claims'],['C1','C2'])
        self.assertFalse((self.root/'extraction-review.json').exists())
        for name in ('proof-results.json','semantic-review.md','environment.lock'):
            self.assertFalse((self.root/name).exists());self.assertEqual((self.root/result['history']/name).read_text(),'old result')
        self.assertIn('Total is 3.',(self.root/result['history']/'prior-derived-text.md').read_text())
        self.assertFalse(corpus.search(self.root,'"Total is 3"')['results'])
        self.assertTrue(corpus.search(self.root,'"Total is 4"')['results'])
        corpus.verify(self.root)

    def test_identical_original_refresh_preserves_complete_and_partial_imports(self):
        self.apply('report')
        for coverage,expected in (('complete','ready'),('partial','partial')):
            with self.subTest(coverage=coverage):
                value=self.bundle();value['coverage']['status']=coverage
                imported=self.apply(value=value)
                before=corpus.passage(self.root,self.docs['source']['logical'],'S1')
                corpus.save(self.root/'proof-results.json',{'fixture':'prior success to invalidate'})
                replacement=self.case/(coverage+'.unknown')
                replacement.write_bytes(self.source.read_bytes())
                result=corpus.refresh(self.root,self.docs['source']['id'],replacement)
                revised=Path(result['workspace'])
                self.assertNotEqual(revised,self.root)
                for operation in ('refresh','retry','reimport'):
                    if operation=='retry':corpus.resume(revised,retry=True)
                    if operation=='reimport':
                        repeated=agent_extraction.import_extraction(revised,self.docs['source']['id'],self.case/'bundle-source.json')
                        self.assertFalse(repeated['changed'])
                    document=next(d for d in corpus.inventory(revised) if d['role']=='source')
                    self.assertEqual(document['status'],expected,operation)
                    self.assertEqual(corpus.read(revised/'ingestion.json')['complete'],coverage=='complete',operation)
                    self.assertEqual(corpus.passage(revised,self.docs['source']['logical'],'S1'),before)
                    self.assertEqual((revised/document['original']).read_bytes(),self.source.read_bytes())
                    corpus.verify(revised)
                self.assertTrue((revised/imported['extraction_bundle']).exists())
                self.assertFalse((revised/'proof-results.json').exists())
                self.assertTrue((revised/'history/parent/proof-results.json').exists())
                self.assertEqual(corpus.read(revised/'invalidation.json')['technical_results'],'all invalidated')

    def test_changed_original_does_not_retain_imported_projection(self):
        self.ready();replacement=self.case/'replacement.unknown';replacement.write_text('New unhandled bytes')
        revised=Path(corpus.refresh(self.root,self.docs['source']['id'],replacement)['workspace'])
        self.assertIsNone(corpus.passage(revised,self.docs['source']['logical'],'S1'))
        self.assertEqual(next(d for d in corpus.inventory(revised) if d['role']=='source')['status'],'blocked')
        self.assertIsNotNone(corpus.passage(self.root,self.docs['source']['logical'],'S1'))

    def test_per_run_stable_lean_policy(self):
        self.assertEqual(corpus.read(self.root/'input/audit-policy.json')['lean_version'],'4.25.1')
        self.assertEqual(corpus.read(self.root/'run.json')['lean_version'],'4.25.1')
        for version in ('3.4.0','4.24.0-rc1','4.024.0','4.24.0/../../x'):
            with self.assertRaises(ValueError):corpus.prepare(SimpleNamespace(lean_version=version))


if __name__=='__main__':unittest.main()
