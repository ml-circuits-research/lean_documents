"""Build deterministic synthetic native sources; masters never enter evidence inputs."""
from pathlib import Path
import hashlib,json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'builders'))
from fixture_formats import write_docx,write_pdf,write_scan_pdf
S=ROOT/'sources'; S.mkdir(exist_ok=True)
M=ROOT/'masters'; M.mkdir(exist_ok=True)
R=ROOT/'revisions'; R.mkdir(exist_ok=True)
policy=[
'Cedar laboratory transfer policy P1. Effective 4 November 2026. All entities and events are synthetic.',
'P1: For transfer T7 on 4 November 2026, count the three ledger charges A, B and C once each, in whole credits. No tax, discount or currency conversion applies. A revised ledger explicitly supersedes the prior ledger for this transfer.',
'P2: Each individual charge must be at most 50 credits. A charge above 50 breaches the individual-charge cap; aggregate totals do not replace this test.',
'P3: T7 receipt is timely if the physical receipt timestamp is no later than 16:30 local time on 4 November 2026. No grace period applies. Dispatch time is irrelevant.',
'P4: T7 release eligibility requires both quality approval and security approval by 17:00 local time. Quality approval alone is insufficient. A missing security-status field is not a statement that no approval event occurred.',
'P5: This package contains no definition or grading scale for the adjective exemplary. The package is complete only for charges A, B and C; it is not a complete approval-event history.'
]
write_docx(S/'01-policy.docx',policy)
(M/'policy.txt').write_text('\n\n'.join(policy)+'\n')
for revision,c in [(1,20),(2,45)]:
    text=f'''Cedar laboratory T7 charge and quality ledger - revision {revision}
Transfer date: 4 November 2026. Unit: whole credits.
Charge A: 60 credits.
Charge B: 40 credits.
Charge C: {c} credits.
This is the complete charge list for transfer T7. Count each line once.
Quality approval: granted at 16:00 local time on 4 November 2026.
Security approval status: not supplied. This ledger is not an approval-event history.
'''
    if revision==2:text+='Revision 2 supersedes revision 1 for T7. Charge C is corrected from 20 to 45 credits. All other fields remain unchanged.\n'
    (M/f'ledger-r{revision}.txt').write_text(text)
    write_pdf(S/'02-ledger.pdf' if revision==1 else R/'02-ledger-r2.pdf',[text])
scan='''CEDAR LABORATORY - PHYSICAL RECEIPT
Transfer: T7
Receipt date: 4 November 2026
Physical receipt time: 16:40 local time
Dispatch time: 16:10 local time
Recorded by: Receiving desk
This receipt records physical arrival only.
It does not record quality or security approval.'''
(M/'receipt.txt').write_text(scan+'\n')
write_scan_pdf(S/'03-receipt-scan.pdf',[scan])
bad=[
('The total T7 charge is 130 credits.','The ledger lists A as 60, B as 40 and C as 20 credits; adding those lines gives 130 credits.'),
('Charge A complies with the individual-charge cap.','Policy P2 sets the cap at 50 credits, and the ledger records A as 60 credits.'),
('The physical receipt occurred at 16:40 local time on 4 November 2026.','The physical receipt scan records that timestamp for T7.'),
('The physical receipt was timely under policy P3.','The applicable receipt deadline was 17:00, and the receipt scan records 16:40.'),
('T7 release eligibility is established.','The ledger records quality approval at 16:00; quality approval alone establishes release eligibility.'),
('Charge B is 40 credits.',''),
('The handover was exemplary.','No grading criterion is offered for this evaluation.')]
good=[
('The total T7 charge is 120 credits.','The ledger lists A as 60, B as 40 and C as 20 credits; adding those lines gives 120 credits.'),
('Charge A breaches the individual-charge cap.','Policy P2 sets the cap at 50 credits, and the ledger records A as 60 credits.'),
('The physical receipt occurred at 16:40 local time on 4 November 2026.','The physical receipt scan records that timestamp for T7.'),
('The physical receipt missed the policy P3 deadline.','Policy P3 sets the receipt deadline at 16:30; the receipt scan records 16:40.'),
('The supplied records do not establish T7 release eligibility.','Policy P4 requires quality and security approvals; the ledger records quality approval but supplies no security status, and the receipt records arrival only. This does not establish that security approval never occurred.'),
('Charge B is 40 credits.',''),
('The supplied package provides no grading criterion for calling the handover exemplary.','Policy P5 expressly states that no such definition or scale is supplied; no exemplary grade is inferred.')]
for name,rows in [('report.md',bad),('report-correct.md',good)]:
    (ROOT/name).write_text('# T7 transfer review\n\n'+ '\n\n'.join(f'<a id="R{i}"></a>\n{claim}'+(' '+arg if arg else '') for i,(claim,arg) in enumerate(rows,1))+'\n')
manifest={'fixture_id':'15-native-revision','synthetic':True,'brief':'not supplied; infer criteria','source_revision_initial':1,'revision_replacement':'revisions/02-ledger-r2.pdf','authoring':'Nonblind fixture construction; execution recorded separately.','files':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(ROOT.rglob('*')) if p.is_file() and p.name not in ('manifest.json','README.md') and '__pycache__' not in str(p)}}
(ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
