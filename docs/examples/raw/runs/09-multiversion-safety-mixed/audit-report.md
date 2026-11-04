# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

[Semantic correspondence review](semantic-review.md)

Extraction inventory: 9 documents; 0 pending, partial or blocked. See [ingestion details](ingestion.json) and [coverage](coverage.md).

## C09-ERR-01

### Exact report claim

`input/report.md#C09-ERR-01`

> **C09-ERR-01.** L01 failed its historical demonstration because 118 exceeds the current 100-millisecond limit.

### Verification question

Did L01 fail its historical delay demonstration because its maximum exceeds today's threshold?

### Source evidence

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-p-0001`

> [V1-01] SYNTHETIC H-7 SPECIFICATION, REVISION 1. This document concerns the fictional Heliostat H-7 demonstration controller. It is not an actual safety standard and supplies no real-world safety advice. Revision 1 applies to tests executed before 1 June 2033 unless an explicitly approved profile says otherwise. The finite demonstration concerns measured trip delay under stated laboratory conditions. It does not certify lifetime reliability, mechanical protection, network security, or population defect rates. A report should identify the proposition actually tested rather than replace it with an undefined claim that the whole design is safe. The table below defines exact synthetic limits for this bounded exercise.

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-p-0002`

> [V1-02] HISTORICAL ACCEPTANCE TABLE. The NORMAL temperature interval includes both endpoints. A missing authorized route outside that interval is not a zero threshold and does not imply a physical failure. Three repeated runs must be valid and belong to the same unit and profile. Values copied from another serial number do not complete a missing run. The supply condition belongs to applicability rather than to an independent exemption from other prerequisites.

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 2, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-p-0025`

> [V1-05] HISTORICAL L01 RECORD. Unit L01 was tested on 20 May 2033 at 20 degrees Celsius. Its three valid delays were 110, 115, and 118 milliseconds. Both channels were measured using instrument K1, which was current for that date. These observations establish the historical delay demonstration under the 120-millisecond threshold. No fault-injection closure or final release signature for L01 is supplied here. A later tighter rule does not retroactively change the applicable threshold unless an operative transition clause explicitly requires reassessment. Historical acceptance and present authorization should remain separate questions, even when a later report discusses them together.

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[5]", "paragraph_index_in_story": 25, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0001`

> [V2-01] SYNTHETIC H-7 SPECIFICATION, REVISION 2. Revision 2 takes effect at 00:00 on 1 June 2033 for newly executed tests. It supersedes revision 1 for that prospective scope. Historical tests retain their historical approved rules unless explicitly retested; no retroactive reassessment is required here. Test execution time determines the applicable revision, not report publication time, file modification time, or the order in which an auditor discovers files. Identical serial numbers may appear in different periods because a unit can be retested. Every conclusion must identify the actual event being judged rather than attach a timeless pass or fail label to a serial number.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/04-test-runs.pdf.md](input/sources/04-test-runs.pdf.md) — `pdf-page-0001`

> SYNTHETIC H-7 TEST PACKET
> [P01] Unit group: L01. Execution: 20 May 2033. Profile: NORMAL. Temperature: 20 degrees
> Celsius. Integer delay values: 110, 115, 118.
> Revision 1 applies. All three runs are valid and both channels were measured with K1. The
> historical threshold is 120. Fault-injection closure and final release signature are not
> supplied. Passing the historical delay demonstration does not establish full release.
> [P01-METHOD] Each valid listed value is a distinct acquired observation for its named unit
> and profile. A missing observation cannot be replaced by a borrowed run, a copied previous
> value, or an assumed zero. The reviewer must first identify the applicable revision and any
> incorporated exception, then compare the exact observed number with the relevant threshold.
> The same numerical delay may pass one profile and fail another because the supplied criteria
> differ. This packet does not interpolate unspecified temperature ranges.
> [P01-SCOPE] This record supports a bounded demonstration. It supplies no production defect
> rate, lifetime prediction, or real-world safety certification. Preserve unit, execution
> time, profile, temperature, calibration, channel completeness, and validity when extracting
> a row. Cite the original PDF path and stable marker. A successful delay comparison does not
> automatically establish fault closure or signing authority. A failed valid run can refute a
> universal passing claim; a missing run instead identifies a support gap. The distinction
> must remain explicit in an evidence-backed audit result.

Original: [input/originals/D00006.pdf](input/originals/D00006.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 1, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0001.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-tidfeggy"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0001-c0001-p0001`

> Profile

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 3, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 1, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0001-c0002-p0001`

> Environment

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 2, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0001-c0003-p0001`

> Maximum delay

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 5, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 3, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0001-c0004-p0001`

> Valid runs

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 4, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0001-c0005-p0001`

> Other conditions

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 7, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 5, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0002-c0001-p0001`

> NORMAL

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 1, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0002-c0002-p0001`

> 10 through 30 degrees Celsius inclusive

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 9, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 2, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0002-c0003-p0001`

> 120 milliseconds

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 3, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0002-c0004-p0001`

> 3 per unit

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 11, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 4, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0002-c0005-p0001`

> Both channels measured; 24 volts nominal

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 5, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0003-c0001-p0001`

> COLD

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 13, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 1, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0003-c0002-p0001`

> Below 10 degrees Celsius

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 2, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0003-c0003-p0001`

> No authorized criterion in revision 1

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 15, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 3, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0003-c0004-p0001`

> Not specified

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 16, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 4, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0003-c0005-p0001`

> No qualification route supplied

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 17, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 5, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0004-c0001-p0001`

> HOT

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 1, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0004-c0002-p0001`

> Above 30 degrees Celsius

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 19, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 2, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0004-c0003-p0001`

> No authorized criterion in revision 1

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 20, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 3, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0004-c0004-p0001`

> Not specified

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 21, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 4, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0004-c0005-p0001`

> No qualification route supplied

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 22, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 5, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

### Rules

- V2-01 selects version by test execution; V2-02 and V1-02 select profile thresholds; Annex X narrows the E17 exception.
- V2-03 release is a conjunction; V2-05 invalidity and calibration chronology cannot be replaced by favorable numbers.
- A supplied sufficient route does not establish universal necessity, missing measurements do not predict outcomes, and finite tests do not establish unbounded safety.

### Assumptions

- The fictional document authorities, exact integer values, profiles and event dates are accepted as supplied. Threshold selection is explicitly source-linked in the model notes.

### Reasoning

- 1. L01 was tested May 20 under revision 1; the transition explicitly preserves historical rules.
- 2. Its three valid values 110,115,118 all satisfy the applicable inclusive 120 limit. Applying the later 100 limit retroactively is invalid.

### Limits

- This concerns the named synthetic test events and the narrow stated assurance route, not certification of actual safety hardware.
- Formal targets encode reviewed rule selections; source authenticity and semantic fidelity remain outside kernel checking. Missing/invalid data are never silently promoted to valid observations.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim01` in module `Audit` (refutes): `Audit.within Audit.Unit.l01 = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target011.lean) · [Actual proof log](logs/target-011.log)

### Recommendation

Retain L01's historical delay pass; do not infer full release from it.

## C09-ERR-02

### Exact report claim

`input/report.md#C09-ERR-02`

> **C09-ERR-02.** N02 passes because 101 is below the revision 1 limit of 120.

### Verification question

Does N02 pass its June 3 NORMAL delay requirement under the old 120 limit?

### Source evidence

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0001`

> [V2-01] SYNTHETIC H-7 SPECIFICATION, REVISION 2. Revision 2 takes effect at 00:00 on 1 June 2033 for newly executed tests. It supersedes revision 1 for that prospective scope. Historical tests retain their historical approved rules unless explicitly retested; no retroactive reassessment is required here. Test execution time determines the applicable revision, not report publication time, file modification time, or the order in which an auditor discovers files. Identical serial numbers may appear in different periods because a unit can be retested. Every conclusion must identify the actual event being judged rather than attach a timeless pass or fail label to a serial number.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0002`

> [V2-02] CURRENT ACCEPTANCE TABLE. Every endpoint in the stated intervals is inclusive. A valid NORMAL delay of 100 milliseconds satisfies the numeric limit; 101 does not. The COLD route additionally requires a current cold-fixture certificate. There is no supplied HOT route, and no route below zero degrees. A table row cannot be applied without checking the environment and profile. The limits in this synthetic exercise are exact integer comparisons; realistic measurement error models are outside scope. The absence of an error model must not be filled by an invented uncertainty discount or an assumed rounding allowance.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 2, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/04-test-runs.pdf.md](input/sources/04-test-runs.pdf.md) — `pdf-page-0002`

> SYNTHETIC H-7 TEST PACKET
> [P02] Unit group: N01 and N02. Execution: 3 June 2033. Profile: NORMAL. Temperature: 20
> degrees Celsius. Integer delay values: N01: 92, 95, 99; N02: 90, 97, 101.
> Revision 2 applies. All six listed runs are valid. Both channels were measured with K1. N01
> has closed fault injections and authorized release. N02 was explicitly denied release
> because its third valid run of 101 exceeds its applicable 100 limit. No exception applies to
> N02.
> [P02-METHOD] Each valid listed value is a distinct acquired observation for its named unit
> and profile. A missing observation cannot be replaced by a borrowed run, a copied previous
> value, or an assumed zero. The reviewer must first identify the applicable revision and any
> incorporated exception, then compare the exact observed number with the relevant threshold.
> The same numerical delay may pass one profile and fail another because the supplied criteria
> differ. This packet does not interpolate unspecified temperature ranges.
> [P02-SCOPE] This record supports a bounded demonstration. It supplies no production defect
> rate, lifetime prediction, or real-world safety certification. Preserve unit, execution
> time, profile, temperature, calibration, channel completeness, and validity when extracting
> a row. Cite the original PDF path and stable marker. A successful delay comparison does not
> automatically establish fault closure or signing authority. A failed valid run can refute a
> universal passing claim; a missing run instead identifies a support gap. The distinction
> must remain explicit in an evidence-backed audit result.

Original: [input/originals/D00006.pdf](input/originals/D00006.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-tidfeggy"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0001`

> [X01] SYNTHETIC INCORPORATED ANNEX X. Requirements owner Mara Flint approved this exception under delegation AUTH-7 at 09:00 on 2 June 2033. It applies only to serial E17 for NORMAL tests executed from 09:00 on 2 June through 18:00 on 4 June inclusive. The maximum valid delay for those tests is 110 milliseconds rather than 100. The environment remains 10 through 30 degrees, and every other revision 2 prerequisite remains operative. The exception expressly does not apply to N02, even if N02 shares the same hardware build. The table records the operative scope rather than an illustrative example.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-3_2qqhln"}`.

- [input/sources/05-calibration-and-authority.md](input/sources/05-calibration-and-authority.md) — `P03`

> [AUTH01] Mara Flint holds the AUTH-7 requirements-exception delegation for E17. Operator Oren Vale can execute and record tests but cannot change thresholds or authorize release. Release owner Sera Moss signed release entries for N01, E17, and C01 after checking their listed fault closures. No release signature is supplied for N03. N02 has an explicit release denial because its valid third delay run exceeded the applicable limit. The release ledger is complete for these named units through 5 June. A signatory identity is not interchangeable with a different role, and an operator's favorable comment is not a release signature.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 653, "end_character": 1286, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "f4d7b1be08d6dd13db756c34f068696ffe5ec31564ff09ac4b47a63db180e175", "artifact_directory": "extraction/D00007/attempt-lersvmwr"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0001-p0001`

> Profile

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 3, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0002-p0001`

> Environment

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0003-p0001`

> Maximum delay

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 5, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0004-p0001`

> Valid runs

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0005-p0001`

> Additional conditions

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 7, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0001-p0001`

> NORMAL

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0002-p0001`

> 10 through 30 degrees Celsius

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 9, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0003-p0001`

> 100 milliseconds

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0004-p0001`

> 3 per unit

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 11, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0005-p0001`

> Both channels measured

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0001-p0001`

> COLD

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 13, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0002-p0001`

> 0 through 9 degrees Celsius

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0003-p0001`

> 150 milliseconds

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 15, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0004-p0001`

> 3 per unit

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 16, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0005-p0001`

> Both channels measured and cold-fixture certificate

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 17, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0001-p0001`

> HOT

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0002-p0001`

> Above 30 degrees Celsius

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 19, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0003-p0001`

> No authorized threshold

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 20, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0004-p0001`

> No route

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 21, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0005-p0001`

> No qualification supplied

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 22, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

### Rules

- V2-01 selects version by test execution; V2-02 and V1-02 select profile thresholds; Annex X narrows the E17 exception.
- V2-03 release is a conjunction; V2-05 invalidity and calibration chronology cannot be replaced by favorable numbers.
- A supplied sufficient route does not establish universal necessity, missing measurements do not predict outcomes, and finite tests do not establish unbounded safety.

### Assumptions

- The fictional document authorities, exact integer values, profiles and event dates are accepted as supplied. Threshold selection is explicitly source-linked in the model notes.

### Reasoning

- 1. June 3 tests use revision 2 and NORMAL 100; the Annex expressly excludes N02.
- 2. The valid third observation is 101, above 100, and release was explicitly denied. Comparison with obsolete 120 is irrelevant to the applicable requirement.

### Limits

- This concerns the named synthetic test events and the narrow stated assurance route, not certification of actual safety hardware.
- Formal targets encode reviewed rule selections; source authenticity and semantic fidelity remain outside kernel checking. Missing/invalid data are never silently promoted to valid observations.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim02` in module `Audit` (refutes): `Audit.within Audit.Unit.n02 = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target012.lean) · [Actual proof log](logs/target-012.log)

### Recommendation

Report N02's failed 101-millisecond current run.

## C09-ERR-03

### Exact report claim

`input/report.md#C09-ERR-03`

> **C09-ERR-03.** All N01 valid delay runs satisfy 100 milliseconds.

### Verification question

Do all three actual valid N01 delay runs meet 100 milliseconds?

### Source evidence

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0002`

> [V2-02] CURRENT ACCEPTANCE TABLE. Every endpoint in the stated intervals is inclusive. A valid NORMAL delay of 100 milliseconds satisfies the numeric limit; 101 does not. The COLD route additionally requires a current cold-fixture certificate. There is no supplied HOT route, and no route below zero degrees. A table row cannot be applied without checking the environment and profile. The limits in this synthetic exercise are exact integer comparisons; realistic measurement error models are outside scope. The absence of an error model must not be filled by an invented uncertainty discount or an assumed rounding allowance.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 2, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/04-test-runs.pdf.md](input/sources/04-test-runs.pdf.md) — `pdf-page-0002`

> SYNTHETIC H-7 TEST PACKET
> [P02] Unit group: N01 and N02. Execution: 3 June 2033. Profile: NORMAL. Temperature: 20
> degrees Celsius. Integer delay values: N01: 92, 95, 99; N02: 90, 97, 101.
> Revision 2 applies. All six listed runs are valid. Both channels were measured with K1. N01
> has closed fault injections and authorized release. N02 was explicitly denied release
> because its third valid run of 101 exceeds its applicable 100 limit. No exception applies to
> N02.
> [P02-METHOD] Each valid listed value is a distinct acquired observation for its named unit
> and profile. A missing observation cannot be replaced by a borrowed run, a copied previous
> value, or an assumed zero. The reviewer must first identify the applicable revision and any
> incorporated exception, then compare the exact observed number with the relevant threshold.
> The same numerical delay may pass one profile and fail another because the supplied criteria
> differ. This packet does not interpolate unspecified temperature ranges.
> [P02-SCOPE] This record supports a bounded demonstration. It supplies no production defect
> rate, lifetime prediction, or real-world safety certification. Preserve unit, execution
> time, profile, temperature, calibration, channel completeness, and validity when extracting
> a row. Cite the original PDF path and stable marker. A successful delay comparison does not
> automatically establish fault closure or signing authority. A failed valid run can refute a
> universal passing claim; a missing run instead identifies a support gap. The distinction
> must remain explicit in an evidence-backed audit result.

Original: [input/originals/D00006.pdf](input/originals/D00006.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-tidfeggy"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/05-calibration-and-authority.md](input/sources/05-calibration-and-authority.md) — `P02`

> [CAL01] Instrument K1 was calibrated through 23:59 on 30 June 2033 and was used for L01, N01, N02, E17, and C01 in the test packet. Instrument K2 expired at 23:59 on 1 June and was used for N03 on 3 June. K2 renewal is dated 5 June and contains no retrospective clause. Thus K1 has affirmative evidence of current calibration at the named runs, while K2 has affirmative evidence of expiry at its N03 use. A later renewal cannot be silently moved backward in time. The registry is complete for these instruments and dates, but it does not certify every instrument ever used by the fictional organization.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 48, "end_character": 651, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "f4d7b1be08d6dd13db756c34f068696ffe5ec31564ff09ac4b47a63db180e175", "artifact_directory": "extraction/D00007/attempt-lersvmwr"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0001-p0001`

> Profile

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 3, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0002-p0001`

> Environment

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0003-p0001`

> Maximum delay

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 5, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0004-p0001`

> Valid runs

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0005-p0001`

> Additional conditions

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 7, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0001-p0001`

> NORMAL

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0002-p0001`

> 10 through 30 degrees Celsius

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 9, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0003-p0001`

> 100 milliseconds

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0004-p0001`

> 3 per unit

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 11, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0005-p0001`

> Both channels measured

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0001-p0001`

> COLD

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 13, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0002-p0001`

> 0 through 9 degrees Celsius

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0003-p0001`

> 150 milliseconds

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 15, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0004-p0001`

> 3 per unit

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 16, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0005-p0001`

> Both channels measured and cold-fixture certificate

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 17, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0001-p0001`

> HOT

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0002-p0001`

> Above 30 degrees Celsius

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 19, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0003-p0001`

> No authorized threshold

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 20, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0004-p0001`

> No route

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 21, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0005-p0001`

> No qualification supplied

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 22, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

### Rules

- V2-01 selects version by test execution; V2-02 and V1-02 select profile thresholds; Annex X narrows the E17 exception.
- V2-03 release is a conjunction; V2-05 invalidity and calibration chronology cannot be replaced by favorable numbers.
- A supplied sufficient route does not establish universal necessity, missing measurements do not predict outcomes, and finite tests do not establish unbounded safety.

### Assumptions

- The fictional document authorities, exact integer values, profiles and event dates are accepted as supplied. Threshold selection is explicitly source-linked in the model notes.

### Reasoning

- 1. P02 identifies N01 at 20 degrees under NORMAL with three valid observations and both channels measured.
- 2. The values 92,95,99 each satisfy the inclusive 100 limit. This supports the narrow delay assertion.

### Limits

- This concerns the named synthetic test events and the narrow stated assurance route, not certification of actual safety hardware.
- Formal targets encode reviewed rule selections; source authenticity and semantic fidelity remain outside kernel checking. Missing/invalid data are never silently promoted to valid observations.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim03` in module `Audit` (supports): `Audit.within Audit.Unit.n01 = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target013.lean) · [Actual proof log](logs/target-013.log)

### Recommendation

Retain the bounded N01 delay finding; separate other release requirements.

## C09-ERR-04

### Exact report claim

`input/report.md#C09-ERR-04`

> **C09-ERR-04.** Every named NORMAL unit passed every required delay run.

### Verification question

Did every named NORMAL unit pass every required delay run?

### Source evidence

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0002`

> [V2-02] CURRENT ACCEPTANCE TABLE. Every endpoint in the stated intervals is inclusive. A valid NORMAL delay of 100 milliseconds satisfies the numeric limit; 101 does not. The COLD route additionally requires a current cold-fixture certificate. There is no supplied HOT route, and no route below zero degrees. A table row cannot be applied without checking the environment and profile. The limits in this synthetic exercise are exact integer comparisons; realistic measurement error models are outside scope. The absence of an error model must not be filled by an invented uncertainty discount or an assumed rounding allowance.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 2, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0026`

> [V2-06] REVIEW UNIVERSE. The named units are L01, N01, N02, N03, E17, and C01; X99 is an invalid demonstration trace. These cases do not constitute a random sample of a production population. No statistical inference about all manufactured controllers is supplied. A universal statement about the named valid runs can be refuted by one in-scope explicit run above its applicable threshold. A universal statement about all temperatures requires additional defined criteria and observations. Preserve successful bounded demonstrations while identifying unsupported extensions. Every name, signature, instrument, and event here is synthetic, so no conclusion should be mistaken for certification of a real product.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 26, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/04-test-runs.pdf.md](input/sources/04-test-runs.pdf.md) — `pdf-page-0002`

> SYNTHETIC H-7 TEST PACKET
> [P02] Unit group: N01 and N02. Execution: 3 June 2033. Profile: NORMAL. Temperature: 20
> degrees Celsius. Integer delay values: N01: 92, 95, 99; N02: 90, 97, 101.
> Revision 2 applies. All six listed runs are valid. Both channels were measured with K1. N01
> has closed fault injections and authorized release. N02 was explicitly denied release
> because its third valid run of 101 exceeds its applicable 100 limit. No exception applies to
> N02.
> [P02-METHOD] Each valid listed value is a distinct acquired observation for its named unit
> and profile. A missing observation cannot be replaced by a borrowed run, a copied previous
> value, or an assumed zero. The reviewer must first identify the applicable revision and any
> incorporated exception, then compare the exact observed number with the relevant threshold.
> The same numerical delay may pass one profile and fail another because the supplied criteria
> differ. This packet does not interpolate unspecified temperature ranges.
> [P02-SCOPE] This record supports a bounded demonstration. It supplies no production defect
> rate, lifetime prediction, or real-world safety certification. Preserve unit, execution
> time, profile, temperature, calibration, channel completeness, and validity when extracting
> a row. Cite the original PDF path and stable marker. A successful delay comparison does not
> automatically establish fault closure or signing authority. A failed valid run can refute a
> universal passing claim; a missing run instead identifies a support gap. The distinction
> must remain explicit in an evidence-backed audit result.

Original: [input/originals/D00006.pdf](input/originals/D00006.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-tidfeggy"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0001`

> [X01] SYNTHETIC INCORPORATED ANNEX X. Requirements owner Mara Flint approved this exception under delegation AUTH-7 at 09:00 on 2 June 2033. It applies only to serial E17 for NORMAL tests executed from 09:00 on 2 June through 18:00 on 4 June inclusive. The maximum valid delay for those tests is 110 milliseconds rather than 100. The environment remains 10 through 30 degrees, and every other revision 2 prerequisite remains operative. The exception expressly does not apply to N02, even if N02 shares the same hardware build. The table records the operative scope rather than an illustrative example.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-3_2qqhln"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0001-p0001`

> Profile

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 3, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0002-p0001`

> Environment

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0003-p0001`

> Maximum delay

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 5, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0004-p0001`

> Valid runs

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0005-p0001`

> Additional conditions

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 7, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0001-p0001`

> NORMAL

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0002-p0001`

> 10 through 30 degrees Celsius

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 9, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0003-p0001`

> 100 milliseconds

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0004-p0001`

> 3 per unit

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 11, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0005-p0001`

> Both channels measured

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0001-p0001`

> COLD

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 13, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0002-p0001`

> 0 through 9 degrees Celsius

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0003-p0001`

> 150 milliseconds

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 15, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0004-p0001`

> 3 per unit

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 16, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0005-p0001`

> Both channels measured and cold-fixture certificate

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 17, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0001-p0001`

> HOT

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0002-p0001`

> Above 30 degrees Celsius

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 19, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0003-p0001`

> No authorized threshold

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 20, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0004-p0001`

> No route

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 21, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0005-p0001`

> No qualification supplied

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 22, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

### Rules

- V2-01 selects version by test execution; V2-02 and V1-02 select profile thresholds; Annex X narrows the E17 exception.
- V2-03 release is a conjunction; V2-05 invalidity and calibration chronology cannot be replaced by favorable numbers.
- A supplied sufficient route does not establish universal necessity, missing measurements do not predict outcomes, and finite tests do not establish unbounded safety.

### Assumptions

- The fictional document authorities, exact integer values, profiles and event dates are accepted as supplied. Threshold selection is explicitly source-linked in the model notes.

### Reasoning

- 1. N02 is a named NORMAL unit at 20 degrees, tested after revision 2 began, without an applicable exception.
- 2. Its explicitly valid 101 observation exceeds 100. That one in-domain counterexample refutes the universal, independently of missing N03 evidence.

### Limits

- This concerns the named synthetic test events and the narrow stated assurance route, not certification of actual safety hardware.
- Formal targets encode reviewed rule selections; source authenticity and semantic fidelity remain outside kernel checking. Missing/invalid data are never silently promoted to valid observations.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim04` in module `Audit` (refutes): `¬ (∀ u, Audit.normal u = true → Audit.within u = true)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target014.lean) · [Actual proof log](logs/target-014.log)

### Recommendation

Replace the universal with per-unit outcomes; name N02 as the counterexample.

## C09-ERR-05

### Exact report claim

`input/report.md#C09-ERR-05`

> **C09-ERR-05.** E17 failed because 108 exceeds 100 milliseconds.

### Verification question

Did E17 fail because its maximum of 108 exceeds the general NORMAL limit?

### Source evidence

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0024`

> [V2-04] INCORPORATED EXCEPTION. Annex X changes the NORMAL delay threshold for one named serial number and a specific time interval. It changes no other requirement. In particular, it does not expand the temperature range, waive channel B measurement, make expired calibration current, close fault injections, or delegate release signing authority. The applicable general rule and exception must be combined before comparing observed delay. A general threshold alone is an incomplete rule set for a unit covered by an exception. Conversely, resemblance to the exempt unit does not extend an exception to other serial numbers or later dates.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 24, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0001`

> [X01] SYNTHETIC INCORPORATED ANNEX X. Requirements owner Mara Flint approved this exception under delegation AUTH-7 at 09:00 on 2 June 2033. It applies only to serial E17 for NORMAL tests executed from 09:00 on 2 June through 18:00 on 4 June inclusive. The maximum valid delay for those tests is 110 milliseconds rather than 100. The environment remains 10 through 30 degrees, and every other revision 2 prerequisite remains operative. The exception expressly does not apply to N02, even if N02 shares the same hardware build. The table records the operative scope rather than an illustrative example.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-3_2qqhln"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0012`

> [X02] AUTHORIZATION AND LIMITS. Mara holds authority to grant this bounded threshold change. Test operator Oren Vale does not possess that authority independently. The E17 runs on 3 June fall within the interval; a new test on 5 June would not. This annex cannot supply a missing channel measurement or a final release signature. The approval date, effective interval, and later report date are separate fields. An audit concluding that a 108-millisecond E17 run satisfies its requirement should cite both the general specification and this incorporated exception, including the identity and temporal match rather than merely quoting the larger number.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-3_2qqhln"}`.

- [input/sources/04-test-runs.pdf.md](input/sources/04-test-runs.pdf.md) — `pdf-page-0003`

> SYNTHETIC H-7 TEST PACKET
> [P03] Unit group: E17. Execution: 3 June 2033. Profile: NORMAL. Temperature: 20 degrees
> Celsius. Integer delay values: 104, 108, 106.
> Revision 2 and incorporated Annex X apply. All three runs are valid and within the named
> exception interval. Both channels were measured using K1, required fault injections were
> closed, and Sera Moss signed release. The largest value is 108, below the applicable 110
> threshold.
> [P03-METHOD] Each valid listed value is a distinct acquired observation for its named unit
> and profile. A missing observation cannot be replaced by a borrowed run, a copied previous
> value, or an assumed zero. The reviewer must first identify the applicable revision and any
> incorporated exception, then compare the exact observed number with the relevant threshold.
> The same numerical delay may pass one profile and fail another because the supplied criteria
> differ. This packet does not interpolate unspecified temperature ranges.
> [P03-SCOPE] This record supports a bounded demonstration. It supplies no production defect
> rate, lifetime prediction, or real-world safety certification. Preserve unit, execution
> time, profile, temperature, calibration, channel completeness, and validity when extracting
> a row. Cite the original PDF path and stable marker. A successful delay comparison does not
> automatically establish fault closure or signing authority. A failed valid run can refute a
> universal passing claim; a missing run instead identifies a support gap. The distinction
> must remain explicit in an evidence-backed audit result.

Original: [input/originals/D00006.pdf](input/originals/D00006.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 3, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0003.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-tidfeggy"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/05-calibration-and-authority.md](input/sources/05-calibration-and-authority.md) — `P02`

> [CAL01] Instrument K1 was calibrated through 23:59 on 30 June 2033 and was used for L01, N01, N02, E17, and C01 in the test packet. Instrument K2 expired at 23:59 on 1 June and was used for N03 on 3 June. K2 renewal is dated 5 June and contains no retrospective clause. Thus K1 has affirmative evidence of current calibration at the named runs, while K2 has affirmative evidence of expiry at its N03 use. A later renewal cannot be silently moved backward in time. The registry is complete for these instruments and dates, but it does not certify every instrument ever used by the fictional organization.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 48, "end_character": 651, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "f4d7b1be08d6dd13db756c34f068696ffe5ec31564ff09ac4b47a63db180e175", "artifact_directory": "extraction/D00007/attempt-lersvmwr"}`.

- [input/sources/05-calibration-and-authority.md](input/sources/05-calibration-and-authority.md) — `P03`

> [AUTH01] Mara Flint holds the AUTH-7 requirements-exception delegation for E17. Operator Oren Vale can execute and record tests but cannot change thresholds or authorize release. Release owner Sera Moss signed release entries for N01, E17, and C01 after checking their listed fault closures. No release signature is supplied for N03. N02 has an explicit release denial because its valid third delay run exceeded the applicable limit. The release ledger is complete for these named units through 5 June. A signatory identity is not interchangeable with a different role, and an operator's favorable comment is not a release signature.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 653, "end_character": 1286, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "f4d7b1be08d6dd13db756c34f068696ffe5ec31564ff09ac4b47a63db180e175", "artifact_directory": "extraction/D00007/attempt-lersvmwr"}`.

### Rules

- V2-01 selects version by test execution; V2-02 and V1-02 select profile thresholds; Annex X narrows the E17 exception.
- V2-03 release is a conjunction; V2-05 invalidity and calibration chronology cannot be replaced by favorable numbers.
- A supplied sufficient route does not establish universal necessity, missing measurements do not predict outcomes, and finite tests do not establish unbounded safety.

### Assumptions

- The fictional document authorities, exact integer values, profiles and event dates are accepted as supplied. Threshold selection is explicitly source-linked in the model notes.

### Reasoning

- 1. Annex X was authorized for E17 NORMAL from June 2 09:00 through June 4 18:00; its June 3 runs at 20 degrees are in scope.
- 2. The applicable limit is 110, not 100. All values 104,108,106 meet 110. The source separately records valid runs, channels, fault closure and authorized release.

### Limits

- This concerns the named synthetic test events and the narrow stated assurance route, not certification of actual safety hardware.
- Formal targets encode reviewed rule selections; source authenticity and semantic fidelity remain outside kernel checking. Missing/invalid data are never silently promoted to valid observations.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim05` in module `Audit` (refutes): `Audit.within Audit.Unit.e17 = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target015.lean) · [Actual proof log](logs/target-015.log)

### Recommendation

Report the bounded E17 pass under the incorporated exception, retaining its identity and dates.

## C09-ERR-06

### Exact report claim

`input/report.md#C09-ERR-06`

> **C09-ERR-06.** Annex X also grants the 110-millisecond allowance to N02.

### Verification question

Does Annex X extend the 110 threshold to N02?

### Source evidence

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0001`

> [X01] SYNTHETIC INCORPORATED ANNEX X. Requirements owner Mara Flint approved this exception under delegation AUTH-7 at 09:00 on 2 June 2033. It applies only to serial E17 for NORMAL tests executed from 09:00 on 2 June through 18:00 on 4 June inclusive. The maximum valid delay for those tests is 110 milliseconds rather than 100. The environment remains 10 through 30 degrees, and every other revision 2 prerequisite remains operative. The exception expressly does not apply to N02, even if N02 shares the same hardware build. The table records the operative scope rather than an illustrative example.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-3_2qqhln"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0012`

> [X02] AUTHORIZATION AND LIMITS. Mara holds authority to grant this bounded threshold change. Test operator Oren Vale does not possess that authority independently. The E17 runs on 3 June fall within the interval; a new test on 5 June would not. This annex cannot supply a missing channel measurement or a final release signature. The approval date, effective interval, and later report date are separate fields. An audit concluding that a 108-millisecond E17 run satisfies its requirement should cite both the general specification and this incorporated exception, including the identity and temporal match rather than merely quoting the larger number.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-3_2qqhln"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0013`

> [X03] REQUEST HISTORY. The stated synthetic rationale is a demonstration fixture with an extra reporting stage. An informal proposal sought the same allowance for all units, but that proposal was rejected. Only the narrow E17 text became operative. A rationale explains a request; it does not enlarge approved scope. A forwarded subject line reading threshold allowance cannot substitute for the final signed body. No additional exception appears in the complete exception register for the named units during this interval. This bounded completeness helps reject a fabricated N02 exemption without claiming that no exception could ever exist in a different period.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 13, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-3_2qqhln"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0024`

> [V2-04] INCORPORATED EXCEPTION. Annex X changes the NORMAL delay threshold for one named serial number and a specific time interval. It changes no other requirement. In particular, it does not expand the temperature range, waive channel B measurement, make expired calibration current, close fault injections, or delegate release signing authority. The applicable general rule and exception must be combined before comparing observed delay. A general threshold alone is an incomplete rule set for a unit covered by an exception. Conversely, resemblance to the exempt unit does not extend an exception to other serial numbers or later dates.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 24, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

### Rules

- V2-01 selects version by test execution; V2-02 and V1-02 select profile thresholds; Annex X narrows the E17 exception.
- V2-03 release is a conjunction; V2-05 invalidity and calibration chronology cannot be replaced by favorable numbers.
- A supplied sufficient route does not establish universal necessity, missing measurements do not predict outcomes, and finite tests do not establish unbounded safety.

### Assumptions

- The fictional document authorities, exact integer values, profiles and event dates are accepted as supplied. Threshold selection is explicitly source-linked in the model notes.

### Reasoning

- 1. The approved exception names E17 only and explicitly excludes N02, regardless of shared hardware.
- 2. The broad proposal was rejected; the complete bounded exception register supplies no N02 exception.

### Limits

- This concerns the named synthetic test events and the narrow stated assurance route, not certification of actual safety hardware.
- Formal targets encode reviewed rule selections; source authenticity and semantic fidelity remain outside kernel checking. Missing/invalid data are never silently promoted to valid observations.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim06` in module `Audit` (refutes): `Audit.annexApplies Audit.Unit.n02 = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target016.lean) · [Actual proof log](logs/target-016.log)

### Recommendation

Keep N02 at its general 100 limit.

## C09-ERR-07

### Exact report claim

`input/report.md#C09-ERR-07`

> **C09-ERR-07.** C01 failed its applicable requirement because 149 exceeds 100.

### Verification question

Did C01 fail its applicable profile because its maximum is above 100?

### Source evidence

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0002`

> [V2-02] CURRENT ACCEPTANCE TABLE. Every endpoint in the stated intervals is inclusive. A valid NORMAL delay of 100 milliseconds satisfies the numeric limit; 101 does not. The COLD route additionally requires a current cold-fixture certificate. There is no supplied HOT route, and no route below zero degrees. A table row cannot be applied without checking the environment and profile. The limits in this synthetic exercise are exact integer comparisons; realistic measurement error models are outside scope. The absence of an error model must not be filled by an invented uncertainty discount or an assumed rounding allowance.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 2, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/04-test-runs.pdf.md](input/sources/04-test-runs.pdf.md) — `pdf-page-0004`

> SYNTHETIC H-7 TEST PACKET
> [P04] Unit group: C01. Execution: 3 June 2033. Profile: COLD. Temperature: 5 degrees
> Celsius. Integer delay values: 142, 145, 149.
> Revision 2 COLD applies. All three runs are valid. The cold-fixture certificate is present
> and current. Both channels were measured with K1, fault injections were closed, and Sera
> Moss signed release. The applicable limit is 150, not the NORMAL limit of 100.
> [P04-METHOD] Each valid listed value is a distinct acquired observation for its named unit
> and profile. A missing observation cannot be replaced by a borrowed run, a copied previous
> value, or an assumed zero. The reviewer must first identify the applicable revision and any
> incorporated exception, then compare the exact observed number with the relevant threshold.
> The same numerical delay may pass one profile and fail another because the supplied criteria
> differ. This packet does not interpolate unspecified temperature ranges.
> [P04-SCOPE] This record supports a bounded demonstration. It supplies no production defect
> rate, lifetime prediction, or real-world safety certification. Preserve unit, execution
> time, profile, temperature, calibration, channel completeness, and validity when extracting
> a row. Cite the original PDF path and stable marker. A successful delay comparison does not
> automatically establish fault closure or signing authority. A failed valid run can refute a
> universal passing claim; a missing run instead identifies a support gap. The distinction
> must remain explicit in an evidence-backed audit result.

Original: [input/originals/D00006.pdf](input/originals/D00006.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 4, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0004.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-tidfeggy"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/06-applicability-and-open-items.md](input/sources/06-applicability-and-open-items.md) — `P02`

> [AP01] C01 is a COLD-profile unit tested at 5 degrees with a current cold-fixture certificate; its limit is 150 milliseconds. N01, N02, N03, and E17 were tested at 20 degrees under NORMAL. No valid HOT qualification or authorized threshold above 30 degrees is supplied. The packet therefore does not establish a claim of qualification across every temperature. This missing scope is not a measurement proving that all hot operation physically fails. An analyst should state the unsupported extension precisely rather than discard the bounded favorable evidence for C01 or N01.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 42, "end_character": 618, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "dec4280b23593ada8abc1e1648682a3f31385bd2a7146aed36688ab157b715dc", "artifact_directory": "extraction/D00008/attempt-6dw0cals"}`.

- [input/sources/05-calibration-and-authority.md](input/sources/05-calibration-and-authority.md) — `P02`

> [CAL01] Instrument K1 was calibrated through 23:59 on 30 June 2033 and was used for L01, N01, N02, E17, and C01 in the test packet. Instrument K2 expired at 23:59 on 1 June and was used for N03 on 3 June. K2 renewal is dated 5 June and contains no retrospective clause. Thus K1 has affirmative evidence of current calibration at the named runs, while K2 has affirmative evidence of expiry at its N03 use. A later renewal cannot be silently moved backward in time. The registry is complete for these instruments and dates, but it does not certify every instrument ever used by the fictional organization.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 48, "end_character": 651, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "f4d7b1be08d6dd13db756c34f068696ffe5ec31564ff09ac4b47a63db180e175", "artifact_directory": "extraction/D00007/attempt-lersvmwr"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0001-p0001`

> Profile

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 3, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0002-p0001`

> Environment

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0003-p0001`

> Maximum delay

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 5, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0004-p0001`

> Valid runs

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0001-c0005-p0001`

> Additional conditions

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 7, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0001-p0001`

> NORMAL

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0002-p0001`

> 10 through 30 degrees Celsius

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 9, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0003-p0001`

> 100 milliseconds

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0004-p0001`

> 3 per unit

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 11, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0005-p0001`

> Both channels measured

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0001-p0001`

> COLD

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 13, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0002-p0001`

> 0 through 9 degrees Celsius

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0003-p0001`

> 150 milliseconds

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 15, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0004-p0001`

> 3 per unit

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 16, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0005-p0001`

> Both channels measured and cold-fixture certificate

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 17, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0001-p0001`

> HOT

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0002-p0001`

> Above 30 degrees Celsius

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 19, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0003-p0001`

> No authorized threshold

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 20, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0004-p0001`

> No route

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 21, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0005-p0001`

> No qualification supplied

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 22, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

### Rules

- V2-01 selects version by test execution; V2-02 and V1-02 select profile thresholds; Annex X narrows the E17 exception.
- V2-03 release is a conjunction; V2-05 invalidity and calibration chronology cannot be replaced by favorable numbers.
- A supplied sufficient route does not establish universal necessity, missing measurements do not predict outcomes, and finite tests do not establish unbounded safety.

### Assumptions

- The fictional document authorities, exact integer values, profiles and event dates are accepted as supplied. Threshold selection is explicitly source-linked in the model notes.

### Reasoning

- 1. C01 is COLD at 5 degrees with a current cold-fixture certificate; the profile limit is 150.
- 2. Its three valid values 142,145,149 all meet 150. The NORMAL limit does not apply to this event.

### Limits

- This concerns the named synthetic test events and the narrow stated assurance route, not certification of actual safety hardware.
- Formal targets encode reviewed rule selections; source authenticity and semantic fidelity remain outside kernel checking. Missing/invalid data are never silently promoted to valid observations.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim07` in module `Audit` (refutes): `Audit.within Audit.Unit.c01 = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target017.lean) · [Actual proof log](logs/target-017.log)

### Recommendation

Report C01's COLD demonstration pass without extending it to other temperatures.

## C09-ERR-08

### Exact report claim

`input/report.md#C09-ERR-08`

> **C09-ERR-08.** N03 channel B would have passed if measured.

### Verification question

Can the unmeasured N03 channel B outcome be predicted as passing?

### Source evidence

- [input/sources/06-applicability-and-open-items.md](input/sources/06-applicability-and-open-items.md) — `P03`

> [AP02] N03 lacks channel B measurement and a third valid repeated run. Its second attempted trace aborted before acquisition and has no delay value. X99 has a raw 85-millisecond number but is explicitly invalid because synchronization was lost. It cannot contribute to N03 or any other unit's valid-run count. The correct support-gap finding identifies the exact missing channel and repetition, relevant requirement, and unavailable evidence. It does not predict what the unmeasured channel would have done. Invalid, missing, and explicitly failing measurements have different meanings and must remain distinguishable in the report.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 620, "end_character": 1252, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "dec4280b23593ada8abc1e1648682a3f31385bd2a7146aed36688ab157b715dc", "artifact_directory": "extraction/D00008/attempt-6dw0cals"}`.

- [input/sources/04-test-runs.pdf.md](input/sources/04-test-runs.pdf.md) — `pdf-page-0005`

> SYNTHETIC H-7 TEST PACKET
> [P05] Unit group: N03 and trace X99. Execution: 3 June 2033. Profile: NORMAL. Temperature:
> 20 degrees Celsius. Integer delay values: N03: first valid run 94; second attempt blank;
> third run absent. X99: 85 INVALID.
> N03 used K2 after its expiry. Channel B has no measurement, fault closure is missing, and no
> release signature is supplied. The second attempt aborted before acquisition; blank does not
> mean zero. X99 lost clock synchronization and is explicitly invalid. No supplied record
> repairs these gaps.
> [P05-METHOD] Each valid listed value is a distinct acquired observation for its named unit
> and profile. A missing observation cannot be replaced by a borrowed run, a copied previous
> value, or an assumed zero. The reviewer must first identify the applicable revision and any
> incorporated exception, then compare the exact observed number with the relevant threshold.
> The same numerical delay may pass one profile and fail another because the supplied criteria
> differ. This packet does not interpolate unspecified temperature ranges.
> [P05-SCOPE] This record supports a bounded demonstration. It supplies no production defect
> rate, lifetime prediction, or real-world safety certification. Preserve unit, execution
> time, profile, temperature, calibration, channel completeness, and validity when extracting
> a row. Cite the original PDF path and stable marker. A successful delay comparison does not
> automatically establish fault closure or signing authority. A failed valid run can refute a
> universal passing claim; a missing run instead identifies a support gap. The distinction
> must remain explicit in an evidence-backed audit result.

Original: [input/originals/D00006.pdf](input/originals/D00006.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 5, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0005.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-tidfeggy"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0023`

> [V2-03] RELEASE CONJUNCTION. The specified release route requires an applicable delay demonstration, current calibration at every contributing run, both sensor channels measured, closure of the required fault injections, and an authorized release signature. Each conjunct is necessary under this route. Their conjunction is sufficient only within the finite H-7 demonstration scope. A signature does not overwrite an explicit failed run. A favorable channel A result cannot establish an absent channel B result. An explicit recorded failure supplies a counterexample to a claim that all requirements passed; a missing measurement instead leaves a required argument unsupported. These evidentiary situations should not be collapsed into one generic negative verdict.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 23, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-p-0024`

> [V1-04] DATA HANDLING. A run aborted before acquisition supplies no delay measurement. A blank cell means unavailable evidence unless a signed explanatory note explicitly gives another meaning. It is not zero. An operator may invalidate a trace after discovering synchronization loss; the invalidation accompanies the printed value. Each extraction should retain unit identity, run date, profile, environment, validity, instrument, measured channels, and observed value. Comparing a column of numbers without those fields can apply the wrong revision or count invalid evidence. Missing measurements should be reported as concrete support gaps, not silently replaced by favorable numbers from a neighboring row.

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 24, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

### Rules

- V2-01 selects version by test execution; V2-02 and V1-02 select profile thresholds; Annex X narrows the E17 exception.
- V2-03 release is a conjunction; V2-05 invalidity and calibration chronology cannot be replaced by favorable numbers.
- A supplied sufficient route does not establish universal necessity, missing measurements do not predict outcomes, and finite tests do not establish unbounded safety.

### Assumptions

- The fictional document authorities, exact integer values, profiles and event dates are accepted as supplied. Threshold selection is explicitly source-linked in the model notes.

### Reasoning

- 1. No channel B measurement is supplied, and AP02 expressly distinguishes missing evidence from an observed outcome.
- 2. The favorable first delay value and neighboring units cannot determine what an unmeasured channel would have done. Full-corpus review finds no substitute evidence.

### Limits

- This concerns the named synthetic test events and the narrow stated assurance route, not certification of actual safety hardware.
- Formal targets encode reviewed rule selections; source authenticity and semantic fidelity remain outside kernel checking. Missing/invalid data are never silently promoted to valid observations.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **blocked**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Obtain a valid channel B measurement; retain a support gap without declaring physical failure.

## C09-ERR-09

### Exact report claim

`input/report.md#C09-ERR-09`

> **C09-ERR-09.** K2 was current at the N03 run because it was renewed on 5 June.

### Verification question

Was K2 current during the June 3 N03 run because it was renewed June 5?

### Source evidence

- [input/sources/05-calibration-and-authority.md](input/sources/05-calibration-and-authority.md) — `P02`

> [CAL01] Instrument K1 was calibrated through 23:59 on 30 June 2033 and was used for L01, N01, N02, E17, and C01 in the test packet. Instrument K2 expired at 23:59 on 1 June and was used for N03 on 3 June. K2 renewal is dated 5 June and contains no retrospective clause. Thus K1 has affirmative evidence of current calibration at the named runs, while K2 has affirmative evidence of expiry at its N03 use. A later renewal cannot be silently moved backward in time. The registry is complete for these instruments and dates, but it does not certify every instrument ever used by the fictional organization.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 48, "end_character": 651, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "f4d7b1be08d6dd13db756c34f068696ffe5ec31564ff09ac4b47a63db180e175", "artifact_directory": "extraction/D00007/attempt-lersvmwr"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0025`

> [V2-05] VALIDITY AND TIME. A recorded clock synchronization failure invalidates the affected trace even if its printed delay is small. Repeated runs belong to their named unit and profile. Calibration is current only when the run timestamp is on or before the stated expiry instant. A renewal after a run is not retrospective unless an authorized statement explicitly says it is. The packet contains no such retrospective calibration statement. The analyst must distinguish an absent certificate from a certificate affirmatively showing expiry. Both may prevent an assurance argument, but only the latter supplies direct contrary evidence about calibration at the specific instant.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[5]", "paragraph_index_in_story": 25, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/04-test-runs.pdf.md](input/sources/04-test-runs.pdf.md) — `pdf-page-0005`

> SYNTHETIC H-7 TEST PACKET
> [P05] Unit group: N03 and trace X99. Execution: 3 June 2033. Profile: NORMAL. Temperature:
> 20 degrees Celsius. Integer delay values: N03: first valid run 94; second attempt blank;
> third run absent. X99: 85 INVALID.
> N03 used K2 after its expiry. Channel B has no measurement, fault closure is missing, and no
> release signature is supplied. The second attempt aborted before acquisition; blank does not
> mean zero. X99 lost clock synchronization and is explicitly invalid. No supplied record
> repairs these gaps.
> [P05-METHOD] Each valid listed value is a distinct acquired observation for its named unit
> and profile. A missing observation cannot be replaced by a borrowed run, a copied previous
> value, or an assumed zero. The reviewer must first identify the applicable revision and any
> incorporated exception, then compare the exact observed number with the relevant threshold.
> The same numerical delay may pass one profile and fail another because the supplied criteria
> differ. This packet does not interpolate unspecified temperature ranges.
> [P05-SCOPE] This record supports a bounded demonstration. It supplies no production defect
> rate, lifetime prediction, or real-world safety certification. Preserve unit, execution
> time, profile, temperature, calibration, channel completeness, and validity when extracting
> a row. Cite the original PDF path and stable marker. A successful delay comparison does not
> automatically establish fault closure or signing authority. A failed valid run can refute a
> universal passing claim; a missing run instead identifies a support gap. The distinction
> must remain explicit in an evidence-backed audit result.

Original: [input/originals/D00006.pdf](input/originals/D00006.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 5, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0005.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-tidfeggy"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

### Rules

- V2-01 selects version by test execution; V2-02 and V1-02 select profile thresholds; Annex X narrows the E17 exception.
- V2-03 release is a conjunction; V2-05 invalidity and calibration chronology cannot be replaced by favorable numbers.
- A supplied sufficient route does not establish universal necessity, missing measurements do not predict outcomes, and finite tests do not establish unbounded safety.

### Assumptions

- The fictional document authorities, exact integer values, profiles and event dates are accepted as supplied. Threshold selection is explicitly source-linked in the model notes.

### Reasoning

- 1. K2 affirmatively expired June 1 at 23:59. Its use on June 3 is after expiry.
- 2. The June 5 renewal has no retrospective clause and cannot establish current calibration two days earlier. This is contrary evidence, not merely an absent certificate.

### Limits

- This concerns the named synthetic test events and the narrow stated assurance route, not certification of actual safety hardware.
- Formal targets encode reviewed rule selections; source authenticity and semantic fidelity remain outside kernel checking. Missing/invalid data are never silently promoted to valid observations.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim09` in module `Audit` (refutes): `¬ Audit.n03RunDay ≤ Audit.k2ExpiryDay`.
  [Model](models/Audit.lean) · [Executed check](checks/Target018.lean) · [Actual proof log](logs/target-018.log)

### Recommendation

Record expired calibration at the N03 run; distinguish later renewal.

## C09-ERR-10

### Exact report claim

`input/report.md#C09-ERR-10`

> **C09-ERR-10.** X99 is a valid 85-millisecond run that replaces N03 missing repetition.

### Verification question

Is X99 a valid 85-millisecond measurement usable as N03's missing repetition?

### Source evidence

- [input/sources/04-test-runs.pdf.md](input/sources/04-test-runs.pdf.md) — `pdf-page-0005`

> SYNTHETIC H-7 TEST PACKET
> [P05] Unit group: N03 and trace X99. Execution: 3 June 2033. Profile: NORMAL. Temperature:
> 20 degrees Celsius. Integer delay values: N03: first valid run 94; second attempt blank;
> third run absent. X99: 85 INVALID.
> N03 used K2 after its expiry. Channel B has no measurement, fault closure is missing, and no
> release signature is supplied. The second attempt aborted before acquisition; blank does not
> mean zero. X99 lost clock synchronization and is explicitly invalid. No supplied record
> repairs these gaps.
> [P05-METHOD] Each valid listed value is a distinct acquired observation for its named unit
> and profile. A missing observation cannot be replaced by a borrowed run, a copied previous
> value, or an assumed zero. The reviewer must first identify the applicable revision and any
> incorporated exception, then compare the exact observed number with the relevant threshold.
> The same numerical delay may pass one profile and fail another because the supplied criteria
> differ. This packet does not interpolate unspecified temperature ranges.
> [P05-SCOPE] This record supports a bounded demonstration. It supplies no production defect
> rate, lifetime prediction, or real-world safety certification. Preserve unit, execution
> time, profile, temperature, calibration, channel completeness, and validity when extracting
> a row. Cite the original PDF path and stable marker. A successful delay comparison does not
> automatically establish fault closure or signing authority. A failed valid run can refute a
> universal passing claim; a missing run instead identifies a support gap. The distinction
> must remain explicit in an evidence-backed audit result.

Original: [input/originals/D00006.pdf](input/originals/D00006.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 5, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0005.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-tidfeggy"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/06-applicability-and-open-items.md](input/sources/06-applicability-and-open-items.md) — `P03`

> [AP02] N03 lacks channel B measurement and a third valid repeated run. Its second attempted trace aborted before acquisition and has no delay value. X99 has a raw 85-millisecond number but is explicitly invalid because synchronization was lost. It cannot contribute to N03 or any other unit's valid-run count. The correct support-gap finding identifies the exact missing channel and repetition, relevant requirement, and unavailable evidence. It does not predict what the unmeasured channel would have done. Invalid, missing, and explicitly failing measurements have different meanings and must remain distinguishable in the report.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 620, "end_character": 1252, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "dec4280b23593ada8abc1e1648682a3f31385bd2a7146aed36688ab157b715dc", "artifact_directory": "extraction/D00008/attempt-6dw0cals"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0025`

> [V2-05] VALIDITY AND TIME. A recorded clock synchronization failure invalidates the affected trace even if its printed delay is small. Repeated runs belong to their named unit and profile. Calibration is current only when the run timestamp is on or before the stated expiry instant. A renewal after a run is not retrospective unless an authorized statement explicitly says it is. The packet contains no such retrospective calibration statement. The analyst must distinguish an absent certificate from a certificate affirmatively showing expiry. Both may prevent an assurance argument, but only the latter supplies direct contrary evidence about calibration at the specific instant.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[5]", "paragraph_index_in_story": 25, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-p-0024`

> [V1-04] DATA HANDLING. A run aborted before acquisition supplies no delay measurement. A blank cell means unavailable evidence unless a signed explanatory note explicitly gives another meaning. It is not zero. An operator may invalidate a trace after discovering synchronization loss; the invalidation accompanies the printed value. Each extraction should retain unit identity, run date, profile, environment, validity, instrument, measured channels, and observed value. Comparing a column of numbers without those fields can apply the wrong revision or count invalid evidence. Missing measurements should be reported as concrete support gaps, not silently replaced by favorable numbers from a neighboring row.

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 24, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

### Rules

- V2-01 selects version by test execution; V2-02 and V1-02 select profile thresholds; Annex X narrows the E17 exception.
- V2-03 release is a conjunction; V2-05 invalidity and calibration chronology cannot be replaced by favorable numbers.
- A supplied sufficient route does not establish universal necessity, missing measurements do not predict outcomes, and finite tests do not establish unbounded safety.

### Assumptions

- The fictional document authorities, exact integer values, profiles and event dates are accepted as supplied. Threshold selection is explicitly source-linked in the model notes.

### Reasoning

- 1. The raw value is expressly labeled INVALID following synchronization loss.
- 2. Invalid traces contribute no valid run; identity-specific repetition cannot be repaired by copying another trace. Invalidity alone refutes the compound assertion.

### Limits

- This concerns the named synthetic test events and the narrow stated assurance route, not certification of actual safety hardware.
- Formal targets encode reviewed rule selections; source authenticity and semantic fidelity remain outside kernel checking. Missing/invalid data are never silently promoted to valid observations.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim10` in module `Audit` (refutes): `Audit.x99Valid ≠ true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target019.lean) · [Actual proof log](logs/target-019.log)

### Recommendation

Exclude X99 from valid repetitions and identify the N03 missing/aborted runs.

## C09-ERR-11

### Exact report claim

`input/report.md#C09-ERR-11`

> **C09-ERR-11.** Passing delay alone is sufficient for full release.

### Verification question

Does a passing delay alone suffice for full release under the specified route?

### Source evidence

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0023`

> [V2-03] RELEASE CONJUNCTION. The specified release route requires an applicable delay demonstration, current calibration at every contributing run, both sensor channels measured, closure of the required fault injections, and an authorized release signature. Each conjunct is necessary under this route. Their conjunction is sufficient only within the finite H-7 demonstration scope. A signature does not overwrite an explicit failed run. A favorable channel A result cannot establish an absent channel B result. An explicit recorded failure supplies a counterexample to a claim that all requirements passed; a missing measurement instead leaves a required argument unsupported. These evidentiary situations should not be collapsed into one generic negative verdict.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 23, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-p-0023`

> [V1-03] IMPLICATION DIRECTION. Three valid NORMAL runs within the applicable limit are sufficient for the narrowly defined delay demonstration. They are not stated necessary for every conceivable alternative assurance method. Full release additionally requires current calibration, both sensor channels measured, closure of required fault injections, and an authorized release signature. Passing a delay subrequirement alone is therefore insufficient for full release. The specification intentionally distinguishes a sufficient route to one predicate from a conjunction of prerequisites for another predicate. An audit must not reverse an implication merely because its converse sounds plausible or because no alternative route is described in this packet.

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 23, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/07-fault-closure-register.md](input/sources/07-fault-closure-register.md) — `P02`

> [FC01] Scope of the closure records. The required demonstration fault set contains three named injections: simulated stuck channel A, simulated stuck channel B, and loss of the synthetic telemetry heartbeat. These are invented administrative test labels, not instructions for testing or deploying actual hardware. A closure entry means the named required exercise was performed and its stipulated acceptance record was signed. It does not add a new measured trip-delay run. A unit may therefore have a complete delay demonstration while still lacking fault closure, or possess fault closure while an independent delay run fails. The register keeps these predicates separate.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 46, "end_character": 720, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "832f5bc068a88b4ee4756897c1c5f36af0e6ba4e0f76e4581918223f338b1d3b", "artifact_directory": "extraction/D00009/attempt-u5l3atgr"}`.

- [input/sources/07-fault-closure-register.md](input/sources/07-fault-closure-register.md) — `P05`

> [FC04] N02 and N03 disposition. N02's valid 101-millisecond run remains a failed delay requirement regardless of whether other administrative records are favorable. The release denial explicitly cites that run, and no closure statement in this register overrides it. N03 has no completed closure set in the supplied packet. The operator's worksheet has three empty closure slots marked pending. Those slots are missing assurance evidence; they do not describe observed physical behavior under the unperformed or undocumented injections. The audit should report the required argument that is absent without inventing an injection outcome or treating pending as a numerical failure measurement.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 1979, "end_character": 2671, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "832f5bc068a88b4ee4756897c1c5f36af0e6ba4e0f76e4581918223f338b1d3b", "artifact_directory": "extraction/D00009/attempt-u5l3atgr"}`.

### Rules

- V2-01 selects version by test execution; V2-02 and V1-02 select profile thresholds; Annex X narrows the E17 exception.
- V2-03 release is a conjunction; V2-05 invalidity and calibration chronology cannot be replaced by favorable numbers.
- A supplied sufficient route does not establish universal necessity, missing measurements do not predict outcomes, and finite tests do not establish unbounded safety.

### Assumptions

- The fictional document authorities, exact integer values, profiles and event dates are accepted as supplied. Threshold selection is explicitly source-linked in the model notes.

### Reasoning

- 1. V2-03 requires delay, current calibration, both channels, fault closure and authorized signature.
- 2. A model with passing delay and absent fault closure satisfies the definition but does not release. This refutes the claimed sufficiency of delay alone, not the actual physical safety of an untested unit.

### Limits

- This concerns the named synthetic test events and the narrow stated assurance route, not certification of actual safety hardware.
- Formal targets encode reviewed rule selections; source authenticity and semantic fidelity remain outside kernel checking. Missing/invalid data are never silently promoted to valid observations.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim11` in module `Audit` (refutes): `¬ (∀ c b f s : Bool, Audit.release true c b f s = true)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target020.lean) · [Actual proof log](logs/target-020.log)

### Recommendation

Require evidence for every release conjunct.

## C09-ERR-12

### Exact report claim

`input/report.md#C09-ERR-12`

> **C09-ERR-12.** Every possible compliant assurance method must use exactly the listed three-run route.

### Verification question

Must every conceivable compliant assurance method necessarily use the supplied three-run route?

### Source evidence

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0014`

> [X04] ALTERNATIVE METHODS. The three-run route is sufficient for its bounded delay demonstration, not stated necessary for every possible assurance method. No alternative qualification argument is supplied for N03. Therefore this packet cannot establish N03 through an unspecified alternative, while it also does not prove that every conceivable alternative is impossible. The reviewer should identify the missing necessity argument in a claim that the listed route is universally mandatory. Absence of an alternative in a finite packet is not a formal counterexample to such necessity; it simply leaves that broader assertion unproved. The distinction between refutation and unsupported generalization is intentional.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-3_2qqhln"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-p-0023`

> [V1-03] IMPLICATION DIRECTION. Three valid NORMAL runs within the applicable limit are sufficient for the narrowly defined delay demonstration. They are not stated necessary for every conceivable alternative assurance method. Full release additionally requires current calibration, both sensor channels measured, closure of required fault injections, and an authorized release signature. Passing a delay subrequirement alone is therefore insufficient for full release. The specification intentionally distinguishes a sufficient route to one predicate from a conjunction of prerequisites for another predicate. An audit must not reverse an implication merely because its converse sounds plausible or because no alternative route is described in this packet.

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 23, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

- [input/sources/07-fault-closure-register.md](input/sources/07-fault-closure-register.md) — `P06`

> [FC05] Configuration and signature custody. Every signed closure includes a unit identifier, the applicable profile, the required injection label, and the review date. A later formatting copy retains the original effective facts but does not turn a missing signature into an approved one. The register is complete for closure entries supplied for the named units through 5 June, while it makes no claim about unnamed units or later tests. This bounded source statement supports evidence inventory findings. It does not establish that no other method could ever supply assurance, nor does it expand the finite demonstration into a universal assertion of real-world safety.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 11, "start_character": 2673, "end_character": 3344, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "832f5bc068a88b4ee4756897c1c5f36af0e6ba4e0f76e4581918223f338b1d3b", "artifact_directory": "extraction/D00009/attempt-u5l3atgr"}`.

### Rules

- V2-01 selects version by test execution; V2-02 and V1-02 select profile thresholds; Annex X narrows the E17 exception.
- V2-03 release is a conjunction; V2-05 invalidity and calibration chronology cannot be replaced by favorable numbers.
- A supplied sufficient route does not establish universal necessity, missing measurements do not predict outcomes, and finite tests do not establish unbounded safety.

### Assumptions

- The fictional document authorities, exact integer values, profiles and event dates are accepted as supplied. Threshold selection is explicitly source-linked in the model notes.

### Reasoning

- 1. The documents give a sufficient bounded route, not a necessity theorem over all methods.
- 2. No alternative argument is supplied for N03, but absence of alternatives does not prove no alternative can exist. Neither a necessity proof nor a concrete compliant alternative refuting it is supplied.

### Limits

- This concerns the named synthetic test events and the narrow stated assurance route, not certification of actual safety hardware.
- Formal targets encode reviewed rule selections; source authenticity and semantic fidelity remain outside kernel checking. Missing/invalid data are never silently promoted to valid observations.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **blocked**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Limit the assertion to the listed route; request an explicit necessity rule before generalizing.

## C09-ERR-13

### Exact report claim

`input/report.md#C09-ERR-13`

> **C09-ERR-13.** The design is safe at every temperature throughout its lifetime.

### Verification question

Does the packet establish safety at every temperature over the design's entire lifetime?

### Source evidence

- [input/sources/06-applicability-and-open-items.md](input/sources/06-applicability-and-open-items.md) — `P02`

> [AP01] C01 is a COLD-profile unit tested at 5 degrees with a current cold-fixture certificate; its limit is 150 milliseconds. N01, N02, N03, and E17 were tested at 20 degrees under NORMAL. No valid HOT qualification or authorized threshold above 30 degrees is supplied. The packet therefore does not establish a claim of qualification across every temperature. This missing scope is not a measurement proving that all hot operation physically fails. An analyst should state the unsupported extension precisely rather than discard the bounded favorable evidence for C01 or N01.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 42, "end_character": 618, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "dec4280b23593ada8abc1e1648682a3f31385bd2a7146aed36688ab157b715dc", "artifact_directory": "extraction/D00008/attempt-6dw0cals"}`.

- [input/sources/06-applicability-and-open-items.md](input/sources/06-applicability-and-open-items.md) — `P04`

> [AP03] The packet provides no argument about population defect rates, lifetime reliability, network threats, mechanical strength, or an unrestricted meaning of safe. The finite release conjunction is narrower than universal design safety. Aesthetic opinions about the clarity or beauty of a specification are likewise outside the threshold predicates unless a separate criterion is supplied. The exercise is a reasoning fixture using invented documents, not guidance for deploying a real safety system. Favorable arithmetic and complete signatures can support the specified synthetic release route without supporting unbounded real-world conclusions.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1254, "end_character": 1904, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "dec4280b23593ada8abc1e1648682a3f31385bd2a7146aed36688ab157b715dc", "artifact_directory": "extraction/D00008/attempt-6dw0cals"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0026`

> [V2-06] REVIEW UNIVERSE. The named units are L01, N01, N02, N03, E17, and C01; X99 is an invalid demonstration trace. These cases do not constitute a random sample of a production population. No statistical inference about all manufactured controllers is supplied. A universal statement about the named valid runs can be refuted by one in-scope explicit run above its applicable threshold. A universal statement about all temperatures requires additional defined criteria and observations. Preserve successful bounded demonstrations while identifying unsupported extensions. Every name, signature, instrument, and event here is synthetic, so no conclusion should be mistaken for certification of a real product.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 26, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-p-0001`

> [V1-01] SYNTHETIC H-7 SPECIFICATION, REVISION 1. This document concerns the fictional Heliostat H-7 demonstration controller. It is not an actual safety standard and supplies no real-world safety advice. Revision 1 applies to tests executed before 1 June 2033 unless an explicitly approved profile says otherwise. The finite demonstration concerns measured trip delay under stated laboratory conditions. It does not certify lifetime reliability, mechanical protection, network security, or population defect rates. A report should identify the proposition actually tested rather than replace it with an undefined claim that the whole design is safe. The table below defines exact synthetic limits for this bounded exercise.

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-kpt318mr"}`.

### Rules

- V2-01 selects version by test execution; V2-02 and V1-02 select profile thresholds; Annex X narrows the E17 exception.
- V2-03 release is a conjunction; V2-05 invalidity and calibration chronology cannot be replaced by favorable numbers.
- A supplied sufficient route does not establish universal necessity, missing measurements do not predict outcomes, and finite tests do not establish unbounded safety.

### Assumptions

- The fictional document authorities, exact integer values, profiles and event dates are accepted as supplied. Threshold selection is explicitly source-linked in the model notes.

### Reasoning

- 1. The evidence is bounded laboratory delay/release demonstration, with no HOT route above 30 degrees or route below zero.
- 2. No lifetime, population, mechanical or network argument supplies the additional scope; undefined global safety cannot be inferred from finite favorable measurements.
- 3. This absence does not prove unsafe operation at every omitted condition.

### Limits

- This concerns the named synthetic test events and the narrow stated assurance route, not certification of actual safety hardware.
- Formal targets encode reviewed rule selections; source authenticity and semantic fidelity remain outside kernel checking. Missing/invalid data are never silently promoted to valid observations.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **blocked**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

State only the supported profile/event results; obtain defined lifetime and full-temperature criteria and evidence for the broader claim.

## C09-ERR-14

### Exact report claim

`input/report.md#C09-ERR-14`

> **C09-ERR-14.** The specification is beautifully organized.

### Verification question

Is there a supplied formal criterion for the specification being beautifully organized?

### Source evidence

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0026`

> [V2-06] REVIEW UNIVERSE. The named units are L01, N01, N02, N03, E17, and C01; X99 is an invalid demonstration trace. These cases do not constitute a random sample of a production population. No statistical inference about all manufactured controllers is supplied. A universal statement about the named valid runs can be refuted by one in-scope explicit run above its applicable threshold. A universal statement about all temperatures requires additional defined criteria and observations. Preserve successful bounded demonstrations while identifying unsupported extensions. Every name, signature, instrument, and event here is synthetic, so no conclusion should be mistaken for certification of a real product.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 26, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-j56kwram"}`.

- [input/sources/06-applicability-and-open-items.md](input/sources/06-applicability-and-open-items.md) — `P04`

> [AP03] The packet provides no argument about population defect rates, lifetime reliability, network threats, mechanical strength, or an unrestricted meaning of safe. The finite release conjunction is narrower than universal design safety. Aesthetic opinions about the clarity or beauty of a specification are likewise outside the threshold predicates unless a separate criterion is supplied. The exercise is a reasoning fixture using invented documents, not guidance for deploying a real safety system. Favorable arithmetic and complete signatures can support the specified synthetic release route without supporting unbounded real-world conclusions.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1254, "end_character": 1904, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "dec4280b23593ada8abc1e1648682a3f31385bd2a7146aed36688ab157b715dc", "artifact_directory": "extraction/D00008/attempt-6dw0cals"}`.

### Rules

- V2-01 selects version by test execution; V2-02 and V1-02 select profile thresholds; Annex X narrows the E17 exception.
- V2-03 release is a conjunction; V2-05 invalidity and calibration chronology cannot be replaced by favorable numbers.
- A supplied sufficient route does not establish universal necessity, missing measurements do not predict outcomes, and finite tests do not establish unbounded safety.

### Assumptions

- The fictional document authorities, exact integer values, profiles and event dates are accepted as supplied. Threshold selection is explicitly source-linked in the model notes.

### Reasoning

- 1. The cited review-universe text defines finite scope, not aesthetic quality.
- 2. AP03 places beauty outside threshold predicates absent a separate criterion.

### Limits

- This concerns the named synthetic test events and the narrow stated assurance route, not certification of actual safety hardware.
- Formal targets encode reviewed rule selections; source authenticity and semantic fidelity remain outside kernel checking. Missing/invalid data are never silently promoted to valid observations.

### Result

Semantic state: **not_applicable**; argument status: **nonformal**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Label as an editorial opinion or define an assessment rubric.
