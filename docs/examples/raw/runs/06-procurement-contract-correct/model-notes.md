# Model notes and correspondence review

## Scope and source trust

The model concerns the finite synthetic HPS dossier for May-June 2029. It does not create a substantive procurement report. Every result maps to a supplied report claim group; component statements remain in findings.json and claims.json. Documentary corroboration and limits are stated separately from the arithmetic/formal target. Sources remain immutable, including original imperfect OCR; append-only reviewed transcriptions provide the cited A01-A04 text.

The author visually inspected all material scan pages and searchable PDF clauses and read the original DOCX XML. Hash-bound decisions appear in extraction-review.json. Visual inspection found A01-A04 markers misread as AQ labels, 10:00/11:00 misread with @, Tomas's signing time 14:30 misread14:38, and L01 misreadL@1. The transcribe tool retained original passages, coordinate ancestry, original hashes, reviewed text hashes, snapshots and history. No approval-event ambiguity remains from those typography errors, but the source testimony itself genuinely conflicts. Signature authenticity is stipulated by A03 within the synthetic dossier; it is not cryptographically reverified by this audit.

## Arithmetic and aggregation

Currency values are nonnegative integer cents unless explicitly represented by numerator/denominator euros. `roundCents num den = (num*200+den)/(den*2)` implements nearest-cent half-up rounding for the concrete positive denominators. It performs exact rational multiplication before one integer division, never intermediate floating-point rounding. P04 is the operative rule; F01/F02 are corroboration only.

P13 exact amount/rate: V05 supplies USD 27777.775 =27777775/1000 and rate0.9=9/10, giving numerator249999975, denominator10000 euros. Its exact EUR 24999.9975 is below25000 before rounding, while normalized cents equal2500000. `p13Normalization` supports C03 arithmetic and threshold plus the certificate date9<commitment11 (June 10 beforeJune12), and finite competition-satisfied result using L03's complete certificate. `p13Intermediate` supports C04's contrasting comparisons; P04 establishes why the unrounded comparison is procedurally wrong. P14 exact24999994/1000 euros rounds to2499999 cents, checked by `p14Normalization` for C05, with its nonaggregation supplied by L03/F02.

`threshold` maps revision 1→2000000 and revision 2→2500000 cents (P02). `rackTotal` sums L02 normalized1240000+1260000. `rackAggregates` combines the explicitly true same-project, same-legal-supplier and same-operational-requirement facts from L02/F04, the19≤2+29 date window and prior knowledge at day-4<day 2. These booleans are source transcriptions, not inferred from coincident labels. `rackObligation` supports C01 and `rackSum` C02. The combined requirement was known May 28; June 3/June 20 commitments are17 dates apart. This is not an assertion that all purchases from one laboratory aggregate.

`competitionSatisfied rev value certificate exception` implements below-threshold or complete competition or established exception. False certificate/exception inputs for P11/P12 and R17 are justified by explicit none in L02/L05 under L01, not generic file omission. True certificate for P13 is the complete timely L03 certificate. `compliant` combines this condition with valid order approval per P08. It makes competition and approval separate conjuncts.

## Calendar and authority

The UTC minute origin is2029-06-01 00:00. `revisionAt` selects revision 1 for negative accepted-receipt minutes and revision 2 otherwise, following V01 for original scope. R17 is -1; R18 is0; R11 is540. June n is date offset n-1. Exact calendar-to-offset transcription was independently checked with Python datetime and manual counting in visual-review/independent-transcription-check.log. There are no imported weekends, grace periods, later-market rates or real procurement rules.

`expiry=14*1440+1020=21180` is June 15 17:00. `validDana` requires consumables, value≤1500000 cents, approval≤expiry and approval<commitment. Nat offsets restrict these particular modeled approvals to at/after June 1; the predicate is not claimed to govern pre-origin approvals. D01 provides the interval/category/limit, D02 rules out amendments and D03 fixes exact minute boundaries. `p15Approval` supports C06 at 21180<21181. `p16ApprovalFailure` supports C07: value ceiling holds, but21181>21180, and `p16ValidApproval` combines invalid Dana approval with false alternative approval from explicit complete L04. No approval inference is drawn from a missing folder alone.

R17's false added-requirement/price-increase fields come from visually reviewed V03 and V02. `r17Version` supports C08; `r17CompetitionFailure` supports C09 by revision 1 threshold violation and a false competition condition despite true director approval. `r18NoCompetition` supports C10 at boundary0 with2250000<2500000 and explicit nonaggregation V04. Both source requisitions are nonempty concrete witnesses; the model does not conflate their identical values or commitment dates.

## Urgent exception

`urgentException` is active incident, declaration exists, review exists, declaration strictly before commitment, review at/after commitment and review≤commitment+2880 minutes. X01 supplies confirmed active risk, X02 explicitly supplies both declaration and a separate order-approval decision in EM19. Their time is June 22 09:45=30825; commitment10:00=30840; review June 24 10:00=33720. `e19Exception` supports C11's temporal conjunction and exact48 h elapsed interval; P05 plus the instrument's explicit second decision supplies separate approval, not an inference from emergency declaration alone. `urgencyInsufficient` is an auxiliary counterexample for C12 with incident true and declaration/review false; it does not negate the actual E19 records. C11's checked target and X02 establish those actual additional conditions.

## Missing definitions, testimony and payment

`CompatibilityTest.warranty` and `.physical` are illustrative possible meanings, not claimed Annex Q contents. `onlyCompatible` records the two readings of X03/X04: sole certification allows true under a warranty-based exclusivity reading, while a physically functional rival gives false under a physical-function reading. `compatibilityOpen` is auxiliary for C13/C14. P07 reserves actual certification/test/treatment to missing Annex Q; V06 and X05 establish only missing supplied definition/determination. The concrete two-reading computation is not proof of actual qualification or disqualification, nor an exhaustive classification of possible Annex Q rules.

`ApprovalStatement` separates attributed approval assertions from event truth. Mara and Tomas share order21, date offset26 (June 27), approval-minute600 (10:00); asserted polarities are true/false and both retracted=false. These are visually reviewed A01-A03 transcriptions. `approvalConflict` supports C15's exact-event contradiction and unretracted status; absence of precedence/adjudication is documented in A03, not chosen by the model. No inconsistent world premises are introduced. P21 is explicitly outside L01 completeness.

`PaymentWorld` holds invoice and delivery true while universally varying paid. `paymentOpen` is auxiliary for C16: it constructs both possible payment outcomes from the same limited document facts. P01/A04/F03 justify the missing linkage and finance's uncertainty. There is no closed-world premise for payment. Payment and nonpayment remain unresolved even if approval were later reconciled.

`objectiveFailures` checks C17's three separate compliance witnesses: rack competition false/approval true; R17 competition false/approval true; P16 competition satisfied below threshold/approval false. The report's exact named failures are supported; no blanket judgment on P21/E20 or the entire organization follows. C18 accurately attributes management opinion and the absent standard metric. The qualified document-content claim is supported, while the underlying adjectives are nonformal and have no Lean target.

## Execution limits

Actual checks and logs are retained separately in proof-results.json and logs/. Kernel success proves the supplied target types against this transcription and rule interpretation; it does not establish source authenticity or replace independent semantic review. No external kernel implementation is claimed. Source review was done by the model author; independent correspondence review remains unavailable and is expressly documented in semantic-review.md.

Executed validation: Lean 4.24.0 passed all sixteen declared-theorem audits and all seventeen finding target-type checks (33 checks total). Every referenced/dependent theorem has an empty axiom list. The actual version/build/check output is retained in proof-results.json and logs/.
