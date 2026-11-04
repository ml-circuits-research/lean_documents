# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

[Semantic correspondence review](semantic-review.md)

## VD-01a

### Exact report claim

`input/report.md#VD-01`

> **VD-01.** Revision 1 governs D-201, and its deadline was 2028-03-01 17:00 UTC.

### Verification question

Does revision 1 govern D-201 under the receipt-based transition at the evidence cutoff?

### Source evidence

- [input/sources/case-register.md](input/sources/case-register.md) — `C01`

> D-201 is a standard case. Accepted receipt: 2028-02-20 09:00 UTC. Internal assignment: 2028-03-01 08:00 UTC. Submission: 2028-03-01 17:00 UTC. No receipt correction is recorded.

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-01`

> Revision 1 applies to cases received before 2028-03-01 00:00 UTC, including cases still open after that instant. Receipt is the timestamp of the intake service's accepted receipt, not the later internal assignment timestamp.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-01`

> Revision 2 takes effect at 2028-03-01 00:00 UTC and applies to cases received at or after that instant. Cases received earlier retain revision 1 even if assigned, reviewed, or submitted after revision 2 becomes effective. Intake accepted receipt determines applicability. The boundary instant belongs to revision 2. This transition clause supersedes any informal dashboard version label.

- [input/sources/transfer-note.md](input/sources/transfer-note.md) — `T01`

> The 2028-03-15 export labels D-201, D-202, D-203, and D-204 “revision 2.” The accompanying technical note says that this dashboard field displays the currently active revision on the export date; it does not record the revision legally applicable within fictional workflow W-6 to each individual case. The field is not a receipt correction.

### Rules

- V1-01 and V2-01 choose revision by accepted receipt before versus at/after 2028-03-01 00:00 UTC; assignment and export date are immaterial.

### Assumptions

- The accepted register and supplied fictional rules are faithful inputs; the audit does not authenticate their historical accuracy.
- Gregorian UTC dates use receipt day zero and inclusive 17:00 deadlines; no working-day rollover is permitted.

### Reasoning

- 1. C01 records accepted receipt on February 20, before the March 1 boundary.
- 2. The later assignment and dashboard revision-2 label cannot replace accepted receipt.
- 3. Revision 1 applies; the model checks the finite receipt-based selector.

### Limits

- The conclusion is conditional on accurate supplied records and the stated W-6 scope; it does not certify source authenticity or apply outside these four cases.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.version201` in module `Audit` (supports): `Audit.revision Audit.c201 = 1`.
  [Model](models/Audit.lean) · [Executed check](checks/Target011.lean) · [Actual proof log](logs/target-011.log)

### Recommendation

Retain the version statement and cite C01 plus the transition clause.

## VD-01b

### Exact report claim

`input/report.md#VD-01`

> **VD-01.** Revision 1 governs D-201, and its deadline was 2028-03-01 17:00 UTC.

### Verification question

Is D-201 standard-case deadline March 1, 2028 at 17:00 UTC?

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

- V1-01 and V2-01 choose revision by accepted receipt before versus at/after 2028-03-01 00:00 UTC; assignment and export date are immaterial.
- V1-02 grants standard revision-1 cases 10 calendar days; V2-02 grants standard revision-2 cases 7 calendar days, receipt date day zero, at 17:00 UTC inclusive.

### Assumptions

- The accepted register and supplied fictional rules are faithful inputs; the audit does not authenticate their historical accuracy.
- Gregorian UTC dates use receipt day zero and inclusive 17:00 deadlines; no working-day rollover is permitted.

### Reasoning

- 1. D-201 is standard and received February 20 under revision 1.
- 2. February 20 is offset 0; leap-day February 29 is offset 9; March 1 is offset 10.
- 3. Adding ten dates gives March 1 at 17:00, minute 15420 from origin. Python Gregorian date offsets independently agree with manual counting.

### Limits

- The conclusion is conditional on accurate supplied records and the stated W-6 scope; it does not certify source authenticity or apply outside these four cases.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.deadline201` in module `Audit` (supports): `Audit.standardDue Audit.c201 = some (Audit.at17 10)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target012.lean) · [Actual proof log](logs/target-012.log)

### Recommendation

Retain the stated deadline and show the leap-year calculation.

## VD-02

### Exact report claim

`input/report.md#VD-02`

> **VD-02.** D-201's submission was timely.

### Verification question

Was D-201 submission at the exact inclusive deadline timely?

### Source evidence

- [input/sources/case-register.md](input/sources/case-register.md) — `C01`

> D-201 is a standard case. Accepted receipt: 2028-02-20 09:00 UTC. Internal assignment: 2028-03-01 08:00 UTC. Submission: 2028-03-01 17:00 UTC. No receipt correction is recorded.

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-01`

> Revision 1 applies to cases received before 2028-03-01 00:00 UTC, including cases still open after that instant. Receipt is the timestamp of the intake service's accepted receipt, not the later internal assignment timestamp.

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-02`

> For a standard case under revision 1, submission is due 10 calendar days after its receipt date, at 17:00 UTC on that date, inclusive. Receipt date is day zero. There is no weekend or holiday adjustment. This rule's calendar convention matches the audit brief.

### Rules

- V1-01 and V2-01 choose revision by accepted receipt before versus at/after 2028-03-01 00:00 UTC; assignment and export date are immaterial.
- V1-02 grants standard revision-1 cases 10 calendar days; V2-02 grants standard revision-2 cases 7 calendar days, receipt date day zero, at 17:00 UTC inclusive.

### Assumptions

- The accepted register and supplied fictional rules are faithful inputs; the audit does not authenticate their historical accuracy.
- Gregorian UTC dates use receipt day zero and inclusive 17:00 deadlines; no working-day rollover is permitted.

### Reasoning

- 1. D-201 deadline is March 1 17:00, from February 20 plus ten dates.
- 2. C01 submission is March 1 17:00, exactly equal to the deadline.
- 3. Inclusive means submission ≤ deadline; equality is timely.

### Limits

- The conclusion is conditional on accurate supplied records and the stated W-6 scope; it does not certify source authenticity or apply outside these four cases.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.timely201` in module `Audit` (supports): `Audit.standardDue Audit.c201 = some (Audit.at17 10) ∧ Audit.timely Audit.c201.submission (Audit.at17 10)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target013.lean) · [Actual proof log](logs/target-013.log)

### Recommendation

Retain the finding and explain the inclusive boundary.

## VD-03

### Exact report claim

`input/report.md#VD-03`

> **VD-03.** Revision 2 governs D-202 because its internal assignment occurred after revision 2 became effective.

### Verification question

Does D-202 receive revision 2 because assignment followed the effective instant?

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

- V1-01 and V2-01 choose revision by accepted receipt before versus at/after 2028-03-01 00:00 UTC; assignment and export date are immaterial.

### Assumptions

- The accepted register and supplied fictional rules are faithful inputs; the audit does not authenticate their historical accuracy.
- Gregorian UTC dates use receipt day zero and inclusive 17:00 deadlines; no working-day rollover is permitted.

### Reasoning

- 1. C02 accepted receipt is February 29 23:59, minute 14399; March 1 00:00 is minute 14400.
- 2. Receipt is one minute before the boundary, so revision 1 is retained.
- 3. The assignment-based inference uses the wrong event. T01 independently explains why its revision-2 dashboard label is not a competing applicability rule.
- 4. The model establishes revision 1 and explicitly denies revision 2 for this in-scope case.

### Limits

- The conclusion is conditional on accurate supplied records and the stated W-6 scope; it does not certify source authenticity or apply outside these four cases.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.version202Refuted` in module `Audit` (refutes): `Audit.revision Audit.c202 ≠ 2 ∧ Audit.revision Audit.c202 = 1`.
  [Model](models/Audit.lean) · [Executed check](checks/Target014.lean) · [Actual proof log](logs/target-014.log)

### Recommendation

Replace revision 2 with revision 1 and select the version from accepted receipt.

## VD-04

### Exact report claim

`input/report.md#VD-04`

> **VD-04.** D-202's deadline was 2028-03-10 17:00 UTC.

### Verification question

Is D-202 deadline March 10 17:00 despite its report misclassifying the revision?

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

- V1-01 and V2-01 choose revision by accepted receipt before versus at/after 2028-03-01 00:00 UTC; assignment and export date are immaterial.
- V1-02 grants standard revision-1 cases 10 calendar days; V2-02 grants standard revision-2 cases 7 calendar days, receipt date day zero, at 17:00 UTC inclusive.

### Assumptions

- The accepted register and supplied fictional rules are faithful inputs; the audit does not authenticate their historical accuracy.
- Gregorian UTC dates use receipt day zero and inclusive 17:00 deadlines; no working-day rollover is permitted.

### Reasoning

- 1. D-202 is standard and its February 29 accepted receipt selects revision 1.
- 2. February 29 is offset 9. Adding ten calendar dates gives offset 19, March 10.
- 3. The deadline is March 10 17:00, minute 28380. This exact deadline is independently supported even though VD-03 provides an incompatible version premise.

### Limits

- Independent source reconstruction supports the date. The surrounding report contains a version error; support for this date does not validate that explanation.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.deadline202` in module `Audit` (supports): `Audit.standardDue Audit.c202 = some (Audit.at17 19)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target015.lean) · [Actual proof log](logs/target-015.log)

### Recommendation

Retain the date, but explain that revision 1 and its ten-day rule establish it; repair VD-03.

## VD-05

### Exact report claim

`input/report.md#VD-05`

> **VD-05.** D-202's submission was timely.

### Verification question

Was D-202 submission at March 10 17:01 within its inclusive 17:00 deadline?

### Source evidence

- [input/sources/case-register.md](input/sources/case-register.md) — `C02`

> D-202 is a standard case. Accepted receipt: 2028-02-29 23:59 UTC. Internal assignment: 2028-03-01 08:30 UTC. Submission: 2028-03-10 17:01 UTC. No receipt correction is recorded.

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-01`

> Revision 1 applies to cases received before 2028-03-01 00:00 UTC, including cases still open after that instant. Receipt is the timestamp of the intake service's accepted receipt, not the later internal assignment timestamp.

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-02`

> For a standard case under revision 1, submission is due 10 calendar days after its receipt date, at 17:00 UTC on that date, inclusive. Receipt date is day zero. There is no weekend or holiday adjustment. This rule's calendar convention matches the audit brief.

### Rules

- V1-01 and V2-01 choose revision by accepted receipt before versus at/after 2028-03-01 00:00 UTC; assignment and export date are immaterial.
- V1-02 grants standard revision-1 cases 10 calendar days; V2-02 grants standard revision-2 cases 7 calendar days, receipt date day zero, at 17:00 UTC inclusive.

### Assumptions

- The accepted register and supplied fictional rules are faithful inputs; the audit does not authenticate their historical accuracy.
- Gregorian UTC dates use receipt day zero and inclusive 17:00 deadlines; no working-day rollover is permitted.

### Reasoning

- 1. The correct revision-1 deadline is March 10 at 17:00, minute 28380.
- 2. The recorded submission is March 10 17:01, minute 28381.
- 3. 28381 exceeds 28380; inclusive 17:00 does not admit 17:01. D-202 is the direct in-scope counterexample to its timeliness assertion.

### Limits

- The conclusion is conditional on accurate supplied records and the stated W-6 scope; it does not certify source authenticity or apply outside these four cases.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.timely202Refuted` in module `Audit` (refutes): `Audit.standardDue Audit.c202 = some (Audit.at17 19) ∧ ¬ Audit.timely Audit.c202.submission (Audit.at17 19)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target016.lean) · [Actual proof log](logs/target-016.log)

### Recommendation

Replace timely with late by one minute.

## VD-06a

### Exact report claim

`input/report.md#VD-06`

> **VD-06.** Revision 2 governs D-203, and its submission at 2028-03-08 17:00 UTC was timely.

### Verification question

Does accepted receipt at the exact transition instant put D-203 under revision 2?

### Source evidence

- [input/sources/case-register.md](input/sources/case-register.md) — `C03`

> D-203 is a standard case. Accepted receipt: 2028-03-01 00:00 UTC. Internal assignment: 2028-03-01 08:45 UTC. Submission: 2028-03-08 17:00 UTC. No receipt correction is recorded.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-01`

> Revision 2 takes effect at 2028-03-01 00:00 UTC and applies to cases received at or after that instant. Cases received earlier retain revision 1 even if assigned, reviewed, or submitted after revision 2 becomes effective. Intake accepted receipt determines applicability. The boundary instant belongs to revision 2. This transition clause supersedes any informal dashboard version label.

### Rules

- V1-01 and V2-01 choose revision by accepted receipt before versus at/after 2028-03-01 00:00 UTC; assignment and export date are immaterial.

### Assumptions

- The accepted register and supplied fictional rules are faithful inputs; the audit does not authenticate their historical accuracy.
- Gregorian UTC dates use receipt day zero and inclusive 17:00 deadlines; no working-day rollover is permitted.

### Reasoning

- 1. C03 accepted receipt is exactly March 1 00:00, minute 14400.
- 2. The explicit at-or-after transition includes the boundary instant.
- 3. Revision 2 governs D-203, independently of assignment.

### Limits

- The conclusion is conditional on accurate supplied records and the stated W-6 scope; it does not certify source authenticity or apply outside these four cases.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.version203` in module `Audit` (supports): `Audit.revision Audit.c203 = 2`.
  [Model](models/Audit.lean) · [Executed check](checks/Target017.lean) · [Actual proof log](logs/target-017.log)

### Recommendation

Retain the version statement and cite the inclusive transition clause.

## VD-06b

### Exact report claim

`input/report.md#VD-06`

> **VD-06.** Revision 2 governs D-203, and its submission at 2028-03-08 17:00 UTC was timely.

### Verification question

Was standard D-203 submission at March 8 17:00 timely under revision 2?

### Source evidence

- [input/sources/case-register.md](input/sources/case-register.md) — `C03`

> D-203 is a standard case. Accepted receipt: 2028-03-01 00:00 UTC. Internal assignment: 2028-03-01 08:45 UTC. Submission: 2028-03-08 17:00 UTC. No receipt correction is recorded.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-01`

> Revision 2 takes effect at 2028-03-01 00:00 UTC and applies to cases received at or after that instant. Cases received earlier retain revision 1 even if assigned, reviewed, or submitted after revision 2 becomes effective. Intake accepted receipt determines applicability. The boundary instant belongs to revision 2. This transition clause supersedes any informal dashboard version label.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-02`

> For a standard case under revision 2, submission is due 7 calendar days after its receipt date, at 17:00 UTC on that date, inclusive. Receipt date is day zero. There is no weekend or holiday adjustment.

### Rules

- V1-01 and V2-01 choose revision by accepted receipt before versus at/after 2028-03-01 00:00 UTC; assignment and export date are immaterial.
- V1-02 grants standard revision-1 cases 10 calendar days; V2-02 grants standard revision-2 cases 7 calendar days, receipt date day zero, at 17:00 UTC inclusive.

### Assumptions

- The accepted register and supplied fictional rules are faithful inputs; the audit does not authenticate their historical accuracy.
- Gregorian UTC dates use receipt day zero and inclusive 17:00 deadlines; no working-day rollover is permitted.

### Reasoning

- 1. D-203 is standard and received at the revision-2 boundary.
- 2. March 1 is offset 10. Receipt day zero plus seven dates is offset 17, March 8.
- 3. Its March 8 17:00 submission equals the inclusive deadline, so it is timely.

### Limits

- The conclusion is conditional on accurate supplied records and the stated W-6 scope; it does not certify source authenticity or apply outside these four cases.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.timely203` in module `Audit` (supports): `Audit.standardDue Audit.c203 = some (Audit.at17 17) ∧ Audit.timely Audit.c203.submission (Audit.at17 17)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target018.lean) · [Actual proof log](logs/target-018.log)

### Recommendation

Retain the timely finding; cite the seven-day rule and receipt-day-zero convention.

## VD-07

### Exact report claim

`input/report.md#VD-07`

> **VD-07.** The submission deadline for D-203 was 2028-03-07 17:00 UTC because its receipt date counts as day one.

### Verification question

Can receipt-day-one counting justify March 7 17:00 as D-203 deadline?

### Source evidence

- [input/sources/case-register.md](input/sources/case-register.md) — `C03`

> D-203 is a standard case. Accepted receipt: 2028-03-01 00:00 UTC. Internal assignment: 2028-03-01 08:45 UTC. Submission: 2028-03-08 17:00 UTC. No receipt correction is recorded.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-01`

> Revision 2 takes effect at 2028-03-01 00:00 UTC and applies to cases received at or after that instant. Cases received earlier retain revision 1 even if assigned, reviewed, or submitted after revision 2 becomes effective. Intake accepted receipt determines applicability. The boundary instant belongs to revision 2. This transition clause supersedes any informal dashboard version label.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-02`

> For a standard case under revision 2, submission is due 7 calendar days after its receipt date, at 17:00 UTC on that date, inclusive. Receipt date is day zero. There is no weekend or holiday adjustment.

### Rules

- V1-01 and V2-01 choose revision by accepted receipt before versus at/after 2028-03-01 00:00 UTC; assignment and export date are immaterial.
- V1-02 grants standard revision-1 cases 10 calendar days; V2-02 grants standard revision-2 cases 7 calendar days, receipt date day zero, at 17:00 UTC inclusive.

### Assumptions

- The accepted register and supplied fictional rules are faithful inputs; the audit does not authenticate their historical accuracy.
- Gregorian UTC dates use receipt day zero and inclusive 17:00 deadlines; no working-day rollover is permitted.

### Reasoning

- 1. V2-02 explicitly makes receipt date day zero; the report instead counts it as day one.
- 2. Seven dates after March 1 is March 8 (offset 17), not March 7 (offset 16).
- 3. The model checks the actual deadline and its inequality with the claimed March 7 deadline, so this is a direct refutation, not merely missing support.

### Limits

- The conclusion is conditional on accurate supplied records and the stated W-6 scope; it does not certify source authenticity or apply outside these four cases.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.deadline203Refuted` in module `Audit` (refutes): `Audit.standardDue Audit.c203 ≠ some (Audit.at17 16) ∧ Audit.standardDue Audit.c203 = some (Audit.at17 17)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target019.lean) · [Actual proof log](logs/target-019.log)

### Recommendation

Correct the deadline to March 8 17:00 and count receipt as day zero.

## VD-08

### Exact report claim

`input/report.md#VD-08`

> **VD-08.** D-204's final submission deadline was 2028-03-09 17:00 UTC.

### Verification question

Does supplied evidence determine D-204 final deadline as March 9 17:00?

### Source evidence

- [input/sources/case-register.md](input/sources/case-register.md) — `C04`

> D-204 is a restricted case. Accepted receipt: 2028-03-02 10:00 UTC. Internal assignment: 2028-03-02 11:00 UTC. Submission: 2028-03-12 16:00 UTC. A pause request was filed on 2028-03-04, but no pause decision or Annex R text is supplied. Filing the request is the only established pause-related event.

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-03`

> For a restricted case, the deadline and any pausing rules are determined exclusively by Annex R. The standard-case rule V1-02 does not apply to restricted cases. Annex R is a separate normative attachment, not reproduced here.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-01`

> Revision 2 takes effect at 2028-03-01 00:00 UTC and applies to cases received at or after that instant. Cases received earlier retain revision 1 even if assigned, reviewed, or submitted after revision 2 becomes effective. Intake accepted receipt determines applicability. The boundary instant belongs to revision 2. This transition clause supersedes any informal dashboard version label.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-03`

> For a restricted case, the deadline and pausing rules continue to be governed exclusively by Annex R. Nothing in revision 2 substitutes the seven-day standard-case rule for Annex R. This amendment is the only supplied change to revision 1.

- [input/sources/transfer-note.md](input/sources/transfer-note.md) — `T02`

> The supplied package contains revisions 1 and 2, the transition amendment, the case register, and this transfer note. Annex R was not transferred. No source states its deadline duration, calendar basis, or pause criteria, nor that any pause was approved for D-204. The package supplies no independent final due date for D-204.

### Rules

- V1-03 and V2-03 reserve restricted-case deadlines and pause criteria exclusively to Annex R; standard deadlines cannot be substituted.
- The supplied file inventory is not completeness evidence for Annex R rules or pause decisions.

### Assumptions

- The accepted register and supplied fictional rules are faithful inputs; the audit does not authenticate their historical accuracy.
- Gregorian UTC dates use receipt day zero and inclusive 17:00 deadlines; no working-day rollover is permitted.

### Reasoning

- 1. D-204 is restricted; its March 2 receipt places it under revision 2, but V2-03 excludes the seven-day standard rule.
- 2. March 9 would result from borrowing the standard seven-day formula. That borrowing is unauthorized; no report citation or independent supplied source gives a restricted duration.
- 3. C04 establishes a filed pause request only, while T02 supplies neither Annex R nor an independent final deadline.
- 4. Hypothetical Annex R deadlines March 9 17:00 and March 13 17:00 both leave the recorded receipt and submission unchanged and contradict no supplied restricted duration. Their differing dates demonstrate unresolved precision.

### Limits

- Annex R is absent. The model cannot determine the actual restricted deadline, pause criteria, or whether a pause was approved.
- The existential theorem compares hypothetical completions of missing Annex R data. It is auxiliary non-entailment evidence, not proof that either hypothetical deadline is legally operative or that the report assertion is false.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **auxiliary**.

### Formal evidence

- `Audit.restrictedDeadlineOpen` in module `Audit` (auxiliary): `Audit.standardDue Audit.c204 = none ∧ ∃ early late : Nat, early = Audit.at17 18 ∧ late ≠ Audit.at17 18 ∧ ¬ Audit.timely Audit.c204.submission early ∧ Audit.timely Audit.c204.submission late`.
  [Model](models/Audit.lean) · [Executed check](checks/Target020.lean) · [Actual proof log](logs/target-020.log)

### Recommendation

Obtain Annex R applicable to D-204 and relevant pause decisions before publishing a final deadline.

## VD-09

### Exact report claim

`input/report.md#VD-09`

> **VD-09.** D-204's submission was timely.

### Verification question

Does D-204 recorded March 12 16:00 submission establish timeliness with no Annex R deadline?

### Source evidence

- [input/sources/case-register.md](input/sources/case-register.md) — `C04`

> D-204 is a restricted case. Accepted receipt: 2028-03-02 10:00 UTC. Internal assignment: 2028-03-02 11:00 UTC. Submission: 2028-03-12 16:00 UTC. A pause request was filed on 2028-03-04, but no pause decision or Annex R text is supplied. Filing the request is the only established pause-related event.

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-03`

> For a restricted case, the deadline and any pausing rules are determined exclusively by Annex R. The standard-case rule V1-02 does not apply to restricted cases. Annex R is a separate normative attachment, not reproduced here.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-03`

> For a restricted case, the deadline and pausing rules continue to be governed exclusively by Annex R. Nothing in revision 2 substitutes the seven-day standard-case rule for Annex R. This amendment is the only supplied change to revision 1.

- [input/sources/transfer-note.md](input/sources/transfer-note.md) — `T02`

> The supplied package contains revisions 1 and 2, the transition amendment, the case register, and this transfer note. Annex R was not transferred. No source states its deadline duration, calendar basis, or pause criteria, nor that any pause was approved for D-204. The package supplies no independent final due date for D-204.

### Rules

- V1-03 and V2-03 reserve restricted-case deadlines and pause criteria exclusively to Annex R; standard deadlines cannot be substituted.
- The supplied file inventory is not completeness evidence for Annex R rules or pause decisions.

### Assumptions

- The accepted register and supplied fictional rules are faithful inputs; the audit does not authenticate their historical accuracy.
- Gregorian UTC dates use receipt day zero and inclusive 17:00 deadlines; no working-day rollover is permitted.

### Reasoning

- 1. C04 fixes the submission at March 12 16:00 but supplies no final restricted deadline.
- 2. A pause request is established; approval and its effect are not. Absence of a supplied approval decision cannot be converted into proof that approval never occurred.
- 3. Independent review of all supplied rules and T02 finds no duration, calendar basis, pause criteria or final due date.
- 4. With hypothetical March 9 17:00 deadline, the recorded submission is late; with hypothetical March 13 17:00 deadline, it is timely. The auxiliary model holds all observed case data constant and demonstrates why present information determines neither outcome.

### Limits

- Annex R is absent. The model cannot determine the actual restricted deadline, pause criteria, or whether a pause was approved.
- The existential theorem compares hypothetical completions of missing Annex R data. It is auxiliary non-entailment evidence, not proof that either hypothetical deadline is legally operative or that the report assertion is false.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **auxiliary**.

### Formal evidence

- `Audit.restrictedDeadlineOpen` in module `Audit` (auxiliary): `Audit.standardDue Audit.c204 = none ∧ ∃ early late : Nat, early = Audit.at17 18 ∧ late ≠ Audit.at17 18 ∧ ¬ Audit.timely Audit.c204.submission early ∧ Audit.timely Audit.c204.submission late`.
  [Model](models/Audit.lean) · [Executed check](checks/Target020.lean) · [Actual proof log](logs/target-020.log)

### Recommendation

Obtain the applicable Annex R and evidence of any deadline adjustments; then compare the exact submission timestamp to the final deadline.

## VD-10

### Exact report claim

`input/report.md#VD-10`

> **VD-10.** Revision 2 gives applicants a fairer timetable than revision 1.

### Verification question

Is revision 2 objectively fairer for applicants under any supplied evaluable criterion?

### Source evidence

- [input/sources/rule-v1.md](input/sources/rule-v1.md) — `V1-02`

> For a standard case under revision 1, submission is due 10 calendar days after its receipt date, at 17:00 UTC on that date, inclusive. Receipt date is day zero. There is no weekend or holiday adjustment. This rule's calendar convention matches the audit brief.

- [input/sources/rule-v2-and-amendment.md](input/sources/rule-v2-and-amendment.md) — `V2-02`

> For a standard case under revision 2, submission is due 7 calendar days after its receipt date, at 17:00 UTC on that date, inclusive. Receipt date is day zero. There is no weekend or holiday adjustment.

- [input/sources/transfer-note.md](input/sources/transfer-note.md) — `T03`

> The service team calls the revision 2 timetable “fairer” in an informal comment. Neither rule defines fairness, supplies a metric, or specifies a population against which that comparison should be evaluated.

### Rules

- A substantive fairness comparison requires an operational criterion, affected population and relevant outcomes; no such criterion is supplied.

### Assumptions

- The accepted register and supplied fictional rules are faithful inputs; the audit does not authenticate their historical accuracy.
- Gregorian UTC dates use receipt day zero and inclusive 17:00 deadlines; no working-day rollover is permitted.

### Reasoning

- 1. The standard duration changes from ten days to seven; this numerical change alone does not define fairness.
- 2. T03 attributes the word fairer to an informal service-team comment. Attribution establishes that the comment was made, not the underlying value judgment.
- 3. No measurable criterion or comparison population supports a formal truth test for the exact claim.

### Limits

- No Lean target is proposed for the undefined fairness judgment. This does not refute the opinion or settle whether applicants prefer one timetable.

### Result

Semantic state: **not_applicable**; argument status: **nonformal**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Attribute the opinion to the service team or specify a fairness criterion and evidence before presenting a comparative finding.
