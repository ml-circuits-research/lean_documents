# Evaluator-only design expectations

WITHHOLD THIS FILE AND ITS DIRECTORY FROM BLIND AUDITORS. These are authored expectations, not executed validation results or evidence. No theorem has been executed as part of this fixture preparation.

## Deliberately mixed report

| Finding | Expected treatment | Essential evidence and reasoning |
| --- | --- | --- |
| F11-01 | Supported conclusion and arithmetic argument | L-02 sums to 50000. |
| F11-02 | Refuted arithmetic claim | P-05, L-01–L-02 imply balance 55000 − 50000 = 5000, not 6000. |
| F11-03 | Refuted conclusion; incomplete and unsound argument | P-02 alone is not exhaustive. B satisfies every conjunct of P-03: R2, 10 ≤ 12 ≤ 14, 11 ≤ 12, 12 − 11 ≤ 2, 12 ≤ 15, 15 − 12 ≤ 3. |
| F11-04 | Refuted conclusion and arithmetic premise | C fails ordinary approval and has delay 16 − 12 = 4 > 3. No third route exists. |
| F11-05 | Supported conclusion with a defective supplied argument | B is eligible via compliant approval, PASS, and South membership. Checksum alone is not sufficient. C and D are finite counterexamples to that proposed implication. Do not mark the conclusion false because its report argument fails. |
| F11-06 | Refuted source-attribution claim | L-03 states package-integrity meaning and expressly disclaims timing attestation. L-02 also shows B and C approved after release. Audit the exact attribution separately from any cohort timing proposition inferred from it. |
| F11-07 | Missing evidence / unsupported assertion, with an invalid evidence claim | K-02 lists the annex as not supplied, not as confirming zero incidents. Its actual later reliability remains unknown; no incident can be inferred from absence of evidence. |
| F11-08 | Undefined evaluation criterion and unsupported argument | P-06 and K-03 supply no robustness rubric. Checksum PASS is real but does not define or prove operational robustness. Do not substitute an invented threshold or call the underlying rating mathematically false. |
| F11-09 | Refuted claim of unambiguous evidential support; unresolved underlying acceptance | R-01 and R-02 disagree on the same event and time. R-03 supplies equal standing and no reconciliation. Distinguish the demonstrably false assertion that the evidence is unambiguous from the unresolved real-world question of acceptance. |
| F11-10 | Refuted boundary claim | P-03 limits the release window to 10–14 inclusive, and 15 > 14. |
| F11-11 | Refuted amount and eligibility argument | Approval and destination predicates leave exactly A and B eligible; total 30000. C fails approval; D fails membership. |
| F11-12 | Scope/support gap; unsupported population equality | L-01 and K-03 establish only a four-of-forty record scope. No amounts for the other 36 are supplied. Do not assume positive amounts, derive a strict population lower bound, or prove that 50000 is necessarily false. |

## Cautious report

Every F11-OK finding is intended to be supported in its expressed scope. Numerical or policy propositions in OK-01 through OK-05 and OK-10 through OK-11 admit finite Lean checks after transparent extraction. OK-06 is a source-text entailment. OK-07, OK-08, and OK-12 are justified packet-limit findings, not affirmative proofs of unobserved events. OK-09 is a documented conflict, not a resolution of acceptance. All supplied arguments still require independent inspection; correctness must not be presumed from the filename.

## Audit quality requirements

Audit all twelve findings per report and separately address material premises and reasons embedded after “Argument.” For F11-05 the conclusion can be formally supported while its stated sufficiency rule is refuted using C or D. For F11-09, keep the evidential-support assertion and physical acceptance assertion distinct. A formal source model must not collapse contradictory observations into axioms asserting both acceptance and its negation and then prove arbitrary conclusions.

Every audit result should reproduce the exact claim, its verification problem, source evidence, applicable rules, assumptions, reasoning, and limits. Explain refutations explicitly. Treat unsupported claims and missing arguments as useful support gaps. Do not expose these expectations to a blind reviewer, and do not report intended formalizations as actual proof executions.
