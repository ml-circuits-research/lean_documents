# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

## Registered claim coverage

Coverage: **complete_registration**; 11 reviewed anchors; 10 audited and 0 deferred claims.

Registration reconciles declared claims and reviewed report anchors; it does not establish semantic completeness, faithful decomposition, or that declared searches were actually performed.

- `P01`: non_claim — Document title only.
- `P02`: claims — One substantive conclusion; its supplied premises, citations and inference are audited separately below.
- `P03`: claims — One substantive conclusion; its supplied premises, citations and inference are audited separately below.
- `P04`: claims — One substantive conclusion; its supplied premises, citations and inference are audited separately below.
- `P05`: claims — One substantive conclusion; its supplied premises, citations and inference are audited separately below.
- `P06`: claims — One substantive conclusion; its supplied premises, citations and inference are audited separately below.
- `P07`: claims — One substantive conclusion; its supplied premises, citations and inference are audited separately below.
- `P08`: claims — One substantive conclusion; its supplied premises, citations and inference are audited separately below.
- `P09`: claims — One substantive conclusion; its supplied premises, citations and inference are audited separately below.
- `P10`: claims — One substantive conclusion; its supplied premises, citations and inference are audited separately below.
- `P11`: claims — One substantive conclusion; its supplied premises, citations and inference are audited separately below.
[Semantic correspondence review](semantic-review.md)

## C16-01

### Exact report claim

`input/report.md#P02`

> The union of pauses A and B is 30 minutes.

### Verification question

How many distinct minutes lie in A or B within the actual gross window?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P02`

> [P1] This synthetic protocol governs incident H16 and its November 2026 invoice. All times are integer minute offsets from 09:00 UTC on 2 November 2026. Pause intervals are half-open [start,end); a minute belongs to the interval exactly when start <= minute < end. The gross incident window is [0,180). Count each paused minute once using the union of approved in-scope intervals, clipped to the gross window. An interval of zero length contributes zero. Intervals marked other-case never pause H16.

- [input/sources/operations.md](input/sources/operations.md) — `P02`

> [O1] Incident H16 opened at minute 0 and restoration occurred at minute 180. Approved H16 pause A is [20,40); approved H16 pause B is [30,50). Both records refer to the same stopped-service clock and overlap.


### C16-01: criteria and report argument audit

Criteria origin: **inferred**. Scope: H16 actual and explicitly identified extension scenario, invoice N16, separate CN16, and the explicitly scoped August–October historical prerequisite.

How many distinct minutes lie in A or B within the actual gross window?

- Decision criterion: A covers minutes 20 through 39 and B covers 30 through 49. Their overlap is 30 through 39, so their union is 20 through 49: 30 minutes. Adding 20 and 20 double-counts ten minutes.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P02`:

> Their common ten minutes are counted once under P1.

Assessment: **verified**. A covers minutes 20 through 39 and B covers 30 through 49. Their overlap is 30 through 39, so their union is 20 through 49: 30 minutes. Adding 20 and 20 double-counts ten minutes.

[evidence 0](input/sources/policy.md) at `P02`, [evidence 1](input/sources/operations.md) at `P02`, [proof 0: Settlement.overlap30](models/IntervalModel.lean)

Report citation at `P02`:

> P1

Assessment: **verified**. The cited passage exists and its content matches the attributed bounded statement.

[evidence 0](input/sources/policy.md) at `P02`

Independent audit reasoning:

- A covers minutes 20 through 39 and B covers 30 through 49. Their overlap is 30 through 39, so their union is 20 through 49: 30 minutes. Adding 20 and 20 double-counts ten minutes.

[evidence 0](input/sources/policy.md) at `P02`, [evidence 1](input/sources/operations.md) at `P02`, [proof 0: Settlement.overlap30](models/IntervalModel.lean)

Audited claim dependencies: None declared.

Formalization rationale: Use finite interval union and exact signed integer rounding, with direct targets and explicitly auxiliary checks.

- Proof 0 source-to-target correspondence: A covers minutes 20 through 39 and B covers 30 through 49. Their overlap is 30 through 39, so their union is 20 through 49: 30 minutes. Adding 20 and 20 double-counts ten minutes. The model transcribes the cited integer values and the explicit policy, assuming faithful source transcription and protocol applicability. It does not authenticate records.

Declared bounded support search: Read the complete three-file source corpus and this report paragraph, including policy, full pause inventory, invoice and explicit historical limitations.

Queries: H16; pause; SLA; round; historical; reasonable

- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P01`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P02`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P01`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P02`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P01`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P02`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P03`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P05`.

A covers minutes 20 through 39 and B covers 30 through 49. Their overlap is 30 through 39, so their union is 20 through 49: 30 minutes. Adding 20 and 20 double-counts ten minutes.

Search limits: No external sources, missing historical records, or alternate report were used as evidence.

### Rules

- [P1] This synthetic protocol governs incident H16 and its November 2026 invoice. All times are integer minute offsets from 09:00 UTC on 2 November 2026. Pause intervals are half-open [start,end); a minute belongs to the interval exactly when start <= minute < end. The gross incident window is [0,180). Count each paused minute once using the union of approved in-scope intervals, clipped to the gross window. An interval of zero length contributes zero. Intervals marked other-case never pause H16.

### Assumptions

- The synthetic source transcriptions are faithful and SR-16 applies to H16; no external facts are added.

### Reasoning

- A covers minutes 20 through 39 and B covers 30 through 49. Their overlap is 30 through 39, so their union is 20 through 49: 30 minutes. Adding 20 and 20 double-counts ten minutes.

### Limits

- The supplied corpus is the entire search boundary. The model does not authenticate sources or establish missing historical events. Partial-window clipping is not independently exercised by this dossier.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Settlement.overlap30` in module `IntervalModel` (supports): `Settlement.unionMinutes 180 [Settlement.a, Settlement.b] = 30`.
  [Model](models/IntervalModel.lean) · [Executed check](checks/Target020.lean) · [Actual proof log](logs/target-020.log)

### Recommendation

Use a 30-minute union for A and B.

## C16-02

### Exact report claim

`input/report.md#P03`

> Adding touching pause C gives a 40-minute union.

### Verification question

How many distinct minutes lie in A, B or touching C within the actual gross window?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P02`

> [P1] This synthetic protocol governs incident H16 and its November 2026 invoice. All times are integer minute offsets from 09:00 UTC on 2 November 2026. Pause intervals are half-open [start,end); a minute belongs to the interval exactly when start <= minute < end. The gross incident window is [0,180). Count each paused minute once using the union of approved in-scope intervals, clipped to the gross window. An interval of zero length contributes zero. Intervals marked other-case never pause H16.

- [input/sources/operations.md](input/sources/operations.md) — `P02`

> [O1] Incident H16 opened at minute 0 and restoration occurred at minute 180. Approved H16 pause A is [20,40); approved H16 pause B is [30,50). Both records refer to the same stopped-service clock and overlap.

- [input/sources/operations.md](input/sources/operations.md) — `P03`

> [O2] Approved H16 pause C is [50,60). Approved H16 administrative marker Z is [60,60). Approved pause X is [70,80) but is marked other-case H17. Approved H16 pause Y is [190,200), wholly outside the actual incident window. A, B, C, Z, X and Y are the complete pause inventory for H16's actual decision.


### C16-02: criteria and report argument audit

Criteria origin: **inferred**. Scope: H16 actual and explicitly identified extension scenario, invoice N16, separate CN16, and the explicitly scoped August–October historical prerequisite.

How many distinct minutes lie in A, B or touching C within the actual gross window?

- Decision criterion: A and B already cover [20,50). C covers [50,60). Their touching boundary adds no minute beyond the enumerated 20 through 59, giving 40 minutes.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P03`:

> Half-open boundaries join [20,50) and [50,60) without a duplicate or extra minute.

Assessment: **verified**. A and B already cover [20,50). C covers [50,60). Their touching boundary adds no minute beyond the enumerated 20 through 59, giving 40 minutes.

[evidence 0](input/sources/policy.md) at `P02`, [evidence 1](input/sources/operations.md) at `P02`, [evidence 2](input/sources/operations.md) at `P03`, [proof 0: Settlement.touching40](models/IntervalModel.lean), [proof 1: Settlement.touching_union](models/IntervalModel.lean)

Independent audit reasoning:

- A and B already cover [20,50). C covers [50,60). Their touching boundary adds no minute beyond the enumerated 20 through 59, giving 40 minutes.

[evidence 0](input/sources/policy.md) at `P02`, [evidence 1](input/sources/operations.md) at `P02`, [evidence 2](input/sources/operations.md) at `P03`, [proof 0: Settlement.touching40](models/IntervalModel.lean), [proof 1: Settlement.touching_union](models/IntervalModel.lean)

Audited claim dependencies: None declared.

Formalization rationale: Use finite interval union and exact signed integer rounding, with direct targets and explicitly auxiliary checks.

- Proof 0 source-to-target correspondence: A and B already cover [20,50). C covers [50,60). Their touching boundary adds no minute beyond the enumerated 20 through 59, giving 40 minutes. The model transcribes the cited integer values and the explicit policy, assuming faithful source transcription and protocol applicability. It does not authenticate records.
- Proof 1 source-to-target correspondence: This symbolic half-open membership equivalence applies to ordered endpoints, independently of incident values. It explains why touching intervals do not add an extra boundary minute; it is auxiliary rather than a source authenticity result.

Declared bounded support search: Read the complete three-file source corpus and this report paragraph, including policy, full pause inventory, invoice and explicit historical limitations.

Queries: H16; pause; SLA; round; historical; reasonable

- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P01`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P02`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P01`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P02`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P01`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P02`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P03`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P05`.

A and B already cover [20,50). C covers [50,60). Their touching boundary adds no minute beyond the enumerated 20 through 59, giving 40 minutes.

Search limits: No external sources, missing historical records, or alternate report were used as evidence.

### Rules

- [P1] This synthetic protocol governs incident H16 and its November 2026 invoice. All times are integer minute offsets from 09:00 UTC on 2 November 2026. Pause intervals are half-open [start,end); a minute belongs to the interval exactly when start <= minute < end. The gross incident window is [0,180). Count each paused minute once using the union of approved in-scope intervals, clipped to the gross window. An interval of zero length contributes zero. Intervals marked other-case never pause H16.

### Assumptions

- The synthetic source transcriptions are faithful and SR-16 applies to H16; no external facts are added.

### Reasoning

- A and B already cover [20,50). C covers [50,60). Their touching boundary adds no minute beyond the enumerated 20 through 59, giving 40 minutes.

### Limits

- The supplied corpus is the entire search boundary. The model does not authenticate sources or establish missing historical events. Partial-window clipping is not independently exercised by this dossier.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Settlement.touching40` in module `IntervalModel` (supports): `Settlement.unionMinutes 180 [Settlement.a, Settlement.b, Settlement.c] = 40`.
  [Model](models/IntervalModel.lean) · [Executed check](checks/Target021.lean) · [Actual proof log](logs/target-021.log)

- `Settlement.touching_union` in module `IntervalModel` (auxiliary): `∀ (lo mid hi minute : Nat), lo ≤ mid → mid ≤ hi → (((lo ≤ minute ∧ minute < mid) ∨ (mid ≤ minute ∧ minute < hi)) ↔ (lo ≤ minute ∧ minute < hi))`.
  [Model](models/IntervalModel.lean) · [Executed check](checks/Target022.lean) · [Actual proof log](logs/target-022.log)

### Recommendation

Use a 40-minute union after adding C.

## C16-03

### Exact report claim

`input/report.md#P04`

> The actual H16 paused time remains 40 minutes after all six records are considered.

### Verification question

What is the union duration after zero-length, case-scope and window rules are applied to the complete actual inventory?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P02`

> [P1] This synthetic protocol governs incident H16 and its November 2026 invoice. All times are integer minute offsets from 09:00 UTC on 2 November 2026. Pause intervals are half-open [start,end); a minute belongs to the interval exactly when start <= minute < end. The gross incident window is [0,180). Count each paused minute once using the union of approved in-scope intervals, clipped to the gross window. An interval of zero length contributes zero. Intervals marked other-case never pause H16.

- [input/sources/operations.md](input/sources/operations.md) — `P02`

> [O1] Incident H16 opened at minute 0 and restoration occurred at minute 180. Approved H16 pause A is [20,40); approved H16 pause B is [30,50). Both records refer to the same stopped-service clock and overlap.

- [input/sources/operations.md](input/sources/operations.md) — `P03`

> [O2] Approved H16 pause C is [50,60). Approved H16 administrative marker Z is [60,60). Approved pause X is [70,80) but is marked other-case H17. Approved H16 pause Y is [190,200), wholly outside the actual incident window. A, B, C, Z, X and Y are the complete pause inventory for H16's actual decision.


### C16-03: criteria and report argument audit

Criteria origin: **inferred**. Scope: H16 actual and explicitly identified extension scenario, invoice N16, separate CN16, and the explicitly scoped August–October historical prerequisite.

What is the union duration after zero-length, case-scope and window rules are applied to the complete actual inventory?

- Decision criterion: The complete inventory covers forty actual-window minutes. Z=[60,60) contains no minute; X belongs to H17; Y=[190,200) has no member in [0,180). Neither a zero-length marker nor another case adds a minute.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P04`:

> Z has zero length, X is other-case, and Y lies outside the actual window.

Assessment: **verified**. The complete inventory covers forty actual-window minutes. Z=[60,60) contains no minute; X belongs to H17; Y=[190,200) has no member in [0,180). Neither a zero-length marker nor another case adds a minute.

[evidence 0](input/sources/policy.md) at `P02`, [evidence 1](input/sources/operations.md) at `P02`, [evidence 2](input/sources/operations.md) at `P03`, [proof 0: Settlement.actual40](models/IntervalModel.lean), [proof 1: Settlement.empty_interval](models/IntervalModel.lean)

Independent audit reasoning:

- The complete inventory covers forty actual-window minutes. Z=[60,60) contains no minute; X belongs to H17; Y=[190,200) has no member in [0,180). Neither a zero-length marker nor another case adds a minute.

[evidence 0](input/sources/policy.md) at `P02`, [evidence 1](input/sources/operations.md) at `P02`, [evidence 2](input/sources/operations.md) at `P03`, [proof 0: Settlement.actual40](models/IntervalModel.lean), [proof 1: Settlement.empty_interval](models/IntervalModel.lean)

Audited claim dependencies: None declared.

Formalization rationale: Use finite interval union and exact signed integer rounding, with direct targets and explicitly auxiliary checks.

- Proof 0 source-to-target correspondence: The complete inventory covers forty actual-window minutes. Z=[60,60) contains no minute; X belongs to H17; Y=[190,200) has no member in [0,180). Neither a zero-length marker nor another case adds a minute. The model transcribes the cited integer values and the explicit policy, assuming faithful source transcription and protocol applicability. It does not authenticate records.
- Proof 1 source-to-target correspondence: The symbolic target states no natural minute is both at least and below the same endpoint. P1 uses that half-open convention, so Z contributes zero. This does not establish other interval scopes.

Declared bounded support search: Read the complete three-file source corpus and this report paragraph, including policy, full pause inventory, invoice and explicit historical limitations.

Queries: H16; pause; SLA; round; historical; reasonable

- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P01`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P02`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P01`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P02`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P01`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P02`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P03`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P05`.

The complete inventory covers forty actual-window minutes. Z=[60,60) contains no minute; X belongs to H17; Y=[190,200) has no member in [0,180). Neither a zero-length marker nor another case adds a minute.

Search limits: No external sources, missing historical records, or alternate report were used as evidence.

### Rules

- [P1] This synthetic protocol governs incident H16 and its November 2026 invoice. All times are integer minute offsets from 09:00 UTC on 2 November 2026. Pause intervals are half-open [start,end); a minute belongs to the interval exactly when start <= minute < end. The gross incident window is [0,180). Count each paused minute once using the union of approved in-scope intervals, clipped to the gross window. An interval of zero length contributes zero. Intervals marked other-case never pause H16.

### Assumptions

- The synthetic source transcriptions are faithful and SR-16 applies to H16; no external facts are added.

### Reasoning

- The complete inventory covers forty actual-window minutes. Z=[60,60) contains no minute; X belongs to H17; Y=[190,200) has no member in [0,180). Neither a zero-length marker nor another case adds a minute.

### Limits

- The supplied corpus is the entire search boundary. The model does not authenticate sources or establish missing historical events. Partial-window clipping is not independently exercised by this dossier.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Settlement.actual40` in module `IntervalModel` (supports): `Settlement.unionMinutes Settlement.actualGross Settlement.inventory = 40`.
  [Model](models/IntervalModel.lean) · [Executed check](checks/Target023.lean) · [Actual proof log](logs/target-023.log)

- `Settlement.empty_interval` in module `IntervalModel` (auxiliary): `∀ (point minute : Nat), ¬ (point ≤ minute ∧ minute < point)`.
  [Model](models/IntervalModel.lean) · [Executed check](checks/Target024.lean) · [Actual proof log](logs/target-024.log)

### Recommendation

Retain 40 actual paused minutes and exclude Z, X and Y under the separate rules.

## C16-04

### Exact report claim

`input/report.md#P05`

> H16 meets the inclusive SLA.

### Verification question

Does actual gross duration minus its paused union satisfy the inclusive 140-minute SLA?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P02`

> [P1] This synthetic protocol governs incident H16 and its November 2026 invoice. All times are integer minute offsets from 09:00 UTC on 2 November 2026. Pause intervals are half-open [start,end); a minute belongs to the interval exactly when start <= minute < end. The gross incident window is [0,180). Count each paused minute once using the union of approved in-scope intervals, clipped to the gross window. An interval of zero length contributes zero. Intervals marked other-case never pause H16.

- [input/sources/policy.md](input/sources/policy.md) — `P03`

> [P2] The SLA limit is 140 chargeable minutes inclusive. Chargeable time is gross elapsed minutes minus distinct approved in-scope paused minutes. An incident meets the SLA exactly when chargeable time <= 140. For the explicit extension scenario only, restoration occurs at minute 181 and all listed pause intervals and scope flags remain unchanged. No automatic tolerance minute applies.

- [input/sources/operations.md](input/sources/operations.md) — `P02`

> [O1] Incident H16 opened at minute 0 and restoration occurred at minute 180. Approved H16 pause A is [20,40); approved H16 pause B is [30,50). Both records refer to the same stopped-service clock and overlap.

- [input/sources/operations.md](input/sources/operations.md) — `P03`

> [O2] Approved H16 pause C is [50,60). Approved H16 administrative marker Z is [60,60). Approved pause X is [70,80) but is marked other-case H17. Approved H16 pause Y is [190,200), wholly outside the actual incident window. A, B, C, Z, X and Y are the complete pause inventory for H16's actual decision.


### C16-04: criteria and report argument audit

Criteria origin: **inferred**. Scope: H16 actual and explicitly identified extension scenario, invoice N16, separate CN16, and the explicitly scoped August–October historical prerequisite.

Does actual gross duration minus its paused union satisfy the inclusive 140-minute SLA?

- Decision criterion: The ledger gives gross 180, and the approved in-case union is 40. Thus chargeable time is 140. P2 includes equality, establishing that H16 meets the SLA.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P05`:

> Its gross 180 minutes minus 40 paused minutes gives exactly the permitted 140 chargeable minutes.

Assessment: **verified**. The ledger gives gross 180, and the approved in-case union is 40. Thus chargeable time is 140. P2 includes equality, establishing that H16 meets the SLA.

[evidence 0](input/sources/policy.md) at `P02`, [evidence 1](input/sources/policy.md) at `P03`, [evidence 2](input/sources/operations.md) at `P02`, [evidence 3](input/sources/operations.md) at `P03`, [proof 0: Settlement.exactDeadline](models/IntervalModel.lean)

Independent audit reasoning:

- The ledger gives gross 180, and the approved in-case union is 40. Thus chargeable time is 140. P2 includes equality, establishing that H16 meets the SLA.

[evidence 0](input/sources/policy.md) at `P02`, [evidence 1](input/sources/policy.md) at `P03`, [evidence 2](input/sources/operations.md) at `P02`, [evidence 3](input/sources/operations.md) at `P03`, [proof 0: Settlement.exactDeadline](models/IntervalModel.lean)

Audited claim dependencies: None declared.

Formalization rationale: Use finite interval union and exact signed integer rounding, with direct targets and explicitly auxiliary checks.

- Proof 0 source-to-target correspondence: The ledger gives gross 180, and the approved in-case union is 40. Thus chargeable time is 140. P2 includes equality, establishing that H16 meets the SLA. The model transcribes the cited integer values and the explicit policy, assuming faithful source transcription and protocol applicability. It does not authenticate records.

Declared bounded support search: Read the complete three-file source corpus and this report paragraph, including policy, full pause inventory, invoice and explicit historical limitations.

Queries: H16; pause; SLA; round; historical; reasonable

- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P01`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P02`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P01`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P02`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P01`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P02`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P03`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P05`.

The ledger gives gross 180, and the approved in-case union is 40. Thus chargeable time is 140. P2 includes equality, establishing that H16 meets the SLA.

Search limits: No external sources, missing historical records, or alternate report were used as evidence.

### Rules

- [P1] This synthetic protocol governs incident H16 and its November 2026 invoice. All times are integer minute offsets from 09:00 UTC on 2 November 2026. Pause intervals are half-open [start,end); a minute belongs to the interval exactly when start <= minute < end. The gross incident window is [0,180). Count each paused minute once using the union of approved in-scope intervals, clipped to the gross window. An interval of zero length contributes zero. Intervals marked other-case never pause H16.
- [P2] The SLA limit is 140 chargeable minutes inclusive. Chargeable time is gross elapsed minutes minus distinct approved in-scope paused minutes. An incident meets the SLA exactly when chargeable time <= 140. For the explicit extension scenario only, restoration occurs at minute 181 and all listed pause intervals and scope flags remain unchanged. No automatic tolerance minute applies.

### Assumptions

- The synthetic source transcriptions are faithful and SR-16 applies to H16; no external facts are added.

### Reasoning

- The ledger gives gross 180, and the approved in-case union is 40. Thus chargeable time is 140. P2 includes equality, establishing that H16 meets the SLA.

### Limits

- The supplied corpus is the entire search boundary. The model does not authenticate sources or establish missing historical events. Partial-window clipping is not independently exercised by this dossier.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Settlement.exactDeadline` in module `IntervalModel` (supports): `Settlement.meets Settlement.actualGross`.
  [Model](models/IntervalModel.lean) · [Executed check](checks/Target025.lean) · [Actual proof log](logs/target-025.log)

### Recommendation

Retain SLA compliance using gross 180, paused 40 and chargeable 140.

## C16-05

### Exact report claim

`input/report.md#P06`

> The explicit 181-minute extension scenario fails the SLA.

### Verification question

Does the explicit 181-minute extension satisfy the same inclusive SLA with unchanged intervals?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P02`

> [P1] This synthetic protocol governs incident H16 and its November 2026 invoice. All times are integer minute offsets from 09:00 UTC on 2 November 2026. Pause intervals are half-open [start,end); a minute belongs to the interval exactly when start <= minute < end. The gross incident window is [0,180). Count each paused minute once using the union of approved in-scope intervals, clipped to the gross window. An interval of zero length contributes zero. Intervals marked other-case never pause H16.

- [input/sources/policy.md](input/sources/policy.md) — `P03`

> [P2] The SLA limit is 140 chargeable minutes inclusive. Chargeable time is gross elapsed minutes minus distinct approved in-scope paused minutes. An incident meets the SLA exactly when chargeable time <= 140. For the explicit extension scenario only, restoration occurs at minute 181 and all listed pause intervals and scope flags remain unchanged. No automatic tolerance minute applies.

- [input/sources/operations.md](input/sources/operations.md) — `P02`

> [O1] Incident H16 opened at minute 0 and restoration occurred at minute 180. Approved H16 pause A is [20,40); approved H16 pause B is [30,50). Both records refer to the same stopped-service clock and overlap.

- [input/sources/operations.md](input/sources/operations.md) — `P03`

> [O2] Approved H16 pause C is [50,60). Approved H16 administrative marker Z is [60,60). Approved pause X is [70,80) but is marked other-case H17. Approved H16 pause Y is [190,200), wholly outside the actual incident window. A, B, C, Z, X and Y are the complete pause inventory for H16's actual decision.


### C16-05: criteria and report argument audit

Criteria origin: **inferred**. Scope: H16 actual and explicitly identified extension scenario, invoice N16, separate CN16, and the explicitly scoped August–October historical prerequisite.

Does the explicit 181-minute extension satisfy the same inclusive SLA with unchanged intervals?

- Decision criterion: At gross 181, Y still begins after the window. The union stays 40, giving 141 chargeable minutes. P2 allows 140 inclusive and explicitly excludes a tolerance minute, so the extended incident fails.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P06`:

> With Y still outside the scenario window, 181 minus 40 is 141, above the inclusive 140-minute limit.

Assessment: **verified**. At gross 181, Y still begins after the window. The union stays 40, giving 141 chargeable minutes. P2 allows 140 inclusive and explicitly excludes a tolerance minute, so the extended incident fails.

[evidence 0](input/sources/policy.md) at `P02`, [evidence 1](input/sources/policy.md) at `P03`, [evidence 2](input/sources/operations.md) at `P02`, [evidence 3](input/sources/operations.md) at `P03`, [proof 0: Settlement.extensionFails](models/IntervalModel.lean)

Independent audit reasoning:

- At gross 181, Y still begins after the window. The union stays 40, giving 141 chargeable minutes. P2 allows 140 inclusive and explicitly excludes a tolerance minute, so the extended incident fails.

[evidence 0](input/sources/policy.md) at `P02`, [evidence 1](input/sources/policy.md) at `P03`, [evidence 2](input/sources/operations.md) at `P02`, [evidence 3](input/sources/operations.md) at `P03`, [proof 0: Settlement.extensionFails](models/IntervalModel.lean)

Audited claim dependencies: None declared.

Formalization rationale: Use finite interval union and exact signed integer rounding, with direct targets and explicitly auxiliary checks.

- Proof 0 source-to-target correspondence: At gross 181, Y still begins after the window. The union stays 40, giving 141 chargeable minutes. P2 allows 140 inclusive and explicitly excludes a tolerance minute, so the extended incident fails. The model transcribes the cited integer values and the explicit policy, assuming faithful source transcription and protocol applicability. It does not authenticate records.

Declared bounded support search: Read the complete three-file source corpus and this report paragraph, including policy, full pause inventory, invoice and explicit historical limitations.

Queries: H16; pause; SLA; round; historical; reasonable

- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P01`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P02`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P01`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P02`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P01`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P02`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P03`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P05`.

At gross 181, Y still begins after the window. The union stays 40, giving 141 chargeable minutes. P2 allows 140 inclusive and explicitly excludes a tolerance minute, so the extended incident fails.

Search limits: No external sources, missing historical records, or alternate report were used as evidence.

### Rules

- [P1] This synthetic protocol governs incident H16 and its November 2026 invoice. All times are integer minute offsets from 09:00 UTC on 2 November 2026. Pause intervals are half-open [start,end); a minute belongs to the interval exactly when start <= minute < end. The gross incident window is [0,180). Count each paused minute once using the union of approved in-scope intervals, clipped to the gross window. An interval of zero length contributes zero. Intervals marked other-case never pause H16.
- [P2] The SLA limit is 140 chargeable minutes inclusive. Chargeable time is gross elapsed minutes minus distinct approved in-scope paused minutes. An incident meets the SLA exactly when chargeable time <= 140. For the explicit extension scenario only, restoration occurs at minute 181 and all listed pause intervals and scope flags remain unchanged. No automatic tolerance minute applies.

### Assumptions

- The synthetic source transcriptions are faithful and SR-16 applies to H16; no external facts are added.

### Reasoning

- At gross 181, Y still begins after the window. The union stays 40, giving 141 chargeable minutes. P2 allows 140 inclusive and explicitly excludes a tolerance minute, so the extended incident fails.

### Limits

- The supplied corpus is the entire search boundary. The model does not authenticate sources or establish missing historical events. Partial-window clipping is not independently exercised by this dossier.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Settlement.extensionFails` in module `IntervalModel` (supports): `¬ Settlement.meets 181`.
  [Model](models/IntervalModel.lean) · [Executed check](checks/Target026.lean) · [Actual proof log](logs/target-026.log)

### Recommendation

Record the extension as failing at 141 chargeable minutes.

## C16-06

### Exact report claim

`input/report.md#P07`

> Invoice line L1 rounds to +101 cents.

### Verification question

What integer cent amount does the exact positive half-cent line produce under away-from-zero rounding?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P04`

> [P3] Monetary source amounts are signed integer mills: ten mills equal one cent. Round each invoice line separately to integer cents, choosing the nearest cent and resolving an exact half-cent tie away from zero. For a negative credit, round its absolute magnitude under the same rule and restore the negative sign. Sum the signed rounded lines; never round the unrounded invoice aggregate instead. The separate credit note is not an invoice line.

- [input/sources/invoice.md](input/sources/invoice.md) — `P02`

> [I1] Invoice N16 contains precisely three signed lines: service component L1 +1005 mills; service component L2 +1005 mills; adjustment L3 -1000 mills. These amounts are exact, not measured approximations. No tax or additional lines apply.


### C16-06: criteria and report argument audit

Criteria origin: **inferred**. Scope: H16 actual and explicitly identified extension scenario, invoice N16, separate CN16, and the explicitly scoped August–October historical prerequisite.

What integer cent amount does the exact positive half-cent line produce under away-from-zero rounding?

- Decision criterion: 1005 mills divided by ten is 100.5 cents. P3 sends the exact positive tie away from zero to 101 cents; 100 would implement the wrong tie policy.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P07`:

> Its +1005 mills is exactly +100.5 cents, and P3 resolves the tie away from zero.

Assessment: **verified**. 1005 mills divided by ten is 100.5 cents. P3 sends the exact positive tie away from zero to 101 cents; 100 would implement the wrong tie policy.

[evidence 0](input/sources/policy.md) at `P04`, [evidence 1](input/sources/invoice.md) at `P02`, [proof 0: Settlement.positiveTie](models/IntervalModel.lean)

Report citation at `P07`:

> P3

Assessment: **verified**. The cited passage exists and its content matches the attributed bounded statement.

[evidence 0](input/sources/policy.md) at `P04`

Independent audit reasoning:

- 1005 mills divided by ten is 100.5 cents. P3 sends the exact positive tie away from zero to 101 cents; 100 would implement the wrong tie policy.

[evidence 0](input/sources/policy.md) at `P04`, [evidence 1](input/sources/invoice.md) at `P02`, [proof 0: Settlement.positiveTie](models/IntervalModel.lean)

Audited claim dependencies: None declared.

Formalization rationale: Use finite interval union and exact signed integer rounding, with direct targets and explicitly auxiliary checks.

- Proof 0 source-to-target correspondence: 1005 mills divided by ten is 100.5 cents. P3 sends the exact positive tie away from zero to 101 cents; 100 would implement the wrong tie policy. The model transcribes the cited integer values and the explicit policy, assuming faithful source transcription and protocol applicability. It does not authenticate records.

Declared bounded support search: Read the complete three-file source corpus and this report paragraph, including policy, full pause inventory, invoice and explicit historical limitations.

Queries: H16; pause; SLA; round; historical; reasonable

- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P01`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P02`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P01`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P02`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P01`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P02`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P03`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P05`.

1005 mills divided by ten is 100.5 cents. P3 sends the exact positive tie away from zero to 101 cents; 100 would implement the wrong tie policy.

Search limits: No external sources, missing historical records, or alternate report were used as evidence.

### Rules

- [P3] Monetary source amounts are signed integer mills: ten mills equal one cent. Round each invoice line separately to integer cents, choosing the nearest cent and resolving an exact half-cent tie away from zero. For a negative credit, round its absolute magnitude under the same rule and restore the negative sign. Sum the signed rounded lines; never round the unrounded invoice aggregate instead. The separate credit note is not an invoice line.

### Assumptions

- The synthetic source transcriptions are faithful and SR-16 applies to H16; no external facts are added.

### Reasoning

- 1005 mills divided by ten is 100.5 cents. P3 sends the exact positive tie away from zero to 101 cents; 100 would implement the wrong tie policy.

### Limits

- The supplied corpus is the entire search boundary. The model does not authenticate sources or establish missing historical events. Partial-window clipping is not independently exercised by this dossier.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Settlement.positiveTie` in module `IntervalModel` (supports): `Settlement.roundCents 1005 = 101`.
  [Model](models/IntervalModel.lean) · [Executed check](checks/Target027.lean) · [Actual proof log](logs/target-027.log)

### Recommendation

Record L1 as +101 cents.

## C16-07

### Exact report claim

`input/report.md#P08`

> Credit note CN16 rounds to -101 cents.

### Verification question

What integer cent amount does the exact negative half-cent credit produce under away-from-zero rounding?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P04`

> [P3] Monetary source amounts are signed integer mills: ten mills equal one cent. Round each invoice line separately to integer cents, choosing the nearest cent and resolving an exact half-cent tie away from zero. For a negative credit, round its absolute magnitude under the same rule and restore the negative sign. Sum the signed rounded lines; never round the unrounded invoice aggregate instead. The separate credit note is not an invoice line.

- [input/sources/invoice.md](input/sources/invoice.md) — `P03`

> [I2] The separately issued credit note CN16 is -1005 mills and is excluded from invoice N16's total. Its exact absolute magnitude is 1005 mills.


### C16-07: criteria and report argument audit

Criteria origin: **inferred**. Scope: H16 actual and explicitly identified extension scenario, invoice N16, separate CN16, and the explicitly scoped August–October historical prerequisite.

What integer cent amount does the exact negative half-cent credit produce under away-from-zero rounding?

- Decision criterion: The absolute credit magnitude is 1005 mills, or 100.5 cents. Round magnitude to 101 and restore the negative sign: -101 cents. Moving to -100 would round the tie toward zero.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P08`:

> P3 applies away-from-zero rounding to the exact negative half-cent tie.

Assessment: **verified**. The absolute credit magnitude is 1005 mills, or 100.5 cents. Round magnitude to 101 and restore the negative sign: -101 cents. Moving to -100 would round the tie toward zero.

[evidence 0](input/sources/policy.md) at `P04`, [evidence 1](input/sources/invoice.md) at `P03`, [proof 0: Settlement.negativeTie](models/IntervalModel.lean)

Report citation at `P08`:

> P3

Assessment: **verified**. The cited passage exists and its content matches the attributed bounded statement.

[evidence 0](input/sources/policy.md) at `P04`

Independent audit reasoning:

- The absolute credit magnitude is 1005 mills, or 100.5 cents. Round magnitude to 101 and restore the negative sign: -101 cents. Moving to -100 would round the tie toward zero.

[evidence 0](input/sources/policy.md) at `P04`, [evidence 1](input/sources/invoice.md) at `P03`, [proof 0: Settlement.negativeTie](models/IntervalModel.lean)

Audited claim dependencies: None declared.

Formalization rationale: Use finite interval union and exact signed integer rounding, with direct targets and explicitly auxiliary checks.

- Proof 0 source-to-target correspondence: The absolute credit magnitude is 1005 mills, or 100.5 cents. Round magnitude to 101 and restore the negative sign: -101 cents. Moving to -100 would round the tie toward zero. The model transcribes the cited integer values and the explicit policy, assuming faithful source transcription and protocol applicability. It does not authenticate records.

Declared bounded support search: Read the complete three-file source corpus and this report paragraph, including policy, full pause inventory, invoice and explicit historical limitations.

Queries: H16; pause; SLA; round; historical; reasonable

- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P01`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P02`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P01`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P02`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P01`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P02`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P03`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P05`.

The absolute credit magnitude is 1005 mills, or 100.5 cents. Round magnitude to 101 and restore the negative sign: -101 cents. Moving to -100 would round the tie toward zero.

Search limits: No external sources, missing historical records, or alternate report were used as evidence.

### Rules

- [P3] Monetary source amounts are signed integer mills: ten mills equal one cent. Round each invoice line separately to integer cents, choosing the nearest cent and resolving an exact half-cent tie away from zero. For a negative credit, round its absolute magnitude under the same rule and restore the negative sign. Sum the signed rounded lines; never round the unrounded invoice aggregate instead. The separate credit note is not an invoice line.

### Assumptions

- The synthetic source transcriptions are faithful and SR-16 applies to H16; no external facts are added.

### Reasoning

- The absolute credit magnitude is 1005 mills, or 100.5 cents. Round magnitude to 101 and restore the negative sign: -101 cents. Moving to -100 would round the tie toward zero.

### Limits

- The supplied corpus is the entire search boundary. The model does not authenticate sources or establish missing historical events. Partial-window clipping is not independently exercised by this dossier.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Settlement.negativeTie` in module `IntervalModel` (supports): `Settlement.roundCents (-1005) = -101`.
  [Model](models/IntervalModel.lean) · [Executed check](checks/Target028.lean) · [Actual proof log](logs/target-028.log)

### Recommendation

Record CN16 as -101 cents.

## C16-08

### Exact report claim

`input/report.md#P09`

> Invoice N16 totals +102 cents.

### Verification question

What is the signed sum after rounding each of the three invoice lines separately?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P04`

> [P3] Monetary source amounts are signed integer mills: ten mills equal one cent. Round each invoice line separately to integer cents, choosing the nearest cent and resolving an exact half-cent tie away from zero. For a negative credit, round its absolute magnitude under the same rule and restore the negative sign. Sum the signed rounded lines; never round the unrounded invoice aggregate instead. The separate credit note is not an invoice line.

- [input/sources/invoice.md](input/sources/invoice.md) — `P02`

> [I1] Invoice N16 contains precisely three signed lines: service component L1 +1005 mills; service component L2 +1005 mills; adjustment L3 -1000 mills. These amounts are exact, not measured approximations. No tax or additional lines apply.

- [input/sources/invoice.md](input/sources/invoice.md) — `P03`

> [I2] The separately issued credit note CN16 is -1005 mills and is excluded from invoice N16's total. Its exact absolute magnitude is 1005 mills.


### C16-08: criteria and report argument audit

Criteria origin: **inferred**. Scope: H16 actual and explicitly identified extension scenario, invoice N16, separate CN16, and the explicitly scoped August–October historical prerequisite.

What is the signed sum after rounding each of the three invoice lines separately?

- Decision criterion: Round +1005 to +101, +1005 to +101, and -1000 to -100. Sum is +102 cents. The aggregate 1010 mills rounds to +101, but P3 expressly requires per-line rounding and excludes the separate CN16 credit note.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P09`:

> The separately rounded lines are +101, +101 and -100 cents, and the credit note is excluded.

Assessment: **verified**. Round +1005 to +101, +1005 to +101, and -1000 to -100. Sum is +102 cents. The aggregate 1010 mills rounds to +101, but P3 expressly requires per-line rounding and excludes the separate CN16 credit note.

[evidence 0](input/sources/policy.md) at `P04`, [evidence 1](input/sources/invoice.md) at `P02`, [evidence 2](input/sources/invoice.md) at `P03`, [proof 0: Settlement.invoice102](models/IntervalModel.lean), [proof 1: Settlement.aggregateIs101](models/IntervalModel.lean)

Independent audit reasoning:

- Round +1005 to +101, +1005 to +101, and -1000 to -100. Sum is +102 cents. The aggregate 1010 mills rounds to +101, but P3 expressly requires per-line rounding and excludes the separate CN16 credit note.

[evidence 0](input/sources/policy.md) at `P04`, [evidence 1](input/sources/invoice.md) at `P02`, [evidence 2](input/sources/invoice.md) at `P03`, [proof 0: Settlement.invoice102](models/IntervalModel.lean), [proof 1: Settlement.aggregateIs101](models/IntervalModel.lean)

Audited claim dependencies: None declared.

Formalization rationale: Use finite interval union and exact signed integer rounding, with direct targets and explicitly auxiliary checks.

- Proof 0 source-to-target correspondence: Round +1005 to +101, +1005 to +101, and -1000 to -100. Sum is +102 cents. The aggregate 1010 mills rounds to +101, but P3 expressly requires per-line rounding and excludes the separate CN16 credit note. The model transcribes the cited integer values and the explicit policy, assuming faithful source transcription and protocol applicability. It does not authenticate records.
- Proof 1 source-to-target correspondence: The three I1 signed mills sum to 1010, which rounds to 101 cents. This verifies the alternative aggregate calculation only; P3 prohibits using it as the invoice total. The direct total target instead sums rounded lines.

Declared bounded support search: Read the complete three-file source corpus and this report paragraph, including policy, full pause inventory, invoice and explicit historical limitations.

Queries: H16; pause; SLA; round; historical; reasonable

- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P01`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P02`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P01`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P02`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P01`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P02`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P03`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P05`.

Round +1005 to +101, +1005 to +101, and -1000 to -100. Sum is +102 cents. The aggregate 1010 mills rounds to +101, but P3 expressly requires per-line rounding and excludes the separate CN16 credit note.

Search limits: No external sources, missing historical records, or alternate report were used as evidence.

### Rules

- [P3] Monetary source amounts are signed integer mills: ten mills equal one cent. Round each invoice line separately to integer cents, choosing the nearest cent and resolving an exact half-cent tie away from zero. For a negative credit, round its absolute magnitude under the same rule and restore the negative sign. Sum the signed rounded lines; never round the unrounded invoice aggregate instead. The separate credit note is not an invoice line.

### Assumptions

- The synthetic source transcriptions are faithful and SR-16 applies to H16; no external facts are added.

### Reasoning

- Round +1005 to +101, +1005 to +101, and -1000 to -100. Sum is +102 cents. The aggregate 1010 mills rounds to +101, but P3 expressly requires per-line rounding and excludes the separate CN16 credit note.

### Limits

- The supplied corpus is the entire search boundary. The model does not authenticate sources or establish missing historical events. Partial-window clipping is not independently exercised by this dossier.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Settlement.invoice102` in module `IntervalModel` (supports): `Settlement.invoiceTotal = 102`.
  [Model](models/IntervalModel.lean) · [Executed check](checks/Target029.lean) · [Actual proof log](logs/target-029.log)

- `Settlement.aggregateIs101` in module `IntervalModel` (auxiliary): `Settlement.roundCents Settlement.invoiceLines.sum = 101`.
  [Model](models/IntervalModel.lean) · [Executed check](checks/Target030.lean) · [Actual proof log](logs/target-030.log)

### Recommendation

Record invoice N16 as +102 cents; keep CN16 separate.

## C16-09

### Exact report claim

`input/report.md#P10`

> The supplied corpus cannot establish entitlement to the historical rebate.

### Verification question

Do the supplied sources establish the necessary prior-quarter breach threshold for historical rebate entitlement?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P05`

> [P4] A historical rebate requires at least three SLA breaches during August through October 2026. An H16 decision in November cannot establish the earlier-quarter breach count. This protocol provides no definition, benchmark, or test for whether compensation is reasonable.

- [input/sources/operations.md](input/sources/operations.md) — `P04`

> [O3] This delivery contains only the H16 incident record. No August, September or October incident records, aggregate breach counts, or completeness certification for those months are supplied. The absence of those records does not assert that no earlier breaches occurred.


### C16-09: criteria and report argument audit

Criteria origin: **inferred**. Scope: H16 actual and explicitly identified extension scenario, invoice N16, separate CN16, and the explicitly scoped August–October historical prerequisite.

Do the supplied sources establish the necessary prior-quarter breach threshold for historical rebate entitlement?

- Decision criterion: P4 makes three earlier-quarter breaches a necessary condition. O3 explicitly provides no earlier-quarter counts or events. Neither a zero count nor three breaches may be asserted as actual. Counts zero and three illustrate why the available history does not select a threshold outcome; meeting the threshold alone is not proved sufficient for entitlement.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P10`:

> P4 requires three prior-quarter breaches and O3 supplies no prior-quarter breach history.

Assessment: **verified**. P4 makes three earlier-quarter breaches a necessary condition. O3 explicitly provides no earlier-quarter counts or events. Neither a zero count nor three breaches may be asserted as actual. Counts zero and three illustrate why the available history does not select a threshold outcome; meeting the threshold alone is not proved sufficient for entitlement.

[evidence 0](input/sources/policy.md) at `P05`, [evidence 1](input/sources/operations.md) at `P04`

Report citation at `P10`:

> P4

Assessment: **verified**. The cited passage exists and its content matches the attributed bounded statement.

[evidence 0](input/sources/policy.md) at `P05`

Report citation at `P10`:

> O3

Assessment: **verified**. The cited passage exists and its content matches the attributed bounded statement.

[evidence 1](input/sources/operations.md) at `P04`

Independent audit reasoning:

- P4 makes three earlier-quarter breaches a necessary condition. O3 explicitly provides no earlier-quarter counts or events. Neither a zero count nor three breaches may be asserted as actual. Counts zero and three illustrate why the available history does not select a threshold outcome; meeting the threshold alone is not proved sufficient for entitlement.

[evidence 0](input/sources/policy.md) at `P05`, [evidence 1](input/sources/operations.md) at `P04`

Audited claim dependencies: None declared.

Formalization rationale: A bounded documentary metaclaim is checked by source inspection; no historical fact or undefined qualitative judgment is encoded as a theorem.


Declared bounded support search: Read the complete three-file source corpus and this report paragraph, including policy, full pause inventory, invoice and explicit historical limitations.

Queries: H16; pause; SLA; round; historical; reasonable

- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P01`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P02`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P01`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P02`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P01`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P02`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P03`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P05`.

P4 makes three earlier-quarter breaches a necessary condition. O3 explicitly provides no earlier-quarter counts or events. Neither a zero count nor three breaches may be asserted as actual. Counts zero and three illustrate why the available history does not select a threshold outcome; meeting the threshold alone is not proved sufficient for entitlement.

Search limits: No external sources, missing historical records, or alternate report were used as evidence.

### Rules

- [P4] A historical rebate requires at least three SLA breaches during August through October 2026. An H16 decision in November cannot establish the earlier-quarter breach count. This protocol provides no definition, benchmark, or test for whether compensation is reasonable.

### Assumptions

- The synthetic source transcriptions are faithful and SR-16 applies to H16; no external facts are added.

### Reasoning

- P4 makes three earlier-quarter breaches a necessary condition. O3 explicitly provides no earlier-quarter counts or events. Neither a zero count nor three breaches may be asserted as actual. Counts zero and three illustrate why the available history does not select a threshold outcome; meeting the threshold alone is not proved sufficient for entitlement.

### Limits

- The supplied corpus is the entire search boundary. The model does not authenticate sources or establish missing historical events. Partial-window clipping is not independently exercised by this dossier.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Obtain the August–October breach records and any additional entitlement requirements before deciding the historical rebate.

## C16-10

### Exact report claim

`input/report.md#P11`

> Whether H16 compensation is reasonable remains unresolved under the supplied protocol.

### Verification question

Does the supplied protocol define an operational standard permitting a reasonableness verdict?

### Source evidence

- [input/sources/policy.md](input/sources/policy.md) — `P05`

> [P4] A historical rebate requires at least three SLA breaches during August through October 2026. An H16 decision in November cannot establish the earlier-quarter breach count. This protocol provides no definition, benchmark, or test for whether compensation is reasonable.


### C16-10: criteria and report argument audit

Criteria origin: **inferred**. Scope: H16 actual and explicitly identified extension scenario, invoice N16, separate CN16, and the explicitly scoped August–October historical prerequisite.

Does the supplied protocol define an operational standard permitting a reasonableness verdict?

- Decision criterion: P4 explicitly states that no definition, benchmark or test of reasonable compensation is supplied. Full source inspection finds no substitute standard. A substantive reasonableness conclusion cannot be determined without an authorized criterion. This is not a refutation of compensation being reasonable.

Missing definitions: Operational reasonableness criterion.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P11`:

> P4 supplies no operational definition or benchmark for reasonableness.

Assessment: **verified**. P4 explicitly states that no definition, benchmark or test of reasonable compensation is supplied. Full source inspection finds no substitute standard. A substantive reasonableness conclusion cannot be determined without an authorized criterion. This is not a refutation of compensation being reasonable.

[evidence 0](input/sources/policy.md) at `P05`

Report citation at `P11`:

> P4

Assessment: **verified**. The cited passage exists and its content matches the attributed bounded statement.

[evidence 0](input/sources/policy.md) at `P05`

Independent audit reasoning:

- P4 explicitly states that no definition, benchmark or test of reasonable compensation is supplied. Full source inspection finds no substitute standard. A substantive reasonableness conclusion cannot be determined without an authorized criterion. This is not a refutation of compensation being reasonable.

[evidence 0](input/sources/policy.md) at `P05`

Audited claim dependencies: None declared.

Formalization rationale: A bounded documentary metaclaim is checked by source inspection; no historical fact or undefined qualitative judgment is encoded as a theorem.


Declared bounded support search: Read the complete three-file source corpus and this report paragraph, including policy, full pause inventory, invoice and explicit historical limitations.

Queries: H16; pause; SLA; round; historical; reasonable

- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P01`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P02`.
- Inspected [input/sources/invoice.md](input/sources/invoice.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P01`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P02`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P03`.
- Inspected [input/sources/operations.md](input/sources/operations.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P01`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P02`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P03`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P04`.
- Inspected [input/sources/policy.md](input/sources/policy.md) at `P05`.

P4 explicitly states that no definition, benchmark or test of reasonable compensation is supplied. Full source inspection finds no substitute standard. A substantive reasonableness conclusion cannot be determined without an authorized criterion. This is not a refutation of compensation being reasonable.

Search limits: No external sources, missing historical records, or alternate report were used as evidence.

### Rules

- [P4] A historical rebate requires at least three SLA breaches during August through October 2026. An H16 decision in November cannot establish the earlier-quarter breach count. This protocol provides no definition, benchmark, or test for whether compensation is reasonable.

### Assumptions

- The synthetic source transcriptions are faithful and SR-16 applies to H16; no external facts are added.

### Reasoning

- P4 explicitly states that no definition, benchmark or test of reasonable compensation is supplied. Full source inspection finds no substitute standard. A substantive reasonableness conclusion cannot be determined without an authorized criterion. This is not a refutation of compensation being reasonable.

### Limits

- The supplied corpus is the entire search boundary. The model does not authenticate sources or establish missing historical events. Partial-window clipping is not independently exercised by this dossier.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Obtain an authorized definition or benchmark before assessing reasonableness.
