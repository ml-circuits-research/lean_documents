# Agent-native claim audit

Selected report: `report-mixed.md`. Sources: `source.md`. No review brief supplied.
Execution mode: agent-native. The Python artifact checker and Lake were not used.
The alternate correct report is a fixture companion, not evidence and not audited in this run.

## Source facts and model interpretation

| Source | Model | Meaning and scope |
| --- | --- | --- |
| S1: “The recorded amount for item A is 9 units.” | `dossier w := w.amount = 9` | The recorded nonnegative integral amount is fixed. This is not source authentication. |
| S2: “An item is within budget exactly when its amount is at most 10 units.” | `withinBudget w := w.amount ≤ 10` | The supplied threshold determines the budget criterion. |
| S3: “This record contains no information about approval. Both approval states remain possible.” | `approved w := w.approved = true` with no dossier constraint | Approval is an independent Boolean with both values admitted. |

For this model, amounts are natural-number units. The recorded value and threshold are integers; that restriction is enough for these targets and for the counterexample 11, but does not formalize every possible fractional amount. The source is deliberately small and read in full. There are no other supplied rules, dates or approval records. The countermodel uses nonnegative integral amounts; the report's unrestricted positive-amount inference already fails in that subdomain.

## Verification methods and results

### C1 — supported conclusion, refuted argument premise

Exact claim R1: “Item A is within budget because every positive amount is within budget.”
The conclusion is that A is within budget. The proposed rule is that every positive amount is within budget.

Method: instantiate S1 and S2, check the inequality, and separately test the report's universal implication. `budgetSupported` proves non-vacuous support: at least one world satisfies the dossier, and every such world has amount 9 ≤ 10. `positiveRuleRefuted` disproves the offered universal rule using amount 11, which is positive but exceeds 10. This counterexample targets the report's general rule, not the actual recorded amount. Thus the conclusion is correct in the source model while its justification uses a false rule. Modus ponens would be valid if the universal rule were true; the defect is the rule, not that inference form.

### C2 — refuted

Exact claim R2: “Item A is over budget.”
Interpret “over budget” as the negation of the supplied within-budget definition for these numeric amounts.
Method: apply S1 and S2. `overBudgetRefuted` proves that the nonempty evidence model entails the negation of this claim: 9 ≤ 10, so A cannot be over budget. R2 supplies no additional argument to verify. This refutes the scoped claim, not the authenticity of the record.

### C3 — insufficient support, formally underdetermined

Exact claim R3: “Item A was approved.”
The report offers no approval evidence or inference. The search inspected all of S1–S3 and all of R1–R3, for approval status and any rule connecting amount to approval. S3 explicitly leaves approval unconstrained. No outside records were searched.
Method: construct two worlds with the same amount 9, one approved and the other not approved. `approvalUnderdetermined` verifies both witnesses; `approvalNeither` establishes that the dossier model supports neither approval nor its negation. Missing support is an audit finding; it is not a refutation of actual approval.

## Executed assurance and limits

Lean 4.24.0 compiled the final combined `Audit.lean`, including exact target assertions and `#print axioms` for all five referenced results. Final exit status: 0. All five report no axiom dependencies. The first failed compilation attempt is retained separately; its output is not a successful proof. Explicit proposition unfolding corrected its decidability elaboration failures before the final run.

The source mappings, full passage coverage and quotations were inspected by the auditing agent, not certified by the Python contract validator. An independent semantic review is recorded separately. Actual events outside the synthetic source, source authenticity, and general handling of arbitrary real document formats are not proved by this fixture.
