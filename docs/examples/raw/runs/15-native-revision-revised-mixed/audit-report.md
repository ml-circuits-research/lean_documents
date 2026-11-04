# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

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
[Semantic correspondence review](semantic-review.md)

Extraction inventory: 4 documents; 1 pending, partial or blocked. See [ingestion details](ingestion.json) and [coverage](coverage.md).

## R1

### Exact report claim

`input/report.md#R1`

> The total T7 charge is 130 credits.

### Verification question

Does the reported T7 total equal the current authoritative sum of A, B and C?

### Source evidence

- [input/sources/01-policy.docx.md](input/sources/01-policy.docx.md) — `docx-p-0002`

> P1: For transfer T7 on 4 November 2026, count the three ledger charges A, B and C once each, in whole credits. No tax, discount or currency conversion applies. A revised ledger explicitly supersedes the prior ledger for this transfer.

Original: [input/originals/D00002.docx](input/originals/D00002.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 2, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00002.docx", "original_sha256": "4a0cf796e8b3917bc1606f856a688d36c5d1aac4d82a6aba8e1576be91be5c42", "artifact_directory": "extraction/D00002/attempt-iak8g2wr"}`.

- [input/sources/02-ledger.pdf.md](input/sources/02-ledger.pdf.md) — `pdf-page-0001`

> Cedar laboratory T7 charge and quality ledger - revision 2
> Transfer date: 4 November 2026. Unit: whole credits.
> Charge A: 60 credits.
> Charge B: 40 credits.
> Charge C: 45 credits.
> This is the complete charge list for transfer T7. Count each line once.
> Quality approval: granted at 16:00 local time on 4 November 2026.
> Security approval status: not supplied. This ledger is not an approval-event history.
> Revision 2 supersedes revision 1 for T7. Charge C is corrected from 20 to 45 credits. All
> other fields remain unchanged.

Original: [input/originals/D00003.pdf](input/originals/D00003.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 1, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0001.bbox.xhtml", "total_pages": 1, "original": "input/originals/D00003.pdf", "original_sha256": "3c49680f3332d2f30535aff99f59c551c046d049fcc7e02444a446309cb8a6a4", "artifact_directory": "extraction/D00003/attempt-33t64ln6"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.


### R1: criteria and report argument audit

Criteria origin: **inferred**. Scope: Transfer T7, 4 November 2026; current supplied source revision only. No separate brief was supplied.

Does the reported T7 total equal the current authoritative sum of A, B and C?

- Decision criterion: P1: sum the complete current three-charge list once without adjustments.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **unsound**.

Report premise at `R1`:

> The ledger lists A as 60, B as 40 and C as 20 credits

Assessment: **contradicted**. The current ledger C value is 45. Revision 2 supersedes revision 1.

[evidence 1](input/sources/02-ledger.pdf.md) at `pdf-page-0001`

Report inference at `R1`:

> adding those lines gives 130 credits.

Assessment: **contradicted**. For the stated report operands 60+40+20=120. The asserted sum130 is arithmetically false, independently of the later C correction.

[evidence 1](input/sources/02-ledger.pdf.md) at `pdf-page-0001`

Independent audit reasoning:

- The applicable ledger revision records charges 60, 40 and 45 whole credits. P1 makes this a closed list of three charges, each counted once.
- Their sum is 145, so the exact report total 130 is contradicted by the complete charge list.
- The unchanged report also offers the now-superseded C=20 premise; revision 2 expressly supersedes revision 1. This is a source-version mismatch, not contradictory simultaneous ledgers.

[evidence 0](input/sources/01-policy.docx.md) at `docx-p-0002`, [evidence 1](input/sources/02-ledger.pdf.md) at `pdf-page-0001`, [proof 0: Audit.claim1](models/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: A small arithmetic or Boolean target checks the stated operational issue without assuming the conclusion.

- Proof 0 source-to-target correspondence: The applicable ledger revision records charges 60, 40 and 45 whole credits. P1 makes this a closed list of three charges, each counted once. Their sum is 145, so the exact report total 130 is contradicted by the complete charge list. The unchanged report also offers the now-superseded C=20 premise; revision 2 expressly supersedes revision 1. This is a source-version mismatch, not contradictory simultaneous ledgers. Source facts are assumptions of this translation; this target does not authenticate records.

Declared bounded support search: Read the exact report finding and all evidence passages listed here in context; checked current ledger version, governing rule and receipt where relevant.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/01-policy.docx.md](input/sources/01-policy.docx.md) at `docx-p-0002`.
- Inspected [input/sources/02-ledger.pdf.md](input/sources/02-ledger.pdf.md) at `pdf-page-0001`.

The applicable ledger revision records charges 60, 40 and 45 whole credits. P1 makes this a closed list of three charges, each counted once. Their sum is 145, so the exact report total 130 is contradicted by the complete charge list. The unchanged report also offers the now-superseded C=20 premise; revision 2 expressly supersedes revision 1. This is a source-version mismatch, not contradictory simultaneous ledgers.

Search limits: This is a bounded search of the supplied package, with no outside or missing approval-event records.

### Rules

- P1: sum the complete current three-charge list once without adjustments.

### Assumptions

- Interpret the supplied synthetic records as the authoritative documentary package for T7 on 4 November 2026.
- The manually reviewed source-to-symbol translation is faithful; Lean verifies only the encoded proposition.

### Reasoning

- The applicable ledger revision records charges 60, 40 and 45 whole credits. P1 makes this a closed list of three charges, each counted once.
- Their sum is 145, so the exact report total 130 is contradicted by the complete charge list.
- The unchanged report also offers the now-superseded C=20 premise; revision 2 expressly supersedes revision 1. This is a source-version mismatch, not contradictory simultaneous ledgers.

### Limits

- The dossier is synthetic; hashes and Lean do not authenticate real-world events.
- The auditor authored the fixture: this is a nonblind demonstration with a separate coordinator source-first/model review, not a blind accuracy benchmark.

### Result

Semantic state: **refuted**; argument status: **unsound_argument**; formal status: **refuted**.

### Formal evidence

- `Audit.claim1` in module `Audit` (refutes): `Audit.currentLedger.chargeA + Audit.currentLedger.chargeB + Audit.currentLedger.chargeC ≠ 130`.
  [Model](models/Audit.lean) · [Executed check](checks/Target007.lean) · [Actual proof log](logs/target-007.log)

### Recommendation

Replace the claim with the source-grounded result explained above; do not infer absent historical events.

## R2

### Exact report claim

`input/report.md#R2`

> Charge A complies with the individual-charge cap.

### Verification question

Does charge A satisfy the inclusive individual-charge cap?

### Source evidence

- [input/sources/01-policy.docx.md](input/sources/01-policy.docx.md) — `docx-p-0003`

> P2: Each individual charge must be at most 50 credits. A charge above 50 breaches the individual-charge cap; aggregate totals do not replace this test.

Original: [input/originals/D00002.docx](input/originals/D00002.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 3, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00002.docx", "original_sha256": "4a0cf796e8b3917bc1606f856a688d36c5d1aac4d82a6aba8e1576be91be5c42", "artifact_directory": "extraction/D00002/attempt-iak8g2wr"}`.

- [input/sources/02-ledger.pdf.md](input/sources/02-ledger.pdf.md) — `pdf-page-0001`

> Cedar laboratory T7 charge and quality ledger - revision 2
> Transfer date: 4 November 2026. Unit: whole credits.
> Charge A: 60 credits.
> Charge B: 40 credits.
> Charge C: 45 credits.
> This is the complete charge list for transfer T7. Count each line once.
> Quality approval: granted at 16:00 local time on 4 November 2026.
> Security approval status: not supplied. This ledger is not an approval-event history.
> Revision 2 supersedes revision 1 for T7. Charge C is corrected from 20 to 45 credits. All
> other fields remain unchanged.

Original: [input/originals/D00003.pdf](input/originals/D00003.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 1, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0001.bbox.xhtml", "total_pages": 1, "original": "input/originals/D00003.pdf", "original_sha256": "3c49680f3332d2f30535aff99f59c551c046d049fcc7e02444a446309cb8a6a4", "artifact_directory": "extraction/D00003/attempt-33t64ln6"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.


### R2: criteria and report argument audit

Criteria origin: **inferred**. Scope: Transfer T7, 4 November 2026; current supplied source revision only. No separate brief was supplied.

Does charge A satisfy the inclusive individual-charge cap?

- Decision criterion: P2: an individual charge complies exactly when it is at most 50 credits.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **invalid**.

Report premise at `R2`:

> Policy P2 sets the cap at 50 credits, and the ledger records A as 60 credits.

Assessment: **verified**. Both the inclusive cap50 and A60 premise match the sources.

[evidence 0](input/sources/01-policy.docx.md) at `docx-p-0003`, [evidence 1](input/sources/02-ledger.pdf.md) at `pdf-page-0001`

Report inference at `R2`:

> Charge A complies with the individual-charge cap.

Assessment: **contradicted**. 60>50, so breach follows and compliance does not.

[evidence 0](input/sources/01-policy.docx.md) at `docx-p-0003`, [evidence 1](input/sources/02-ledger.pdf.md) at `pdf-page-0001`, [proof 0: Audit.claim2](models/Audit.lean)

Independent audit reasoning:

- The ledger records A=60 credits; P2 sets an inclusive per-charge maximum of 50.
- 60 exceeds 50. A is an in-scope counterexample to compliance; no aggregate averaging or exception is available.

[evidence 0](input/sources/01-policy.docx.md) at `docx-p-0003`, [evidence 1](input/sources/02-ledger.pdf.md) at `pdf-page-0001`, [proof 0: Audit.claim2](models/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: A small arithmetic or Boolean target checks the stated operational issue without assuming the conclusion.

- Proof 0 source-to-target correspondence: The ledger records A=60 credits; P2 sets an inclusive per-charge maximum of 50. 60 exceeds 50. A is an in-scope counterexample to compliance; no aggregate averaging or exception is available. Source facts are assumptions of this translation; this target does not authenticate records.

Declared bounded support search: Read the exact report finding and all evidence passages listed here in context; checked current ledger version, governing rule and receipt where relevant.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/01-policy.docx.md](input/sources/01-policy.docx.md) at `docx-p-0003`.
- Inspected [input/sources/02-ledger.pdf.md](input/sources/02-ledger.pdf.md) at `pdf-page-0001`.

The ledger records A=60 credits; P2 sets an inclusive per-charge maximum of 50. 60 exceeds 50. A is an in-scope counterexample to compliance; no aggregate averaging or exception is available.

Search limits: This is a bounded search of the supplied package, with no outside or missing approval-event records.

### Rules

- P2: an individual charge complies exactly when it is at most 50 credits.

### Assumptions

- Interpret the supplied synthetic records as the authoritative documentary package for T7 on 4 November 2026.
- The manually reviewed source-to-symbol translation is faithful; Lean verifies only the encoded proposition.

### Reasoning

- The ledger records A=60 credits; P2 sets an inclusive per-charge maximum of 50.
- 60 exceeds 50. A is an in-scope counterexample to compliance; no aggregate averaging or exception is available.

### Limits

- The dossier is synthetic; hashes and Lean do not authenticate real-world events.
- The auditor authored the fixture: this is a nonblind demonstration with a separate coordinator source-first/model review, not a blind accuracy benchmark.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim2` in module `Audit` (refutes): `¬ (Audit.currentLedger.chargeA ≤ Audit.individualCap)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target008.lean) · [Actual proof log](logs/target-008.log)

### Recommendation

Replace the claim with the source-grounded result explained above; do not infer absent historical events.

## R3

### Exact report claim

`input/report.md#R3`

> The physical receipt occurred at 16:40 local time on 4 November 2026.

### Verification question

Does the original scan record the exact receipt timestamp claimed for T7?

### Source evidence

- [input/sources/03-receipt-scan.pdf.md](input/sources/03-receipt-scan.pdf.md) — `pdf-page-0001-reviewed-0001`

> CEDAR LABORATORY - PHYSICAL RECEIPT
> Transfer: T7
> Receipt date: 4 November 2026
> Physical receipt time: 16:40 local time
> Dispatch time: 16:10 local time
> Recorded by: Receiving desk
> This receipt records physical arrival only.
> It does not record quality or security approval.

Original: [input/originals/D00004.pdf](input/originals/D00004.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 1, "origin": {"format": "pdf", "page": 1, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 1}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0001-raster.png", "tsv_artifact": "pdf-page-0001.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 94.56868992682926, "minimum_word_confidence": 59.075352, "confidence_threshold": 85.0, "low_confidence_words": 2, "word_count": 41, "original": "input/originals/D00004.pdf", "original_sha256": "2d22efef6a77638e22040fbedad784697ae8cf45d91131a088e60d16b7e86eba", "artifact_directory": "extraction/D00004/attempt-eye7enel", "source_anchor": "pdf-page-0001", "root_source_anchor": "pdf-page-0001", "reviewer": "Native revision dossier author (nonblind)", "reason": "Visually inspected the original scan raster using view_image: transfer is T7, but OCR reads 17. Verified date, 16:40 receipt, 16:10 dispatch and approval disclaimer. Corrected only the identifier; preserved original OCR.", "reviewed_at": "2026-11-04T18:09:00.010095+00:00", "transcription_snapshot": "input/manual-transcriptions/D00004/27a8dd0b9c08462610f0237b36aebddc5203fb42d149a2cf510126e2ed638151.txt", "transcription_file_sha256": "1d9e98e3d732af7f3a90f3e31c00987755ef174bb746dd11b1bb84237cd180ea", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.


### R3: criteria and report argument audit

Criteria origin: **inferred**. Scope: Transfer T7, 4 November 2026; current supplied source revision only. No separate brief was supplied.

Does the original scan record the exact receipt timestamp claimed for T7?

- Decision criterion: Use physical receipt time, with date and transfer identity preserved.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **sufficient**.

Report citation at `R3`:

> The physical receipt scan records that timestamp for T7.

Assessment: **verified**. The visually inspected original identifies T7 and receipt time 16:40 on the stated date. Raw OCR misreads T7 as 17; the reviewed transcription corrects that identifier. The typed Receipt record preserves transfer identity T7, calendar date 2026-11-04 and receipt minute 1000 (16:40). The exact target checks all three recorded fields; documentary attribution rests on the reviewed scan.

[evidence 0](input/sources/03-receipt-scan.pdf.md) at `pdf-page-0001-reviewed-0001`, [proof 0: Audit.claim3](models/Audit.lean)

Independent audit reasoning:

- The visually inspected original identifies T7 and receipt time 16:40 on the stated date. Raw OCR misreads T7 as 17; the reviewed transcription corrects that identifier.
- The typed Receipt record preserves transfer identity T7, calendar date 2026-11-04 and receipt minute 1000 (16:40). The exact target checks all three recorded fields; documentary attribution rests on the reviewed scan.

[evidence 0](input/sources/03-receipt-scan.pdf.md) at `pdf-page-0001-reviewed-0001`, [proof 0: Audit.claim3](models/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: A small arithmetic or Boolean target checks the stated operational issue without assuming the conclusion.

- Proof 0 source-to-target correspondence: The visually inspected original identifies T7 and receipt time 16:40 on the stated date. Raw OCR misreads T7 as 17; the reviewed transcription corrects that identifier. The typed Receipt record preserves transfer identity T7, calendar date 2026-11-04 and receipt minute 1000 (16:40). The exact target checks all three recorded fields; documentary attribution rests on the reviewed scan. Source facts are assumptions of this translation; this target does not authenticate records.

Declared bounded support search: Read the exact report finding and all evidence passages listed here in context; checked current ledger version, governing rule and receipt where relevant.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/03-receipt-scan.pdf.md](input/sources/03-receipt-scan.pdf.md) at `pdf-page-0001-reviewed-0001`.

The visually inspected original identifies T7 and receipt time 16:40 on the stated date. Raw OCR misreads T7 as 17; the reviewed transcription corrects that identifier. The typed Receipt record preserves transfer identity T7, calendar date 2026-11-04 and receipt minute 1000 (16:40). The exact target checks all three recorded fields; documentary attribution rests on the reviewed scan.

Search limits: This is a bounded search of the supplied package, with no outside or missing approval-event records.

### Rules

- Use physical receipt time, with date and transfer identity preserved.

### Assumptions

- Interpret the supplied synthetic records as the authoritative documentary package for T7 on 4 November 2026.
- The manually reviewed source-to-symbol translation is faithful; Lean verifies only the encoded proposition.

### Reasoning

- The visually inspected original identifies T7 and receipt time 16:40 on the stated date. Raw OCR misreads T7 as 17; the reviewed transcription corrects that identifier.
- The typed Receipt record preserves transfer identity T7, calendar date 2026-11-04 and receipt minute 1000 (16:40). The exact target checks all three recorded fields; documentary attribution rests on the reviewed scan.

### Limits

- The dossier is synthetic; hashes and Lean do not authenticate real-world events.
- The auditor authored the fixture: this is a nonblind demonstration with a separate coordinator source-first/model review, not a blind accuracy benchmark.
- Original OCR remains available; reviewed transcription corrects T7/17. Coordinates/confidences describe the original extraction, not independent witnesses.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim3` in module `Audit` (supports): `Audit.currentReceipt.transfer = "T7" ∧ Audit.currentReceipt.date = "2026-11-04" ∧ Audit.currentReceipt.minute = 1000`.
  [Model](models/Audit.lean) · [Executed check](checks/Target009.lean) · [Actual proof log](logs/target-009.log)

### Recommendation

Retain the claim with its stated documentary scope.

## R4

### Exact report claim

`input/report.md#R4`

> The physical receipt was timely under policy P3.

### Verification question

Was physical receipt on time under the applicable receipt rule, rather than the approval rule?

### Source evidence

- [input/sources/01-policy.docx.md](input/sources/01-policy.docx.md) — `docx-p-0004`

> P3: T7 receipt is timely if the physical receipt timestamp is no later than 16:30 local time on 4 November 2026. No grace period applies. Dispatch time is irrelevant.

Original: [input/originals/D00002.docx](input/originals/D00002.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00002.docx", "original_sha256": "4a0cf796e8b3917bc1606f856a688d36c5d1aac4d82a6aba8e1576be91be5c42", "artifact_directory": "extraction/D00002/attempt-iak8g2wr"}`.

- [input/sources/03-receipt-scan.pdf.md](input/sources/03-receipt-scan.pdf.md) — `pdf-page-0001-reviewed-0001`

> CEDAR LABORATORY - PHYSICAL RECEIPT
> Transfer: T7
> Receipt date: 4 November 2026
> Physical receipt time: 16:40 local time
> Dispatch time: 16:10 local time
> Recorded by: Receiving desk
> This receipt records physical arrival only.
> It does not record quality or security approval.

Original: [input/originals/D00004.pdf](input/originals/D00004.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 1, "origin": {"format": "pdf", "page": 1, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 1}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0001-raster.png", "tsv_artifact": "pdf-page-0001.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 94.56868992682926, "minimum_word_confidence": 59.075352, "confidence_threshold": 85.0, "low_confidence_words": 2, "word_count": 41, "original": "input/originals/D00004.pdf", "original_sha256": "2d22efef6a77638e22040fbedad784697ae8cf45d91131a088e60d16b7e86eba", "artifact_directory": "extraction/D00004/attempt-eye7enel", "source_anchor": "pdf-page-0001", "root_source_anchor": "pdf-page-0001", "reviewer": "Native revision dossier author (nonblind)", "reason": "Visually inspected the original scan raster using view_image: transfer is T7, but OCR reads 17. Verified date, 16:40 receipt, 16:10 dispatch and approval disclaimer. Corrected only the identifier; preserved original OCR.", "reviewed_at": "2026-11-04T18:09:00.010095+00:00", "transcription_snapshot": "input/manual-transcriptions/D00004/27a8dd0b9c08462610f0237b36aebddc5203fb42d149a2cf510126e2ed638151.txt", "transcription_file_sha256": "1d9e98e3d732af7f3a90f3e31c00987755ef174bb746dd11b1bb84237cd180ea", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.


### R4: criteria and report argument audit

Criteria origin: **inferred**. Scope: Transfer T7, 4 November 2026; current supplied source revision only. No separate brief was supplied.

Was physical receipt on time under the applicable receipt rule, rather than the approval rule?

- Decision criterion: P3: timely receipt requires receipt time ≤16:30 on 4 November 2026.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **unsound**.

Report premise at `R4`:

> The applicable receipt deadline was 17:00, and the receipt scan records 16:40.

Assessment: **contradicted**. P3 sets the receipt cutoff at 16:30 with no grace period. The reviewed scan records receipt at 16:40, ten minutes after that cutoff. The 16:10 dispatch is not receipt. The 17:00 approval deadline in P4 does not alter P3.

[evidence 0](input/sources/01-policy.docx.md) at `docx-p-0004`, [evidence 1](input/sources/03-receipt-scan.pdf.md) at `pdf-page-0001-reviewed-0001`, [proof 0: Audit.claim4](models/Audit.lean)

Independent audit reasoning:

- P3 sets the receipt cutoff at 16:30 with no grace period. The reviewed scan records receipt at 16:40, ten minutes after that cutoff.
- The 16:10 dispatch is not receipt. The 17:00 approval deadline in P4 does not alter P3.

[evidence 0](input/sources/01-policy.docx.md) at `docx-p-0004`, [evidence 1](input/sources/03-receipt-scan.pdf.md) at `pdf-page-0001-reviewed-0001`, [proof 0: Audit.claim4](models/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: A small arithmetic or Boolean target checks the stated operational issue without assuming the conclusion.

- Proof 0 source-to-target correspondence: P3 sets the receipt cutoff at 16:30 with no grace period. The reviewed scan records receipt at 16:40, ten minutes after that cutoff. The 16:10 dispatch is not receipt. The 17:00 approval deadline in P4 does not alter P3. Source facts are assumptions of this translation; this target does not authenticate records.

Declared bounded support search: Read the exact report finding and all evidence passages listed here in context; checked current ledger version, governing rule and receipt where relevant.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/01-policy.docx.md](input/sources/01-policy.docx.md) at `docx-p-0004`.
- Inspected [input/sources/03-receipt-scan.pdf.md](input/sources/03-receipt-scan.pdf.md) at `pdf-page-0001-reviewed-0001`.

P3 sets the receipt cutoff at 16:30 with no grace period. The reviewed scan records receipt at 16:40, ten minutes after that cutoff. The 16:10 dispatch is not receipt. The 17:00 approval deadline in P4 does not alter P3.

Search limits: This is a bounded search of the supplied package, with no outside or missing approval-event records.

### Rules

- P3: timely receipt requires receipt time ≤16:30 on 4 November 2026.

### Assumptions

- Interpret the supplied synthetic records as the authoritative documentary package for T7 on 4 November 2026.
- The manually reviewed source-to-symbol translation is faithful; Lean verifies only the encoded proposition.

### Reasoning

- P3 sets the receipt cutoff at 16:30 with no grace period. The reviewed scan records receipt at 16:40, ten minutes after that cutoff.
- The 16:10 dispatch is not receipt. The 17:00 approval deadline in P4 does not alter P3.

### Limits

- The dossier is synthetic; hashes and Lean do not authenticate real-world events.
- The auditor authored the fixture: this is a nonblind demonstration with a separate coordinator source-first/model review, not a blind accuracy benchmark.
- Original OCR remains available; reviewed transcription corrects T7/17. Coordinates/confidences describe the original extraction, not independent witnesses.

### Result

Semantic state: **refuted**; argument status: **unsound_argument**; formal status: **refuted**.

### Formal evidence

- `Audit.claim4` in module `Audit` (refutes): `¬ (Audit.currentReceipt.minute ≤ Audit.receiptDeadline)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target010.lean) · [Actual proof log](logs/target-010.log)

### Recommendation

Replace the claim with the source-grounded result explained above; do not infer absent historical events.

## R5

### Exact report claim

`input/report.md#R5`

> T7 release eligibility is established.

### Verification question

Do these supplied records establish both required approval premises without treating missing security status as a negative event?

### Source evidence

- [input/sources/01-policy.docx.md](input/sources/01-policy.docx.md) — `docx-p-0005`

> P4: T7 release eligibility requires both quality approval and security approval by 17:00 local time. Quality approval alone is insufficient. A missing security-status field is not a statement that no approval event occurred.

Original: [input/originals/D00002.docx](input/originals/D00002.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[5]", "paragraph_index_in_story": 5, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00002.docx", "original_sha256": "4a0cf796e8b3917bc1606f856a688d36c5d1aac4d82a6aba8e1576be91be5c42", "artifact_directory": "extraction/D00002/attempt-iak8g2wr"}`.

- [input/sources/02-ledger.pdf.md](input/sources/02-ledger.pdf.md) — `pdf-page-0001`

> Cedar laboratory T7 charge and quality ledger - revision 2
> Transfer date: 4 November 2026. Unit: whole credits.
> Charge A: 60 credits.
> Charge B: 40 credits.
> Charge C: 45 credits.
> This is the complete charge list for transfer T7. Count each line once.
> Quality approval: granted at 16:00 local time on 4 November 2026.
> Security approval status: not supplied. This ledger is not an approval-event history.
> Revision 2 supersedes revision 1 for T7. Charge C is corrected from 20 to 45 credits. All
> other fields remain unchanged.

Original: [input/originals/D00003.pdf](input/originals/D00003.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 1, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0001.bbox.xhtml", "total_pages": 1, "original": "input/originals/D00003.pdf", "original_sha256": "3c49680f3332d2f30535aff99f59c551c046d049fcc7e02444a446309cb8a6a4", "artifact_directory": "extraction/D00003/attempt-33t64ln6"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/03-receipt-scan.pdf.md](input/sources/03-receipt-scan.pdf.md) — `pdf-page-0001-reviewed-0001`

> CEDAR LABORATORY - PHYSICAL RECEIPT
> Transfer: T7
> Receipt date: 4 November 2026
> Physical receipt time: 16:40 local time
> Dispatch time: 16:10 local time
> Recorded by: Receiving desk
> This receipt records physical arrival only.
> It does not record quality or security approval.

Original: [input/originals/D00004.pdf](input/originals/D00004.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 1, "origin": {"format": "pdf", "page": 1, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 1}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0001-raster.png", "tsv_artifact": "pdf-page-0001.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 94.56868992682926, "minimum_word_confidence": 59.075352, "confidence_threshold": 85.0, "low_confidence_words": 2, "word_count": 41, "original": "input/originals/D00004.pdf", "original_sha256": "2d22efef6a77638e22040fbedad784697ae8cf45d91131a088e60d16b7e86eba", "artifact_directory": "extraction/D00004/attempt-eye7enel", "source_anchor": "pdf-page-0001", "root_source_anchor": "pdf-page-0001", "reviewer": "Native revision dossier author (nonblind)", "reason": "Visually inspected the original scan raster using view_image: transfer is T7, but OCR reads 17. Verified date, 16:40 receipt, 16:10 dispatch and approval disclaimer. Corrected only the identifier; preserved original OCR.", "reviewed_at": "2026-11-04T18:09:00.010095+00:00", "transcription_snapshot": "input/manual-transcriptions/D00004/27a8dd0b9c08462610f0237b36aebddc5203fb42d149a2cf510126e2ed638151.txt", "transcription_file_sha256": "1d9e98e3d732af7f3a90f3e31c00987755ef174bb746dd11b1bb84237cd180ea", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/01-policy.docx.md](input/sources/01-policy.docx.md) — `docx-p-0006`

> P5: This package contains no definition or grading scale for the adjective exemplary. The package is complete only for charges A, B and C; it is not a complete approval-event history.

Original: [input/originals/D00002.docx](input/originals/D00002.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00002.docx", "original_sha256": "4a0cf796e8b3917bc1606f856a688d36c5d1aac4d82a6aba8e1576be91be5c42", "artifact_directory": "extraction/D00002/attempt-iak8g2wr"}`.


### R5: criteria and report argument audit

Criteria origin: **inferred**. Scope: Transfer T7, 4 November 2026; current supplied source revision only. No separate brief was supplied.

Do these supplied records establish both required approval premises without treating missing security status as a negative event?

- Decision criterion: P4 requires quality AND security approval; unknown security status is not false.

Missing definitions: None declared.

Alternatives: Eligibility may hold or fail depending on the unprovided security event.

Report justification outcome: **unsound**.

Report premise at `R5`:

> The ledger records quality approval at 16:00

Assessment: **verified**. Quality approval at16:00 is explicitly recorded.

[evidence 1](input/sources/02-ledger.pdf.md) at `pdf-page-0001`

Report premise at `R5`:

> quality approval alone establishes release eligibility.

Assessment: **contradicted**. P4 expressly denies quality-only sufficiency; the Boolean witness makes the missing required security condition explicit.

[evidence 0](input/sources/01-policy.docx.md) at `docx-p-0005`, [proof 0: Audit.claim5](models/Audit.lean)

Report inference at `R5`:

> T7 release eligibility is established.

Assessment: **unsupported**. The offered sufficient rule is false. The corpus cannot establish actual eligibility or its negation; the report certainty is unsupported.

[evidence 0](input/sources/01-policy.docx.md) at `docx-p-0005`, [evidence 1](input/sources/02-ledger.pdf.md) at `pdf-page-0001`, [evidence 2](input/sources/03-receipt-scan.pdf.md) at `pdf-page-0001-reviewed-0001`, [evidence 3](input/sources/01-policy.docx.md) at `docx-p-0006`, [proof 0: Audit.claim5](models/Audit.lean)

Independent audit reasoning:

- P4 requires both quality and security approvals by 17:00. The ledger records quality at 16:00 but expressly supplies no security status. The scan records arrival only; P5 denies approval-history completeness.
- Two compatible possibilities remain: timely security approval occurred, or it did not. Actual eligibility is unresolved, and its establishment from this package fails. The mixed report wording is epistemic: its asserted certainty is unsupported even though the underlying eligibility event is left undetermined.
- The Lean counterexample q=true, s=false refutes the offered quality-only rule. It does not prove actual security refusal or actual ineligibility.

[evidence 0](input/sources/01-policy.docx.md) at `docx-p-0005`, [evidence 1](input/sources/02-ledger.pdf.md) at `pdf-page-0001`, [evidence 2](input/sources/03-receipt-scan.pdf.md) at `pdf-page-0001-reviewed-0001`, [evidence 3](input/sources/01-policy.docx.md) at `docx-p-0006`, [proof 0: Audit.claim5](models/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: A small arithmetic or Boolean target checks the stated operational issue without assuming the conclusion.

- Proof 0 source-to-target correspondence: P4 requires both quality and security approvals by 17:00. The ledger records quality at 16:00 but expressly supplies no security status. The scan records arrival only; P5 denies approval-history completeness. Two compatible possibilities remain: timely security approval occurred, or it did not. Actual eligibility is unresolved, and its establishment from this package fails. The mixed report wording is epistemic: its asserted certainty is unsupported even though the underlying eligibility event is left undetermined. The Lean counterexample q=true, s=false refutes the offered quality-only rule. It does not prove actual security refusal or actual ineligibility. Source facts are assumptions of this translation; this target does not authenticate records.

Declared bounded support search: Read the exact report finding and all evidence passages listed here in context; checked current ledger version, governing rule and receipt where relevant.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/01-policy.docx.md](input/sources/01-policy.docx.md) at `docx-p-0005`.
- Inspected [input/sources/02-ledger.pdf.md](input/sources/02-ledger.pdf.md) at `pdf-page-0001`.
- Inspected [input/sources/03-receipt-scan.pdf.md](input/sources/03-receipt-scan.pdf.md) at `pdf-page-0001-reviewed-0001`.
- Inspected [input/sources/01-policy.docx.md](input/sources/01-policy.docx.md) at `docx-p-0006`.

P4 requires both quality and security approvals by 17:00. The ledger records quality at 16:00 but expressly supplies no security status. The scan records arrival only; P5 denies approval-history completeness. Two compatible possibilities remain: timely security approval occurred, or it did not. Actual eligibility is unresolved, and its establishment from this package fails. The mixed report wording is epistemic: its asserted certainty is unsupported even though the underlying eligibility event is left undetermined. The Lean counterexample q=true, s=false refutes the offered quality-only rule. It does not prove actual security refusal or actual ineligibility.

Search limits: This is a bounded search of the supplied package, with no outside or missing approval-event records.

### Rules

- P4 requires quality AND security approval; unknown security status is not false.

### Assumptions

- Interpret the supplied synthetic records as the authoritative documentary package for T7 on 4 November 2026.
- The manually reviewed source-to-symbol translation is faithful; Lean verifies only the encoded proposition.

### Reasoning

- P4 requires both quality and security approvals by 17:00. The ledger records quality at 16:00 but expressly supplies no security status. The scan records arrival only; P5 denies approval-history completeness.
- Two compatible possibilities remain: timely security approval occurred, or it did not. Actual eligibility is unresolved, and its establishment from this package fails. The mixed report wording is epistemic: its asserted certainty is unsupported even though the underlying eligibility event is left undetermined.
- The Lean counterexample q=true, s=false refutes the offered quality-only rule. It does not prove actual security refusal or actual ineligibility.

### Limits

- The dossier is synthetic; hashes and Lean do not authenticate real-world events.
- The auditor authored the fixture: this is a nonblind demonstration with a separate coordinator source-first/model review, not a blind accuracy benchmark.
- Original OCR remains available; reviewed transcription corrects T7/17. Coordinates/confidences describe the original extraction, not independent witnesses.
- No complete approval-event history is supplied; neither approval absence nor actual ineligibility is established.

### Result

Semantic state: **undetermined**; argument status: **unsound_argument**; formal status: **auxiliary**.

### Formal evidence

- `Audit.claim5` in module `Audit` (auxiliary): `¬ (∀ q s : Bool, q = true → (q = true ∧ s = true))`.
  [Model](models/Audit.lean) · [Executed check](checks/Target011.lean) · [Actual proof log](logs/target-011.log)

### Recommendation

Replace the claim with the source-grounded result explained above; do not infer absent historical events.

## R6

### Exact report claim

`input/report.md#R6`

> Charge B is 40 credits.

### Verification question

Is the unsupported report amount for B independently documented?

### Source evidence

- [input/sources/02-ledger.pdf.md](input/sources/02-ledger.pdf.md) — `pdf-page-0001`

> Cedar laboratory T7 charge and quality ledger - revision 2
> Transfer date: 4 November 2026. Unit: whole credits.
> Charge A: 60 credits.
> Charge B: 40 credits.
> Charge C: 45 credits.
> This is the complete charge list for transfer T7. Count each line once.
> Quality approval: granted at 16:00 local time on 4 November 2026.
> Security approval status: not supplied. This ledger is not an approval-event history.
> Revision 2 supersedes revision 1 for T7. Charge C is corrected from 20 to 45 credits. All
> other fields remain unchanged.

Original: [input/originals/D00003.pdf](input/originals/D00003.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 1, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0001.bbox.xhtml", "total_pages": 1, "original": "input/originals/D00003.pdf", "original_sha256": "3c49680f3332d2f30535aff99f59c551c046d049fcc7e02444a446309cb8a6a4", "artifact_directory": "extraction/D00003/attempt-33t64ln6"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.


### R6: criteria and report argument audit

Criteria origin: **inferred**. Scope: Transfer T7, 4 November 2026; current supplied source revision only. No separate brief was supplied.

Is the unsupported report amount for B independently documented?

- Decision criterion: Read the B entry and preserve its whole-credit unit.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **not_provided**.

Independent audit reasoning:

- The ledger directly records B=40 credits in both revisions.
- The report gives no derivation or citation for this sentence. Independent evidence supports it, while its author-supplied support is absent. The theorem reads the named chargeB field of the typed Ledger record, whose source correspondence is documented.

[evidence 0](input/sources/02-ledger.pdf.md) at `pdf-page-0001`, [proof 0: Audit.claim6](models/Audit.lean)

Audited claim dependencies: None declared.

Formalization rationale: A small arithmetic or Boolean target checks the stated operational issue without assuming the conclusion.

- Proof 0 source-to-target correspondence: The ledger directly records B=40 credits in both revisions. The report gives no derivation or citation for this sentence. Independent evidence supports it, while its author-supplied support is absent. The theorem reads the named chargeB field of the typed Ledger record, whose source correspondence is documented. Source facts are assumptions of this translation; this target does not authenticate records.

Declared bounded support search: Read the exact report finding and all evidence passages listed here in context; checked current ledger version, governing rule and receipt where relevant.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/02-ledger.pdf.md](input/sources/02-ledger.pdf.md) at `pdf-page-0001`.

The ledger directly records B=40 credits in both revisions. The report gives no derivation or citation for this sentence. Independent evidence supports it, while its author-supplied support is absent. The theorem reads the named chargeB field of the typed Ledger record, whose source correspondence is documented.

Search limits: This is a bounded search of the supplied package, with no outside or missing approval-event records.

### Rules

- Read the B entry and preserve its whole-credit unit.

### Assumptions

- Interpret the supplied synthetic records as the authoritative documentary package for T7 on 4 November 2026.
- The manually reviewed source-to-symbol translation is faithful; Lean verifies only the encoded proposition.

### Reasoning

- The ledger directly records B=40 credits in both revisions.
- The report gives no derivation or citation for this sentence. Independent evidence supports it, while its author-supplied support is absent. The theorem reads the named chargeB field of the typed Ledger record, whose source correspondence is documented.

### Limits

- The dossier is synthetic; hashes and Lean do not authenticate real-world events.
- The auditor authored the fixture: this is a nonblind demonstration with a separate coordinator source-first/model review, not a blind accuracy benchmark.

### Result

Semantic state: **supported**; argument status: **insufficient_support**; formal status: **proved**.

### Formal evidence

- `Audit.claim6` in module `Audit` (supports): `Audit.currentLedger.chargeB = 40`.
  [Model](models/Audit.lean) · [Executed check](checks/Target012.lean) · [Actual proof log](logs/target-012.log)

### Recommendation

Retain the claim with its stated documentary scope.

## R7

### Exact report claim

`input/report.md#R7`

> The handover was exemplary.

### Verification question

Does the supplied package define an operational grading criterion for exemplary?

### Source evidence

- [input/sources/01-policy.docx.md](input/sources/01-policy.docx.md) — `docx-p-0006`

> P5: This package contains no definition or grading scale for the adjective exemplary. The package is complete only for charges A, B and C; it is not a complete approval-event history.

Original: [input/originals/D00002.docx](input/originals/D00002.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00002.docx", "original_sha256": "4a0cf796e8b3917bc1606f856a688d36c5d1aac4d82a6aba8e1576be91be5c42", "artifact_directory": "extraction/D00002/attempt-iak8g2wr"}`.

- [input/sources/02-ledger.pdf.md](input/sources/02-ledger.pdf.md) — `pdf-page-0001`

> Cedar laboratory T7 charge and quality ledger - revision 2
> Transfer date: 4 November 2026. Unit: whole credits.
> Charge A: 60 credits.
> Charge B: 40 credits.
> Charge C: 45 credits.
> This is the complete charge list for transfer T7. Count each line once.
> Quality approval: granted at 16:00 local time on 4 November 2026.
> Security approval status: not supplied. This ledger is not an approval-event history.
> Revision 2 supersedes revision 1 for T7. Charge C is corrected from 20 to 45 credits. All
> other fields remain unchanged.

Original: [input/originals/D00003.pdf](input/originals/D00003.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 1, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0001.bbox.xhtml", "total_pages": 1, "original": "input/originals/D00003.pdf", "original_sha256": "3c49680f3332d2f30535aff99f59c551c046d049fcc7e02444a446309cb8a6a4", "artifact_directory": "extraction/D00003/attempt-33t64ln6"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/03-receipt-scan.pdf.md](input/sources/03-receipt-scan.pdf.md) — `pdf-page-0001-reviewed-0001`

> CEDAR LABORATORY - PHYSICAL RECEIPT
> Transfer: T7
> Receipt date: 4 November 2026
> Physical receipt time: 16:40 local time
> Dispatch time: 16:10 local time
> Recorded by: Receiving desk
> This receipt records physical arrival only.
> It does not record quality or security approval.

Original: [input/originals/D00004.pdf](input/originals/D00004.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 1, "origin": {"format": "pdf", "page": 1, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 1}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0001-raster.png", "tsv_artifact": "pdf-page-0001.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 94.56868992682926, "minimum_word_confidence": 59.075352, "confidence_threshold": 85.0, "low_confidence_words": 2, "word_count": 41, "original": "input/originals/D00004.pdf", "original_sha256": "2d22efef6a77638e22040fbedad784697ae8cf45d91131a088e60d16b7e86eba", "artifact_directory": "extraction/D00004/attempt-eye7enel", "source_anchor": "pdf-page-0001", "root_source_anchor": "pdf-page-0001", "reviewer": "Native revision dossier author (nonblind)", "reason": "Visually inspected the original scan raster using view_image: transfer is T7, but OCR reads 17. Verified date, 16:40 receipt, 16:10 dispatch and approval disclaimer. Corrected only the identifier; preserved original OCR.", "reviewed_at": "2026-11-04T18:09:00.010095+00:00", "transcription_snapshot": "input/manual-transcriptions/D00004/27a8dd0b9c08462610f0237b36aebddc5203fb42d149a2cf510126e2ed638151.txt", "transcription_file_sha256": "1d9e98e3d732af7f3a90f3e31c00987755ef174bb746dd11b1bb84237cd180ea", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.


### R7: criteria and report argument audit

Criteria origin: **inferred**. Scope: Transfer T7, 4 November 2026; current supplied source revision only. No separate brief was supplied.

Does the supplied package define an operational grading criterion for exemplary?

- Decision criterion: No supplied exemplary grading criterion; do not invent a scale.

Missing definitions: No operational exemplary grading scale.

Alternatives: None declared.

Report justification outcome: **nonformal**.

Report premise at `R7`:

> No grading criterion is offered for this evaluation.

Assessment: **nonformal**. P5 expressly states that no definition or grading scale for exemplary is supplied. The ledger and receipt contain event and amount records, not a grading scale. Exemplary has no operational decision criterion here. No numeric result or timestamp settles that evaluative judgment.

[evidence 0](input/sources/01-policy.docx.md) at `docx-p-0006`, [evidence 1](input/sources/02-ledger.pdf.md) at `pdf-page-0001`, [evidence 2](input/sources/03-receipt-scan.pdf.md) at `pdf-page-0001-reviewed-0001`

Independent audit reasoning:

- P5 expressly states that no definition or grading scale for exemplary is supplied. The ledger and receipt contain event and amount records, not a grading scale.
- Exemplary has no operational decision criterion here. No numeric result or timestamp settles that evaluative judgment.

[evidence 0](input/sources/01-policy.docx.md) at `docx-p-0006`, [evidence 1](input/sources/02-ledger.pdf.md) at `pdf-page-0001`, [evidence 2](input/sources/03-receipt-scan.pdf.md) at `pdf-page-0001-reviewed-0001`

Audited claim dependencies: None declared.

Formalization rationale: Documentary interpretation or evaluative scope is the issue; no faithful additional Lean target is claimed.


Declared bounded support search: Read the exact report finding and all evidence passages listed here in context; checked current ledger version, governing rule and receipt where relevant.

Queries: No text queries; see inspection scope.

- Inspected [input/sources/01-policy.docx.md](input/sources/01-policy.docx.md) at `docx-p-0006`.
- Inspected [input/sources/02-ledger.pdf.md](input/sources/02-ledger.pdf.md) at `pdf-page-0001`.
- Inspected [input/sources/03-receipt-scan.pdf.md](input/sources/03-receipt-scan.pdf.md) at `pdf-page-0001-reviewed-0001`.

P5 expressly states that no definition or grading scale for exemplary is supplied. The ledger and receipt contain event and amount records, not a grading scale. Exemplary has no operational decision criterion here. No numeric result or timestamp settles that evaluative judgment.

Search limits: This is a bounded search of the supplied package, with no outside or missing approval-event records.

### Rules

- No supplied exemplary grading criterion; do not invent a scale.

### Assumptions

- Interpret the supplied synthetic records as the authoritative documentary package for T7 on 4 November 2026.
- The manually reviewed source-to-symbol translation is faithful; Lean verifies only the encoded proposition.

### Reasoning

- P5 expressly states that no definition or grading scale for exemplary is supplied. The ledger and receipt contain event and amount records, not a grading scale.
- Exemplary has no operational decision criterion here. No numeric result or timestamp settles that evaluative judgment.

### Limits

- The dossier is synthetic; hashes and Lean do not authenticate real-world events.
- The auditor authored the fixture: this is a nonblind demonstration with a separate coordinator source-first/model review, not a blind accuracy benchmark.
- The absence of a supplied grading criterion is not a universal impossibility of qualitative evaluation.

### Result

Semantic state: **not_applicable**; argument status: **nonformal**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Replace the claim with the source-grounded result explained above; do not infer absent historical events.
