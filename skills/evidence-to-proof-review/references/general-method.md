# General report-audit method

## Inputs and inferred criteria

The minimum input is a selected report and the authorized source set. A brief is optional. A dossier may contain heterogeneous or incomplete sources; process supported formats, record blocked extraction, and keep the audit scope explicit. There is no fixed number of documents or domain-specific claim template. Finite memory, time and proof budgets lead to retained, resumable work and declared partial coverage.

For every material finding, identify exactly what would make it true or false. Preserve quantifiers, population, time, units, attribution, relevant policy version and exceptions. Derive the question from the finding; derive applicable rules from the sources, an explicitly supplied criterion, or a declared mathematical definition. The report's assertion that a rule applies is itself reviewable. Do not silently import external law, a quality standard, causal assumptions, or a closed-world interpretation. If a necessary standard is missing, identify that missing definition; where useful give conditional results for named interpretations. Missing criteria on one claim must not stop other claims.

Review every extracted report passage, including introductions, tables, footnotes and conclusions. Classify non-claims with reasons. Split composite findings into atomic claims, retaining their exact report quotes and common source anchor. Premises and inference steps may appear elsewhere in the report: collect them in the corresponding argument audit and register independently material assertions as claims. A paragraph marked reviewed may still be misinterpreted by an agent; registration is a mechanical completeness control, not a semantic oracle.

## Two questions per claim

1. Does independent evidence in the supplied sources support or contradict the exact claim?
2. Are the report's own material premises, citations and inference steps valid?

These questions have separate outputs. A correct conclusion with an invalid argument remains supported with an argument defect. A real quote may be irrelevant, out of date, reversed, attributed to the wrong person, or outweighed by a scoped exception. A missing citation can be repaired by independent evidence without pretending the report already supplied it. An invalid inference can have a true conclusion; a countermodel to its premises proves that the argument does not entail the conclusion, not that the actual event did not occur.

Record exact report quotations for argument items, check source passages in context, and link evidence/proof references. Trace multi-claim dependencies and reject explicit cycles as independent support. Acyclic graphs may still contain an unsupported leaf; inspect every material premise. Never promote repeated claims from the report into independent source observations.

## Formalization is selected by the question

Use finite typed data and exhaustive checks for inventories, totals, membership and explicit counterexamples; exact arithmetic for quantities and units; predicates for conditions and exceptions; temporal relations and transitions for ordering and procedures; attributed records for testimony and narrative assertions; symbolic propositions and countermodels for inference validity. Combine these methods when needed. Do not flatten all document sentences into unquestioned axioms. Formalize the relevant source statements and their dependencies, preserving the rest in the searchable source ledger.

Each finding needs a formalization rationale, even when no proof is possible. Each proof needs a target-to-claim explanation and source-to-symbol mappings in model notes. Attempt support and refutation as appropriate; do not choose the direction only because it matches the report. A direct negative result needs a checked negation or an in-scope counterexample, not merely a failed positive proof. Non-vacuity checks and finite satisfying assignments help expose empty domains and inconsistent assumptions.

The shipped verifier uses pinned Lean 4.24.0 with Init/Std and an audited axiom policy. This is an implementation restriction, not a claim that other libraries or formalisms are inherently invalid. Complex analysis or specialized mathematical libraries may require an explicitly reviewed extension; until then report a blocked formalization or a smaller justified theorem. No custom theorem generator for each document domain is required: the coding agent authors the task's Lean model.

## Missing evidence is an output

An empty evidence list is valid when it honestly describes the outcome. Supply a bounded search record: the requested evidence, queries or manual inspection method, inspected source anchors, uninspected material, missing documents, and limits. A genuinely empty dossier may have no inspected anchors; state that explicitly. Never attach an irrelevant quote just to satisfy a schema.

Distinguish:

- Source evidence not found in the reviewed corpus.
- A missing material premise in the report's argument.
- Provable non-entailment in a stated model/rule system, for example two admissible assignments that agree with all premises but disagree on the claim.
- An actual source-backed refutation.

The first two do not imply the fourth. A proof about a finite ledger's entries does not establish that an unrecorded event never happened unless the ledger's completeness for that event class and time is explicitly justified.

## What the implementation enforces

New runs freeze contract version 2 in the input manifest. Every extracted report anchor must be reviewed; every registered atomic claim is audited exactly once or explicitly deferred. Unknown IDs, duplicates, changed claim quotes, unfinished classifications, unsupported source locations, missing criteria, malformed argument links, explicit dependency cycles and absent formalization rationales fail validation. Checked results bind to the final registry, findings, models, source manifest and review notes; changing them requires rechecking.

The verifier runs Lean, checks the exact declared target type and inspects theorem axioms. It validates literal quote locations and source hashes, not semantic entailment from a quotation. It accepts partial audits with visible deferred claims, and records nonformal or unresolved results without inventing proofs. Historical bundles remain reproducible as legacy audits and are explicitly labelled as lacking v2 registration/argument controls.

## Remaining judgment

An agent still interprets language, chooses material claims, searches the sources, defines the model and judges whether a citation supports a premise. Independent source reconstruction and adversarial review can catch mistakes but cannot eliminate them. Source authenticity, omitted real-world documents and all possible interpretations are outside Lean's guarantee. Unrestricted proof search may not terminate. These limits are disclosed per finding, not used to avoid the authorized audit.
