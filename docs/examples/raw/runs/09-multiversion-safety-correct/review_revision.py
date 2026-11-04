from pathlib import Path
import json,hashlib
w=Path(__file__).resolve().parent
ledger=json.loads((w/'input/report-ledger.json').read_text())
f=json.loads((w/'findings.json').read_text())
claims=json.loads((w/'claims.json').read_text())
review_notes=[
'Clarified maximum 118 ms, below 120 ms, replaces the ambiguous margin wording. Historical acceptance remains expressly documented by V1-05/P01; arithmetic is auxiliary and no separate 24V raw log is invented.',
'Unchanged execution-date assertion: P02 June 3 falls after V2-01 June 1 commencement; the whole-day interval proof remains exact.',
'Unchanged finite N01 assertion: three valid NORMAL 20-degree runs 92,95,99 meet V2 NORMAL 100; no release inference.',
'Unchanged N02 witness: valid 101 exceeds 100, and X01/X03 exclude exception extension.',
'Unchanged E17 assertion: authorized serial-specific exception covers all of June 3; 104,108,106 meet 110.',
'Unchanged exception exclusion: X01 expressly excludes N02; model serial inequality retains the exact scope.',
'Unchanged C01 assertion: COLD 5-degree current fixture and valid 142,145,149 meet the 150 criterion.',
'Unchanged source inventory: N03 channel B and third valid run absent; aborted second run remains distinct, no zero substitution.',
'Unchanged positive expiry: K2 June 1 23:59 expiry precedes all June 3 minutes; June 5 renewal is not retrospective.',
'Unchanged validity assertion: X99 85 remains raw invalid trace after synchronization loss, not a passing repeated run.',
'Unchanged logical insufficiency: the V2 release conjunction has independent calibration, channel, fault and signature prerequisites; delay alone does not imply it.',
'Unchanged textual implication direction: route is sufficient, not stated universally necessary. Logical auxiliary counterassignment does not supply an actual alternative method.',
'Unchanged signature inventory: AUTH01 gives Sera authorized release signatures for N01/E17/C01; no cryptographic authentication claimed.',
'Unchanged packet-scope inventory: both supplied HOT rows have no qualification route; none does not mean zero or physical impossibility.'
]
changed=[]
for a,note in zip(f,review_notes):
 cid=a['claim_id']; old=a['report_quote']; a['report_quote']=ledger[cid]
 if old != ledger[cid]: changed.append(cid)
assert changed==['C09-OK-01'],changed
for a in claims['claims']:a['report_quote']=ledger[a['claim_id']]
claims['coverage']='All fourteen claim groups and their material components reviewed against the clarified selected report and unchanged source packet.'
claims['claims'][0]['components'][1]['target']='The maximum equals 118 ms and is below the 120-ms limit; the arithmetic margin is 2 ms.'
a=f[0]
a['question']='Does the supplied historical record establish the bounded revision 1 delay demonstration for L01, with maximum 118 ms below the 120-ms limit?'
a['rules'][1]='The maximum of the actual three integer delay values is compared with the applicable historical limit; this numeric result is distinct from complete release authorization.'
a['assumptions']=['Accept V1-05 as documentary evidence of historical acceptance; do not infer independently measured supply voltage from it.','The selected revised report explicitly states a maximum of 118 ms below the 120-ms limit; it does not assert a 118-ms margin.']
a['reasoning']=[
'1. P01/V1-05 record three valid L01 NORMAL observations at 20 degrees on May 20: 110, 115 and 118 ms, with both channels measured and K1 current. V1-05 expressly establishes the historical delay demonstration. V2-01 retains the historical rule for these tests.',
'2. The actual maximum is 118 ms; all three observations are below 120 ms. The arithmetic margin is 120 - 118 = 2 ms. The clarified report states this maximum and comparison unambiguously.',
'3. The historical-acceptance component is supported by the express source record. Its complete laboratory applicability is not independently reconstructed: the V1 table includes nominal 24V, but the packet supplies no separate raw supply-voltage log.',
'4. The theorem checks three observations, maximum, inequality and margin only. Its relation remains auxiliary for the grouped historical-acceptance claim; it does not assume the report conclusion to prove it and does not certify full release.'
]
a['semantic_state']='supported';a['argument_status']='sufficient'
a['limits']=['Support for historical acceptance is documentary and conditional on the supplied source record; the Lean result certifies only the encoded arithmetic.','No separate raw supply-voltage log or historical L01 fault closure/final release is supplied. The arithmetic does not establish full release or real-world safety.']
a['recommendation']='Retain the clarified maximum and historical scope, with documentary acceptance and auxiliary arithmetic distinguished.'
(w/'findings.json').write_text(json.dumps(f,indent=2,ensure_ascii=False)+'\n')
(w/'claims.json').write_text(json.dumps(claims,indent=2,ensure_ascii=False)+'\n')
revision={'revision_manifest_sha256':hashlib.sha256((w/'input/manifest.json').read_bytes()).hexdigest(),'reviewed_claims':[a['claim_id'] for a in f],'reviewer':'audit_01m','changed_report_claims':changed,'review_details':[{'claim_id':a['claim_id'],'review':note} for a,note in zip(f,review_notes)],'scope':'All fourteen refreshed claims were reviewed against the complete new selected report and their existing exact source mappings. Only D00002 changed; evidence and model parameters remain unchanged. No prior proof result is reused as current execution.'}
(w/'revision-review.json').write_text(json.dumps(revision,indent=2)+'\n')
p=w/'review-plan.md';t=p.read_text();start=t.index('Claim01 wording needs clarification:');end=t.index('\n\n',start);t=t[:start]+"The revised selected report clarifies C09-OK-01 as a maximum of 118 ms below the 120-ms limit. All fourteen claims were reviewed anew after conservative invalidation; revision-review.json records each assessment and current manifest hash. The historical acceptance component relies on express V1-05/P01 records; no raw nominal-24V supply log is invented. The unchanged arithmetic theorem remains auxiliary for this grouped documentary claim. Original ambiguous wording and its disputed assessment are retained by the coordinator in the immutable parent audit, not silently overwritten."+t[end:];p.write_text(t)
p=w/'model-notes.md';t=p.read_text();start=t.index('C09-OK-01 remains');end=t.index('\n\n',start);t=t[:start]+"C09-OK-01 in the revised selected report explicitly states maximum 118 ms below the 120-ms limit. This removes the original grammatical ambiguity; the complete revised claim is supported documentarily. V1-05/P01 expressly establish historical acceptance; `claim01Arithmetic` remains auxiliary, checking three valid values, maximum, inequality and the actual 2-ms margin. The theorem does not independently reconstruct every historical laboratory condition. The V1 table includes nominal 24V but no separate raw supply-voltage log is included. This requirement is retained, not erased or asserted as independently measured. Historical acceptance is a source assertion; the theorem does not assume that conclusion to derive it or certify full release. All fourteen report claims were re-reviewed after refresh; exact scope reviews and current manifest hash are in revision-review.json."+t[end:];t=t[:t.index('\nActual execution:')];p.write_text(t)
# Retain the former generation helper explicitly as history; prevent accidental regeneration of superseded interpretation.
p=w/'build_findings.py';t=p.read_text();p.write_text("# Historical generation script for the original report wording.\n# The current revision was reviewed explicitly in review_revision.py.\nraise SystemExit('Historical helper: do not regenerate the revised findings from original wording')\n"+t)
print(json.dumps({'reviewed':len(f),'changed':changed,'manifest':revision['revision_manifest_sha256']}))
