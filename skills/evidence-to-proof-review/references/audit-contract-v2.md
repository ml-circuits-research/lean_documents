# Audit contract version 2

Version 2 makes declared report coverage, the report's own argument, and the auditor's independent verification separately inspectable. The immutable `input/audit-policy.json` selects this contract with `contract_version: 2`; `brief_origin` records `provided` or `inferred`. A separate brief is optional. Criteria may be inferred from each claim and its supplied sources. Missing definitions, reasonable alternative readings, and unresolved scope must be recorded rather than silently supplied.

This is a mechanical consistency contract. It cannot establish that the reviewer found every semantic claim, decomposed claims correctly, chose adequate criteria, performed the declared searches, or faithfully translated a source into Lean. Those questions require independent semantic review. A valid registration is not a certification of completeness or truth.

## Claim registration

`contracts.initialize(root)` writes `claims.json`, seeding **every report-ledger anchor as pending**. It does not infer which paragraphs contain claims. The reviewer changes each classification to `claims` or `non_claim` with a nonempty reason, and lists atomic claims separately. Retain the generated `report_sha256` values; they bind reviews to the current anchored report text.

Example after review (replace the placeholder hash with the generated value):

```json
{
  "schema_version": 2,
  "anchors": [
    {
      "report_anchor": "R1",
      "report_sha256": "COPY_THE_VALUE_FROM_INITIALIZE",
      "classification": "claims",
      "reason": "The paragraph asserts an arithmetic total."
    }
  ],
  "claims": [
    {
      "claim_id": "C1",
      "report_anchor": "R1",
      "report_quote": "The total is three.",
      "disposition": "audited"
    }
  ]
}
```

A claim quote must be an exact, nonempty substring of the indicated report passage. A finding must reproduce its registered quote and anchor exactly; selecting a different substring is rejected. Every `claims` anchor needs at least one registered claim, and every registered `audited` claim needs exactly one finding. Findings for unknown, duplicate, or deferred IDs are rejected. `non_claim` anchors cannot own registered claims.

For a claim outside the completed work, set `disposition` to `deferred` and add `reason`. Do not create a finding for it. It remains visible in coverage, and the result is labelled `partial`. Even a run with zero deferred claims is labelled `complete_registration`, not semantically complete. An all-deferred batch or a report with no registered claims may have an empty findings list; callers must preserve this distinction.

Repeated initialization preserves reviews on unchanged anchors. New or changed anchors become pending; changed reviews are retained under `previous_review`. Removed reviews move to `retired_anchors`. Claims are preserved so reviewers must explicitly reconcile stale claims. Initialization never silently approves new material or deletes prior claim decisions.

## Finding extensions

The existing finding fields remain required, including exact claim, verification question, evidence, rules, assumptions, reasoning, semantic state, argument status, formal status, proof references, limits, and recommendation. Add the following fields. This complete extension example applies to a report that states the conclusion but provides no argument; the independent source records amounts one and two.

```json
{
  "criteria": {
    "origin": "inferred",
    "operational_question": "Does the reported total equal the sum of the supplied amounts?",
    "decision_criteria": ["Add each recorded amount once and compare with three."],
    "scope": "The two amounts in the supplied ledger; no other transactions.",
    "missing_definitions": [],
    "alternatives": []
  },
  "argument_audit": {
    "outcome": "not_provided",
    "report_items": [],
    "independent_reasoning": ["The source records one and two. Their sum is three; the report itself supplies no derivation."],
    "evidence_refs": [0],
    "proof_refs": [],
    "claim_dependencies": []
  },
  "formalization": {
    "rationale": "Documentary verification only in this batch; no Lean execution is claimed.",
    "correspondence": []
  },
  "support_search": {
    "scope": "Read the supplied ledger passage L1 and the report paragraph R1.",
    "queries": ["total", "sum"],
    "inspected": [{"path": "input/sources/ledger.md", "anchor": "L1"}],
    "limitations": ["No external materials or unprovided transactions were searched."],
    "conclusion": "Independent evidence supports the total, but the report supplies no explicit argument."
  }
}
```

Here the base finding has `argument_status: "insufficient_support"`, `semantic_state: "supported"`, `formal_status: "not_attempted"`, `proofs: []`, and evidence index 0 identifies the quoted ledger passage. Insufficient report justification does not refute the underlying conclusion.

Criteria require `origin` (`inferred`, `provided`, or `source`), an operational question, at least one decision criterion, scope, and explicit lists of missing definitions and alternatives. The last two lists may be empty. Explain source-derived or supplied criteria in the finding's evidence, rules, and reasoning. The contract deliberately does not prescribe a domain-specific method or force formalization where terms or evidence are inadequate.

## Report argument audit

`argument_audit.outcome` is one of `sufficient`, `insufficient`, `invalid`, `unsound`, `disputed`, `nonformal`, or `not_provided`. It describes the justification supplied **by the report**, independently of whether the auditor can substantiate the conclusion. Its required `independent_reasoning` explains that assessment using the supplied sources and any formal results.

The existing `argument_status` maps `insufficient` and `not_provided` to `insufficient_support`, `invalid` to `invalid_inference`, and `unsound` to `unsound_argument`; other values map identically. Inconsistent statuses are rejected. Use `unsound` when a material offered premise or rule is contradicted, even if the inference form is valid and the conclusion independently supported. This outcome requires a quoted `premise` assessed as `contradicted` with evidence or proof references. Use `invalid` for an inference that fails to follow from its premises; if both defects occur, explain both and classify each report item. An unsupported premise alone warrants insufficient support, not a false-premise verdict.

For any outcome other than `not_provided`, quote the report premises, citations, or inferences being audited in `report_items`. A report item looks like:

```json
{
  "kind": "inference",
  "report_anchor": "R1",
  "report_quote": "One plus two is three.",
  "assessment": "verified",
  "reasoning": "The source amounts match the stated operands and the arithmetic is valid.",
  "evidence_refs": [0],
  "proof_refs": [0]
}
```

`kind` is `premise`, `citation`, or `inference`; `assessment` is `verified`, `unsupported`, `contradicted`, `disputed`, or `nonformal`. Every item needs independent reasoning and an exact anchored report quote. Fabricated quotes are rejected. For citations, quote the actual citation text in the report and link the checked source passage through `evidence_refs`; explain mismatches, missing sources, or scope limitations. Merely repeating the report's conclusion is not sufficient justification.

All `evidence_refs` and `proof_refs` are zero-based indexes into the **same finding's** evidence and proof arrays. They must exist and be distinct within each list. Empty reference lists are permitted when no such artifact exists; reasoning must state what can and cannot be established. Links are rendered for both individual report items and independent argument reasoning. `not_provided` requires an empty `report_items` list and an explanation; do not fabricate premises to fill the schema.

`claim_dependencies` lists other audited claim IDs used as independently established premises. Deferred and unknown dependencies, self-dependencies, and cycles are rejected. These checks address explicitly declared dependencies; they cannot detect undeclared circular reasoning in prose, duplicated source material, or all implicit dependence. Independent source evidence and inspected passages must use paths under `input/sources/`. The report and audit brief cannot supply independent evidence for a report conclusion.

## Formalization and actual execution

Each finding requires `formalization.rationale`: explain the chosen formal method, why a meaningful proof attempt is blocked or omitted, or why the existing proof targets represent the question. Existing `formal_status` records the finding's formal disposition; only actual `proof-results.json` and retained proof logs establish execution.

Every listed proof, including auxiliary proofs, requires exactly one entry in `formalization.correspondence`:

```json
{
  "proof_ref": 0,
  "explanation": "The source's two amounts are represented as natural numbers one and two, each counted once. The target (1 + 2 : Nat) = 3 checks their sum. It assumes faithful transcription and does not establish source authenticity."
}
```

Existing proof references retain module, theorem, relation, and exact target. The correspondence explanation must connect source values and applicable rules to that target, state assumptions, and explain limits. Contract validation checks the presence and references of this explanation, not its truth. Actual Lean execution and independent semantic review are separate requirements.

## Bounded support searches and empty evidence

A `support_search` is required when the argument outcome is `insufficient` or `not_provided`, when the semantic state is `undetermined`, or when the independent evidence array is empty. Otherwise it is optional, but validated when supplied.

Record the scope, queries, inspected source paths and anchors, at least one limitation, and conclusion. `queries` may be empty for direct reading. Each inspected passage must exist in the supplied corpus. This verifies that inspection references are real; it does not establish that the reviewer performed the inspection. Do not list merely discovered search hits as inspected passages.

An empty evidence array is valid for a real absence of independent support; do not invent evidence. Inspected passages can document the bounded search even when none supports the claim. If no passage could be inspected, use `inspected: []` and give a nonempty `uninspected_reason`, for example that source extraction is blocked. Keep the resulting conclusion bounded: failure to find support is not proof of falsity, and lack of accessible material is not a completed substantive search.

## Integration API

```python
import contracts

registry = contracts.initialize(root)
coverage = contracts.validate(root, findings)
markdown_lines = contracts.render(root, findings)
```

- `initialize(root)` creates or synchronizes `claims.json` and returns its object. Invoke it after preparing the report ledger and after resumed extraction changes the report ledger.
- `validate(root, findings, source_lookup=None)` returns coverage metadata or raises `ValueError`. Metadata includes `contract_version`, `report_anchors`, `claim_anchors`, `non_claim_anchors`, `registered_claims`, `audited_claims`, `deferred_claims`, `coverage`, and `limitation`.
- `source_lookup(path, anchor)` is an optional callback returning source passage text, a dictionary containing `quote`, or `None`. Without it, the validator uses the indexed corpus if present, otherwise the legacy source ledger. Source evidence quotes and inspection references are checked through this resolver.
- `render(root, findings)` validates again and returns Markdown lines covering registration, deferred claims, criteria, report arguments, independent reasoning, formalization correspondence, and bounded searches.

The caller verifies immutable manifests first, selects this contract using the immutable policy, validates existing base finding fields, checks actual Lean execution, and includes `claims.json` in the checked snapshot. For policy version 2, allow empty evidence arrays and empty findings lists when explicit registration explains coverage. Do not reinterpret historic audits as version 2: retain their original artifacts and label their legacy profile explicitly. The v2 validator intentionally does not silently migrate legacy claims or invent retrospective argument audits.

A supported or refuted substantive verdict with no cited source evidence requires a direct proof (for example pure arithmetic or an explicitly justified empty-evidence model); an empty search alone cannot establish either verdict. Byte-identical copies of the selected report cannot be used as independent sources, including renamed copies. After changed ingestion, the previous semantic review is archived and must be renewed. Search dependencies and transitive claim dependencies participate in revision invalidation.
