# Evaluator-only expectations

Do not include this directory in an auditing agent's input workspace. The auditor must receive the selected report and its source documents; it must not receive the expected verdicts before deriving its own assessment.

The five JSON files contain editorial expectations for both report variants. These are provisional test targets, not Lean results, and have not been certified by a domain expert. The current independent fixture review provides a separate semantic check; disagreement with an expectation must be investigated rather than automatically scored as an agent error.

The common expectation vocabulary is:

- `semantic_state`: `supported`, `refuted`, `both`, `undetermined`, or `not_applicable`.
- `prospective_disposition`: `proof`, `refutation`, `blocked`, or `nonformal`.

`proof` means a candidate for future formalization, not a completed proof. `blocked` includes evidence gaps; it does not mean that no useful documentary audit can be delivered. A supported statement about missing evidence does not establish the missing event's presence or absence.

These fixture expectations predate the final runtime schema. Production output will additionally separate evidence state, argument sufficiency, formal result, semantic review, and coverage, as described in [the architecture](../../docs/architecture.html). Every future audit must explain its evidence and reasoning, including why a refutation works or why support is insufficient.

Run each variant independently, compare only afterward, and retain the claim-level explanations and any reproducible proof artifacts. Five dossiers are a seed regression set, not a statistically validated benchmark.
