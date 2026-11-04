from pathlib import Path
import sys,json,tempfile
from types import SimpleNamespace
REPO=Path('/home/salboaie/work/lean_documents')
sys.path.insert(0,str(REPO/'skills/evidence-to-proof-review/scripts'))
sys.path.insert(0,str(REPO/'tests'))
import corpus,corrections
from test_extractors import write_pdf
case=Path(tempfile.mkdtemp(prefix='manual-retry-',dir=REPO/'tmp/extension-code-review'))
brief=case/'brief.md';brief.write_text('Audit the supplied statement.')
report=case/'report.md';report.write_text('<a id="R1"></a>\nThe value is three.')
source=case/'source.pdf';write_pdf(source,['The value is three.','A second source page.'])
manual=case/'manual.txt';manual.write_text('The visually reviewed value is three.\n')
root=Path(corpus.prepare(SimpleNamespace(brief=brief,report=report,sources=[source],temp_root=case/'runs',ocr_language='eng',extract_timeout=60,max_pages=1,max_documents=None,max_seconds=None))['workspace'])
path='input/sources/source.pdf.md'
result=corrections.transcribe(root,path,'pdf-page-0001',manual,'Independent test reviewer','Synthetic fixture manual-transcription retention check.')
assert corpus.passage(root,path,result['anchor'])
before=(root/path).read_text()
resumed=corpus.resume(root,retry=True,max_pages=2)
after=corpus.passage(root,path,result['anchor'])
corpus.verify(root)
report={'workspace':str(root),'manual_anchor':result['anchor'],'before_present':result['anchor'] in before,'after_passage':after,'after_derived_present':result['anchor'] in (root/path).read_text(),'manual_snapshot_retained':(root/result['transcription_snapshot']).exists(),'complete':resumed['coverage']['complete'],'search_manual_text':corpus.search(root,'visually')['total_matching_chunks']}
(case/'result.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
