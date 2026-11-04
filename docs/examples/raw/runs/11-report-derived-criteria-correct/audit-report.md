# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

## Registered claim coverage

Coverage: **complete_registration**; 14 reviewed anchors; 45 audited and 0 deferred claims.

Registration reconciles declared claims and reviewed report anchors; it does not establish semantic completeness, faithful decomposition, or that declared searches were actually performed.

- `P01`: non_claim — Title and report framing prescribe review scope and absence of a brief, rather than making an independent source finding.
- `P02`: non_claim — Title and report framing prescribe review scope and absence of a brief, rather than making an independent source finding.
- `P03`: claims — Contains a material conclusion and, where present, separately registered supporting premises and inferences.
- `P04`: claims — Contains a material conclusion and, where present, separately registered supporting premises and inferences.
- `P05`: claims — Contains a material conclusion and, where present, separately registered supporting premises and inferences.
- `P06`: claims — Contains a material conclusion and, where present, separately registered supporting premises and inferences.
- `P07`: claims — Contains a material conclusion and, where present, separately registered supporting premises and inferences.
- `P08`: claims — Contains a material conclusion and, where present, separately registered supporting premises and inferences.
- `P09`: claims — Contains a material conclusion and, where present, separately registered supporting premises and inferences.
- `P10`: claims — Contains a material conclusion and, where present, separately registered supporting premises and inferences.
- `P11`: claims — Contains a material conclusion and, where present, separately registered supporting premises and inferences.
- `P12`: claims — Contains a material conclusion and, where present, separately registered supporting premises and inferences.
- `P13`: claims — Contains a material conclusion and, where present, separately registered supporting premises and inferences.
- `P14`: claims — Contains a material conclusion and, where present, separately registered supporting premises and inferences.
[Semantic correspondence review](semantic-review.md)

## F11-OK-01

### Exact report claim

`input/report.md#P03`

> The total amount of the reviewed cohort is 50000 euro cents.

### Verification question

Does the sum of exactly A–D equal 50000 integer euro cents?

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |


### F11-OK-01: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the sum of exactly A–D equal 50000 integer euro cents?

- Decision criterion: L-01 enumerates exactly A–D; sum each L-02 amount once.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report inference at `P03`:

> 12000 + 18000 + 9000 + 11000 = 50000.

Assessment: **verified**. The only cohort amounts are 12000, 18000, 9000 and 11000. Their sum is 50000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [proof 0: Campaign.total](models/Campaign.lean)

Report citation at `P03`:

> dispatch-ledger.md L-02.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`

Independent audit reasoning:

- The only cohort amounts are 12000, 18000, 9000 and 11000.
- Their sum is 50000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [proof 0: Campaign.total](models/Campaign.lean)

Audited claim dependencies: None declared.

Formalization rationale: Finite integer model transcribes the recorded amounts, days, finite membership and explicit rules; direct target is scoped to this claim.

- Proof 0 source-to-target correspondence: L-02 values and P-02/P-03/P-04 rules are transcribed into Campaign declarations; D-01 closes destination membership only during days 1–20. The only cohort amounts are 12000, 18000, 9000 and 11000. Their sum is 50000. The target Campaign.cohortTotal = 50000 checks the stated finite calculation or rule evaluation. Faithful transcription and the packet domain are assumed; source authenticity is outside the model.

Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

The only cohort amounts are 12000, 18000, 9000 and 11000. Their sum is 50000.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- L-01 enumerates exactly A–D; sum each L-02 amount once.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. The only cohort amounts are 12000, 18000, 9000 and 11000.
- 2. Their sum is 50000.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Campaign.total` in module `Campaign` (supports): `Campaign.cohortTotal = 50000`.
  [Model](models/Campaign.lean) · [Executed check](checks/Target018.lean) · [Actual proof log](logs/target-018.log)

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-01-A01

### Exact report claim

`input/report.md#P03`

> 12000 + 18000 + 9000 + 11000 = 50000.

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-01: 12000 + 18000 + 9000 + 11000 = 50000.

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |


### F11-OK-01-A01: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-01: 12000 + 18000 + 9000 + 11000 = 50000.

- Decision criterion: L-01 enumerates exactly A–D; sum each L-02 amount once.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report inference at `P03`:

> 12000 + 18000 + 9000 + 11000 = 50000.

Assessment: **verified**. The only cohort amounts are 12000, 18000, 9000 and 11000. Their sum is 50000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`

Report citation at `P03`:

> dispatch-ledger.md L-02.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`

Independent audit reasoning:

- The only cohort amounts are 12000, 18000, 9000 and 11000.
- Their sum is 50000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

The only cohort amounts are 12000, 18000, 9000 and 11000. Their sum is 50000.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- L-01 enumerates exactly A–D; sum each L-02 amount once.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. The only cohort amounts are 12000, 18000, 9000 and 11000.
- 2. Their sum is 50000.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-01; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-02

### Exact report claim

`input/report.md#P04`

> The cohort budget balance is 5000 euro cents.

### Verification question

Does the P-05 comparison-budget-minus-cohort-amount definition yield 5000?

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P06`

> [P-05] A budget balance means the comparison budget less the sum of dispatch amounts for the stated cohort. Eligible settlement amount means the sum of amounts for the cohort members satisfying P-04. Neither amount includes dispatches outside the stated cohort.


### F11-OK-02: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the P-05 comparison-budget-minus-cohort-amount definition yield 5000?

- Decision criterion: P-05 defines balance as comparison budget less cohort expenditure, with no outside dispatches.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report inference at `P04`:

> 55000 − 50000 = 5000 under the stated balance definition.

Assessment: **verified**. L-01 gives budget 55000; independently summing L-02 gives 50000. Integer subtraction gives 5000; this is not a claim about all-campaign funds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P06`, [proof 0: Campaign.balance](models/Campaign.lean)

Report citation at `P04`:

> dispatch-ledger.md L-01–L-02; dispatch-policy.md P-05.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P06`

Independent audit reasoning:

- L-01 gives budget 55000; independently summing L-02 gives 50000.
- Integer subtraction gives 5000; this is not a claim about all-campaign funds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P06`, [proof 0: Campaign.balance](models/Campaign.lean)

Audited claim dependencies: None declared.

Formalization rationale: Finite integer model transcribes the recorded amounts, days, finite membership and explicit rules; direct target is scoped to this claim.

- Proof 0 source-to-target correspondence: L-02 values and P-02/P-03/P-04 rules are transcribed into Campaign declarations; D-01 closes destination membership only during days 1–20. L-01 gives budget 55000; independently summing L-02 gives 50000. Integer subtraction gives 5000; this is not a claim about all-campaign funds. The target (55000 : Int) - Campaign.cohortTotal = 5000 checks the stated finite calculation or rule evaluation. Faithful transcription and the packet domain are assumed; source authenticity is outside the model.

Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

L-01 gives budget 55000; independently summing L-02 gives 50000. Integer subtraction gives 5000; this is not a claim about all-campaign funds.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-05 defines balance as comparison budget less cohort expenditure, with no outside dispatches.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. L-01 gives budget 55000; independently summing L-02 gives 50000.
- 2. Integer subtraction gives 5000; this is not a claim about all-campaign funds.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Campaign.balance` in module `Campaign` (supports): `(55000 : Int) - Campaign.cohortTotal = 5000`.
  [Model](models/Campaign.lean) · [Executed check](checks/Target019.lean) · [Actual proof log](logs/target-019.log)

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-02-A01

### Exact report claim

`input/report.md#P04`

> 55000 − 50000 = 5000 under the stated balance definition.

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-02: 55000 − 50000 = 5000 under the stated balance definition.

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P06`

> [P-05] A budget balance means the comparison budget less the sum of dispatch amounts for the stated cohort. Eligible settlement amount means the sum of amounts for the cohort members satisfying P-04. Neither amount includes dispatches outside the stated cohort.


### F11-OK-02-A01: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-02: 55000 − 50000 = 5000 under the stated balance definition.

- Decision criterion: P-05 defines balance as comparison budget less cohort expenditure, with no outside dispatches.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report inference at `P04`:

> 55000 − 50000 = 5000 under the stated balance definition.

Assessment: **verified**. L-01 gives budget 55000; independently summing L-02 gives 50000. Integer subtraction gives 5000; this is not a claim about all-campaign funds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P06`

Report citation at `P04`:

> dispatch-ledger.md L-01–L-02; dispatch-policy.md P-05.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P06`

Independent audit reasoning:

- L-01 gives budget 55000; independently summing L-02 gives 50000.
- Integer subtraction gives 5000; this is not a claim about all-campaign funds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P06`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

L-01 gives budget 55000; independently summing L-02 gives 50000. Integer subtraction gives 5000; this is not a claim about all-campaign funds.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-05 defines balance as comparison budget less cohort expenditure, with no outside dispatches.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. L-01 gives budget 55000; independently summing L-02 gives 50000.
- 2. Integer subtraction gives 5000; this is not a claim about all-campaign funds.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-02; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-03

### Exact report claim

`input/report.md#P05`

> B has compliant approval at cutoff under the temporary exception.

### Verification question

Does B satisfy every conjunct of P-03 at end of day 20?

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.


### F11-OK-03: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does B satisfy every conjunct of P-03 at end of day 20?

- Decision criterion: P-03 requires R2, release 10–14 inclusive, declaration at most two days before release, and approval between release and release+3 inclusive.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P05`:

> route R2

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`, [proof 0: Campaign.bException](models/Campaign.lean)

Report premise at `P05`:

> release day 12 within days 10–14

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`, [proof 0: Campaign.bException](models/Campaign.lean)

Report premise at `P05`:

> declaration day 11 one day before release

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`, [proof 0: Campaign.bException](models/Campaign.lean)

Report premise at `P05`:

> approval day 15 exactly three days after release

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`, [proof 0: Campaign.bException](models/Campaign.lean)

Report inference at `P05`:

> satisfy every exception condition.

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`, [proof 0: Campaign.bException](models/Campaign.lean)

Report citation at `P05`:

> dispatch-ledger.md L-02; dispatch-policy.md P-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Independent audit reasoning:

- B is R2 and releases on day 12, within the inclusive window.
- Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20.
- Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`, [proof 0: Campaign.bException](models/Campaign.lean)

Audited claim dependencies: None declared.

Formalization rationale: Finite integer model transcribes the recorded amounts, days, finite membership and explicit rules; direct target is scoped to this claim.

- Proof 0 source-to-target correspondence: L-02 values and P-02/P-03/P-04 rules are transcribed into Campaign declarations; D-01 closes destination membership only during days 1–20. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds. The target Campaign.exception Campaign.Dispatch.b checks the stated finite calculation or rule evaluation. Faithful transcription and the packet domain are assumed; source authenticity is outside the model.

Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-03 requires R2, release 10–14 inclusive, declaration at most two days before release, and approval between release and release+3 inclusive.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. B is R2 and releases on day 12, within the inclusive window.
- 2. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20.
- 3. Every exception condition holds.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Campaign.bException` in module `Campaign` (supports): `Campaign.exception Campaign.Dispatch.b`.
  [Model](models/Campaign.lean) · [Executed check](checks/Target020.lean) · [Actual proof log](logs/target-020.log)

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-03-A01

### Exact report claim

`input/report.md#P05`

> route R2

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-03: route R2

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.


### F11-OK-03-A01: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-03: route R2

- Decision criterion: P-03 requires R2, release 10–14 inclusive, declaration at most two days before release, and approval between release and release+3 inclusive.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P05`:

> route R2

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report premise at `P05`:

> release day 12 within days 10–14

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report premise at `P05`:

> declaration day 11 one day before release

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report premise at `P05`:

> approval day 15 exactly three days after release

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report inference at `P05`:

> satisfy every exception condition.

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report citation at `P05`:

> dispatch-ledger.md L-02; dispatch-policy.md P-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Independent audit reasoning:

- B is R2 and releases on day 12, within the inclusive window.
- Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20.
- Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-03 requires R2, release 10–14 inclusive, declaration at most two days before release, and approval between release and release+3 inclusive.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. B is R2 and releases on day 12, within the inclusive window.
- 2. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20.
- 3. Every exception condition holds.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-03; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-03-A02

### Exact report claim

`input/report.md#P05`

> release day 12 within days 10–14

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-03: release day 12 within days 10–14

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.


### F11-OK-03-A02: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-03: release day 12 within days 10–14

- Decision criterion: P-03 requires R2, release 10–14 inclusive, declaration at most two days before release, and approval between release and release+3 inclusive.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P05`:

> route R2

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report premise at `P05`:

> release day 12 within days 10–14

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report premise at `P05`:

> declaration day 11 one day before release

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report premise at `P05`:

> approval day 15 exactly three days after release

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report inference at `P05`:

> satisfy every exception condition.

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report citation at `P05`:

> dispatch-ledger.md L-02; dispatch-policy.md P-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Independent audit reasoning:

- B is R2 and releases on day 12, within the inclusive window.
- Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20.
- Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-03 requires R2, release 10–14 inclusive, declaration at most two days before release, and approval between release and release+3 inclusive.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. B is R2 and releases on day 12, within the inclusive window.
- 2. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20.
- 3. Every exception condition holds.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-03; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-03-A03

### Exact report claim

`input/report.md#P05`

> declaration day 11 one day before release

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-03: declaration day 11 one day before release

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.


### F11-OK-03-A03: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-03: declaration day 11 one day before release

- Decision criterion: P-03 requires R2, release 10–14 inclusive, declaration at most two days before release, and approval between release and release+3 inclusive.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P05`:

> route R2

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report premise at `P05`:

> release day 12 within days 10–14

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report premise at `P05`:

> declaration day 11 one day before release

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report premise at `P05`:

> approval day 15 exactly three days after release

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report inference at `P05`:

> satisfy every exception condition.

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report citation at `P05`:

> dispatch-ledger.md L-02; dispatch-policy.md P-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Independent audit reasoning:

- B is R2 and releases on day 12, within the inclusive window.
- Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20.
- Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-03 requires R2, release 10–14 inclusive, declaration at most two days before release, and approval between release and release+3 inclusive.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. B is R2 and releases on day 12, within the inclusive window.
- 2. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20.
- 3. Every exception condition holds.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-03; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-03-A04

### Exact report claim

`input/report.md#P05`

> approval day 15 exactly three days after release

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-03: approval day 15 exactly three days after release

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.


### F11-OK-03-A04: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-03: approval day 15 exactly three days after release

- Decision criterion: P-03 requires R2, release 10–14 inclusive, declaration at most two days before release, and approval between release and release+3 inclusive.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P05`:

> route R2

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report premise at `P05`:

> release day 12 within days 10–14

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report premise at `P05`:

> declaration day 11 one day before release

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report premise at `P05`:

> approval day 15 exactly three days after release

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report inference at `P05`:

> satisfy every exception condition.

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report citation at `P05`:

> dispatch-ledger.md L-02; dispatch-policy.md P-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Independent audit reasoning:

- B is R2 and releases on day 12, within the inclusive window.
- Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20.
- Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-03 requires R2, release 10–14 inclusive, declaration at most two days before release, and approval between release and release+3 inclusive.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. B is R2 and releases on day 12, within the inclusive window.
- 2. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20.
- 3. Every exception condition holds.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-03; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-03-A05

### Exact report claim

`input/report.md#P05`

> satisfy every exception condition.

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-03: satisfy every exception condition.

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.


### F11-OK-03-A05: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-03: satisfy every exception condition.

- Decision criterion: P-03 requires R2, release 10–14 inclusive, declaration at most two days before release, and approval between release and release+3 inclusive.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P05`:

> route R2

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report premise at `P05`:

> release day 12 within days 10–14

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report premise at `P05`:

> declaration day 11 one day before release

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report premise at `P05`:

> approval day 15 exactly three days after release

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report inference at `P05`:

> satisfy every exception condition.

Assessment: **verified**. B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Report citation at `P05`:

> dispatch-ledger.md L-02; dispatch-policy.md P-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Independent audit reasoning:

- B is R2 and releases on day 12, within the inclusive window.
- Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20.
- Every exception condition holds.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

B is R2 and releases on day 12, within the inclusive window. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20. Every exception condition holds.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-03 requires R2, release 10–14 inclusive, declaration at most two days before release, and approval between release and release+3 inclusive.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. B is R2 and releases on day 12, within the inclusive window.
- 2. Declaration 11 is one day before 12. Approval 15 is three days after 12, and occurred before cutoff 20.
- 3. Every exception condition holds.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-03; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-04

### Exact report claim

`input/report.md#P06`

> C has noncompliant approval at cutoff.

### Verification question

Do both and all applicable approval routes fail for C?

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P03`

> [P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.


### F11-OK-04: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Do both and all applicable approval routes fail for C?

- Decision criterion: Ordinary approval is strictly before release; P-03 permits at most three days after release and exhausts alternate routes.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P06`:

> approval day 16 is later than release day 12

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [proof 0: Campaign.cNoncompliant](models/Campaign.lean)

Report inference at `P06`:

> the ordinary route fails

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [proof 0: Campaign.cNoncompliant](models/Campaign.lean)

Report premise at `P06`:

> it is four days after release

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [proof 0: Campaign.cNoncompliant](models/Campaign.lean)

Report inference at `P06`:

> the exception also fails.

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [proof 0: Campaign.cNoncompliant](models/Campaign.lean)

Report inference at `P06`:

> These are the only approval routes.

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [proof 0: Campaign.cNoncompliant](models/Campaign.lean)

Report citation at `P06`:

> dispatch-ledger.md L-02; dispatch-policy.md P-02–P-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Independent audit reasoning:

- C releases on 12 and its only approval is 16. Thus ordinary approval fails.
- Approval is four days after release, exceeding the exception maximum of three.
- L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [proof 0: Campaign.cNoncompliant](models/Campaign.lean)

Audited claim dependencies: None declared.

Formalization rationale: Finite integer model transcribes the recorded amounts, days, finite membership and explicit rules; direct target is scoped to this claim.

- Proof 0 source-to-target correspondence: L-02 values and P-02/P-03/P-04 rules are transcribed into Campaign declarations; D-01 closes destination membership only during days 1–20. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort. The target ¬ Campaign.compliant Campaign.Dispatch.c checks the stated finite calculation or rule evaluation. Faithful transcription and the packet domain are assumed; source authenticity is outside the model.

Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- Ordinary approval is strictly before release; P-03 permits at most three days after release and exhausts alternate routes.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. C releases on 12 and its only approval is 16. Thus ordinary approval fails.
- 2. Approval is four days after release, exceeding the exception maximum of three.
- 3. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Campaign.cNoncompliant` in module `Campaign` (supports): `¬ Campaign.compliant Campaign.Dispatch.c`.
  [Model](models/Campaign.lean) · [Executed check](checks/Target021.lean) · [Actual proof log](logs/target-021.log)

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-04-A01

### Exact report claim

`input/report.md#P06`

> approval day 16 is later than release day 12

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-04: approval day 16 is later than release day 12

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P03`

> [P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.


### F11-OK-04-A01: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-04: approval day 16 is later than release day 12

- Decision criterion: Ordinary approval is strictly before release; P-03 permits at most three days after release and exhausts alternate routes.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P06`:

> approval day 16 is later than release day 12

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report inference at `P06`:

> the ordinary route fails

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report premise at `P06`:

> it is four days after release

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report inference at `P06`:

> the exception also fails.

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report inference at `P06`:

> These are the only approval routes.

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report citation at `P06`:

> dispatch-ledger.md L-02; dispatch-policy.md P-02–P-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Independent audit reasoning:

- C releases on 12 and its only approval is 16. Thus ordinary approval fails.
- Approval is four days after release, exceeding the exception maximum of three.
- L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- Ordinary approval is strictly before release; P-03 permits at most three days after release and exhausts alternate routes.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. C releases on 12 and its only approval is 16. Thus ordinary approval fails.
- 2. Approval is four days after release, exceeding the exception maximum of three.
- 3. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-04; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-04-A02

### Exact report claim

`input/report.md#P06`

> the ordinary route fails

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-04: the ordinary route fails

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P03`

> [P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.


### F11-OK-04-A02: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-04: the ordinary route fails

- Decision criterion: Ordinary approval is strictly before release; P-03 permits at most three days after release and exhausts alternate routes.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P06`:

> approval day 16 is later than release day 12

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report inference at `P06`:

> the ordinary route fails

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report premise at `P06`:

> it is four days after release

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report inference at `P06`:

> the exception also fails.

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report inference at `P06`:

> These are the only approval routes.

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report citation at `P06`:

> dispatch-ledger.md L-02; dispatch-policy.md P-02–P-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Independent audit reasoning:

- C releases on 12 and its only approval is 16. Thus ordinary approval fails.
- Approval is four days after release, exceeding the exception maximum of three.
- L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- Ordinary approval is strictly before release; P-03 permits at most three days after release and exhausts alternate routes.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. C releases on 12 and its only approval is 16. Thus ordinary approval fails.
- 2. Approval is four days after release, exceeding the exception maximum of three.
- 3. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-04; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-04-A03

### Exact report claim

`input/report.md#P06`

> it is four days after release

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-04: it is four days after release

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P03`

> [P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.


### F11-OK-04-A03: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-04: it is four days after release

- Decision criterion: Ordinary approval is strictly before release; P-03 permits at most three days after release and exhausts alternate routes.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P06`:

> approval day 16 is later than release day 12

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report inference at `P06`:

> the ordinary route fails

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report premise at `P06`:

> it is four days after release

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report inference at `P06`:

> the exception also fails.

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report inference at `P06`:

> These are the only approval routes.

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report citation at `P06`:

> dispatch-ledger.md L-02; dispatch-policy.md P-02–P-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Independent audit reasoning:

- C releases on 12 and its only approval is 16. Thus ordinary approval fails.
- Approval is four days after release, exceeding the exception maximum of three.
- L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- Ordinary approval is strictly before release; P-03 permits at most three days after release and exhausts alternate routes.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. C releases on 12 and its only approval is 16. Thus ordinary approval fails.
- 2. Approval is four days after release, exceeding the exception maximum of three.
- 3. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-04; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-04-A04

### Exact report claim

`input/report.md#P06`

> the exception also fails.

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-04: the exception also fails.

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P03`

> [P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.


### F11-OK-04-A04: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-04: the exception also fails.

- Decision criterion: Ordinary approval is strictly before release; P-03 permits at most three days after release and exhausts alternate routes.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P06`:

> approval day 16 is later than release day 12

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report inference at `P06`:

> the ordinary route fails

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report premise at `P06`:

> it is four days after release

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report inference at `P06`:

> the exception also fails.

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report inference at `P06`:

> These are the only approval routes.

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report citation at `P06`:

> dispatch-ledger.md L-02; dispatch-policy.md P-02–P-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Independent audit reasoning:

- C releases on 12 and its only approval is 16. Thus ordinary approval fails.
- Approval is four days after release, exceeding the exception maximum of three.
- L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- Ordinary approval is strictly before release; P-03 permits at most three days after release and exhausts alternate routes.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. C releases on 12 and its only approval is 16. Thus ordinary approval fails.
- 2. Approval is four days after release, exceeding the exception maximum of three.
- 3. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-04; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-04-A05

### Exact report claim

`input/report.md#P06`

> These are the only approval routes.

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-04: These are the only approval routes.

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P03`

> [P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.


### F11-OK-04-A05: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-04: These are the only approval routes.

- Decision criterion: Ordinary approval is strictly before release; P-03 permits at most three days after release and exhausts alternate routes.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P06`:

> approval day 16 is later than release day 12

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report inference at `P06`:

> the ordinary route fails

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report premise at `P06`:

> it is four days after release

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report inference at `P06`:

> the exception also fails.

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report inference at `P06`:

> These are the only approval routes.

Assessment: **verified**. C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Report citation at `P06`:

> dispatch-ledger.md L-02; dispatch-policy.md P-02–P-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Independent audit reasoning:

- C releases on 12 and its only approval is 16. Thus ordinary approval fails.
- Approval is four days after release, exceeding the exception maximum of three.
- L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

C releases on 12 and its only approval is 16. Thus ordinary approval fails. Approval is four days after release, exceeding the exception maximum of three. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- Ordinary approval is strictly before release; P-03 permits at most three days after release and exhausts alternate routes.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. C releases on 12 and its only approval is 16. Thus ordinary approval fails.
- 2. Approval is four days after release, exceeding the exception maximum of three.
- 3. L-02 states final complete fields and sole approval event; P-03 rules out additional routes. Therefore noncompliance follows within the cohort.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-04; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-05

### Exact report claim

`input/report.md#P07`

> B is eligible for settlement at cutoff.

### Verification question

Does B satisfy all three necessary and jointly sufficient P-04 conditions?

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P05`

> [P-04] A dispatch is eligible for settlement if and only if it has compliant approval under P-02 or P-03, its recorded checksum result is PASS, and its destination appears in the supplied destination list DL-7. These are three separate necessary conditions; together they are sufficient. Delivery acceptance is not a settlement condition.

- [input/sources/destination-list.md](input/sources/destination-list.md) — `P02`

> [D-01] DL-7 is the destination list referenced by DP-7 P-04. It was effective throughout campaign days 1–20. Its complete membership is North and South. East is not a member. No amendments apply during this interval.


### F11-OK-05: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does B satisfy all three necessary and jointly sufficient P-04 conditions?

- Decision criterion: P-04 is a biconditional: compliant approval AND PASS AND membership in DL-7.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P07`:

> the temporary exception establishes compliant approval

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`, [proof 0: Campaign.bEligible](models/Campaign.lean)

Report premise at `P07`:

> the ledger records checksum PASS

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`, [proof 0: Campaign.bEligible](models/Campaign.lean)

Report premise at `P07`:

> its destination South belongs to DL-7.

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`, [proof 0: Campaign.bEligible](models/Campaign.lean)

Report inference at `P07`:

> These jointly satisfy P-04.

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`, [proof 0: Campaign.bEligible](models/Campaign.lean)

Report citation at `P07`:

> dispatch-policy.md P-03–P-04; dispatch-ledger.md L-02; destination-list.md D-01.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Independent audit reasoning:

- Independently applying P-03 to B establishes its exception approval.
- L-02 records PASS and South; D-01 lists South throughout days 1–20.
- All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`, [proof 0: Campaign.bEligible](models/Campaign.lean)

Audited claim dependencies: None declared.

Formalization rationale: Finite integer model transcribes the recorded amounts, days, finite membership and explicit rules; direct target is scoped to this claim.

- Proof 0 source-to-target correspondence: L-02 values and P-02/P-03/P-04 rules are transcribed into Campaign declarations; D-01 closes destination membership only during days 1–20. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion. The target Campaign.eligible Campaign.Dispatch.b checks the stated finite calculation or rule evaluation. Faithful transcription and the packet domain are assumed; source authenticity is outside the model.

Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-04 is a biconditional: compliant approval AND PASS AND membership in DL-7.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. Independently applying P-03 to B establishes its exception approval.
- 2. L-02 records PASS and South; D-01 lists South throughout days 1–20.
- 3. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Campaign.bEligible` in module `Campaign` (supports): `Campaign.eligible Campaign.Dispatch.b`.
  [Model](models/Campaign.lean) · [Executed check](checks/Target022.lean) · [Actual proof log](logs/target-022.log)

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-05-A01

### Exact report claim

`input/report.md#P07`

> the temporary exception establishes compliant approval

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-05: the temporary exception establishes compliant approval

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P05`

> [P-04] A dispatch is eligible for settlement if and only if it has compliant approval under P-02 or P-03, its recorded checksum result is PASS, and its destination appears in the supplied destination list DL-7. These are three separate necessary conditions; together they are sufficient. Delivery acceptance is not a settlement condition.

- [input/sources/destination-list.md](input/sources/destination-list.md) — `P02`

> [D-01] DL-7 is the destination list referenced by DP-7 P-04. It was effective throughout campaign days 1–20. Its complete membership is North and South. East is not a member. No amendments apply during this interval.


### F11-OK-05-A01: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-05: the temporary exception establishes compliant approval

- Decision criterion: P-04 is a biconditional: compliant approval AND PASS AND membership in DL-7.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P07`:

> the temporary exception establishes compliant approval

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Report premise at `P07`:

> the ledger records checksum PASS

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Report premise at `P07`:

> its destination South belongs to DL-7.

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Report inference at `P07`:

> These jointly satisfy P-04.

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Report citation at `P07`:

> dispatch-policy.md P-03–P-04; dispatch-ledger.md L-02; destination-list.md D-01.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Independent audit reasoning:

- Independently applying P-03 to B establishes its exception approval.
- L-02 records PASS and South; D-01 lists South throughout days 1–20.
- All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-04 is a biconditional: compliant approval AND PASS AND membership in DL-7.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. Independently applying P-03 to B establishes its exception approval.
- 2. L-02 records PASS and South; D-01 lists South throughout days 1–20.
- 3. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-05; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-05-A02

### Exact report claim

`input/report.md#P07`

> the ledger records checksum PASS

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-05: the ledger records checksum PASS

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P05`

> [P-04] A dispatch is eligible for settlement if and only if it has compliant approval under P-02 or P-03, its recorded checksum result is PASS, and its destination appears in the supplied destination list DL-7. These are three separate necessary conditions; together they are sufficient. Delivery acceptance is not a settlement condition.

- [input/sources/destination-list.md](input/sources/destination-list.md) — `P02`

> [D-01] DL-7 is the destination list referenced by DP-7 P-04. It was effective throughout campaign days 1–20. Its complete membership is North and South. East is not a member. No amendments apply during this interval.


### F11-OK-05-A02: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-05: the ledger records checksum PASS

- Decision criterion: P-04 is a biconditional: compliant approval AND PASS AND membership in DL-7.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P07`:

> the temporary exception establishes compliant approval

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Report premise at `P07`:

> the ledger records checksum PASS

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Report premise at `P07`:

> its destination South belongs to DL-7.

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Report inference at `P07`:

> These jointly satisfy P-04.

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Report citation at `P07`:

> dispatch-policy.md P-03–P-04; dispatch-ledger.md L-02; destination-list.md D-01.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Independent audit reasoning:

- Independently applying P-03 to B establishes its exception approval.
- L-02 records PASS and South; D-01 lists South throughout days 1–20.
- All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-04 is a biconditional: compliant approval AND PASS AND membership in DL-7.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. Independently applying P-03 to B establishes its exception approval.
- 2. L-02 records PASS and South; D-01 lists South throughout days 1–20.
- 3. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-05; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-05-A03

### Exact report claim

`input/report.md#P07`

> its destination South belongs to DL-7.

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-05: its destination South belongs to DL-7.

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P05`

> [P-04] A dispatch is eligible for settlement if and only if it has compliant approval under P-02 or P-03, its recorded checksum result is PASS, and its destination appears in the supplied destination list DL-7. These are three separate necessary conditions; together they are sufficient. Delivery acceptance is not a settlement condition.

- [input/sources/destination-list.md](input/sources/destination-list.md) — `P02`

> [D-01] DL-7 is the destination list referenced by DP-7 P-04. It was effective throughout campaign days 1–20. Its complete membership is North and South. East is not a member. No amendments apply during this interval.


### F11-OK-05-A03: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-05: its destination South belongs to DL-7.

- Decision criterion: P-04 is a biconditional: compliant approval AND PASS AND membership in DL-7.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P07`:

> the temporary exception establishes compliant approval

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Report premise at `P07`:

> the ledger records checksum PASS

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Report premise at `P07`:

> its destination South belongs to DL-7.

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Report inference at `P07`:

> These jointly satisfy P-04.

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Report citation at `P07`:

> dispatch-policy.md P-03–P-04; dispatch-ledger.md L-02; destination-list.md D-01.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Independent audit reasoning:

- Independently applying P-03 to B establishes its exception approval.
- L-02 records PASS and South; D-01 lists South throughout days 1–20.
- All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-04 is a biconditional: compliant approval AND PASS AND membership in DL-7.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. Independently applying P-03 to B establishes its exception approval.
- 2. L-02 records PASS and South; D-01 lists South throughout days 1–20.
- 3. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-05; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-05-A04

### Exact report claim

`input/report.md#P07`

> These jointly satisfy P-04.

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-05: These jointly satisfy P-04.

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P05`

> [P-04] A dispatch is eligible for settlement if and only if it has compliant approval under P-02 or P-03, its recorded checksum result is PASS, and its destination appears in the supplied destination list DL-7. These are three separate necessary conditions; together they are sufficient. Delivery acceptance is not a settlement condition.

- [input/sources/destination-list.md](input/sources/destination-list.md) — `P02`

> [D-01] DL-7 is the destination list referenced by DP-7 P-04. It was effective throughout campaign days 1–20. Its complete membership is North and South. East is not a member. No amendments apply during this interval.


### F11-OK-05-A04: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-05: These jointly satisfy P-04.

- Decision criterion: P-04 is a biconditional: compliant approval AND PASS AND membership in DL-7.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P07`:

> the temporary exception establishes compliant approval

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Report premise at `P07`:

> the ledger records checksum PASS

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Report premise at `P07`:

> its destination South belongs to DL-7.

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Report inference at `P07`:

> These jointly satisfy P-04.

Assessment: **verified**. Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Report citation at `P07`:

> dispatch-policy.md P-03–P-04; dispatch-ledger.md L-02; destination-list.md D-01.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Independent audit reasoning:

- Independently applying P-03 to B establishes its exception approval.
- L-02 records PASS and South; D-01 lists South throughout days 1–20.
- All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

Independently applying P-03 to B establishes its exception approval. L-02 records PASS and South; D-01 lists South throughout days 1–20. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-04 is a biconditional: compliant approval AND PASS AND membership in DL-7.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. Independently applying P-03 to B establishes its exception approval.
- 2. L-02 records PASS and South; D-01 lists South throughout days 1–20.
- 3. All three settlement conditions hold. Delivery acceptance is explicitly not a condition, so its conflict cannot defeat this conclusion.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-05; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-06

### Exact report claim

`input/report.md#P08`

> Ledger paragraph L-03 restricts the meaning of checksum PASS to package integrity.

### Verification question

Does L-03 actually limit the checksum attestation to package integrity?

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P05`

> [L-03] Checksum PASS means that the byte checksum of the dispatched package matched the approved package checksum. This field describes package integrity only. It does not attest to approval timing, delivery acceptance, future reliability, or eligibility for settlement.


### F11-OK-06: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does L-03 actually limit the checksum attestation to package integrity?

- Decision criterion: Interpret the explicit attestation scope, not an implied guarantee of other properties.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report citation at `P08`:

> dispatch-ledger.md L-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P05`

Independent audit reasoning:

- L-03 states integrity only and explicitly excludes approval timing, acceptance, reliability and settlement.
- The report accurately reports the ledger meaning; this does not claim the package is otherwise safe.

[evidence 0](input/sources/dispatch-ledger.md) at `P05`

Audited claim dependencies: None declared.

Formalization rationale: This is a statement about source text, absence of a definition, or attributed disagreement. Direct documentary inspection is the appropriate method; no mathematical proof of external facts is claimed.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

L-03 states integrity only and explicitly excludes approval timing, acceptance, reliability and settlement. The report accurately reports the ledger meaning; this does not claim the package is otherwise safe.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- Interpret the explicit attestation scope, not an implied guarantee of other properties.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. L-03 states integrity only and explicitly excludes approval timing, acceptance, reliability and settlement.
- 2. The report accurately reports the ledger meaning; this does not claim the package is otherwise safe.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-07

### Exact report claim

`input/report.md#P09`

> The supplied packet cannot establish whether B had zero reliability incidents during days 21–50.

### Verification question

Does the supplied packet determine zero versus any later reliability incidents for B?

### Source evidence

- [input/sources/packet-register.md](input/sources/packet-register.md) — `P02`

> [K-01] The supplied primary packet consists of dispatch-policy.md, dispatch-ledger.md, destination-list.md, delivery-records.md, and this packet-register.md. It contains records only through the end of campaign day 20. The reports under review are not primary evidence.

- [input/sources/packet-register.md](input/sources/packet-register.md) — `P03`

> [K-02] A proposed reliability annex covering days 21–50 is listed as “not supplied.” No observations, measurements, or findings from that period are included in this packet. The register does not state whether any reliability incident actually occurred during that later period.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P05`

> [L-03] Checksum PASS means that the byte checksum of the dispatched package matched the approved package checksum. This field describes package integrity only. It does not attest to approval timing, delivery acceptance, future reliability, or eligibility for settlement.


### F11-OK-07: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet determine zero versus any later reliability incidents for B?

- Decision criterion: A through-day-20 packet and checksum integrity do not observe days 21–50. No bridge rule or later observations are supplied.

Missing definitions: None declared.

Alternatives: Actual acceptance and actual later incidents remain unresolved where mentioned; attributed evidence is not world truth.

Report justification outcome: **sufficient**.

Report premise at `P09`:

> the reliability annex is not supplied

Assessment: **verified**. K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`, [proof 0: Campaign.laterAlternatives](models/Campaign.lean)

Report premise at `P09`:

> there are no observations for that period

Assessment: **verified**. K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`, [proof 0: Campaign.laterAlternatives](models/Campaign.lean)

Report inference at `P09`:

> this is an evidence limitation, not a finding that an incident occurred.

Assessment: **verified**. K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`, [proof 0: Campaign.laterAlternatives](models/Campaign.lean)

Report citation at `P09`:

> packet-register.md K-01–K-02.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`

Independent audit reasoning:

- K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included.
- A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free.
- The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`, [proof 0: Campaign.laterAlternatives](models/Campaign.lean)

Audited claim dependencies: None declared.

Formalization rationale: Auxiliary two-completion witness illustrates the missing constraint; the documentary search establishes which constraints the packet supplies. It is not a direct proof about the unobserved world.

- Proof 0 source-to-target correspondence: L-02 values and P-02/P-03/P-04 rules are transcribed into Campaign declarations; D-01 closes destination membership only during days 1–20. K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free. The meta-level evidence limitation is supported; the actual later incident count remains undetermined. The target Campaign.laterCompatible 0 ∧ Campaign.laterCompatible 1 ∧ (0 : Nat) ≠ 1 is an auxiliary illustration only; it does not determine any missing value. Faithful transcription and the packet domain are assumed; source authenticity is outside the model.

Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- A through-day-20 packet and checksum integrity do not observe days 21–50. No bridge rule or later observations are supplied.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included.
- 2. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free.
- 3. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

### Limits

- No later incident occurrence or nonoccurrence is established. The auxiliary witness formalizes the absence of a supplied constraint; the full packet reading, not the tautological compatibility predicate, justifies that absence.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **auxiliary**.

### Formal evidence

- `Campaign.laterAlternatives` in module `Campaign` (auxiliary): `Campaign.laterCompatible 0 ∧ Campaign.laterCompatible 1 ∧ (0 : Nat) ≠ 1`.
  [Model](models/Campaign.lean) · [Executed check](checks/Target023.lean) · [Actual proof log](logs/target-023.log)

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-07-A01

### Exact report claim

`input/report.md#P09`

> the reliability annex is not supplied

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-07: the reliability annex is not supplied

### Source evidence

- [input/sources/packet-register.md](input/sources/packet-register.md) — `P02`

> [K-01] The supplied primary packet consists of dispatch-policy.md, dispatch-ledger.md, destination-list.md, delivery-records.md, and this packet-register.md. It contains records only through the end of campaign day 20. The reports under review are not primary evidence.

- [input/sources/packet-register.md](input/sources/packet-register.md) — `P03`

> [K-02] A proposed reliability annex covering days 21–50 is listed as “not supplied.” No observations, measurements, or findings from that period are included in this packet. The register does not state whether any reliability incident actually occurred during that later period.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P05`

> [L-03] Checksum PASS means that the byte checksum of the dispatched package matched the approved package checksum. This field describes package integrity only. It does not attest to approval timing, delivery acceptance, future reliability, or eligibility for settlement.


### F11-OK-07-A01: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-07: the reliability annex is not supplied

- Decision criterion: A through-day-20 packet and checksum integrity do not observe days 21–50. No bridge rule or later observations are supplied.

Missing definitions: None declared.

Alternatives: Actual acceptance and actual later incidents remain unresolved where mentioned; attributed evidence is not world truth.

Report justification outcome: **sufficient**.

Report premise at `P09`:

> the reliability annex is not supplied

Assessment: **verified**. K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`

Report premise at `P09`:

> there are no observations for that period

Assessment: **verified**. K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`

Report inference at `P09`:

> this is an evidence limitation, not a finding that an incident occurred.

Assessment: **verified**. K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`

Report citation at `P09`:

> packet-register.md K-01–K-02.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`

Independent audit reasoning:

- K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included.
- A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free.
- The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- A through-day-20 packet and checksum integrity do not observe days 21–50. No bridge rule or later observations are supplied.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included.
- 2. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free.
- 3. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

### Limits

- No later incident occurrence or nonoccurrence is established. The auxiliary witness formalizes the absence of a supplied constraint; the full packet reading, not the tautological compatibility predicate, justifies that absence.
- This fragment is read in its exact parent context F11-OK-07; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-07-A02

### Exact report claim

`input/report.md#P09`

> there are no observations for that period

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-07: there are no observations for that period

### Source evidence

- [input/sources/packet-register.md](input/sources/packet-register.md) — `P02`

> [K-01] The supplied primary packet consists of dispatch-policy.md, dispatch-ledger.md, destination-list.md, delivery-records.md, and this packet-register.md. It contains records only through the end of campaign day 20. The reports under review are not primary evidence.

- [input/sources/packet-register.md](input/sources/packet-register.md) — `P03`

> [K-02] A proposed reliability annex covering days 21–50 is listed as “not supplied.” No observations, measurements, or findings from that period are included in this packet. The register does not state whether any reliability incident actually occurred during that later period.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P05`

> [L-03] Checksum PASS means that the byte checksum of the dispatched package matched the approved package checksum. This field describes package integrity only. It does not attest to approval timing, delivery acceptance, future reliability, or eligibility for settlement.


### F11-OK-07-A02: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-07: there are no observations for that period

- Decision criterion: A through-day-20 packet and checksum integrity do not observe days 21–50. No bridge rule or later observations are supplied.

Missing definitions: None declared.

Alternatives: Actual acceptance and actual later incidents remain unresolved where mentioned; attributed evidence is not world truth.

Report justification outcome: **sufficient**.

Report premise at `P09`:

> the reliability annex is not supplied

Assessment: **verified**. K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`

Report premise at `P09`:

> there are no observations for that period

Assessment: **verified**. K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`

Report inference at `P09`:

> this is an evidence limitation, not a finding that an incident occurred.

Assessment: **verified**. K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`

Report citation at `P09`:

> packet-register.md K-01–K-02.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`

Independent audit reasoning:

- K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included.
- A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free.
- The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- A through-day-20 packet and checksum integrity do not observe days 21–50. No bridge rule or later observations are supplied.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included.
- 2. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free.
- 3. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

### Limits

- No later incident occurrence or nonoccurrence is established. The auxiliary witness formalizes the absence of a supplied constraint; the full packet reading, not the tautological compatibility predicate, justifies that absence.
- This fragment is read in its exact parent context F11-OK-07; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-07-A03

### Exact report claim

`input/report.md#P09`

> this is an evidence limitation, not a finding that an incident occurred.

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-07: this is an evidence limitation, not a finding that an incident occurred.

### Source evidence

- [input/sources/packet-register.md](input/sources/packet-register.md) — `P02`

> [K-01] The supplied primary packet consists of dispatch-policy.md, dispatch-ledger.md, destination-list.md, delivery-records.md, and this packet-register.md. It contains records only through the end of campaign day 20. The reports under review are not primary evidence.

- [input/sources/packet-register.md](input/sources/packet-register.md) — `P03`

> [K-02] A proposed reliability annex covering days 21–50 is listed as “not supplied.” No observations, measurements, or findings from that period are included in this packet. The register does not state whether any reliability incident actually occurred during that later period.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P05`

> [L-03] Checksum PASS means that the byte checksum of the dispatched package matched the approved package checksum. This field describes package integrity only. It does not attest to approval timing, delivery acceptance, future reliability, or eligibility for settlement.


### F11-OK-07-A03: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-07: this is an evidence limitation, not a finding that an incident occurred.

- Decision criterion: A through-day-20 packet and checksum integrity do not observe days 21–50. No bridge rule or later observations are supplied.

Missing definitions: None declared.

Alternatives: Actual acceptance and actual later incidents remain unresolved where mentioned; attributed evidence is not world truth.

Report justification outcome: **sufficient**.

Report premise at `P09`:

> the reliability annex is not supplied

Assessment: **verified**. K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`

Report premise at `P09`:

> there are no observations for that period

Assessment: **verified**. K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`

Report inference at `P09`:

> this is an evidence limitation, not a finding that an incident occurred.

Assessment: **verified**. K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`

Report citation at `P09`:

> packet-register.md K-01–K-02.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`

Independent audit reasoning:

- K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included.
- A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free.
- The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- A through-day-20 packet and checksum integrity do not observe days 21–50. No bridge rule or later observations are supplied.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. K-01 ends records at day 20; K-02 expressly says later annex not supplied and no observations included.
- 2. A later incident count of zero and one are both compatible with that absence of observations; the auxiliary model leaves this omitted count free.
- 3. The meta-level evidence limitation is supported; the actual later incident count remains undetermined.

### Limits

- No later incident occurrence or nonoccurrence is established. The auxiliary witness formalizes the absence of a supplied constraint; the full packet reading, not the tautological compatibility predicate, justifies that absence.
- This fragment is read in its exact parent context F11-OK-07; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-08

### Exact report claim

`input/report.md#P10`

> The supplied packet provides no definition or rating rule for “operationally robust.”

### Verification question

Is an operationally robust definition or rubric present anywhere in the supplied packet?

### Source evidence

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P07`

> [P-06] DP-7 does not define a rating called “operationally robust” or a rule that checksum success implies compliant approval. No other rating standard is incorporated by reference.

- [input/sources/packet-register.md](input/sources/packet-register.md) — `P04`

> [K-03] The packet contains no dispatch-level records for the other 36 campaign dispatches and no statistical sampling or extrapolation method. No additional qualitative rating rubric is supplied.


### F11-OK-08: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Is an operationally robust definition or rubric present anywhere in the supplied packet?

- Decision criterion: A rating needs a supplied operational definition or referenced rubric; none may be invented.

Missing definitions: No operational robustness definition or rating rule is supplied.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report citation at `P10`:

> dispatch-policy.md P-06; packet-register.md K-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-policy.md) at `P07`, [evidence 1](input/sources/packet-register.md) at `P04`

Independent audit reasoning:

- P-06 explicitly disclaims the rating definition and incorporation of another standard.
- K-03 says no further rubric; full reading of all five sources found no contrary rubric.
- The claim concerns packet contents; no objective robustness rating follows.

[evidence 0](input/sources/dispatch-policy.md) at `P07`, [evidence 1](input/sources/packet-register.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This is a statement about source text, absence of a definition, or attributed disagreement. Direct documentary inspection is the appropriate method; no mathematical proof of external facts is claimed.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

P-06 explicitly disclaims the rating definition and incorporation of another standard. K-03 says no further rubric; full reading of all five sources found no contrary rubric. The claim concerns packet contents; no objective robustness rating follows.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- A rating needs a supplied operational definition or referenced rubric; none may be invented.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. P-06 explicitly disclaims the rating definition and incorporation of another standard.
- 2. K-03 says no further rubric; full reading of all five sources found no contrary rubric.
- 3. The claim concerns packet contents; no objective robustness rating follows.

### Limits

- The absence is bounded to the supplied packet. Standards outside it were not searched, and no external rating is inferred.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-09

### Exact report claim

`input/report.md#P11`

> The supplied records conflict about B's acceptance at the end of day 12.

### Verification question

Do two equal-standing records assert and deny the same acceptance event at the same instant?

### Source evidence

- [input/sources/delivery-records.md](input/sources/delivery-records.md) — `P02`

> [R-01] The signed receiving register records: “Dispatch B: ACCEPTED at the end of day 12.” This statement concerns physical delivery acceptance, not approval or settlement.

- [input/sources/delivery-records.md](input/sources/delivery-records.md) — `P03`

> [R-02] The signed incident register records: “Dispatch B: REJECTED at the end of day 12; acceptance did not occur at that time.” This concerns the same physical delivery event and instant as R-01.

- [input/sources/delivery-records.md](input/sources/delivery-records.md) — `P04`

> [R-03] Both records were signed on day 13 by their respective responsible officers. The packet contains no correction, withdrawal, reconciliation, precedence rule, or independent adjudication between R-01 and R-02. For this exercise the two registers have equal evidential standing. Their disagreement is preserved verbatim; neither register is designated authoritative over the other.


### F11-OK-09: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Do two equal-standing records assert and deny the same acceptance event at the same instant?

- Decision criterion: Preserve attribution and compare event, instant, and evidential standing; never conjoin incompatible testimony as world truth.

Missing definitions: None declared.

Alternatives: Actual acceptance and actual later incidents remain unresolved where mentioned; attributed evidence is not world truth.

Report justification outcome: **sufficient**.

Report premise at `P11`:

> R-01 records acceptance

Assessment: **verified**. R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event. R-03 assigns equal evidential standing and supplies no resolution. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Report premise at `P11`:

> R-02 denies it for the same event and instant

Assessment: **verified**. R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event. R-03 assigns equal evidential standing and supplies no resolution. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Report premise at `P11`:

> R-03 supplies no resolution.

Assessment: **verified**. R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event. R-03 assigns equal evidential standing and supplies no resolution. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Report citation at `P11`:

> delivery-records.md R-01–R-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Independent audit reasoning:

- R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event.
- R-03 assigns equal evidential standing and supplies no resolution.
- The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This is a statement about source text, absence of a definition, or attributed disagreement. Direct documentary inspection is the appropriate method; no mathematical proof of external facts is claimed.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event. R-03 assigns equal evidential standing and supplies no resolution. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- Preserve attribution and compare event, instant, and evidential standing; never conjoin incompatible testimony as world truth.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event.
- 2. R-03 assigns equal evidential standing and supplies no resolution.
- 3. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

### Limits

- No proof of acceptance or rejection is claimed. This supported finding is about conflicting records, not simultaneous truth of incompatible events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-09-A01

### Exact report claim

`input/report.md#P11`

> R-01 records acceptance

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-09: R-01 records acceptance

### Source evidence

- [input/sources/delivery-records.md](input/sources/delivery-records.md) — `P02`

> [R-01] The signed receiving register records: “Dispatch B: ACCEPTED at the end of day 12.” This statement concerns physical delivery acceptance, not approval or settlement.

- [input/sources/delivery-records.md](input/sources/delivery-records.md) — `P03`

> [R-02] The signed incident register records: “Dispatch B: REJECTED at the end of day 12; acceptance did not occur at that time.” This concerns the same physical delivery event and instant as R-01.

- [input/sources/delivery-records.md](input/sources/delivery-records.md) — `P04`

> [R-03] Both records were signed on day 13 by their respective responsible officers. The packet contains no correction, withdrawal, reconciliation, precedence rule, or independent adjudication between R-01 and R-02. For this exercise the two registers have equal evidential standing. Their disagreement is preserved verbatim; neither register is designated authoritative over the other.


### F11-OK-09-A01: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-09: R-01 records acceptance

- Decision criterion: Preserve attribution and compare event, instant, and evidential standing; never conjoin incompatible testimony as world truth.

Missing definitions: None declared.

Alternatives: Actual acceptance and actual later incidents remain unresolved where mentioned; attributed evidence is not world truth.

Report justification outcome: **sufficient**.

Report premise at `P11`:

> R-01 records acceptance

Assessment: **verified**. R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event. R-03 assigns equal evidential standing and supplies no resolution. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Report premise at `P11`:

> R-02 denies it for the same event and instant

Assessment: **verified**. R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event. R-03 assigns equal evidential standing and supplies no resolution. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Report premise at `P11`:

> R-03 supplies no resolution.

Assessment: **verified**. R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event. R-03 assigns equal evidential standing and supplies no resolution. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Report citation at `P11`:

> delivery-records.md R-01–R-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Independent audit reasoning:

- R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event.
- R-03 assigns equal evidential standing and supplies no resolution.
- The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event. R-03 assigns equal evidential standing and supplies no resolution. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- Preserve attribution and compare event, instant, and evidential standing; never conjoin incompatible testimony as world truth.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event.
- 2. R-03 assigns equal evidential standing and supplies no resolution.
- 3. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

### Limits

- No proof of acceptance or rejection is claimed. This supported finding is about conflicting records, not simultaneous truth of incompatible events.
- This fragment is read in its exact parent context F11-OK-09; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-09-A02

### Exact report claim

`input/report.md#P11`

> R-02 denies it for the same event and instant

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-09: R-02 denies it for the same event and instant

### Source evidence

- [input/sources/delivery-records.md](input/sources/delivery-records.md) — `P02`

> [R-01] The signed receiving register records: “Dispatch B: ACCEPTED at the end of day 12.” This statement concerns physical delivery acceptance, not approval or settlement.

- [input/sources/delivery-records.md](input/sources/delivery-records.md) — `P03`

> [R-02] The signed incident register records: “Dispatch B: REJECTED at the end of day 12; acceptance did not occur at that time.” This concerns the same physical delivery event and instant as R-01.

- [input/sources/delivery-records.md](input/sources/delivery-records.md) — `P04`

> [R-03] Both records were signed on day 13 by their respective responsible officers. The packet contains no correction, withdrawal, reconciliation, precedence rule, or independent adjudication between R-01 and R-02. For this exercise the two registers have equal evidential standing. Their disagreement is preserved verbatim; neither register is designated authoritative over the other.


### F11-OK-09-A02: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-09: R-02 denies it for the same event and instant

- Decision criterion: Preserve attribution and compare event, instant, and evidential standing; never conjoin incompatible testimony as world truth.

Missing definitions: None declared.

Alternatives: Actual acceptance and actual later incidents remain unresolved where mentioned; attributed evidence is not world truth.

Report justification outcome: **sufficient**.

Report premise at `P11`:

> R-01 records acceptance

Assessment: **verified**. R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event. R-03 assigns equal evidential standing and supplies no resolution. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Report premise at `P11`:

> R-02 denies it for the same event and instant

Assessment: **verified**. R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event. R-03 assigns equal evidential standing and supplies no resolution. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Report premise at `P11`:

> R-03 supplies no resolution.

Assessment: **verified**. R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event. R-03 assigns equal evidential standing and supplies no resolution. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Report citation at `P11`:

> delivery-records.md R-01–R-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Independent audit reasoning:

- R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event.
- R-03 assigns equal evidential standing and supplies no resolution.
- The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event. R-03 assigns equal evidential standing and supplies no resolution. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- Preserve attribution and compare event, instant, and evidential standing; never conjoin incompatible testimony as world truth.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event.
- 2. R-03 assigns equal evidential standing and supplies no resolution.
- 3. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

### Limits

- No proof of acceptance or rejection is claimed. This supported finding is about conflicting records, not simultaneous truth of incompatible events.
- This fragment is read in its exact parent context F11-OK-09; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-09-A03

### Exact report claim

`input/report.md#P11`

> R-03 supplies no resolution.

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-09: R-03 supplies no resolution.

### Source evidence

- [input/sources/delivery-records.md](input/sources/delivery-records.md) — `P02`

> [R-01] The signed receiving register records: “Dispatch B: ACCEPTED at the end of day 12.” This statement concerns physical delivery acceptance, not approval or settlement.

- [input/sources/delivery-records.md](input/sources/delivery-records.md) — `P03`

> [R-02] The signed incident register records: “Dispatch B: REJECTED at the end of day 12; acceptance did not occur at that time.” This concerns the same physical delivery event and instant as R-01.

- [input/sources/delivery-records.md](input/sources/delivery-records.md) — `P04`

> [R-03] Both records were signed on day 13 by their respective responsible officers. The packet contains no correction, withdrawal, reconciliation, precedence rule, or independent adjudication between R-01 and R-02. For this exercise the two registers have equal evidential standing. Their disagreement is preserved verbatim; neither register is designated authoritative over the other.


### F11-OK-09-A03: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-09: R-03 supplies no resolution.

- Decision criterion: Preserve attribution and compare event, instant, and evidential standing; never conjoin incompatible testimony as world truth.

Missing definitions: None declared.

Alternatives: Actual acceptance and actual later incidents remain unresolved where mentioned; attributed evidence is not world truth.

Report justification outcome: **sufficient**.

Report premise at `P11`:

> R-01 records acceptance

Assessment: **verified**. R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event. R-03 assigns equal evidential standing and supplies no resolution. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Report premise at `P11`:

> R-02 denies it for the same event and instant

Assessment: **verified**. R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event. R-03 assigns equal evidential standing and supplies no resolution. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Report premise at `P11`:

> R-03 supplies no resolution.

Assessment: **verified**. R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event. R-03 assigns equal evidential standing and supplies no resolution. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Report citation at `P11`:

> delivery-records.md R-01–R-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Independent audit reasoning:

- R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event.
- R-03 assigns equal evidential standing and supplies no resolution.
- The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event. R-03 assigns equal evidential standing and supplies no resolution. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- Preserve attribution and compare event, instant, and evidential standing; never conjoin incompatible testimony as world truth.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. R-01 records B accepted at end of day 12; R-02 denies acceptance at that same instant and event.
- 2. R-03 assigns equal evidential standing and supplies no resolution.
- 3. The existence of documentary conflict is supported. Actual acceptance remains unresolved; neither source is privileged.

### Limits

- No proof of acceptance or rejection is claimed. This supported finding is about conflicting records, not simultaneous truth of incompatible events.
- This fragment is read in its exact parent context F11-OK-09; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-10

### Exact report claim

`input/report.md#P12`

> Release on day 15 is outside the temporary exception's release window.

### Verification question

Is 15 outside the inclusive release interval [10,14] in P-03?

### Source evidence

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.


### F11-OK-10: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Is 15 outside the inclusive release interval [10,14] in P-03?

- Decision criterion: The exception release window is 10–14 inclusive; ordinary approval is a separate possible route.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P12`:

> the latest permitted release day is 14.

Assessment: **verified**. P-03 gives upper release boundary 14. Day 15 is greater than 14, hence outside that window. This alone does not imply noncompliance under the ordinary route.

[evidence 0](input/sources/dispatch-policy.md) at `P02`, [evidence 1](input/sources/dispatch-policy.md) at `P04`, [proof 0: Campaign.outsideWindow](models/Campaign.lean)

Report citation at `P12`:

> dispatch-policy.md P-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-policy.md) at `P02`, [evidence 1](input/sources/dispatch-policy.md) at `P04`

Independent audit reasoning:

- P-03 gives upper release boundary 14.
- Day 15 is greater than 14, hence outside that window. This alone does not imply noncompliance under the ordinary route.

[evidence 0](input/sources/dispatch-policy.md) at `P02`, [evidence 1](input/sources/dispatch-policy.md) at `P04`, [proof 0: Campaign.outsideWindow](models/Campaign.lean)

Audited claim dependencies: None declared.

Formalization rationale: Finite integer model transcribes the recorded amounts, days, finite membership and explicit rules; direct target is scoped to this claim.

- Proof 0 source-to-target correspondence: L-02 values and P-02/P-03/P-04 rules are transcribed into Campaign declarations; D-01 closes destination membership only during days 1–20. P-03 gives upper release boundary 14. Day 15 is greater than 14, hence outside that window. This alone does not imply noncompliance under the ordinary route. The target ¬ ((10 : Int) ≤ 15 ∧ (15 : Int) ≤ 14) checks the stated finite calculation or rule evaluation. Faithful transcription and the packet domain are assumed; source authenticity is outside the model.

Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

P-03 gives upper release boundary 14. Day 15 is greater than 14, hence outside that window. This alone does not imply noncompliance under the ordinary route.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- The exception release window is 10–14 inclusive; ordinary approval is a separate possible route.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. P-03 gives upper release boundary 14.
- 2. Day 15 is greater than 14, hence outside that window. This alone does not imply noncompliance under the ordinary route.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Campaign.outsideWindow` in module `Campaign` (supports): `¬ ((10 : Int) ≤ 15 ∧ (15 : Int) ≤ 14)`.
  [Model](models/Campaign.lean) · [Executed check](checks/Target024.lean) · [Actual proof log](logs/target-024.log)

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-10-A01

### Exact report claim

`input/report.md#P12`

> the latest permitted release day is 14.

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-10: the latest permitted release day is 14.

### Source evidence

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.


### F11-OK-10-A01: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-10: the latest permitted release day is 14.

- Decision criterion: The exception release window is 10–14 inclusive; ordinary approval is a separate possible route.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P12`:

> the latest permitted release day is 14.

Assessment: **verified**. P-03 gives upper release boundary 14. Day 15 is greater than 14, hence outside that window. This alone does not imply noncompliance under the ordinary route.

[evidence 0](input/sources/dispatch-policy.md) at `P02`, [evidence 1](input/sources/dispatch-policy.md) at `P04`

Report citation at `P12`:

> dispatch-policy.md P-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-policy.md) at `P02`, [evidence 1](input/sources/dispatch-policy.md) at `P04`

Independent audit reasoning:

- P-03 gives upper release boundary 14.
- Day 15 is greater than 14, hence outside that window. This alone does not imply noncompliance under the ordinary route.

[evidence 0](input/sources/dispatch-policy.md) at `P02`, [evidence 1](input/sources/dispatch-policy.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

P-03 gives upper release boundary 14. Day 15 is greater than 14, hence outside that window. This alone does not imply noncompliance under the ordinary route.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- The exception release window is 10–14 inclusive; ordinary approval is a separate possible route.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. P-03 gives upper release boundary 14.
- 2. Day 15 is greater than 14, hence outside that window. This alone does not imply noncompliance under the ordinary route.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-10; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-11

### Exact report claim

`input/report.md#P13`

> The reviewed cohort's eligible settlement amount is 30000 euro cents.

### Verification question

Which of exactly A–D satisfy P-04, and what is their summed integer amount?

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P03`

> [P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P05`

> [P-04] A dispatch is eligible for settlement if and only if it has compliant approval under P-02 or P-03, its recorded checksum result is PASS, and its destination appears in the supplied destination list DL-7. These are three separate necessary conditions; together they are sufficient. Delivery acceptance is not a settlement condition.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P06`

> [P-05] A budget balance means the comparison budget less the sum of dispatch amounts for the stated cohort. Eligible settlement amount means the sum of amounts for the cohort members satisfying P-04. Neither amount includes dispatches outside the stated cohort.

- [input/sources/destination-list.md](input/sources/destination-list.md) — `P02`

> [D-01] DL-7 is the destination list referenced by DP-7 P-04. It was effective throughout campaign days 1–20. Its complete membership is North and South. East is not a member. No amendments apply during this interval.


### F11-OK-11: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Which of exactly A–D satisfy P-04, and what is their summed integer amount?

- Decision criterion: P-02/P-03 exhaust approval routes; P-04 requires approval, PASS, and listed destination; P-05 sums eligible cohort members only.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P13`:

> A has prior approval

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`, [proof 0: Campaign.eligibleExactly](models/Campaign.lean), [proof 1: Campaign.settlement](models/Campaign.lean)

Report premise at `P13`:

> PASS checksum

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`, [proof 0: Campaign.eligibleExactly](models/Campaign.lean), [proof 1: Campaign.settlement](models/Campaign.lean)

Report premise at `P13`:

> listed destination North

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`, [proof 0: Campaign.eligibleExactly](models/Campaign.lean), [proof 1: Campaign.settlement](models/Campaign.lean)

Report inference at `P13`:

> B satisfies all three conditions as shown in the cited records

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`, [proof 0: Campaign.eligibleExactly](models/Campaign.lean), [proof 1: Campaign.settlement](models/Campaign.lean)

Report inference at `P13`:

> C fails approval timing

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`, [proof 0: Campaign.eligibleExactly](models/Campaign.lean), [proof 1: Campaign.settlement](models/Campaign.lean)

Report premise at `P13`:

> D's destination East is not listed.

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`, [proof 0: Campaign.eligibleExactly](models/Campaign.lean), [proof 1: Campaign.settlement](models/Campaign.lean)

Report inference at `P13`:

> the eligible cohort members are exactly A and B

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`, [proof 0: Campaign.eligibleExactly](models/Campaign.lean), [proof 1: Campaign.settlement](models/Campaign.lean)

Report inference at `P13`:

> 12000 + 18000 = 30000.

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`, [proof 0: Campaign.eligibleExactly](models/Campaign.lean), [proof 1: Campaign.settlement](models/Campaign.lean)

Report citation at `P13`:

> dispatch-policy.md P-02–P-05; dispatch-ledger.md L-02; destination-list.md D-01.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Independent audit reasoning:

- A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South.
- C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list.
- The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`, [proof 0: Campaign.eligibleExactly](models/Campaign.lean), [proof 1: Campaign.settlement](models/Campaign.lean)

Audited claim dependencies: None declared.

Formalization rationale: Finite integer model transcribes the recorded amounts, days, finite membership and explicit rules; direct target is scoped to this claim.

- Proof 0 source-to-target correspondence: L-02 values and P-02/P-03/P-04 rules are transcribed into Campaign declarations; D-01 closes destination membership only during days 1–20. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000. The target ∀ x : Campaign.Dispatch, Campaign.eligible x ↔ x = Campaign.Dispatch.a ∨ x = Campaign.Dispatch.b checks the stated finite calculation or rule evaluation. Faithful transcription and the packet domain are assumed; source authenticity is outside the model.
- Proof 1 source-to-target correspondence: L-02 values and P-02/P-03/P-04 rules are transcribed into Campaign declarations; D-01 closes destination membership only during days 1–20. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000. The target Campaign.settlementTotal = 30000 checks the stated finite calculation or rule evaluation. Faithful transcription and the packet domain are assumed; source authenticity is outside the model.

Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-02/P-03 exhaust approval routes; P-04 requires approval, PASS, and listed destination; P-05 sums eligible cohort members only.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South.
- 2. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list.
- 3. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Campaign.eligibleExactly` in module `Campaign` (supports): `∀ x : Campaign.Dispatch, Campaign.eligible x ↔ x = Campaign.Dispatch.a ∨ x = Campaign.Dispatch.b`.
  [Model](models/Campaign.lean) · [Executed check](checks/Target025.lean) · [Actual proof log](logs/target-025.log)

- `Campaign.settlement` in module `Campaign` (supports): `Campaign.settlementTotal = 30000`.
  [Model](models/Campaign.lean) · [Executed check](checks/Target026.lean) · [Actual proof log](logs/target-026.log)

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-11-A01

### Exact report claim

`input/report.md#P13`

> A has prior approval

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-11: A has prior approval

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P03`

> [P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P05`

> [P-04] A dispatch is eligible for settlement if and only if it has compliant approval under P-02 or P-03, its recorded checksum result is PASS, and its destination appears in the supplied destination list DL-7. These are three separate necessary conditions; together they are sufficient. Delivery acceptance is not a settlement condition.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P06`

> [P-05] A budget balance means the comparison budget less the sum of dispatch amounts for the stated cohort. Eligible settlement amount means the sum of amounts for the cohort members satisfying P-04. Neither amount includes dispatches outside the stated cohort.

- [input/sources/destination-list.md](input/sources/destination-list.md) — `P02`

> [D-01] DL-7 is the destination list referenced by DP-7 P-04. It was effective throughout campaign days 1–20. Its complete membership is North and South. East is not a member. No amendments apply during this interval.


### F11-OK-11-A01: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-11: A has prior approval

- Decision criterion: P-02/P-03 exhaust approval routes; P-04 requires approval, PASS, and listed destination; P-05 sums eligible cohort members only.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P13`:

> A has prior approval

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> PASS checksum

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> listed destination North

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> B satisfies all three conditions as shown in the cited records

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> C fails approval timing

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> D's destination East is not listed.

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> the eligible cohort members are exactly A and B

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> 12000 + 18000 = 30000.

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report citation at `P13`:

> dispatch-policy.md P-02–P-05; dispatch-ledger.md L-02; destination-list.md D-01.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Independent audit reasoning:

- A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South.
- C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list.
- The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-02/P-03 exhaust approval routes; P-04 requires approval, PASS, and listed destination; P-05 sums eligible cohort members only.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South.
- 2. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list.
- 3. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-11; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-11-A02

### Exact report claim

`input/report.md#P13`

> PASS checksum

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-11: PASS checksum

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P03`

> [P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P05`

> [P-04] A dispatch is eligible for settlement if and only if it has compliant approval under P-02 or P-03, its recorded checksum result is PASS, and its destination appears in the supplied destination list DL-7. These are three separate necessary conditions; together they are sufficient. Delivery acceptance is not a settlement condition.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P06`

> [P-05] A budget balance means the comparison budget less the sum of dispatch amounts for the stated cohort. Eligible settlement amount means the sum of amounts for the cohort members satisfying P-04. Neither amount includes dispatches outside the stated cohort.

- [input/sources/destination-list.md](input/sources/destination-list.md) — `P02`

> [D-01] DL-7 is the destination list referenced by DP-7 P-04. It was effective throughout campaign days 1–20. Its complete membership is North and South. East is not a member. No amendments apply during this interval.


### F11-OK-11-A02: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-11: PASS checksum

- Decision criterion: P-02/P-03 exhaust approval routes; P-04 requires approval, PASS, and listed destination; P-05 sums eligible cohort members only.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P13`:

> A has prior approval

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> PASS checksum

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> listed destination North

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> B satisfies all three conditions as shown in the cited records

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> C fails approval timing

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> D's destination East is not listed.

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> the eligible cohort members are exactly A and B

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> 12000 + 18000 = 30000.

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report citation at `P13`:

> dispatch-policy.md P-02–P-05; dispatch-ledger.md L-02; destination-list.md D-01.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Independent audit reasoning:

- A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South.
- C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list.
- The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-02/P-03 exhaust approval routes; P-04 requires approval, PASS, and listed destination; P-05 sums eligible cohort members only.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South.
- 2. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list.
- 3. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-11; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-11-A03

### Exact report claim

`input/report.md#P13`

> listed destination North

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-11: listed destination North

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P03`

> [P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P05`

> [P-04] A dispatch is eligible for settlement if and only if it has compliant approval under P-02 or P-03, its recorded checksum result is PASS, and its destination appears in the supplied destination list DL-7. These are three separate necessary conditions; together they are sufficient. Delivery acceptance is not a settlement condition.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P06`

> [P-05] A budget balance means the comparison budget less the sum of dispatch amounts for the stated cohort. Eligible settlement amount means the sum of amounts for the cohort members satisfying P-04. Neither amount includes dispatches outside the stated cohort.

- [input/sources/destination-list.md](input/sources/destination-list.md) — `P02`

> [D-01] DL-7 is the destination list referenced by DP-7 P-04. It was effective throughout campaign days 1–20. Its complete membership is North and South. East is not a member. No amendments apply during this interval.


### F11-OK-11-A03: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-11: listed destination North

- Decision criterion: P-02/P-03 exhaust approval routes; P-04 requires approval, PASS, and listed destination; P-05 sums eligible cohort members only.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P13`:

> A has prior approval

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> PASS checksum

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> listed destination North

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> B satisfies all three conditions as shown in the cited records

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> C fails approval timing

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> D's destination East is not listed.

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> the eligible cohort members are exactly A and B

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> 12000 + 18000 = 30000.

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report citation at `P13`:

> dispatch-policy.md P-02–P-05; dispatch-ledger.md L-02; destination-list.md D-01.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Independent audit reasoning:

- A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South.
- C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list.
- The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-02/P-03 exhaust approval routes; P-04 requires approval, PASS, and listed destination; P-05 sums eligible cohort members only.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South.
- 2. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list.
- 3. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-11; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-11-A04

### Exact report claim

`input/report.md#P13`

> B satisfies all three conditions as shown in the cited records

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-11: B satisfies all three conditions as shown in the cited records

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P03`

> [P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P05`

> [P-04] A dispatch is eligible for settlement if and only if it has compliant approval under P-02 or P-03, its recorded checksum result is PASS, and its destination appears in the supplied destination list DL-7. These are three separate necessary conditions; together they are sufficient. Delivery acceptance is not a settlement condition.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P06`

> [P-05] A budget balance means the comparison budget less the sum of dispatch amounts for the stated cohort. Eligible settlement amount means the sum of amounts for the cohort members satisfying P-04. Neither amount includes dispatches outside the stated cohort.

- [input/sources/destination-list.md](input/sources/destination-list.md) — `P02`

> [D-01] DL-7 is the destination list referenced by DP-7 P-04. It was effective throughout campaign days 1–20. Its complete membership is North and South. East is not a member. No amendments apply during this interval.


### F11-OK-11-A04: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-11: B satisfies all three conditions as shown in the cited records

- Decision criterion: P-02/P-03 exhaust approval routes; P-04 requires approval, PASS, and listed destination; P-05 sums eligible cohort members only.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P13`:

> A has prior approval

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> PASS checksum

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> listed destination North

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> B satisfies all three conditions as shown in the cited records

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> C fails approval timing

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> D's destination East is not listed.

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> the eligible cohort members are exactly A and B

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> 12000 + 18000 = 30000.

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report citation at `P13`:

> dispatch-policy.md P-02–P-05; dispatch-ledger.md L-02; destination-list.md D-01.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Independent audit reasoning:

- A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South.
- C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list.
- The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-02/P-03 exhaust approval routes; P-04 requires approval, PASS, and listed destination; P-05 sums eligible cohort members only.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South.
- 2. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list.
- 3. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-11; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-11-A05

### Exact report claim

`input/report.md#P13`

> C fails approval timing

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-11: C fails approval timing

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P03`

> [P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P05`

> [P-04] A dispatch is eligible for settlement if and only if it has compliant approval under P-02 or P-03, its recorded checksum result is PASS, and its destination appears in the supplied destination list DL-7. These are three separate necessary conditions; together they are sufficient. Delivery acceptance is not a settlement condition.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P06`

> [P-05] A budget balance means the comparison budget less the sum of dispatch amounts for the stated cohort. Eligible settlement amount means the sum of amounts for the cohort members satisfying P-04. Neither amount includes dispatches outside the stated cohort.

- [input/sources/destination-list.md](input/sources/destination-list.md) — `P02`

> [D-01] DL-7 is the destination list referenced by DP-7 P-04. It was effective throughout campaign days 1–20. Its complete membership is North and South. East is not a member. No amendments apply during this interval.


### F11-OK-11-A05: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-11: C fails approval timing

- Decision criterion: P-02/P-03 exhaust approval routes; P-04 requires approval, PASS, and listed destination; P-05 sums eligible cohort members only.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P13`:

> A has prior approval

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> PASS checksum

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> listed destination North

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> B satisfies all three conditions as shown in the cited records

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> C fails approval timing

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> D's destination East is not listed.

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> the eligible cohort members are exactly A and B

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> 12000 + 18000 = 30000.

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report citation at `P13`:

> dispatch-policy.md P-02–P-05; dispatch-ledger.md L-02; destination-list.md D-01.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Independent audit reasoning:

- A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South.
- C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list.
- The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-02/P-03 exhaust approval routes; P-04 requires approval, PASS, and listed destination; P-05 sums eligible cohort members only.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South.
- 2. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list.
- 3. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-11; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-11-A06

### Exact report claim

`input/report.md#P13`

> D's destination East is not listed.

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-11: D's destination East is not listed.

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P03`

> [P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P05`

> [P-04] A dispatch is eligible for settlement if and only if it has compliant approval under P-02 or P-03, its recorded checksum result is PASS, and its destination appears in the supplied destination list DL-7. These are three separate necessary conditions; together they are sufficient. Delivery acceptance is not a settlement condition.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P06`

> [P-05] A budget balance means the comparison budget less the sum of dispatch amounts for the stated cohort. Eligible settlement amount means the sum of amounts for the cohort members satisfying P-04. Neither amount includes dispatches outside the stated cohort.

- [input/sources/destination-list.md](input/sources/destination-list.md) — `P02`

> [D-01] DL-7 is the destination list referenced by DP-7 P-04. It was effective throughout campaign days 1–20. Its complete membership is North and South. East is not a member. No amendments apply during this interval.


### F11-OK-11-A06: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-11: D's destination East is not listed.

- Decision criterion: P-02/P-03 exhaust approval routes; P-04 requires approval, PASS, and listed destination; P-05 sums eligible cohort members only.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P13`:

> A has prior approval

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> PASS checksum

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> listed destination North

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> B satisfies all three conditions as shown in the cited records

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> C fails approval timing

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> D's destination East is not listed.

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> the eligible cohort members are exactly A and B

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> 12000 + 18000 = 30000.

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report citation at `P13`:

> dispatch-policy.md P-02–P-05; dispatch-ledger.md L-02; destination-list.md D-01.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Independent audit reasoning:

- A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South.
- C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list.
- The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-02/P-03 exhaust approval routes; P-04 requires approval, PASS, and listed destination; P-05 sums eligible cohort members only.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South.
- 2. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list.
- 3. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-11; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-11-A07

### Exact report claim

`input/report.md#P13`

> the eligible cohort members are exactly A and B

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-11: the eligible cohort members are exactly A and B

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P03`

> [P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P05`

> [P-04] A dispatch is eligible for settlement if and only if it has compliant approval under P-02 or P-03, its recorded checksum result is PASS, and its destination appears in the supplied destination list DL-7. These are three separate necessary conditions; together they are sufficient. Delivery acceptance is not a settlement condition.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P06`

> [P-05] A budget balance means the comparison budget less the sum of dispatch amounts for the stated cohort. Eligible settlement amount means the sum of amounts for the cohort members satisfying P-04. Neither amount includes dispatches outside the stated cohort.

- [input/sources/destination-list.md](input/sources/destination-list.md) — `P02`

> [D-01] DL-7 is the destination list referenced by DP-7 P-04. It was effective throughout campaign days 1–20. Its complete membership is North and South. East is not a member. No amendments apply during this interval.


### F11-OK-11-A07: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-11: the eligible cohort members are exactly A and B

- Decision criterion: P-02/P-03 exhaust approval routes; P-04 requires approval, PASS, and listed destination; P-05 sums eligible cohort members only.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P13`:

> A has prior approval

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> PASS checksum

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> listed destination North

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> B satisfies all three conditions as shown in the cited records

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> C fails approval timing

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> D's destination East is not listed.

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> the eligible cohort members are exactly A and B

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> 12000 + 18000 = 30000.

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report citation at `P13`:

> dispatch-policy.md P-02–P-05; dispatch-ledger.md L-02; destination-list.md D-01.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Independent audit reasoning:

- A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South.
- C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list.
- The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-02/P-03 exhaust approval routes; P-04 requires approval, PASS, and listed destination; P-05 sums eligible cohort members only.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South.
- 2. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list.
- 3. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-11; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-11-A08

### Exact report claim

`input/report.md#P13`

> 12000 + 18000 = 30000.

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-11: 12000 + 18000 = 30000.

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P03`

> [P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P05`

> [P-04] A dispatch is eligible for settlement if and only if it has compliant approval under P-02 or P-03, its recorded checksum result is PASS, and its destination appears in the supplied destination list DL-7. These are three separate necessary conditions; together they are sufficient. Delivery acceptance is not a settlement condition.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P06`

> [P-05] A budget balance means the comparison budget less the sum of dispatch amounts for the stated cohort. Eligible settlement amount means the sum of amounts for the cohort members satisfying P-04. Neither amount includes dispatches outside the stated cohort.

- [input/sources/destination-list.md](input/sources/destination-list.md) — `P02`

> [D-01] DL-7 is the destination list referenced by DP-7 P-04. It was effective throughout campaign days 1–20. Its complete membership is North and South. East is not a member. No amendments apply during this interval.


### F11-OK-11-A08: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-11: 12000 + 18000 = 30000.

- Decision criterion: P-02/P-03 exhaust approval routes; P-04 requires approval, PASS, and listed destination; P-05 sums eligible cohort members only.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P13`:

> A has prior approval

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> PASS checksum

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> listed destination North

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> B satisfies all three conditions as shown in the cited records

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> C fails approval timing

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report premise at `P13`:

> D's destination East is not listed.

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> the eligible cohort members are exactly A and B

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report inference at `P13`:

> 12000 + 18000 = 30000.

Assessment: **verified**. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Report citation at `P13`:

> dispatch-policy.md P-02–P-05; dispatch-ledger.md L-02; destination-list.md D-01.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Independent audit reasoning:

- A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South.
- C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list.
- The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [evidence 4](input/sources/dispatch-policy.md) at `P03`, [evidence 5](input/sources/dispatch-policy.md) at `P04`, [evidence 6](input/sources/dispatch-policy.md) at `P05`, [evidence 7](input/sources/dispatch-policy.md) at `P06`, [evidence 8](input/sources/destination-list.md) at `P02`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- P-02/P-03 exhaust approval routes; P-04 requires approval, PASS, and listed destination; P-05 sums eligible cohort members only.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. A has approval 4 < release 5, PASS, North; B has exception approval, PASS, South.
- 2. C fails both approval routes; D has ordinary approval and PASS but destination East is explicitly absent from the complete D-01 list.
- 3. The nonempty complete cohort is exactly A–D, so eligible members are exactly A and B. Their amounts 12000 and 18000 total 30000.

### Limits

- This is a documentary conclusion conditional on faithful transcription of the synthetic packet, not authentication of actual dispatch events.
- This fragment is read in its exact parent context F11-OK-11; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-12

### Exact report claim

`input/report.md#P14`

> The supplied four-row ledger does not establish the total amount of all 40 campaign dispatches.

### Verification question

Does four-row cohort evidence determine the sum of the full population of 40 dispatches?

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/packet-register.md](input/sources/packet-register.md) — `P04`

> [K-03] The packet contains no dispatch-level records for the other 36 campaign dispatches and no statistical sampling or extrapolation method. No additional qualitative rating rubric is supplied.


### F11-OK-12: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does four-row cohort evidence determine the sum of the full population of 40 dispatches?

- Decision criterion: L-01 limits this complete cohort snapshot to four of 40; K-03 denies records and an extrapolation method for the other 36.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P14`:

> the snapshot covers four named dispatches

Assessment: **verified**. Known cohort total is 50000, but the other 36 amounts are not supplied. A completion with each omitted amount zero gives 50000; one euro cent each gives 50036. Neither completion is excluded by the supplied amount constraints. This auxiliary countermodel pair illustrates nondetermination, not either actual full population total.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/packet-register.md) at `P04`, [proof 0: Campaign.populationAlternatives](models/Campaign.lean)

Report premise at `P14`:

> supplies no amounts for the remaining 36.

Assessment: **verified**. Known cohort total is 50000, but the other 36 amounts are not supplied. A completion with each omitted amount zero gives 50000; one euro cent each gives 50036. Neither completion is excluded by the supplied amount constraints. This auxiliary countermodel pair illustrates nondetermination, not either actual full population total.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/packet-register.md) at `P04`, [proof 0: Campaign.populationAlternatives](models/Campaign.lean)

Report citation at `P14`:

> dispatch-ledger.md L-01–L-02; packet-register.md K-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/packet-register.md) at `P04`

Independent audit reasoning:

- Known cohort total is 50000, but the other 36 amounts are not supplied.
- A completion with each omitted amount zero gives 50000; one euro cent each gives 50036. Neither completion is excluded by the supplied amount constraints.
- This auxiliary countermodel pair illustrates nondetermination, not either actual full population total.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/packet-register.md) at `P04`, [proof 0: Campaign.populationAlternatives](models/Campaign.lean)

Audited claim dependencies: None declared.

Formalization rationale: Auxiliary two-completion witness illustrates the missing constraint; the documentary search establishes which constraints the packet supplies. It is not a direct proof about the unobserved world.

- Proof 0 source-to-target correspondence: L-02 values and P-02/P-03/P-04 rules are transcribed into Campaign declarations; D-01 closes destination membership only during days 1–20. Known cohort total is 50000, but the other 36 amounts are not supplied. A completion with each omitted amount zero gives 50000; one euro cent each gives 50036. Neither completion is excluded by the supplied amount constraints. This auxiliary countermodel pair illustrates nondetermination, not either actual full population total. The target Campaign.populationCompletion 0 = 50000 ∧ Campaign.populationCompletion 1 = 50036 ∧ Campaign.populationCompletion 0 ≠ Campaign.populationCompletion 1 is an auxiliary illustration only; it does not determine any missing value. Faithful transcription and the packet domain are assumed; source authenticity is outside the model.

Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

Known cohort total is 50000, but the other 36 amounts are not supplied. A completion with each omitted amount zero gives 50000; one euro cent each gives 50036. Neither completion is excluded by the supplied amount constraints. This auxiliary countermodel pair illustrates nondetermination, not either actual full population total.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- L-01 limits this complete cohort snapshot to four of 40; K-03 denies records and an extrapolation method for the other 36.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. Known cohort total is 50000, but the other 36 amounts are not supplied.
- 2. A completion with each omitted amount zero gives 50000; one euro cent each gives 50036. Neither completion is excluded by the supplied amount constraints.
- 3. This auxiliary countermodel pair illustrates nondetermination, not either actual full population total.

### Limits

- The actual full-population total is undetermined; no extrapolation or value for the unprovided 36 records is asserted.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **auxiliary**.

### Formal evidence

- `Campaign.populationAlternatives` in module `Campaign` (auxiliary): `Campaign.populationCompletion 0 = 50000 ∧ Campaign.populationCompletion 1 = 50036 ∧ Campaign.populationCompletion 0 ≠ Campaign.populationCompletion 1`.
  [Model](models/Campaign.lean) · [Executed check](checks/Target027.lean) · [Actual proof log](logs/target-027.log)

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-12-A01

### Exact report claim

`input/report.md#P14`

> the snapshot covers four named dispatches

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-12: the snapshot covers four named dispatches

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/packet-register.md](input/sources/packet-register.md) — `P04`

> [K-03] The packet contains no dispatch-level records for the other 36 campaign dispatches and no statistical sampling or extrapolation method. No additional qualitative rating rubric is supplied.


### F11-OK-12-A01: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-12: the snapshot covers four named dispatches

- Decision criterion: L-01 limits this complete cohort snapshot to four of 40; K-03 denies records and an extrapolation method for the other 36.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P14`:

> the snapshot covers four named dispatches

Assessment: **verified**. Known cohort total is 50000, but the other 36 amounts are not supplied. A completion with each omitted amount zero gives 50000; one euro cent each gives 50036. Neither completion is excluded by the supplied amount constraints. This auxiliary countermodel pair illustrates nondetermination, not either actual full population total.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/packet-register.md) at `P04`

Report premise at `P14`:

> supplies no amounts for the remaining 36.

Assessment: **verified**. Known cohort total is 50000, but the other 36 amounts are not supplied. A completion with each omitted amount zero gives 50000; one euro cent each gives 50036. Neither completion is excluded by the supplied amount constraints. This auxiliary countermodel pair illustrates nondetermination, not either actual full population total.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/packet-register.md) at `P04`

Report citation at `P14`:

> dispatch-ledger.md L-01–L-02; packet-register.md K-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/packet-register.md) at `P04`

Independent audit reasoning:

- Known cohort total is 50000, but the other 36 amounts are not supplied.
- A completion with each omitted amount zero gives 50000; one euro cent each gives 50036. Neither completion is excluded by the supplied amount constraints.
- This auxiliary countermodel pair illustrates nondetermination, not either actual full population total.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/packet-register.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

Known cohort total is 50000, but the other 36 amounts are not supplied. A completion with each omitted amount zero gives 50000; one euro cent each gives 50036. Neither completion is excluded by the supplied amount constraints. This auxiliary countermodel pair illustrates nondetermination, not either actual full population total.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- L-01 limits this complete cohort snapshot to four of 40; K-03 denies records and an extrapolation method for the other 36.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. Known cohort total is 50000, but the other 36 amounts are not supplied.
- 2. A completion with each omitted amount zero gives 50000; one euro cent each gives 50036. Neither completion is excluded by the supplied amount constraints.
- 3. This auxiliary countermodel pair illustrates nondetermination, not either actual full population total.

### Limits

- The actual full-population total is undetermined; no extrapolation or value for the unprovided 36 records is asserted.
- This fragment is read in its exact parent context F11-OK-12; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.

## F11-OK-12-A02

### Exact report claim

`input/report.md#P14`

> supplies no amounts for the remaining 36.

### Verification question

Does the supplied packet support this explicit premise or inference of F11-OK-12: supplies no amounts for the remaining 36.

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/packet-register.md](input/sources/packet-register.md) — `P04`

> [K-03] The packet contains no dispatch-level records for the other 36 campaign dispatches and no statistical sampling or extrapolation method. No additional qualitative rating rubric is supplied.


### F11-OK-12-A02: criteria and report argument audit

Criteria origin: **inferred**. Scope: A–D at cutoff day 20 unless explicitly concerning later days 21–50, acceptance at end of day 12, or the full population of 40.

Does the supplied packet support this explicit premise or inference of F11-OK-12: supplies no amounts for the remaining 36.

- Decision criterion: L-01 limits this complete cohort snapshot to four of 40; K-03 denies records and an extrapolation method for the other 36.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P14`:

> the snapshot covers four named dispatches

Assessment: **verified**. Known cohort total is 50000, but the other 36 amounts are not supplied. A completion with each omitted amount zero gives 50000; one euro cent each gives 50036. Neither completion is excluded by the supplied amount constraints. This auxiliary countermodel pair illustrates nondetermination, not either actual full population total.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/packet-register.md) at `P04`

Report premise at `P14`:

> supplies no amounts for the remaining 36.

Assessment: **verified**. Known cohort total is 50000, but the other 36 amounts are not supplied. A completion with each omitted amount zero gives 50000; one euro cent each gives 50036. Neither completion is excluded by the supplied amount constraints. This auxiliary countermodel pair illustrates nondetermination, not either actual full population total.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/packet-register.md) at `P04`

Report citation at `P14`:

> dispatch-ledger.md L-01–L-02; packet-register.md K-03.

Assessment: **verified**. The named author passages were inspected in context. Their source labels map to the generated ledger anchors below; L-02 includes its separately anchored table. These passages support the stated claim within the disclosed scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/packet-register.md) at `P04`

Independent audit reasoning:

- Known cohort total is 50000, but the other 36 amounts are not supplied.
- A completion with each omitted amount zero gives 50000; one euro cent each gives 50036. Neither completion is excluded by the supplied amount constraints.
- This auxiliary countermodel pair illustrates nondetermination, not either actual full population total.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/packet-register.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: This separately registered argument component is checked directly against the source evidence and contextual reasoning. The parent conclusion carries any larger formal calculation; no separate direct proof is claimed for this fragment.


Declared bounded support search: Read every passage of all five supplied sources, checked author citations in context and sought counterevidence; no report text used as independent evidence.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P01`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P02`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P03`.
- Inspected [input/sources/delivery-records.md](input/sources/delivery-records.md) at `P04`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P01`.
- Inspected [input/sources/destination-list.md](input/sources/destination-list.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P01`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P02`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P03`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P04`.
- Inspected [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P01`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P02`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P03`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P04`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P05`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P06`.
- Inspected [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) at `P07`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P01`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P02`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P03`.
- Inspected [input/sources/packet-register.md](input/sources/packet-register.md) at `P04`.

Known cohort total is 50000, but the other 36 amounts are not supplied. A completion with each omitted amount zero gives 50000; one euro cent each gives 50036. Neither completion is excluded by the supplied amount constraints. This auxiliary countermodel pair illustrates nondetermination, not either actual full population total.

Search limits: The search is confined to the supplied packet; no withheld annex, other dispatch records, external rating rules or external source authentication are available.

### Rules

- L-01 limits this complete cohort snapshot to four of 40; K-03 denies records and an extrapolation method for the other 36.

### Assumptions

- The supplied synthetic packet is read literally in its declared scope; source authenticity is not established.

### Reasoning

- 1. Known cohort total is 50000, but the other 36 amounts are not supplied.
- 2. A completion with each omitted amount zero gives 50000; one euro cent each gives 50036. Neither completion is excluded by the supplied amount constraints.
- 3. This auxiliary countermodel pair illustrates nondetermination, not either actual full population total.

### Limits

- The actual full-population total is undetermined; no extrapolation or value for the unprovided 36 records is asserted.
- This fragment is read in its exact parent context F11-OK-12; it is not generalized beyond that dispatch, period or population.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the finding with its stated scope and evidence limitations.
