# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

[Semantic correspondence review](semantic-review.md)

## VD-C01

### Exact report claim

`input/report.md#VD-C01`

> **VD-C01.** Revision 1 governs D-201. Its deadline was 2028-03-01 17:00 UTC, and its submission exactly at that deadline was timely.

### Verification question

Does D-201 retain revision 1 despite March 1 assignment, and does its February 20 receipt yield a March 1 17:00 inclusive deadline met exactly by its actual submission?

### Source evidence

- [input/sources/case-register.md](input/sources/case-register.md) — `C01`

> D-201 is a standard case. Accepted receipt: 2028-02-20 09:00 UTC. Internal assignment: 2028-03-01 08:00 UTC. Submission: 2028-03-01 17:00 UTC. No receipt correction is recorded.

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-01`

> Revision 1 applies to cases received before 2028-03-01 00:00 UTC, including cases still open after that instant. Receipt is the timestamp of the intake service's accepted receipt, not the later internal assignment timestamp.

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-02`

> For a standard case under revision 1, submission is due 10 calendar days after its receipt date, at 17:00 UTC on that date, inclusive. Receipt date is day zero. There is no weekend or holiday adjustment. This rule's calendar convention matches the audit brief.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-01`

> Revision 2 takes effect at 2028-03-01 00:00 UTC and applies to cases received at or after that instant. Cases received earlier retain revision 1 even if assigned, reviewed, or submitted after revision 2 becomes effective. Intake accepted receipt determines applicability. The boundary instant belongs to revision 2. This transition clause supersedes any informal dashboard version label.

### Rules

- V1-01 and V2-01 select the revision using accepted receipt and preserve revision 1 for earlier receipts.
- V1-02 adds ten calendar dates from receipt date as day zero and sets an inclusive 17:00 UTC cutoff with no holiday adjustment.

### Assumptions

- Accepted receipts, case classes and submissions are transcribed faithfully from the supplied register; documentary assertions are used within the fictional W-6 mandate without independent authentication.
- Gregorian UTC date conversion and the day-zero, inclusive 17:00 convention in B02 apply; no business-day adjustment is introduced.

### Reasoning

- 1. C01 records a standard case received February 20 at 09:00, before the March 1 boundary; later assignment does not alter revision 1 applicability.
- 2. 2028 includes February 29. Adding ten dates to February 20 gives March 1, not March 2. Independently executed datetime arithmetic confirms the cutoff offset 15420.
- 3. The submission is March 1 at 17:00, exactly that cutoff. Inclusive comparison establishes timeliness. All three report components are supported.

### Limits

- Lean checks integer arithmetic after source/calendar transcription, not a standalone Gregorian calendar implementation or source authenticity.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim01` in module `Audit` (supports): `Audit.revision Audit.d201 = .one ∧ Audit.standardDeadline Audit.d201 = some 15420 ∧ Audit.d201.submitted = 15420 ∧ Audit.d201.submitted ≤ 15420`.
  [Model](models/Audit.lean) · [Executed check](checks/Target009.lean) · [Actual proof log](logs/target-009.log)

### Recommendation

Retain and cite accepted receipt, the transition rule, and the leap-year day-zero calculation.

## VD-C02

### Exact report claim

`input/report.md#VD-C02`

> **VD-C02.** Revision 1 governs D-202 because accepted receipt occurred one minute before the revision boundary; later internal assignment does not change applicability.

### Verification question

Does D-202 accepted receipt at 2028-02-29 23:59 select revision 1, exactly one minute before the March 1 boundary, irrespective of later internal assignment?

### Source evidence

- [input/sources/case-register.md](input/sources/case-register.md) — `C02`

> D-202 is a standard case. Accepted receipt: 2028-02-29 23:59 UTC. Internal assignment: 2028-03-01 08:30 UTC. Submission: 2028-03-10 17:01 UTC. No receipt correction is recorded.

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-01`

> Revision 1 applies to cases received before 2028-03-01 00:00 UTC, including cases still open after that instant. Receipt is the timestamp of the intake service's accepted receipt, not the later internal assignment timestamp.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-01`

> Revision 2 takes effect at 2028-03-01 00:00 UTC and applies to cases received at or after that instant. Cases received earlier retain revision 1 even if assigned, reviewed, or submitted after revision 2 becomes effective. Intake accepted receipt determines applicability. The boundary instant belongs to revision 2. This transition clause supersedes any informal dashboard version label.

- [input/sources/transfer-note.md](input/sources/transfer-note.md) — `T01`

> The 2028-03-15 export labels D-201, D-202, D-203, and D-204 “revision 2.” The accompanying technical note says that this dashboard field displays the currently active revision on the export date; it does not record the revision legally applicable within fictional workflow W-6 to each individual case. The field is not a receipt correction.

### Rules

- Intake accepted receipt determines applicability. Earlier receipts retain revision 1 even after later assignment, review or submission; T01 labels do not override this.

### Assumptions

- Accepted receipts, case classes and submissions are transcribed faithfully from the supplied register; documentary assertions are used within the fictional W-6 mandate without independent authentication.
- Gregorian UTC date conversion and the day-zero, inclusive 17:00 convention in B02 apply; no business-day adjustment is introduced.

### Reasoning

- 1. C02 gives accepted receipt at February 29 23:59 and assignment at March 1 08:30.
- 2. The receipt minute offset 14399 is one less than the transition offset 14400, so it is strictly before the boundary and revision 1 applies.
- 3. The revision function depends only on accepted receipt. Changing assignment alone cannot change its result; the formal target quantifies over assignment values.
- 4. T01 is a display field rather than a receipt correction, so it supplies no competing authoritative version assignment.

### Limits

- Assignment invariance is about the supplied transition rule, not a general principle for other workflows.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim02` in module `Audit` (supports): `Audit.revision Audit.d202 = .one ∧ Audit.d202.received + 1 = Audit.boundary ∧ (∀ a, Audit.revision (Audit.withAssignment Audit.d202 a) = .one)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target010.lean) · [Actual proof log](logs/target-010.log)

### Recommendation

Retain the one-minute distinction and make the accepted-receipt basis explicit.

## VD-C03

### Exact report claim

`input/report.md#VD-C03`

> **VD-C03.** D-202's deadline was 2028-03-10 17:00 UTC, and its 17:01 submission that day was late.

### Verification question

Under the applicable revision 1 standard rule, is D-202 deadline March 10 17:00 UTC and its March 10 17:01 submission late?

### Source evidence

- [input/sources/case-register.md](input/sources/case-register.md) — `C02`

> D-202 is a standard case. Accepted receipt: 2028-02-29 23:59 UTC. Internal assignment: 2028-03-01 08:30 UTC. Submission: 2028-03-10 17:01 UTC. No receipt correction is recorded.

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-01`

> Revision 1 applies to cases received before 2028-03-01 00:00 UTC, including cases still open after that instant. Receipt is the timestamp of the intake service's accepted receipt, not the later internal assignment timestamp.

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-02`

> For a standard case under revision 1, submission is due 10 calendar days after its receipt date, at 17:00 UTC on that date, inclusive. Receipt date is day zero. There is no weekend or holiday adjustment. This rule's calendar convention matches the audit brief.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-01`

> Revision 2 takes effect at 2028-03-01 00:00 UTC and applies to cases received at or after that instant. Cases received earlier retain revision 1 even if assigned, reviewed, or submitted after revision 2 becomes effective. Intake accepted receipt determines applicability. The boundary instant belongs to revision 2. This transition clause supersedes any informal dashboard version label.

### Rules

- Revision 1 remains applicable to receipt before the boundary; its standard deadline is receipt date plus ten calendar days at inclusive 17:00 UTC.

### Assumptions

- Accepted receipts, case classes and submissions are transcribed faithfully from the supplied register; documentary assertions are used within the fictional W-6 mandate without independent authentication.
- Gregorian UTC date conversion and the day-zero, inclusive 17:00 convention in B02 apply; no business-day adjustment is introduced.

### Reasoning

- 1. D-202 is standard and its February 29 23:59 accepted receipt precedes the boundary.
- 2. Receipt day is February 29 regardless of its late hour. Adding ten calendar dates gives March 10; the cutoff is 17:00, offset 28380.
- 3. C02 records submission at 17:01 that day, offset 28381. The submission exceeds the inclusive cutoff by one minute and is late.

### Limits

- The computation is calendar dates from receipt date, not ten rolling 24-hour periods from 23:59. No real regulatory conclusion is implied.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim03` in module `Audit` (supports): `Audit.standardDeadline Audit.d202 = some 28380 ∧ 28380 < Audit.d202.submitted`.
  [Model](models/Audit.lean) · [Executed check](checks/Target011.lean) · [Actual proof log](logs/target-011.log)

### Recommendation

Retain the deadline and lateness with the one-minute calculation.

## VD-C04

### Exact report claim

`input/report.md#VD-C04`

> **VD-C04.** Revision 2 governs D-203 because its receipt was exactly at the boundary. Its deadline was 2028-03-08 17:00 UTC, and its submission was timely at that inclusive endpoint.

### Verification question

Does D-203 exact-boundary accepted receipt select revision 2, produce March 8 17:00 UTC as its seven-calendar-day deadline, and make the equal-time submission timely?

### Source evidence

- [input/sources/case-register.md](input/sources/case-register.md) — `C03`

> D-203 is a standard case. Accepted receipt: 2028-03-01 00:00 UTC. Internal assignment: 2028-03-01 08:45 UTC. Submission: 2028-03-08 17:00 UTC. No receipt correction is recorded.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-01`

> Revision 2 takes effect at 2028-03-01 00:00 UTC and applies to cases received at or after that instant. Cases received earlier retain revision 1 even if assigned, reviewed, or submitted after revision 2 becomes effective. Intake accepted receipt determines applicability. The boundary instant belongs to revision 2. This transition clause supersedes any informal dashboard version label.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-02`

> For a standard case under revision 2, submission is due 7 calendar days after its receipt date, at 17:00 UTC on that date, inclusive. Receipt date is day zero. There is no weekend or holiday adjustment.

### Rules

- V2-01 includes the boundary instant in revision 2. V2-02 applies a seven-calendar-day standard cutoff at inclusive 17:00 UTC.

### Assumptions

- Accepted receipts, case classes and submissions are transcribed faithfully from the supplied register; documentary assertions are used within the fictional W-6 mandate without independent authentication.
- Gregorian UTC date conversion and the day-zero, inclusive 17:00 convention in B02 apply; no business-day adjustment is introduced.

### Reasoning

- 1. C03 records a standard case with accepted receipt exactly March 1 00:00, the revision boundary; at-or-after includes equality.
- 2. March 1 plus seven calendar dates is March 8. The 17:00 cutoff is offset 25500.
- 3. C03 records submission exactly March 8 at 17:00, so it is timely at the inclusive endpoint.

### Limits

- The equality result depends on both explicitly inclusive boundaries: the revision transition and submission cutoff.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim04` in module `Audit` (supports): `Audit.d203.received = Audit.boundary ∧ Audit.revision Audit.d203 = .two ∧ Audit.standardDeadline Audit.d203 = some 25500 ∧ Audit.d203.submitted = 25500 ∧ Audit.d203.submitted ≤ 25500`.
  [Model](models/Audit.lean) · [Executed check](checks/Target012.lean) · [Actual proof log](logs/target-012.log)

### Recommendation

Retain both equality-boundary explanations.

## VD-C05

### Exact report claim

`input/report.md#VD-C05`

> **VD-C05.** The dashboard's revision 2 labels describe the active revision at export, not the applicable revision of each case.

### Verification question

Does the supplied dashboard revision field describe the active revision at export rather than per-case applicability?

### Source evidence

- [input/sources/transfer-note.md](input/sources/transfer-note.md) — `T01`

> The 2028-03-15 export labels D-201, D-202, D-203, and D-204 “revision 2.” The accompanying technical note says that this dashboard field displays the currently active revision on the export date; it does not record the revision legally applicable within fictional workflow W-6 to each individual case. The field is not a receipt correction.

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-01`

> Revision 1 applies to cases received before 2028-03-01 00:00 UTC, including cases still open after that instant. Receipt is the timestamp of the intake service's accepted receipt, not the later internal assignment timestamp.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-01`

> Revision 2 takes effect at 2028-03-01 00:00 UTC and applies to cases received at or after that instant. Cases received earlier retain revision 1 even if assigned, reviewed, or submitted after revision 2 becomes effective. Intake accepted receipt determines applicability. The boundary instant belongs to revision 2. This transition clause supersedes any informal dashboard version label.

- [input/sources/case-register.md](input/sources/case-register.md) — `C01`

> D-201 is a standard case. Accepted receipt: 2028-02-20 09:00 UTC. Internal assignment: 2028-03-01 08:00 UTC. Submission: 2028-03-01 17:00 UTC. No receipt correction is recorded.

- [input/sources/case-register.md](input/sources/case-register.md) — `C02`

> D-202 is a standard case. Accepted receipt: 2028-02-29 23:59 UTC. Internal assignment: 2028-03-01 08:30 UTC. Submission: 2028-03-10 17:01 UTC. No receipt correction is recorded.

- [input/sources/case-register.md](input/sources/case-register.md) — `C03`

> D-203 is a standard case. Accepted receipt: 2028-03-01 00:00 UTC. Internal assignment: 2028-03-01 08:45 UTC. Submission: 2028-03-08 17:00 UTC. No receipt correction is recorded.

- [input/sources/case-register.md](input/sources/case-register.md) — `C04`

> D-204 is a restricted case. Accepted receipt: 2028-03-02 10:00 UTC. Internal assignment: 2028-03-02 11:00 UTC. Submission: 2028-03-12 16:00 UTC. A pause request was filed on 2028-03-04, but no pause decision or Annex R text is supplied. Filing the request is the only established pause-related event.

### Rules

- The V2-01 transition clause supersedes informal dashboard labels. T01 explicitly defines the field as current active revision and says it is not a receipt correction.

### Assumptions

- The T01 technical note faithfully describes this supplied export field; no broader dashboard behavior is inferred.

### Reasoning

- 1. T01 states that all four cases display revision 2 on March 15 and directly explains the display semantics.
- 2. Applicable versions still derive from accepted receipt: D-201 and D-202 retain revision 1 while D-203 and D-204 use revision 2.
- 3. The explicit technical note supports the report. The finite model additionally verifies all four labels and the mismatch for the two pre-boundary cases, preventing their misinterpretation as case-level applicability evidence.

### Limits

- The theorem verifies the finite encoded display behavior and mismatch; T01 supplies the documentary field meaning. It does not inspect a live dashboard or implementation.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim05` in module `Audit` (supports): `Audit.dashboard Audit.d201 = .two ∧ Audit.dashboard Audit.d202 = .two ∧ Audit.dashboard Audit.d203 = .two ∧ Audit.dashboard Audit.d204 = .two ∧ Audit.dashboard Audit.d201 ≠ Audit.revision Audit.d201 ∧ Audit.dashboard Audit.d202 ≠ Audit.revision Audit.d202`.
  [Model](models/Audit.lean) · [Executed check](checks/Target013.lean) · [Actual proof log](logs/target-013.log)

### Recommendation

Retain and label dashboard values as export-time metadata rather than applicable case revision.

## VD-C06

### Exact report claim

`input/report.md#VD-C06`

> **VD-C06.** D-204 is restricted, so the seven-day standard-case rule does not determine its deadline.

### Verification question

Is D-204 restricted and therefore excluded from the revision 2 seven-day standard-case deadline rule?

### Source evidence

- [input/sources/case-register.md](input/sources/case-register.md) — `C04`

> D-204 is a restricted case. Accepted receipt: 2028-03-02 10:00 UTC. Internal assignment: 2028-03-02 11:00 UTC. Submission: 2028-03-12 16:00 UTC. A pause request was filed on 2028-03-04, but no pause decision or Annex R text is supplied. Filing the request is the only established pause-related event.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-01`

> Revision 2 takes effect at 2028-03-01 00:00 UTC and applies to cases received at or after that instant. Cases received earlier retain revision 1 even if assigned, reviewed, or submitted after revision 2 becomes effective. Intake accepted receipt determines applicability. The boundary instant belongs to revision 2. This transition clause supersedes any informal dashboard version label.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-02`

> For a standard case under revision 2, submission is due 7 calendar days after its receipt date, at 17:00 UTC on that date, inclusive. Receipt date is day zero. There is no weekend or holiday adjustment.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-03`

> For a restricted case, the deadline and pausing rules continue to be governed exclusively by Annex R. Nothing in revision 2 substitutes the seven-day standard-case rule for Annex R. This amendment is the only supplied change to revision 1.

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-03`

> For a restricted case, the deadline and any pausing rules are determined exclusively by Annex R. The standard-case rule V1-02 does not apply to restricted cases. Annex R is a separate normative attachment, not reproduced here.

### Rules

- V2-02 is limited to standard cases. V2-03 exclusively assigns restricted deadlines and pause rules to Annex R and does not substitute the seven-day rule.

### Assumptions

- Accepted receipts, case classes and submissions are transcribed faithfully from the supplied register; documentary assertions are used within the fictional W-6 mandate without independent authentication.
- Gregorian UTC date conversion and the day-zero, inclusive 17:00 convention in B02 apply; no business-day adjustment is introduced.

### Reasoning

- 1. C04 explicitly classifies D-204 as restricted and gives March 2 receipt, after the revision boundary.
- 2. Revision 2 applies, but its standard-case duration does not: V2-03 preserves the exclusive Annex R rule for restricted cases.
- 3. The model returns no result from the standard-deadline function for this class. That expresses rule inapplicability, not absence of any actual deadline.

### Limits

- No actual D-204 due date follows from this exclusion; Annex R is not supplied.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim06` in module `Audit` (supports): `Audit.d204.kind = .restricted ∧ Audit.revision Audit.d204 = .two ∧ Audit.standardDeadline Audit.d204 = none`.
  [Model](models/Audit.lean) · [Executed check](checks/Target014.lean) · [Actual proof log](logs/target-014.log)

### Recommendation

Retain the exclusion and avoid substituting either standard duration for Annex R.

## VD-C07

### Exact report claim

`input/report.md#VD-C07`

> **VD-C07.** The supplied package omits Annex R and establishes no exact final deadline for D-204. Consequently, this evidence does not determine whether its submission was timely.

### Verification question

Does the supplied package omit Annex R and leave D-204 final deadline and submission timeliness undetermined, rather than establishing a precise deadline or a late/timely verdict?

### Source evidence

- [input/sources/transfer-note.md](input/sources/transfer-note.md) — `T02`

> The supplied package contains revisions 1 and 2, the transition amendment, the case register, and this transfer note. Annex R was not transferred. No source states its deadline duration, calendar basis, or pause criteria, nor that any pause was approved for D-204. The package supplies no independent final due date for D-204.

- [input/sources/case-register.md](input/sources/case-register.md) — `C04`

> D-204 is a restricted case. Accepted receipt: 2028-03-02 10:00 UTC. Internal assignment: 2028-03-02 11:00 UTC. Submission: 2028-03-12 16:00 UTC. A pause request was filed on 2028-03-04, but no pause decision or Annex R text is supplied. Filing the request is the only established pause-related event.

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-03`

> For a restricted case, the deadline and any pausing rules are determined exclusively by Annex R. The standard-case rule V1-02 does not apply to restricted cases. Annex R is a separate normative attachment, not reproduced here.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-03`

> For a restricted case, the deadline and pausing rules continue to be governed exclusively by Annex R. Nothing in revision 2 substitutes the seven-day standard-case rule for Annex R. This amendment is the only supplied change to revision 1.

### Rules

- Restricted-case deadlines and pause rules derive exclusively from Annex R. Complete supplied-file inventory does not imply completeness of missing normative content. Timeliness requires comparing submission to an applicable final deadline.

### Assumptions

- The supplied-source inventory is complete for this review; absent Annex R remains unknown rather than empty.
- Auxiliary candidate due dates are explicitly hypothetical completions and introduce no actual pause approval.

### Reasoning

- 1. T02 explicitly states Annex R was not transferred, no source supplies its duration/calendar/pause criteria, and no independent D-204 final due date is supplied.
- 2. C04 establishes the actual March 12 16:00 submission but supplies neither the missing rule nor a pause decision.
- 3. Without a final applicable deadline, submission time alone cannot settle timeliness. The report accurately describes that evidence gap.
- 4. The auxiliary model keeps package absence fixed and assigns two hypothetical due dates: March 12 17:00 makes the known submission timely; March 11 17:00 makes it late. Neither contradicts a supplied restricted-case rule because none provides a duration. These are witnesses of underdetermination, not asserted Annex R contents.

### Limits

- The report's evidential-limit assertion is supported; the underlying precise deadline and timeliness remain undetermined. Lean does not prove actual Annex R rules or either hypothetical date.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **auxiliary**.

### Formal evidence

- `Audit.claim07Alternatives` in module `Audit` (auxiliary): `Audit.timelyCompletion.annexTransferred = false ∧ Audit.lateCompletion.annexTransferred = false ∧ Audit.timelyCompletion.due ≠ Audit.lateCompletion.due ∧ Audit.d204.submitted ≤ Audit.timelyCompletion.due ∧ Audit.lateCompletion.due < Audit.d204.submitted`.
  [Model](models/Audit.lean) · [Executed check](checks/Target015.lean) · [Actual proof log](logs/target-015.log)

### Recommendation

Retain the gap finding. Obtain Annex R and any applicable pause decisions or an independently established final due date before judging D-204 timeliness.

## VD-C08

### Exact report claim

`input/report.md#VD-C08`

> **VD-C08.** A pause request for D-204 is documented, but no supplied evidence establishes that a pause was approved.

### Verification question

Does the corpus establish a D-204 pause request while supplying no evidence that approval occurred?

### Source evidence

- [input/sources/case-register.md](input/sources/case-register.md) — `C04`

> D-204 is a restricted case. Accepted receipt: 2028-03-02 10:00 UTC. Internal assignment: 2028-03-02 11:00 UTC. Submission: 2028-03-12 16:00 UTC. A pause request was filed on 2028-03-04, but no pause decision or Annex R text is supplied. Filing the request is the only established pause-related event.

- [input/sources/transfer-note.md](input/sources/transfer-note.md) — `T02`

> The supplied package contains revisions 1 and 2, the transition amendment, the case register, and this transfer note. Annex R was not transferred. No source states its deadline duration, calendar basis, or pause criteria, nor that any pause was approved for D-204. The package supplies no independent final due date for D-204.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-03`

> For a restricted case, the deadline and pausing rules continue to be governed exclusively by Annex R. Nothing in revision 2 substitutes the seven-day standard-case rule for Annex R. This amendment is the only supplied change to revision 1.

### Rules

- C04 identifies filing the request as the only established pause-related event. A request and a decision are distinct; the missing Annex R pause criteria cannot be invented.

### Assumptions

- C04 and T02 are accepted as complete statements of the supplied pause evidence, not of all historical pause events.

### Reasoning

- 1. C04 explicitly records a request filed March 4 and states that no pause decision is supplied.
- 2. T02 independently states that no source says any pause was approved for D-204.
- 3. The supplied-evidence inventory therefore contains the request and no approval evidence, directly supporting the scoped report claim.
- 4. This is not proof that approval never occurred, nor permission to add pause days when calculating an unknown deadline.

### Limits

- The finite model records supplied evidence only. Actual pause approval/denial and its effect remain unknown.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim08` in module `Audit` (supports): `Audit.PauseEvidence.request ∈ Audit.suppliedPauseEvidence ∧ Audit.PauseEvidence.approval ∉ Audit.suppliedPauseEvidence`.
  [Model](models/Audit.lean) · [Executed check](checks/Target016.lean) · [Actual proof log](logs/target-016.log)

### Recommendation

Retain the request-versus-approval distinction and seek an actual decision together with Annex R before applying a pause.

## VD-C09

### Exact report claim

`input/report.md#VD-C09`

> **VD-C09.** Neither supplied rule defines a fairness measure for comparing the two timetables.

### Verification question

Do either of the two supplied rule texts define a fairness measure for comparing their timetables?

### Source evidence

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-01`

> Revision 1 applies to cases received before 2028-03-01 00:00 UTC, including cases still open after that instant. Receipt is the timestamp of the intake service's accepted receipt, not the later internal assignment timestamp.

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-02`

> For a standard case under revision 1, submission is due 10 calendar days after its receipt date, at 17:00 UTC on that date, inclusive. Receipt date is day zero. There is no weekend or holiday adjustment. This rule's calendar convention matches the audit brief.

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-03`

> For a restricted case, the deadline and any pausing rules are determined exclusively by Annex R. The standard-case rule V1-02 does not apply to restricted cases. Annex R is a separate normative attachment, not reproduced here.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-01`

> Revision 2 takes effect at 2028-03-01 00:00 UTC and applies to cases received at or after that instant. Cases received earlier retain revision 1 even if assigned, reviewed, or submitted after revision 2 becomes effective. Intake accepted receipt determines applicability. The boundary instant belongs to revision 2. This transition clause supersedes any informal dashboard version label.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-02`

> For a standard case under revision 2, submission is due 7 calendar days after its receipt date, at 17:00 UTC on that date, inclusive. Receipt date is day zero. There is no weekend or holiday adjustment.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-03`

> For a restricted case, the deadline and pausing rules continue to be governed exclusively by Annex R. Nothing in revision 2 substitutes the seven-day standard-case rule for Annex R. This amendment is the only supplied change to revision 1.

- [input/sources/transfer-note.md](input/sources/transfer-note.md) — `T03`

> The service team calls the revision 2 timetable “fairer” in an informal comment. Neither rule defines fairness, supplies a metric, or specifies a population against which that comparison should be evaluated.

### Rules

- The scope is the two supplied rule texts. A duration difference alone is not an operational fairness definition; T03 explicitly states no definition, metric, or comparison population is supplied.

### Assumptions

- The complete supplied versions are the corpus being compared; no claim is made about definitions in absent external documents.

### Reasoning

- 1. Both complete rule texts were examined: they specify version applicability, standard timing and restricted-case delegation, but no fairness measure.
- 2. T03 attributes the informal fairer comment to the service team and explicitly confirms that neither rule defines fairness, a metric, or a comparison population.
- 3. The report is a supported descriptive claim about the absence of a definition in these texts. It does not itself assert that either timetable is fairer.

### Limits

- No formal theorem is needed or claimed for this textual scope judgment. Whether either timetable is actually fairer remains nonformal without an agreed criterion and population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Retain the scoped textual finding; require an explicit metric and population before assessing the separate informal fairness comparison.
