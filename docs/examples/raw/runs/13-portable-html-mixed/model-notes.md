# Source facts and source-to-symbol map

All statements are attributed to the supplied synthetic current-stock register; they are assumed faithfully stated for this scoped audit, not independently authenticated. Its heading fixes 4 November 2026. Units are exact whole stock units. Rules apply to rows at that snapshot; no legal jurisdiction or historical completeness is supplied.

| ID | Original HTML location and extracted anchor | Role and representation |
|---|---|---|
| F0 | Lines 5-6, h1 and scope | Snapshot time and explicit completeness of the current population A/B/C. Stock.rows contains exactly these three rows. This is a closed current population, not a closed historical event domain. |
| N1 | Line 7, count-rule | Definition: active and quarantined count; archived does not. Stock.counted implements this status filter before Stock.total sums quantities. |
| N2 | Line 8, release-rule | Normative biconditional: release eligibility requires active status AND signed yes. Stock.eligible represents both conjuncts. |
| F1 | Line 9, row-a | Reported observation: A active, 18 units, signed yes; Stock.a. |
| F2 | Line 10, row-b | Reported observation: B quarantined, 27 units, signed yes; Stock.b. |
| F3 | Line 11, row-c | Reported observation: C archived, 15 units, signed no; Stock.c. |
| L1 | Line 12, history | Scope limitation: no historical records supplied and no claim to event-history completeness. Historical existence remains a free Boolean; true means at least one prior clearance occurred, false means none. |

The HTML paragraphs were read from immutable original bytes and compared with the imported text and original line numbers. This was terminal inspection of simple source markup, not a rendered-browser or visual-image review; the file contains no scripts, hidden content, CSS or complex layout. The imported projections are not independent corroboration of the same original. Review acceptances bind the original hash and complete quoted segment hash.

# Methods and proof correspondence

R1 uses exact finite filtering and addition: A and B count, C is excluded, and 18+27=45. R2 tests the same filtered sum against 60; an auxiliary theorem establishes that the unfiltered arithmetic is 60, isolating the erroneous inclusion rule. R3 separately tests actual eligibility of A and the signature-only inference: B is an actual in-population signed row that fails active status and hence eligibility. That argument counterexample does not refute A's release eligibility.

R4 uses a bounded full-corpus documentary search and two-model analysis. Stock.currentEvidence compresses the fixed current dataset to two established consequences, total=45 and eligibility of A, and deliberately imposes no historical constraint. All other current facts are fixed by definitions independently of the Boolean. The false-history and true-history worlds therefore have identical current facts but opposite values for no prior clearance. This proves non-entailment in the declared model, not any real historical event and not the completeness of possible real-world interpretations. The EvidenceLogic vocabulary is copied verbatim from the isolated skill and inspected; its generic theorems are also audited by the helper.

No custom axioms, external libraries, cached compiled objects or independent kernel checker are used. This proof language does not authenticate the source or validate an operational release in the real world.
