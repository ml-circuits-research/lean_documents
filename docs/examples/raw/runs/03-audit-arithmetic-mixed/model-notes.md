# Model interpretation

## Source-to-symbol mapping

The model uses exact nonnegative integer cents, as specified in B-02. `Payment.amount` and `Payment.approved` transcribe the four rows of ledger L-02 without rounding; `p01` through `p04` preserve row identity through named constants. All `matched` fields are true because inspection I-01 explicitly says all four sampled payments matched their invoices. `sample` contains exactly these four entries, with its completeness justified only for the selected sample by L-01. No population-wide ledger completeness is assumed.

`sampleTotal` sums all four amounts once. `budget = 300000` maps to L-03 and is a sample comparison reference. `exceptions` selects false approval fields, applying M-02; amount and invoice match do not determine exception membership. `exceptionCount` and `exceptionTotal` count and sum that filtered list. Currency equivalence uses exactly 100 cents per euro. Percentage comparisons use cross multiplication over the nonzero sample size 4 and population size 20; no integer division rounding occurs. The budget theorem also proves that sampleTotal is below budget, avoiding a misleading use of truncated natural subtraction.

`populationExceptions n = exceptionCount + n` represents the complete population as the four distinct selected entries plus sixteen other entries. `n` denotes the unknown count of missing approvals among those sixteen, bounded by 16 when used as a feasible population count. It is not a source-derived actual count. The model's 0 and 8 completions are both permitted by the supplied missing-data boundary: they demonstrate different compatible rates, including the reported 50%, and do not refute that report claim as an actual-world proposition. The lower-bound theorem is conditional on the sample being part of the twenty-entry population, as described in L-01, and on counting each missing approval once per entry.

## Theorem relationships

- `paymentTotal`: direct support for C03-01's cents total and EUR conversion.
- `budgetDifference`: direct finite refutation of C03-02's 35000-cent difference, with corrected 25000-cent difference. The correct EUR difference is 250.00 by B-02.
- `sampleExceptionRate`: direct support for C03-03's two exceptions among four entries and 50% rate.
- `missingApprovalTotal`: direct support for C03-05's 75000 cents.
- `allInvoicesMatched`: direct support for the explicit factual premise of C03-06.
- `approvalCounterexample`: direct refutation of C03-06's universal approval conclusion, witnessed by P03 inside the sample; it also demonstrates why matching does not imply approval. P04 provides additional documentary counterevidence.
- `populationCompletionAlternatives`: auxiliary result for C03-04; shows failure of inference from the sample to an exact population rate, not an actual population counterexample.
- `populationLowerBound`: direct support for C03-10 under the stated population inclusion/count interpretation.

C03-07 is a literal textual misrepresentation and receives a documentary refutation without pretending that Lean understands prose. C03-08 remains undetermined because Annex C is absent; the index proves only that the document is listed. C03-09 has no operational aesthetic truth criterion and is not formalized.

## Trust and limits

Data and mapping are human transcriptions. The proof checker establishes encoded targets, not source authenticity, historical events, semantic adequacy, fraud, control effectiveness, or the unknown content of Annex C. There are no custom axioms or assumed conclusions. The concrete sample is nonempty; the population lower bound does not rely on vacuous universal quantification over an empty domain. This is the audit author's model and has not yet received an independent semantic review. Actual execution status is recorded separately in proof-results.json and logs.
