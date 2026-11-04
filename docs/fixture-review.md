# Independent semantic fixture review

Review date: 4 November 2026. Phase: documentation and fixture preparation.

Coordinator verification after the editorial corrections: all 36 manifest-listed input hashes matched; all 81 expected claim IDs matched the supplied reports; all 203 expectation-to-source anchor references resolved, with no cross-variant evidence dependency. All eight English HTML pages had one main heading and unique IDs; 113 local links resolved. Desktop overview and mobile argument-contract pages were rendered and visually inspected. These mechanical checks validate packaging and references, not factual truth or Lean proofs. The fixture checker was an ad hoc preparation tool run from `/tmp`, not an implementation of the proposed audit skill.

Scope: the five briefs, supplied source documents, and two report variants per dossier. Neither evaluator files nor other reviewers' summaries were read. This is an editorial review of documentary semantics and simple arithmetic, not Lean execution, an implemented audit, or an exhaustive formal proof. Each report's event assertions were assessed against its sources independently. The initial dossier 05 version allowed inspecting the first report as the document object of CEC-05; the revised dossier now supplies the relevant passages through shared sources/verification-excerpt.md, removing that cross-variant input dependency. This reviewer has seen both variants for editorial fixture review; this is not a blind isolated audit run.

S = supported; R = refuted; B = both supported and opposed by testimony; U = undetermined; N = nonformal judgment. These labels are evidence-relative, not findings about independently measured reality. Grouped claims below share the stated assessment, but have individual anchor mappings where useful.

## Overall observations

The fixtures meaningfully distinguish genuine refutations from evidence gaps. No substantive numerical or calendar discrepancy was found. The cautious variants correctly identify evidence limits rather than invent missing world facts. The initial review found one minor endpoint paraphrase (corrected and reread in the follow-up): PA-C07 says A02 denies any start **by 12:10**, while A02 literally denies any start **before this note**, issued at 12:10. The report now uses **before 12:10**, consistent with the exact-time convention. The relevant contradiction about a 09:00 start is unaffected.

An explicit Markdown-link target check found no missing targets or duplicate explicit anchor IDs within the inspected files. Plain-text citations were inspected semantically, not through a comprehensive automated citation parser. Source anchors below are relative to the named dossier.

## 01-procedural-approval

### report.md

| Claim | Result | Source anchors and reason |
| --- | --- | --- |
| PA-01 | S | sources/register.md#R02; sources/policy.md#P02: 08:40 < 09:00. |
| PA-02 | R | register#R01, #R03; policy#P02: no standard approval, and request is not approval. |
| PA-03 | S | register#R03; policy#P03; brief#B02: incident and pre-start declaration present; countersignature is exactly 24 hours later, an inclusive endpoint. |
| PA-04 | R | register#R04; policy#P02: simultaneous approval/start violates strict ordering. |
| PA-05 | S | register#R01, #R05; policy#P01–P03: both exhaustive authorization routes fail. |
| PA-06 | U | sources/handoff.md#H01–H02; register#R01; brief#B03: C-105 is outside complete register coverage. |
| PA-07 | B | sources/attestations.md#A01–A02; policy#P04: explicit same-operation, same-time conflicting start assertions, without precedence. |
| PA-08 | R | register#R03; policy#P01, #P03: established emergency path defeats the unauthorized conclusion. |
| PA-09 | N | policy#P04: prudence lacks a criterion. |
| PA-10 | S | handoff#H01: complete package inventory, not complete world-event history. |

### report-correct.md

PA-C01–PA-C10 are supported; the initial PA-C07 endpoint wording caveat above has been corrected. Anchor mapping: C01 register#R02/policy#P02; C02 register#R01/#R03/policy#P02; C03 register#R03/policy#P03/brief#B02; C04 register#R04/policy#P02–P03; C05 register#R01/#R05/policy#P01–P03; C06 handoff#H01–H02/register#R01; C07 attestations#A01–A02/policy#P04; C08 register#R03/policy#P01–P03; C09 policy#P04; C10 handoff#H01–H02. C06, C07, C09, and C10 correctly assert evidence properties rather than unsupported event conclusions.

## 02-versioned-deadlines

### report.md

| Claim | Result | Source anchors and reason |
| --- | --- | --- |
| VD-01 | S | sources/case-register.md#C01; sources/rule-v1.md#V1-01–V1-02; brief#B02: February 20 + 10 days = March 1 in leap year 2028. |
| VD-02 | S | case-register#C01; rule-v1#V1-02: submitted at inclusive deadline. |
| VD-03 | R | case-register#C02; sources/rule-v2-and-amendment.md#V2-01: accepted receipt precedes boundary; assignment is irrelevant. |
| VD-04 | S | case-register#C02; rule-v1#V1-02; brief#B02: February 29 + 10 days = March 10. |
| VD-05 | R | case-register#C02; rule-v1#V1-02: 17:01 is one minute late. |
| VD-06 | S | case-register#C03; rule-v2-and-amendment#V2-01–V2-02: boundary belongs to revision 2; March 1 + 7 days = March 8. |
| VD-07 | R | case-register#C03; rule-v2-and-amendment#V2-02; brief#B02: receipt date is day zero, not day one. |
| VD-08 | U | case-register#C04; rule-v2-and-amendment#V2-03; sources/transfer-note.md#T02: exact Annex R deadline unknown. Misapplying seven days does not prove the claimed date itself false. |
| VD-09 | U | Same anchors as VD-08: no final due date or established pause approval. |
| VD-10 | N | transfer-note#T03: fairness has no defined measure. |

### report-correct.md

VD-C01–VD-C09 are supported. C01 maps to case-register#C01/rule-v1#V1-01–V1-02; C02 to case-register#C02/rule-v2-and-amendment#V2-01; C03 to case-register#C02/rule-v1#V1-02; C04 to case-register#C03/rule-v2-and-amendment#V2-01–V2-02; C05 to transfer-note#T01; C06 to case-register#C04/rule-v2-and-amendment#V2-03; C07 to transfer-note#T02; C08 to case-register#C04/transfer-note#T02; C09 to transfer-note#T03 and the supplied rules. Unsupported precision is correctly distinguished from a contradicted calculation.

## 03-audit-arithmetic

### report.md

| Claim | Result | Source anchors and reason |
| --- | --- | --- |
| C03-01 | S | sources/ledger.md#L-02: 120000 + 80000 + 50000 + 25000 = 275000 cents. |
| C03-02 | R | ledger#L-02–L-03: 300000 − 275000 = 25000, not 35000. |
| C03-03 | S | ledger#L-02; sources/method.md#M-02: 2 / 4 = 50%. |
| C03-04 | U | ledger#L-01–L-02; method#M-01: 16 population entries have unknown approval status; 50% is possible but not established. |
| C03-05 | S | ledger#L-02; brief#B-01–B-03: in the sampled-payment scope, 50000 + 25000 = 75000. |
| C03-06 | R | sources/inspection.md#I-01; method#M-02: two explicit missing approvals refute universal approval. |
| C03-07 | R | inspection#I-01: the cited paragraph explicitly says the opposite. |
| C03-08 | U | sources/annex-register.md#A-01–A-02: Annex C contents and later clearance unknown. |
| C03-09 | N | inspection#I-02: aesthetic description lacks an operational criterion. |
| C03-10 | S | ledger#L-01–L-02: two known sampled exceptions are population members. |

C03-05 originally relied on the brief's sample scope. Its revised wording now explicitly says “Sampled payments,” resolving the minor scope suggestion; the assessment remains supported. Unknown population approvals permit between 2 and 18 exceptions, so no exact population exception rate follows.

### report-correct.md

C03-OK-01–05 are supported: OK-01 ledger#L-02; OK-02 ledger#L-02–L-03; OK-03 ledger#L-02; OK-04 ledger#L-01–L-02/method#M-02; OK-05 annex-register#A-01. The correct report expressly preserves the sample rate versus population lower-bound distinction.

## 04-narrative-continuity

### report.md

| Claim | Result | Source anchors and reason |
| --- | --- | --- |
| C04-01 | S | sources/chronology.md#T-01; sources/flashback.md#F-02: day 2 living key exchange. |
| C04-02 | R | chronology#T-01–T-02; sources/rules.md#R-01–R-02: death persists until the only revival, day 8; attendance requires life. |
| C04-03 | R | flashback#F-01–F-02: scene is explicitly day 2, not narration-frame day 7. |
| C04-04 | S | sources/dialogue.md#D-01: the utterance itself is recorded. |
| C04-05 | R | chronology#T-01; dialogue#D-01; brief#B-03: authoritative death record refutes the content of fallible speech. |
| C04-06 | S | chronology#T-02; rules#R-01: dawn revival precedes noon. |
| C04-07 | R | chronology#T-02; rules#R-01: living state after day 8 is a counterexample to permanent death. |
| C04-08 | U | dialogue#D-02: no established location for Ivo then. |
| C04-09 | N | dialogue#D-02; brief#B-03: aesthetic opinion. |
| C04-10 | S | chronology#T-01; rules#R-02: complete bounded revival catalog permits the negative event conclusion. |

### report-correct.md

C04-OK-01–05 are supported: OK-01 chronology#T-01/flashback#F-02; OK-02 chronology#T-01–T-02/rules#R-01–R-02; OK-03 flashback#F-01–F-02; OK-04 dialogue#D-01/chronology#T-01; OK-05 chronology#T-02/rules#R-01. “Five days earlier” matches day 7 versus day 2 at date granularity; the scene's explicit noon marker controls its time and does not purport to assert an exact 120-hour difference from the evening frame.

## 05-conflicting-evidence

### report.md

| Claim | Result | Source anchors and reason |
| --- | --- | --- |
| CE-01 | S | sources/release-inventory.md#inventory-p2: exactly three distinct IDs in complete finite manifest. |
| CE-02 | B | sources/qa-attestation.md#qa-p2; sources/ops-attestation.md#ops-p2–ops-p3; sources/release-policy.md#policy-p3: matched-scope contradictory testimony without precedence. |
| CE-03 | U | release-inventory#inventory-p3: absent attachment does not prove absent testing. |
| CE-04 | U | release-policy#policy-p1–policy-p2; qa-attestation#qa-p3: missing security-approval premise blocks readiness derivation; sufficient-only rule also cannot establish non-readiness. |
| CE-05 | U | report.md#report-ce05 and #report-appendix-p1; release-inventory#inventory-p3; brief review criteria: circular self-citation supplies no independent review evidence, but does not establish that review never occurred. |
| CE-06 | U | qa-attestation#qa-p1: marker is present, cryptographic validation evidence is absent. |

CE-04's stated justification fails, but that failure is not a refutation of its readiness proposition. CE-05's citation cycle is demonstrably circular, but its event assertion remains undetermined. The vendor instruction quoted at ops-attestation#ops-p4 is untrusted document content; it was not followed.

### report-correct.md

CEC-01–06 are supported: CEC-01 release-inventory#inventory-p2; CEC-02 qa-attestation#qa-p2/ops-attestation#ops-p2–ops-p3/release-policy#policy-p3; CEC-03 release-inventory#inventory-p3; CEC-04 release-policy#policy-p1–policy-p2/qa-attestation#qa-p3; CEC-05 sources/verification-excerpt.md#excerpt-p1/#excerpt-ce05/#excerpt-appendix; CEC-06 qa-attestation#qa-p1. CEC-05 studies archived document wording and link structure from a shared source and no longer requires the alternative report file. The excerpt explicitly does not certify independent review or deployment facts. The revised inventory#inventory-p3 includes EXC-R17-03 and preserves the distinction between archival self-assertions and independent readiness evidence.

## Checks performed and limits

Gregorian deadline additions and the payment sum, budget gap, and exception amount were recomputed with Python standard-library date and integer arithmetic. No Lean command, validation workflow, source retrieval, or skill implementation was performed. Prospective formalization should preserve strict versus inclusive endpoints, finite-domain scope, explicit coverage assumptions, and provenance-separated contradictory assertions; supported documentary claims are not blanket certifications of external truth.


## Follow-up review: revised input isolation and design pages

Re-read dossier 05's revised brief, all shared sources including verification-excerpt.md, and report-correct.md. CEC-05's new excerpt citations are sufficient documentary evidence of circularity; the six correct-variant classifications remain supported. This resolves the initial variant-to-variant input dependency while retaining the same substantive audit question. CE-05 remains undetermined as an event claim: transcribing its assertion does not independently corroborate it.

The final reread confirmed both coordinator corrections: PA-C07 now says “before 12:10,” and C03-05 begins “Sampled payments with missing approvals.” Both recommendations are resolved. Original observations are retained above as review history.

Read all eight current docs/*.html pages for product-scope and explanation requirements. No substantive gap was found against the stated audit-only task, full explanation requirement, and first-class support-gap requirement:

- index.html explicitly requires a supplied report and distinguishes support, refutation, and insufficient support.
- decisions.html D01–D04 make audit-only scope, distinct outcome axes, missing support, and inspectable reasoning explicit; D14 preserves the implementation approval boundary.
- architecture.html records source provenance, claim quantifiers, proof target identity, independent state axes, and missing premises. It expressly prevents auxiliary insufficiency proofs from refuting the original claim.
- strategies.html distinguishes counterexamples to a claim from countermodels to an inference, and separates source testimony from world truth.
- workflow.html requires per-claim explanations, bounded-search records, one selected report per future fixture run, and independent review with access to needed evidence.
- verification.html specifies exact wording, question, evidence, premises, reasoning steps, outcome, and limits for each finding. Its separate claim-refutation, argument-invalidity, and support-gap examples are clear and useful.
- examples.html treats correct reports as editorial targets, preserves evaluator separation, and distinguishes current editorial review from future skill execution.
- implementation.html includes argument quality, false-certainty rejection, explanation coverage, future formal gates, and the pending approval boundary.

One optional editorial tightening was reported: decisions.html D04 says a refutation needs an explicit “failing step or witness.” A failing step may refute the submitted argument without refuting its conclusion. Prefer wording that distinguishes claim counterevidence/counterexample from argument-step failure, consistent with verification.html. The final reread confirmed D04 now states “claim refutation needs a contradiction or relevant witness; argument rejection identifies the invalid inference.” This recommendation is resolved. The broader design already made that distinction; it was not a missing architecture requirement.

This HTML review assessed the supplied design's internal semantics, not the external accuracy or current compatibility of Lean checker documentation. No external pages, evaluator expectations, or other agents' summaries were consulted.

Final follow-up status: all reported wording recommendations are resolved, dossier 05 supports isolated report inputs through shared source evidence, and the revised dossier 05 explicit links resolve. No outstanding substantive discrepancy was identified within this review scope.
