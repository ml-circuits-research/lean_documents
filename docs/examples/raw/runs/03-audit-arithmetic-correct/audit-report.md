# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

[Semantic correspondence review](semantic-review.md)

## C03-OK-01

### Exact report claim

`input/report.md#C03-OK-01`

> **C03-OK-01.** The four sampled payments total exactly 275000 euro cents. Citation: ledger L-02.

### Verification question

Do the four complete sampled entries at the cutoff total exactly 275000 euro cents?

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

- Sum each of the four distinct in-scope entries exactly once; 100 cents equal EUR 1.00.

### Assumptions

- The supplied ledger accurately transcribes the four complete selected sample entries and their approval status at the 30 June 2031 cutoff; document authenticity is outside this audit.
- Amounts are exact nonnegative integer euro cents, without rounding or unstated adjustments.

### Reasoning

- 1. L-01 identifies four entries as the complete selected sample; L-02 gives P01=120000, P02=80000, P03=50000 and P04=25000 cents.
- 2. 120000 + 80000 = 200000; 50000 + 25000 = 75000; 200000 + 75000 = 275000.
- 3. The report citation L-02 supports the transcribed values and the resulting exact total; no supplied source contradicts them.

### Limits

- The proof establishes arithmetic on the supplied finite records, not source authenticity, population amounts or later events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.sampleTotal` in module `Audit` (supports): `Audit.total Audit.sample = 275000`.
  [Model](models/Audit.lean) · [Executed check](checks/Target007.lean) · [Actual proof log](logs/target-007.log)

### Recommendation

Retain the exact total and cite L-01 alongside L-02 to make completeness explicit.

## C03-OK-02

### Exact report claim

`input/report.md#C03-OK-02`

> **C03-OK-02.** The 300000-cent comparison budget exceeds the sampled payments by exactly 25000 euro cents. Citations: ledger L-02, L-03.

### Verification question

Does the sample comparison budget exceed the four sampled payments by exactly 25000 cents?

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

- [input/sources/ledger.md](input/sources/ledger.md) — `L-03`

> ## L-03 — Budget reference
> The budget used for the sample comparison is exactly 300000 euro cents. This budget is a comparison reference for these four entries only, not a statement of the population budget.

### Rules

- Budget difference is comparison budget minus the sum of four sampled payments; L-03 restricts this budget to the sample comparison.

### Assumptions

- The supplied ledger accurately transcribes the four complete selected sample entries and their approval status at the 30 June 2031 cutoff; document authenticity is outside this audit.
- Amounts are exact nonnegative integer euro cents, without rounding or unstated adjustments.

### Reasoning

- 1. L-03 supplies a 300000-cent comparison budget, while L-02 yields a sampled total of 275000 cents.
- 2. 275000 ≤ 300000, so subtraction is a nonnegative excess and natural-number subtraction does not truncate a negative value.
- 3. 300000 - 275000 = 25000 cents. The report comparison is exact and confined to its proper sample domain.

### Limits

- The proof establishes arithmetic on the supplied finite records, not source authenticity, population amounts or later events.
- No population budget or population budget variance is supplied or inferred.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.budgetDifference` in module `Audit` (supports): `Audit.total Audit.sample ≤ Audit.budget ∧ Audit.budget - Audit.total Audit.sample = 25000`.
  [Model](models/Audit.lean) · [Executed check](checks/Target008.lean) · [Actual proof log](logs/target-008.log)

### Recommendation

Retain the 25000-cent sample difference and its sample-only qualification.

## C03-OK-03a

### Exact report claim

`input/report.md#C03-OK-03`

> **C03-OK-03.** Exactly two of the four sampled entries had missing required approvals at the cutoff: P03 and P04. Their combined amount was 75000 euro cents. Citation: ledger L-02.

### Verification question

Are P03 and P04 exactly the two approval exceptions among the four sampled entries at the cutoff?

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

- [input/sources/inspection.md](input/sources/inspection.md) — `I-01`

> ## I-01 — Inspection result
> All four sampled payments matched their invoices. Required approvals were absent for P03 and P04 at the cutoff; approvals were present for P01 and P02. The absence of an approval does not by itself establish fraud.

### Rules

- M-02 counts one exception per entry with absent required approval, irrespective of amount.
- Invoice matching and required approval are separate controls; invoice matching cannot replace an approval.

### Assumptions

- The supplied ledger accurately transcribes the four complete selected sample entries and their approval status at the 30 June 2031 cutoff; document authenticity is outside this audit.
- Amounts are exact nonnegative integer euro cents, without rounding or unstated adjustments.

### Reasoning

- 1. L-02 states approvals present for P01 and P02 and absent for P03 and P04.
- 2. The complete four-entry domain therefore filters to exactly the distinct IDs P03 and P04, giving two exceptions out of four entries.
- 3. I-01 independently confirms these statuses. Its statement that all invoices matched does not contradict missing approvals because M-02 separates the controls.

### Limits

- The proof establishes arithmetic on the supplied finite records, not source authenticity, population amounts or later events.
- Missing approval alone does not establish fraud; later clearance and unsampled statuses are outside this claim.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.exactExceptions` in module `Audit` (supports): `Audit.sample.length = 4 ∧ Audit.exceptions.length = 2 ∧ Audit.exceptionIDs = [Audit.p03ID, Audit.p04ID]`.
  [Model](models/Audit.lean) · [Executed check](checks/Target009.lean) · [Actual proof log](logs/target-009.log)

### Recommendation

Retain the count and named exceptions with the cutoff explicitly attached.

## C03-OK-03b

### Exact report claim

`input/report.md#C03-OK-03`

> **C03-OK-03.** Exactly two of the four sampled entries had missing required approvals at the cutoff: P03 and P04. Their combined amount was 75000 euro cents. Citation: ledger L-02.

### Verification question

Do the two sampled approval-exception entries P03 and P04 have combined amount 75000 cents?

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

- [input/sources/inspection.md](input/sources/inspection.md) — `I-01`

> ## I-01 — Inspection result
> All four sampled payments matched their invoices. Required approvals were absent for P03 and P04 at the cutoff; approvals were present for P01 and P02. The absence of an approval does not by itself establish fraud.

### Rules

- Select entries by absent required approval, then sum their full paid amounts once; amount does not determine the exception count.

### Assumptions

- The supplied ledger accurately transcribes the four complete selected sample entries and their approval status at the 30 June 2031 cutoff; document authenticity is outside this audit.
- Amounts are exact nonnegative integer euro cents, without rounding or unstated adjustments.

### Reasoning

- 1. The approval filter identifies P03 and P04, confirmed by I-01.
- 2. Their amounts from L-02 are 50000 and 25000 cents, respectively.
- 3. 50000 + 25000 = 75000. This is the paid amount associated with exceptions, not a measured loss or fraud amount.

### Limits

- The proof establishes arithmetic on the supplied finite records, not source authenticity, population amounts or later events.
- The 75000-cent amount is neither established loss nor evidence of fraud.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.exceptionTotal` in module `Audit` (supports): `Audit.total Audit.exceptions = 75000`.
  [Model](models/Audit.lean) · [Executed check](checks/Target010.lean) · [Actual proof log](logs/target-010.log)

### Recommendation

Retain the combined amount as payments associated with the two exceptions.

## C03-OK-04a

### Exact report claim

`input/report.md#C03-OK-04`

> **C03-OK-04.** The sample approval exception rate is exactly 50%; at least two entries in the 20-entry population had missing approvals at the cutoff. These figures describe a sample rate and a population lower bound, respectively. Citations: ledger L-01, L-02; method M-02.

### Verification question

Is the exact sample approval exception rate 50 percent?

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

- [input/sources/method.md](input/sources/method.md) — `M-02`

> ## M-02 — Separate controls
> An invoice match and a required approval are separate controls. An invoice match alone does not establish that required approval was present. Missing approval counts as one approval exception per entry, irrespective of that entry's amount.

- [input/sources/inspection.md](input/sources/inspection.md) — `I-01`

> ## I-01 — Inspection result
> All four sampled payments matched their invoices. Required approvals were absent for P03 and P04 at the cutoff; approvals were present for P01 and P02. The absence of an approval does not by itself establish fraud.

### Rules

- Sample exception rate equals count of sampled entries with missing required approval divided by sample count, without amount weighting.
- M-01 provides judgment selection and disclaims representativeness for the other 16 entries.

### Assumptions

- The supplied ledger accurately transcribes the four complete selected sample entries and their approval status at the 30 June 2031 cutoff; document authenticity is outside this audit.
- Amounts are exact nonnegative integer euro cents, without rounding or unstated adjustments.

### Reasoning

- 1. The complete sample has four entries and the approval filter has exactly two exceptions.
- 2. The denominator is positive. Two divided by four equals one half, or 50 percent; exact cross multiplication is 2×100 = 4×50.
- 3. This statement is a sample rate. Neither invoice matching nor judgment-based selection warrants transferring that exact rate to the population.

### Limits

- The proof establishes arithmetic on the supplied finite records, not source authenticity, population amounts or later events.
- The 50 percent rate does not estimate or prove a 50 percent population rate. No sampling-based uncertainty or random-selection assumption is introduced.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.sampleRate` in module `Audit` (supports): `0 < Audit.sample.length ∧ Audit.exceptions.length * 100 = Audit.sample.length * 50`.
  [Model](models/Audit.lean) · [Executed check](checks/Target011.lean) · [Actual proof log](logs/target-011.log)

### Recommendation

Retain the 50 percent sample rate and keep it distinct from the population lower bound.

## C03-OK-04b

### Exact report claim

`input/report.md#C03-OK-04`

> **C03-OK-04.** The sample approval exception rate is exactly 50%; at least two entries in the 20-entry population had missing approvals at the cutoff. These figures describe a sample rate and a population lower bound, respectively. Citations: ledger L-01, L-02; method M-02.

### Verification question

Do the two named sampled approval exceptions establish at least two exceptions within the 20-entry population, with no exact population rate inferred?

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

- [input/sources/method.md](input/sources/method.md) — `M-02`

> ## M-02 — Separate controls
> An invoice match and a required approval are separate controls. An invoice match alone does not establish that required approval was present. Missing approval counts as one approval exception per entry, irrespective of that entry's amount.

- [input/sources/inspection.md](input/sources/inspection.md) — `I-01`

> ## I-01 — Inspection result
> All four sampled payments matched their invoices. Required approvals were absent for P03 and P04 at the cutoff; approvals were present for P01 and P02. The absence of an approval does not by itself establish fraud.

### Rules

- The four sampled entries are distinct members of the target population, so their two witnessed exceptions also belong to that population.
- The other 16 entries have unknown approval statuses; their exception count can be any integer from zero through sixteen.

### Assumptions

- The supplied ledger accurately transcribes the four complete selected sample entries and their approval status at the 30 June 2031 cutoff; document authenticity is outside this audit.
- Amounts are exact nonnegative integer euro cents, without rounding or unstated adjustments.
- Sample membership in the stated population is taken from L-01 and M-01; the two named sample exceptions are distinct population entries.

### Reasoning

- 1. P03 and P04 are two distinct sampled entries with required approval absent at the cutoff.
- 2. L-01 identifies the complete selected sample within a population of 20; M-01 explicitly identifies the other 16 entries. Thus these two sample witnesses are also population witnesses.
- 3. Let u be the number of approval exceptions among the 16 unsampled entries. Without knowing any of their statuses, 0 ≤ u ≤ 16 and the population count is 2+u.
- 4. For every such u, 2 ≤ 2+u ≤ 18. The report correctly gives a lower bound of two, while its 50 percent figure describes only the sample.

### Limits

- The proof establishes arithmetic on the supplied finite records, not source authenticity, population amounts or later events.
- The exact population exception count remains unknown, from 2 through 18. The two sampled entries with approvals rule out 19 or 20 exceptions. No unsampled status is set to false.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.populationLowerBound` in module `Audit` (supports): `∀ unsampledMissing : Nat, unsampledMissing ≤ 16 → 2 ≤ Audit.populationExceptions unsampledMissing ∧ Audit.populationExceptions unsampledMissing ≤ 18`.
  [Model](models/Audit.lean) · [Executed check](checks/Target012.lean) · [Actual proof log](logs/target-012.log)

### Recommendation

Retain the at-least-two population count and distinguish it from an exact count or population rate.

## C03-OK-05a

### Exact report claim

`input/report.md#C03-OK-05`

> **C03-OK-05.** Annex C is not included in the supplied packet, and the register records no finding about subsequent clearance. Citation: annex register A-01.

### Verification question

Does the supplied packet omit Annex C despite listing it in the packet index?

### Source evidence

- [input/sources/annex-register.md](input/sources/annex-register.md) — `A-01`

> ## A-01 — Missing material
> The report packet index lists Annex C, titled “Post-cutoff approval follow-up.” Annex C is not included in the supplied packet. The register records no finding about whether either missing approval was subsequently obtained.

- [input/sources/annex-register.md](input/sources/annex-register.md) — `A-02`

> ## A-02 — Available packet
> The supplied substantive evidence consists of the sampled ledger, the review method, the inspection note, and this annex register. The register's listing of a document is evidence of that listing, not evidence of its contents.

### Rules

- A document listing establishes the listing, not its contents. The supplied packet inventory can establish what was supplied without establishing facts inside an absent annex.

### Assumptions

- A-01 and A-02 are read as statements about this supplied packet, not all documents that may exist elsewhere.

### Reasoning

- 1. A-01 explicitly states that Annex C is listed and is not included in the supplied packet.
- 2. A-02 identifies the supplied substantive material as ledger, method, inspection note and annex register; none supplies Annex C contents.
- 3. The report accurately describes the omission and does not assert that Annex C never existed.

### Limits

- This is a directly sourced documentary finding, not a Lean theorem. The audit has no Annex C contents and makes no finding about their truth or meaning.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Retain the packet-absence statement; obtain Annex C if subsequent follow-up must be assessed.

## C03-OK-05b

### Exact report claim

`input/report.md#C03-OK-05`

> **C03-OK-05.** Annex C is not included in the supplied packet, and the register records no finding about subsequent clearance. Citation: annex register A-01.

### Verification question

Does the annex register record no finding about whether either missing approval was subsequently obtained?

### Source evidence

- [input/sources/annex-register.md](input/sources/annex-register.md) — `A-01`

> ## A-01 — Missing material
> The report packet index lists Annex C, titled “Post-cutoff approval follow-up.” Annex C is not included in the supplied packet. The register records no finding about whether either missing approval was subsequently obtained.

- [input/sources/annex-register.md](input/sources/annex-register.md) — `A-02`

> ## A-02 — Available packet
> The supplied substantive evidence consists of the sampled ledger, the review method, the inspection note, and this annex register. The register's listing of a document is evidence of that listing, not evidence of its contents.

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

- A-01 explicitly withholds a finding on subsequent approvals; silence about later events cannot establish either later clearance or lack of clearance.
- Cutoff status and subsequent status are different temporal propositions.

### Assumptions

- The scope is the supplied register and subsequent-clearance question, not an exhaustive search of real-world follow-up events.

### Reasoning

- 1. A-01 says the register records no finding about whether either missing approval was subsequently obtained.
- 2. L-02 and I-01 concern approval absence at the cutoff only. They cannot establish the later status.
- 3. A-02 prevents treating the annex listing as its contents. Therefore the report accurately describes the register, while actual later clearance remains undetermined.

### Limits

- The exact meta-level statement about register contents is supported. Whether either approval was later obtained remains undetermined; it is neither refuted nor proved by packet omission.
- No Lean target is needed for the literal document-content observation.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Retain the no-finding statement. To decide actual later clearance, obtain Annex C and dated approval evidence.
