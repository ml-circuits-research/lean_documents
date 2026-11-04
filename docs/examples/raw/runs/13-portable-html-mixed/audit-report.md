# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

## Registered claim coverage

Coverage: **complete_registration**; 5 reviewed anchors; 4 audited and 0 deferred claims.

Registration reconciles declared claims and reviewed report anchors; it does not establish semantic completeness, faithful decomposition, or that declared searches were actually performed.

- `R1`: claims — One principal atomic conclusion is registered; its material premises and inference are separately covered in argument_audit.report_items.
- `R2`: claims — One principal atomic conclusion is registered; its material premises and inference are separately covered in argument_audit.report_items.
- `R3`: claims — One principal atomic conclusion is registered; its material premises and inference are separately covered in argument_audit.report_items.
- `R4`: claims — One principal atomic conclusion is registered; its material premises and inference are separately covered in argument_audit.report_items.
- `document-preamble`: non_claim — The title identifies the report and makes no substantive stock or historical assertion.
[Semantic correspondence review](semantic-review.md)

Extraction inventory: 2 documents; 0 pending, partial or blocked. See [ingestion details](ingestion.json) and [coverage](coverage.md).

## C1

### Exact report claim

`input/report.md#R1`

> Counted stock is 45 units.

### Verification question

Does the current source-defined counted stock total exactly 45 whole units?

### Source evidence

- [input/sources/stock.html.md](input/sources/stock.html.md) — `scope`

> This is the complete current stock population: A, B and C. Quantities are exact whole units at this snapshot.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 6, "end_line": 6, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `count-rule`

> Counted stock includes active and quarantined rows only; archived rows are excluded.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 7, "end_line": 7, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-a`

> A: status active; quantity 18 units; signed yes.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 9, "end_line": 9, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-b`

> B: status quarantined; quantity 27 units; signed yes.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 10, "end_line": 10, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-c`

> C: status archived; quantity 15 units; signed no.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 11, "end_line": 11, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.


### C1: criteria and report argument audit

Criteria origin: **inferred**. Scope: The complete current A/B/C population at 4 November 2026; historical event existence is assessed only for what this corpus can establish.

Does the current source-defined counted stock total exactly 45 whole units?

- Decision criterion: Include each active or quarantined row once and exclude archived rows.
- Decision criterion: Sum the exact in-scope quantities and compare with 45.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report premise at `R1`:

> The rule counts active or quarantined stock

Assessment: **verified**. This matches original line 7; archived C is excluded.

[evidence 1](input/sources/stock.html.md) at `count-rule`, [evidence 4](input/sources/stock.html.md) at `row-c`

Report premise at `R1`:

> A contributes 18 and B contributes 27

Assessment: **verified**. The row statuses make both included, and their exact quantities match original lines 9 and 10.

[evidence 1](input/sources/stock.html.md) at `count-rule`, [evidence 2](input/sources/stock.html.md) at `row-a`, [evidence 3](input/sources/stock.html.md) at `row-b`

Report inference at `R1`:

> so 18 + 27 = 45.

Assessment: **verified**. The stated operands are exactly the in-scope rows; the checked filtered total establishes this arithmetic.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 1](input/sources/stock.html.md) at `count-rule`, [evidence 2](input/sources/stock.html.md) at `row-a`, [evidence 3](input/sources/stock.html.md) at `row-b`, [evidence 4](input/sources/stock.html.md) at `row-c`, [proof 0: StockAudit.counted45](models/Stock/Audit.lean)

Independent audit reasoning:

- 1. The current complete population is A, B and C; A is active, B quarantined and C archived.
- 2. The rule includes A and B and excludes C, so the relevant quantities are 18 and 27.
- 3. Their exact sum is 45, and the report states the same rule and operands; its conclusion and stated arithmetic argument are supported.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 1](input/sources/stock.html.md) at `count-rule`, [evidence 2](input/sources/stock.html.md) at `row-a`, [evidence 3](input/sources/stock.html.md) at `row-b`, [evidence 4](input/sources/stock.html.md) at `row-c`, [proof 0: StockAudit.counted45](models/Stock/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: Use exact finite arithmetic, row predicates and a separate countermodel where indicated; proof targets represent only the source-linked scoped obligations.

- Proof 0 source-to-target correspondence: Stock.rows represents the complete source population, Stock.counted implements the status rule, and Stock.total sums only A=18 and B=27. The equality is the exact 45-unit claim, conditional on source fidelity.

Declared bounded support search: Read the complete supplied HTML, original lines 1-14, and every report paragraph; no other source was supplied.

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

3. Their exact sum is 45, and the report states the same rule and operands; its conclusion and stated arithmetic argument are supported.

Search limits: A complete supplied file inventory and current stock population do not establish a complete historical event history. No external source was searched.

### Rules

- Include each active or quarantined row once and exclude archived rows.
- Sum the exact in-scope quantities and compare with 45.

### Assumptions

- The supplied register is faithfully transcribed and its stated current-population completeness and rules are accepted for this scoped audit. No historical completeness is assumed.

### Reasoning

- 1. The current complete population is A, B and C; A is active, B quarantined and C archived.
- 2. The rule includes A and B and excludes C, so the relevant quantities are 18 and 27.
- 3. Their exact sum is 45, and the report states the same rule and operands; its conclusion and stated arithmetic argument are supported.

### Limits

- The synthetic supplied source is not authenticated. The model checks the stated snapshot and rules; it does not establish real-world operational permission or historical events.
- A separate coordinator completed source-first and model correspondence review, but knew the synthetic fixture design; this is not a blind benchmark or domain-expert certification.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `StockAudit.counted45` in module `Stock.Audit` (supports): `Stock.total = 45`.
  [Model](models/Stock/Audit.lean) · [Executed check](checks/Target012.lean) · [Actual proof log](logs/target-012.log)

### Recommendation

Retain the 45-unit total with the source-defined inclusion rule.

## C2

### Exact report claim

`input/report.md#R2`

> Counted stock is 60 units.

### Verification question

Does the current source-defined counted stock total 60 whole units?

### Source evidence

- [input/sources/stock.html.md](input/sources/stock.html.md) — `scope`

> This is the complete current stock population: A, B and C. Quantities are exact whole units at this snapshot.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 6, "end_line": 6, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `count-rule`

> Counted stock includes active and quarantined rows only; archived rows are excluded.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 7, "end_line": 7, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-a`

> A: status active; quantity 18 units; signed yes.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 9, "end_line": 9, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-b`

> B: status quarantined; quantity 27 units; signed yes.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 10, "end_line": 10, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-c`

> C: status archived; quantity 15 units; signed no.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 11, "end_line": 11, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.


### C2: criteria and report argument audit

Criteria origin: **inferred**. Scope: The complete current A/B/C population at 4 November 2026; historical event existence is assessed only for what this corpus can establish.

Does the current source-defined counted stock total 60 whole units?

- Decision criterion: Apply the counted-status filter before summing; archived stock is excluded.
- Decision criterion: Distinguish the arithmetic total of all rows from the total of counted rows.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **unsound**.

Report premise at `R2`:

> All three rows contribute

Assessment: **contradicted**. Archived C does not contribute under the counted-stock rule; it is in the table but outside the counted set.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 1](input/sources/stock.html.md) at `count-rule`, [evidence 4](input/sources/stock.html.md) at `row-c`, [proof 2: StockAudit.archivedExcluded](models/Stock/Audit.lean)

Report inference at `R2`:

> 18 + 27 + 15 = 60.

Assessment: **verified**. The all-row arithmetic is correct, although applying that sum to counted stock is invalid.

[evidence 2](input/sources/stock.html.md) at `row-a`, [evidence 3](input/sources/stock.html.md) at `row-b`, [evidence 4](input/sources/stock.html.md) at `row-c`, [proof 1: StockAudit.allRows60](models/Stock/Audit.lean)

Independent audit reasoning:

- 1. The all-row quantities do sum to 60, so the addition itself is not the error.
- 2. The report includes archived C=15 despite the explicit exclusion rule; C is not in the counted set.
- 3. The source-defined counted total is 45, which differs from 60; the exact claim is false within this snapshot model. The offered inclusion premise is false; its arithmetic is valid, but the argument is unsound.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 1](input/sources/stock.html.md) at `count-rule`, [evidence 2](input/sources/stock.html.md) at `row-a`, [evidence 3](input/sources/stock.html.md) at `row-b`, [evidence 4](input/sources/stock.html.md) at `row-c`, [proof 0: StockAudit.notCounted60](models/Stock/Audit.lean), [proof 1: StockAudit.allRows60](models/Stock/Audit.lean), [proof 2: StockAudit.archivedExcluded](models/Stock/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: Use exact finite arithmetic, row predicates and a separate countermodel where indicated; proof targets represent only the source-linked scoped obligations.

- Proof 0 source-to-target correspondence: The target negates the exact claimed counted total after applying original line 7 to the current rows. It refutes this modelled claim, not the faithful addition of all source quantities.
- Proof 1 source-to-target correspondence: This unfiltered sum verifies the author arithmetic separately; it is auxiliary and does not support the counted-stock conclusion.
- Proof 2 source-to-target correspondence: C is archived at original line 11 and excluded by original line 7; this isolates the unsupported inclusion premise.

Declared bounded support search: Read the complete supplied HTML, original lines 1-14, and every report paragraph; no other source was supplied.

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

3. The source-defined counted total is 45, which differs from 60; the exact claim is false within this snapshot model. The offered inclusion premise is false; its arithmetic is valid, but the argument is unsound.

Search limits: A complete supplied file inventory and current stock population do not establish a complete historical event history. No external source was searched.

### Rules

- Apply the counted-status filter before summing; archived stock is excluded.
- Distinguish the arithmetic total of all rows from the total of counted rows.

### Assumptions

- The supplied register is faithfully transcribed and its stated current-population completeness and rules are accepted for this scoped audit. No historical completeness is assumed.

### Reasoning

- 1. The all-row quantities do sum to 60, so the addition itself is not the error.
- 2. The report includes archived C=15 despite the explicit exclusion rule; C is not in the counted set.
- 3. The source-defined counted total is 45, which differs from 60; the exact claim is false within this snapshot model. The offered inclusion premise is false; its arithmetic is valid, but the argument is unsound.

### Limits

- The synthetic supplied source is not authenticated. The model checks the stated snapshot and rules; it does not establish real-world operational permission or historical events.
- A separate coordinator completed source-first and model correspondence review, but knew the synthetic fixture design; this is not a blind benchmark or domain-expert certification.

### Result

Semantic state: **refuted**; argument status: **unsound_argument**; formal status: **refuted**.

### Formal evidence

- `StockAudit.notCounted60` in module `Stock.Audit` (refutes): `Stock.total ≠ 60`.
  [Model](models/Stock/Audit.lean) · [Executed check](checks/Target013.lean) · [Actual proof log](logs/target-013.log)

- `StockAudit.allRows60` in module `Stock.Audit` (auxiliary): `(Stock.rows.map Stock.Row.quantity).sum = 60`.
  [Model](models/Stock/Audit.lean) · [Executed check](checks/Target014.lean) · [Actual proof log](logs/target-014.log)

- `StockAudit.archivedExcluded` in module `Stock.Audit` (auxiliary): `Stock.counted Stock.c = false`.
  [Model](models/Stock/Audit.lean) · [Executed check](checks/Target015.lean) · [Actual proof log](logs/target-015.log)

### Recommendation

Replace 60 with 45 for counted stock; 60 may be labelled as the total of all recorded statuses.

## C3

### Exact report claim

`input/report.md#R3`

> A is eligible for release.

### Verification question

Does A meet the source release criterion, and does a signature alone justify that conclusion?

### Source evidence

- [input/sources/stock.html.md](input/sources/stock.html.md) — `scope`

> This is the complete current stock population: A, B and C. Quantities are exact whole units at this snapshot.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 6, "end_line": 6, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `release-rule`

> A row is eligible for release if and only if it is active and signed.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 8, "end_line": 8, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-a`

> A: status active; quantity 18 units; signed yes.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 9, "end_line": 9, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-b`

> B: status quarantined; quantity 27 units; signed yes.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 10, "end_line": 10, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.


### C3: criteria and report argument audit

Criteria origin: **inferred**. Scope: The complete current A/B/C population at 4 November 2026; historical event existence is assessed only for what this corpus can establish.

Does A meet the source release criterion, and does a signature alone justify that conclusion?

- Decision criterion: Release eligibility holds exactly when the row is active AND signed.
- Decision criterion: Test A against both conditions, then test the report signature-only implication separately.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **unsound**.

Report premise at `R3`:

> A is signed

Assessment: **verified**. The A row states signed yes.

[evidence 2](input/sources/stock.html.md) at `row-a`

Report premise at `R3`:

> a signature alone is sufficient for release.

Assessment: **contradicted**. The source requires active status as well; B is signed yet fails eligibility. The general sufficiency rule is false in the supplied population.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 1](input/sources/stock.html.md) at `release-rule`, [evidence 3](input/sources/stock.html.md) at `row-b`, [proof 1: StockAudit.signatureInsufficient](models/Stock/Audit.lean)

Independent audit reasoning:

- 1. A is active and signed, so independent source evidence satisfies both release conditions.
- 2. The report verifies only A signature and then asserts a signature-only rule, omitting active status.
- 3. B is an in-scope signed quarantined row and therefore not eligible; it is a counterexample to the proposed signature-only rule.
- 4. A eligibility remains supported. The author justification is unsound because its sufficient-condition premise is false; the inference form would be valid if that premise were true. The counterexample does not refute A eligibility.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 1](input/sources/stock.html.md) at `release-rule`, [evidence 2](input/sources/stock.html.md) at `row-a`, [evidence 3](input/sources/stock.html.md) at `row-b`, [proof 0: StockAudit.aEligible](models/Stock/Audit.lean), [proof 1: StockAudit.signatureInsufficient](models/Stock/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: Use exact finite arithmetic, row predicates and a separate countermodel where indicated; proof targets represent only the source-linked scoped obligations.

- Proof 0 source-to-target correspondence: A has active status and signed yes at original line 9. Stock.eligible encodes the biconditional at line 8, and the theorem establishes both conditions for A.
- Proof 1 source-to-target correspondence: B is an actual member of the current population, signed yes but quarantined. This is a witness against signature-only sufficiency, not a refutation of A release eligibility.

Declared bounded support search: Read the complete supplied HTML, original lines 1-14, and every report paragraph; no other source was supplied.

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

4. A eligibility remains supported. The author justification is unsound because its sufficient-condition premise is false; the inference form would be valid if that premise were true. The counterexample does not refute A eligibility.

Search limits: A complete supplied file inventory and current stock population do not establish a complete historical event history. No external source was searched.

### Rules

- Release eligibility holds exactly when the row is active AND signed.
- Test A against both conditions, then test the report signature-only implication separately.

### Assumptions

- The supplied register is faithfully transcribed and its stated current-population completeness and rules are accepted for this scoped audit. No historical completeness is assumed.

### Reasoning

- 1. A is active and signed, so independent source evidence satisfies both release conditions.
- 2. The report verifies only A signature and then asserts a signature-only rule, omitting active status.
- 3. B is an in-scope signed quarantined row and therefore not eligible; it is a counterexample to the proposed signature-only rule.
- 4. A eligibility remains supported. The author justification is unsound because its sufficient-condition premise is false; the inference form would be valid if that premise were true. The counterexample does not refute A eligibility.

### Limits

- The synthetic supplied source is not authenticated. The model checks the stated snapshot and rules; it does not establish real-world operational permission or historical events.
- A separate coordinator completed source-first and model correspondence review, but knew the synthetic fixture design; this is not a blind benchmark or domain-expert certification.

### Result

Semantic state: **supported**; argument status: **unsound_argument**; formal status: **proved**.

### Formal evidence

- `StockAudit.aEligible` in module `Stock.Audit` (supports): `Stock.eligible Stock.a`.
  [Model](models/Stock/Audit.lean) · [Executed check](checks/Target016.lean) · [Actual proof log](logs/target-016.log)

- `StockAudit.signatureInsufficient` in module `Stock.Audit` (auxiliary): `Stock.b ∈ Stock.rows ∧ Stock.b.signed = true ∧ ¬ Stock.eligible Stock.b`.
  [Model](models/Stock/Audit.lean) · [Executed check](checks/Target017.lean) · [Actual proof log](logs/target-017.log)

### Recommendation

Retain A eligibility but replace the signature-only explanation with the two verified conditions: active and signed.

## C4

### Exact report claim

`input/report.md#R4`

> A never received prior clearance.

### Verification question

Does the absence of supplied historical records establish that A never received earlier clearance?

### Source evidence

- [input/sources/stock.html.md](input/sources/stock.html.md) — `scope`

> This is the complete current stock population: A, B and C. Quantities are exact whole units at this snapshot.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 6, "end_line": 6, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `count-rule`

> Counted stock includes active and quarantined rows only; archived rows are excluded.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 7, "end_line": 7, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `release-rule`

> A row is eligible for release if and only if it is active and signed.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 8, "end_line": 8, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-a`

> A: status active; quantity 18 units; signed yes.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 9, "end_line": 9, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-b`

> B: status quarantined; quantity 27 units; signed yes.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 10, "end_line": 10, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `row-c`

> C: status archived; quantity 15 units; signed no.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 11, "end_line": 11, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.

- [input/sources/stock.html.md](input/sources/stock.html.md) — `history`

> This file contains no historical clearance records. It is not a history of clearance events.

Original: [input/originals/D00002.html](input/originals/D00002.html); extraction: agent-extraction.
Coordinates: `{"kind": "line", "start_line": 12, "end_line": 12, "original": "input/originals/D00002.html", "original_sha256": "49335a218d26cb5c9a79726b21c1565eb5f5318821add20f66c1e7e4dcac7c55", "artifact_directory": "extraction/D00002/agent-attempt-xz03otnd", "extraction_bundle_sha256": "883ad822a2df572cd0b90ffba73cf4c58d5b3ce48df3e31a4e52e5f28fb36622", "extraction_reviewer": "Portability audit agent", "coordinate_interpretation": "Declared original-source coordinates; fidelity requires original-source inspection."}`.

Extraction uncertainty: Agent-produced transcription and original coordinates require explicit material inspection of the original source before a direct formal verdict. Import validation does not establish fidelity, authenticity, semantic completeness, or truth.


### C4: criteria and report argument audit

Criteria origin: **inferred**. Scope: The complete current A/B/C population at 4 November 2026; historical event existence is assessed only for what this corpus can establish.

Does the absence of supplied historical records establish that A never received earlier clearance?

- Decision criterion: Treat the current population completeness statement as current-only.
- Decision criterion: Require historical event evidence or a justified complete historical registry before concluding no earlier clearance existed.
- Decision criterion: Test whether opposite historical states remain consistent with every current source fact.

Missing definitions: No complete historical clearance registry or historical rule linking events to this snapshot is supplied.

Alternatives: Interpreting absence as absence of supplied documentation would be a narrower supported statement, but the report asserts nonexistence of events.

Report justification outcome: **invalid**.

Report premise at `R4`:

> No historical clearance record was supplied

Assessment: **verified**. The entire supplied source was inspected; line 12 explicitly states this limited absence of documentation. The report is not independent history evidence.

[evidence 6](input/sources/stock.html.md) at `history`

Report inference at `R4`:

> No historical clearance record was supplied, so no earlier clearance existed.

Assessment: **unsupported**. No complete historical registry or rule connecting absence of supplied records to absence of events is supplied. The checked countermodel invalidates the implication; it does not contradict the actual historical conclusion.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 6](input/sources/stock.html.md) at `history`, [proof 0: StockAudit.historyUnderdetermined](models/Stock/Audit.lean), [proof 1: StockAudit.noHistoricalEntailment](models/Stock/Audit.lean)

Independent audit reasoning:

- 1. Full reading confirms that no historical clearance record is supplied; the source explicitly disclaims an event history.
- 2. Current-stock completeness does not state historical-clearance completeness and imposes no condition linking current status to earlier events.
- 3. Two models retain the identical current facts but assign opposite truth values to whether a prior clearance occurred; neither documentary support nor refutation of the historical event claim follows.
- 4. The missing historical premise is a support gap. The report absence-to-nonexistence inference is invalid, but the underlying historical claim remains undetermined rather than false.

[evidence 0](input/sources/stock.html.md) at `scope`, [evidence 1](input/sources/stock.html.md) at `count-rule`, [evidence 2](input/sources/stock.html.md) at `release-rule`, [evidence 3](input/sources/stock.html.md) at `row-a`, [evidence 4](input/sources/stock.html.md) at `row-b`, [evidence 5](input/sources/stock.html.md) at `row-c`, [evidence 6](input/sources/stock.html.md) at `history`, [proof 0: StockAudit.historyUnderdetermined](models/Stock/Audit.lean), [proof 1: StockAudit.noHistoricalEntailment](models/Stock/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: Use a bounded full-corpus search plus two explicitly consistent historical assignments to prove non-entailment. Only auxiliary proof status is justified because no historical event truth is established.

- Proof 0 source-to-target correspondence: The fixed current facts constrain neither historical Boolean value. Both witnesses satisfy the same current model; one has no prior clearance and the other has a prior clearance. This is formal underdetermination in the declared model, not proof that either historical event occurred.
- Proof 1 source-to-target correspondence: The true-history witness satisfies the current evidence but falsifies no-prior-clearance, showing that the documentary model does not entail the historical negation. Source-to-model adequacy and real history remain outside the kernel proof.

Declared bounded support search: Read the complete supplied HTML, original lines 1-14, and every report paragraph; no other source was supplied.

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

4. The missing historical premise is a support gap. The report absence-to-nonexistence inference is invalid, but the underlying historical claim remains undetermined rather than false.

Search limits: A complete supplied file inventory and current stock population do not establish a complete historical event history. No external source was searched.

### Rules

- Treat the current population completeness statement as current-only.
- Require historical event evidence or a justified complete historical registry before concluding no earlier clearance existed.
- Test whether opposite historical states remain consistent with every current source fact.

### Assumptions

- The supplied register is faithfully transcribed and its stated current-population completeness and rules are accepted for this scoped audit. No historical completeness is assumed.

### Reasoning

- 1. Full reading confirms that no historical clearance record is supplied; the source explicitly disclaims an event history.
- 2. Current-stock completeness does not state historical-clearance completeness and imposes no condition linking current status to earlier events.
- 3. Two models retain the identical current facts but assign opposite truth values to whether a prior clearance occurred; neither documentary support nor refutation of the historical event claim follows.
- 4. The missing historical premise is a support gap. The report absence-to-nonexistence inference is invalid, but the underlying historical claim remains undetermined rather than false.

### Limits

- The synthetic supplied source is not authenticated. The model checks the stated snapshot and rules; it does not establish real-world operational permission or historical events.
- A separate coordinator completed source-first and model correspondence review, but knew the synthetic fixture design; this is not a blind benchmark or domain-expert certification.

### Result

Semantic state: **undetermined**; argument status: **invalid_inference**; formal status: **auxiliary**.

### Formal evidence

- `StockAudit.historyUnderdetermined` in module `Stock.Audit` (auxiliary): `EvidenceLogic.Underdetermined Stock.currentEvidence Stock.noPriorClearance`.
  [Model](models/Stock/Audit.lean) · [Executed check](checks/Target018.lean) · [Actual proof log](logs/target-018.log)

- `StockAudit.noHistoricalEntailment` in module `Stock.Audit` (auxiliary): `¬ EvidenceLogic.Entails Stock.currentEvidence Stock.noPriorClearance`.
  [Model](models/Stock/Audit.lean) · [Executed check](checks/Target019.lean) · [Actual proof log](logs/target-019.log)

### Recommendation

Replace the event claim with the bounded statement that no historical record was supplied, or obtain an authoritative historical registry with a justified completeness scope.
