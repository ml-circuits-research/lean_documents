import json
from pathlib import Path
root=Path('/tmp/claim-audit-jfapv2gh')
report=json.loads((root/'input/report-ledger.json').read_text())
sources=json.loads((root/'input/source-ledger.json').read_text())

def e(anchor):
    for path, passages in sources.items():
        if path.startswith('input/sources/') and anchor in passages:
            return {'path':path,'anchor':anchor,'quote':passages[anchor]}
    raise ValueError(anchor)

def p(theorem,target):
    return {'module':'Audit','theorem':'Audit.'+theorem,'target':target,'relation':'supports'}

def finding(cid, question, evidence, rules, assumptions, reasoning, formal, proofs, limits, recommendation):
    return dict(claim_id=cid,report_quote=report[cid],report_anchor=cid,question=question,evidence=[e(a) for a in evidence],
        rules=rules,assumptions=assumptions,reasoning=reasoning,semantic_state='supported',argument_status='sufficient',
        formal_status=formal,proofs=proofs,limits=limits,recommendation=recommendation)

findings=[
finding('C04-OK-01','Was Mira alive when the physical brass-key exchange took place at noon on story day 2?',
    ['T-01','F-02'],
    ['The authoritative chronology supplies story events; the explicitly labeled flashback scene stays at its own story date.','The state model places the recorded death at dawn day 5 and the revival at dawn day 8, within the brief’s bounded chronology.'],
    ['Treat T-01 as an authoritative world record and F-02 as the described remembered scene, as directed by B-02/B-03.','The numeric time encoding faithfully preserves the stated story-day and phase order.'],
    ['1. T-01 records Mira physically handing the brass key to Ivo at noon day 2.','2. F-02 independently identifies this same remembered scene as day 2 and explicitly states that Mira is alive in it.','3. The modeled noon day 2 instant precedes dawn day 5 death; the Lean target checks that it lies in the living interval. The direct textual statement already establishes the scene-specific living state.','4. Nothing about its later narration frame changes the event’s story date.'],
    'proved',[p('keyExchangeAlive','Audit.AliveAt (Audit.instant 2 Audit.noon)')],
    ['This supports Mira’s state at the specified exchange, not a later present-time meeting or Ivo’s subsequent key storage.','The model’s transcription and source interpretation require human review; Lean does not authenticate narrative sources.'],
    'Retain the claim with the day 2 story-date scope and the direct F-02 support.'),
finding('C04-OK-02','Under the bounded world rules, was Mira dead at noon day 6, and does that rule out physical meeting attendance then?',
    ['T-01','T-02','R-01','R-02'],
    ['R-01 makes death immediate and persistent until an explicitly recorded revival; alive and dead exclude one another at the same instant.','R-02 is explicitly complete for Mira’s revivals during days 1–10, containing only dawn day 8.','R-01 requires being alive for physical attendance; B-03 excludes ghosts, dreams, impersonators, and metaphors from that category.'],
    ['Apply the rules only to Mira and the stated days 1–10 interval.','Use the explicitly complete revival catalog, rather than generic source silence, to exclude an intervening revival before noon day 6.'],
    ['1. T-01 fixes death at dawn day 5; T-02 fixes restoration at dawn day 8.','2. Noon day 6 is after the death and before the only revival allowed by the complete bounded catalog.','3. R-01’s persistence rule therefore places Mira in the dead state at noon day 6, while exclusivity rules out being alive then. The first checked theorem verifies both modeled predicates.','4. If she physically attended at that instant, the attendance rule would require life, contradicting the established state. The second checked theorem verifies precisely this implication-to-impossibility argument.'],
    'proved',[p('daySixDead','Audit.DeadAt (Audit.instant 6 Audit.noon) ∧ ¬ Audit.AliveAt (Audit.instant 6 Audit.noon)'),
        p('daySixNoPhysicalAttendance','∀ attends : Prop, (attends → Audit.AliveAt (Audit.instant 6 Audit.noon)) → ¬ attends')],
    ['The result applies only to physical attendance at noon day 6 in this supplied bounded world.','It does not establish that a meeting actually occurred, where Ivo was, or whether other forms of appearance were depicted.','No general permanent-death rule is asserted; the later revival is explicitly permitted.'],
    'Retain both conclusions and their reliance on the complete bounded catalog and physical-attendance rule.'),
finding('C04-OK-03','Does chapter seven narrate the noon day 2 exchange from an evening day 7 frame without moving the exchange to day 7?',
    ['F-01','F-02','T-01'],
    ['B-02 locates a remembered scene at its explicitly labeled story date independently of narration date.','An explicit flashback marker and frame return control interpretation; do not invent a present-time scene.'],
    ['Treat the supplied chapter-seven excerpt and chronology as the complete evidence needed for this specifically described passage.'],
    ['1. F-01 names the narration frame as the evening of day 7.','2. The same paragraph explicitly marks the following scene as a flashback to noon day 2, consistent with the recalled exchange five days earlier.','3. F-02 depicts the key handover in that day 2 flashback and then returns to the day 7 frame without a present-time meeting with Mira.','4. T-01 independently dates the exchange to noon day 2. Thus the report preserves the two time levels correctly.'],
    'not_attempted',[],
    ['This is a documentary interpretation of explicit temporal labels, not a Lean-certified understanding of prose.','The flashback does not establish physical attendance by Mira at the later narration frame.'],
    'Retain the distinction between day 2 story action and day 7 narration frame.'),
finding('C04-OK-04','Did Mira utter “I never died” at noon day 9 while the authoritative chronology records death at dawn day 5?',
    ['D-01','T-01'],
    ['B-03 distinguishes attributed character speech from authoritative world facts.','D-01 explicitly denies any rule making Mira’s testimony infallible and preserves chronological authority.'],
    ['Treat D-01 as evidence of the utterance and T-01 as evidence of the world event, according to their stated evidential roles.'],
    ['1. D-01 states that Mira says “I never died” to Ivo at noon day 9; this supports the report’s attributed speech claim.','2. T-01 independently records her death at dawn day 5 and identifies its events as world facts.','3. The report juxtaposes the utterance and the authoritative event; it does not assert the utterance’s content as a true world proposition.','4. There is therefore no contradiction in the report itself. The quoted denial is false under the supplied world chronology, while the fact that it was said is supported.'],
    'not_attempted',[],
    ['No reason for Mira’s utterance—deception, confusion, metaphor, or another explanation—is established by the supplied evidence.','Lean is not claimed to verify attribution, language understanding, or character intent.'],
    'Retain the explicit speech attribution and the distinction between its content and authoritative chronology.'),
finding('C04-OK-05','Does the recorded dawn day 8 ritual restore Mira to life, with life persisting through noon that same day?',
    ['T-02','R-01','R-02'],
    ['R-01 allows the recorded revival ritual to reverse death; it contains no rule making death permanent.','B-02 orders dawn before noon on the same story day.','T-02 explicitly says Mira remains alive through the end of day 10.'],
    ['Treat the Keeper’s recorded ritual and its stated effect as authoritative world facts.','The time encoding preserves dawn-before-noon ordering and the bounded interval through day 10.'],
    ['1. T-02 records the Keeper’s ritual at dawn day 8 and explicitly says it restores Mira to life.','2. R-01 permits this restoration and R-02 confirms it is the single recorded revival in scope.','3. Noon day 8 follows dawn that day. T-02’s continued-life statement includes this noon instant.','4. The checked theorem verifies the modeled restoration time, life at dawn and noon, and the strict within-day order. No permanent-death assumption blocks the restoration.'],
    'proved',[p('revivalAndNoonLife','Audit.revivalTime = Audit.instant 8 Audit.dawn ∧ Audit.AliveAt (Audit.instant 8 Audit.dawn) ∧ Audit.AliveAt (Audit.instant 8 Audit.noon) ∧ Audit.instant 8 Audit.dawn < Audit.instant 8 Audit.noon')],
    ['This establishes the stated life transition and noon state, not unrelated events, meetings, or other characters’ locations.','No claim is made about life beyond the supplied interval ending day 10.'],
    'Retain the claim with the recorded ritual and dawn-to-noon ordering as its justification.')]

(root/'findings.json').write_text(json.dumps(findings,indent=2,ensure_ascii=False)+'\n')
claims={'scope':'All five numbered claims in the selected report, including their compound factual components.',
    'numbered_report_findings':5,'audit_records':5,
    'claims':[{'claim_id':f['claim_id'],'parent_report_anchor':f['report_anchor'],'report_quote':f['report_quote'],
        'verification_question':f['question'],'coverage':'reviewed','finding_id':f['claim_id']} for f in findings],
    'compound_claims':{'C04-OK-01':['Noon day 2 exchange','Mira alive during that exchange'],
        'C04-OK-02':['Mira dead at noon day 6','Physical attendance impossible under the living prerequisite'],
        'C04-OK-03':['Day 2 flashback story time','Evening day 7 narration frame'],
        'C04-OK-04':['Day 9 noon utterance attributed to Mira','Authoritative dawn day 5 death despite denial'],
        'C04-OK-05':['Dawn day 8 recorded revival restoring life','Alive at noon day 8']},
    'exclusions':[],
    'unclaimed_topics':['Ivo’s day 6 location, later key custody, and aesthetic quality are not asserted by the selected report and receive no invented verdict.'],
    'independent_semantic_review':'Not performed by the audit author.'}
(root/'claims.json').write_text(json.dumps(claims,indent=2,ensure_ascii=False)+'\n')
