# Synthetic audit arithmetic brief

<a id="B-01"></a>
## B-01 — Scope and finite questions
Audit the numbered claims in the selected supplied report (`report.md` or `report-correct.md`) against the four supplied sources. For each claim, distinguish support, refutation, conflicting evidence, insufficient evidence, and nonformal judgment. Questions concern the sampled payment total, budget difference, approval exceptions, sample and population rates, the content of a cited paragraph, and whether a missing annex establishes clearance.

<a id="B-02"></a>
## B-02 — Arithmetic conventions
All amounts are exact nonnegative integer euro cents; 100 cents equal EUR 1.00. Budget difference means budget minus the sum of the four sampled payments. An approval exception is an entry whose required approval was absent at the cutoff. Sample exception rate means exception count divided by sample count. The target population contains exactly 20 entries, but attributes of the 16 unsampled entries are unknown. Sample and population are different domains.

<a id="B-03"></a>
## B-03 — Evidence conventions
Use only supplied source paragraphs as substantive evidence; this brief fixes scope and definitions. The selected report is the object being audited, not evidence for itself; the other report variant is excluded from that audit. A source citation does not make a claim true. Source omission does not establish a negative world fact. The supplied ledger is complete for the four sampled entries; no such completeness assumption applies to the population or missing annex. Annex C has not been supplied, so its contents cannot be inferred. No Lean workflow or external retrieval is authorized for this fixture review.
