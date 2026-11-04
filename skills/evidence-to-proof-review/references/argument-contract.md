# Mandatory argument contract

For each finding deliver:

1. Exact original claim, report anchor, atomic target and relation to its parent finding.
2. Verification question with quantifier, domain, period, relevant version and interpretation.
3. Exact evidence quotes with source paths and anchors, including counterevidence.
4. Applicable rules, explicit assumptions and exceptions; each material premise must have a source or an honest assumption label.
5. Numbered reasoning steps from evidence through rules to the outcome.
6. A precise result, any checked theorem and its relation to the original claim, and what has not been established.
7. A correction or the specific missing evidence that would resolve the issue.

For **claim refutation**, identify a contradictory relevant case or a proof of the exact negation. Show witness membership and applicable conditions. A claim about every operation fails when one in-scope operation violates the applicable rule; an out-of-scope operation is not a witness.

For **invalid inference**, identify the failing inference rather than just calling the report wrong. Example: a rule `(smokePassed AND securityApproved) -> ready` cannot establish readiness from smoke tests alone. A model with smoke=true, security=false, ready=false satisfies the rule and smoke premise, so the inference fails. This does not establish actual non-readiness.

For **insufficient support**, distinguish the report's own justification from what an independent corpus search found. Name the missing premise, searched sources and limits, and why present evidence does not establish it. “No approval attachment” does not establish “approval never existed”. Conversely, independent evidence can support a poorly cited claim while its citation defect remains an audit observation.

For conflicting testimony preserve both attributed statements and compare scope, time and proposition before declaring a conflict. Never resolve it by selecting whichever source agrees with the report.

Use human-readable reasoning even when a Lean target is a simple computation. Explain how values were extracted and how the mathematical target corresponds to the report. Definition-unfolding alone must not masquerade as external evidence.
