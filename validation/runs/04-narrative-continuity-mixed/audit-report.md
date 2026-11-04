# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

[Semantic correspondence review](semantic-review.md)

## C04-01

### Exact report claim

`input/report.md#C04-01`

> **C04-01.** Mira was alive when she handed Ivo the brass key at noon on day 2. Citations: chronology T-01; flashback F-02.

### Verification question

Was Mira alive at the physical brass-key handover at noon on day 2, in the supplied canonical story?

### Source evidence

- [input/sources/chronology.md](input/sources/chronology.md) — `T-01`

> Mira was alive on day 1 and physically handed a brass key to Ivo at noon on day 2. At dawn on day 5, Mira died in the northern tower. These are world facts, not a character's account.

- [input/sources/flashback.md](input/sources/flashback.md) — `F-02`

> In the day 2 flashback, Mira physically hands the brass key to Ivo. Mira is alive in this remembered scene. The chapter then returns to the day 7 frame without staging a present-time meeting with Mira.

### Rules

- F-02 explicitly says Mira is alive in the remembered day 2 scene.
- B-02 locates a remembered scene at its stated story time.

### Assumptions

- The supplied canonical chronology and rules are accepted as authoritative within this fictional world, as directed by brief B-02/B-03; no external authenticity is certified.
- Named story instants are encoded with an order-preserving integer coordinate; dawn=6, noon=12 and evening=18 are coding choices preserving the brief's ordering, not supplied clock measurements.

### Reasoning

- 1. T-01 identifies the handover at day 2 noon as a world fact.
- 2. F-02 independently identifies the same physical handover and explicitly records Mira alive.
- 3. The model associates that handover with day 2 noon and its positive life fact; claim01 verifies their conjunction.

### Limits

- The result is local to that handover; it does not certify every earlier life state or any later meeting.
- Checked Lean results establish only the transcribed model targets; semantic correspondence still requires review.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim01` in module `Audit` (supports): `Audit.keyStoryTime = Audit.tick 2 12 ∧ Audit.ConfirmedAliveAt Audit.keyStoryTime`.
  [Model](models/Audit.lean) · [Executed check](checks/Target009.lean) · [Actual proof log](logs/target-009.log)

### Recommendation

Retain the claim with both source anchors and the distinction between event date and narration date.

## C04-02

### Exact report claim

`input/report.md#C04-02`

> **C04-02.** Mira physically attended a meeting with Ivo at noon on day 6. Citations: chronology T-01, T-02; rules R-01, R-02.

### Verification question

Could Mira physically attend the specified day 6 noon meeting under the death-persistence and physical-attendance rules?

### Source evidence

- [input/sources/chronology.md](input/sources/chronology.md) — `T-01`

> Mira was alive on day 1 and physically handed a brass key to Ivo at noon on day 2. At dawn on day 5, Mira died in the northern tower. These are world facts, not a character's account.

- [input/sources/chronology.md](input/sources/chronology.md) — `T-02`

> At dawn on day 8, the Keeper performed the revival ritual on Mira, restoring her to life. Mira remained alive through the end of day 10. The record does not identify where Ivo kept the brass key after day 2.

- [input/sources/rules.md](input/sources/rules.md) — `R-01`

> For Mira during days 1 through 10, death makes her dead immediately, and that state persists until an explicitly recorded revival ritual restores life. Dead and alive are mutually exclusive at any single instant. Physical attendance at a meeting requires being alive. Death is reversible only through the recorded revival ritual; there is no general rule that death is permanent forever.

- [input/sources/rules.md](input/sources/rules.md) — `R-02`

> The complete list of revival rituals affecting Mira during days 1 through 10 contains exactly one event: the Keeper's ritual at dawn on day 8, recorded in chronology T-02. There were no other revivals of Mira in this interval. This completeness assertion says nothing about events outside this interval or other people.

### Rules

- R-01 makes death immediate and persistent until a recorded revival.
- R-02 is complete only for Mira revivals during days 1–10: the only one is day 8 dawn.
- R-01 and B-02 require life for physical attendance; R-01 excludes simultaneous life and death.

### Assumptions

- The supplied canonical chronology and rules are accepted as authoritative within this fictional world, as directed by brief B-02/B-03; no external authenticity is certified.
- Named story instants are encoded with an order-preserving integer coordinate; dawn=6, noon=12 and evening=18 are coding choices preserving the brief's ordering, not supplied clock measurements.

### Reasoning

- 1. The authoritative death occurs at day 5 dawn.
- 2. The complete revival catalog contains only day 8 dawn; day 6 noon lies strictly between these events, so the death state persists then.
- 3. Physical attendance would require being alive and hence not dead at that same instant.
- 4. Claim02 proves that any occurrence proposition satisfying this independently sourced attendance condition is false at day 6 noon. This is an impossibility refutation, not a deduction from a missing meeting record.

### Limits

- The formal target is conditional on the sourced necessary attendance rule and is about physical attendance only; speech, a ghost, dream, impersonator, or metaphor is outside it.
- Checked Lean results establish only the transcribed model targets; semantic correspondence still requires review.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim02` in module `Audit` (refutes): `∀ (attendance : Prop), (attendance → ¬ Audit.DeadAt (Audit.tick 6 12)) → ¬ attendance`.
  [Model](models/Audit.lean) · [Executed check](checks/Target010.lean) · [Actual proof log](logs/target-010.log)

### Recommendation

Remove the physical meeting claim; an intended revision would require a changed canonical scene or rule, which is not present in the supplied corpus.

## C04-03

### Exact report claim

`input/report.md#C04-03`

> **C04-03.** The key exchange in chapter seven occurs on day 7 because that is the chapter's narration frame. Citations: flashback F-01, F-02.

### Verification question

Does the unique chapter-seven key exchange have day 7 as its story date merely because its narration frame is day 7?

### Source evidence

- [input/sources/flashback.md](input/sources/flashback.md) — `F-01`

> The narration frame is the evening of day 7. The narrator announces: “I remember the exchange five days earlier.” The following scene is explicitly marked as a flashback to noon on day 2.

- [input/sources/flashback.md](input/sources/flashback.md) — `F-02`

> In the day 2 flashback, Mira physically hands the brass key to Ivo. Mira is alive in this remembered scene. The chapter then returns to the day 7 frame without staging a present-time meeting with Mira.

### Rules

- B-02 places a remembered scene at its explicit story date.
- F-01 distinguishes day 7 evening narration from day 2 noon flashback; F-02 returns to the frame without a present meeting.

### Assumptions

- The supplied canonical chronology and rules are accepted as authoritative within this fictional world, as directed by brief B-02/B-03; no external authenticity is certified.
- Named story instants are encoded with an order-preserving integer coordinate; dawn=6, noon=12 and evening=18 are coding choices preserving the brief's ordering, not supplied clock measurements.

### Reasoning

- 1. F-01 explicitly labels the exchange scene a flashback to day 2 noon.
- 2. F-02 confirms that event and explicitly denies staging a present-time meeting upon return to the day 7 frame.
- 3. The report substitutes narration time for event time. The model records the event time separately; its extracted story day is 2 and differs from 7.

### Limits

- The theorem concerns this identified key exchange, not every possible event narrated in chapter seven.
- Checked Lean results establish only the transcribed model targets; semantic correspondence still requires review.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim03` in module `Audit` (refutes): `¬ (Audit.keyStoryTime / 24 + 1 = 7)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target011.lean) · [Actual proof log](logs/target-011.log)

### Recommendation

Replace day 7 with day 2 and identify day 7 evening only as the narration frame.

## C04-04

### Exact report claim

`input/report.md#C04-04`

> **C04-04.** Mira utters the words “I never died” at noon on day 9. Citation: dialogue D-01.

### Verification question

Does the supplied scene record Mira uttering the exact words “I never died” at noon on day 9?

### Source evidence

- [input/sources/dialogue.md](input/sources/dialogue.md) — `D-01`

> At noon on day 9, Mira says to Ivo, “I never died.” This line is quoted character speech. The canonical chronology remains authoritative; the text gives no rule making Mira's testimony infallible.

### Rules

- B-03 distinguishes utterance occurrence from the truth of its content.
- D-01 identifies the speaker, exact words, and story time.

### Assumptions

- The supplied canonical chronology and rules are accepted as authoritative within this fictional world, as directed by brief B-02/B-03; no external authenticity is certified.
- Named story instants are encoded with an order-preserving integer coordinate; dawn=6, noon=12 and evening=18 are coding choices preserving the brief's ordering, not supplied clock measurements.

### Reasoning

- 1. D-01 explicitly reports Mira saying the words to Ivo at day 9 noon.
- 2. The model stores this as an attributed Speech record, with the utterance label mapped exactly to those quoted words.
- 3. Claim04 checks the speaker, time, and utterance identity; no rule turns this utterance into the world proposition that she never died.

### Limits

- The Lean enum denotes the exact cited utterance through the source legend; it does not verify truth of the words or source authenticity.
- Checked Lean results establish only the transcribed model targets; semantic correspondence still requires review.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim04` in module `Audit` (supports): `Audit.miraSpeech.speaker = Audit.Person.mira ∧ Audit.miraSpeech.time = Audit.tick 9 12 ∧ Audit.miraSpeech.words = Audit.Utterance.neverDied`.
  [Model](models/Audit.lean) · [Executed check](checks/Target012.lean) · [Actual proof log](logs/target-012.log)

### Recommendation

Retain the speech claim; avoid using it as evidence that no death occurred.

## C04-05

### Exact report claim

`input/report.md#C04-05`

> **C04-05.** Mira never died before day 9. Citation: dialogue D-01.

### Verification question

Is the universal absence of Mira death before day 9 compatible with the canonical world chronology?

### Source evidence

- [input/sources/dialogue.md](input/sources/dialogue.md) — `D-01`

> At noon on day 9, Mira says to Ivo, “I never died.” This line is quoted character speech. The canonical chronology remains authoritative; the text gives no rule making Mira's testimony infallible.

- [input/sources/chronology.md](input/sources/chronology.md) — `T-01`

> Mira was alive on day 1 and physically handed a brass key to Ivo at noon on day 2. At dawn on day 5, Mira died in the northern tower. These are world facts, not a character's account.

### Rules

- B-03 says utterance does not establish world truth.
- D-01 explicitly denies any infallibility rule for Mira.
- T-01 presents the dawn day 5 death as a world fact.

### Assumptions

- The supplied canonical chronology and rules are accepted as authoritative within this fictional world, as directed by brief B-02/B-03; no external authenticity is certified.
- Named story instants are encoded with an order-preserving integer coordinate; dawn=6, noon=12 and evening=18 are coding choices preserving the brief's ordering, not supplied clock measurements.

### Reasoning

- 1. The cited speech establishes only that Mira says she never died.
- 2. Independently checking the chronology finds a canonical death at day 5 dawn, which is strictly before the beginning of day 9.
- 3. That one in-scope event contradicts the universal no-death claim. Claim05 refutes even the necessary restriction that no recorded death predates day 9.
- 4. No completeness assumption about all deaths is needed: the positive witness is sufficient.

### Limits

- This rejects the factual no-death assertion, not the existence of the utterance; no inference of narrator inconsistency is warranted when a character says something false.
- Checked Lean results establish only the transcribed model targets; semantic correspondence still requires review.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim05` in module `Audit` (refutes): `¬ Audit.NeverDiedBefore9`.
  [Model](models/Audit.lean) · [Executed check](checks/Target013.lean) · [Actual proof log](logs/target-013.log)

### Recommendation

State that Mira says “I never died,” while the authoritative chronology records her death on day 5.

## C04-06

### Exact report claim

`input/report.md#C04-06`

> **C04-06.** Mira is alive at noon on day 8 following the recorded ritual. Citations: chronology T-02; rules R-01.

### Verification question

Is Mira alive at day 8 noon after the recorded dawn ritual?

### Source evidence

- [input/sources/chronology.md](input/sources/chronology.md) — `T-02`

> At dawn on day 8, the Keeper performed the revival ritual on Mira, restoring her to life. Mira remained alive through the end of day 10. The record does not identify where Ivo kept the brass key after day 2.

- [input/sources/rules.md](input/sources/rules.md) — `R-01`

> For Mira during days 1 through 10, death makes her dead immediately, and that state persists until an explicitly recorded revival ritual restores life. Dead and alive are mutually exclusive at any single instant. Physical attendance at a meeting requires being alive. Death is reversible only through the recorded revival ritual; there is no general rule that death is permanent forever.

### Rules

- R-01 allows a recorded ritual to restore life.
- T-02 records actual restoration at day 8 dawn and continued life through day 10.
- B-02 orders dawn before noon.

### Assumptions

- The supplied canonical chronology and rules are accepted as authoritative within this fictional world, as directed by brief B-02/B-03; no external authenticity is certified.
- Named story instants are encoded with an order-preserving integer coordinate; dawn=6, noon=12 and evening=18 are coding choices preserving the brief's ordering, not supplied clock measurements.

### Reasoning

- 1. T-02 states the Keeper revived Mira at day 8 dawn, restoring her to life.
- 2. The same paragraph says she remained alive through day 10, so day 8 noon is inside that explicit living interval.
- 3. Claim06 verifies membership in that positive living interval; it does not assume an unsupported off-page revival.

### Limits

- This is bounded to the supplied world chronology and does not assert permanent immortality.
- Checked Lean results establish only the transcribed model targets; semantic correspondence still requires review.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim06` in module `Audit` (supports): `Audit.ConfirmedAliveAt (Audit.tick 8 12)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target014.lean) · [Actual proof log](logs/target-014.log)

### Recommendation

Retain the claim with T-02 as the direct event source and R-01 as the transition rule.

## C04-07

### Exact report claim

`input/report.md#C04-07`

> **C04-07.** Mira is dead at every instant after dawn on day 5 through the end of day 10. Citations: chronology T-01; rules R-01.

### Verification question

Does Mira remain dead at every instant strictly after dawn day 5 through the end of day 10, including after her revival?

### Source evidence

- [input/sources/chronology.md](input/sources/chronology.md) — `T-01`

> Mira was alive on day 1 and physically handed a brass key to Ivo at noon on day 2. At dawn on day 5, Mira died in the northern tower. These are world facts, not a character's account.

- [input/sources/chronology.md](input/sources/chronology.md) — `T-02`

> At dawn on day 8, the Keeper performed the revival ritual on Mira, restoring her to life. Mira remained alive through the end of day 10. The record does not identify where Ivo kept the brass key after day 2.

- [input/sources/rules.md](input/sources/rules.md) — `R-01`

> For Mira during days 1 through 10, death makes her dead immediately, and that state persists until an explicitly recorded revival ritual restores life. Dead and alive are mutually exclusive at any single instant. Physical attendance at a meeting requires being alive. Death is reversible only through the recorded revival ritual; there is no general rule that death is permanent forever.

### Rules

- R-01 makes death persist until revival, not permanently.
- T-02 records restoration at day 8 dawn and subsequent life.
- R-01 excludes being alive and dead simultaneously.

### Assumptions

- The supplied canonical chronology and rules are accepted as authoritative within this fictional world, as directed by brief B-02/B-03; no external authenticity is certified.
- Named story instants are encoded with an order-preserving integer coordinate; dawn=6, noon=12 and evening=18 are coding choices preserving the brief's ordering, not supplied clock measurements.

### Reasoning

- 1. The cited death event starts a dead interval, but R-01 gives it a revival exception.
- 2. The independent T-02 event actually triggers that exception at day 8 dawn.
- 3. Day 8 noon is strictly after day 5 dawn and before the end of day 10; T-02 establishes Mira is alive then, so she cannot be dead then.
- 4. Claim07 uses that in-scope instant to refute the universal assertion. A single counterexample suffices; it does not discretize away any possible rescue of the universal claim.

### Limits

- Only a concrete counterexample is required; the integer encoding does not purport to enumerate every real instant or to establish events outside days 1–10.
- Checked Lean results establish only the transcribed model targets; semantic correspondence still requires review.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim07` in module `Audit` (refutes): `¬ Audit.AlwaysDeadAfter5`.
  [Model](models/Audit.lean) · [Executed check](checks/Target015.lean) · [Actual proof log](logs/target-015.log)

### Recommendation

State that Mira remained dead from day 5 dawn until the day 8 dawn revival, then remained alive through day 10.

## C04-08

### Exact report claim

`input/report.md#C04-08`

> **C04-08.** Ivo was inside the southern archive at noon on day 6. Citation: dialogue D-02.

### Verification question

Do any supplied sources establish or deny that Ivo was inside the southern archive at day 6 noon?

### Source evidence

- [input/sources/dialogue.md](input/sources/dialogue.md) — `D-02`

> A reader writes, “The revival scene feels tender, but the brass key thread is unresolved.” This is an aesthetic response. No scene or record supplied here identifies Ivo's location at noon on day 6.

- [input/sources/chronology.md](input/sources/chronology.md) — `T-01`

> Mira was alive on day 1 and physically handed a brass key to Ivo at noon on day 2. At dawn on day 5, Mira died in the northern tower. These are world facts, not a character's account.

- [input/sources/chronology.md](input/sources/chronology.md) — `T-02`

> At dawn on day 8, the Keeper performed the revival ritual on Mira, restoring her to life. Mira remained alive through the end of day 10. The record does not identify where Ivo kept the brass key after day 2.

- [input/sources/flashback.md](input/sources/flashback.md) — `F-01`

> The narration frame is the evening of day 7. The narrator announces: “I remember the exchange five days earlier.” The following scene is explicitly marked as a flashback to noon on day 2.

- [input/sources/flashback.md](input/sources/flashback.md) — `F-02`

> In the day 2 flashback, Mira physically hands the brass key to Ivo. Mira is alive in this remembered scene. The chapter then returns to the day 7 frame without staging a present-time meeting with Mira.

- [input/sources/dialogue.md](input/sources/dialogue.md) — `D-01`

> At noon on day 9, Mira says to Ivo, “I never died.” This line is quoted character speech. The canonical chronology remains authoritative; the text gives no rule making Mira's testimony infallible.

- [input/sources/rules.md](input/sources/rules.md) — `R-01`

> For Mira during days 1 through 10, death makes her dead immediately, and that state persists until an explicitly recorded revival ritual restores life. Dead and alive are mutually exclusive at any single instant. Physical attendance at a meeting requires being alive. Death is reversible only through the recorded revival ritual; there is no general rule that death is permanent forever.

- [input/sources/rules.md](input/sources/rules.md) — `R-02`

> The complete list of revival rituals affecting Mira during days 1 through 10 contains exactly one event: the Keeper's ritual at dawn on day 8, recorded in chronology T-02. There were no other revivals of Mira in this interval. This completeness assertion says nothing about events outside this interval or other people.

### Rules

- B-03 forbids treating source silence as a negative fact outside explicitly complete catalogs.
- R-02 closes Mira's revival catalog only, not Ivo's locations.

### Assumptions

- The supplied canonical chronology and rules are accepted as authoritative within this fictional world, as directed by brief B-02/B-03; no external authenticity is certified.

### Reasoning

- 1. The author cites D-02, an aesthetic marginal note; it expressly says no supplied scene or record identifies Ivo's day 6 noon location.
- 2. The independent full-corpus search finds Ivo in the day 2 handover and day 9 speech, neither of which determines his day 6 location.
- 3. No trajectory, travel constraint, location observation, or complete location catalog resolves the required premise.
- 4. The report therefore lacks sufficient support for the archive assertion. The absence of location evidence is not evidence that he was elsewhere; the underlying claim remains undetermined.

### Limits

- The conclusion is a support-gap finding about this finite corpus, not a refutation of the location claim. No Lean target establishes or negates that location.
- Checked Lean results establish only the transcribed model targets; semantic correspondence still requires review.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **blocked**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Obtain a canonical day 6 location scene or an explicit applicable location rule, or mark the archive location as unestablished.

## C04-09

### Exact report claim

`input/report.md#C04-09`

> **C04-09.** The revival scene is emotionally satisfying and beautifully paced. Citation: dialogue D-02.

### Verification question

Is there a supplied operational criterion that determines whether the revival is emotionally satisfying and beautifully paced?

### Source evidence

- [input/sources/dialogue.md](input/sources/dialogue.md) — `D-02`

> A reader writes, “The revival scene feels tender, but the brass key thread is unresolved.” This is an aesthetic response. No scene or record supplied here identifies Ivo's location at noon on day 6.

### Rules

- B-03 distinguishes aesthetic response from world facts.
- No supplied rule defines emotional satisfaction or beautiful pacing.

### Assumptions

- The supplied canonical chronology and rules are accepted as authoritative within this fictional world, as directed by brief B-02/B-03; no external authenticity is certified.

### Reasoning

- 1. D-02 offers one reader's attributed reaction that the scene feels tender and the key thread unresolved.
- 2. That reaction supplies neither the exact evaluative content of the report nor a measurable criterion for the report's judgment.
- 3. The audit can identify the opinion and its attribution, but cannot prove or refute this aesthetic assessment under the supplied world rules.

### Limits

- A subjective evaluation can still be editorially useful. This nonformal classification does not establish the assessment false or aesthetically unreasonable.
- Checked Lean results establish only the transcribed model targets; semantic correspondence still requires review.

### Result

Semantic state: **not_applicable**; argument status: **nonformal**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Label the sentence as an editorial judgment, explain the pacing criteria if desired, and do not present it as a formally verified continuity finding.

## C04-10

### Exact report claim

`input/report.md#C04-10`

> **C04-10.** No revival of Mira occurred after her death and before noon on day 6. Citations: chronology T-01; rules R-02.

### Verification question

Was there any revival affecting Mira strictly after her day 5 dawn death and strictly before day 6 noon?

### Source evidence

- [input/sources/chronology.md](input/sources/chronology.md) — `T-01`

> Mira was alive on day 1 and physically handed a brass key to Ivo at noon on day 2. At dawn on day 5, Mira died in the northern tower. These are world facts, not a character's account.

- [input/sources/chronology.md](input/sources/chronology.md) — `T-02`

> At dawn on day 8, the Keeper performed the revival ritual on Mira, restoring her to life. Mira remained alive through the end of day 10. The record does not identify where Ivo kept the brass key after day 2.

- [input/sources/rules.md](input/sources/rules.md) — `R-01`

> For Mira during days 1 through 10, death makes her dead immediately, and that state persists until an explicitly recorded revival ritual restores life. Dead and alive are mutually exclusive at any single instant. Physical attendance at a meeting requires being alive. Death is reversible only through the recorded revival ritual; there is no general rule that death is permanent forever.

- [input/sources/rules.md](input/sources/rules.md) — `R-02`

> The complete list of revival rituals affecting Mira during days 1 through 10 contains exactly one event: the Keeper's ritual at dawn on day 8, recorded in chronology T-02. There were no other revivals of Mira in this interval. This completeness assertion says nothing about events outside this interval or other people.

### Rules

- R-02 explicitly and completely lists Mira revivals only during days 1–10.
- The queried interval is wholly inside that catalog domain.

### Assumptions

- The supplied canonical chronology and rules are accepted as authoritative within this fictional world, as directed by brief B-02/B-03; no external authenticity is certified.
- Named story instants are encoded with an order-preserving integer coordinate; dawn=6, noon=12 and evening=18 are coding choices preserving the brief's ordering, not supplied clock measurements.

### Reasoning

- 1. T-01 establishes the lower boundary at day 5 dawn.
- 2. R-02 states the complete relevant revival list contains exactly the day 8 dawn event recorded in T-02.
- 3. Day 8 dawn is later than day 6 noon, so it is not a member of the queried open interval.
- 4. Exhausting the one-element complete catalog proves there is no qualifying revival; this is authorized bounded absence reasoning, unlike the unsupported location inference.

### Limits

- The result concerns Mira and this bounded interval only; it says nothing about other people, earlier/later periods, or catalog authenticity.
- Checked Lean results establish only the transcribed model targets; semantic correspondence still requires review.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim10` in module `Audit` (supports): `Audit.NoRevivalBefore6`.
  [Model](models/Audit.lean) · [Executed check](checks/Target016.lean) · [Actual proof log](logs/target-016.log)

### Recommendation

Retain the claim and explicitly cite R-02 completeness; do not generalize it beyond Mira or days 1–10.
