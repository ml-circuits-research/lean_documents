# Agent-native execution without the Python helpers

The reusable method requires a coding agent able to inspect/preserve documents and execute Lean. The bundled Python helpers, SQLite index, Poppler and Tesseract adapters are conveniences, not mandatory dependencies of the method. Use existing agent tools for reading, visual inspection, OCR, conversion, search, filesystem operations and hashing. Do not claim a converter or validator ran when it did not.

## Select and disclose the execution mode

- **Bundled helpers:** use the commands and contracts in this skill. Python and the appropriate optional adapters are needed for those commands. Their automated gates and logs establish only their actual executed scope.
- **Agent-native:** use the same evidence, argument and coverage obligations with the agent's available tools and a Lean project. Record `execution_mode: agent-native` in `run.json`, tool versions and which automated checks were not run. Do not label the Python v2 validator as passed. The Lean proof can still be checked, but registration, quote correspondence, target correspondence and provenance checks need recorded agent/reviewer inspection unless independently automated.

The mode distinction is part of the delivered assurance, not a reason to stop useful work when Python or an adapter is unavailable. Do not silently switch mode after a failed helper gate to conceal the failure: preserve the failure, repair the issue or explicitly narrow the guarantee.

## Portable procedure

1. Create a fresh retained workspace in the current project's `tmp/` (or the user's chosen work root). Preserve exact input bytes and record identities, versions and hashes using available agent tools. Keep original documents separate from extracted projections. A document-processing method can handle any readable format; report unreadable portions and missing coordinates instead of fabricating completeness.
2. Register report passages and material claims. Reconstruct source facts/rules, infer criteria and define verification methods using [facts and methods](facts-and-methods.md). Use the [v2 artifact contract](audit-contract-v2.md) where practical so downstream tooling can inspect the result. If an agent-native artifact differs, provide an explicit equivalent mapping and declare which helper checks cannot be applied.
3. Inspect `lean --version`. Pin the observed Lean toolchain for this run, including installed library versions if any. There is no global requirement to install a particular release just because the regression fixtures use it. A deliberate version mismatch remains an execution problem, not a semantic refutation.
4. Write reviewed Lean sources and source-to-symbol/model notes. Core Lean and locally reviewed definitions are sufficient for the generic method. If a specialized installed Lean library is useful, record exact imports, dependency revisions and axiom policy; do not silently rely on ambient unrecorded libraries. The bundled helper profile supports core and local modules, while broader dependency management is an explicitly reviewed agent-native project choice.
5. Run Lean on the actual sources. A single-file model needs only `lean Audit.lean`. With the standard Lean toolchain, Lake can build a multi-module project. Rebuild local compiled modules from reviewed sources rather than trusting pre-existing `.olean` files. Retain commands, standard output, standard error, exit status and actual version. No `sorry`, custom unapproved axioms or execution shortcuts replacing a kernel-checked proof.
6. For each referenced theorem, compile an additional exact-target assertion, not just a lookup of its name. In a single-file audit, place the following after the reviewed declarations; in a project, import the reviewed module in a separate check file:

```lean
-- Illustrative names: substitute the actual proposition and theorem.
example : IntendedProposition := Audit.checkedTheorem
#print axioms Audit.checkedTheorem
```

   Inspect reported dependencies against the declared axiom policy. Preserve that exact check source and its actual execution log. A theorem with a different conclusion, or with the desired conclusion assumed as a hypothesis, is not a successful audit. Common core axioms such as `propext`, `Classical.choice` and `Quot.sound` must still be disclosed.
7. Independently review the evidence-to-model and theorem-to-report correspondence when a separate reviewer is available. Recheck after changes. Produce one explained result per registered finding plus explicit deferrals, and separate original report argument defects from independently supported conclusions. Deliver the originals, extracted projections, facts/methods, models, exact-target checks, logs, dependency/version records, coverage, and review limits. Retain the working directory.

## Assurance record

Maintain the same [phase journal](phase-journal.md) using agent tools when Python is unavailable. Record each finding individually through registration, evidence, analysis, verification and verdict, with single-claim `claim_step` events and retained intermediate snapshots. Shared events do not replace those traces. Include a grounded `executive_summary` with conclusion, how_verified and limits for each finding. Disclose which mechanical profile gates were not executed. Record actual timestamps, claim links and exact artifact hashes at each action. Missing historical events remain unknown; never synthesize a completed phase from the existence of an output file.

A minimal execution record can state which checks were `executed`, `agent_reviewed`, `unavailable`, `failed` or `not_attempted`: Lean compilation, exact targets, axiom audit, source hashes, quote correspondence, claim-register reconciliation, source-to-model review, external dependency review, and independent review. Attach evidence for executed checks. Distinguish the real Lean success from agent-reviewed metadata; neither implies source authenticity.

For visual or unsupported document formats, [agent extraction import](agent-extraction.md) lets available agent tools produce projections that the bundled helpers can subsequently ingest. Choosing agent-native analysis does not require writing a new converter plugin or copying this repository's examples.
