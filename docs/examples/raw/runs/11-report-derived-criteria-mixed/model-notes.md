# Model correspondence and limits

`models/Audit.lean` is a small projection of the supplied packet, not a replacement substantive report. The source extraction uses generated Pxx paragraph anchors; the quoted human labels L-01, L-02, P-01 etc remain visible in each evidence record. All source files were read in full before model authoring, including every table cell.

## Domains, units and values

`Dispatch` stores integer euro cents, route, integer campaign release and approval days, optional integer declaration day, checksum Boolean and destination. Integers preserve the source's arithmetic semantics without truncated subtraction. `a`, `b`, `c`, `d` reproduce the four rows in dispatch-ledger.md generated P04 (human L-02 table). The declaration `none` is licensed by that document's P03 completeness explanation: no declaration existed through day 20. `cohort` includes each of the four actual dispatches once, matching P02 (human L-01); the snapshot finality through day 20 supplies a scoped closed world for these fields, not for later events or the 36 other dispatches.

`ordinary` is approval strictly before release, from dispatch-policy.md P03 (human P-02). `window` uses inclusive integer boundaries 10 and 14. `exception` is the conjunction of route R2, release window, declaration existence and its two-day bound, and approval between release and release+3. This follows dispatch-policy.md P04 (human P-03) without dropping any conjunct. `compliant` is ordinary OR exception; the source's no-other-route statement licenses this equivalence only for the reviewed cohort. Negative results for C therefore use completeness actually stated in the packet.

`listed` is North OR South from destination-list.md P02 (human D-01), whose membership is explicitly complete and whose effective interval includes all four releases through cutoff. `eligible` conjoins compliant approval, checksum PASS and listed destination, following dispatch-policy.md P05 (human P-04). Delivery acceptance has no role. `total` sums all cohort amounts, `balance` subtracts that sum from L-01's 55000-cent budget, and `eligibleTotal` filters by eligibility before summing, following human P-05.

## Direct targets and auxiliary targets

- `expenditure` proves the exact F11-01 sum. `headroom` proves the corrected F11-02 result and excludes 6000.
- `bApproval` refutes the negative F11-03 conclusion; `bException` shows why ordinary-route failure does not establish noncompliance.
- `cApproval` refutes F11-04's exception compliance by proving no compliant route; `cDelay` independently checks the failing four-day gap.
- `bEligible` proves F11-05's conclusion. `passInsufficient` checks a concrete D witness belonging to the cohort, with PASS and ineligibility; this invalidates the author's inference without invalidating the supported conclusion.
- `notAllPrior` disproves universal prior approval on the table, but is only auxiliary for F11-06: a theorem about events is not a theorem about what natural-language L-03 states. The exact attribution claim is refuted by reading L-03's explicit disclaimer.
- `releaseWindow` proves F11-10's exact negated interval membership.
- `settlement` excludes F11-11's total and proves 30000; `eligibleMembers` supplies the eligible A/B and ineligible C/D partition.

`Record` and `saysAccepted` store attributed statements from delivery-records.md P02 and P03 (human R-01 and R-02), not actual acceptance values. `recordConflict` checks their opposite assertions. P04 (R-03) independently states equal evidential standing and no precedence or correction. Accordingly F11-09's claim that the evidence is unambiguous is documentarily false, while actual physical acceptance remains disputed. No contradiction is injected into Lean assumptions; there is no explosion or purported proof of both actual acceptance and rejection.

## Non-entailment projections

`Extension` adds a later B incident count and a list of the missing 36 dispatch amounts to the globally fixed cohort facts. `compatible` requires precisely 36 missing amounts, preserving L-01's population cardinality. Every policy rule and known datum stays fixed globally. The supplied packet imposes no later incident constraint (packet-register.md P03, K-02) and no amount constraint for those missing rows (P04, K-03). Nothing requires a strictly positive dispatch amount. Thus these extensions satisfy every applicable constraint on the projected variables; omitted fields of the missing dispatches can be arbitrary because there is no supplied record or rule requiring a particular amount or subsequent incident count.

`quiet` and `incident` differ only in zero versus one later incident, preserving exactly the same observed cohort. `laterNonentailment` witnesses both possibilities, proving neither history from the packet. `quiet` and `extraAmount` supply 36 zero amounts versus one one-cent amount and 35 zero amounts; `populationNonentailment` witnesses population totals 50000 and 50001. These are compatible possibilities, not fabricated actual dispatch observations. The results are auxiliary and do not refute the original unobserved event or population total.

No predicate is invented for operational robustness. F11-08 remains blocked by missing definition/rubric; checksum success does not make an arbitrary rating rule legitimate.

## Trust and execution

The model uses ordinary definitions and kernel-checked decidable computations, no custom axioms, `sorry`, native computation shortcut, imports or elaborators. The finite concrete dispatches witness nonempty scope. The input transcription and policy interpretation remain semantic assumptions; Lean cannot authenticate documents. Positive and negative targets are separately represented according to claim polarity, and the non-entailment targets preserve both alternatives instead of converting a missing premise into falsehood.

The first development compile identified a missing Decidable instance for the extension compatibility predicate. That instance was added without changing the proposition. The final retained helper logs, proof-results.json and environment.lock identify the actual execution and per-target axiom checks; no independent external kernel checker is claimed.

Independent review clarified the F11-07 documentary wording: the unavailable annex content is unsupported, not refuted. K-02 is evidence of the supplied packet's limits and does not reveal what an unseen annex says. This correction changes no model definition or proof target; the later-event witness was already auxiliary and preserved both possibilities.
