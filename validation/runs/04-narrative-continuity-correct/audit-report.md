# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

[Semantic correspondence review](semantic-review.md)

## C04-OK-01

### Exact report claim

`input/report.md#C04-OK-01`

> **C04-OK-01.** Mira was alive at the key exchange at noon on day 2. Citations: chronology T-01; flashback F-02.

### Verification question

Was Mira alive when the physical brass-key exchange took place at noon on story day 2?

### Source evidence

- [input/sources/chronology.md](input/sources/chronology.md) — `T-01`

> ## T-01 — Early events
> Mira was alive on day 1 and physically handed a brass key to Ivo at noon on day 2. At dawn on day 5, Mira died in the northern tower. These are world facts, not a character's account.

- [input/sources/flashback.md](input/sources/flashback.md) — `F-02`

> ## F-02 — Remembered scene
> In the day 2 flashback, Mira physically hands the brass key to Ivo. Mira is alive in this remembered scene. The chapter then returns to the day 7 frame without staging a present-time meeting with Mira.

### Rules

- The authoritative chronology supplies story events; the explicitly labeled flashback scene stays at its own story date.
- The state model places the recorded death at dawn day 5 and the revival at dawn day 8, within the brief’s bounded chronology.

### Assumptions

- Treat T-01 as an authoritative world record and F-02 as the described remembered scene, as directed by B-02/B-03.
- The numeric time encoding faithfully preserves the stated story-day and phase order.

### Reasoning

- 1. T-01 records Mira physically handing the brass key to Ivo at noon day 2.
- 2. F-02 independently identifies this same remembered scene as day 2 and explicitly states that Mira is alive in it.
- 3. The modeled noon day 2 instant precedes dawn day 5 death; the Lean target checks that it lies in the living interval. The direct textual statement already establishes the scene-specific living state.
- 4. Nothing about its later narration frame changes the event’s story date.

### Limits

- This supports Mira’s state at the specified exchange, not a later present-time meeting or Ivo’s subsequent key storage.
- The model’s transcription and source interpretation require human review; Lean does not authenticate narrative sources.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.keyExchangeAlive` in module `Audit` (supports): `Audit.AliveAt (Audit.instant 2 Audit.noon)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target005.lean) · [Actual proof log](logs/target-005.log)

### Recommendation

Retain the claim with the day 2 story-date scope and the direct F-02 support.

## C04-OK-02

### Exact report claim

`input/report.md#C04-OK-02`

> **C04-OK-02.** Under the supplied world rules, Mira was dead at noon on day 6 and could not physically attend a meeting then. Citations: chronology T-01, T-02; rules R-01, R-02.

### Verification question

Under the bounded world rules, was Mira dead at noon day 6, and does that rule out physical meeting attendance then?

### Source evidence

- [input/sources/chronology.md](input/sources/chronology.md) — `T-01`

> ## T-01 — Early events
> Mira was alive on day 1 and physically handed a brass key to Ivo at noon on day 2. At dawn on day 5, Mira died in the northern tower. These are world facts, not a character's account.

- [input/sources/chronology.md](input/sources/chronology.md) — `T-02`

> ## T-02 — Later events
> At dawn on day 8, the Keeper performed the revival ritual on Mira, restoring her to life. Mira remained alive through the end of day 10. The record does not identify where Ivo kept the brass key after day 2.

- [input/sources/rules.md](input/sources/rules.md) — `R-01`

> ## R-01 — Life, death, and attendance
> For Mira during days 1 through 10, death makes her dead immediately, and that state persists until an explicitly recorded revival ritual restores life. Dead and alive are mutually exclusive at any single instant. Physical attendance at a meeting requires being alive. Death is reversible only through the recorded revival ritual; there is no general rule that death is permanent forever.

- [input/sources/rules.md](input/sources/rules.md) — `R-02`

> ## R-02 — Complete bounded catalog
> The complete list of revival rituals affecting Mira during days 1 through 10 contains exactly one event: the Keeper's ritual at dawn on day 8, recorded in chronology T-02. There were no other revivals of Mira in this interval. This completeness assertion says nothing about events outside this interval or other people.

### Rules

- R-01 makes death immediate and persistent until an explicitly recorded revival; alive and dead exclude one another at the same instant.
- R-02 is explicitly complete for Mira’s revivals during days 1–10, containing only dawn day 8.
- R-01 requires being alive for physical attendance; B-03 excludes ghosts, dreams, impersonators, and metaphors from that category.

### Assumptions

- Apply the rules only to Mira and the stated days 1–10 interval.
- Use the explicitly complete revival catalog, rather than generic source silence, to exclude an intervening revival before noon day 6.

### Reasoning

- 1. T-01 fixes death at dawn day 5; T-02 fixes restoration at dawn day 8.
- 2. Noon day 6 is after the death and before the only revival allowed by the complete bounded catalog.
- 3. R-01’s persistence rule therefore places Mira in the dead state at noon day 6, while exclusivity rules out being alive then. The first checked theorem verifies both modeled predicates.
- 4. If she physically attended at that instant, the attendance rule would require life, contradicting the established state. The second checked theorem verifies precisely this implication-to-impossibility argument.

### Limits

- The result applies only to physical attendance at noon day 6 in this supplied bounded world.
- It does not establish that a meeting actually occurred, where Ivo was, or whether other forms of appearance were depicted.
- No general permanent-death rule is asserted; the later revival is explicitly permitted.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.daySixDead` in module `Audit` (supports): `Audit.DeadAt (Audit.instant 6 Audit.noon) ∧ ¬ Audit.AliveAt (Audit.instant 6 Audit.noon)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target006.lean) · [Actual proof log](logs/target-006.log)

- `Audit.daySixNoPhysicalAttendance` in module `Audit` (supports): `∀ attends : Prop, (attends → Audit.AliveAt (Audit.instant 6 Audit.noon)) → ¬ attends`.
  [Model](models/Audit.lean) · [Executed check](checks/Target007.lean) · [Actual proof log](logs/target-007.log)

### Recommendation

Retain both conclusions and their reliance on the complete bounded catalog and physical-attendance rule.

## C04-OK-03

### Exact report claim

`input/report.md#C04-OK-03`

> **C04-OK-03.** Chapter seven narrates the day 2 key exchange as a flashback from the evening of day 7. Citations: flashback F-01, F-02.

### Verification question

Does chapter seven narrate the noon day 2 exchange from an evening day 7 frame without moving the exchange to day 7?

### Source evidence

- [input/sources/flashback.md](input/sources/flashback.md) — `F-01`

> ## F-01 — Narration frame
> The narration frame is the evening of day 7. The narrator announces: “I remember the exchange five days earlier.” The following scene is explicitly marked as a flashback to noon on day 2.

- [input/sources/flashback.md](input/sources/flashback.md) — `F-02`

> ## F-02 — Remembered scene
> In the day 2 flashback, Mira physically hands the brass key to Ivo. Mira is alive in this remembered scene. The chapter then returns to the day 7 frame without staging a present-time meeting with Mira.

- [input/sources/chronology.md](input/sources/chronology.md) — `T-01`

> ## T-01 — Early events
> Mira was alive on day 1 and physically handed a brass key to Ivo at noon on day 2. At dawn on day 5, Mira died in the northern tower. These are world facts, not a character's account.

### Rules

- B-02 locates a remembered scene at its explicitly labeled story date independently of narration date.
- An explicit flashback marker and frame return control interpretation; do not invent a present-time scene.

### Assumptions

- Treat the supplied chapter-seven excerpt and chronology as the complete evidence needed for this specifically described passage.

### Reasoning

- 1. F-01 names the narration frame as the evening of day 7.
- 2. The same paragraph explicitly marks the following scene as a flashback to noon day 2, consistent with the recalled exchange five days earlier.
- 3. F-02 depicts the key handover in that day 2 flashback and then returns to the day 7 frame without a present-time meeting with Mira.
- 4. T-01 independently dates the exchange to noon day 2. Thus the report preserves the two time levels correctly.

### Limits

- This is a documentary interpretation of explicit temporal labels, not a Lean-certified understanding of prose.
- The flashback does not establish physical attendance by Mira at the later narration frame.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Retain the distinction between day 2 story action and day 7 narration frame.

## C04-OK-04

### Exact report claim

`input/report.md#C04-OK-04`

> **C04-OK-04.** Mira says “I never died” at noon on day 9, although the authoritative chronology records her death at dawn on day 5. Citations: dialogue D-01; chronology T-01.

### Verification question

Did Mira utter “I never died” at noon day 9 while the authoritative chronology records death at dawn day 5?

### Source evidence

- [input/sources/dialogue.md](input/sources/dialogue.md) — `D-01`

> ## D-01 — Day 9 speech
> At noon on day 9, Mira says to Ivo, “I never died.” This line is quoted character speech. The canonical chronology remains authoritative; the text gives no rule making Mira's testimony infallible.

- [input/sources/chronology.md](input/sources/chronology.md) — `T-01`

> ## T-01 — Early events
> Mira was alive on day 1 and physically handed a brass key to Ivo at noon on day 2. At dawn on day 5, Mira died in the northern tower. These are world facts, not a character's account.

### Rules

- B-03 distinguishes attributed character speech from authoritative world facts.
- D-01 explicitly denies any rule making Mira’s testimony infallible and preserves chronological authority.

### Assumptions

- Treat D-01 as evidence of the utterance and T-01 as evidence of the world event, according to their stated evidential roles.

### Reasoning

- 1. D-01 states that Mira says “I never died” to Ivo at noon day 9; this supports the report’s attributed speech claim.
- 2. T-01 independently records her death at dawn day 5 and identifies its events as world facts.
- 3. The report juxtaposes the utterance and the authoritative event; it does not assert the utterance’s content as a true world proposition.
- 4. There is therefore no contradiction in the report itself. The quoted denial is false under the supplied world chronology, while the fact that it was said is supported.

### Limits

- No reason for Mira’s utterance—deception, confusion, metaphor, or another explanation—is established by the supplied evidence.
- Lean is not claimed to verify attribution, language understanding, or character intent.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Retain the explicit speech attribution and the distinction between its content and authoritative chronology.

## C04-OK-05

### Exact report claim

`input/report.md#C04-OK-05`

> **C04-OK-05.** The recorded ritual restores Mira to life at dawn on day 8, and she is alive at noon that day. Citations: chronology T-02; rules R-01.

### Verification question

Does the recorded dawn day 8 ritual restore Mira to life, with life persisting through noon that same day?

### Source evidence

- [input/sources/chronology.md](input/sources/chronology.md) — `T-02`

> ## T-02 — Later events
> At dawn on day 8, the Keeper performed the revival ritual on Mira, restoring her to life. Mira remained alive through the end of day 10. The record does not identify where Ivo kept the brass key after day 2.

- [input/sources/rules.md](input/sources/rules.md) — `R-01`

> ## R-01 — Life, death, and attendance
> For Mira during days 1 through 10, death makes her dead immediately, and that state persists until an explicitly recorded revival ritual restores life. Dead and alive are mutually exclusive at any single instant. Physical attendance at a meeting requires being alive. Death is reversible only through the recorded revival ritual; there is no general rule that death is permanent forever.

- [input/sources/rules.md](input/sources/rules.md) — `R-02`

> ## R-02 — Complete bounded catalog
> The complete list of revival rituals affecting Mira during days 1 through 10 contains exactly one event: the Keeper's ritual at dawn on day 8, recorded in chronology T-02. There were no other revivals of Mira in this interval. This completeness assertion says nothing about events outside this interval or other people.

### Rules

- R-01 allows the recorded revival ritual to reverse death; it contains no rule making death permanent.
- B-02 orders dawn before noon on the same story day.
- T-02 explicitly says Mira remains alive through the end of day 10.

### Assumptions

- Treat the Keeper’s recorded ritual and its stated effect as authoritative world facts.
- The time encoding preserves dawn-before-noon ordering and the bounded interval through day 10.

### Reasoning

- 1. T-02 records the Keeper’s ritual at dawn day 8 and explicitly says it restores Mira to life.
- 2. R-01 permits this restoration and R-02 confirms it is the single recorded revival in scope.
- 3. Noon day 8 follows dawn that day. T-02’s continued-life statement includes this noon instant.
- 4. The checked theorem verifies the modeled restoration time, life at dawn and noon, and the strict within-day order. No permanent-death assumption blocks the restoration.

### Limits

- This establishes the stated life transition and noon state, not unrelated events, meetings, or other characters’ locations.
- No claim is made about life beyond the supplied interval ending day 10.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.revivalAndNoonLife` in module `Audit` (supports): `Audit.revivalTime = Audit.instant 8 Audit.dawn ∧ Audit.AliveAt (Audit.instant 8 Audit.dawn) ∧ Audit.AliveAt (Audit.instant 8 Audit.noon) ∧ Audit.instant 8 Audit.dawn < Audit.instant 8 Audit.noon`.
  [Model](models/Audit.lean) · [Executed check](checks/Target008.lean) · [Actual proof log](logs/target-008.log)

### Recommendation

Retain the claim with the recorded ritual and dawn-to-noon ordering as its justification.
