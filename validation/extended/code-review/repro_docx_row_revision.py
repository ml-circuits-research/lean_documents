from pathlib import Path
import sys,json,tempfile
from types import SimpleNamespace
REPO=Path('/home/salboaie/work/lean_documents')
sys.path.insert(0,str(REPO/'skills/evidence-to-proof-review/scripts'));sys.path.insert(0,str(REPO/'tests'))
import corpus
from test_extractors import write_docx
case=Path(tempfile.mkdtemp(prefix='docx-row-revision-',dir=REPO/'tmp/extension-code-review'))
brief=case/'brief.md';brief.write_text('Audit the supplied approval statement.')
report=case/'report.md';report.write_text('<a id="R1"></a>\nApproval was denied.')
source=case/'source.docx'
write_docx(source,'<w:tbl><w:tr><w:trPr><w:del w:id="1" w:author="Reviewer" w:date="2026-11-04T12:00:00Z"/></w:trPr><w:tc><w:p><w:r><w:t>Approval was denied.</w:t></w:r></w:p></w:tc></w:tr></w:tbl>')
root=Path(corpus.prepare(SimpleNamespace(brief=brief,report=report,sources=[source],temp_root=case/'runs',ocr_language='eng',extract_timeout=60,max_pages=None,max_documents=None,max_seconds=None))['workspace'])
path='input/sources/source.docx.md';anchor='docx-table-0001-r0001-c0001-p0001';seg=corpus.passage(root,path,anchor)
finding={'claim_id':'C1','evidence':[{'path':path,'anchor':anchor}], 'report_anchor':'R1','formal_status':'proved'}
try:corpus.assert_reviewable(root,[finding]);gate='accepted_without_source_review'
except ValueError as e:gate=str(e)
out={'workspace':str(root),'source_document':next(d for d in corpus.inventory(root) if d['logical']==path),'segment':seg,'formal_review_gate':gate}
(case/'result.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
