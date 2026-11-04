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

Reason: OCR ingestion remains partial due low-confidence characters and omitted pale bottom D quantity field. Every original scan page was actually viewed. Five controlled reviewed-0001 transcriptions correct legible markers/time/punctuation; original OCR and histories remain. Page5 reviewed text covers the legible main text, not a definitive transcription of the pale bottom field.

Impact: The exact A/B container counts and signed movement stages used for formal arithmetic were legible and corroborated by journal/correspondence. The faint D numeral is not promoted into accepted quantity: receiver acceptance is blank, unsigned messages differ, and recount evidence is missing. C08-OK-11 explicitly reports this unresolved acceptance; no numeric proof uses a guessed D amount. No page is omitted, but no complete visual-to-text extraction of the pale field is claimed.


## Claim outcomes

| Claim | Semantic state | Argument status | Formal status |
|---|---|---|---|
| C08-OK-01 | supported | sufficient | proved |
| C08-OK-02 | supported | sufficient | proved |
| C08-OK-03 | supported | sufficient | proved |
| C08-OK-04 | supported | sufficient | proved |
| C08-OK-05 | supported | sufficient | proved |
| C08-OK-06 | supported | sufficient | proved |
| C08-OK-07 | supported | sufficient | proved |
| C08-OK-08 | supported | sufficient | proved |
| C08-OK-09 | supported | sufficient | proved |
| C08-OK-10 | supported | sufficient | proved |
| C08-OK-11 | supported | sufficient | auxiliary |
| C08-OK-12 | supported | sufficient | proved |
| C08-OK-13 | supported | sufficient | proved |
| C08-OK-14 | supported | sufficient | proved |

Coverage enumerates submitted findings; it does not establish that every report claim was identified.
