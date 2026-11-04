# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

## Registered claim coverage

Coverage: **complete_registration**; 14 reviewed anchors; 12 audited and 0 deferred claims.

Registration reconciles declared claims and reviewed report anchors; it does not establish semantic completeness, faithful decomposition, or that declared searches were actually performed.

- `P01`: non_claim — Heading or statement of review scope; no domain finding.
- `P02`: non_claim — Heading or statement of review scope; no domain finding.
- `P03`: claims — Atomic finding conclusion; all material author premises, citations and steps are audited separately in argument_audit.
- `P04`: claims — Atomic finding conclusion; all material author premises, citations and steps are audited separately in argument_audit.
- `P05`: claims — Atomic finding conclusion; all material author premises, citations and steps are audited separately in argument_audit.
- `P06`: claims — Atomic finding conclusion; all material author premises, citations and steps are audited separately in argument_audit.
- `P07`: claims — Atomic finding conclusion; all material author premises, citations and steps are audited separately in argument_audit.
- `P08`: claims — Atomic finding conclusion; all material author premises, citations and steps are audited separately in argument_audit.
- `P09`: claims — Atomic finding conclusion; all material author premises, citations and steps are audited separately in argument_audit.
- `P10`: claims — Atomic finding conclusion; all material author premises, citations and steps are audited separately in argument_audit.
- `P11`: claims — Atomic finding conclusion; all material author premises, citations and steps are audited separately in argument_audit.
- `P12`: claims — Atomic finding conclusion; all material author premises, citations and steps are audited separately in argument_audit.
- `P13`: claims — Atomic finding conclusion; all material author premises, citations and steps are audited separately in argument_audit.
- `P14`: claims — Atomic finding conclusion; all material author premises, citations and steps are audited separately in argument_audit.
[Semantic correspondence review](semantic-review.md)

## F11-01

### Exact report claim

`input/report.md#P03`

> The total amount of the reviewed cohort is 50000 euro cents.

### Verification question

Does the complete four-dispatch cohort sum to 50000 cents?

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


### F11-01: criteria and report argument audit

Criteria origin: **inferred**. Scope: Exactly dispatches A, B, C and D through end of campaign day 20; integer campaign days and euro cents under DP-7 and DL-7.

Does the complete four-dispatch cohort sum to 50000 cents?

- Decision criterion: Sum each of the exactly four cohort amounts once.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P03`:

> 12000 + 18000 + 9000 + 11000

Assessment: **verified**. All four operands agree with L-02.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P06`, [proof 0: Audit.expenditure](models/Audit.lean)

Report inference at `P03`:

> 12000 + 18000 + 9000 + 11000 = 50000.

Assessment: **verified**. The exact integer sum is checked independently.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P06`, [proof 0: Audit.expenditure](models/Audit.lean)

Report citation at `P03`:

> dispatch-ledger.md L-02.

Assessment: **verified**. The named supplied passages exist and are reproduced in evidence; their relevance and inferential limits are assessed separately below.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P06`, [proof 0: Audit.expenditure](models/Audit.lean)

Independent audit reasoning:

- L-01 defines A–D as the complete reviewed cohort; L-02 records 12000, 18000, 9000 and 11000 cents.
- The sum is 50000; both the author operands and computation are correct.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P06`, [proof 0: Audit.expenditure](models/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: Small finite source-linked model checks arithmetic, rule applications or a precisely limited auxiliary target; statements of unavailable events remain unconstrained.

- Proof 0 source-to-target correspondence: Audit.cohort contains the four L-02 rows exactly once and total sums their Int amounts; the target is the original cohort total, assuming faithful transcription.

Declared bounded support search: Read every paragraph and table in all five supplied source documents, including cited passages and counterevidence.

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

L-01 defines A–D as the complete reviewed cohort; L-02 records 12000, 18000, 9000 and 11000 cents. The sum is 50000; both the author operands and computation are correct.

Search limits: No external evidence, unavailable reliability annex, missing 36 population records, or unprovided rating rubric was inspected.

### Rules

- Sum each of the exactly four cohort amounts once.

### Assumptions

- The supplied synthetic records are faithfully transcribed; source authenticity is outside this audit.

### Reasoning

- L-01 defines A–D as the complete reviewed cohort; L-02 records 12000, 18000, 9000 and 11000 cents.
- The sum is 50000; both the author operands and computation are correct.

### Limits

- The result is scoped to the supplied synthetic packet and declared policy.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.expenditure` in module `Audit` (supports): `Audit.total = 50000`.
  [Model](models/Audit.lean) · [Executed check](checks/Target016.lean) · [Actual proof log](logs/target-016.log)

### Recommendation

Retain the finding and its cohort limitation.

## F11-02

### Exact report claim

`input/report.md#P04`

> The cohort budget balance is 6000 euro cents.

### Verification question

Is the cohort budget less cohort expenditure equal to 6000 cents?

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P06`

> [P-05] A budget balance means the comparison budget less the sum of dispatch amounts for the stated cohort. Eligible settlement amount means the sum of amounts for the cohort members satisfying P-04. Neither amount includes dispatches outside the stated cohort.


### F11-02: criteria and report argument audit

Criteria origin: **inferred**. Scope: Exactly dispatches A, B, C and D through end of campaign day 20; integer campaign days and euro cents under DP-7 and DL-7.

Is the cohort budget less cohort expenditure equal to 6000 cents?

- Decision criterion: P-05 defines balance as 55000 minus the four-dispatch sum.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **invalid**.

Report premise at `P04`:

> 55000-cent comparison budget

Assessment: **verified**. L-01 gives exactly this budget.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P04`, [evidence 2](input/sources/dispatch-policy.md) at `P06`, [proof 0: Audit.headroom](models/Audit.lean)

Report inference at `P04`:

> subtract the four dispatch amounts from the 55000-cent comparison budget.

Assessment: **contradicted**. This stated operation produces 5000, not the claimed 6000; the inference to that result fails.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P04`, [evidence 2](input/sources/dispatch-policy.md) at `P06`, [proof 0: Audit.headroom](models/Audit.lean)

Report citation at `P04`:

> dispatch-ledger.md L-01–L-02; dispatch-policy.md P-05.

Assessment: **verified**. The named supplied passages exist and are reproduced in evidence; their relevance and inferential limits are assessed separately below.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P04`, [evidence 2](input/sources/dispatch-policy.md) at `P06`, [proof 0: Audit.headroom](models/Audit.lean)

Independent audit reasoning:

- The source budget is 55000 and the four entries sum to 50000.
- 55000 - 50000 = 5000, contradicting 6000. The proposed subtraction method is valid but does not yield the reported value.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P04`, [evidence 2](input/sources/dispatch-policy.md) at `P06`, [proof 0: Audit.headroom](models/Audit.lean)

Audited claim dependencies: F11-01

Formalization rationale: Small finite source-linked model checks arithmetic, rule applications or a precisely limited auxiliary target; statements of unavailable events remain unconstrained.

- Proof 0 source-to-target correspondence: Balance uses the 55000 budget from L-01 and the four L-02 amounts with Int subtraction, not truncated natural subtraction; 6000 is directly excluded.

Declared bounded support search: Read every paragraph and table in all five supplied source documents, including cited passages and counterevidence.

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

The source budget is 55000 and the four entries sum to 50000. 55000 - 50000 = 5000, contradicting 6000. The proposed subtraction method is valid but does not yield the reported value.

Search limits: No external evidence, unavailable reliability annex, missing 36 population records, or unprovided rating rubric was inspected.

### Rules

- P-05 defines balance as 55000 minus the four-dispatch sum.

### Assumptions

- The supplied synthetic records are faithfully transcribed; source authenticity is outside this audit.

### Reasoning

- The source budget is 55000 and the four entries sum to 50000.
- 55000 - 50000 = 5000, contradicting 6000. The proposed subtraction method is valid but does not yield the reported value.

### Limits

- The result is scoped to the supplied synthetic packet and declared policy.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.headroom` in module `Audit` (refutes): `Audit.balance = 5000 ∧ Audit.balance ≠ 6000`.
  [Model](models/Audit.lean) · [Executed check](checks/Target017.lean) · [Actual proof log](logs/target-017.log)

### Recommendation

Replace 6000 with 5000 euro cents.

## F11-03

### Exact report claim

`input/report.md#P05`

> B has noncompliant approval at cutoff.

### Verification question

Does B fail both available approval routes at cutoff?

### Source evidence

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


### F11-03: criteria and report argument audit

Criteria origin: **inferred**. Scope: Exactly dispatches A, B, C and D through end of campaign day 20; integer campaign days and euro cents under DP-7 and DL-7.

Does B fail both available approval routes at cutoff?

- Decision criterion: Ordinary approval requires approval strictly before release.
- Decision criterion: P-03 also permits R2 releases on days 10–14 with a declaration no more than two days earlier and approval no more than three days later.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **invalid**.

Report premise at `P05`:

> its approval on day 15 was later than its release on day 12

Assessment: **verified**. The ledger records 15 > 12.

[evidence 0](input/sources/dispatch-ledger.md) at `P03`, [evidence 1](input/sources/dispatch-ledger.md) at `P04`, [evidence 2](input/sources/dispatch-policy.md) at `P02`, [evidence 3](input/sources/dispatch-policy.md) at `P03`, [evidence 4](input/sources/dispatch-policy.md) at `P04`, [proof 0: Audit.bApproval](models/Audit.lean), [proof 1: Audit.bException](models/Audit.lean)

Report inference at `P05`:

> so it fails the only approval route.

Assessment: **contradicted**. P-03 expressly provides a second route, which B satisfies.

[evidence 0](input/sources/dispatch-ledger.md) at `P03`, [evidence 1](input/sources/dispatch-ledger.md) at `P04`, [evidence 2](input/sources/dispatch-policy.md) at `P02`, [evidence 3](input/sources/dispatch-policy.md) at `P03`, [evidence 4](input/sources/dispatch-policy.md) at `P04`, [proof 0: Audit.bApproval](models/Audit.lean), [proof 1: Audit.bException](models/Audit.lean)

Report citation at `P05`:

> dispatch-ledger.md L-02; dispatch-policy.md P-02.

Assessment: **verified**. The named supplied passages exist and are reproduced in evidence; their relevance and inferential limits are assessed separately below. P-02 describes only the ordinary route; the author omitted P-03.

[evidence 0](input/sources/dispatch-ledger.md) at `P03`, [evidence 1](input/sources/dispatch-ledger.md) at `P04`, [evidence 2](input/sources/dispatch-policy.md) at `P02`, [evidence 3](input/sources/dispatch-policy.md) at `P03`, [evidence 4](input/sources/dispatch-policy.md) at `P04`, [proof 0: Audit.bApproval](models/Audit.lean), [proof 1: Audit.bException](models/Audit.lean)

Independent audit reasoning:

- B release 12 and approval 15 fail the ordinary route.
- B is R2, release 12 is within 10–14, declaration 11 is one day before release, and approval 15 is exactly three days later. Every exception conjunct holds.
- B has compliant approval, so the report is false. Failure of one route does not imply failure of the alternative.

[evidence 0](input/sources/dispatch-ledger.md) at `P03`, [evidence 1](input/sources/dispatch-ledger.md) at `P04`, [evidence 2](input/sources/dispatch-policy.md) at `P02`, [evidence 3](input/sources/dispatch-policy.md) at `P03`, [evidence 4](input/sources/dispatch-policy.md) at `P04`, [proof 0: Audit.bApproval](models/Audit.lean), [proof 1: Audit.bException](models/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: Small finite source-linked model checks arithmetic, rule applications or a precisely limited auxiliary target; statements of unavailable events remain unconstrained.

- Proof 0 source-to-target correspondence: The exact claim is noncompliance, so proof of B compliance refutes it. P-02 and P-03 are a disjunction and all B fields come from L-02.
- Proof 1 source-to-target correspondence: B fails the ordinary timing predicate but satisfies every temporary-exception conjunct; this isolates the author omission.

Declared bounded support search: Read every paragraph and table in all five supplied source documents, including cited passages and counterevidence.

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

B release 12 and approval 15 fail the ordinary route. B is R2, release 12 is within 10–14, declaration 11 is one day before release, and approval 15 is exactly three days later. Every exception conjunct holds. B has compliant approval, so the report is false. Failure of one route does not imply failure of the alternative.

Search limits: No external evidence, unavailable reliability annex, missing 36 population records, or unprovided rating rubric was inspected.

### Rules

- Ordinary approval requires approval strictly before release.
- P-03 also permits R2 releases on days 10–14 with a declaration no more than two days earlier and approval no more than three days later.

### Assumptions

- The supplied synthetic records are faithfully transcribed; source authenticity is outside this audit.

### Reasoning

- B release 12 and approval 15 fail the ordinary route.
- B is R2, release 12 is within 10–14, declaration 11 is one day before release, and approval 15 is exactly three days later. Every exception conjunct holds.
- B has compliant approval, so the report is false. Failure of one route does not imply failure of the alternative.

### Limits

- The result is scoped to the supplied synthetic packet and declared policy.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.bApproval` in module `Audit` (refutes): `Audit.compliant Audit.b`.
  [Model](models/Audit.lean) · [Executed check](checks/Target018.lean) · [Actual proof log](logs/target-018.log)

- `Audit.bException` in module `Audit` (auxiliary): `¬ Audit.ordinary Audit.b ∧ Audit.exception Audit.b`.
  [Model](models/Audit.lean) · [Executed check](checks/Target019.lean) · [Actual proof log](logs/target-019.log)

### Recommendation

State that B is compliant through the exception; include P-03.

## F11-04

### Exact report claim

`input/report.md#P06`

> C has compliant approval at cutoff under the temporary exception.

### Verification question

Does C satisfy every temporary-exception condition?

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P03`

> [L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P03`

> [P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.


### F11-04: criteria and report argument audit

Criteria origin: **inferred**. Scope: Exactly dispatches A, B, C and D through end of campaign day 20; integer campaign days and euro cents under DP-7 and DL-7.

Does C satisfy every temporary-exception condition?

- Decision criterion: The exception permits approval at most three days after release; no other route beyond ordinary or exception applies.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **invalid**.

Report premise at `P06`:

> approval on day 16 was within three days of release on day 12.

Assessment: **contradicted**. 16 - 12 equals four, not at most three.

[evidence 0](input/sources/dispatch-ledger.md) at `P03`, [evidence 1](input/sources/dispatch-ledger.md) at `P04`, [evidence 2](input/sources/dispatch-policy.md) at `P03`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [proof 0: Audit.cApproval](models/Audit.lean), [proof 1: Audit.cDelay](models/Audit.lean)

Report inference at `P06`:

> approval on day 16 was within three days of release on day 12.

Assessment: **contradicted**. The false deadline premise cannot establish exception compliance.

[evidence 0](input/sources/dispatch-ledger.md) at `P03`, [evidence 1](input/sources/dispatch-ledger.md) at `P04`, [evidence 2](input/sources/dispatch-policy.md) at `P03`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [proof 0: Audit.cApproval](models/Audit.lean), [proof 1: Audit.cDelay](models/Audit.lean)

Report citation at `P06`:

> dispatch-ledger.md L-02; dispatch-policy.md P-03.

Assessment: **verified**. The named supplied passages exist and are reproduced in evidence; their relevance and inferential limits are assessed separately below.

[evidence 0](input/sources/dispatch-ledger.md) at `P03`, [evidence 1](input/sources/dispatch-ledger.md) at `P04`, [evidence 2](input/sources/dispatch-policy.md) at `P03`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [proof 0: Audit.cApproval](models/Audit.lean), [proof 1: Audit.cDelay](models/Audit.lean)

Independent audit reasoning:

- C release 12 and approval 16 have a four-day gap.
- C fails the exception upper bound and also fails ordinary prior approval. Its route, release-window and declaration checks do not repair the failed approval deadline.

[evidence 0](input/sources/dispatch-ledger.md) at `P03`, [evidence 1](input/sources/dispatch-ledger.md) at `P04`, [evidence 2](input/sources/dispatch-policy.md) at `P03`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [proof 0: Audit.cApproval](models/Audit.lean), [proof 1: Audit.cDelay](models/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: Small finite source-linked model checks arithmetic, rule applications or a precisely limited auxiliary target; statements of unavailable events remain unconstrained.

- Proof 0 source-to-target correspondence: With final L-02 approval 16 and release 12, neither P-02 nor P-03 is satisfied; this excludes in particular the claimed exception compliance.
- Proof 1 source-to-target correspondence: The source dates differ by four integer days, directly checking the report arithmetic premise.

Declared bounded support search: Read every paragraph and table in all five supplied source documents, including cited passages and counterevidence.

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

C release 12 and approval 16 have a four-day gap. C fails the exception upper bound and also fails ordinary prior approval. Its route, release-window and declaration checks do not repair the failed approval deadline.

Search limits: No external evidence, unavailable reliability annex, missing 36 population records, or unprovided rating rubric was inspected.

### Rules

- The exception permits approval at most three days after release; no other route beyond ordinary or exception applies.

### Assumptions

- The supplied synthetic records are faithfully transcribed; source authenticity is outside this audit.

### Reasoning

- C release 12 and approval 16 have a four-day gap.
- C fails the exception upper bound and also fails ordinary prior approval. Its route, release-window and declaration checks do not repair the failed approval deadline.

### Limits

- The result is scoped to the supplied synthetic packet and declared policy.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.cApproval` in module `Audit` (refutes): `¬ Audit.compliant Audit.c`.
  [Model](models/Audit.lean) · [Executed check](checks/Target020.lean) · [Actual proof log](logs/target-020.log)

- `Audit.cDelay` in module `Audit` (auxiliary): `Audit.c.approved - Audit.c.released = 4`.
  [Model](models/Audit.lean) · [Executed check](checks/Target021.lean) · [Actual proof log](logs/target-021.log)

### Recommendation

State that C is noncompliant at cutoff: approval was four days after release.

## F11-05

### Exact report claim

`input/report.md#P07`

> B is eligible for settlement at cutoff.

### Verification question

Is B eligible under all three P-04 conditions, and is PASS alone sufficient?

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P05`

> [L-03] Checksum PASS means that the byte checksum of the dispatched package matched the approved package checksum. This field describes package integrity only. It does not attest to approval timing, delivery acceptance, future reliability, or eligibility for settlement.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P03`

> [P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P05`

> [P-04] A dispatch is eligible for settlement if and only if it has compliant approval under P-02 or P-03, its recorded checksum result is PASS, and its destination appears in the supplied destination list DL-7. These are three separate necessary conditions; together they are sufficient. Delivery acceptance is not a settlement condition.

- [input/sources/destination-list.md](input/sources/destination-list.md) — `P02`

> [D-01] DL-7 is the destination list referenced by DP-7 P-04. It was effective throughout campaign days 1–20. Its complete membership is North and South. East is not a member. No amendments apply during this interval.


### F11-05: criteria and report argument audit

Criteria origin: **inferred**. Scope: Exactly dispatches A, B, C and D through end of campaign day 20; integer campaign days and euro cents under DP-7 and DL-7.

Is B eligible under all three P-04 conditions, and is PASS alone sufficient?

- Decision criterion: Eligibility is exactly compliant approval AND PASS checksum AND destination in DL-7.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **invalid**.

Report premise at `P07`:

> its checksum is PASS

Assessment: **verified**. L-02 records B PASS.

[evidence 0](input/sources/dispatch-ledger.md) at `P04`, [evidence 1](input/sources/dispatch-ledger.md) at `P05`, [evidence 2](input/sources/dispatch-policy.md) at `P03`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`, [proof 0: Audit.bEligible](models/Audit.lean), [proof 1: Audit.passInsufficient](models/Audit.lean)

Report inference at `P07`:

> a PASS checksum alone is sufficient for settlement eligibility.

Assessment: **contradicted**. P-04 explicitly requires three separate conditions; D witnesses failure of this inference.

[evidence 0](input/sources/dispatch-ledger.md) at `P04`, [evidence 1](input/sources/dispatch-ledger.md) at `P05`, [evidence 2](input/sources/dispatch-policy.md) at `P03`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`, [proof 0: Audit.bEligible](models/Audit.lean), [proof 1: Audit.passInsufficient](models/Audit.lean)

Report citation at `P07`:

> dispatch-ledger.md L-02–L-03; dispatch-policy.md P-04.

Assessment: **verified**. The named supplied passages exist and are reproduced in evidence; their relevance and inferential limits are assessed separately below.

[evidence 0](input/sources/dispatch-ledger.md) at `P04`, [evidence 1](input/sources/dispatch-ledger.md) at `P05`, [evidence 2](input/sources/dispatch-policy.md) at `P03`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`, [proof 0: Audit.bEligible](models/Audit.lean), [proof 1: Audit.passInsufficient](models/Audit.lean)

Independent audit reasoning:

- B satisfies the P-03 exception, has PASS, and South belongs to DL-7; independent evidence establishes eligibility.
- The author states only PASS is sufficient. D is an in-cohort counterexample: PASS and compliant ordinary approval, but destination East is excluded.
- The conclusion is supported while its justification is invalid.

[evidence 0](input/sources/dispatch-ledger.md) at `P04`, [evidence 1](input/sources/dispatch-ledger.md) at `P05`, [evidence 2](input/sources/dispatch-policy.md) at `P03`, [evidence 3](input/sources/dispatch-policy.md) at `P04`, [evidence 4](input/sources/dispatch-policy.md) at `P05`, [evidence 5](input/sources/destination-list.md) at `P02`, [proof 0: Audit.bEligible](models/Audit.lean), [proof 1: Audit.passInsufficient](models/Audit.lean)

Audited claim dependencies: F11-03

Formalization rationale: Small finite source-linked model checks arithmetic, rule applications or a precisely limited auxiliary target; statements of unavailable events remain unconstrained.

- Proof 0 source-to-target correspondence: P-04 is encoded as a conjunction; B approval, checksum and South membership are independently verified from L-02, P-03 and D-01.
- Proof 1 source-to-target correspondence: D is an actual reviewed dispatch with PASS and excluded East destination, refuting PASS-implies-eligible without refuting B eligibility.

Declared bounded support search: Read every paragraph and table in all five supplied source documents, including cited passages and counterevidence.

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

B satisfies the P-03 exception, has PASS, and South belongs to DL-7; independent evidence establishes eligibility. The author states only PASS is sufficient. D is an in-cohort counterexample: PASS and compliant ordinary approval, but destination East is excluded. The conclusion is supported while its justification is invalid.

Search limits: No external evidence, unavailable reliability annex, missing 36 population records, or unprovided rating rubric was inspected.

### Rules

- Eligibility is exactly compliant approval AND PASS checksum AND destination in DL-7.

### Assumptions

- The supplied synthetic records are faithfully transcribed; source authenticity is outside this audit.

### Reasoning

- B satisfies the P-03 exception, has PASS, and South belongs to DL-7; independent evidence establishes eligibility.
- The author states only PASS is sufficient. D is an in-cohort counterexample: PASS and compliant ordinary approval, but destination East is excluded.
- The conclusion is supported while its justification is invalid.

### Limits

- The result is scoped to the supplied synthetic packet and declared policy.

### Result

Semantic state: **supported**; argument status: **invalid_inference**; formal status: **proved**.

### Formal evidence

- `Audit.bEligible` in module `Audit` (supports): `Audit.eligible Audit.b`.
  [Model](models/Audit.lean) · [Executed check](checks/Target022.lean) · [Actual proof log](logs/target-022.log)

- `Audit.passInsufficient` in module `Audit` (auxiliary): `Audit.d ∈ Audit.cohort ∧ Audit.d.passed = true ∧ ¬ Audit.eligible Audit.d`.
  [Model](models/Audit.lean) · [Executed check](checks/Target023.lean) · [Actual proof log](logs/target-023.log)

### Recommendation

Retain B eligibility but replace the checksum-only argument with all three conditions.

## F11-06

### Exact report claim

`input/report.md#P08`

> Ledger paragraph L-03 states that every reviewed dispatch received approval before release.

### Verification question

Does L-03 contain the attributed assertion that all four approvals preceded release?

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P05`

> [L-03] Checksum PASS means that the byte checksum of the dispatched package matched the approved package checksum. This field describes package integrity only. It does not attest to approval timing, delivery acceptance, future reliability, or eligibility for settlement.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P03`

> [P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.


### F11-06: criteria and report argument audit

Criteria origin: **inferred**. Scope: Exactly dispatches A, B, C and D through end of campaign day 20; integer campaign days and euro cents under DP-7 and DL-7.

Does L-03 contain the attributed assertion that all four approvals preceded release?

- Decision criterion: An attribution claim must match the cited passage; integrity checks cannot be rewritten as timing attestations.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **invalid**.

Report citation at `P08`:

> dispatch-ledger.md L-03.

Assessment: **contradicted**. L-03 explicitly disclaims approval-timing attestation; the attributed statement is absent and contrary to its stated scope.

[evidence 0](input/sources/dispatch-ledger.md) at `P05`, [evidence 1](input/sources/dispatch-ledger.md) at `P04`, [evidence 2](input/sources/dispatch-policy.md) at `P03`, [proof 0: Audit.notAllPrior](models/Audit.lean)

Independent audit reasoning:

- L-03 describes byte-checksum equality and explicitly says it does not attest approval timing.
- The attributed statement is therefore documentarily refuted. Separately, B and C approval days occur after release; the universal timing event claim would also be false.
- The formal counterexample concerns event timing only; it does not mechanize natural-language attribution.

[evidence 0](input/sources/dispatch-ledger.md) at `P05`, [evidence 1](input/sources/dispatch-ledger.md) at `P04`, [evidence 2](input/sources/dispatch-policy.md) at `P03`, [proof 0: Audit.notAllPrior](models/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: Small finite source-linked model checks arithmetic, rule applications or a precisely limited auxiliary target; statements of unavailable events remain unconstrained.

- Proof 0 source-to-target correspondence: The finite L-02 rows refute universal prior approval; this corroborates but does not itself prove the distinct textual claim about what L-03 says.

Declared bounded support search: Read every paragraph and table in all five supplied source documents, including cited passages and counterevidence.

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

L-03 describes byte-checksum equality and explicitly says it does not attest approval timing. The attributed statement is therefore documentarily refuted. Separately, B and C approval days occur after release; the universal timing event claim would also be false. The formal counterexample concerns event timing only; it does not mechanize natural-language attribution.

Search limits: No external evidence, unavailable reliability annex, missing 36 population records, or unprovided rating rubric was inspected.

### Rules

- An attribution claim must match the cited passage; integrity checks cannot be rewritten as timing attestations.

### Assumptions

- The supplied synthetic records are faithfully transcribed; source authenticity is outside this audit.

### Reasoning

- L-03 describes byte-checksum equality and explicitly says it does not attest approval timing.
- The attributed statement is therefore documentarily refuted. Separately, B and C approval days occur after release; the universal timing event claim would also be false.
- The formal counterexample concerns event timing only; it does not mechanize natural-language attribution.

### Limits

- The result is scoped to the supplied synthetic packet and declared policy.
- No Lean theorem claims to interpret natural-language statements or certify a textual attribution.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **auxiliary**.

### Formal evidence

- `Audit.notAllPrior` in module `Audit` (auxiliary): `¬ (∀ x ∈ Audit.cohort, Audit.ordinary x)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target024.lean) · [Actual proof log](logs/target-024.log)

### Recommendation

Replace the attribution with L-03 actual integrity-only scope.

## F11-07

### Exact report claim

`input/report.md#P09`

> B had zero reliability incidents during days 21–50.

### Verification question

Do supplied observations establish zero B reliability incidents on days 21–50?

### Source evidence

- [input/sources/packet-register.md](input/sources/packet-register.md) — `P02`

> [K-01] The supplied primary packet consists of dispatch-policy.md, dispatch-ledger.md, destination-list.md, delivery-records.md, and this packet-register.md. It contains records only through the end of campaign day 20. The reports under review are not primary evidence.

- [input/sources/packet-register.md](input/sources/packet-register.md) — `P03`

> [K-02] A proposed reliability annex covering days 21–50 is listed as “not supplied.” No observations, measurements, or findings from that period are included in this packet. The register does not state whether any reliability incident actually occurred during that later period.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P05`

> [L-03] Checksum PASS means that the byte checksum of the dispatched package matched the approved package checksum. This field describes package integrity only. It does not attest to approval timing, delivery acceptance, future reliability, or eligibility for settlement.


### F11-07: criteria and report argument audit

Criteria origin: **inferred**. Scope: B reliability during days 21–50, after the day-20 evidence cutoff.

Do supplied observations establish zero B reliability incidents on days 21–50?

- Decision criterion: No-event claims require observations or a justified completeness rule for the named future period; attachment inventory is not event history.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **insufficient**.

Report premise at `P09`:

> the listed reliability annex confirms the absence of incidents.

Assessment: **unsupported**. The annex is not supplied, so its contents cannot be checked. Listing it provides no observations and neither verifies nor refutes what that unseen annex might say.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`, [proof 0: Audit.laterNonentailment](models/Audit.lean)

Report inference at `P09`:

> the listed reliability annex confirms the absence of incidents.

Assessment: **unsupported**. Neither absence nor presence of incidents follows from K-02.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`, [proof 0: Audit.laterNonentailment](models/Audit.lean)

Report citation at `P09`:

> packet-register.md K-02.

Assessment: **contradicted**. The supplied K-02 does not contain the claimed confirmation: it lists the annex as not supplied and contains no later observations. This rejects the citation as confirmation by K-02; it does not refute any assertion about the unseen annex contents.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`, [proof 0: Audit.laterNonentailment](models/Audit.lean)

Independent audit reasoning:

- The primary packet stops at day 20; K-02 explicitly lists the reliability annex as not supplied and contains no later observations.
- No supplied passage supports either zero or nonzero later incidents. The claim about what the unseen annex confirms is unsupported because its contents are unavailable. K-02 itself contains no confirmation; the underlying zero-incident proposition remains undetermined.
- Two extensions preserve all supplied cohort facts while assigning zero or one later incident; neither is asserted as actual history.

[evidence 0](input/sources/packet-register.md) at `P02`, [evidence 1](input/sources/packet-register.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P05`, [proof 0: Audit.laterNonentailment](models/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: Small finite source-linked model checks arithmetic, rule applications or a precisely limited auxiliary target; statements of unavailable events remain unconstrained.

- Proof 0 source-to-target correspondence: K-02 imposes no constraint on later incident count. quiet and incident carry the same 36 unobserved dispatch positions and fixed cohort while differing only in 0 versus 1 later B incidents. The witness shows non-entailment in the declared projection, not actual incident occurrence.

Declared bounded support search: Read every paragraph and table in all five supplied source documents, including cited passages and counterevidence.

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

The primary packet stops at day 20; K-02 explicitly lists the reliability annex as not supplied and contains no later observations. No supplied passage supports either zero or nonzero later incidents. The claim about what the unseen annex confirms is unsupported because its contents are unavailable. K-02 itself contains no confirmation; the underlying zero-incident proposition remains undetermined. Two extensions preserve all supplied cohort facts while assigning zero or one later incident; neither is asserted as actual history.

Search limits: No external evidence, unavailable reliability annex, missing 36 population records, or unprovided rating rubric was inspected.

### Rules

- No-event claims require observations or a justified completeness rule for the named future period; attachment inventory is not event history.

### Assumptions

- The supplied synthetic records are faithfully transcribed; source authenticity is outside this audit.

### Reasoning

- The primary packet stops at day 20; K-02 explicitly lists the reliability annex as not supplied and contains no later observations.
- No supplied passage supports either zero or nonzero later incidents. The claim about what the unseen annex confirms is unsupported because its contents are unavailable. K-02 itself contains no confirmation; the underlying zero-incident proposition remains undetermined.
- Two extensions preserve all supplied cohort facts while assigning zero or one later incident; neither is asserted as actual history.

### Limits

- The result is scoped to the supplied synthetic packet and declared policy.
- A zero/one model witness is a logical extension, not an observation.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **auxiliary**.

### Formal evidence

- `Audit.laterNonentailment` in module `Audit` (auxiliary): `Audit.compatible Audit.quiet ∧ Audit.compatible Audit.incident ∧ Audit.quiet.laterIncidents = 0 ∧ Audit.incident.laterIncidents ≠ 0`.
  [Model](models/Audit.lean) · [Executed check](checks/Target025.lean) · [Actual proof log](logs/target-025.log)

### Recommendation

Mark the later incident count unresolved and obtain the actual days 21–50 annex.

## F11-08

### Exact report claim

`input/report.md#P10`

> The cohort is operationally robust.

### Verification question

Is there an applicable definition permitting an operationally robust rating?

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P05`

> [L-03] Checksum PASS means that the byte checksum of the dispatched package matched the approved package checksum. This field describes package integrity only. It does not attest to approval timing, delivery acceptance, future reliability, or eligibility for settlement.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P07`

> [P-06] DP-7 does not define a rating called “operationally robust” or a rule that checksum success implies compliant approval. No other rating standard is incorporated by reference.

- [input/sources/packet-register.md](input/sources/packet-register.md) — `P04`

> [K-03] The packet contains no dispatch-level records for the other 36 campaign dispatches and no statistical sampling or extrapolation method. No additional qualitative rating rubric is supplied.


### F11-08: criteria and report argument audit

Criteria origin: **inferred**. Scope: Exactly dispatches A, B, C and D through end of campaign day 20; integer campaign days and euro cents under DP-7 and DL-7.

Is there an applicable definition permitting an operationally robust rating?

- Decision criterion: A qualitative rating needs an explicit definition or adopted rubric; checksum success alone supplies only integrity evidence.

Missing definitions: Operationally robust: dimensions, thresholds, aggregation and treatment of missing evidence are undefined.

Alternatives: None declared.

Report justification outcome: **nonformal**.

Report premise at `P10`:

> every checksum passed.

Assessment: **verified**. All four L-02 checksum entries are PASS.

[evidence 0](input/sources/dispatch-ledger.md) at `P04`, [evidence 1](input/sources/dispatch-ledger.md) at `P05`, [evidence 2](input/sources/dispatch-policy.md) at `P07`, [evidence 3](input/sources/packet-register.md) at `P04`

Report inference at `P10`:

> every checksum passed.

Assessment: **nonformal**. No supplied rule connects this true premise to the undefined qualitative rating.

[evidence 0](input/sources/dispatch-ledger.md) at `P04`, [evidence 1](input/sources/dispatch-ledger.md) at `P05`, [evidence 2](input/sources/dispatch-policy.md) at `P07`, [evidence 3](input/sources/packet-register.md) at `P04`

Report citation at `P10`:

> dispatch-ledger.md L-02–L-03; dispatch-policy.md P-06.

Assessment: **unsupported**. The ledger supports checksum success, but P-06 expressly says the rating is undefined and no rating rule is incorporated.

[evidence 0](input/sources/dispatch-ledger.md) at `P04`, [evidence 1](input/sources/dispatch-ledger.md) at `P05`, [evidence 2](input/sources/dispatch-policy.md) at `P07`, [evidence 3](input/sources/packet-register.md) at `P04`

Independent audit reasoning:

- Every checksum is PASS.
- P-06 supplies no definition of operationally robust and no incorporated rating standard; K-03 confirms no further rubric.
- The rating cannot be evaluated as a well-defined predicate. This is an unresolved criterion and support gap, not proof that the cohort lacks operational robustness.

[evidence 0](input/sources/dispatch-ledger.md) at `P04`, [evidence 1](input/sources/dispatch-ledger.md) at `P05`, [evidence 2](input/sources/dispatch-policy.md) at `P07`, [evidence 3](input/sources/packet-register.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: No well-defined operational rating predicate or adopted rubric exists. A proof would require inventing a rule, so formalization is blocked.


Declared bounded support search: Read every paragraph and table in all five supplied source documents, including cited passages and counterevidence.

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

Every checksum is PASS. P-06 supplies no definition of operationally robust and no incorporated rating standard; K-03 confirms no further rubric. The rating cannot be evaluated as a well-defined predicate. This is an unresolved criterion and support gap, not proof that the cohort lacks operational robustness.

Search limits: No external evidence, unavailable reliability annex, missing 36 population records, or unprovided rating rubric was inspected.

### Rules

- A qualitative rating needs an explicit definition or adopted rubric; checksum success alone supplies only integrity evidence.

### Assumptions

- The supplied synthetic records are faithfully transcribed; source authenticity is outside this audit.

### Reasoning

- Every checksum is PASS.
- P-06 supplies no definition of operationally robust and no incorporated rating standard; K-03 confirms no further rubric.
- The rating cannot be evaluated as a well-defined predicate. This is an unresolved criterion and support gap, not proof that the cohort lacks operational robustness.

### Limits

- The result is scoped to the supplied synthetic packet and declared policy.

### Result

Semantic state: **undetermined**; argument status: **nonformal**; formal status: **blocked**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Request an operational rating definition, thresholds and evidence requirements before assigning the rating.

## F11-09

### Exact report claim

`input/report.md#P11`

> The supplied delivery evidence unambiguously establishes that B was accepted at the end of day 12.

### Verification question

Does the whole supplied packet unambiguously establish B physical acceptance at end of day 12?

### Source evidence

- [input/sources/delivery-records.md](input/sources/delivery-records.md) — `P02`

> [R-01] The signed receiving register records: “Dispatch B: ACCEPTED at the end of day 12.” This statement concerns physical delivery acceptance, not approval or settlement.

- [input/sources/delivery-records.md](input/sources/delivery-records.md) — `P03`

> [R-02] The signed incident register records: “Dispatch B: REJECTED at the end of day 12; acceptance did not occur at that time.” This concerns the same physical delivery event and instant as R-01.

- [input/sources/delivery-records.md](input/sources/delivery-records.md) — `P04`

> [R-03] Both records were signed on day 13 by their respective responsible officers. The packet contains no correction, withdrawal, reconciliation, precedence rule, or independent adjudication between R-01 and R-02. For this exercise the two registers have equal evidential standing. Their disagreement is preserved verbatim; neither register is designated authoritative over the other.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P05`

> [P-04] A dispatch is eligible for settlement if and only if it has compliant approval under P-02 or P-03, its recorded checksum result is PASS, and its destination appears in the supplied destination list DL-7. These are three separate necessary conditions; together they are sufficient. Delivery acceptance is not a settlement condition.


### F11-09: criteria and report argument audit

Criteria origin: **inferred**. Scope: Physical delivery of B at the end of day 12; separate from approval and settlement.

Does the whole supplied packet unambiguously establish B physical acceptance at end of day 12?

- Decision criterion: Preserve attributed testimony; compare the same event and instant, and apply only a supplied precedence or reconciliation rule.

Missing definitions: None declared.

Alternatives: If the claim were only that R-01 records acceptance, it would be supported; it instead says supplied evidence unambiguously establishes the event.

Report justification outcome: **disputed**.

Report premise at `P11`:

> the signed receiving register records acceptance.

Assessment: **verified**. R-01 does record acceptance, attributed to that register.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P05`, [proof 0: Audit.recordConflict](models/Audit.lean)

Report inference at `P11`:

> the signed receiving register records acceptance.

Assessment: **disputed**. R-02 at equal standing contradicts R-01, so the one cited record cannot establish unambiguous acceptance.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P05`, [proof 0: Audit.recordConflict](models/Audit.lean)

Report citation at `P11`:

> delivery-records.md R-01.

Assessment: **verified**. R-01 does contain an attributed acceptance statement; R-02 and R-03 prevent treating it as unambiguous.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P05`, [proof 0: Audit.recordConflict](models/Audit.lean)

Independent audit reasoning:

- R-01 records acceptance; R-02 records rejection and explicitly denies acceptance at the same instant.
- R-03 grants equal standing and supplies no correction or precedence. The report premise about R-01 is correct but does not settle the opposing record.
- The exact unambiguous-establishment claim is refuted by the unresolved contradiction. Actual acceptance remains undetermined/conflicting; neither register is promoted to world truth.

[evidence 0](input/sources/delivery-records.md) at `P02`, [evidence 1](input/sources/delivery-records.md) at `P03`, [evidence 2](input/sources/delivery-records.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P05`, [proof 0: Audit.recordConflict](models/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: Small finite source-linked model checks arithmetic, rule applications or a precisely limited auxiliary target; statements of unavailable events remain unconstrained.

- Proof 0 source-to-target correspondence: The two Bool values represent what R-01 and R-02 state, not two simultaneous event facts. The theorem preserves their opposite attributed polarities; documentary reasoning with R-03 refutes unambiguity.

Declared bounded support search: Read every paragraph and table in all five supplied source documents, including cited passages and counterevidence.

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

R-01 records acceptance; R-02 records rejection and explicitly denies acceptance at the same instant. R-03 grants equal standing and supplies no correction or precedence. The report premise about R-01 is correct but does not settle the opposing record. The exact unambiguous-establishment claim is refuted by the unresolved contradiction. Actual acceptance remains undetermined/conflicting; neither register is promoted to world truth.

Search limits: No external evidence, unavailable reliability annex, missing 36 population records, or unprovided rating rubric was inspected.

### Rules

- Preserve attributed testimony; compare the same event and instant, and apply only a supplied precedence or reconciliation rule.

### Assumptions

- The supplied synthetic records are faithfully transcribed; source authenticity is outside this audit.

### Reasoning

- R-01 records acceptance; R-02 records rejection and explicitly denies acceptance at the same instant.
- R-03 grants equal standing and supplies no correction or precedence. The report premise about R-01 is correct but does not settle the opposing record.
- The exact unambiguous-establishment claim is refuted by the unresolved contradiction. Actual acceptance remains undetermined/conflicting; neither register is promoted to world truth.

### Limits

- The result is scoped to the supplied synthetic packet and declared policy.
- The exact claim about unambiguity is refuted; the event proposition is not classified as false.

### Result

Semantic state: **refuted**; argument status: **disputed**; formal status: **auxiliary**.

### Formal evidence

- `Audit.recordConflict` in module `Audit` (auxiliary): `Audit.saysAccepted Audit.Record.receiving = true ∧ Audit.saysAccepted Audit.Record.incident = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target026.lean) · [Actual proof log](logs/target-026.log)

### Recommendation

State that acceptance is disputed and seek reconciliation or an adjudication.

## F11-10

### Exact report claim

`input/report.md#P12`

> Release on day 15 is within the temporary exception's release window.

### Verification question

Does day 15 belong to the inclusive release interval from day 10 through day 14?

### Source evidence

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P04`

> [P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.


### F11-10: criteria and report argument audit

Criteria origin: **inferred**. Scope: A release on day 15 under DP-7 temporary exception; no specific dispatch is required.

Does day 15 belong to the inclusive release interval from day 10 through day 14?

- Decision criterion: Temporary-exception release days must satisfy 10 ≤ day ≤ 14.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **invalid**.

Report citation at `P12`:

> dispatch-policy.md P-03.

Assessment: **verified**. The named supplied passages exist and are reproduced in evidence; their relevance and inferential limits are assessed separately below.

[evidence 0](input/sources/dispatch-policy.md) at `P02`, [evidence 1](input/sources/dispatch-policy.md) at `P04`, [proof 0: Audit.releaseWindow](models/Audit.lean)

Independent audit reasoning:

- The policy makes both endpoints inclusive.
- Day 15 exceeds upper endpoint 14, so the claimed interval membership is false.

[evidence 0](input/sources/dispatch-policy.md) at `P02`, [evidence 1](input/sources/dispatch-policy.md) at `P04`, [proof 0: Audit.releaseWindow](models/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: Small finite source-linked model checks arithmetic, rule applications or a precisely limited auxiliary target; statements of unavailable events remain unconstrained.

- Proof 0 source-to-target correspondence: Audit.window uses exactly the integer bounds 10 and 14 from P-03; the negative target excludes day 15.

Declared bounded support search: Read every paragraph and table in all five supplied source documents, including cited passages and counterevidence.

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

The policy makes both endpoints inclusive. Day 15 exceeds upper endpoint 14, so the claimed interval membership is false.

Search limits: No external evidence, unavailable reliability annex, missing 36 population records, or unprovided rating rubric was inspected.

### Rules

- Temporary-exception release days must satisfy 10 ≤ day ≤ 14.

### Assumptions

- The supplied synthetic records are faithfully transcribed; source authenticity is outside this audit.

### Reasoning

- The policy makes both endpoints inclusive.
- Day 15 exceeds upper endpoint 14, so the claimed interval membership is false.

### Limits

- The result is scoped to the supplied synthetic packet and declared policy.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.releaseWindow` in module `Audit` (refutes): `¬ Audit.window 15`.
  [Model](models/Audit.lean) · [Executed check](checks/Target027.lean) · [Actual proof log](logs/target-027.log)

### Recommendation

Correct the exception release window to days 10–14 inclusive.

## F11-11

### Exact report claim

`input/report.md#P13`

> The reviewed cohort's eligible settlement amount is 39000 euro cents.

### Verification question

Does the P-04 eligible subset of A–D have amount 39000 cents?

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


### F11-11: criteria and report argument audit

Criteria origin: **inferred**. Scope: Exactly dispatches A, B, C and D through end of campaign day 20; integer campaign days and euro cents under DP-7 and DL-7.

Does the P-04 eligible subset of A–D have amount 39000 cents?

- Decision criterion: Select precisely cohort members satisfying approval, PASS and DL-7 membership, then sum their amounts.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **invalid**.

Report premise at `P13`:

> A, B, and C are eligible

Assessment: **contradicted**. A and B satisfy P-04, but C approval delay is four days.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P03`, [evidence 4](input/sources/dispatch-policy.md) at `P04`, [evidence 5](input/sources/dispatch-policy.md) at `P05`, [evidence 6](input/sources/dispatch-policy.md) at `P06`, [evidence 7](input/sources/destination-list.md) at `P02`, [proof 0: Audit.settlement](models/Audit.lean), [proof 1: Audit.eligibleMembers](models/Audit.lean)

Report inference at `P13`:

> so add their amounts.

Assessment: **unsupported**. Summation is correct only after correct eligibility selection; inclusion of C invalidates this sum as eligible amount.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P03`, [evidence 4](input/sources/dispatch-policy.md) at `P04`, [evidence 5](input/sources/dispatch-policy.md) at `P05`, [evidence 6](input/sources/dispatch-policy.md) at `P06`, [evidence 7](input/sources/destination-list.md) at `P02`, [proof 0: Audit.settlement](models/Audit.lean), [proof 1: Audit.eligibleMembers](models/Audit.lean)

Report citation at `P13`:

> dispatch-policy.md P-02–P-05; dispatch-ledger.md L-02; destination-list.md D-01.

Assessment: **verified**. The named supplied passages exist and are reproduced in evidence; their relevance and inferential limits are assessed separately below.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P03`, [evidence 4](input/sources/dispatch-policy.md) at `P04`, [evidence 5](input/sources/dispatch-policy.md) at `P05`, [evidence 6](input/sources/dispatch-policy.md) at `P06`, [evidence 7](input/sources/destination-list.md) at `P02`, [proof 0: Audit.settlement](models/Audit.lean), [proof 1: Audit.eligibleMembers](models/Audit.lean)

Independent audit reasoning:

- A has prior approval, PASS and North; B has exception approval, PASS and South. Both are eligible.
- C fails approval timing; D has destination East outside DL-7. They are ineligible.
- Only A and B contribute: 12000 + 18000 = 30000, not 39000. The author incorrectly included C; summing A+B+C is arithmetically 39000 but the membership premise fails.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P03`, [evidence 2](input/sources/dispatch-ledger.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P03`, [evidence 4](input/sources/dispatch-policy.md) at `P04`, [evidence 5](input/sources/dispatch-policy.md) at `P05`, [evidence 6](input/sources/dispatch-policy.md) at `P06`, [evidence 7](input/sources/destination-list.md) at `P02`, [proof 0: Audit.settlement](models/Audit.lean), [proof 1: Audit.eligibleMembers](models/Audit.lean)

Audited claim dependencies: F11-04, F11-05

Formalization rationale: Small finite source-linked model checks arithmetic, rule applications or a precisely limited auxiliary target; statements of unavailable events remain unconstrained.

- Proof 0 source-to-target correspondence: eligibleTotal filters the exact A–D list with the P-04 conjunction and sums Int amounts; source finality and exhaustive approval routes justify excluding C and D.
- Proof 1 source-to-target correspondence: Individual membership checks map each L-02 row through P-02/P-03, P-04 and D-01; C deadline failure and D destination exclusion explain the correction.

Declared bounded support search: Read every paragraph and table in all five supplied source documents, including cited passages and counterevidence.

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

A has prior approval, PASS and North; B has exception approval, PASS and South. Both are eligible. C fails approval timing; D has destination East outside DL-7. They are ineligible. Only A and B contribute: 12000 + 18000 = 30000, not 39000. The author incorrectly included C; summing A+B+C is arithmetically 39000 but the membership premise fails.

Search limits: No external evidence, unavailable reliability annex, missing 36 population records, or unprovided rating rubric was inspected.

### Rules

- Select precisely cohort members satisfying approval, PASS and DL-7 membership, then sum their amounts.

### Assumptions

- The supplied synthetic records are faithfully transcribed; source authenticity is outside this audit.

### Reasoning

- A has prior approval, PASS and North; B has exception approval, PASS and South. Both are eligible.
- C fails approval timing; D has destination East outside DL-7. They are ineligible.
- Only A and B contribute: 12000 + 18000 = 30000, not 39000. The author incorrectly included C; summing A+B+C is arithmetically 39000 but the membership premise fails.

### Limits

- The result is scoped to the supplied synthetic packet and declared policy.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.settlement` in module `Audit` (refutes): `Audit.eligibleTotal = 30000 ∧ Audit.eligibleTotal ≠ 39000`.
  [Model](models/Audit.lean) · [Executed check](checks/Target028.lean) · [Actual proof log](logs/target-028.log)

- `Audit.eligibleMembers` in module `Audit` (auxiliary): `Audit.eligible Audit.a ∧ Audit.eligible Audit.b ∧ ¬ Audit.eligible Audit.c ∧ ¬ Audit.eligible Audit.d`.
  [Model](models/Audit.lean) · [Executed check](checks/Target029.lean) · [Actual proof log](logs/target-029.log)

### Recommendation

Correct eligible settlement amount to 30000 cents and eligible members to A and B.

## F11-12

### Exact report claim

`input/report.md#P14`

> The total amount of all 40 campaign dispatches is 50000 euro cents.

### Verification question

Do four supplied rows establish the aggregate amount of all 40 dispatches?

### Source evidence

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P02`

> [L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

- [input/sources/dispatch-ledger.md](input/sources/dispatch-ledger.md) — `P04`

> | Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
> | --- | ---: | --- | ---: | --- | ---: | --- | --- |
> | A | 12000 | R1 | 5 | None | 4 | PASS | North |
> | B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
> | C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
> | D | 11000 | R1 | 15 | None | 14 | PASS | East |

- [input/sources/packet-register.md](input/sources/packet-register.md) — `P04`

> [K-03] The packet contains no dispatch-level records for the other 36 campaign dispatches and no statistical sampling or extrapolation method. No additional qualitative rating rubric is supplied.

- [input/sources/dispatch-policy.md](input/sources/dispatch-policy.md) — `P02`

> [P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.


### F11-12: criteria and report argument audit

Criteria origin: **inferred**. Scope: All 40 campaign dispatches; unlike F11-01 this expressly extends beyond reviewed cohort.

Do four supplied rows establish the aggregate amount of all 40 dispatches?

- Decision criterion: A population aggregate needs all population amounts or a valid supplied derivation; four cohort rows establish only their own sum.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **insufficient**.

Report premise at `P14`:

> the four ledger rows sum to that amount.

Assessment: **verified**. The cohort sum is exactly 50000.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P04`, [evidence 2](input/sources/packet-register.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [proof 0: Audit.populationNonentailment](models/Audit.lean)

Report inference at `P14`:

> the four ledger rows sum to that amount.

Assessment: **unsupported**. A correct four-row aggregate cannot establish a forty-dispatch total when 36 amounts are unavailable.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P04`, [evidence 2](input/sources/packet-register.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [proof 0: Audit.populationNonentailment](models/Audit.lean)

Report citation at `P14`:

> dispatch-ledger.md L-01–L-02; packet-register.md K-03.

Assessment: **unsupported**. L-01 limits the ledger to four dispatches and K-03 says the other 36 records are absent; these citations cannot supply a population total.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P04`, [evidence 2](input/sources/packet-register.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [proof 0: Audit.populationNonentailment](models/Audit.lean)

Independent audit reasoning:

- L-01 identifies 40 campaign dispatches but gives records for exactly four; those four sum to 50000.
- K-03 supplies no amounts for the remaining 36 and no extrapolation method. Neither the claimed full total nor its negation is established.
- Two extensions contain exactly 36 missing amounts, all zero versus one amount equal to one cent and 35 zero; both preserve the supplied packet while giving different population totals. No rule in the packet requires strictly positive amounts.

[evidence 0](input/sources/dispatch-ledger.md) at `P02`, [evidence 1](input/sources/dispatch-ledger.md) at `P04`, [evidence 2](input/sources/packet-register.md) at `P04`, [evidence 3](input/sources/dispatch-policy.md) at `P02`, [proof 0: Audit.populationNonentailment](models/Audit.lean)

Audited claim dependencies: F11-01

Formalization rationale: Small finite source-linked model checks arithmetic, rule applications or a precisely limited auxiliary target; statements of unavailable events remain unconstrained.

- Proof 0 source-to-target correspondence: L-01 fixes 36 additional dispatches and P-01 integer-cent units, but supplies no amount constraints. Both lists have length 36; zero versus one extra cent yields 50000 versus 50001. These logical extensions prove non-entailment of either exact population conclusion in the declared source projection.

Declared bounded support search: Read every paragraph and table in all five supplied source documents, including cited passages and counterevidence.

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

L-01 identifies 40 campaign dispatches but gives records for exactly four; those four sum to 50000. K-03 supplies no amounts for the remaining 36 and no extrapolation method. Neither the claimed full total nor its negation is established. Two extensions contain exactly 36 missing amounts, all zero versus one amount equal to one cent and 35 zero; both preserve the supplied packet while giving different population totals. No rule in the packet requires strictly positive amounts.

Search limits: No external evidence, unavailable reliability annex, missing 36 population records, or unprovided rating rubric was inspected.

### Rules

- A population aggregate needs all population amounts or a valid supplied derivation; four cohort rows establish only their own sum.

### Assumptions

- The supplied synthetic records are faithfully transcribed; source authenticity is outside this audit.

### Reasoning

- L-01 identifies 40 campaign dispatches but gives records for exactly four; those four sum to 50000.
- K-03 supplies no amounts for the remaining 36 and no extrapolation method. Neither the claimed full total nor its negation is established.
- Two extensions contain exactly 36 missing amounts, all zero versus one amount equal to one cent and 35 zero; both preserve the supplied packet while giving different population totals. No rule in the packet requires strictly positive amounts.

### Limits

- The result is scoped to the supplied synthetic packet and declared policy.
- The witness does not assume missing amounts are actually zero or one cent.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **auxiliary**.

### Formal evidence

- `Audit.populationNonentailment` in module `Audit` (auxiliary): `Audit.compatible Audit.quiet ∧ Audit.compatible Audit.extraAmount ∧ Audit.populationTotal Audit.quiet = 50000 ∧ Audit.populationTotal Audit.extraAmount ≠ 50000`.
  [Model](models/Audit.lean) · [Executed check](checks/Target030.lean) · [Actual proof log](logs/target-030.log)

### Recommendation

State only the 50000-cent cohort total and obtain the other 36 dispatch amounts.
