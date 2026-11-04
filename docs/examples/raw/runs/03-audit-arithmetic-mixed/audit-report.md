# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

[Semantic correspondence review](semantic-review.md)

## C03-01

### Exact report claim

`input/report.md#C03-01`

> **C03-01.** The four sampled payments total exactly 275000 euro cents (EUR 2750.00). Citation: ledger L-02.

### Verification question

Do all four listed payments sum to exactly 275000 cents, equivalent to EUR 2750.00?

### Source evidence

- [input/sources/ledger.md](input/sources/ledger.md) — `L-01`

> ## L-01 — Cutoff and coverage
> At the 30 June 2031 audit cutoff, the target population contained exactly 20 paid entries. The following four entries are the complete selected sample. No values for unsampled entries are included in this extract.

- [input/sources/ledger.md](input/sources/ledger.md) — `L-02`

> ## L-02 — Exact amounts and approval status
> | Entry | Paid amount, euro cents | Required approval present at cutoff |
> | --- | ---: | --- |
> | P01 | 120000 | Yes |
> | P02 | 80000 | Yes |
> | P03 | 50000 | No |
> | P04 | 25000 | No |

### Rules

- The selected ledger is complete for four distinct entries, so each row is counted once.
- B-02 defines exact integer cents and 100 cents per euro.

### Assumptions

- The supplied synthetic documents accurately describe the stated sample and cutoff; this audit does not independently authenticate them.

### Reasoning

- 1. Extract P01=120000, P02=80000, P03=50000 and P04=25000 cents from L-02.
- 2. Add the four values: 120000 + 80000 + 50000 + 25000 = 275000.
- 3. 2750 × 100 = 275000, so the EUR 2750.00 rendering has no rounding discrepancy.

### Limits

- The result applies to the complete selected sample at the 30 June 2031 cutoff and does not establish unobserved population attributes.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.paymentTotal` in module `Audit` (supports): `Audit.sampleTotal = 275000 ∧ Audit.sampleTotal = 2750 * 100`.
  [Model](models/Audit.lean) · [Executed check](checks/Target009.lean) · [Actual proof log](logs/target-009.log)

### Recommendation

Retain this claim within the stated scope.

## C03-02

### Exact report claim

`input/report.md#C03-02`

> **C03-02.** The budget exceeds the sampled payment total by exactly 35000 euro cents (EUR 350.00). Citations: ledger L-02, L-03.

### Verification question

Is the sample-only budget minus the actual four-payment total 35000 cents?

### Source evidence

- [input/sources/ledger.md](input/sources/ledger.md) — `L-02`

> ## L-02 — Exact amounts and approval status
> | Entry | Paid amount, euro cents | Required approval present at cutoff |
> | --- | ---: | --- |
> | P01 | 120000 | Yes |
> | P02 | 80000 | Yes |
> | P03 | 50000 | No |
> | P04 | 25000 | No |

- [input/sources/ledger.md](input/sources/ledger.md) — `L-03`

> ## L-03 — Budget reference
> The budget used for the sample comparison is exactly 300000 euro cents. This budget is a comparison reference for these four entries only, not a statement of the population budget.

### Rules

- B-02 defines budget difference as budget minus the four sampled payments.
- Budget and payments must be compared in the same exact cent unit.

### Assumptions

- The supplied synthetic documents accurately describe the stated sample and cutoff; this audit does not independently authenticate them.

### Reasoning

- 1. L-02 sums to 275000 cents; L-03 supplies a budget of 300000 cents.
- 2. 300000 - 275000 = 25000 cents, or EUR 250.00.
- 3. 25000 is unequal to the reported 35000. This exact finite arithmetic contradiction refutes the claimed difference; the positive excess itself is correctly implied by budget being larger.

### Limits

- The result applies to the complete selected sample at the 30 June 2031 cutoff and does not establish unobserved population attributes.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.budgetDifference` in module `Audit` (refutes): `Audit.budget - Audit.sampleTotal = 25000 ∧ Audit.budget - Audit.sampleTotal ≠ 35000 ∧ Audit.sampleTotal ≤ Audit.budget`.
  [Model](models/Audit.lean) · [Executed check](checks/Target010.lean) · [Actual proof log](logs/target-010.log)

### Recommendation

Replace 35000 cents / EUR 350.00 with 25000 cents / EUR 250.00.

## C03-03

### Exact report claim

`input/report.md#C03-03`

> **C03-03.** Exactly two of the four sampled entries have approval exceptions, giving an exact sample exception rate of 50%. Citations: ledger L-02; method M-02.

### Verification question

Are exactly two of the four selected entries approval exceptions, and is the exact sample rate 50%?

### Source evidence

- [input/sources/ledger.md](input/sources/ledger.md) — `L-01`

> ## L-01 — Cutoff and coverage
> At the 30 June 2031 audit cutoff, the target population contained exactly 20 paid entries. The following four entries are the complete selected sample. No values for unsampled entries are included in this extract.

- [input/sources/ledger.md](input/sources/ledger.md) — `L-02`

> ## L-02 — Exact amounts and approval status
> | Entry | Paid amount, euro cents | Required approval present at cutoff |
> | --- | ---: | --- |
> | P01 | 120000 | Yes |
> | P02 | 80000 | Yes |
> | P03 | 50000 | No |
> | P04 | 25000 | No |

- [input/sources/method.md](input/sources/method.md) — `M-02`

> ## M-02 — Separate controls
> An invoice match and a required approval are separate controls. An invoice match alone does not establish that required approval was present. Missing approval counts as one approval exception per entry, irrespective of that entry's amount.

### Rules

- Count one exception for each entry whose required approval was absent at the cutoff.
- B-02 defines sample rate as exception count divided by the sample count, without amount weighting.

### Assumptions

- The supplied synthetic documents accurately describe the stated sample and cutoff; this audit does not independently authenticate them.

### Reasoning

- 1. P01 and P02 show approvals present; P03 and P04 show approvals absent.
- 2. Therefore exactly two of the four sample entries count as exceptions under M-02.
- 3. The denominator is four and nonzero; 2/4 = 50/100. The Lean target checks this exact equality by cross multiplication.

### Limits

- The result applies to the complete selected sample at the 30 June 2031 cutoff and does not establish unobserved population attributes.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.sampleExceptionRate` in module `Audit` (supports): `Audit.sample.length = 4 ∧ Audit.exceptionCount = 2 ∧ Audit.exceptionCount * 100 = 50 * Audit.sample.length`.
  [Model](models/Audit.lean) · [Executed check](checks/Target011.lean) · [Actual proof log](logs/target-011.log)

### Recommendation

Retain this claim within the stated scope.

## C03-04

### Exact report claim

`input/report.md#C03-04`

> **C03-04.** Exactly 50% of the entire 20-entry population has approval exceptions. Citations: ledger L-01, L-02; method M-01.

### Verification question

Does the sample establish that exactly ten of the twenty population entries had missing approvals?

### Source evidence

- [input/sources/ledger.md](input/sources/ledger.md) — `L-01`

> ## L-01 — Cutoff and coverage
> At the 30 June 2031 audit cutoff, the target population contained exactly 20 paid entries. The following four entries are the complete selected sample. No values for unsampled entries are included in this extract.

- [input/sources/ledger.md](input/sources/ledger.md) — `L-02`

> ## L-02 — Exact amounts and approval status
> | Entry | Paid amount, euro cents | Required approval present at cutoff |
> | --- | ---: | --- |
> | P01 | 120000 | Yes |
> | P02 | 80000 | Yes |
> | P03 | 50000 | No |
> | P04 | 25000 | No |

- [input/sources/method.md](input/sources/method.md) — `M-01`

> ## M-01 — Selection
> The four sample entries were selected by reviewer judgment, not by random selection. This review does not assert that the selected entries are representative of the other 16 population entries.

### Rules

- Sample counts and population counts concern different domains.
- An exact population rate requires the missing-approval count among the other sixteen entries or another sufficient completeness argument.
- A compatible hypothetical completion diagnoses non-entailment and is not an observed actual-world counterexample.

### Assumptions

- The supplied synthetic documents accurately describe the stated sample and cutoff; this audit does not independently authenticate them.

### Reasoning

- 1. L-01/L-02 identify two missing approvals in the complete four-entry sample, but give no statuses for the other sixteen population entries.
- 2. M-01 explicitly states judgmental selection and no assertion of representativeness; it does not license the exact 50% extrapolation.
- 3. A compatible completion with zero additional missing approvals gives 2/20 = 10%; another with eight additional missing approvals gives 10/20 = 50%. Both additional counts fit within sixteen.
- 4. The auxiliary Lean result verifies these alternative arithmetic completions. Thus the proposed inference is invalid, while the actual exact population rate remains undetermined; the 50% statement could happen to be true.

### Limits

- No actual statuses for the sixteen unsampled entries are supplied.
- Alternative completions show failure of entailment and do not refute 50% as an actual population fact.
- The actual population rate could range from 10% to 90% under the supplied distinct-entry model; neither endpoint is asserted as actual.

### Result

Semantic state: **undetermined**; argument status: **invalid_inference**; formal status: **auxiliary**.

### Formal evidence

- `Audit.populationCompletionAlternatives` in module `Audit` (auxiliary): `Audit.populationExceptions 0 * 100 ≠ 50 * 20 ∧ Audit.populationExceptions 8 * 100 = 50 * 20 ∧ (0 : Nat) ≤ 16 ∧ (8 : Nat) ≤ 16`.
  [Model](models/Audit.lean) · [Executed check](checks/Target012.lean) · [Actual proof log](logs/target-012.log)

### Recommendation

Report the 50% sample rate separately; obtain approval statuses for all sixteen other entries before asserting an exact population rate.

## C03-05

### Exact report claim

`input/report.md#C03-05`

> **C03-05.** Sampled payments with missing approvals total exactly 75000 euro cents. Citation: ledger L-02.

### Verification question

Do the sampled payments with absent required approvals sum to 75000 cents?

### Source evidence

- [input/sources/ledger.md](input/sources/ledger.md) — `L-02`

> ## L-02 — Exact amounts and approval status
> | Entry | Paid amount, euro cents | Required approval present at cutoff |
> | --- | ---: | --- |
> | P01 | 120000 | Yes |
> | P02 | 80000 | Yes |
> | P03 | 50000 | No |
> | P04 | 25000 | No |

- [input/sources/method.md](input/sources/method.md) — `M-02`

> ## M-02 — Separate controls
> An invoice match and a required approval are separate controls. An invoice match alone does not establish that required approval was present. Missing approval counts as one approval exception per entry, irrespective of that entry's amount.

### Rules

- Select entries by approval status at the cutoff, then sum their amounts once.

### Assumptions

- The supplied synthetic documents accurately describe the stated sample and cutoff; this audit does not independently authenticate them.

### Reasoning

- 1. The only missing-approval entries in the complete selected sample are P03 and P04.
- 2. Their amounts are 50000 and 25000 cents.
- 3. 50000 + 25000 = 75000 cents, matching the report.

### Limits

- The result applies to the complete selected sample at the 30 June 2031 cutoff and does not establish unobserved population attributes.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.missingApprovalTotal` in module `Audit` (supports): `Audit.exceptionTotal = 75000`.
  [Model](models/Audit.lean) · [Executed check](checks/Target013.lean) · [Actual proof log](logs/target-013.log)

### Recommendation

Retain this claim within the stated scope.

## C03-06-premise

### Exact report claim

`input/report.md#C03-06`

> all four invoices matched

### Verification question

Did all four sampled payments match their invoices?

### Source evidence

- [input/sources/inspection.md](input/sources/inspection.md) — `I-01`

> ## I-01 — Inspection result
> All four sampled payments matched their invoices. Required approvals were absent for P03 and P04 at the cutoff; approvals were present for P01 and P02. The absence of an approval does not by itself establish fraud.

- [input/sources/ledger.md](input/sources/ledger.md) — `L-01`

> ## L-01 — Cutoff and coverage
> At the 30 June 2031 audit cutoff, the target population contained exactly 20 paid entries. The following four entries are the complete selected sample. No values for unsampled entries are included in this extract.

### Rules

- Preserve a true factual premise separately from an invalid inference drawn from it.

### Assumptions

- The supplied synthetic documents accurately describe the stated sample and cutoff; this audit does not independently authenticate them.

### Reasoning

- 1. I-01 explicitly says all four sampled payments matched their invoices.
- 2. L-01 fixes the complete sample domain to four entries.
- 3. The model assigns matched=true to those four entries and checks their universal matching statement; this does not imply approval.

### Limits

- The result applies to the complete selected sample at the 30 June 2031 cutoff and does not establish unobserved population attributes.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.allInvoicesMatched` in module `Audit` (supports): `∀ p ∈ Audit.sample, p.matched = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target014.lean) · [Actual proof log](logs/target-014.log)

### Recommendation

Retain invoice matching as a separate control observation, without an approval inference.

## C03-06

### Exact report claim

`input/report.md#C03-06`

> **C03-06.** Because all four invoices matched, every sampled payment had its required approval at the cutoff. Citation: inspection I-01.

### Verification question

Does universal invoice matching establish that every sampled payment had required approval at the cutoff?

### Source evidence

- [input/sources/inspection.md](input/sources/inspection.md) — `I-01`

> ## I-01 — Inspection result
> All four sampled payments matched their invoices. Required approvals were absent for P03 and P04 at the cutoff; approvals were present for P01 and P02. The absence of an approval does not by itself establish fraud.

- [input/sources/method.md](input/sources/method.md) — `M-02`

> ## M-02 — Separate controls
> An invoice match and a required approval are separate controls. An invoice match alone does not establish that required approval was present. Missing approval counts as one approval exception per entry, irrespective of that entry's amount.

- [input/sources/ledger.md](input/sources/ledger.md) — `L-02`

> ## L-02 — Exact amounts and approval status
> | Entry | Paid amount, euro cents | Required approval present at cutoff |
> | --- | ---: | --- |
> | P01 | 120000 | Yes |
> | P02 | 80000 | Yes |
> | P03 | 50000 | No |
> | P04 | 25000 | No |

### Rules

- M-02 treats invoice matching and required approval as separate controls.
- A universal approval statement fails when an in-scope sampled entry has approval absent at the same cutoff.

### Assumptions

- The supplied synthetic documents accurately describe the stated sample and cutoff; this audit does not independently authenticate them.

### Reasoning

- 1. The invoice-matching premise is supported, but M-02 supplies no implication from matching to approval.
- 2. I-01 and L-02 identify P03 and P04 as sampled entries missing required approval at the cutoff.
- 3. P03 is an explicit in-scope counterexample: it matched its invoice and lacked approval. Hence the universal approval conclusion is false, as well as unsupported by the proposed inference.
- 4. The Lean target checks sample membership, matched=true, approved=false, and the negation of universal sample approval.

### Limits

- The result applies to the complete selected sample at the 30 June 2031 cutoff and does not establish unobserved population attributes.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.approvalCounterexample` in module `Audit` (refutes): `Audit.p03 ∈ Audit.sample ∧ Audit.p03.matched = true ∧ Audit.p03.approved = false ∧ ¬ (∀ p ∈ Audit.sample, p.approved = true)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target015.lean) · [Actual proof log](logs/target-015.log)

### Recommendation

State invoice matching separately and report the two missing approvals at the cutoff. Do not infer fraud or later approval status.

## C03-07

### Exact report claim

`input/report.md#C03-07`

> **C03-07.** Inspection paragraph I-01 says that no sampled payments were missing required approvals. Citation: inspection I-01.

### Verification question

Does I-01 literally state that no sampled payments were missing required approvals?

### Source evidence

- [input/sources/inspection.md](input/sources/inspection.md) — `I-01`

> ## I-01 — Inspection result
> All four sampled payments matched their invoices. Required approvals were absent for P03 and P04 at the cutoff; approvals were present for P01 and P02. The absence of an approval does not by itself establish fraud.

### Rules

- A claim about what a cited paragraph says must match its literal attributed content and temporal scope.

### Assumptions

- The supplied synthetic documents accurately describe the stated sample and cutoff; this audit does not independently authenticate them.

### Reasoning

- 1. Read all of I-01, rather than only the invoice-matching sentence.
- 2. Its next sentence explicitly says required approvals were absent for P03 and P04 at the cutoff.
- 3. That named absence directly contradicts the report’s characterization that I-01 says no sampled payments lacked approval. This is a textual citation refutation, independently consistent with L-02.

### Limits

- The refutation is documentary: Lean is not being claimed to interpret the English paragraph.
- Approval absence at cutoff does not imply fraud or establish subsequent approval history.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Correct the citation summary to say I-01 identifies missing approvals for P03 and P04 at the cutoff.

## C03-08

### Exact report claim

`input/report.md#C03-08`

> **C03-08.** Annex C confirms that both missing approvals were obtained after the cutoff. Citation: annex register A-01.

### Verification question

Does the supplied evidence establish Annex C’s contents or that both missing approvals were obtained after the cutoff?

### Source evidence

- [input/sources/annex-register.md](input/sources/annex-register.md) — `A-01`

> ## A-01 — Missing material
> The report packet index lists Annex C, titled “Post-cutoff approval follow-up.” Annex C is not included in the supplied packet. The register records no finding about whether either missing approval was subsequently obtained.

- [input/sources/annex-register.md](input/sources/annex-register.md) — `A-02`

> ## A-02 — Available packet
> The supplied substantive evidence consists of the sampled ledger, the review method, the inspection note, and this annex register. The register's listing of a document is evidence of that listing, not evidence of its contents.

- [input/sources/inspection.md](input/sources/inspection.md) — `I-01`

> ## I-01 — Inspection result
> All four sampled payments matched their invoices. Required approvals were absent for P03 and P04 at the cutoff; approvals were present for P01 and P02. The absence of an approval does not by itself establish fraud.

### Rules

- A document-index entry establishes a listing, not the document’s contents.
- Absence of supplied evidence does not establish that later approvals did or did not occur.

### Assumptions

- The supplied synthetic documents accurately describe the stated sample and cutoff; this audit does not independently authenticate them.

### Reasoning

- 1. A-01 lists Annex C under the title “Post-cutoff approval follow-up,” but explicitly says Annex C is not included.
- 2. The same paragraph records no finding about whether either approval was subsequently obtained; A-02 expressly distinguishes listing from contents.
- 3. I-01 establishes only approval absence at cutoff. Reading the complete supplied packet finds no follow-up approval evidence.
- 4. The report’s claim about confirmation in Annex C and the underlying subsequent approvals is therefore insufficiently supported and remains undetermined. Missing material is not a refutation of later approval.

### Limits

- Annex C is unavailable; its content and the subsequent approval events cannot be inferred.
- The title does not establish that both, one, or neither approval was obtained.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Obtain Annex C and underlying dated approval records; until then identify post-cutoff clearance as unverified.

## C03-09

### Exact report claim

`input/report.md#C03-09`

> **C03-09.** The invoice matching process is impressively elegant. Citation: inspection I-02.

### Verification question

Is “impressively elegant” an operationally defined, evidence-verifiable assessment here?

### Source evidence

- [input/sources/inspection.md](input/sources/inspection.md) — `I-02`

> ## I-02 — Reviewer observation
> The reviewer described the invoice matching process as orderly. This qualitative description was not an assessment of whether the approval control was adequate across the population.

### Rules

- No supplied source or brief defines a measurable criterion for elegance.
- Preserve qualitative observations as attributed judgments; do not convert them into control-effectiveness claims.

### Assumptions

None stated.

### Reasoning

- 1. I-02 attributes the description “orderly” to a reviewer.
- 2. “Impressively elegant” is an evaluative embellishment without an operational standard in the supplied corpus.
- 3. This subjective judgment is not classified as a true or false finite proposition. It receives no formal proof and implies nothing about population-wide approval controls.

### Limits

- No objective elegance criterion or audience preference is supplied.
- I-02 explicitly disclaims a population-wide control adequacy assessment.

### Result

Semantic state: **not_applicable**; argument status: **nonformal**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Label this as the report author’s subjective assessment, or use the accurately attributed reviewer description “orderly.”

## C03-10

### Exact report claim

`input/report.md#C03-10`

> **C03-10.** At least two entries in the 20-entry population had missing required approvals at the cutoff. Citations: ledger L-01, L-02.

### Verification question

Does the known sample establish at least two missing-approval entries in the twenty-entry population at cutoff?

### Source evidence

- [input/sources/ledger.md](input/sources/ledger.md) — `L-01`

> ## L-01 — Cutoff and coverage
> At the 30 June 2031 audit cutoff, the target population contained exactly 20 paid entries. The following four entries are the complete selected sample. No values for unsampled entries are included in this extract.

- [input/sources/ledger.md](input/sources/ledger.md) — `L-02`

> ## L-02 — Exact amounts and approval status
> | Entry | Paid amount, euro cents | Required approval present at cutoff |
> | --- | ---: | --- |
> | P01 | 120000 | Yes |
> | P02 | 80000 | Yes |
> | P03 | 50000 | No |
> | P04 | 25000 | No |

- [input/sources/inspection.md](input/sources/inspection.md) — `I-01`

> ## I-01 — Inspection result
> All four sampled payments matched their invoices. Required approvals were absent for P03 and P04 at the cutoff; approvals were present for P01 and P02. The absence of an approval does not by itself establish fraud.

### Rules

- The four distinct sample entries belong to the target population described in L-01.
- Known missing approvals in a subset provide a lower bound for the whole domain; unknown additional entries cannot subtract known exceptions.

### Assumptions

- Sample identifiers denote distinct population entries, as the L-01/L-02 sample representation indicates.
- The unknown additional exception count is a nonnegative integer no greater than sixteen.

### Reasoning

- 1. L-01 identifies the four listed entries as the selected sample of a twenty-entry population.
- 2. P03 and P04 are two distinct sample members missing required approvals at the cutoff, as L-02 and I-01 agree.
- 3. Write the population exception count as 2+n, where n is the unknown exception count among sixteen other entries and 0≤n≤16.
- 4. For every such n, 2+n≥2. This lower bound is supported even though an exact population rate remains unknown.

### Limits

- The result supplies a lower bound only; it does not identify an exact population rate or any unsampled entry’s approval status.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.populationLowerBound` in module `Audit` (supports): `∀ unknownExceptions : Nat, unknownExceptions ≤ 16 → 2 ≤ Audit.populationExceptions unknownExceptions`.
  [Model](models/Audit.lean) · [Executed check](checks/Target016.lean) · [Actual proof log](logs/target-016.log)

### Recommendation

Retain this population lower bound and keep it separate from unsupported exact-rate extrapolation.
