# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

[Semantic correspondence review](semantic-review.md)

Extraction inventory: 9 documents; 0 pending, partial or blocked. See [ingestion details](ingestion.json) and [coverage](coverage.md).

## C09-OK-01

### Exact report claim

`input/report.md#C09-OK-01`

> **C09-OK-01.** L01 satisfies the historical revision 1 delay demonstration; its maximum is 118 milliseconds, below the 120-millisecond limit.
> 
> Citations: sources/01-specification-v1.docx#[V1-02]; sources/04-test-runs.pdf#[P01].

### Verification question

Does the supplied historical record establish the bounded revision 1 delay demonstration for L01, with maximum 118 ms below the 120-ms limit?

### Source evidence

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-p-0001`

> [V1-01] SYNTHETIC H-7 SPECIFICATION, REVISION 1. This document concerns the fictional Heliostat H-7 demonstration controller. It is not an actual safety standard and supplies no real-world safety advice. Revision 1 applies to tests executed before 1 June 2033 unless an explicitly approved profile says otherwise. The finite demonstration concerns measured trip delay under stated laboratory conditions. It does not certify lifetime reliability, mechanical protection, network security, or population defect rates. A report should identify the proposition actually tested rather than replace it with an undefined claim that the whole design is safe. The table below defines exact synthetic limits for this bounded exercise.

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-q2aiztjx"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-p-0002`

> [V1-02] HISTORICAL ACCEPTANCE TABLE. The NORMAL temperature interval includes both endpoints. A missing authorized route outside that interval is not a zero threshold and does not imply a physical failure. Three repeated runs must be valid and belong to the same unit and profile. Values copied from another serial number do not complete a missing run. The supply condition belongs to applicability rather than to an independent exemption from other prerequisites.

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 2, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-q2aiztjx"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0002-c0001-p0001`

> NORMAL

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 1, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-q2aiztjx"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0002-c0002-p0001`

> 10 through 30 degrees Celsius inclusive

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 9, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 2, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-q2aiztjx"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0002-c0003-p0001`

> 120 milliseconds

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 3, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-q2aiztjx"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0002-c0004-p0001`

> 3 per unit

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 11, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 4, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-q2aiztjx"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0002-c0005-p0001`

> Both channels measured; 24 volts nominal

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 5, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-q2aiztjx"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-p-0023`

> [V1-03] IMPLICATION DIRECTION. Three valid NORMAL runs within the applicable limit are sufficient for the narrowly defined delay demonstration. They are not stated necessary for every conceivable alternative assurance method. Full release additionally requires current calibration, both sensor channels measured, closure of required fault injections, and an authorized release signature. Passing a delay subrequirement alone is therefore insufficient for full release. The specification intentionally distinguishes a sufficient route to one predicate from a conjunction of prerequisites for another predicate. An audit must not reverse an implication merely because its converse sounds plausible or because no alternative route is described in this packet.

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 23, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-q2aiztjx"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-p-0025`

> [V1-05] HISTORICAL L01 RECORD. Unit L01 was tested on 20 May 2033 at 20 degrees Celsius. Its three valid delays were 110, 115, and 118 milliseconds. Both channels were measured using instrument K1, which was current for that date. These observations establish the historical delay demonstration under the 120-millisecond threshold. No fault-injection closure or final release signature for L01 is supplied here. A later tighter rule does not retroactively change the applicable threshold unless an operative transition clause explicitly requires reassessment. Historical acceptance and present authorization should remain separate questions, even when a later report discusses them together.

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[5]", "paragraph_index_in_story": 25, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-q2aiztjx"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0001`

> [V2-01] SYNTHETIC H-7 SPECIFICATION, REVISION 2. Revision 2 takes effect at 00:00 on 1 June 2033 for newly executed tests. It supersedes revision 1 for that prospective scope. Historical tests retain their historical approved rules unless explicitly retested; no retroactive reassessment is required here. Test execution time determines the applicable revision, not report publication time, file modification time, or the order in which an auditor discovers files. Identical serial numbers may appear in different periods because a unit can be retested. Every conclusion must identify the actual event being judged rather than attach a timeless pass or fail label to a serial number.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

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
Coordinates: `{"kind": "pdf", "page": 1, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0001.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-2cguc1oa"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/05-calibration-and-authority.md](input/sources/05-calibration-and-authority.md) — `P02`

> [CAL01] Instrument K1 was calibrated through 23:59 on 30 June 2033 and was used for L01, N01, N02, E17, and C01 in the test packet. Instrument K2 expired at 23:59 on 1 June and was used for N03 on 3 June. K2 renewal is dated 5 June and contains no retrospective clause. Thus K1 has affirmative evidence of current calibration at the named runs, while K2 has affirmative evidence of expiry at its N03 use. A later renewal cannot be silently moved backward in time. The registry is complete for these instruments and dates, but it does not certify every instrument ever used by the fictional organization.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 48, "end_character": 651, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "f4d7b1be08d6dd13db756c34f068696ffe5ec31564ff09ac4b47a63db180e175", "artifact_directory": "extraction/D00007/attempt-ch9omgbm"}`.

### Rules

- Revision 1 governs May 20 historical execution, with NORMAL10..30 inclusive and 120-ms limit; the historical table also specifies both channels and nominal 24V.
- The maximum of the actual three integer delay values is compared with the applicable historical limit; this numeric result is distinct from complete release authorization.

### Assumptions

- Accept V1-05 as documentary evidence of historical acceptance; do not infer independently measured supply voltage from it.
- The selected revised report explicitly states a maximum of 118 ms below the 120-ms limit; it does not assert a 118-ms margin.

### Reasoning

- 1. P01/V1-05 record three valid L01 NORMAL observations at 20 degrees on May 20: 110, 115 and 118 ms, with both channels measured and K1 current. V1-05 expressly establishes the historical delay demonstration. V2-01 retains the historical rule for these tests.
- 2. The actual maximum is 118 ms; all three observations are below 120 ms. The arithmetic margin is 120 - 118 = 2 ms. The clarified report states this maximum and comparison unambiguously.
- 3. The historical-acceptance component is supported by the express source record. Its complete laboratory applicability is not independently reconstructed: the V1 table includes nominal 24V, but the packet supplies no separate raw supply-voltage log.
- 4. The theorem checks three observations, maximum, inequality and margin only. Its relation remains auxiliary for the grouped historical-acceptance claim; it does not assume the report conclusion to prove it and does not certify full release.

### Limits

- Support for historical acceptance is documentary and conditional on the supplied source record; the Lean result certifies only the encoded arithmetic.
- No separate raw supply-voltage log or historical L01 fault closure/final release is supplied. The arithmetic does not establish full release or real-world safety.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **auxiliary**.

### Formal evidence

- `Audit.claim01Arithmetic` in module `Audit` (auxiliary): `Audit.l01.length = 3 ∧ Audit.within Audit.l01 120 = true ∧ Audit.maximum Audit.l01 = 118 ∧ Audit.maximum Audit.l01 < 120 ∧ 120 - Audit.maximum Audit.l01 = 2`.
  [Model](models/Audit.lean) · [Executed check](checks/Target017.lean) · [Actual proof log](logs/target-017.log)

### Recommendation

Retain the clarified maximum and historical scope, with documentary acceptance and auxiliary arithmetic distinguished.

## C09-OK-02

### Exact report claim

`input/report.md#C09-OK-02`

> **C09-OK-02.** Revision 2 governs the N01 and N02 tests executed on 3 June.
> 
> Citations: sources/02-specification-v2.docx#[V2-01]; sources/04-test-runs.pdf#[P02].

### Verification question

Does revision 2 govern the actual N01 andN02 NORMAL tests executed on June 3 rather than their report date or earlier specification discovery?

### Source evidence

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0001`

> [V2-01] SYNTHETIC H-7 SPECIFICATION, REVISION 2. Revision 2 takes effect at 00:00 on 1 June 2033 for newly executed tests. It supersedes revision 1 for that prospective scope. Historical tests retain their historical approved rules unless explicitly retested; no retroactive reassessment is required here. Test execution time determines the applicable revision, not report publication time, file modification time, or the order in which an auditor discovers files. Identical serial numbers may appear in different periods because a unit can be retested. Every conclusion must identify the actual event being judged rather than attach a timeless pass or fail label to a serial number.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0026`

> [V2-06] REVIEW UNIVERSE. The named units are L01, N01, N02, N03, E17, and C01; X99 is an invalid demonstration trace. These cases do not constitute a random sample of a production population. No statistical inference about all manufactured controllers is supplied. A universal statement about the named valid runs can be refuted by one in-scope explicit run above its applicable threshold. A universal statement about all temperatures requires additional defined criteria and observations. Preserve successful bounded demonstrations while identifying unsupported extensions. Every name, signature, instrument, and event here is synthetic, so no conclusion should be mistaken for certification of a real product.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 26, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

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
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-2cguc1oa"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

### Rules

- V2-01 governs newly executed tests at/after June 1 00:00 and retains only earlier tests under historical rules.

### Assumptions

- Use the supplied synthetic H-7 evidence model, exact integer delay values and expressly stated execution/profile/validity fields. No real product certification or measurement-error allowance is inferred.
- Original DOCX bodies/tables and all PDF pages were inspected; source-to-model and civil-date conversions are recorded in model-notes.md and arithmetic-check.md.

### Reasoning

- 1. P02 identifies both N01/N02 executions as June 3, after the June 1 boundary.
- 2. The exact minute is unnecessary: every minute of June 3 (offsets 2880..4319) is after transition and maps to revision 2.
- 3. The conclusion applies to these named execution events, not timeless serial-number labels or all historic tests.

### Limits

- No June 3 precise minute is invented; this is an entire-day bound on a source date.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim02` in module `Audit` (supports): `∀ t : Int, 2880 ≤ t → t ≤ 4319 → Audit.revision t = 2`.
  [Model](models/Audit.lean) · [Executed check](checks/Target018.lean) · [Actual proof log](logs/target-018.log)

### Recommendation

Retain revision 2 for the specified June 3 events.

## C09-OK-03

### Exact report claim

`input/report.md#C09-OK-03`

> **C09-OK-03.** All three N01 valid delay runs satisfy the applicable 100-millisecond limit.
> 
> Citations: sources/02-specification-v2.docx#[V2-02]; sources/04-test-runs.pdf#[P02].

### Verification question

Do all three actual valid N01 NORMAL20-degree delay runs meet the applicable inclusive 100-ms revision 2 limit?

### Source evidence

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0001`

> [V2-01] SYNTHETIC H-7 SPECIFICATION, REVISION 2. Revision 2 takes effect at 00:00 on 1 June 2033 for newly executed tests. It supersedes revision 1 for that prospective scope. Historical tests retain their historical approved rules unless explicitly retested; no retroactive reassessment is required here. Test execution time determines the applicable revision, not report publication time, file modification time, or the order in which an auditor discovers files. Identical serial numbers may appear in different periods because a unit can be retested. Every conclusion must identify the actual event being judged rather than attach a timeless pass or fail label to a serial number.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0002`

> [V2-02] CURRENT ACCEPTANCE TABLE. Every endpoint in the stated intervals is inclusive. A valid NORMAL delay of 100 milliseconds satisfies the numeric limit; 101 does not. The COLD route additionally requires a current cold-fixture certificate. There is no supplied HOT route, and no route below zero degrees. A table row cannot be applied without checking the environment and profile. The limits in this synthetic exercise are exact integer comparisons; realistic measurement error models are outside scope. The absence of an error model must not be filled by an invented uncertainty discount or an assumed rounding allowance.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 2, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0001-p0001`

> NORMAL

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0002-p0001`

> 10 through 30 degrees Celsius

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 9, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0003-p0001`

> 100 milliseconds

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0004-p0001`

> 3 per unit

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 11, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0005-p0001`

> Both channels measured

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

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
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-2cguc1oa"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/06-applicability-and-open-items.md](input/sources/06-applicability-and-open-items.md) — `P02`

> [AP01] C01 is a COLD-profile unit tested at 5 degrees with a current cold-fixture certificate; its limit is 150 milliseconds. N01, N02, N03, and E17 were tested at 20 degrees under NORMAL. No valid HOT qualification or authorized threshold above 30 degrees is supplied. The packet therefore does not establish a claim of qualification across every temperature. This missing scope is not a measurement proving that all hot operation physically fails. An analyst should state the unsupported extension precisely rather than discard the bounded favorable evidence for C01 or N01.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 42, "end_character": 618, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "dec4280b23593ada8abc1e1648682a3f31385bd2a7146aed36688ab157b715dc", "artifact_directory": "extraction/D00008/attempt-ckwquukc"}`.

### Rules

- Revision 2 NORMAL10..30 has an inclusive 100-ms limit. Runs must be valid, distinct and tied to the same unit/profile.

### Assumptions

- Use the supplied synthetic H-7 evidence model, exact integer delay values and expressly stated execution/profile/validity fields. No real product certification or measurement-error allowance is inferred.
- Original DOCX bodies/tables and all PDF pages were inspected; source-to-model and civil-date conversions are recorded in model-notes.md and arithmetic-check.md.

### Reasoning

- 1. P02 supplies exactly three valid N01 observations 92,95,99, both channels at 20 degrees; AP01 confirmsNORMAL applicability.
- 2. Each value is at most 100 and maximum 99 is below 100. The list length is 3, so the result is nonvacuous and does not borrow N02 values.
- 3. The bounded all-three numeric claim is supported without inferring release from delay alone.

### Limits

- This is the named finite delay demonstration only; other release predicates have separate evidence.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim03` in module `Audit` (supports): `Audit.baseLimit 2 .normal 20 = some 100 ∧ Audit.n01.length = 3 ∧ Audit.within Audit.n01 100 = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target019.lean) · [Actual proof log](logs/target-019.log)

### Recommendation

Retain the successful finite N01 result and its unit/profile scope.

## C09-OK-04

### Exact report claim

`input/report.md#C09-OK-04`

> **C09-OK-04.** N02 has a concrete failing valid run of 101 milliseconds.
> 
> Citations: sources/04-test-runs.pdf#[P02]; sources/02-specification-v2.docx#[V2-02].

### Verification question

Is N02 third valid 101-ms run an explicit in-scope failure under its applicable 100-ms limit?

### Source evidence

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
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-2cguc1oa"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0002`

> [V2-02] CURRENT ACCEPTANCE TABLE. Every endpoint in the stated intervals is inclusive. A valid NORMAL delay of 100 milliseconds satisfies the numeric limit; 101 does not. The COLD route additionally requires a current cold-fixture certificate. There is no supplied HOT route, and no route below zero degrees. A table row cannot be applied without checking the environment and profile. The limits in this synthetic exercise are exact integer comparisons; realistic measurement error models are outside scope. The absence of an error model must not be filled by an invented uncertainty discount or an assumed rounding allowance.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 2, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0001-p0001`

> NORMAL

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0002-p0001`

> 10 through 30 degrees Celsius

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 9, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0003-p0001`

> 100 milliseconds

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0004-p0001`

> 3 per unit

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 11, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0005-p0001`

> Both channels measured

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0024`

> [V2-04] INCORPORATED EXCEPTION. Annex X changes the NORMAL delay threshold for one named serial number and a specific time interval. It changes no other requirement. In particular, it does not expand the temperature range, waive channel B measurement, make expired calibration current, close fault injections, or delegate release signing authority. The applicable general rule and exception must be combined before comparing observed delay. A general threshold alone is an incomplete rule set for a unit covered by an exception. Conversely, resemblance to the exempt unit does not extend an exception to other serial numbers or later dates.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 24, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0001`

> [X01] SYNTHETIC INCORPORATED ANNEX X. Requirements owner Mara Flint approved this exception under delegation AUTH-7 at 09:00 on 2 June 2033. It applies only to serial E17 for NORMAL tests executed from 09:00 on 2 June through 18:00 on 4 June inclusive. The maximum valid delay for those tests is 110 milliseconds rather than 100. The environment remains 10 through 30 degrees, and every other revision 2 prerequisite remains operative. The exception expressly does not apply to N02, even if N02 shares the same hardware build. The table records the operative scope rather than an illustrative example.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-e0u1_qb9"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0013`

> [X03] REQUEST HISTORY. The stated synthetic rationale is a demonstration fixture with an extra reporting stage. An informal proposal sought the same allowance for all units, but that proposal was rejected. Only the narrow E17 text became operative. A rationale explains a request; it does not enlarge approved scope. A forwarded subject line reading threshold allowance cannot substitute for the final signed body. No additional exception appears in the complete exception register for the named units during this interval. This bounded completeness helps reject a fabricated N02 exemption without claiming that no exception could ever exist in a different period.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 13, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-e0u1_qb9"}`.

- [input/sources/05-calibration-and-authority.md](input/sources/05-calibration-and-authority.md) — `P03`

> [AUTH01] Mara Flint holds the AUTH-7 requirements-exception delegation for E17. Operator Oren Vale can execute and record tests but cannot change thresholds or authorize release. Release owner Sera Moss signed release entries for N01, E17, and C01 after checking their listed fault closures. No release signature is supplied for N03. N02 has an explicit release denial because its valid third delay run exceeded the applicable limit. The release ledger is complete for these named units through 5 June. A signatory identity is not interchangeable with a different role, and an operator's favorable comment is not a release signature.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 653, "end_character": 1286, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "f4d7b1be08d6dd13db756c34f068696ffe5ec31564ff09ac4b47a63db180e175", "artifact_directory": "extraction/D00007/attempt-ch9omgbm"}`.

- [input/sources/07-fault-closure-register.md](input/sources/07-fault-closure-register.md) — `P05`

> [FC04] N02 and N03 disposition. N02's valid 101-millisecond run remains a failed delay requirement regardless of whether other administrative records are favorable. The release denial explicitly cites that run, and no closure statement in this register overrides it. N03 has no completed closure set in the supplied packet. The operator's worksheet has three empty closure slots marked pending. Those slots are missing assurance evidence; they do not describe observed physical behavior under the unperformed or undocumented injections. The audit should report the required argument that is absent without inventing an injection outcome or treating pending as a numerical failure measurement.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 1979, "end_character": 2671, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "832f5bc068a88b4ee4756897c1c5f36af0e6ba4e0f76e4581918223f338b1d3b", "artifact_directory": "extraction/D00009/attempt-fpox7ygf"}`.

### Rules

- A valid in-scope run exceeding its applicable inclusive limit is a direct counterexample to all-runs-passed. AnnexX does not apply toN02.

### Assumptions

- Use the supplied synthetic H-7 evidence model, exact integer delay values and expressly stated execution/profile/validity fields. No real product certification or measurement-error allowance is inferred.
- Original DOCX bodies/tables and all PDF pages were inspected; source-to-model and civil-date conversions are recorded in model-notes.md and arithmetic-check.md.

### Reasoning

- 1. P02 records N02 valid runs 90,97,101 atNORMAL20 degrees onJune 3 and explicitly identifies no exception.
- 2. The third run 101 exceeds 100 by 1 and belongs to the named valid N02 run set.
- 3. AUTH01/FC04 corroborate the release denial based on this run; signatures or favorable other records cannot overwrite it. The report correctly identifies an actual failing witness, not missing data.

### Limits

- This does not assert every N02 run failed or generalize to all production units.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim04` in module `Audit` (supports): `(101 : Nat) ∈ Audit.n02 ∧ 100 < (101 : Nat) ∧ Audit.within Audit.n02 100 = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target020.lean) · [Actual proof log](logs/target-020.log)

### Recommendation

Retain 101 as the concrete valid counterexample and distinguish it from N03 missing evidence.

## C09-OK-05

### Exact report claim

`input/report.md#C09-OK-05`

> **C09-OK-05.** E17 satisfies its applicable 110-millisecond exception limit for all three named runs.
> 
> Citations: sources/03-exception-annex.docx#[X01]; sources/04-test-runs.pdf#[P03].

### Verification question

Does E17 match AnnexX identity/profile/time scope and do its three valid runs meet the resulting 110-ms limit?

### Source evidence

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0001`

> [V2-01] SYNTHETIC H-7 SPECIFICATION, REVISION 2. Revision 2 takes effect at 00:00 on 1 June 2033 for newly executed tests. It supersedes revision 1 for that prospective scope. Historical tests retain their historical approved rules unless explicitly retested; no retroactive reassessment is required here. Test execution time determines the applicable revision, not report publication time, file modification time, or the order in which an auditor discovers files. Identical serial numbers may appear in different periods because a unit can be retested. Every conclusion must identify the actual event being judged rather than attach a timeless pass or fail label to a serial number.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0002`

> [V2-02] CURRENT ACCEPTANCE TABLE. Every endpoint in the stated intervals is inclusive. A valid NORMAL delay of 100 milliseconds satisfies the numeric limit; 101 does not. The COLD route additionally requires a current cold-fixture certificate. There is no supplied HOT route, and no route below zero degrees. A table row cannot be applied without checking the environment and profile. The limits in this synthetic exercise are exact integer comparisons; realistic measurement error models are outside scope. The absence of an error model must not be filled by an invented uncertainty discount or an assumed rounding allowance.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 2, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0001-p0001`

> NORMAL

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0002-p0001`

> 10 through 30 degrees Celsius

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 9, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0003-p0001`

> 100 milliseconds

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0004-p0001`

> 3 per unit

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 11, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0002-c0005-p0001`

> Both channels measured

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0024`

> [V2-04] INCORPORATED EXCEPTION. Annex X changes the NORMAL delay threshold for one named serial number and a specific time interval. It changes no other requirement. In particular, it does not expand the temperature range, waive channel B measurement, make expired calibration current, close fault injections, or delegate release signing authority. The applicable general rule and exception must be combined before comparing observed delay. A general threshold alone is an incomplete rule set for a unit covered by an exception. Conversely, resemblance to the exempt unit does not extend an exception to other serial numbers or later dates.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 24, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0001`

> [X01] SYNTHETIC INCORPORATED ANNEX X. Requirements owner Mara Flint approved this exception under delegation AUTH-7 at 09:00 on 2 June 2033. It applies only to serial E17 for NORMAL tests executed from 09:00 on 2 June through 18:00 on 4 June inclusive. The maximum valid delay for those tests is 110 milliseconds rather than 100. The environment remains 10 through 30 degrees, and every other revision 2 prerequisite remains operative. The exception expressly does not apply to N02, even if N02 shares the same hardware build. The table records the operative scope rather than an illustrative example.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-e0u1_qb9"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-table-0001-r0002-c0001-p0001`

> E17 only

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 7, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 1, "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-e0u1_qb9"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-table-0001-r0002-c0002-p0001`

> 2 June 2033 09:00

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 2, "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-e0u1_qb9"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-table-0001-r0002-c0003-p0001`

> 4 June 2033 18:00

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 9, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 3, "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-e0u1_qb9"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-table-0001-r0002-c0004-p0001`

> NORMAL 100 milliseconds

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 4, "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-e0u1_qb9"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-table-0001-r0002-c0005-p0001`

> NORMAL 110 milliseconds

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 11, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 5, "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-e0u1_qb9"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0012`

> [X02] AUTHORIZATION AND LIMITS. Mara holds authority to grant this bounded threshold change. Test operator Oren Vale does not possess that authority independently. The E17 runs on 3 June fall within the interval; a new test on 5 June would not. This annex cannot supply a missing channel measurement or a final release signature. The approval date, effective interval, and later report date are separate fields. An audit concluding that a 108-millisecond E17 run satisfies its requirement should cite both the general specification and this incorporated exception, including the identity and temporal match rather than merely quoting the larger number.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-e0u1_qb9"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0013`

> [X03] REQUEST HISTORY. The stated synthetic rationale is a demonstration fixture with an extra reporting stage. An informal proposal sought the same allowance for all units, but that proposal was rejected. Only the narrow E17 text became operative. A rationale explains a request; it does not enlarge approved scope. A forwarded subject line reading threshold allowance cannot substitute for the final signed body. No additional exception appears in the complete exception register for the named units during this interval. This bounded completeness helps reject a fabricated N02 exemption without claiming that no exception could ever exist in a different period.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 13, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-e0u1_qb9"}`.

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
Coordinates: `{"kind": "pdf", "page": 3, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0003.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-2cguc1oa"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/05-calibration-and-authority.md](input/sources/05-calibration-and-authority.md) — `P03`

> [AUTH01] Mara Flint holds the AUTH-7 requirements-exception delegation for E17. Operator Oren Vale can execute and record tests but cannot change thresholds or authorize release. Release owner Sera Moss signed release entries for N01, E17, and C01 after checking their listed fault closures. No release signature is supplied for N03. N02 has an explicit release denial because its valid third delay run exceeded the applicable limit. The release ledger is complete for these named units through 5 June. A signatory identity is not interchangeable with a different role, and an operator's favorable comment is not a release signature.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 653, "end_character": 1286, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "f4d7b1be08d6dd13db756c34f068696ffe5ec31564ff09ac4b47a63db180e175", "artifact_directory": "extraction/D00007/attempt-ch9omgbm"}`.

### Rules

- V2-04 incorporates the authorized bounded exception; X01 changes NORMAL threshold only forE17 from June 2 09:00 through June 4 18:00 inclusive. Other requirements remain.

### Assumptions

- Use the supplied synthetic H-7 evidence model, exact integer delay values and expressly stated execution/profile/validity fields. No real product certification or measurement-error allowance is inferred.
- Original DOCX bodies/tables and all PDF pages were inspected; source-to-model and civil-date conversions are recorded in model-notes.md and arithmetic-check.md.

### Reasoning

- 1. AUTH01/X01 establish Mara's exception authority and final narrowE17 scope, not the rejected general proposal. P03 identifies E17 NORMAL20-degree valid runs 104,108,106 onJune 3.
- 2. The entire June 3 day lies between exception offsets 1980 and 5400, so all actual but minute-unspecified runs receive 110 rather than 100.
- 3. All three values are at most 110 and maximum 108; the proof separately checks interval applicability and finite values.

### Limits

- The exception does not extend the environment or waive calibration/channels/fault closures/signature; no later test automatically inherits it.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.e17Applicable` in module `Audit` (supports): `∀ t : Int, 2880 ≤ t → t ≤ 4319 → Audit.limitAt .e17 .normal 20 t = some 110`.
  [Model](models/Audit.lean) · [Executed check](checks/Target021.lean) · [Actual proof log](logs/target-021.log)

- `Audit.claim05` in module `Audit` (supports): `Audit.e17.length = 3 ∧ Audit.within Audit.e17 110 = true ∧ Audit.maximum Audit.e17 = 108`.
  [Model](models/Audit.lean) · [Executed check](checks/Target022.lean) · [Actual proof log](logs/target-022.log)

### Recommendation

Retain the combined general-rule plus incorporated-exception reasoning and actual scope match.

## C09-OK-06

### Exact report claim

`input/report.md#C09-OK-06`

> **C09-OK-06.** The E17 exception does not apply to N02.
> 
> Citations: sources/03-exception-annex.docx#[X01].

### Verification question

Does the operativeE17 exception apply toN02 because of similar hardware or a wider rejected request?

### Source evidence

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0001`

> [X01] SYNTHETIC INCORPORATED ANNEX X. Requirements owner Mara Flint approved this exception under delegation AUTH-7 at 09:00 on 2 June 2033. It applies only to serial E17 for NORMAL tests executed from 09:00 on 2 June through 18:00 on 4 June inclusive. The maximum valid delay for those tests is 110 milliseconds rather than 100. The environment remains 10 through 30 degrees, and every other revision 2 prerequisite remains operative. The exception expressly does not apply to N02, even if N02 shares the same hardware build. The table records the operative scope rather than an illustrative example.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-e0u1_qb9"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0012`

> [X02] AUTHORIZATION AND LIMITS. Mara holds authority to grant this bounded threshold change. Test operator Oren Vale does not possess that authority independently. The E17 runs on 3 June fall within the interval; a new test on 5 June would not. This annex cannot supply a missing channel measurement or a final release signature. The approval date, effective interval, and later report date are separate fields. An audit concluding that a 108-millisecond E17 run satisfies its requirement should cite both the general specification and this incorporated exception, including the identity and temporal match rather than merely quoting the larger number.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-e0u1_qb9"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0013`

> [X03] REQUEST HISTORY. The stated synthetic rationale is a demonstration fixture with an extra reporting stage. An informal proposal sought the same allowance for all units, but that proposal was rejected. Only the narrow E17 text became operative. A rationale explains a request; it does not enlarge approved scope. A forwarded subject line reading threshold allowance cannot substitute for the final signed body. No additional exception appears in the complete exception register for the named units during this interval. This bounded completeness helps reject a fabricated N02 exemption without claiming that no exception could ever exist in a different period.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 13, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-e0u1_qb9"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0024`

> [V2-04] INCORPORATED EXCEPTION. Annex X changes the NORMAL delay threshold for one named serial number and a specific time interval. It changes no other requirement. In particular, it does not expand the temperature range, waive channel B measurement, make expired calibration current, close fault injections, or delegate release signing authority. The applicable general rule and exception must be combined before comparing observed delay. A general threshold alone is an incomplete rule set for a unit covered by an exception. Conversely, resemblance to the exempt unit does not extend an exception to other serial numbers or later dates.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 24, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/05-calibration-and-authority.md](input/sources/05-calibration-and-authority.md) — `P03`

> [AUTH01] Mara Flint holds the AUTH-7 requirements-exception delegation for E17. Operator Oren Vale can execute and record tests but cannot change thresholds or authorize release. Release owner Sera Moss signed release entries for N01, E17, and C01 after checking their listed fault closures. No release signature is supplied for N03. N02 has an explicit release denial because its valid third delay run exceeded the applicable limit. The release ledger is complete for these named units through 5 June. A signatory identity is not interchangeable with a different role, and an operator's favorable comment is not a release signature.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 653, "end_character": 1286, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "f4d7b1be08d6dd13db756c34f068696ffe5ec31564ff09ac4b47a63db180e175", "artifact_directory": "extraction/D00007/attempt-ch9omgbm"}`.

### Rules

- X01 expressly restricts serial toE17 and excludesN02; rationale, hardware similarity and rejected proposal do not enlarge approved scope.

### Assumptions

- Use the supplied synthetic H-7 evidence model, exact integer delay values and expressly stated execution/profile/validity fields. No real product certification or measurement-error allowance is inferred.
- Original DOCX bodies/tables and all PDF pages were inspected; source-to-model and civil-date conversions are recorded in model-notes.md and arithmetic-check.md.

### Reasoning

- 1. X01 namesE17 only and explicitly says the exception does not apply toN02. X03 records rejection of the all-unit proposal and no other exception for named units/interval.
- 2. The model checks serial membership before timing or numerical limit; forN02 this particular exception is false under every profile/time.
- 3. The report's nonapplicability statement is supported by explicit scope, not merely absence of a convenient attachment.

### Limits

- This rejects this incorporatedE17 exception forN02, not the possibility of different future approved rules outside the supplied scope.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim06` in module `Audit` (supports): `∀ p temp t, Audit.exceptionApplies .n02 p temp t = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target023.lean) · [Actual proof log](logs/target-023.log)

### Recommendation

RetainN02 exclusion and avoid extending approved scope from the request rationale.

## C09-OK-07

### Exact report claim

`input/report.md#C09-OK-07`

> **C09-OK-07.** C01 satisfies the COLD-profile 150-millisecond delay limit.
> 
> Citations: sources/02-specification-v2.docx#[V2-02]; sources/04-test-runs.pdf#[P04].

### Verification question

Does C01 match the revision 2 COLD0..9 profile, including its fixture prerequisite, and satisfy the 150-ms delay criterion?

### Source evidence

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0001`

> [V2-01] SYNTHETIC H-7 SPECIFICATION, REVISION 2. Revision 2 takes effect at 00:00 on 1 June 2033 for newly executed tests. It supersedes revision 1 for that prospective scope. Historical tests retain their historical approved rules unless explicitly retested; no retroactive reassessment is required here. Test execution time determines the applicable revision, not report publication time, file modification time, or the order in which an auditor discovers files. Identical serial numbers may appear in different periods because a unit can be retested. Every conclusion must identify the actual event being judged rather than attach a timeless pass or fail label to a serial number.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0002`

> [V2-02] CURRENT ACCEPTANCE TABLE. Every endpoint in the stated intervals is inclusive. A valid NORMAL delay of 100 milliseconds satisfies the numeric limit; 101 does not. The COLD route additionally requires a current cold-fixture certificate. There is no supplied HOT route, and no route below zero degrees. A table row cannot be applied without checking the environment and profile. The limits in this synthetic exercise are exact integer comparisons; realistic measurement error models are outside scope. The absence of an error model must not be filled by an invented uncertainty discount or an assumed rounding allowance.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 2, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0001-p0001`

> COLD

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 13, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0002-p0001`

> 0 through 9 degrees Celsius

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0003-p0001`

> 150 milliseconds

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 15, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0004-p0001`

> 3 per unit

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 16, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0003-c0005-p0001`

> Both channels measured and cold-fixture certificate

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[3]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 17, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 3, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

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
Coordinates: `{"kind": "pdf", "page": 4, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0004.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-2cguc1oa"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/06-applicability-and-open-items.md](input/sources/06-applicability-and-open-items.md) — `P02`

> [AP01] C01 is a COLD-profile unit tested at 5 degrees with a current cold-fixture certificate; its limit is 150 milliseconds. N01, N02, N03, and E17 were tested at 20 degrees under NORMAL. No valid HOT qualification or authorized threshold above 30 degrees is supplied. The packet therefore does not establish a claim of qualification across every temperature. This missing scope is not a measurement proving that all hot operation physically fails. An analyst should state the unsupported extension precisely rather than discard the bounded favorable evidence for C01 or N01.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 42, "end_character": 618, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "dec4280b23593ada8abc1e1648682a3f31385bd2a7146aed36688ab157b715dc", "artifact_directory": "extraction/D00008/attempt-ckwquukc"}`.

- [input/sources/05-calibration-and-authority.md](input/sources/05-calibration-and-authority.md) — `P02`

> [CAL01] Instrument K1 was calibrated through 23:59 on 30 June 2033 and was used for L01, N01, N02, E17, and C01 in the test packet. Instrument K2 expired at 23:59 on 1 June and was used for N03 on 3 June. K2 renewal is dated 5 June and contains no retrospective clause. Thus K1 has affirmative evidence of current calibration at the named runs, while K2 has affirmative evidence of expiry at its N03 use. A later renewal cannot be silently moved backward in time. The registry is complete for these instruments and dates, but it does not certify every instrument ever used by the fictional organization.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 48, "end_character": 651, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "f4d7b1be08d6dd13db756c34f068696ffe5ec31564ff09ac4b47a63db180e175", "artifact_directory": "extraction/D00007/attempt-ch9omgbm"}`.

### Rules

- The COLD row has inclusive 0..9 range,150-ms limit, three valid runs, both channels and current cold-fixture certificate; NORMAL100 must not be substituted.

### Assumptions

- Use the supplied synthetic H-7 evidence model, exact integer delay values and expressly stated execution/profile/validity fields. No real product certification or measurement-error allowance is inferred.
- Original DOCX bodies/tables and all PDF pages were inspected; source-to-model and civil-date conversions are recorded in model-notes.md and arithmetic-check.md.

### Reasoning

- 1. P04/AP01 identify C01 COLD5 degrees onJune 3, current cold-fixture certificate, both channels and three valid observations 142,145,149 withK1.
- 2. Five degrees is within the applicableCOLD interval. All three values are at most 150; max 149 is below the inclusive limit.
- 3. The report correctly preserves the profile-specific bounded success. Separate fault/release records exist but are not needed to change the delay comparison.

### Limits

- The theorem compares the named profile/data under source-certified fixture conditions; it does not invent aHOT route or extrapolate across temperatures.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim07` in module `Audit` (supports): `Audit.baseLimit 2 .cold 5 = some 150 ∧ Audit.c01.length = 3 ∧ Audit.within Audit.c01 150 = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target024.lean) · [Actual proof log](logs/target-024.log)

### Recommendation

Retain 150-msCOLD assessment with the current fixture evidence.

## C09-OK-08

### Exact report claim

`input/report.md#C09-OK-08`

> **C09-OK-08.** N03 lacks channel B measurement and a third valid repeated run.
> 
> Citations: sources/06-applicability-and-open-items.md#[AP02]; sources/04-test-runs.pdf#[P05].

### Verification question

Does the supplied N03 evidence lack channelB measurement and a third valid repeated run, rather than supply a zero or a borrowed successful trace?

### Source evidence

- [input/sources/06-applicability-and-open-items.md](input/sources/06-applicability-and-open-items.md) — `P03`

> [AP02] N03 lacks channel B measurement and a third valid repeated run. Its second attempted trace aborted before acquisition and has no delay value. X99 has a raw 85-millisecond number but is explicitly invalid because synchronization was lost. It cannot contribute to N03 or any other unit's valid-run count. The correct support-gap finding identifies the exact missing channel and repetition, relevant requirement, and unavailable evidence. It does not predict what the unmeasured channel would have done. Invalid, missing, and explicitly failing measurements have different meanings and must remain distinguishable in the report.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 620, "end_character": 1252, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "dec4280b23593ada8abc1e1648682a3f31385bd2a7146aed36688ab157b715dc", "artifact_directory": "extraction/D00008/attempt-ckwquukc"}`.

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
Coordinates: `{"kind": "pdf", "page": 5, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0005.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-2cguc1oa"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-p-0024`

> [V1-04] DATA HANDLING. A run aborted before acquisition supplies no delay measurement. A blank cell means unavailable evidence unless a signed explanatory note explicitly gives another meaning. It is not zero. An operator may invalidate a trace after discovering synchronization loss; the invalidation accompanies the printed value. Each extraction should retain unit identity, run date, profile, environment, validity, instrument, measured channels, and observed value. Comparing a column of numbers without those fields can apply the wrong revision or count invalid evidence. Missing measurements should be reported as concrete support gaps, not silently replaced by favorable numbers from a neighboring row.

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 24, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-q2aiztjx"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0023`

> [V2-03] RELEASE CONJUNCTION. The specified release route requires an applicable delay demonstration, current calibration at every contributing run, both sensor channels measured, closure of the required fault injections, and an authorized release signature. Each conjunct is necessary under this route. Their conjunction is sufficient only within the finite H-7 demonstration scope. A signature does not overwrite an explicit failed run. A favorable channel A result cannot establish an absent channel B result. An explicit recorded failure supplies a counterexample to a claim that all requirements passed; a missing measurement instead leaves a required argument unsupported. These evidentiary situations should not be collapsed into one generic negative verdict.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 23, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0025`

> [V2-05] VALIDITY AND TIME. A recorded clock synchronization failure invalidates the affected trace even if its printed delay is small. Repeated runs belong to their named unit and profile. Calibration is current only when the run timestamp is on or before the stated expiry instant. A renewal after a run is not retrospective unless an authorized statement explicitly says it is. The packet contains no such retrospective calibration statement. The analyst must distinguish an absent certificate from a certificate affirmatively showing expiry. Both may prevent an assurance argument, but only the latter supplies direct contrary evidence about calibration at the specific instant.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[5]", "paragraph_index_in_story": 25, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0014`

> [X04] ALTERNATIVE METHODS. The three-run route is sufficient for its bounded delay demonstration, not stated necessary for every possible assurance method. No alternative qualification argument is supplied for N03. Therefore this packet cannot establish N03 through an unspecified alternative, while it also does not prove that every conceivable alternative is impossible. The reviewer should identify the missing necessity argument in a claim that the listed route is universally mandatory. Absence of an alternative in a finite packet is not a formal counterexample to such necessity; it simply leaves that broader assertion unproved. The distinction between refutation and unsupported generalization is intentional.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-e0u1_qb9"}`.

- [input/sources/07-fault-closure-register.md](input/sources/07-fault-closure-register.md) — `P05`

> [FC04] N02 and N03 disposition. N02's valid 101-millisecond run remains a failed delay requirement regardless of whether other administrative records are favorable. The release denial explicitly cites that run, and no closure statement in this register overrides it. N03 has no completed closure set in the supplied packet. The operator's worksheet has three empty closure slots marked pending. Those slots are missing assurance evidence; they do not describe observed physical behavior under the unperformed or undocumented injections. The audit should report the required argument that is absent without inventing an injection outcome or treating pending as a numerical failure measurement.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 1979, "end_character": 2671, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "832f5bc068a88b4ee4756897c1c5f36af0e6ba4e0f76e4581918223f338b1d3b", "artifact_directory": "extraction/D00009/attempt-fpox7ygf"}`.

### Rules

- Blank/aborted/absent are unavailable measurements, not zero. Runs must belong to the named unit/profile; a missing release premise is a support gap, not an observed numeric failure.

### Assumptions

- The theorem models supplied measurement availability, not the historical impossibility of a measurement existing elsewhere.

### Reasoning

- 1. P05/AP02 provide one valid N03 trace 94, a second attempt aborted before acquisition, an absent third run and no channelB measurement.
- 2. X99 cannot fill the gap because it is invalid; neither copying another unit nor assuming a zero is authorized.
- 3. The formal evidence-state model preserves secondaborted and thirdabsent separately and proves no valid third measurement is supplied. The report's exact missing-evidence statement is supported.

### Limits

- No prediction of unmeasured channelB behavior, third-run delay or physical failure is justified. Additional missing calibration/closure/signature premises remain separate.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim08` in module `Audit` (supports): `Audit.n03ChannelBAvailable = false ∧ Audit.n03Second = .aborted ∧ Audit.n03Third = .absent ∧ Audit.validMeasurement Audit.n03Third = none`.
  [Model](models/Audit.lean) · [Executed check](checks/Target025.lean) · [Actual proof log](logs/target-025.log)

### Recommendation

Retain the named channel/repetition gaps without assigning favorable numbers.

## C09-OK-09

### Exact report claim

`input/report.md#C09-OK-09`

> **C09-OK-09.** K2 was expired when used for N03 on 3 June.
> 
> Citations: sources/05-calibration-and-authority.md#[CAL01]; sources/04-test-runs.pdf#[P05].

### Verification question

Was K2 affirmatively expired during N03 June 3 execution despite its later June 5 renewal?

### Source evidence

- [input/sources/05-calibration-and-authority.md](input/sources/05-calibration-and-authority.md) — `P02`

> [CAL01] Instrument K1 was calibrated through 23:59 on 30 June 2033 and was used for L01, N01, N02, E17, and C01 in the test packet. Instrument K2 expired at 23:59 on 1 June and was used for N03 on 3 June. K2 renewal is dated 5 June and contains no retrospective clause. Thus K1 has affirmative evidence of current calibration at the named runs, while K2 has affirmative evidence of expiry at its N03 use. A later renewal cannot be silently moved backward in time. The registry is complete for these instruments and dates, but it does not certify every instrument ever used by the fictional organization.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 48, "end_character": 651, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "f4d7b1be08d6dd13db756c34f068696ffe5ec31564ff09ac4b47a63db180e175", "artifact_directory": "extraction/D00007/attempt-ch9omgbm"}`.

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
Coordinates: `{"kind": "pdf", "page": 5, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0005.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-2cguc1oa"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0025`

> [V2-05] VALIDITY AND TIME. A recorded clock synchronization failure invalidates the affected trace even if its printed delay is small. Repeated runs belong to their named unit and profile. Calibration is current only when the run timestamp is on or before the stated expiry instant. A renewal after a run is not retrospective unless an authorized statement explicitly says it is. The packet contains no such retrospective calibration statement. The analyst must distinguish an absent certificate from a certificate affirmatively showing expiry. Both may prevent an assurance argument, but only the latter supplies direct contrary evidence about calibration at the specific instant.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[5]", "paragraph_index_in_story": 25, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

### Rules

- V2-05 requires the run on/before expiry and excludes retrospective renewal without explicit authority; CAL01 supplies exact expiry and no retrospective clause.

### Assumptions

- Use the supplied synthetic H-7 evidence model, exact integer delay values and expressly stated execution/profile/validity fields. No real product certification or measurement-error allowance is inferred.
- Original DOCX bodies/tables and all PDF pages were inspected; source-to-model and civil-date conversions are recorded in model-notes.md and arithmetic-check.md.

### Reasoning

- 1. CAL01 states K2 expiry atJune 1 23:59 (offset 1439), use forN03 June 3, and renewalJune 5.
- 2. Every possible June 3 minute is at least 2880, strictly after 1439. Thus expired calibration is positively established at the run date, without inventing its exact time.
- 3. This is stronger than an absent certificate: the supplied certificate timing contradicts current calibration. Later renewal does not repair the historical condition.

### Limits

- This proves calibration expiry forK2 at the named use, not that the measured 94-ms trace numerically failed or that all instruments were expired.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim09` in module `Audit` (supports): `∀ t : Int, 2880 ≤ t → t ≤ 4319 → (1439 : Int) < t`.
  [Model](models/Audit.lean) · [Executed check](checks/Target026.lean) · [Actual proof log](logs/target-026.log)

### Recommendation

Retain affirmative expiry and separate it from missing-measurement findings.

## C09-OK-10

### Exact report claim

`input/report.md#C09-OK-10`

> **C09-OK-10.** X99 cannot count as a valid repeated run because synchronization was lost.
> 
> Citations: sources/06-applicability-and-open-items.md#[AP02]; sources/04-test-runs.pdf#[P05].

### Verification question

Can X99 printed 85-ms value count as a valid repeated run despite explicit lost synchronization?

### Source evidence

- [input/sources/06-applicability-and-open-items.md](input/sources/06-applicability-and-open-items.md) — `P03`

> [AP02] N03 lacks channel B measurement and a third valid repeated run. Its second attempted trace aborted before acquisition and has no delay value. X99 has a raw 85-millisecond number but is explicitly invalid because synchronization was lost. It cannot contribute to N03 or any other unit's valid-run count. The correct support-gap finding identifies the exact missing channel and repetition, relevant requirement, and unavailable evidence. It does not predict what the unmeasured channel would have done. Invalid, missing, and explicitly failing measurements have different meanings and must remain distinguishable in the report.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 620, "end_character": 1252, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "dec4280b23593ada8abc1e1648682a3f31385bd2a7146aed36688ab157b715dc", "artifact_directory": "extraction/D00008/attempt-ckwquukc"}`.

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
Coordinates: `{"kind": "pdf", "page": 5, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0005.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-2cguc1oa"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0025`

> [V2-05] VALIDITY AND TIME. A recorded clock synchronization failure invalidates the affected trace even if its printed delay is small. Repeated runs belong to their named unit and profile. Calibration is current only when the run timestamp is on or before the stated expiry instant. A renewal after a run is not retrospective unless an authorized statement explicitly says it is. The packet contains no such retrospective calibration statement. The analyst must distinguish an absent certificate from a certificate affirmatively showing expiry. Both may prevent an assurance argument, but only the latter supplies direct contrary evidence about calibration at the specific instant.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[5]", "paragraph_index_in_story": 25, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-p-0024`

> [V1-04] DATA HANDLING. A run aborted before acquisition supplies no delay measurement. A blank cell means unavailable evidence unless a signed explanatory note explicitly gives another meaning. It is not zero. An operator may invalidate a trace after discovering synchronization loss; the invalidation accompanies the printed value. Each extraction should retain unit identity, run date, profile, environment, validity, instrument, measured channels, and observed value. Comparing a column of numbers without those fields can apply the wrong revision or count invalid evidence. Missing measurements should be reported as concrete support gaps, not silently replaced by favorable numbers from a neighboring row.

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 24, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-q2aiztjx"}`.

### Rules

- Synchronization failure invalidates the affected trace regardless of a favorable printed number; invalid traces cannot satisfy the valid-run count.

### Assumptions

- Use the supplied synthetic H-7 evidence model, exact integer delay values and expressly stated execution/profile/validity fields. No real product certification or measurement-error allowance is inferred.
- Original DOCX bodies/tables and all PDF pages were inspected; source-to-model and civil-date conversions are recorded in model-notes.md and arithmetic-check.md.

### Reasoning

- 1. P05/AP02 explicitly labelX99 invalid after synchronization loss while preserving the raw 85 value.
- 2. The model retains 85 in an invalid constructor and maps it to no valid measurement, rather than deleting the adverse validity field or replacing missingN03 evidence.
- 3. The report correctly states exclusion from valid repeated-run evidence.

### Limits

- Trace invalidity is not an observed above-threshold delay and does not quantify actual unobserved behavior.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim10` in module `Audit` (supports): `Audit.x99 = .invalid 85 ∧ Audit.validMeasurement Audit.x99 = none`.
  [Model](models/Audit.lean) · [Executed check](checks/Target027.lean) · [Actual proof log](logs/target-027.log)

### Recommendation

Retain the 85-ms raw value with its invalidation attached; do not count it as a successful run.

## C09-OK-11

### Exact report claim

`input/report.md#C09-OK-11`

> **C09-OK-11.** A passed delay demonstration alone is insufficient for release under revision 2.
> 
> Citations: sources/02-specification-v2.docx#[V2-03].

### Verification question

Does passing the bounded delay demonstration alone suffice for the revision 2 specified release route?

### Source evidence

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0023`

> [V2-03] RELEASE CONJUNCTION. The specified release route requires an applicable delay demonstration, current calibration at every contributing run, both sensor channels measured, closure of the required fault injections, and an authorized release signature. Each conjunct is necessary under this route. Their conjunction is sufficient only within the finite H-7 demonstration scope. A signature does not overwrite an explicit failed run. A favorable channel A result cannot establish an absent channel B result. An explicit recorded failure supplies a counterexample to a claim that all requirements passed; a missing measurement instead leaves a required argument unsupported. These evidentiary situations should not be collapsed into one generic negative verdict.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 23, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0024`

> [V2-04] INCORPORATED EXCEPTION. Annex X changes the NORMAL delay threshold for one named serial number and a specific time interval. It changes no other requirement. In particular, it does not expand the temperature range, waive channel B measurement, make expired calibration current, close fault injections, or delegate release signing authority. The applicable general rule and exception must be combined before comparing observed delay. A general threshold alone is an incomplete rule set for a unit covered by an exception. Conversely, resemblance to the exempt unit does not extend an exception to other serial numbers or later dates.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 24, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/07-fault-closure-register.md](input/sources/07-fault-closure-register.md) — `P02`

> [FC01] Scope of the closure records. The required demonstration fault set contains three named injections: simulated stuck channel A, simulated stuck channel B, and loss of the synthetic telemetry heartbeat. These are invented administrative test labels, not instructions for testing or deploying actual hardware. A closure entry means the named required exercise was performed and its stipulated acceptance record was signed. It does not add a new measured trip-delay run. A unit may therefore have a complete delay demonstration while still lacking fault closure, or possess fault closure while an independent delay run fails. The register keeps these predicates separate.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 46, "end_character": 720, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "832f5bc068a88b4ee4756897c1c5f36af0e6ba4e0f76e4581918223f338b1d3b", "artifact_directory": "extraction/D00009/attempt-fpox7ygf"}`.

- [input/sources/05-calibration-and-authority.md](input/sources/05-calibration-and-authority.md) — `P03`

> [AUTH01] Mara Flint holds the AUTH-7 requirements-exception delegation for E17. Operator Oren Vale can execute and record tests but cannot change thresholds or authorize release. Release owner Sera Moss signed release entries for N01, E17, and C01 after checking their listed fault closures. No release signature is supplied for N03. N02 has an explicit release denial because its valid third delay run exceeded the applicable limit. The release ledger is complete for these named units through 5 June. A signatory identity is not interchangeable with a different role, and an operator's favorable comment is not a release signature.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 653, "end_character": 1286, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "f4d7b1be08d6dd13db756c34f068696ffe5ec31564ff09ac4b47a63db180e175", "artifact_directory": "extraction/D00007/attempt-ch9omgbm"}`.

### Rules

- V2-03 makes release-route satisfaction a conjunction of applicable delay, current calibration, both channels, required fault closures and authorized signature; each is necessary under that route.

### Assumptions

- Use the supplied synthetic H-7 evidence model, exact integer delay values and expressly stated execution/profile/validity fields. No real product certification or measurement-error allowance is inferred.
- Original DOCX bodies/tables and all PDF pages were inspected; source-to-model and civil-date conversions are recorded in model-notes.md and arithmetic-check.md.

### Reasoning

- 1. The policy explicitly requires additional independent predicates beyond delay. FC01 explains why fault closure is not another delay value and cannot be inferred from one.
- 2. A model with delay=true but calibration=false has releaseRoute=false even if the other three conjuncts hold. Therefore delay alone does not entail this route's release.
- 3. This directly supports the report's logical insufficiency statement without declaring a particular named unit actually uncalibrated from its delay result alone.

### Limits

- The theorem concerns the specified finite conjunction, not universal real-world assurance routes or an actual countermodel history for a chosen unit.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim11` in module `Audit` (supports): `Audit.releaseRoute true false true true true = false ∧ ¬ (∀ calibration channels faults signature, Audit.releaseRoute true calibration channels faults signature = true)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target028.lean) · [Actual proof log](logs/target-028.log)

### Recommendation

Retain the prerequisite separation and require independent evidence for every release conjunct.

## C09-OK-12

### Exact report claim

`input/report.md#C09-OK-12`

> **C09-OK-12.** The listed three-run route is sufficient for the bounded delay demonstration, not stated necessary for every conceivable method.
> 
> Citations: sources/01-specification-v1.docx#[V1-03]; sources/03-exception-annex.docx#[X04].

### Verification question

Do the sources state the listed route as sufficient for bounded delay demonstration while withholding a universal necessity claim over all conceivable methods?

### Source evidence

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-p-0023`

> [V1-03] IMPLICATION DIRECTION. Three valid NORMAL runs within the applicable limit are sufficient for the narrowly defined delay demonstration. They are not stated necessary for every conceivable alternative assurance method. Full release additionally requires current calibration, both sensor channels measured, closure of required fault injections, and an authorized release signature. Passing a delay subrequirement alone is therefore insufficient for full release. The specification intentionally distinguishes a sufficient route to one predicate from a conjunction of prerequisites for another predicate. An audit must not reverse an implication merely because its converse sounds plausible or because no alternative route is described in this packet.

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 23, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-q2aiztjx"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0014`

> [X04] ALTERNATIVE METHODS. The three-run route is sufficient for its bounded delay demonstration, not stated necessary for every possible assurance method. No alternative qualification argument is supplied for N03. Therefore this packet cannot establish N03 through an unspecified alternative, while it also does not prove that every conceivable alternative is impossible. The reviewer should identify the missing necessity argument in a claim that the listed route is universally mandatory. Absence of an alternative in a finite packet is not a formal counterexample to such necessity; it simply leaves that broader assertion unproved. The distinction between refutation and unsupported generalization is intentional.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-e0u1_qb9"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0023`

> [V2-03] RELEASE CONJUNCTION. The specified release route requires an applicable delay demonstration, current calibration at every contributing run, both sensor channels measured, closure of the required fault injections, and an authorized release signature. Each conjunct is necessary under this route. Their conjunction is sufficient only within the finite H-7 demonstration scope. A signature does not overwrite an explicit failed run. A favorable channel A result cannot establish an absent channel B result. An explicit recorded failure supplies a counterexample to a claim that all requirements passed; a missing measurement instead leaves a required argument unsupported. These evidentiary situations should not be collapsed into one generic negative verdict.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 23, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/06-applicability-and-open-items.md](input/sources/06-applicability-and-open-items.md) — `P04`

> [AP03] The packet provides no argument about population defect rates, lifetime reliability, network threats, mechanical strength, or an unrestricted meaning of safe. The finite release conjunction is narrower than universal design safety. Aesthetic opinions about the clarity or beauty of a specification are likewise outside the threshold predicates unless a separate criterion is supplied. The exercise is a reasoning fixture using invented documents, not guidance for deploying a real safety system. Favorable arithmetic and complete signatures can support the specified synthetic release route without supporting unbounded real-world conclusions.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1254, "end_character": 1904, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "dec4280b23593ada8abc1e1648682a3f31385bd2a7146aed36688ab157b715dc", "artifact_directory": "extraction/D00008/attempt-ckwquukc"}`.

### Rules

- Preserve the direction Route implies Demonstration; its converse does not follow. Missing alternative evidence does not establish universal impossibility or supply an actual alternative method.

### Assumptions

- Propositional assignments illustrate implication direction and are not additional real test evidence.

### Reasoning

- 1. V1-03/X04 expressly characterize the three-run route as sufficient and not stated necessary for every possible method.
- 2. The conditional theorem formalizes the supplied implication. A propositional counterassignment Route=false, Demonstration=true satisfies that implication and falsifies the converse. This shows non-entailment only.
- 3. X04 separately states no alternative argument is supplied forN03. The report correctly avoids promoting that absence into a universal necessity theorem or claiming a usable alternative exists.

### Limits

- No actual alternative qualification method is supplied or certified. The counterassignment is logical, not a claim thatN03 has an alternative demonstration.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **auxiliary**.

### Formal evidence

- `Audit.sufficientRoute` in module `Audit` (auxiliary): `∀ (Route Demonstration : Prop), (Route → Demonstration) → Route → Demonstration`.
  [Model](models/Audit.lean) · [Executed check](checks/Target029.lean) · [Actual proof log](logs/target-029.log)

- `Audit.converseNotEntailed` in module `Audit` (auxiliary): `(False → True) ∧ ¬ (True → False)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target030.lean) · [Actual proof log](logs/target-030.log)

### Recommendation

Retain the distinction between sufficient route, absent alternative argument and unproved universal necessity.

## C09-OK-13

### Exact report claim

`input/report.md#C09-OK-13`

> **C09-OK-13.** N01, E17, and C01 have authorized release signatures in the supplied ledger.
> 
> Citations: sources/05-calibration-and-authority.md#[AUTH01].

### Verification question

Does the supplied ledger contain authorized release-owner signatures for exactly the claimed N01,E17,C01 entries?

### Source evidence

- [input/sources/05-calibration-and-authority.md](input/sources/05-calibration-and-authority.md) — `P03`

> [AUTH01] Mara Flint holds the AUTH-7 requirements-exception delegation for E17. Operator Oren Vale can execute and record tests but cannot change thresholds or authorize release. Release owner Sera Moss signed release entries for N01, E17, and C01 after checking their listed fault closures. No release signature is supplied for N03. N02 has an explicit release denial because its valid third delay run exceeded the applicable limit. The release ledger is complete for these named units through 5 June. A signatory identity is not interchangeable with a different role, and an operator's favorable comment is not a release signature.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 653, "end_character": 1286, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "f4d7b1be08d6dd13db756c34f068696ffe5ec31564ff09ac4b47a63db180e175", "artifact_directory": "extraction/D00007/attempt-ch9omgbm"}`.

- [input/sources/05-calibration-and-authority.md](input/sources/05-calibration-and-authority.md) — `P04`

> [AUTH02] The specifications and incorporated annex are native DOCX sources. Their tables must remain attached to the correct revision and profile context during extraction. The native PDF supplies grouped test records, including invalidity and missing-data notes. An extracted numeral is not an independent measurement record. Stable markers identify original passages; derived chunk identifiers are optional navigation aids. All signatories and administrative acts are fictional, and this exercise assumes the supplied signature-role statements rather than claiming real cryptographic authentication. Source hashes identify exact bytes, not institutional truth beyond the stated evidence model.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1288, "end_character": 1983, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "f4d7b1be08d6dd13db756c34f068696ffe5ec31564ff09ac4b47a63db180e175", "artifact_directory": "extraction/D00007/attempt-ch9omgbm"}`.

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
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-2cguc1oa"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

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
Coordinates: `{"kind": "pdf", "page": 3, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0003.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-2cguc1oa"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

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
Coordinates: `{"kind": "pdf", "page": 4, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0004.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00006.pdf", "original_sha256": "44640ce83d9f9b0c669a9d39eb8992d550a5250e75383c8ad15dfe19abb4dd4e", "artifact_directory": "extraction/D00006/attempt-2cguc1oa"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/07-fault-closure-register.md](input/sources/07-fault-closure-register.md) — `P03`

> [FC02] N01 closure. Operator Oren recorded all three required N01 injections after the delay runs on 3 June. Reviewer Sera checked that each closure named N01 and the same configuration used in its valid delay demonstration. All three closure entries were signed before Sera issued the final release. The registry marks the N01 closure set complete. It does not borrow an E17 or C01 result, and it does not infer closure from a low delay value. This provides documentary support for one additional release conjunct beyond N01's three valid observations of 92, 95, and 99 milliseconds.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 722, "end_character": 1306, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "832f5bc068a88b4ee4756897c1c5f36af0e6ba4e0f76e4581918223f338b1d3b", "artifact_directory": "extraction/D00009/attempt-fpox7ygf"}`.

- [input/sources/07-fault-closure-register.md](input/sources/07-fault-closure-register.md) — `P04`

> [FC03] E17 and C01 closure. The E17 closure set names the temporary fixture configuration covered by Annex X and contains all three signed injections. The annex changes only the delay threshold, so those closure records remained necessary under the supplied route. C01 likewise has all three signed closures with the cold-fixture identifier carried through the records. Sera reviewed both sets before their respective release signatures. A cold-fixture certificate establishes an applicability prerequisite, not automatic completion of the injections. The register supplies the separate completion evidence and preserves the serial number attached to every closure set.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1308, "end_character": 1977, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "832f5bc068a88b4ee4756897c1c5f36af0e6ba4e0f76e4581918223f338b1d3b", "artifact_directory": "extraction/D00009/attempt-fpox7ygf"}`.

### Rules

- Release signing authority belongs to Sera, distinct from Oren's test-operation role and Mara's exception authority. Signature inventory is distinct from every release prerequisite.

### Assumptions

- Assume the supplied fictional signature-role statements as instructed byAUTH02; no external identity verification is claimed.

### Reasoning

- 1. AUTH01 explicitly states Sera signed release entries forN01,E17,C01 after checking listed closures; the PDF andFC02/FC03 corroborate their named contexts.
- 2. The finite ledger model contains the three unit/Sera pairs and the release role is authorized.
- 3. The report's scoped signature assertion is supported; no operator favorable comment or wrong unit's closure is substituted.

### Limits

- This is documentary role/signature evidence within the invented exercise, not real cryptographic authentication or permission to overwrite an explicit failed run.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim13` in module `Audit` (supports): `(Audit.Serial.n01, Audit.Signer.sera) ∈ Audit.releaseSignatures ∧ (Audit.Serial.e17, Audit.Signer.sera) ∈ Audit.releaseSignatures ∧ (Audit.Serial.c01, Audit.Signer.sera) ∈ Audit.releaseSignatures ∧ Audit.authorizedReleaseSigner .sera = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target031.lean) · [Actual proof log](logs/target-031.log)

### Recommendation

Retain the three named authorized signature entries and their distinct role.

## C09-OK-14

### Exact report claim

`input/report.md#C09-OK-14`

> **C09-OK-14.** The packet supplies no HOT-profile qualification route.
> 
> Citations: sources/06-applicability-and-open-items.md#[AP01]; sources/02-specification-v2.docx#[V2-02].

### Verification question

Do the supplied applicable tables and open-items source provide any HOT-profile qualification route above 30 degrees?

### Source evidence

- [input/sources/06-applicability-and-open-items.md](input/sources/06-applicability-and-open-items.md) — `P02`

> [AP01] C01 is a COLD-profile unit tested at 5 degrees with a current cold-fixture certificate; its limit is 150 milliseconds. N01, N02, N03, and E17 were tested at 20 degrees under NORMAL. No valid HOT qualification or authorized threshold above 30 degrees is supplied. The packet therefore does not establish a claim of qualification across every temperature. This missing scope is not a measurement proving that all hot operation physically fails. An analyst should state the unsupported extension precisely rather than discard the bounded favorable evidence for C01 or N01.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 42, "end_character": 618, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "dec4280b23593ada8abc1e1648682a3f31385bd2a7146aed36688ab157b715dc", "artifact_directory": "extraction/D00008/attempt-ckwquukc"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-p-0002`

> [V1-02] HISTORICAL ACCEPTANCE TABLE. The NORMAL temperature interval includes both endpoints. A missing authorized route outside that interval is not a zero threshold and does not imply a physical failure. Three repeated runs must be valid and belong to the same unit and profile. Values copied from another serial number do not complete a missing run. The supply condition belongs to applicability rather than to an independent exemption from other prerequisites.

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 2, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-q2aiztjx"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0004-c0001-p0001`

> HOT

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 1, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-q2aiztjx"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0004-c0002-p0001`

> Above 30 degrees Celsius

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 19, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 2, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-q2aiztjx"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0004-c0003-p0001`

> No authorized criterion in revision 1

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 20, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 3, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-q2aiztjx"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0004-c0004-p0001`

> Not specified

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 21, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 4, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-q2aiztjx"}`.

- [input/sources/01-specification-v1.docx.md](input/sources/01-specification-v1.docx.md) — `docx-table-0001-r0004-c0005-p0001`

> No qualification route supplied

Original: [input/originals/D00003.docx](input/originals/D00003.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 22, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 5, "original": "input/originals/D00003.docx", "original_sha256": "42b6976d7613cd50e93501e895fe71377ddaa902f793ed8efc9a002e10c3a8be", "artifact_directory": "extraction/D00003/attempt-q2aiztjx"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0002`

> [V2-02] CURRENT ACCEPTANCE TABLE. Every endpoint in the stated intervals is inclusive. A valid NORMAL delay of 100 milliseconds satisfies the numeric limit; 101 does not. The COLD route additionally requires a current cold-fixture certificate. There is no supplied HOT route, and no route below zero degrees. A table row cannot be applied without checking the environment and profile. The limits in this synthetic exercise are exact integer comparisons; realistic measurement error models are outside scope. The absence of an error model must not be filled by an invented uncertainty discount or an assumed rounding allowance.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 2, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0001-p0001`

> HOT

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 1, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0002-p0001`

> Above 30 degrees Celsius

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 19, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 2, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0003-p0001`

> No authorized threshold

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 20, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 3, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0004-p0001`

> No route

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 21, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 4, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-table-0001-r0004-c0005-p0001`

> No qualification supplied

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[4]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 22, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 4, "cell": 5, "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

- [input/sources/03-exception-annex.docx.md](input/sources/03-exception-annex.docx.md) — `docx-p-0001`

> [X01] SYNTHETIC INCORPORATED ANNEX X. Requirements owner Mara Flint approved this exception under delegation AUTH-7 at 09:00 on 2 June 2033. It applies only to serial E17 for NORMAL tests executed from 09:00 on 2 June through 18:00 on 4 June inclusive. The maximum valid delay for those tests is 110 milliseconds rather than 100. The environment remains 10 through 30 degrees, and every other revision 2 prerequisite remains operative. The exception expressly does not apply to N02, even if N02 shares the same hardware build. The table records the operative scope rather than an illustrative example.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "49ae022a5b2a5568215957e54514add6a50d7c2f129a6f5b354af45ac6931e70", "artifact_directory": "extraction/D00005/attempt-e0u1_qb9"}`.

- [input/sources/02-specification-v2.docx.md](input/sources/02-specification-v2.docx.md) — `docx-p-0024`

> [V2-04] INCORPORATED EXCEPTION. Annex X changes the NORMAL delay threshold for one named serial number and a specific time interval. It changes no other requirement. In particular, it does not expand the temperature range, waive channel B measurement, make expired calibration current, close fault injections, or delegate release signing authority. The applicable general rule and exception must be combined before comparing observed delay. A general threshold alone is an incomplete rule set for a unit covered by an exception. Conversely, resemblance to the exempt unit does not extend an exception to other serial numbers or later dates.

Original: [input/originals/D00004.docx](input/originals/D00004.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 24, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00004.docx", "original_sha256": "c780e4bf1b0a0a08647f2713a2f75c76b7654f8c545ba305a8fe29f0d160169c", "artifact_directory": "extraction/D00004/attempt-6210369o"}`.

### Rules

- An absent authorized threshold/route is not a numeric zero criterion or a physical failure. AnnexX only modifies namedNORMAL tests and cannot addHOT applicability.

### Assumptions

- Use the supplied synthetic H-7 evidence model, exact integer delay values and expressly stated execution/profile/validity fields. No real product certification or measurement-error allowance is inferred.
- Original DOCX bodies/tables and all PDF pages were inspected; source-to-model and civil-date conversions are recorded in model-notes.md and arithmetic-check.md.

### Reasoning

- 1. Both historical and currentHOT rows expressly state no qualification route or authorized criterion; V2-02/AP01 reiterate the absence.
- 2. AnnexX retainsNORMAL10..30 and does not supply aHOT alternative.
- 3. The model returns none forHOT in either supplied revision, supporting the precise packet-scope statement. It does not infer thatHOT operation always fails.

### Limits

- No all-temperature qualification, zero threshold or universal impossibility is established. The absence is restricted to this supplied rule set.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim14` in module `Audit` (supports): `∀ temp, Audit.baseLimit 1 .hot temp = none ∧ Audit.baseLimit 2 .hot temp = none`.
  [Model](models/Audit.lean) · [Executed check](checks/Target032.lean) · [Actual proof log](logs/target-032.log)

### Recommendation

Retain the missing-route scope and avoid extrapolating boundedNORMAL/COLD results toHOT.
