# Claim coverage


## Document extraction coverage

| Document | Source | State |
|---|---|---|
| D00001 | input/brief.md | ready |
| D00002 | input/report.md | ready |
| D00003 | input/sources/approval-attestations.scan.pdf.md | partial |
| D00004 | input/sources/delegation-notice.md | ready |
| D00005 | input/sources/exception-file.md | ready |
| D00006 | input/sources/procurement-standard.docx.md | ready |
| D00007 | input/sources/purchase-register.md | ready |
| D00008 | input/sources/reconciliation-correspondence.md | ready |
| D00009 | input/sources/revision-amendment.pdf.md | ready |

### D00003: partial

["OCR text is not independently verified against the original visual source, regardless of confidence.", "pdf-page-0002: 2/97 OCR words are below confidence 85.", "pdf-page-0003: 4/109 OCR words are below confidence 85.", "pdf-page-0004: 2/106 OCR words are below confidence 85.", "pdf-page-0005: 3/94 OCR words are below confidence 85."]

Reason: The image-only attestation PDF has complete page availability but OCR extraction remains marked partial because words on pages 2-5 fall below confidence 85. The initial TSV quotation-parsing defect was separately detected and retried with a repaired parser, retaining both attempts. Visual inspection of every original page identified A01-A04 marker mistakes, 10:0@/11:0@ time characters, 14:38 instead of 14:30, and L@1 instead of L01; All four corrections were applied through the controlled transcribe command to new pdf-page-0002-reviewed-0001 through pdf-page-0005-reviewed-0001 anchors. Original OCR, source bytes, review reasons and history snapshots are retained.

Impact: All five original pages were actually viewed. Material page content is readable, but erroneous OCR text must not be quoted as faithful source wording. C06-15 uses the exact positive/negative witness statements after controlled visual transcription, while C06-16 uses the packet-level payment-evidence limitation. The substantive approval conflict and missing settlement evidence remain unresolved even after transcription is corrected. No other claim depends on this scan. No page is omitted; raw OCR uncertainty and correction history remain disclosed, and this acknowledgement does not convert absence into a negative event fact.


## Claim outcomes

| Claim | Semantic state | Argument status | Formal status |
|---|---|---|---|
| C06-01 | refuted | invalid_inference | refuted |
| C06-02 | supported | sufficient | proved |
| C06-03 | supported | sufficient | proved |
| C06-04 | refuted | invalid_inference | refuted |
| C06-05 | refuted | invalid_inference | refuted |
| C06-06 | supported | sufficient | proved |
| C06-07 | refuted | invalid_inference | refuted |
| C06-08 | refuted | invalid_inference | refuted |
| C06-09 | supported | sufficient | proved |
| C06-10 | refuted | invalid_inference | refuted |
| C06-11 | supported | sufficient | proved |
| C06-12 | refuted | invalid_inference | refuted |
| C06-13 | undetermined | insufficient_support | auxiliary |
| C06-14 | undetermined | insufficient_support | auxiliary |
| C06-15 | both | disputed | auxiliary |
| C06-16 | undetermined | insufficient_support | auxiliary |
| C06-17 | refuted | invalid_inference | refuted |
| C06-18 | not_applicable | nonformal | not_attempted |

Coverage enumerates submitted findings; it does not establish that every report claim was identified.
