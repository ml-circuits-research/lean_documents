"""Shared fixture-authoring helpers; never audit runtime or audit source material."""
from pathlib import Path
import json,hashlib
from fixture_formats import write_pdf,write_docx,write_scan_pdf
ROOT=Path(__file__).resolve().parents[1]
class Dossier:
 def __init__(self,slug):self.slug=slug;self.base=ROOT/slug;self.sources={};self.expect=[];self.reports=[];self.words=0
 def add(self,name,body,kind='md',**kwargs):
  path='sources/'+name;dest=self.base/path;dest.parent.mkdir(parents=True,exist_ok=True)
  if kind=='md':dest.write_text(body,encoding='utf-8');text=body
  else:
   {'pdf':write_pdf,'docx':write_docx,'scan':write_scan_pdf}[kind](dest,body,**kwargs)
   def flatten(x):return ' '.join(flatten(y) for y in x) if isinstance(x,list) else str(x)
   text=flatten(body)
  self.sources[path]=text;self.words+=len(text.split())
 def report(self,variant,rows):
  path='report-correct.md' if variant=='correct' else 'report.md';prefix='OK' if variant=='correct' else 'ERR'
  out=[f'# Synthetic supplied report: {self.slug} ({variant})','','Audit this supplied report independently against the source packet.','']
  for i,(claim,refs,semantic,disposition,rationale) in enumerate(rows,1):
   cid=f'C{self.slug[:2]}-{prefix}-{i:02d}';refs=['sources/'+r for r in refs]
   out.extend([f'<a id="{cid}"></a>',f'**{cid}.** {claim}','','Citations: '+'; '.join(refs)+'.',''])
   self.expect.append(dict(claim_id=cid,report_path=path,semantic_state=semantic,prospective_disposition=disposition,source_anchors=refs,rationale=rationale))
  (self.base/path).write_text('\n'.join(out),encoding='utf-8');self.reports.append(path)
 def finish(self,notes='',extra=None):
  brief='''# Synthetic supplied-report audit brief

[BR01] Audit exactly one supplied report against all source documents. The product audits findings in existing reports; it does not generate the original substantive report. The other report variant is excluded from the evidence for this audit. All organizations, names, transactions, devices, signatures, and events are invented.

[BR02] Use exact arithmetic, source-defined rules, identity, chronology, and explicitly bounded completeness. Preserve equal-authority evidence conflicts. Missing records establish a support gap unless an explicit complete domain supports a negative conclusion. A sufficient condition is not automatically necessary. Claims about recorded statements differ from claims about the underlying world.

[BR03] Each result must quote the exact claim, state its verification problem, cite original source files and stable bracket markers, identify applicable rules and assumptions, explain reasoning and limits, and explicitly explain a refutation. Native files are evidence; authoring scripts outside this dossier are not. Derived extraction IDs may aid navigation but must not replace original-path citations. Visually inspect uncertain scan fields and seek corroboration.

[BR04] Lean execution is authorized. A prospective result is not an executed result. Retain actual extraction, reviewed encoding, commands, exit statuses, and logs in distinct repository tmp/ directories for each report audit and reproduction. Formal results establish only their reviewed propositions under declared premises. Conflicting, unsupported, and subjective claims must preserve their non-proof dispositions.
'''
  (self.base/'brief.md').write_text(brief,encoding='utf-8')
  (self.base/'README.md').write_text(f'''# {self.slug}: synthetic dossier

This invented packet has {len(self.sources)} source files and approximately {self.words} source words before native rendering. It contains no real-world operational or safety advice.

Audit `report-correct.md` and `report.md` separately against `brief.md` and every file in `sources/`. Auditors receive the selected supplied report and all sources. Only evaluator expectations, stored outside this dossier, are withheld. Reports are objects of review, never source evidence for each other.

Native files use stable bracket markers. Cite the original file and marker, and preserve page or table context. Authoring material is outside the audit inputs under `examples/builders/`; it must not replace native extraction or OCR. The manifest hashes source, brief, and report bytes. README and manifest are entry metadata. Fixture preparation claims no executed Lean result.

{notes}
''',encoding='utf-8')
  entries=[dict(path=p,role='source' if p.startswith('sources/') else ('brief' if p=='brief.md' else 'report'),sha256=hashlib.sha256((self.base/p).read_bytes()).hexdigest()) for p in ['brief.md']+sorted(self.reports)+sorted(self.sources)]
  manifest=dict(schema_version=1,dossier_id=self.slug,synthetic=True,hash_algorithm='sha256',audit_inputs=entries,audit_variants=[dict(id='correct',report='report-correct.md'),dict(id='flawed',report='report.md')],selection_rule='Exactly one selected report with shared brief and all sources. Exclude authoring scripts and evaluator material.',source_count=len(self.sources),authored_source_word_count=self.words,formal_validation_executed_by_fixture_builder=False)
  (self.base/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
  ev=dict(schema_version=1,dossier_id=self.slug,classification='evaluator_only',status='unverified_expectations',warning='Author expectations only, not actual audits or executed Lean results. Withhold from blind reviewers.',expectations=self.expect)
  if extra:ev.update(extra)
  (ROOT/'evaluator'/f'{self.slug}.json').write_text(json.dumps(ev,indent=2)+'\n')
  print(self.slug,len(self.sources),'sources;',self.words,'source words;',len(self.expect),'claims')

def row(claim,refs,state='supported',disp='proof',why='Source-grounded bounded claim.'):
 return claim,refs,state,disp,why
