# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

## Registered claim coverage

Coverage: **complete_registration**; 6 reviewed anchors; 7 audited and 0 deferred claims.

Registration reconciles declared claims and reviewed report anchors; it does not establish semantic completeness, faithful decomposition, or that declared searches were actually performed.

- `P01`: non_claim — Administrative title or companion-publication note, outside substantive stock findings; preserved unchanged and not used as evidence.
- `P02`: non_claim — Administrative title or companion-publication note, outside substantive stock findings; preserved unchanged and not used as evidence.
- `P03`: claims — Atomic conclusions registered separately; material premises and inferences audited in report_items.
- `P04`: claims — Atomic conclusions registered separately; material premises and inferences audited in report_items.
- `P05`: claims — Atomic conclusions registered separately; material premises and inferences audited in report_items.
- `P06`: claims — Atomic conclusions registered separately; material premises and inferences audited in report_items.
[Semantic correspondence review](semantic-review.md)

Extraction inventory: 2 documents; 0 pending, partial or blocked. See [ingestion details](ingestion.json) and [coverage](coverage.md).

## C1

### Exact report claim

`input/report.md#P03`

> Counted stock is 45 units

### Verification question

Is counted stock exactly 45 whole units?

### Source evidence

- [input/sources/stock.html.md](input/sources/stock.html.md) — `scope`

> This is the complete current stock population: A, B and C. Quantities are exact whole units at this snapshot.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 6, "end_line": 6, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `count-rule`

> Counted stock includes active and quarantined rows only; archived rows are excluded.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 7, "end_line": 7, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-a`

> A: status active; quantity 18 units; signed yes.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 9, "end_line": 9, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-b`

> B: status quarantined; quantity 27 units; signed yes.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 10, "end_line": 10, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-c`

> C: status archived; quantity 15 units; signed no.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 11, "end_line": 11, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.


### C1: criteria and report argument audit

Criteria origin: **inferred**. Scope: A/B/C at the 4 November 2026 snapshot; documentary historical knowledge only.

Is counted stock exactly 45 whole units?

- Decision criterion: Count active and quarantined rows once; exclude archived rows.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P03`:

> active A contributes 18 and quarantined B contributes 27.

Assessment: **verified**. Original lines 9 and 10 give these statuses and quantities.

[evidence 2](input/sources/stock.html.md) at `row-a`, [evidence 3](input/sources/stock.html.md) at `row-b`

Report premise at `P03`:

> Archived C is excluded by the supplied rule.

Assessment: **verified**. Original lines 7 and 11 exclude C.

[evidence 1](input/sources/stock.html.md) at `count-rule`, [evidence 4](input/sources/stock.html.md) at `row-c`

Report inference at `P03`:

> Counted stock is 45 units: active A contributes 18 and quarantined B contributes 27.

Assessment: **verified**. Included quantities sum to 45.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 1](input/sources/stock.html.md) at `count-rule`, [evidence 2](input/sources/stock.html.md) at `row-a`, [evidence 3](input/sources/stock.html.md) at `row-b`, [proof 0: StockAudit.counted45](models/Stock/Audit.lean)

Independent audit reasoning:

- 1. A is active with 18 and B quarantined with 27; both are included.
- 2. C is archived, so its 15 is excluded.
- 3. The exact included sum is 18 + 27 = 45.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 1](input/sources/stock.html.md) at `count-rule`, [evidence 2](input/sources/stock.html.md) at `row-a`, [evidence 3](input/sources/stock.html.md) at `row-b`, [evidence 4](input/sources/stock.html.md) at `row-c`, [proof 0: StockAudit.counted45](models/Stock/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: Use the finite source-linked stock model and exact target.

- Proof 0 source-to-target correspondence: Stock.rows transcribes A/B/C; counted filters statuses per original line 7. Summing the included quantities proves 45 conditional on source fidelity.

Declared bounded support search: Read all original HTML lines 1-14 and all six report paragraphs.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `title`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `h1`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `scope`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `count-rule`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `release-rule`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-a`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-b`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-c`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `history`.

3. The exact included sum is 18 + 27 = 45.

Search limits: No external source or historical registry was supplied or searched.

### Rules

- Count active and quarantined rows once; exclude archived rows.

### Assumptions

- The supplied synthetic snapshot and its explicit complete current population and rules are accepted for this audit; historical completeness is not assumed.

### Reasoning

- 1. A is active with 18 and B quarantined with 27; both are included.
- 2. C is archived, so its 15 is excluded.
- 3. The exact included sum is 18 + 27 = 45.

### Limits

- Only this supplied synthetic snapshot is audited; authenticity and actual historical events are not established.
- Initial fixture-familiar self-review was followed by a separate coordinator source-first/model review; both are nonblind.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `StockAudit.counted45` in module `Stock.Audit` (supports): `Stock.total = 45`.
  [Model](models/Stock/Audit.lean) · [Executed check](checks/Target012.lean) · [Actual proof log](logs/target-012.log)

### Recommendation

Retain the scoped claim and its stated limits.

## C2

### Exact report claim

`input/report.md#P04`

> All rows together sum to 60 units

### Verification question

Do all recorded rows total 60 whole units?

### Source evidence

- [input/sources/stock.html.md](input/sources/stock.html.md) — `scope`

> This is the complete current stock population: A, B and C. Quantities are exact whole units at this snapshot.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 6, "end_line": 6, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-a`

> A: status active; quantity 18 units; signed yes.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 9, "end_line": 9, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-b`

> B: status quarantined; quantity 27 units; signed yes.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 10, "end_line": 10, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-c`

> C: status archived; quantity 15 units; signed no.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 11, "end_line": 11, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.


### C2: criteria and report argument audit

Criteria origin: **inferred**. Scope: A/B/C at the 4 November 2026 snapshot; documentary historical knowledge only.

Do all recorded rows total 60 whole units?

- Decision criterion: Sum every member of the complete current population without a status filter.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **not_provided**.

Independent audit reasoning:

- 1. The complete population has quantities 18, 27, 15.
- 2. Their unfiltered sum is 60; the report supplies no calculation for this separate assertion.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 1](input/sources/stock.html.md) at `row-a`, [evidence 2](input/sources/stock.html.md) at `row-b`, [evidence 3](input/sources/stock.html.md) at `row-c`, [proof 0: StockAudit.allRows60](models/Stock/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: Use the finite source-linked stock model and exact target.

- Proof 0 source-to-target correspondence: Unfiltered rows represent all three recorded quantities. This target supports only the all-row total, not counted stock.

Declared bounded support search: Read all original HTML lines 1-14 and all six report paragraphs.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `title`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `h1`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `scope`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `count-rule`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `release-rule`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-a`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-b`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-c`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `history`.

2. Their unfiltered sum is 60; the report supplies no calculation for this separate assertion.

Search limits: No external source or historical registry was supplied or searched.

### Rules

- Sum every member of the complete current population without a status filter.

### Assumptions

- The supplied synthetic snapshot and its explicit complete current population and rules are accepted for this audit; historical completeness is not assumed.

### Reasoning

- 1. The complete population has quantities 18, 27, 15.
- 2. Their unfiltered sum is 60; the report supplies no calculation for this separate assertion.

### Limits

- Only this supplied synthetic snapshot is audited; authenticity and actual historical events are not established.
- Initial fixture-familiar self-review was followed by a separate coordinator source-first/model review; both are nonblind.

### Result

Semantic state: **supported**; argument status: **insufficient_support**; formal status: **proved**.

### Formal evidence

- `StockAudit.allRows60` in module `Stock.Audit` (supports): `(Stock.rows.map Stock.Row.quantity).sum = 60`.
  [Model](models/Stock/Audit.lean) · [Executed check](checks/Target013.lean) · [Actual proof log](logs/target-013.log)

### Recommendation

Retain the scoped claim and its stated limits.

## C3

### Exact report claim

`input/report.md#P04`

> that is not the defined counted-stock total.

### Verification question

Is the preceding 60-unit all-row total different from counted stock?

### Source evidence

- [input/sources/stock.html.md](input/sources/stock.html.md) — `scope`

> This is the complete current stock population: A, B and C. Quantities are exact whole units at this snapshot.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 6, "end_line": 6, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `count-rule`

> Counted stock includes active and quarantined rows only; archived rows are excluded.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 7, "end_line": 7, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-a`

> A: status active; quantity 18 units; signed yes.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 9, "end_line": 9, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-b`

> B: status quarantined; quantity 27 units; signed yes.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 10, "end_line": 10, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-c`

> C: status archived; quantity 15 units; signed no.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 11, "end_line": 11, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.


### C3: criteria and report argument audit

Criteria origin: **inferred**. Scope: A/B/C at the 4 November 2026 snapshot; documentary historical knowledge only.

Is the preceding 60-unit all-row total different from counted stock?

- Decision criterion: Resolve “that” as the immediately preceding 60-unit total.
- Decision criterion: Apply the counted-stock filter before comparison.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P03`:

> Counted stock is 45 units

Assessment: **verified**. The preceding report finding supplies the counted total; C1 independently verifies it using the status rule.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 1](input/sources/stock.html.md) at `count-rule`, [evidence 2](input/sources/stock.html.md) at `row-a`, [evidence 3](input/sources/stock.html.md) at `row-b`, [evidence 4](input/sources/stock.html.md) at `row-c`, [proof 0: StockAudit.notCounted60](models/Stock/Audit.lean)

Report premise at `P04`:

> All rows together sum to 60 units

Assessment: **verified**. C2 independently verifies this total, while retaining its separate report derivation gap.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 2](input/sources/stock.html.md) at `row-a`, [evidence 3](input/sources/stock.html.md) at `row-b`, [evidence 4](input/sources/stock.html.md) at `row-c`

Report inference at `P04`:

> but that is not the defined counted-stock total.

Assessment: **verified**. The implicit comparison of the two explicitly stated distinct totals is valid in whole-report context; counted stock is 45, not 60.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 1](input/sources/stock.html.md) at `count-rule`, [evidence 2](input/sources/stock.html.md) at `row-a`, [evidence 3](input/sources/stock.html.md) at `row-b`, [evidence 4](input/sources/stock.html.md) at `row-c`, [proof 0: StockAudit.notCounted60](models/Stock/Audit.lean)

Independent audit reasoning:

- 1. “That” refers to the 60-unit all-row total in R2.
- 2. R1 explicitly establishes counted stock as 45, and R2 states the all-row total 60.
- 3. Reading the report as a whole, the distinct totals directly justify the negative comparison: 45 is not 60. Independent source computation confirms the distinction.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 1](input/sources/stock.html.md) at `count-rule`, [evidence 2](input/sources/stock.html.md) at `row-a`, [evidence 3](input/sources/stock.html.md) at `row-b`, [evidence 4](input/sources/stock.html.md) at `row-c`, [proof 0: StockAudit.notCounted60](models/Stock/Audit.lean)

Audited claim dependencies: C1, C2

Formalization rationale: Use the finite source-linked stock model and exact target.

- Proof 0 source-to-target correspondence: The target directly supports the report negation of equality, rather than refuting the correctly negative report claim.

Declared bounded support search: Read all original HTML lines 1-14 and all six report paragraphs.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `title`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `h1`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `scope`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `count-rule`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `release-rule`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-a`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-b`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-c`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `history`.

3. Reading the report as a whole, the distinct totals directly justify the negative comparison: 45 is not 60. Independent source computation confirms the distinction.

Search limits: No external source or historical registry was supplied or searched.

### Rules

- Resolve “that” as the immediately preceding 60-unit total.
- Apply the counted-stock filter before comparison.

### Assumptions

- The supplied synthetic snapshot and its explicit complete current population and rules are accepted for this audit; historical completeness is not assumed.

### Reasoning

- 1. “That” refers to the 60-unit all-row total in R2.
- 2. R1 explicitly establishes counted stock as 45, and R2 states the all-row total 60.
- 3. Reading the report as a whole, the distinct totals directly justify the negative comparison: 45 is not 60. Independent source computation confirms the distinction.

### Limits

- Only this supplied synthetic snapshot is audited; authenticity and actual historical events are not established.
- Initial fixture-familiar self-review was followed by a separate coordinator source-first/model review; both are nonblind.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `StockAudit.notCounted60` in module `Stock.Audit` (supports): `Stock.total ≠ 60`.
  [Model](models/Stock/Audit.lean) · [Executed check](checks/Target014.lean) · [Actual proof log](logs/target-014.log)

### Recommendation

Retain the scoped claim and its stated limits.

## C4

### Exact report claim

`input/report.md#P05`

> A is eligible for release

### Verification question

Does A meet the release criterion?

### Source evidence

- [input/sources/stock.html.md](input/sources/stock.html.md) — `release-rule`

> A row is eligible for release if and only if it is active and signed.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 8, "end_line": 8, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-a`

> A: status active; quantity 18 units; signed yes.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 9, "end_line": 9, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.


### C4: criteria and report argument audit

Criteria origin: **inferred**. Scope: A/B/C at the 4 November 2026 snapshot; documentary historical knowledge only.

Does A meet the release criterion?

- Decision criterion: Require both active status and signature.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P05`:

> A is both active and signed.

Assessment: **verified**. Both properties are explicit in the A row.

[evidence 1](input/sources/stock.html.md) at `row-a`

Report inference at `P05`:

> A is eligible for release because A is both active and signed.

Assessment: **verified**. The source biconditional validates both-premise inference.

[evidence 0](input/sources/stock.html.md) at `release-rule`, [evidence 1](input/sources/stock.html.md) at `row-a`, [proof 0: StockAudit.aEligible](models/Stock/Audit.lean)

Independent audit reasoning:

- 1. A is active and signed in original line 9.
- 2. The biconditional at line 8 makes A eligible.

[evidence 0](input/sources/stock.html.md) at `release-rule`, [evidence 1](input/sources/stock.html.md) at `row-a`, [proof 0: StockAudit.aEligible](models/Stock/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: Use the finite source-linked stock model and exact target.

- Proof 0 source-to-target correspondence: eligible is exactly active AND signed from line 8, satisfied by A from line 9.

Declared bounded support search: Read all original HTML lines 1-14 and all six report paragraphs.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `title`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `h1`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `scope`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `count-rule`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `release-rule`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-a`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-b`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-c`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `history`.

2. The biconditional at line 8 makes A eligible.

Search limits: No external source or historical registry was supplied or searched.

### Rules

- Require both active status and signature.

### Assumptions

- The supplied synthetic snapshot and its explicit complete current population and rules are accepted for this audit; historical completeness is not assumed.

### Reasoning

- 1. A is active and signed in original line 9.
- 2. The biconditional at line 8 makes A eligible.

### Limits

- Only this supplied synthetic snapshot is audited; authenticity and actual historical events are not established.
- Initial fixture-familiar self-review was followed by a separate coordinator source-first/model review; both are nonblind.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `StockAudit.aEligible` in module `Stock.Audit` (supports): `Stock.eligible Stock.a`.
  [Model](models/Stock/Audit.lean) · [Executed check](checks/Target015.lean) · [Actual proof log](logs/target-015.log)

### Recommendation

Retain the scoped claim and its stated limits.

## C5

### Exact report claim

`input/report.md#P05`

> A signature alone is insufficient

### Verification question

Is signature alone insufficient for eligibility?

### Source evidence

- [input/sources/stock.html.md](input/sources/stock.html.md) — `scope`

> This is the complete current stock population: A, B and C. Quantities are exact whole units at this snapshot.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 6, "end_line": 6, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `release-rule`

> A row is eligible for release if and only if it is active and signed.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 8, "end_line": 8, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-b`

> B: status quarantined; quantity 27 units; signed yes.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 10, "end_line": 10, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.


### C5: criteria and report argument audit

Criteria origin: **inferred**. Scope: A/B/C at the 4 November 2026 snapshot; documentary historical knowledge only.

Is signature alone insufficient for eligibility?

- Decision criterion: Find an in-scope signed row that fails active status.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P05`:

> B is signed but quarantined.

Assessment: **verified**. This matches original line 10.

[evidence 2](input/sources/stock.html.md) at `row-b`

Report inference at `P05`:

> A signature alone is insufficient: B is signed but quarantined.

Assessment: **verified**. B fails the additional active condition, establishing insufficiency.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 1](input/sources/stock.html.md) at `release-rule`, [evidence 2](input/sources/stock.html.md) at `row-b`, [proof 0: StockAudit.signatureInsufficient](models/Stock/Audit.lean)

Independent audit reasoning:

- 1. B is signed but quarantined and belongs to the current population.
- 2. The release rule also requires active status.
- 3. B is an explicit counterexample to signature-only sufficiency; A eligibility remains true.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 1](input/sources/stock.html.md) at `release-rule`, [evidence 2](input/sources/stock.html.md) at `row-b`, [proof 0: StockAudit.signatureInsufficient](models/Stock/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: Use the finite source-linked stock model and exact target.

- Proof 0 source-to-target correspondence: B is an actual in-scope witness with signature but no eligibility. The existential insufficiency is represented by this explicit named witness, not an assertion about A being ineligible.

Declared bounded support search: Read all original HTML lines 1-14 and all six report paragraphs.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `title`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `h1`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `scope`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `count-rule`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `release-rule`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-a`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-b`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-c`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `history`.

3. B is an explicit counterexample to signature-only sufficiency; A eligibility remains true.

Search limits: No external source or historical registry was supplied or searched.

### Rules

- Find an in-scope signed row that fails active status.

### Assumptions

- The supplied synthetic snapshot and its explicit complete current population and rules are accepted for this audit; historical completeness is not assumed.

### Reasoning

- 1. B is signed but quarantined and belongs to the current population.
- 2. The release rule also requires active status.
- 3. B is an explicit counterexample to signature-only sufficiency; A eligibility remains true.

### Limits

- Only this supplied synthetic snapshot is audited; authenticity and actual historical events are not established.
- Initial fixture-familiar self-review was followed by a separate coordinator source-first/model review; both are nonblind.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `StockAudit.signatureInsufficient` in module `Stock.Audit` (supports): `Stock.b ∈ Stock.rows ∧ Stock.b.signed = true ∧ ¬ Stock.eligible Stock.b`.
  [Model](models/Stock/Audit.lean) · [Executed check](checks/Target016.lean) · [Actual proof log](logs/target-016.log)

### Recommendation

Retain the scoped claim and its stated limits.

## C6

### Exact report claim

`input/report.md#P06`

> No historical clearance records were supplied.

### Verification question

Were historical clearance records supplied in this dossier?

### Source evidence

- [input/sources/stock.html.md](input/sources/stock.html.md) — `history`

> This file contains no historical clearance records. It is not a history of clearance events.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 12, "end_line": 12, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.


### C6: criteria and report argument audit

Criteria origin: **inferred**. Scope: A/B/C at the 4 November 2026 snapshot; documentary historical knowledge only.

Were historical clearance records supplied in this dossier?

- Decision criterion: Inspect the entire supplied source inventory; do not infer absence of events.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **not_provided**.

Independent audit reasoning:

- 1. The only supplied source is the fully inspected 14-line HTML file.
- 2. Line 12 explicitly states no historical clearance records and disclaims an event history.
- 3. Documentary absence is supported; this does not establish event nonexistence.

[evidence 0](input/sources/stock.html.md) at `history`

Audited claim dependencies: None declared.

Formalization rationale: Documentary absence is established by inspecting the entire supplied file and its explicit disclaimer; Lean cannot certify that inspection.


Declared bounded support search: Read all original HTML lines 1-14 and all six report paragraphs.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `title`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `h1`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `scope`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `count-rule`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `release-rule`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-a`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-b`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-c`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `history`.

3. Documentary absence is supported; this does not establish event nonexistence.

Search limits: No external source or historical registry was supplied or searched.

### Rules

- Inspect the entire supplied source inventory; do not infer absence of events.

### Assumptions

- The supplied synthetic snapshot and its explicit complete current population and rules are accepted for this audit; historical completeness is not assumed.

### Reasoning

- 1. The only supplied source is the fully inspected 14-line HTML file.
- 2. Line 12 explicitly states no historical clearance records and disclaims an event history.
- 3. Documentary absence is supported; this does not establish event nonexistence.

### Limits

- Only this supplied synthetic snapshot is audited; authenticity and actual historical events are not established.
- Initial fixture-familiar self-review was followed by a separate coordinator source-first/model review; both are nonblind.

### Result

Semantic state: **supported**; argument status: **insufficient_support**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Retain the scoped claim and its stated limits.

## C7

### Exact report claim

`input/report.md#P06`

> the existence of a prior clearance is not established or refuted by this dossier.

### Verification question

Does this dossier leave prior-clearance existence unresolved?

### Source evidence

- [input/sources/stock.html.md](input/sources/stock.html.md) — `scope`

> This is the complete current stock population: A, B and C. Quantities are exact whole units at this snapshot.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 6, "end_line": 6, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `count-rule`

> Counted stock includes active and quarantined rows only; archived rows are excluded.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 7, "end_line": 7, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `release-rule`

> A row is eligible for release if and only if it is active and signed.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 8, "end_line": 8, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-a`

> A: status active; quantity 18 units; signed yes.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 9, "end_line": 9, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-b`

> B: status quarantined; quantity 27 units; signed yes.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 10, "end_line": 10, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-c`

> C: status archived; quantity 15 units; signed no.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 11, "end_line": 11, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `history`

> This file contains no historical clearance records. It is not a history of clearance events.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 12, "end_line": 12, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-fqfuxgg5", "extraction_bundle_sha256": "e06ea8aad7c99e47e75278c3a40a6efc6d5a902937c8834e98c761058ec3fa64", "extraction_reviewer": "Paired examples preparation agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.


### C7: criteria and report argument audit

Criteria origin: **inferred**. Scope: A/B/C at the 4 November 2026 snapshot; documentary historical knowledge only.

Does this dossier leave prior-clearance existence unresolved?

- Decision criterion: Keep current facts fixed and test opposite historical states.
- Decision criterion: Current population completeness does not imply historical event completeness.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `P06`:

> The source is not a history of clearance events

Assessment: **verified**. Original line 12 states this explicitly.

[evidence 6](input/sources/stock.html.md) at `history`

Report inference at `P06`:

> The source is not a history of clearance events, so the existence of a prior clearance is not established or refuted by this dossier.

Assessment: **verified**. Full-corpus inspection confirms no other rule constrains history; opposite witnesses justify the bounded conclusion.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 1](input/sources/stock.html.md) at `count-rule`, [evidence 2](input/sources/stock.html.md) at `release-rule`, [evidence 3](input/sources/stock.html.md) at `row-a`, [evidence 4](input/sources/stock.html.md) at `row-b`, [evidence 5](input/sources/stock.html.md) at `row-c`, [evidence 6](input/sources/stock.html.md) at `history`, [proof 0: StockAudit.historyUnderdetermined](models/Stock/Audit.lean)

Independent audit reasoning:

- 1. Current stock facts and rules do not constrain earlier clearance events; the source explicitly disclaims history.
- 2. The model fixes all recorded row data and permits the same current evidence with either historical Boolean value.
- 3. Both prior-clearance existence and nonexistence remain compatible; this supports the report epistemic conclusion, not either event claim.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 1](input/sources/stock.html.md) at `count-rule`, [evidence 2](input/sources/stock.html.md) at `release-rule`, [evidence 3](input/sources/stock.html.md) at `row-a`, [evidence 4](input/sources/stock.html.md) at `row-b`, [evidence 5](input/sources/stock.html.md) at `row-c`, [evidence 6](input/sources/stock.html.md) at `history`, [proof 0: StockAudit.historyUnderdetermined](models/Stock/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: Use the finite source-linked stock model and exact target.

- Proof 0 source-to-target correspondence: The historical Boolean true means prior clearance existed. All row constants and rules remain identical in both worlds, while currentEvidence checks their derived total and A eligibility. The target proves two compatible opposite historical states; it directly supports the epistemic claim under this declared complete reading, and establishes no historical event.

Declared bounded support search: Read all original HTML lines 1-14 and all six report paragraphs.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `title`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `h1`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `scope`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `count-rule`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `release-rule`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-a`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-b`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `row-c`.
- Inspected [input/sources/stock.html.md](input/sources/stock.html.md) at `history`.

3. Both prior-clearance existence and nonexistence remain compatible; this supports the report epistemic conclusion, not either event claim.

Search limits: No external source or historical registry was supplied or searched.

### Rules

- Keep current facts fixed and test opposite historical states.
- Current population completeness does not imply historical event completeness.

### Assumptions

- The supplied synthetic snapshot and its explicit complete current population and rules are accepted for this audit; historical completeness is not assumed.

### Reasoning

- 1. Current stock facts and rules do not constrain earlier clearance events; the source explicitly disclaims history.
- 2. The model fixes all recorded row data and permits the same current evidence with either historical Boolean value.
- 3. Both prior-clearance existence and nonexistence remain compatible; this supports the report epistemic conclusion, not either event claim.

### Limits

- Only this supplied synthetic snapshot is audited; authenticity and actual historical events are not established.
- Initial fixture-familiar self-review was followed by a separate coordinator source-first/model review; both are nonblind.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `StockAudit.historyUnderdetermined` in module `Stock.Audit` (supports): `EvidenceLogic.Underdetermined Stock.currentEvidence Stock.noPriorClearance`.
  [Model](models/Stock/Audit.lean) · [Executed check](checks/Target017.lean) · [Actual proof log](logs/target-017.log)

### Recommendation

Retain the scoped claim and its stated limits.
