# Claim coverage


## Document extraction coverage

| Document | Source | State |
|---|---|---|
| D00001 | input/brief.md | ready |
| D00002 | input/report.md | ready |
| D00003 | input/sources/containment-attestations.scan.pdf.md | partial |
| D00004 | input/sources/incident-timeline.md | ready |
| D00005 | input/sources/maintenance-authorization.pdf.md | ready |
| D00006 | input/sources/monitoring-coverage.md | ready |
| D00007 | input/sources/notification-register.md | ready |
| D00008 | input/sources/response-playbook.docx.md | ready |
| D00009 | input/sources/review-correspondence.md | ready |

### D00003: partial

["OCR text is not independently verified against the original visual source, regardless of confidence.", "pdf-page-0002: 3/88 OCR words are below confidence 85.", "pdf-page-0003: 5/93 OCR words are below confidence 85.", "pdf-page-0004: 1/98 OCR words are below confidence 85.", "pdf-page-0005: 1/98 OCR words are below confidence 85."]

Reason: All five scan pages are available and were viewed. Original OCR is marked partial because low-confidence words and visibly erroneous A01-A04/05:00/05:30 characters remain in the preserved machine extraction. Controlled manual transcription created four reviewed-0001 passages with source hashes and explicit visual-review records; the original OCR and histories are retained.

Impact: Only C07-15 relies materially on these attestations. The corrected source wording is readable and establishes opposing attributed claims, but visual correction cannot resolve the actual containment disagreement. No page was omitted; authentic signatures and exact 05:00 statements are not unconditional world truth. Other calculations use separately inspected authoritative sources.


## Claim outcomes

| Claim | Semantic state | Argument status | Formal status |
|---|---|---|---|
| C07-01 | supported | sufficient | proved |
| C07-02 | refuted | invalid_inference | refuted |
| C07-03 | supported | sufficient | proved |
| C07-04 | refuted | invalid_inference | refuted |
| C07-05 | refuted | invalid_inference | refuted |
| C07-06 | refuted | invalid_inference | refuted |
| C07-07 | refuted | invalid_inference | refuted |
| C07-08 | supported | sufficient | proved |
| C07-09 | refuted | invalid_inference | refuted |
| C07-10 | refuted | invalid_inference | refuted |
| C07-11 | refuted | invalid_inference | refuted |
| C07-12 | supported | sufficient | proved |
| C07-13 | refuted | invalid_inference | refuted |
| C07-14 | supported | sufficient | proved |
| C07-15 | both | disputed | auxiliary |
| C07-16 | undetermined | insufficient_support | auxiliary |
| C07-17 | undetermined | insufficient_support | auxiliary |
| C07-18 | not_applicable | nonformal | not_attempted |

Coverage enumerates submitted findings; it does not establish that every report claim was identified.
