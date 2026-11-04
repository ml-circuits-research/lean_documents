# Claim coverage


## Document extraction coverage

| Document | Source | State |
|---|---|---|
| D00001 | input/brief.md | ready |
| D00002 | input/report.md | ready |
| D00003 | input/sources/01-stock-rules.md | ready |
| D00004 | input/sources/02-opening-and-journal.md | ready |
| D00005 | input/sources/03-signed-counts.md | ready |
| D00006 | input/sources/04-receiving-messages.md | ready |
| D00007 | input/sources/05-custody-register.md | ready |
| D00008 | input/sources/06-shipping-tickets-scan.pdf.md | partial |
| D00009 | input/sources/07-bin-and-exception-register.md | ready |

### D00008: partial

["pdf-page-0001: 5/235 OCR words are below confidence 85.", "OCR text is not independently verified against the original visual source, regardless of confidence.", "pdf-page-0002: 4/236 OCR words are below confidence 85.", "pdf-page-0003: 3/249 OCR words are below confidence 85.", "pdf-page-0004: 4/246 OCR words are below confidence 85.", "pdf-page-0005: 4/241 OCR words are below confidence 85."]

Reason: Original five pages visually inspected; pages 1–4 corrected and accepted with hash-bound manual transcriptions. Page 5 pale field not recovered reliably by OCR; accepted quantity also lacks receiver signature.

Impact: All fourteen report findings assessed. C08-ERR-11 remains undetermined, without direct formal claim. Other direct targets use visually checked pages 1–4 and/or independent complete text records. Raw OCR and original bytes remain intact.


## Claim outcomes

| Claim | Semantic state | Argument status | Formal status |
|---|---|---|---|
| C08-ERR-01 | supported | sufficient | proved |
| C08-ERR-02 | refuted | invalid_inference | refuted |
| C08-ERR-03 | refuted | invalid_inference | refuted |
| C08-ERR-04 | refuted | invalid_inference | refuted |
| C08-ERR-05 | refuted | invalid_inference | refuted |
| C08-ERR-06 | supported | sufficient | proved |
| C08-ERR-07 | refuted | invalid_inference | refuted |
| C08-ERR-08 | refuted | invalid_inference | refuted |
| C08-ERR-09 | both | disputed | blocked |
| C08-ERR-10 | undetermined | insufficient_support | blocked |
| C08-ERR-11 | undetermined | insufficient_support | blocked |
| C08-ERR-12 | refuted | invalid_inference | refuted |
| C08-ERR-13 | refuted | invalid_inference | refuted |
| C08-ERR-14 | not_applicable | nonformal | not_attempted |

Coverage enumerates submitted findings; it does not establish that every report claim was identified.
