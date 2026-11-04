# Coordinator semantic review and reconciliation

The coordinator rederived the four outcomes from the supplied report and original HTML before reading the proposed models/findings; see source-first-review.md. The coordinator knew the fixture design, so this is an independent pass over the agent's work, not a blind domain-expert benchmark. No evaluator answer file was supplied to the auditing agent.

I inspected the full original HTML, source extraction, Stock/Data.lean, Stock/Audit.lean, model notes, and four findings. Original paragraphs and line coordinates agree with the imported text. Exact integral quantities, status filter, release biconditional and present-only completeness justify the typed data and finite model. B is an actual member of the supplied population and a valid counterexample to signature-only sufficiency.

R1's 45-unit conclusion and offered arithmetic argument are supported. R2's 60-unit conclusion is refuted, although adding all three rows really yields 60: the defect is the inclusion premise. R3's release conclusion is supported, but its signature-only rule is refuted by B; a deduction using that false rule need not have an invalid inference form. R4's historical conclusion is unsupported, and the absence-to-nonexistence inference fails in the two-world model. Nothing here proves actual historical clearance or its actual absence.

The history model fixes all current facts in definitions and varies only a historical Boolean. currentEvidence is an explicitly explained projection of the fixed facts, not a conclusion secretly assumed about history. Both historical values satisfy it. The Lean targets align with the findings; direct and auxiliary results are distinguished. No custom axiom is introduced.

Review requested two corrections before delivery:

1. Separate a false offered premise from an invalid inference. C2 and C3 use unsound_argument / outcome: unsound; the signature-only statement is a contradicted premise. R4 remains invalid_inference. The helper contract now supports this distinction and rejects an unsound label with no linked contradicted premise.
2. Repair nested proof links in the argument renderer and rerender using the corrected copied helper. These links resolve to models/Stock/Audit.lean.

The final technical check must run after incorporation of this review. Its result, final artifact fingerprint and actual logs determine technical success; this review alone is not a compiler result. Scope remains the supplied synthetic current-stock record, without source authentication or historical completeness. No separate kernel checker was used for this portability audit.
