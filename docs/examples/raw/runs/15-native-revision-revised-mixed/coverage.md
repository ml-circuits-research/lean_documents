# Claim coverage

## Registered claim coverage

Coverage: **complete_registration**; 8 reviewed anchors; 7 audited and 0 deferred claims.

Registration reconciles declared claims and reviewed report anchors; it does not establish semantic completeness, faithful decomposition, or that declared searches were actually performed.

- `R1`: claims — The first sentence is the independently audited conclusion; remaining exact premises, citations and inference are audited as argument obligations below.
- `R2`: claims — The first sentence is the independently audited conclusion; remaining exact premises, citations and inference are audited as argument obligations below.
- `R3`: claims — The first sentence is the independently audited conclusion; remaining exact premises, citations and inference are audited as argument obligations below.
- `R4`: claims — The first sentence is the independently audited conclusion; remaining exact premises, citations and inference are audited as argument obligations below.
- `R5`: claims — The first sentence is the independently audited conclusion; remaining exact premises, citations and inference are audited as argument obligations below.
- `R6`: claims — The first sentence is the independently audited conclusion; remaining exact premises, citations and inference are audited as argument obligations below.
- `R7`: claims — The first sentence is the independently audited conclusion; remaining exact premises, citations and inference are audited as argument obligations below.
- `document-preamble`: non_claim — Document title only.

## Document extraction coverage

| Document | Source | State |
|---|---|---|
| D00001 | input/report.md | ready |
| D00002 | input/sources/01-policy.docx.md | ready |
| D00003 | input/sources/02-ledger.pdf.md | ready |
| D00004 | input/sources/03-receipt-scan.pdf.md | partial |

### D00004: partial

["pdf-page-0001: 2/41 OCR words are below confidence 85.", "OCR text is not independently verified against the original visual source, regardless of confidence."]

Reason: OCR misreads transfer T7 as 17; the original scan was visually inspected and a reviewed full-page transcription was added while preserving OCR. Low-confidence extraction remains partial.

Impact: Receipt-dependent conclusions use the reviewed transcription, not the mistaken identifier. No claim of globally perfect OCR or machine-certified complete ingestion is made.


## Claim outcomes

| Claim | Semantic state | Argument status | Formal status |
|---|---|---|---|
| R1 | refuted | unsound_argument | refuted |
| R2 | refuted | invalid_inference | refuted |
| R3 | supported | sufficient | proved |
| R4 | refuted | unsound_argument | refuted |
| R5 | undetermined | unsound_argument | auxiliary |
| R6 | supported | insufficient_support | proved |
| R7 | not_applicable | nonformal | not_attempted |

Coverage enumerates submitted findings; it does not establish that every report claim was identified.
