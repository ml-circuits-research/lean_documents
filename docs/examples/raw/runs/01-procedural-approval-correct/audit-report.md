# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

[Semantic correspondence review](semantic-review.md)

## PA-C01

### Exact report claim

`input/report.md#PA-C01`

> **PA-C01.** C-101 satisfied the standard authorization path: its 08:40 duty-manager approval was strictly before its 09:00 start.

### Verification question

Did C-101 meet P-17 standard approval strictly before its recorded 2028-04-10 start?

### Source evidence

- [input/sources/register.md](input/sources/register.md) — `R01`

> This extract is a complete record of requests, duty-manager approvals, start timestamps, qualifying incident determinations, emergency declarations, and countersignatures for C-101, C-102, C-103, and C-104 through 2028-04-12 17:00 UTC. In this extract “none” means the specified event did not occur during that coverage period. The register gives recorded starts as facts for those four operations. C-105 is not covered by this register; its external authority records were not received. Completeness must not be extended to C-105.

- [input/sources/register.md](input/sources/register.md) — `R02`

> C-101: request submitted 2028-04-10 08:20 UTC; duty-manager approval granted 2028-04-10 08:40 UTC; start 2028-04-10 09:00 UTC. Qualifying active incident: no. Emergency declaration: none. Countersignature: none.

- [input/sources/policy.md](input/sources/policy.md) — `P01`

> P-17 revision 3 governs all five operations C-101 through C-105 for the entire period covered by this dossier. There is no applicable superseding policy in this fixture. “Authorized start” means satisfying either the standard path P02 or the emergency path P03; these are the only two paths. An emergency path is fully established only when every P03 condition is met.

- [input/sources/policy.md](input/sources/policy.md) — `P02`

> The standard path requires an approval explicitly granted by the duty manager strictly before the operation starts. Submitting or acknowledging a request does not grant approval. Approval at the exact starting timestamp is not strictly before start.

### Rules

- P02 requires a granted duty-manager approval strictly before start.

### Assumptions

- The synthetic supplied records and normative P-17 revision 3 are accepted for documentary assessment, not independently authenticated.
- Timestamps are exact UTC minutes; before is strict and the 24-hour window includes both endpoints (brief B02).

### Reasoning

- 1. R02 records a granted approval at 08:40 and a start at 09:00 on the same day.
- 2. 520 minutes is strictly less than 540 minutes from the UTC day origin.
- 3. The specified officer and timing satisfy the standard path; R02 contains no contrary approval or start record.

### Limits

- This establishes fictional policy compliance for the recorded operation, not source authenticity.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.c01` in module `Audit` (supports): `Audit.Standard Audit.c101 ∧ (520 < 540)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target007.lean) · [Actual proof log](logs/target-007.log)

### Recommendation

Retain the finding with the explicit R02 and P02 citations.

## PA-C02

### Exact report claim

`input/report.md#PA-C02`

> **PA-C02.** C-102 had no standard duty-manager approval in the register coverage period; its 10:00 request was not an approval.

### Verification question

Does the complete covered register establish no standard approval for C-102 and distinguish its request from a grant?

### Source evidence

- [input/sources/register.md](input/sources/register.md) — `R01`

> This extract is a complete record of requests, duty-manager approvals, start timestamps, qualifying incident determinations, emergency declarations, and countersignatures for C-101, C-102, C-103, and C-104 through 2028-04-12 17:00 UTC. In this extract “none” means the specified event did not occur during that coverage period. The register gives recorded starts as facts for those four operations. C-105 is not covered by this register; its external authority records were not received. Completeness must not be extended to C-105.

- [input/sources/register.md](input/sources/register.md) — `R03`

> C-102: request submitted 2028-04-10 10:00 UTC; duty-manager standard approval: none; start 2028-04-10 10:15 UTC. Qualifying active incident: yes, incident I-62 was active at start. Duty-officer emergency declaration 2028-04-10 10:05 UTC. Duty-manager countersignature 2028-04-11 10:15 UTC.

- [input/sources/policy.md](input/sources/policy.md) — `P02`

> The standard path requires an approval explicitly granted by the duty manager strictly before the operation starts. Submitting or acknowledging a request does not grant approval. Approval at the exact starting timestamp is not strictly before start.

### Rules

- R01 explicitly gives none negative-event meaning for C-102 within the coverage period.
- P02 distinguishes requesting from granting approval.

### Assumptions

- The synthetic supplied records and normative P-17 revision 3 are accepted for documentary assessment, not independently authenticated.
- Timestamps are exact UTC minutes; before is strict and the 24-hour window includes both endpoints (brief B02).

### Reasoning

- 1. R03 explicitly records standard approval as none and identifies the 10:00 entry as a request.
- 2. R01 permits the negative approval assertion only for the covered operation and period.
- 3. The model preserves none as covered absence and request as a distinct record kind; the request cannot supply the missing standard approval.

### Limits

- The negative assertion is bounded by register coverage through 2028-04-12 17:00 UTC; none must not be reused for unknown C-105 facts.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.c02` in module `Audit` (supports): `Audit.c102.approval = none ∧ Audit.RecordKind.request ≠ Audit.RecordKind.approval`.
  [Model](models/Audit.lean) · [Executed check](checks/Target008.lean) · [Actual proof log](logs/target-008.log)

### Recommendation

Retain the scope and the explicit distinction between request and approval.

## PA-C03

### Exact report claim

`input/report.md#PA-C03`

> **PA-C03.** C-102 satisfied the emergency authorization path. Its qualifying incident, pre-start declaration, and countersignature exactly 24 hours after start meet all three conditions.

### Verification question

Do all three P03 conditions hold for C-102, including the inclusive upper boundary?

### Source evidence

- [input/sources/register.md](input/sources/register.md) — `R03`

> C-102: request submitted 2028-04-10 10:00 UTC; duty-manager standard approval: none; start 2028-04-10 10:15 UTC. Qualifying active incident: yes, incident I-62 was active at start. Duty-officer emergency declaration 2028-04-10 10:05 UTC. Duty-manager countersignature 2028-04-11 10:15 UTC.

- [input/sources/policy.md](input/sources/policy.md) — `P01`

> P-17 revision 3 governs all five operations C-101 through C-105 for the entire period covered by this dossier. There is no applicable superseding policy in this fixture. “Authorized start” means satisfying either the standard path P02 or the emergency path P03; these are the only two paths. An emergency path is fully established only when every P03 condition is met.

- [input/sources/policy.md](input/sources/policy.md) — `P03`

> The emergency path requires all of: a qualifying active incident, a duty officer's emergency declaration strictly before start, and a duty manager's countersignature at or after start and no later than 24 hours after start. This path permits a start without a standard approval. The declaration alone does not complete this path.

### Rules

- P03 requires an active qualifying incident, a declaration strictly before start, and a countersignature in the closed interval from start to start plus 24 hours.

### Assumptions

- The synthetic supplied records and normative P-17 revision 3 are accepted for documentary assessment, not independently authenticated.
- Timestamps are exact UTC minutes; before is strict and the 24-hour window includes both endpoints (brief B02).

### Reasoning

- 1. R03 records active incident I-62, declaration at 10:05, and start at 10:15 on 10 April.
- 2. The declaration offset 605 is less than start offset 615. The 11 April 10:15 countersignature has offset 2055.
- 3. 2055 equals 615 plus 1440 minutes, satisfying both inclusive bounds. All conditions hold, so the emergency path is satisfied.

### Limits

- Emergency authorization is established once the countersignature condition is met, as assessed at the record cutoff; this is not a claim that every condition was already completed at start.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.c03` in module `Audit` (supports): `Audit.Emergency Audit.c102 ∧ Audit.c102.incident = true ∧ (605 < 615) ∧ (2055 = 615 + 1440)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target009.lean) · [Actual proof log](logs/target-009.log)

### Recommendation

Retain the inclusive deadline explanation and all three source-linked conditions.

## PA-C04

### Exact report claim

`input/report.md#PA-C04`

> **PA-C04.** C-103 failed the standard path because its approval and start were simultaneous; it also lacked the qualifying incident and declaration needed for the emergency path.

### Verification question

Did simultaneous approval fail P02 for C-103, and are emergency prerequisites explicitly absent?

### Source evidence

- [input/sources/register.md](input/sources/register.md) — `R01`

> This extract is a complete record of requests, duty-manager approvals, start timestamps, qualifying incident determinations, emergency declarations, and countersignatures for C-101, C-102, C-103, and C-104 through 2028-04-12 17:00 UTC. In this extract “none” means the specified event did not occur during that coverage period. The register gives recorded starts as facts for those four operations. C-105 is not covered by this register; its external authority records were not received. Completeness must not be extended to C-105.

- [input/sources/register.md](input/sources/register.md) — `R04`

> C-103: request submitted 2028-04-10 11:00 UTC; duty-manager approval granted 2028-04-10 11:30 UTC; start 2028-04-10 11:30 UTC. Qualifying active incident: no. Emergency declaration: none. Countersignature: none.

- [input/sources/policy.md](input/sources/policy.md) — `P02`

> The standard path requires an approval explicitly granted by the duty manager strictly before the operation starts. Submitting or acknowledging a request does not grant approval. Approval at the exact starting timestamp is not strictly before start.

- [input/sources/policy.md](input/sources/policy.md) — `P03`

> The emergency path requires all of: a qualifying active incident, a duty officer's emergency declaration strictly before start, and a duty manager's countersignature at or after start and no later than 24 hours after start. This path permits a start without a standard approval. The declaration alone does not complete this path.

### Rules

- Strict before excludes equality.
- The emergency path is a conjunction; incident and declaration cannot be omitted.

### Assumptions

- The synthetic supplied records and normative P-17 revision 3 are accepted for documentary assessment, not independently authenticated.
- Timestamps are exact UTC minutes; before is strict and the 24-hour window includes both endpoints (brief B02).

### Reasoning

- 1. R04 records both approval and start at 11:30, so both offsets are 690 and 690 is not less than 690.
- 2. R04 explicitly states qualifying incident no and emergency declaration none, within R01 completeness.
- 3. Thus the standard path fails and the required emergency prerequisites are absent; there is no unsupported inference from missing external material.

### Limits

- A recorded start is accepted under R01. No conclusion about prudence or non-P-17 requirements is made.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.c04` in module `Audit` (supports): `¬ Audit.Standard Audit.c103 ∧ Audit.c103.approval = some Audit.c103.start ∧ Audit.c103.incident = false ∧ Audit.c103.declaration = none ∧ ¬ Audit.Emergency Audit.c103`.
  [Model](models/Audit.lean) · [Executed check](checks/Target010.lean) · [Actual proof log](logs/target-010.log)

### Recommendation

Retain the equality boundary and the explicit negative evidence.

## PA-C05

### Exact report claim

`input/report.md#PA-C05`

> **PA-C05.** C-104 started without authorization under either of the two P-17 paths.

### Verification question

Did C-104 actually start while satisfying neither exhaustive P-17 authorization path?

### Source evidence

- [input/sources/register.md](input/sources/register.md) — `R01`

> This extract is a complete record of requests, duty-manager approvals, start timestamps, qualifying incident determinations, emergency declarations, and countersignatures for C-101, C-102, C-103, and C-104 through 2028-04-12 17:00 UTC. In this extract “none” means the specified event did not occur during that coverage period. The register gives recorded starts as facts for those four operations. C-105 is not covered by this register; its external authority records were not received. Completeness must not be extended to C-105.

- [input/sources/register.md](input/sources/register.md) — `R05`

> C-104: request submitted 2028-04-10 13:00 UTC; duty-manager approval: none; start 2028-04-10 13:20 UTC. Qualifying active incident: no. Emergency declaration: none. Countersignature: none.

- [input/sources/policy.md](input/sources/policy.md) — `P01`

> P-17 revision 3 governs all five operations C-101 through C-105 for the entire period covered by this dossier. There is no applicable superseding policy in this fixture. “Authorized start” means satisfying either the standard path P02 or the emergency path P03; these are the only two paths. An emergency path is fully established only when every P03 condition is met.

- [input/sources/policy.md](input/sources/policy.md) — `P02`

> The standard path requires an approval explicitly granted by the duty manager strictly before the operation starts. Submitting or acknowledging a request does not grant approval. Approval at the exact starting timestamp is not strictly before start.

- [input/sources/policy.md](input/sources/policy.md) — `P03`

> The emergency path requires all of: a qualifying active incident, a duty officer's emergency declaration strictly before start, and a duty manager's countersignature at or after start and no later than 24 hours after start. This path permits a start without a standard approval. The declaration alone does not complete this path.

### Rules

- P01 makes standard or emergency the exhaustive definition of authorized start.
- R01 certifies recorded starts and explicit none entries for C-104.

### Assumptions

- The synthetic supplied records and normative P-17 revision 3 are accepted for documentary assessment, not independently authenticated.
- Timestamps are exact UTC minutes; before is strict and the 24-hour window includes both endpoints (brief B02).

### Reasoning

- 1. R05 records a 13:20 start (offset 800), so the assertion is not vacuous about an operation that never began.
- 2. Approval none defeats the standard path. Incident no, declaration none, and countersignature none defeat the emergency path.
- 3. Because P01 supplies exactly two paths, failure of both establishes an unauthorized start under this policy.

### Limits

- The conclusion is bounded to fictional P-17 and the given complete records; it is not a legal or general operational judgment.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.c05` in module `Audit` (supports): `Audit.c104.start = 800 ∧ ¬ Audit.Authorized Audit.c104`.
  [Model](models/Audit.lean) · [Executed check](checks/Target011.lean) · [Actual proof log](logs/target-011.log)

### Recommendation

Retain the finding with the two-path exclusion argument.

## PA-C06

### Exact report claim

`input/report.md#PA-C06`

> **PA-C06.** The supplied C-105 evidence establishes neither presence nor absence of standard approval before the proposed 09:00 start.

### Verification question

Does supplied C-105 evidence establish either polarity of pre-start standard approval?

### Source evidence

- [input/sources/register.md](input/sources/register.md) — `R01`

> This extract is a complete record of requests, duty-manager approvals, start timestamps, qualifying incident determinations, emergency declarations, and countersignatures for C-101, C-102, C-103, and C-104 through 2028-04-12 17:00 UTC. In this extract “none” means the specified event did not occur during that coverage period. The register gives recorded starts as facts for those four operations. C-105 is not covered by this register; its external authority records were not received. Completeness must not be extended to C-105.

- [input/sources/handoff.md](input/sources/handoff.md) — `H01`

> C-105 was administered through the external North Quay unit. The handoff package contains a request sent at 2028-04-11 08:00 UTC, the two witness notes supplied in `attestations.md`, and no external approval register. This list is complete for what the handoff package contains, not for events that occurred at North Quay.

- [input/sources/handoff.md](input/sources/handoff.md) — `H02`

> The North Quay liaison states: “Approval and emergency records were not transferred. I cannot confirm or deny whether an approval, qualifying incident, declaration, or countersignature existed for C-105.” No start timestamp is certified in the handoff. The two witness notes refer to the same proposed operation, C-105, not to separate operations.

- [input/sources/attestations.md](input/sources/attestations.md) — `A01`

> Operator Mira Vale signed a note at 2028-04-11 12:00 UTC: “C-105 began at 09:00 UTC today. I was present when it began.” The note asserts that the operation began; it does not assert duty-manager approval or an emergency path.

- [input/sources/attestations.md](input/sources/attestations.md) — `A02`

> Observer Leon Reed signed a note at 2028-04-11 12:10 UTC: “C-105 did not begin at any time today before this note. The equipment stayed idle.” This explicitly denies a C-105 start at 09:00 UTC on 2028-04-11. No retraction, priority rule, or resolution of the disagreement is supplied.

- [input/sources/policy.md](input/sources/policy.md) — `P02`

> The standard path requires an approval explicitly granted by the duty manager strictly before the operation starts. Submitting or acknowledging a request does not grant approval. Approval at the exact starting timestamp is not strictly before start.

### Rules

- Register completeness explicitly excludes C-105.
- A request is not an approval; unknown external records establish neither presence nor absence.

### Assumptions

- The synthetic supplied records and normative P-17 revision 3 are accepted for documentary assessment, not independently authenticated.
- Timestamps are exact UTC minutes; before is strict and the 24-hour window includes both endpoints (brief B02).

### Reasoning

- 1. R01 excludes C-105. H01 supplies a request but no external register, and H02 explicitly cannot confirm or deny approval.
- 2. The two witness notes address whether the operation started, not whether approval was granted. Neither supplies the missing approval premise or a negative approval record.
- 3. Full search of all four supplied sources finds neither polarity. The report correctly states this evidence limit; it does not claim approval was absent.

### Limits

- Approval status and the proposed start remain unresolved outside the supplied corpus. This supported epistemic finding is not a formal proof of either event polarity.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Retain the uncertainty; obtain the external approval register and resolve the actual start before assessing standard authorization.

## PA-C07

### Exact report claim

`input/report.md#PA-C07`

> **PA-C07.** The two C-105 witness notes conflict: one asserts a 2028-04-11 09:00 start and the other explicitly denies any start before 12:10 that day. No supplied rule resolves the conflict.

### Verification question

Do the attributed notes contradict on the same proposed C-105 start, without a supplied resolution rule?

### Source evidence

- [input/sources/attestations.md](input/sources/attestations.md) — `A01`

> Operator Mira Vale signed a note at 2028-04-11 12:00 UTC: “C-105 began at 09:00 UTC today. I was present when it began.” The note asserts that the operation began; it does not assert duty-manager approval or an emergency path.

- [input/sources/attestations.md](input/sources/attestations.md) — `A02`

> Observer Leon Reed signed a note at 2028-04-11 12:10 UTC: “C-105 did not begin at any time today before this note. The equipment stayed idle.” This explicitly denies a C-105 start at 09:00 UTC on 2028-04-11. No retraction, priority rule, or resolution of the disagreement is supplied.

- [input/sources/handoff.md](input/sources/handoff.md) — `H02`

> The North Quay liaison states: “Approval and emergency records were not transferred. I cannot confirm or deny whether an approval, qualifying incident, declaration, or countersignature existed for C-105.” No start timestamp is certified in the handoff. The two witness notes refer to the same proposed operation, C-105, not to separate operations.

- [input/sources/policy.md](input/sources/policy.md) — `P04`

> P-17 prescribes no measure of whether a start was “prudent.” Authorization and prudence are separate assessments. The policy has no rule for resolving contradictory witness statements about an operation actually occurring.

### Rules

- Preserve speaker attribution and compare the same operation and time.
- P04 supplies no priority rule for conflicting witness statements.

### Assumptions

- The synthetic supplied records and normative P-17 revision 3 are accepted for documentary assessment, not independently authenticated.
- Timestamps are exact UTC minutes; before is strict and the 24-hour window includes both endpoints (brief B02).

### Reasoning

- 1. A01 asserts C-105 began at 09:00 on 11 April. A02 denies any start earlier than its 12:10 note and explicitly denies the 09:00 start.
- 2. H02 identifies the same proposed operation; this is not a mismatch between two operations.
- 3. P04 and A02 offer no resolution. The documentary conflict claim is supported, while the underlying start proposition has both positive and negative testimony.

### Limits

- No finding establishes which witness is correct, cryptographic authenticity, or actual start time. The supported status applies to the report claim that testimony conflicts, not to either incompatible event assertion.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Retain both quotations and obtain an independent start record or a justified reconciliation.

## PA-C08

### Exact report claim

`input/report.md#PA-C08`

> **PA-C08.** A lack of standard approval does not by itself make a start unauthorized under P-17; C-102 meets the alternative emergency path.

### Verification question

Is C-102 a concrete counterexample to inferring unauthorized start solely from no standard approval?

### Source evidence

- [input/sources/register.md](input/sources/register.md) — `R03`

> C-102: request submitted 2028-04-10 10:00 UTC; duty-manager standard approval: none; start 2028-04-10 10:15 UTC. Qualifying active incident: yes, incident I-62 was active at start. Duty-officer emergency declaration 2028-04-10 10:05 UTC. Duty-manager countersignature 2028-04-11 10:15 UTC.

- [input/sources/policy.md](input/sources/policy.md) — `P01`

> P-17 revision 3 governs all five operations C-101 through C-105 for the entire period covered by this dossier. There is no applicable superseding policy in this fixture. “Authorized start” means satisfying either the standard path P02 or the emergency path P03; these are the only two paths. An emergency path is fully established only when every P03 condition is met.

- [input/sources/policy.md](input/sources/policy.md) — `P02`

> The standard path requires an approval explicitly granted by the duty manager strictly before the operation starts. Submitting or acknowledging a request does not grant approval. Approval at the exact starting timestamp is not strictly before start.

- [input/sources/policy.md](input/sources/policy.md) — `P03`

> The emergency path requires all of: a qualifying active incident, a duty officer's emergency declaration strictly before start, and a duty manager's countersignature at or after start and no later than 24 hours after start. This path permits a start without a standard approval. The declaration alone does not complete this path.

### Rules

- P01 defines authorized as standard or emergency.
- P03 expressly permits an emergency path without standard approval.

### Assumptions

- The synthetic supplied records and normative P-17 revision 3 are accepted for documentary assessment, not independently authenticated.
- Timestamps are exact UTC minutes; before is strict and the 24-hour window includes both endpoints (brief B02).

### Reasoning

- 1. R03 supplies a concrete started operation with no standard approval.
- 2. Its qualifying incident, timely declaration, and countersignature at exactly the inclusive deadline satisfy P03.
- 3. Therefore this operation has no standard path yet has emergency authorization. It refutes the general inference from no standard approval to no authorization, and supports the report's qualified statement.

### Limits

- This witness does not imply every operation lacking standard approval is authorized; C-104 demonstrates the opposite possibility.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.c08` in module `Audit` (supports): `¬ Audit.Standard Audit.c102 ∧ Audit.Emergency Audit.c102 ∧ Audit.Authorized Audit.c102`.
  [Model](models/Audit.lean) · [Executed check](checks/Target012.lean) · [Actual proof log](logs/target-012.log)

### Recommendation

Retain the exception and the C-102 witness.

## PA-C09

### Exact report claim

`input/report.md#PA-C09`

> **PA-C09.** The policy supplies no criterion for deciding whether C-102 was prudent.

### Verification question

Does the complete supplied P-17 text define an operational prudence criterion for C-102?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P01`

> P-17 revision 3 governs all five operations C-101 through C-105 for the entire period covered by this dossier. There is no applicable superseding policy in this fixture. “Authorized start” means satisfying either the standard path P02 or the emergency path P03; these are the only two paths. An emergency path is fully established only when every P03 condition is met.

- [input/sources/policy.md](input/sources/policy.md) — `P02`

> The standard path requires an approval explicitly granted by the duty manager strictly before the operation starts. Submitting or acknowledging a request does not grant approval. Approval at the exact starting timestamp is not strictly before start.

- [input/sources/policy.md](input/sources/policy.md) — `P03`

> The emergency path requires all of: a qualifying active incident, a duty officer's emergency declaration strictly before start, and a duty manager's countersignature at or after start and no later than 24 hours after start. This path permits a start without a standard approval. The declaration alone does not complete this path.

- [input/sources/policy.md](input/sources/policy.md) — `P04`

> P-17 prescribes no measure of whether a start was “prudent.” Authorization and prudence are separate assessments. The policy has no rule for resolving contradictory witness statements about an operation actually occurring.

### Rules

- P04 expressly separates prudence from authorization and supplies no measure of prudence.

### Assumptions

- The synthetic supplied records and normative P-17 revision 3 are accepted for documentary assessment, not independently authenticated.
- Timestamps are exact UTC minutes; before is strict and the 24-hour window includes both endpoints (brief B02).

### Reasoning

- 1. The entire supplied policy P01–P04 was reviewed. P02 and P03 define authorization paths only.
- 2. P04 explicitly states no measure of prudence. The report accurately describes the policy limitation.
- 3. Neither prudent nor imprudent is established; introducing an operational measure would require an additional authorized criterion.

### Limits

- Documentary support for absence of a policy criterion is distinct from a formal or substantive assessment of prudence. No Lean theorem is claimed.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Retain the finding; obtain a defined prudence criterion only if that separate assessment is requested.

## PA-C10

### Exact report claim

`input/report.md#PA-C10`

> **PA-C10.** The supplied C-105 handoff package contains no external approval register. That inventory fact does not establish whether an external approval existed.

### Verification question

Does package-level absence of an external approval register leave historical approval existence unresolved?

### Source evidence

- [input/sources/handoff.md](input/sources/handoff.md) — `H01`

> C-105 was administered through the external North Quay unit. The handoff package contains a request sent at 2028-04-11 08:00 UTC, the two witness notes supplied in `attestations.md`, and no external approval register. This list is complete for what the handoff package contains, not for events that occurred at North Quay.

- [input/sources/handoff.md](input/sources/handoff.md) — `H02`

> The North Quay liaison states: “Approval and emergency records were not transferred. I cannot confirm or deny whether an approval, qualifying incident, declaration, or countersignature existed for C-105.” No start timestamp is certified in the handoff. The two witness notes refer to the same proposed operation, C-105, not to separate operations.

- [input/sources/register.md](input/sources/register.md) — `R01`

> This extract is a complete record of requests, duty-manager approvals, start timestamps, qualifying incident determinations, emergency declarations, and countersignatures for C-101, C-102, C-103, and C-104 through 2028-04-12 17:00 UTC. In this extract “none” means the specified event did not occur during that coverage period. The register gives recorded starts as facts for those four operations. C-105 is not covered by this register; its external authority records were not received. Completeness must not be extended to C-105.

### Rules

- Completeness of a package inventory applies to listed attachments, not external events.
- C-105 falls outside the complete event register.

### Assumptions

- The synthetic supplied records and normative P-17 revision 3 are accepted for documentary assessment, not independently authenticated.
- Timestamps are exact UTC minutes; before is strict and the 24-hour window includes both endpoints (brief B02).

### Reasoning

- 1. H01 expressly lists the complete handoff contents and states no external approval register is included.
- 2. H01 limits that completeness to package contents, and H02 cannot confirm or deny external approval. R01 supplies no C-105 event completeness.
- 3. The inventory absence is supported, but approval existence or nonexistence cannot follow from that inventory fact. The report preserves the correct boundary.

### Limits

- This is a documentary assessment of package contents and inferential limits; neither historical polarity is proved and no Lean result is claimed.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Retain the distinction and request external authority records to resolve approval history.
