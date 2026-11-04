import json
from pathlib import Path
root=Path('/tmp/claim-audit-q6_blqcj')
reports=json.loads((root/'input/report-ledger.json').read_text())
sources=json.loads((root/'input/source-ledger.json').read_text())
lookup={anchor:(path,quote) for path,passages in sources.items() for anchor,quote in passages.items()}
def ev(anchors):
    return [{'path':lookup[a][0],'anchor':a,'quote':lookup[a][1].split('\n',1)[1]} for a in anchors]
shared=['The supplied canonical chronology and rules are accepted as authoritative within this fictional world, as directed by brief B-02/B-03; no external authenticity is certified.','Named story instants are encoded with an order-preserving integer coordinate; dawn=6, noon=12 and evening=18 are coding choices preserving the brief\'s ordering, not supplied clock measurements.']
rows=[
('01','supported','sufficient','proved',['T-01','F-02'],
 'Was Mira alive at the physical brass-key handover at noon on day 2, in the supplied canonical story?',
 ['F-02 explicitly says Mira is alive in the remembered day 2 scene.','B-02 locates a remembered scene at its stated story time.'],
 ['T-01 identifies the handover at day 2 noon as a world fact.','F-02 independently identifies the same physical handover and explicitly records Mira alive.','The model associates that handover with day 2 noon and its positive life fact; claim01 verifies their conjunction.'],
 'The result is local to that handover; it does not certify every earlier life state or any later meeting.',
 'Retain the claim with both source anchors and the distinction between event date and narration date.',
 'Audit.keyStoryTime = Audit.tick 2 12 ∧ Audit.ConfirmedAliveAt Audit.keyStoryTime'),
('02','refuted','invalid_inference','refuted',['T-01','T-02','R-01','R-02'],
 'Could Mira physically attend the specified day 6 noon meeting under the death-persistence and physical-attendance rules?',
 ['R-01 makes death immediate and persistent until a recorded revival.','R-02 is complete only for Mira revivals during days 1–10: the only one is day 8 dawn.','R-01 and B-02 require life for physical attendance; R-01 excludes simultaneous life and death.'],
 ['The authoritative death occurs at day 5 dawn.','The complete revival catalog contains only day 8 dawn; day 6 noon lies strictly between these events, so the death state persists then.','Physical attendance would require being alive and hence not dead at that same instant.','Claim02 proves that any occurrence proposition satisfying this independently sourced attendance condition is false at day 6 noon. This is an impossibility refutation, not a deduction from a missing meeting record.'],
 'The formal target is conditional on the sourced necessary attendance rule and is about physical attendance only; speech, a ghost, dream, impersonator, or metaphor is outside it.',
 'Remove the physical meeting claim; an intended revision would require a changed canonical scene or rule, which is not present in the supplied corpus.',
 '∀ (attendance : Prop), (attendance → ¬ Audit.DeadAt (Audit.tick 6 12)) → ¬ attendance'),
('03','refuted','invalid_inference','refuted',['F-01','F-02'],
 'Does the unique chapter-seven key exchange have day 7 as its story date merely because its narration frame is day 7?',
 ['B-02 places a remembered scene at its explicit story date.','F-01 distinguishes day 7 evening narration from day 2 noon flashback; F-02 returns to the frame without a present meeting.'],
 ['F-01 explicitly labels the exchange scene a flashback to day 2 noon.','F-02 confirms that event and explicitly denies staging a present-time meeting upon return to the day 7 frame.','The report substitutes narration time for event time. The model records the event time separately; its extracted story day is 2 and differs from 7.'],
 'The theorem concerns this identified key exchange, not every possible event narrated in chapter seven.',
 'Replace day 7 with day 2 and identify day 7 evening only as the narration frame.',
 '¬ (Audit.keyStoryTime / 24 + 1 = 7)'),
('04','supported','sufficient','proved',['D-01'],
 'Does the supplied scene record Mira uttering the exact words “I never died” at noon on day 9?',
 ['B-03 distinguishes utterance occurrence from the truth of its content.','D-01 identifies the speaker, exact words, and story time.'],
 ['D-01 explicitly reports Mira saying the words to Ivo at day 9 noon.','The model stores this as an attributed Speech record, with the utterance label mapped exactly to those quoted words.','Claim04 checks the speaker, time, and utterance identity; no rule turns this utterance into the world proposition that she never died.'],
 'The Lean enum denotes the exact cited utterance through the source legend; it does not verify truth of the words or source authenticity.',
 'Retain the speech claim; avoid using it as evidence that no death occurred.',
 'Audit.miraSpeech.speaker = Audit.Person.mira ∧ Audit.miraSpeech.time = Audit.tick 9 12 ∧ Audit.miraSpeech.words = Audit.Utterance.neverDied'),
('05','refuted','invalid_inference','refuted',['D-01','T-01'],
 'Is the universal absence of Mira death before day 9 compatible with the canonical world chronology?',
 ['B-03 says utterance does not establish world truth.','D-01 explicitly denies any infallibility rule for Mira.','T-01 presents the dawn day 5 death as a world fact.'],
 ['The cited speech establishes only that Mira says she never died.','Independently checking the chronology finds a canonical death at day 5 dawn, which is strictly before the beginning of day 9.','That one in-scope event contradicts the universal no-death claim. Claim05 refutes even the necessary restriction that no recorded death predates day 9.','No completeness assumption about all deaths is needed: the positive witness is sufficient.'],
 'This rejects the factual no-death assertion, not the existence of the utterance; no inference of narrator inconsistency is warranted when a character says something false.',
 'State that Mira says “I never died,” while the authoritative chronology records her death on day 5.',
 '¬ Audit.NeverDiedBefore9'),
('06','supported','sufficient','proved',['T-02','R-01'],
 'Is Mira alive at day 8 noon after the recorded dawn ritual?',
 ['R-01 allows a recorded ritual to restore life.','T-02 records actual restoration at day 8 dawn and continued life through day 10.','B-02 orders dawn before noon.'],
 ['T-02 states the Keeper revived Mira at day 8 dawn, restoring her to life.','The same paragraph says she remained alive through day 10, so day 8 noon is inside that explicit living interval.','Claim06 verifies membership in that positive living interval; it does not assume an unsupported off-page revival.'],
 'This is bounded to the supplied world chronology and does not assert permanent immortality.',
 'Retain the claim with T-02 as the direct event source and R-01 as the transition rule.',
 'Audit.ConfirmedAliveAt (Audit.tick 8 12)'),
('07','refuted','invalid_inference','refuted',['T-01','T-02','R-01'],
 'Does Mira remain dead at every instant strictly after dawn day 5 through the end of day 10, including after her revival?',
 ['R-01 makes death persist until revival, not permanently.','T-02 records restoration at day 8 dawn and subsequent life.','R-01 excludes being alive and dead simultaneously.'],
 ['The cited death event starts a dead interval, but R-01 gives it a revival exception.','The independent T-02 event actually triggers that exception at day 8 dawn.','Day 8 noon is strictly after day 5 dawn and before the end of day 10; T-02 establishes Mira is alive then, so she cannot be dead then.','Claim07 uses that in-scope instant to refute the universal assertion. A single counterexample suffices; it does not discretize away any possible rescue of the universal claim.'],
 'Only a concrete counterexample is required; the integer encoding does not purport to enumerate every real instant or to establish events outside days 1–10.',
 'State that Mira remained dead from day 5 dawn until the day 8 dawn revival, then remained alive through day 10.',
 '¬ Audit.AlwaysDeadAfter5'),
('08','undetermined','insufficient_support','blocked',['D-02','T-01','T-02','F-01','F-02','D-01','R-01','R-02'],
 'Do any supplied sources establish or deny that Ivo was inside the southern archive at day 6 noon?',
 ['B-03 forbids treating source silence as a negative fact outside explicitly complete catalogs.','R-02 closes Mira\'s revival catalog only, not Ivo\'s locations.'],
 ['The author cites D-02, an aesthetic marginal note; it expressly says no supplied scene or record identifies Ivo\'s day 6 noon location.','The independent full-corpus search finds Ivo in the day 2 handover and day 9 speech, neither of which determines his day 6 location.','No trajectory, travel constraint, location observation, or complete location catalog resolves the required premise.','The report therefore lacks sufficient support for the archive assertion. The absence of location evidence is not evidence that he was elsewhere; the underlying claim remains undetermined.'],
 'The conclusion is a support-gap finding about this finite corpus, not a refutation of the location claim. No Lean target establishes or negates that location.',
 'Obtain a canonical day 6 location scene or an explicit applicable location rule, or mark the archive location as unestablished.',None),
('09','not_applicable','nonformal','not_attempted',['D-02'],
 'Is there a supplied operational criterion that determines whether the revival is emotionally satisfying and beautifully paced?',
 ['B-03 distinguishes aesthetic response from world facts.','No supplied rule defines emotional satisfaction or beautiful pacing.'],
 ['D-02 offers one reader\'s attributed reaction that the scene feels tender and the key thread unresolved.','That reaction supplies neither the exact evaluative content of the report nor a measurable criterion for the report\'s judgment.','The audit can identify the opinion and its attribution, but cannot prove or refute this aesthetic assessment under the supplied world rules.'],
 'A subjective evaluation can still be editorially useful. This nonformal classification does not establish the assessment false or aesthetically unreasonable.',
 'Label the sentence as an editorial judgment, explain the pacing criteria if desired, and do not present it as a formally verified continuity finding.',None),
('10','supported','sufficient','proved',['T-01','T-02','R-01','R-02'],
 'Was there any revival affecting Mira strictly after her day 5 dawn death and strictly before day 6 noon?',
 ['R-02 explicitly and completely lists Mira revivals only during days 1–10.','The queried interval is wholly inside that catalog domain.'],
 ['T-01 establishes the lower boundary at day 5 dawn.','R-02 states the complete relevant revival list contains exactly the day 8 dawn event recorded in T-02.','Day 8 dawn is later than day 6 noon, so it is not a member of the queried open interval.','Exhausting the one-element complete catalog proves there is no qualifying revival; this is authorized bounded absence reasoning, unlike the unsupported location inference.'],
 'The result concerns Mira and this bounded interval only; it says nothing about other people, earlier/later periods, or catalog authenticity.',
 'Retain the claim and explicitly cite R-02 completeness; do not generalize it beyond Mira or days 1–10.',
 'Audit.NoRevivalBefore6')]
findings=[]
for num,sem,arg,formal,anchors,q,rules,reason,limit,rec,target in rows:
    cid='C04-'+num
    proofs=[] if target is None else [{'module':'Audit','theorem':'Audit.claim'+num,'relation':'supports' if formal=='proved' else 'refutes','target':target}]
    findings.append({'claim_id':cid,'report_quote':reports[cid],'report_anchor':cid,'atomic_target':json.loads((root/'claims.json').read_text())['claims'][int(num)-1]['atomic_target'],'parent_finding':cid,'question':q,'evidence':ev(anchors),'rules':rules,'assumptions':shared if target else [shared[0]],'reasoning':[f'{i}. {s}' for i,s in enumerate(reason,1)],'semantic_state':sem,'argument_status':arg,'formal_status':formal,'proofs':proofs,'limits':[limit,'Checked Lean results establish only the transcribed model targets; semantic correspondence still requires review.'],'recommendation':rec})
(root/'findings.json').write_text(json.dumps(findings,indent=2,ensure_ascii=False)+'\n')
claims=json.loads((root/'claims.json').read_text())
for c in claims['claims']: c['coverage']='assessed; see findings.json'
(root/'claims.json').write_text(json.dumps(claims,indent=2,ensure_ascii=False)+'\n')
