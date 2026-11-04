# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

[Semantic correspondence review](semantic-review.md)

## PA-01

### Exact report claim

`input/report.md#PA-01`

> **PA-01.** C-101 satisfied the standard authorization path because its duty-manager approval preceded its start.

### Verification question

Did C-101 satisfy the P-17 revision 3 standard path at its recorded 2028-04-10 09:00 UTC start, and was its explicitly granted duty-manager approval strictly earlier?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P01`

> P-17 revision 3 governs all five operations C-101 through C-105 for the entire period covered by this dossier. There is no applicable superseding policy in this fixture. “Authorized start” means satisfying either the standard path P02 or the emergency path P03; these are the only two paths. An emergency path is fully established only when every P03 condition is met.

- [input/sources/policy.md](input/sources/policy.md) — `P02`

> The standard path requires an approval explicitly granted by the duty manager strictly before the operation starts. Submitting or acknowledging a request does not grant approval. Approval at the exact starting timestamp is not strictly before start.

- [input/sources/register.md](input/sources/register.md) — `R01`

> This extract is a complete record of requests, duty-manager approvals, start timestamps, qualifying incident determinations, emergency declarations, and countersignatures for C-101, C-102, C-103, and C-104 through 2028-04-12 17:00 UTC. In this extract “none” means the specified event did not occur during that coverage period. The register gives recorded starts as facts for those four operations. C-105 is not covered by this register; its external authority records were not received. Completeness must not be extended to C-105.

- [input/sources/register.md](input/sources/register.md) — `R02`

> C-101: request submitted 2028-04-10 08:20 UTC; duty-manager approval granted 2028-04-10 08:40 UTC; start 2028-04-10 09:00 UTC. Qualifying active incident: no. Emergency declaration: none. Countersignature: none.

### Rules

- P02 requires a duty-manager grant strictly before start. P01 makes the standard path sufficient for authorized start.

### Assumptions

- The supplied register is accepted as documentary fact within R01 coverage, and its exact event labels and UTC timestamps are faithfully transcribed; authenticity is not independently established.

### Reasoning

- 1. R02 records a duty-manager grant at 08:40 and actual start at 09:00 on the same UTC date.
- 2. The grant precedes the start by 20 minutes: offsets 520 < 540.
- 3. Both the stated ordering and standard-path conclusion follow; there is no missing conjunct in P02.

### Limits

- This is compliance under fictional P-17 revision 3 only, not an assessment of other policies or prudence.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim01` in module `Audit` (supports): `Audit.standard Audit.c101 = true ∧ (520 : Int) < 540`.
  [Model](models/Audit.lean) · [Executed check](checks/Target010.lean) · [Actual proof log](logs/target-010.log)

### Recommendation

Retain the conclusion and cite R02 and P02.

## PA-02

### Exact report claim

`input/report.md#PA-02`

> **PA-02.** C-102 had a standard duty-manager approval before starting; its 10:00 request was that approval.

### Verification question

Did C-102 have a standard duty-manager grant strictly before its 2028-04-10 10:15 UTC start, and can its 10:00 request count as that grant?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P02`

> The standard path requires an approval explicitly granted by the duty manager strictly before the operation starts. Submitting or acknowledging a request does not grant approval. Approval at the exact starting timestamp is not strictly before start.

- [input/sources/register.md](input/sources/register.md) — `R01`

> This extract is a complete record of requests, duty-manager approvals, start timestamps, qualifying incident determinations, emergency declarations, and countersignatures for C-101, C-102, C-103, and C-104 through 2028-04-12 17:00 UTC. In this extract “none” means the specified event did not occur during that coverage period. The register gives recorded starts as facts for those four operations. C-105 is not covered by this register; its external authority records were not received. Completeness must not be extended to C-105.

- [input/sources/register.md](input/sources/register.md) — `R03`

> C-102: request submitted 2028-04-10 10:00 UTC; duty-manager standard approval: none; start 2028-04-10 10:15 UTC. Qualifying active incident: yes, incident I-62 was active at start. Duty-officer emergency declaration 2028-04-10 10:05 UTC. Duty-manager countersignature 2028-04-11 10:15 UTC.

### Rules

- P02 explicitly separates submitting or acknowledging a request from granting approval. R01 permits treating the explicit covered none as negative evidence.

### Assumptions

- The supplied register is accepted as documentary fact within R01 coverage, and its exact event labels and UTC timestamps are faithfully transcribed; authenticity is not independently established.

### Reasoning

- 1. R03 records the 10:00 request, actual start at 10:15, and standard approval: none.
- 2. A request being earlier than start does not make it an approval; the event-kind requirement fails.
- 3. The covered explicit absence refutes a pre-start standard grant independently of the request/grant distinction. Both assertions in the report fail.

### Limits

- Failure of the standard path alone does not determine overall authorization; the emergency path is assessed separately in PA-03 and PA-08.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim02` in module `Audit` (refutes): `Audit.standard Audit.c102 = false ∧ Audit.c102Request ≠ Audit.EventKind.approval`.
  [Model](models/Audit.lean) · [Executed check](checks/Target011.lean) · [Actual proof log](logs/target-011.log)

### Recommendation

Replace with: C-102 had a pre-start request but no standard duty-manager approval; assess the emergency path separately.

## PA-03

### Exact report claim

`input/report.md#PA-03`

> **PA-03.** C-102 satisfied the emergency authorization path, including a countersignature within 24 hours after start.

### Verification question

Did C-102 meet every P03 condition, including a countersignature at or after actual start and at or before exactly 24 hours later?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P01`

> P-17 revision 3 governs all five operations C-101 through C-105 for the entire period covered by this dossier. There is no applicable superseding policy in this fixture. “Authorized start” means satisfying either the standard path P02 or the emergency path P03; these are the only two paths. An emergency path is fully established only when every P03 condition is met.

- [input/sources/policy.md](input/sources/policy.md) — `P03`

> The emergency path requires all of: a qualifying active incident, a duty officer's emergency declaration strictly before start, and a duty manager's countersignature at or after start and no later than 24 hours after start. This path permits a start without a standard approval. The declaration alone does not complete this path.

- [input/sources/register.md](input/sources/register.md) — `R01`

> This extract is a complete record of requests, duty-manager approvals, start timestamps, qualifying incident determinations, emergency declarations, and countersignatures for C-101, C-102, C-103, and C-104 through 2028-04-12 17:00 UTC. In this extract “none” means the specified event did not occur during that coverage period. The register gives recorded starts as facts for those four operations. C-105 is not covered by this register; its external authority records were not received. Completeness must not be extended to C-105.

- [input/sources/register.md](input/sources/register.md) — `R03`

> C-102: request submitted 2028-04-10 10:00 UTC; duty-manager standard approval: none; start 2028-04-10 10:15 UTC. Qualifying active incident: yes, incident I-62 was active at start. Duty-officer emergency declaration 2028-04-10 10:05 UTC. Duty-manager countersignature 2028-04-11 10:15 UTC.

### Rules

- P03 requires qualifying active incident AND pre-start duty-officer declaration AND duty-manager countersignature in the inclusive interval [start, start + 24 hours].

### Assumptions

- The supplied register is accepted as documentary fact within R01 coverage, and its exact event labels and UTC timestamps are faithfully transcribed; authenticity is not independently established.

### Reasoning

- 1. R03 records qualifying incident I-62 active at start, not merely an emergency declaration.
- 2. The duty-officer declaration at 10:05 on April 10 is strictly before the recorded 10:15 start.
- 3. The duty-manager countersignature at 10:15 on April 11 is exactly 1440 minutes after start; it meets both inclusive endpoints.
- 4. All P03 conditions hold. Lack of a standard grant does not defeat this permitted alternative.

### Limits

- The result uses the explicit inclusive deadline and exact-minute UTC convention; it does not support prudence.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim03` in module `Audit` (supports): `Audit.emergency Audit.c102 = true ∧ (2055 - 615 : Int) = 1440`.
  [Model](models/Audit.lean) · [Executed check](checks/Target012.lean) · [Actual proof log](logs/target-012.log)

### Recommendation

Retain the conclusion and explicitly identify the exactly-24-hour inclusive boundary.

## PA-04

### Exact report claim

`input/report.md#PA-04`

> **PA-04.** C-103 satisfied the standard authorization path because its approval was strictly before start.

### Verification question

Was C-103 duty-manager approval strictly before its recorded 2028-04-10 11:30 UTC start, as required for P02?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P02`

> The standard path requires an approval explicitly granted by the duty manager strictly before the operation starts. Submitting or acknowledging a request does not grant approval. Approval at the exact starting timestamp is not strictly before start.

- [input/sources/register.md](input/sources/register.md) — `R01`

> This extract is a complete record of requests, duty-manager approvals, start timestamps, qualifying incident determinations, emergency declarations, and countersignatures for C-101, C-102, C-103, and C-104 through 2028-04-12 17:00 UTC. In this extract “none” means the specified event did not occur during that coverage period. The register gives recorded starts as facts for those four operations. C-105 is not covered by this register; its external authority records were not received. Completeness must not be extended to C-105.

- [input/sources/register.md](input/sources/register.md) — `R04`

> C-103: request submitted 2028-04-10 11:00 UTC; duty-manager approval granted 2028-04-10 11:30 UTC; start 2028-04-10 11:30 UTC. Qualifying active incident: no. Emergency declaration: none. Countersignature: none.

### Rules

- P02 explicitly excludes approval at exactly the starting timestamp; before means strict less-than.

### Assumptions

- The supplied register is accepted as documentary fact within R01 coverage, and its exact event labels and UTC timestamps are faithfully transcribed; authenticity is not independently established.

### Reasoning

- 1. R04 gives both approval and actual start as 2028-04-10 11:30 UTC.
- 2. Both offsets are 690. Equality cannot satisfy 690 < 690.
- 3. The stated strict ordering is false and the standard-path conclusion fails. This is an actual equal-time counterexample, not missing evidence.

### Limits

- This finding targets the report's standard-path assertion. Other paths require their own conditions.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim04` in module `Audit` (refutes): `Audit.standard Audit.c103 = false ∧ ¬ ((690 : Int) < 690)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target013.lean) · [Actual proof log](logs/target-013.log)

### Recommendation

Correct the finding to say that simultaneous approval and start failed the strict P02 requirement.

## PA-05

### Exact report claim

`input/report.md#PA-05`

> **PA-05.** C-104 started without authorization under either path in P-17.

### Verification question

Did C-104 actually start and satisfy neither of the only two authorization paths under P-17 revision 3 at its 2028-04-10 13:20 UTC start?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P01`

> P-17 revision 3 governs all five operations C-101 through C-105 for the entire period covered by this dossier. There is no applicable superseding policy in this fixture. “Authorized start” means satisfying either the standard path P02 or the emergency path P03; these are the only two paths. An emergency path is fully established only when every P03 condition is met.

- [input/sources/policy.md](input/sources/policy.md) — `P02`

> The standard path requires an approval explicitly granted by the duty manager strictly before the operation starts. Submitting or acknowledging a request does not grant approval. Approval at the exact starting timestamp is not strictly before start.

- [input/sources/policy.md](input/sources/policy.md) — `P03`

> The emergency path requires all of: a qualifying active incident, a duty officer's emergency declaration strictly before start, and a duty manager's countersignature at or after start and no later than 24 hours after start. This path permits a start without a standard approval. The declaration alone does not complete this path.

- [input/sources/register.md](input/sources/register.md) — `R01`

> This extract is a complete record of requests, duty-manager approvals, start timestamps, qualifying incident determinations, emergency declarations, and countersignatures for C-101, C-102, C-103, and C-104 through 2028-04-12 17:00 UTC. In this extract “none” means the specified event did not occur during that coverage period. The register gives recorded starts as facts for those four operations. C-105 is not covered by this register; its external authority records were not received. Completeness must not be extended to C-105.

- [input/sources/register.md](input/sources/register.md) — `R05`

> C-104: request submitted 2028-04-10 13:00 UTC; duty-manager approval: none; start 2028-04-10 13:20 UTC. Qualifying active incident: no. Emergency declaration: none. Countersignature: none.

### Rules

- P01 exhaustively defines authorized start as standard OR emergency. P02 and P03 specify their required conditions. R01 gives covered none entries negative evidential force.

### Assumptions

- The supplied register is accepted as documentary fact within R01 coverage, and its exact event labels and UTC timestamps are faithfully transcribed; authenticity is not independently established.

### Reasoning

- 1. R05 positively records actual start at 13:20, so the claim is not vacuous.
- 2. R05 explicitly records no duty-manager approval, ruling out P02.
- 3. It also records no qualifying incident, no emergency declaration and no countersignature, ruling out P03.
- 4. Because P01 lists no third path, the recorded start was unauthorized under this policy.

### Limits

- Exhaustiveness is confined to P-17 revision 3 and the recorded period; no external legal consequence follows.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim05` in module `Audit` (supports): `Audit.c104.start = 800 ∧ Audit.standard Audit.c104 = false ∧ Audit.emergency Audit.c104 = false ∧ Audit.authorized Audit.c104 = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target014.lean) · [Actual proof log](logs/target-014.log)

### Recommendation

Retain with both failed paths and R01 coverage stated explicitly.

## PA-06

### Exact report claim

`input/report.md#PA-06`

> **PA-06.** C-105 had no standard duty-manager approval before its proposed 2028-04-11 09:00 UTC start.

### Verification question

Does the supplied corpus establish absence of any C-105 standard duty-manager approval before the proposed 2028-04-11 09:00 UTC time?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P02`

> The standard path requires an approval explicitly granted by the duty manager strictly before the operation starts. Submitting or acknowledging a request does not grant approval. Approval at the exact starting timestamp is not strictly before start.

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

### Rules

- R01 completeness explicitly excludes C-105. H01 completeness concerns package contents only. H02 cannot confirm or deny approval events. Missing transferred records do not entail event absence.

### Assumptions

- H01-H02 are interpreted at their explicit documentary scope; neither possible-world assignment is asserted as actual history.

### Reasoning

- 1. No C-105 standard approval is supplied, but neither is a covered explicit negative approval entry.
- 2. H01 proves only that the package lacks the register; H02 says records were not transferred and neither confirms nor denies approval.
- 3. A01 and A02 concern whether the operation began, not approval; neither supplies the missing approval premise.
- 4. An approval before the proposed time and no such approval are both compatible with the recorded package absence. The auxiliary two-assignment witness shows why the absence inference fails.
- 5. The negative event claim remains undetermined; the audit has not established that approval existed.

### Limits

- The model proves a failure of entailment from package absence, not the truth or falsity of the actual C-105 approval claim. Actual start is also disputed, but this claim uses the proposed time and does not require resolving it.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **auxiliary**.

### Formal evidence

- `Audit.claim06Countermodels` in module `Audit` (auxiliary): `Audit.possibleApproved.packageContainsRegister = false ∧ Audit.possibleUnapproved.packageContainsRegister = false ∧ Audit.possibleApproved.approvalBeforeProposedStart = true ∧ Audit.possibleUnapproved.approvalBeforeProposedStart = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target015.lean) · [Actual proof log](logs/target-015.log)

### Recommendation

Obtain a complete external North Quay approval record or a reliable explicit event-level denial; meanwhile state that pre-start approval is unverified.

## PA-07

### Exact report claim

`input/report.md#PA-07`

> **PA-07.** C-105 began at 2028-04-11 09:00 UTC.

### Verification question

What evidence supports and denies that the same proposed operation C-105 began on 2028-04-11 at 09:00 UTC, and can the dispute be resolved?

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

- Attributed witness assertions remain distinct from settled occurrence facts. P04 supplies no conflict-resolution rule; H02 identifies the same proposed operation and certifies no start timestamp.

### Assumptions

- The notes are attributed assertions as supplied; no witness reliability preference is assumed.

### Reasoning

- 1. Mira Vale explicitly affirms the 09:00 start and says she was present.
- 2. Leon Reed explicitly denies any start that day before his 12:10 note, which includes the same 09:00 time.
- 3. H02 rules out interpreting them as separate operations; no retraction or priority rule resolves the contradiction.
- 4. There is both positive and negative evidence for the exact claim. The auxiliary theorem records both attributions, not contradictory historical truth.

### Limits

- Neither witness overrides the other; this audit does not settle whether C-105 actually began. No formal proof of occurrence or nonoccurrence is asserted.

### Result

Semantic state: **both**; argument status: **disputed**; formal status: **auxiliary**.

### Formal evidence

- `Audit.claim07Conflict` in module `Audit` (auxiliary): `Audit.miraAffirmsStart0900 = true ∧ Audit.leonDeniesStart0900 = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target016.lean) · [Actual proof log](logs/target-016.log)

### Recommendation

Present the conflict explicitly and obtain independent start records or a documented resolution of the witness disagreement.

## PA-08

### Exact report claim

`input/report.md#PA-08`

> **PA-08.** C-102 was unauthorized solely because it lacked a standard approval.

### Verification question

Does C-102 lack authorization under P-17 solely because its standard approval is absent, despite the recorded emergency conditions?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P01`

> P-17 revision 3 governs all five operations C-101 through C-105 for the entire period covered by this dossier. There is no applicable superseding policy in this fixture. “Authorized start” means satisfying either the standard path P02 or the emergency path P03; these are the only two paths. An emergency path is fully established only when every P03 condition is met.

- [input/sources/policy.md](input/sources/policy.md) — `P02`

> The standard path requires an approval explicitly granted by the duty manager strictly before the operation starts. Submitting or acknowledging a request does not grant approval. Approval at the exact starting timestamp is not strictly before start.

- [input/sources/policy.md](input/sources/policy.md) — `P03`

> The emergency path requires all of: a qualifying active incident, a duty officer's emergency declaration strictly before start, and a duty manager's countersignature at or after start and no later than 24 hours after start. This path permits a start without a standard approval. The declaration alone does not complete this path.

- [input/sources/register.md](input/sources/register.md) — `R01`

> This extract is a complete record of requests, duty-manager approvals, start timestamps, qualifying incident determinations, emergency declarations, and countersignatures for C-101, C-102, C-103, and C-104 through 2028-04-12 17:00 UTC. In this extract “none” means the specified event did not occur during that coverage period. The register gives recorded starts as facts for those four operations. C-105 is not covered by this register; its external authority records were not received. Completeness must not be extended to C-105.

- [input/sources/register.md](input/sources/register.md) — `R03`

> C-102: request submitted 2028-04-10 10:00 UTC; duty-manager standard approval: none; start 2028-04-10 10:15 UTC. Qualifying active incident: yes, incident I-62 was active at start. Duty-officer emergency declaration 2028-04-10 10:05 UTC. Duty-manager countersignature 2028-04-11 10:15 UTC.

### Rules

- Authorized start is the P01 disjunction of standard and emergency paths. P03 expressly permits start without standard approval. Failure of one disjunct does not imply failure of both.

### Assumptions

- The supplied register is accepted as documentary fact within R01 coverage, and its exact event labels and UTC timestamps are faithfully transcribed; authenticity is not independently established.

### Reasoning

- 1. The claim's premise is true: R03 explicitly records no standard approval.
- 2. The actual same in-scope operation has an active qualifying incident, pre-start declaration and exactly timely countersignature, completing P03.
- 3. Consequently C-102 is authorized under the emergency path, contradicting the report's nonauthorization conclusion.
- 4. C-102 itself is a counterexample to the inference from absent standard approval to unauthorized start; the failure is stronger than a citation gap.

### Limits

- This refutes policy nonauthorization, not any separate qualitative criticism of the emergency decision.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim08` in module `Audit` (refutes): `Audit.standard Audit.c102 = false ∧ Audit.emergency Audit.c102 = true ∧ Audit.authorized Audit.c102 = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target017.lean) · [Actual proof log](logs/target-017.log)

### Recommendation

State that standard approval was absent but C-102 satisfied the alternative emergency path and was authorized under P-17.

## PA-09

### Exact report claim

`input/report.md#PA-09`

> **PA-09.** C-102's emergency start was prudent.

### Verification question

Can the qualitative assertion that C-102 emergency start was prudent be assessed by any operational criterion in the supplied mandate or P-17?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P04`

> P-17 prescribes no measure of whether a start was “prudent.” Authorization and prudence are separate assessments. The policy has no rule for resolving contradictory witness statements about an operation actually occurring.

- [input/sources/policy.md](input/sources/policy.md) — `P03`

> The emergency path requires all of: a qualifying active incident, a duty officer's emergency declaration strictly before start, and a duty manager's countersignature at or after start and no later than 24 hours after start. This path permits a start without a standard approval. The declaration alone does not complete this path.

- [input/sources/register.md](input/sources/register.md) — `R03`

> C-102: request submitted 2028-04-10 10:00 UTC; duty-manager standard approval: none; start 2028-04-10 10:15 UTC. Qualifying active incident: yes, incident I-62 was active at start. Duty-officer emergency declaration 2028-04-10 10:05 UTC. Duty-manager countersignature 2028-04-11 10:15 UTC.

### Rules

- P04 explicitly supplies no prudence measure and separates authorization from prudence. Policy compliance is not a defined prudence criterion.

### Assumptions

- No extra prudence definition or organizational practice is introduced.

### Reasoning

- 1. R03 supports emergency authorization under P03.
- 2. Neither the policy nor supplied documents defines prudence or supplies a rule linking authorization to prudence.
- 3. The evaluative claim is outside formal assessment under this mandate; neither a prudence proof nor its negation is justified.

### Limits

- This is a missing operational criterion, not a finding that the start was imprudent or a computation timeout.

### Result

Semantic state: **not_applicable**; argument status: **nonformal**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Keep the assessment explicitly qualitative, or supply an agreed prudence criterion and the evidence required to apply it.

## PA-10

### Exact report claim

`input/report.md#PA-10`

> **PA-10.** The supplied C-105 handoff package contains no external approval register.

### Verification question

Does the complete supplied C-105 handoff package inventory exclude an external approval register, independently of whether approval events occurred?

### Source evidence

- [input/sources/handoff.md](input/sources/handoff.md) — `H01`

> C-105 was administered through the external North Quay unit. The handoff package contains a request sent at 2028-04-11 08:00 UTC, the two witness notes supplied in `attestations.md`, and no external approval register. This list is complete for what the handoff package contains, not for events that occurred at North Quay.

- [input/sources/handoff.md](input/sources/handoff.md) — `H02`

> The North Quay liaison states: “Approval and emergency records were not transferred. I cannot confirm or deny whether an approval, qualifying incident, declaration, or countersignature existed for C-105.” No start timestamp is certified in the handoff. The two witness notes refer to the same proposed operation, C-105, not to separate operations.

- [input/sources/register.md](input/sources/register.md) — `R01`

> This extract is a complete record of requests, duty-manager approvals, start timestamps, qualifying incident determinations, emergency declarations, and countersignatures for C-101, C-102, C-103, and C-104 through 2028-04-12 17:00 UTC. In this extract “none” means the specified event did not occur during that coverage period. The register gives recorded starts as facts for those four operations. C-105 is not covered by this register; its external authority records were not received. Completeness must not be extended to C-105.

### Rules

- H01 expressly gives complete package contents and expressly limits completeness to that inventory. Documentary nonmembership does not entail event nonoccurrence.

### Assumptions

- The H01 package inventory is accepted as complete only for the supplied handoff package.

### Reasoning

- 1. H01 lists the request and two witness notes and explicitly says no external approval register is in the package.
- 2. The finite package model therefore contains no external approval register.
- 3. H02 corroborates nontransfer, while R01 explains why the local register cannot fill the C-105 coverage gap.
- 4. The exact package-content claim is supported. It must not be extended to PA-06's historical approval-absence assertion.

### Limits

- The conclusion establishes a supplied attachment absence only; it does not show that an approval register or approval never existed externally.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim10` in module `Audit` (supports): `Audit.PackageItem.externalApprovalRegister ∉ Audit.handoffPackage`.
  [Model](models/Audit.lean) · [Executed check](checks/Target018.lean) · [Actual proof log](logs/target-018.log)

### Recommendation

Retain with the explicit package-only scope.
