# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

[Semantic correspondence review](semantic-review.md)

Extraction inventory: 9 documents; 1 pending, partial or blocked. See [ingestion details](ingestion.json) and [coverage](coverage.md).

## C08-ERR-01

### Exact report claim

`input/report.md#C08-ERR-01`

> **C08-ERR-01.** Lot A accepted inbound quantity was 96 units.

### Verification question

Does accepted receipt IN-A comprise exactly 96 individual A units?

### Source evidence

- [input/sources/06-shipping-tickets-scan.pdf.md](input/sources/06-shipping-tickets-scan.pdf.md) — `pdf-page-0001-reviewed-0001`

> SYNTHETIC NORTH QUAY SHIPPING FORM
> [T01] Movement IN-A; 14 April 2032; clock 09:00; lot A.
> Quantity boxes: 8 sealed full crates. Status: Accepted by Elin Shore.
> All eight crates carried A labels matching the receiving request. The clerk checked
> the twelve-unit crate convention and placed the containers on A shelves. No goods
> were held beyond the fence. The receipt is posted and complete, not a forecast of a
> later delivery. No partial, damaged, or empty-container notation changes the full
> quantity.
> [T01-CHAIN] This form belongs to the registered source packet. The warehouse boundary
> includes W1, W2, and the fenced return cage. Read planned quantities separately from
> actual signed handoffs. Standard full-container quantities follow the supplied stock
> rules. Carrier custody is distinct from customer delivery. Preserve lot identity in
> every calculation; quantities from another lot cannot repair this form. Any partial-
> container notation would override the standard full conversion. A source quotation
> should retain this original PDF path and marker rather than presenting an OCR excerpt
> as an independently signed record.
> [T01-LIMIT] The form supports only its named movement and stages. It does not certify
> all warehouse inventory or resolve independent physical count differences. A
> signature name is an invented evidence field within this exercise, not a claim about
> real handwriting authentication. Missing attachments must remain missing in the audit
> reasoning. Reviewers should explain how the movement changes the relevant balance
> before relying on an aggregate total.

Original: [input/originals/D00008.pdf](input/originals/D00008.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 1, "origin": {"format": "pdf", "page": 1, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0001-raster.png", "tsv_artifact": "pdf-page-0001.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.25485498297871, "minimum_word_confidence": 45.506126, "confidence_threshold": 85.0, "low_confidence_words": 5, "word_count": 235, "original": "input/originals/D00008.pdf", "original_sha256": "e64921cc43741a187a1063655d55e820e43a91c3f6152d0671af4fce81f7fe58", "artifact_directory": "extraction/D00008/attempt-5bvezmai", "source_anchor": "pdf-page-0001", "root_source_anchor": "pdf-page-0001", "reviewer": "blind-inventory-auditor", "reason": "Compared actual raster page: marker T01 and clock 09:00 were misread; eight full crates and accepted status visually confirmed.", "reviewed_at": "2026-11-04T15:04:15.283217+00:00", "transcription_snapshot": "input/manual-transcriptions/D00008/27a8dd0b9c08462610f0237b36aebddc5203fb42d149a2cf510126e2ed638151.txt", "transcription_file_sha256": "72e3f904601c4f0cb37fa5e793512cff0066e4cfcec41fbcb65926e95cba5a26", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P02`

> [R01] Unit definitions and boundary. The inventory boundary consists of rooms W1 and W2 and the fenced return cage at the invented North Quay warehouse. The cutoff is 18:00 on 14 April 2032. All quantities are exact integer individual sleeves, called units. A sealed full crate contains twelve units. A sealed full carton contains six units. A pallet has no fixed conversion. A partial-container label overrides the standard full-container quantity; an empty container contributes zero. All names and transactions in this packet are invented. These rules define the finite exercise and do not prescribe real shipping procedures.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 664, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P02`

> [J01] Opening and receipts. At 08:00 lot A opened with 100 units and lot B with 40 units. At 09:00 receipt IN-A accepted eight sealed full crates of A. At 09:30 receipt IN-B accepted two sealed full cartons of B. Clerk Elin Shore accepted custody at the gate. Each container was confirmed full, without a partial notation. These are posted accepted receipts, not expected procurement deliveries. No other opening adjustment or accepted inbound movement for A or B occurred before cutoff. The completeness statement is restricted to the named interval and lots. It does not establish any opening quantity for D or repair the C import anomaly.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 51, "end_character": 692, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-x0nfkf9z"}`.

### Rules

- Use R01 exact full-container conversion, R02 actual custody movements and R03 same-lot availability where applicable.
- R04/K03 completeness covers A/B movements for the stated day only; equal-authority counts remain conflicting and missing D/C evidence is not negative fact.

### Assumptions

- The synthetic source authority and finite warehouse boundary are accepted as stated; no source authenticity outside the fixture is certified.

### Reasoning

- 1. Eight full crates were actually accepted; R01 assigns twelve units per full crate.
- 2. Eight times twelve is 96, with no partial-container exception.

### Limits

- Results concern the specified lots, warehouse boundary and 18:00 cutoff on 14 April 2032. Book arithmetic does not select the true physical A count or resolve D acceptance.
- Native pages 1–4 were visually checked and corrected through retained manual transcriptions; page 5 retains quantity/acceptance uncertainty.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim01` in module `Audit` (supports): `Audit.inboundA = 96`.
  [Model](models/Audit.lean) · [Executed check](checks/Target011.lean) · [Actual proof log](logs/target-011.log)

### Recommendation

Accept 96 inbound A units; do not confuse this movement quantity with closing stock.

## C08-ERR-02

### Exact report claim

`input/report.md#C08-ERR-02`

> **C08-ERR-02.** Lot B accepted inbound quantity was 24 units because a carton equals a crate.

### Verification question

Does IN-B contain 24 units, and are cartons equivalent to crates?

### Source evidence

- [input/sources/06-shipping-tickets-scan.pdf.md](input/sources/06-shipping-tickets-scan.pdf.md) — `pdf-page-0002-reviewed-0001`

> SYNTHETIC NORTH QUAY SHIPPING FORM
> [T02] Movement IN-B; 14 April 2032; clock 09:30; lot B.
> Quantity boxes: 2 sealed full cartons. Status: Accepted by Elin Shore.
> Each carton carried a B label and the standard six-unit quantity. The clerk separated
> this receipt from the eight units reserved for the next-day order. No partial
> notation appears. The two accepted cartons belong to B even though the sleeve
> description resembles A. A crate conversion would attach the wrong unit factor to
> this source.
> [T02-CHAIN] This form belongs to the registered source packet. The warehouse boundary
> includes W1, W2, and the fenced return cage. Read planned quantities separately from
> actual signed handoffs. Standard full-container quantities follow the supplied stock
> rules. Carrier custody is distinct from customer delivery. Preserve lot identity in
> every calculation; quantities from another lot cannot repair this form. Any partial-
> container notation would override the standard full conversion. A source quotation
> should retain this original PDF path and marker rather than presenting an OCR excerpt
> as an independently signed record.
> [T02-LIMIT] The form supports only its named movement and stages. It does not certify
> all warehouse inventory or resolve independent physical count differences. A
> signature name is an invented evidence field within this exercise, not a claim about
> real handwriting authentication. Missing attachments must remain missing in the audit
> reasoning. Reviewers should explain how the movement changes the relevant balance
> before relying on an aggregate total.

Original: [input/originals/D00008.pdf](input/originals/D00008.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 2, "origin": {"format": "pdf", "page": 2, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0002-raster.png", "tsv_artifact": "pdf-page-0002.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 94.90358588559322, "minimum_word_confidence": 8.591576, "confidence_threshold": 85.0, "low_confidence_words": 4, "word_count": 236, "original": "input/originals/D00008.pdf", "original_sha256": "e64921cc43741a187a1063655d55e820e43a91c3f6152d0671af4fce81f7fe58", "artifact_directory": "extraction/D00008/attempt-5bvezmai", "source_anchor": "pdf-page-0002", "root_source_anchor": "pdf-page-0002", "reviewer": "blind-inventory-auditor", "reason": "Compared original raster page; corrected marker and clock OCR errors; material quantity, container, actual handoff and custody text visually verified.", "reviewed_at": "2026-11-04T15:04:21.670067+00:00", "transcription_snapshot": "input/manual-transcriptions/D00008/f2c73ff169fa72a87f8a86ce29319fba80b81b376e3a4b6229800b78686ff70a.txt", "transcription_file_sha256": "62466a0a4466eabee04c4d14d61bc57708d7a1914a5dd71fb33fc3cfbd93898d", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P02`

> [R01] Unit definitions and boundary. The inventory boundary consists of rooms W1 and W2 and the fenced return cage at the invented North Quay warehouse. The cutoff is 18:00 on 14 April 2032. All quantities are exact integer individual sleeves, called units. A sealed full crate contains twelve units. A sealed full carton contains six units. A pallet has no fixed conversion. A partial-container label overrides the standard full-container quantity; an empty container contributes zero. All names and transactions in this packet are invented. These rules define the finite exercise and do not prescribe real shipping procedures.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 664, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P02`

> [J01] Opening and receipts. At 08:00 lot A opened with 100 units and lot B with 40 units. At 09:00 receipt IN-A accepted eight sealed full crates of A. At 09:30 receipt IN-B accepted two sealed full cartons of B. Clerk Elin Shore accepted custody at the gate. Each container was confirmed full, without a partial notation. These are posted accepted receipts, not expected procurement deliveries. No other opening adjustment or accepted inbound movement for A or B occurred before cutoff. The completeness statement is restricted to the named interval and lots. It does not establish any opening quantity for D or repair the C import anomaly.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 51, "end_character": 692, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-x0nfkf9z"}`.

### Rules

- Use R01 exact full-container conversion, R02 actual custody movements and R03 same-lot availability where applicable.
- R04/K03 completeness covers A/B movements for the stated day only; equal-authority counts remain conflicting and missing D/C evidence is not negative fact.

### Assumptions

- The synthetic source authority and finite warehouse boundary are accepted as stated; no source authenticity outside the fixture is certified.

### Reasoning

- 1. The signed accepted receipt is two full cartons, not crates.
- 2. R01 assigns six units per carton and twelve per crate. Thus B inbound is 12, not 24; the claimed conversion uses the wrong container.

### Limits

- Results concern the specified lots, warehouse boundary and 18:00 cutoff on 14 April 2032. Book arithmetic does not select the true physical A count or resolve D acceptance.
- Native pages 1–4 were visually checked and corrected through retained manual transcriptions; page 5 retains quantity/acceptance uncertainty.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim02` in module `Audit` (refutes): `Audit.inboundB ≠ 24`.
  [Model](models/Audit.lean) · [Executed check](checks/Target012.lean) · [Actual proof log](logs/target-012.log)

### Recommendation

Correct B inbound to 12 units and preserve the six-unit carton factor.

## C08-ERR-03

### Exact report claim

`input/report.md#C08-ERR-03`

> **C08-ERR-03.** Lot A book on-hand was 136 units.

### Verification question

Is A book on-hand 136 units at the stated cutoff?

### Source evidence

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P02`

> [J01] Opening and receipts. At 08:00 lot A opened with 100 units and lot B with 40 units. At 09:00 receipt IN-A accepted eight sealed full crates of A. At 09:30 receipt IN-B accepted two sealed full cartons of B. Clerk Elin Shore accepted custody at the gate. Each container was confirmed full, without a partial notation. These are posted accepted receipts, not expected procurement deliveries. No other opening adjustment or accepted inbound movement for A or B occurred before cutoff. The completeness statement is restricted to the named interval and lots. It does not establish any opening quantity for D or repair the C import anomaly.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 51, "end_character": 692, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-x0nfkf9z"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P03`

> [J02] A departure, delivery, and return. OUT-A at 11:00 transferred five full crates to carrier Jun Vale. The customer accepted four crates and declined the fifth. At 16:00 Jun returned the still-sealed fifth crate; Elin accepted it inside the fenced return cage. The entire five-crate departure remains recorded, followed by the separate one-crate return. There were no other A departures or returns that day. At 17:00 seven units already on a W1 shelf were quarantined. They remained inside the inventory boundary. A reviewer must therefore distinguish dispatched quantity, delivered quantity, returned quantity, on-hand, and available stock. None of these labels can be substituted merely because they refer to the same order.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 694, "end_character": 1423, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-x0nfkf9z"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P02`

> [R01] Unit definitions and boundary. The inventory boundary consists of rooms W1 and W2 and the fenced return cage at the invented North Quay warehouse. The cutoff is 18:00 on 14 April 2032. All quantities are exact integer individual sleeves, called units. A sealed full crate contains twelve units. A sealed full carton contains six units. A pallet has no fixed conversion. A partial-container label overrides the standard full-container quantity; an empty container contributes zero. All names and transactions in this packet are invented. These rules define the finite exercise and do not prescribe real shipping procedures.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 664, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P03`

> [R02] Movement semantics. Opening stock plus accepted inbound movements minus completed outbound movements plus accepted returns determines book on-hand. A printed ticket, order, reservation, or pick request changes no physical inventory merely by existing. Departure occurs at the signed actual custody handoff across the boundary. Customer delivery is a separate later event. A carrier can hold inventory that has already departed but is not yet delivered. Return increases on-hand when the receiving custodian accepts the goods back across the boundary. Returned goods in the fenced cage are inside the boundary even before reshelving. An accepted return is a separate movement, not a reason to erase the original departure.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 666, "end_character": 1393, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P05`

> [R04] Evidence scope. Signed actual transfer receipts take precedence over unsigned planned quantities for determining completed custody movements. The journal and register are complete for A and B movements only within the stated day. No such completeness applies to D. Equal-authority physical counts of the same boundary and cutoff remain competing evidence unless a recount or authorized correction resolves them. A later filename does not give precedence. A pale or obscured numeral in a scan requires visual review and corroboration. An OCR guess is not a signed quantity. If available evidence does not establish a unique accepted amount, report the missing argument without inventing a number or asserting that the shipment necessarily failed.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2118, "end_character": 2869, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

- [input/sources/05-custody-register.md](input/sources/05-custody-register.md) — `P04`

> [K03] Bounded completeness. The register and journal list all accepted A and B movements for the stated day. This permits absence of further A or B movements to be used in exact book arithmetic. It does not establish complete D custody, complete C physical reconciliation, or complete warehouse activity over other dates. The A physical count conflict remains unresolved despite complete movement records. Completeness of one evidence type is not an assertion that every other evidence type agrees. A report that says every lot was reconciled therefore needs an argument beyond the limited A/B movement inventory and must confront the explicit unresolved cases.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1377, "end_character": 2038, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "54ba3d90c6fd73c04b139b20f2cc369e144f6050697949c27f883d4209ad2830", "artifact_directory": "extraction/D00007/attempt-ly8ukxxe"}`.

- [input/sources/06-shipping-tickets-scan.pdf.md](input/sources/06-shipping-tickets-scan.pdf.md) — `pdf-page-0003-reviewed-0001`

> SYNTHETIC NORTH QUAY SHIPPING FORM
> [T03] Movement OUT-A / RET-A; 14 April 2032; clock 11:00 / 16:00; lot A.
> Quantity boxes: 5 full crates out; 1 full crate returned. Status: Carrier Jun Vale /
> receiver Elin Shore.
> The carrier accepted five crates before departure. The customer accepted four. The
> fifth remained sealed in the vehicle and returned that afternoon. Elin signed the
> return after placing it inside the fenced cage. The full departure and the separate
> return are both operative entries. Erasing the departure and adding a return would
> count the same reversal twice.
> [T03-CHAIN] This form belongs to the registered source packet. The warehouse boundary
> includes W1, W2, and the fenced return cage. Read planned quantities separately from
> actual signed handoffs. Standard full-container quantities follow the supplied stock
> rules. Carrier custody is distinct from customer delivery. Preserve lot identity in
> every calculation; quantities from another lot cannot repair this form. Any partial-
> container notation would override the standard full conversion. A source quotation
> should retain this original PDF path and marker rather than presenting an OCR excerpt
> as an independently signed record.
> [T03-LIMIT] The form supports only its named movement and stages. It does not certify
> all warehouse inventory or resolve independent physical count differences. A
> signature name is an invented evidence field within this exercise, not a claim about
> real handwriting authentication. Missing attachments must remain missing in the audit
> reasoning. Reviewers should explain how the movement changes the relevant balance
> before relying on an aggregate total.

Original: [input/originals/D00008.pdf](input/originals/D00008.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 3, "origin": {"format": "pdf", "page": 3, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0003-raster.png", "tsv_artifact": "pdf-page-0003.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.59391616867471, "minimum_word_confidence": 44.648014, "confidence_threshold": 85.0, "low_confidence_words": 3, "word_count": 249, "original": "input/originals/D00008.pdf", "original_sha256": "e64921cc43741a187a1063655d55e820e43a91c3f6152d0671af4fce81f7fe58", "artifact_directory": "extraction/D00008/attempt-5bvezmai", "source_anchor": "pdf-page-0003", "root_source_anchor": "pdf-page-0003", "reviewer": "blind-inventory-auditor", "reason": "Compared original raster page; corrected marker and clock OCR errors; material quantity, container, actual handoff and custody text visually verified.", "reviewed_at": "2026-11-04T15:04:21.811157+00:00", "transcription_snapshot": "input/manual-transcriptions/D00008/74d057c1ffd7a573949b5264432bbf95d0ac166f21a1a683072c9f16d09c7d65.txt", "transcription_file_sha256": "8cb046c528b21f24a3e2768bfed2e1a4d71a489c47e9007ea0be72fbf2bfc611", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

### Rules

- Use R01 exact full-container conversion, R02 actual custody movements and R03 same-lot availability where applicable.
- R04/K03 completeness covers A/B movements for the stated day only; equal-authority counts remain conflicting and missing D/C evidence is not negative fact.

### Assumptions

- The synthetic source authority and finite warehouse boundary are accepted as stated; no source authenticity outside the fixture is certified.

### Reasoning

- 1. Start with 100; add 96 accepted inbound; subtract 60 actual outbound; add 12 accepted return.
- 2. The returned crate is inside the fenced cage boundary. Complete A movements give 148; 136 omits the separately accepted return.

### Limits

- Results concern the specified lots, warehouse boundary and 18:00 cutoff on 14 April 2032. Book arithmetic does not select the true physical A count or resolve D acceptance.
- Native pages 1–4 were visually checked and corrected through retained manual transcriptions; page 5 retains quantity/acceptance uncertainty.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim03` in module `Audit` (refutes): `Audit.bookA ≠ 136`.
  [Model](models/Audit.lean) · [Executed check](checks/Target013.lean) · [Actual proof log](logs/target-013.log)

### Recommendation

Correct book A on-hand to 148; retain the departure and its separate return.

## C08-ERR-04

### Exact report claim

`input/report.md#C08-ERR-04`

> **C08-ERR-04.** Lot A available book stock was 148 units because quarantine remains on site.

### Verification question

Does physical presence make A available stock equal its 148-unit book balance?

### Source evidence

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P03`

> [R02] Movement semantics. Opening stock plus accepted inbound movements minus completed outbound movements plus accepted returns determines book on-hand. A printed ticket, order, reservation, or pick request changes no physical inventory merely by existing. Departure occurs at the signed actual custody handoff across the boundary. Customer delivery is a separate later event. A carrier can hold inventory that has already departed but is not yet delivered. Return increases on-hand when the receiving custodian accepts the goods back across the boundary. Returned goods in the fenced cage are inside the boundary even before reshelving. An accepted return is a separate movement, not a reason to erase the original departure.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 666, "end_character": 1393, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P04`

> [R03] Lot identity and availability. Lots A, B, C, and D are separate even though their sleeves share a catalog description. An excess in one lot cannot repair a deficit in another. Available stock is book on-hand minus quarantined units minus separately reserved units, with no overlapping deductions. The A quarantine contains seven units. The B reservation contains eight different units. Quarantine and reservation change internal status without transferring custody. Physical presence, book balance, and available quantity are different predicates. A physical count may disagree with a journal-derived balance, and the disagreement must remain visible rather than silently redefining one quantity to match the other.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1395, "end_character": 2116, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P02`

> [J01] Opening and receipts. At 08:00 lot A opened with 100 units and lot B with 40 units. At 09:00 receipt IN-A accepted eight sealed full crates of A. At 09:30 receipt IN-B accepted two sealed full cartons of B. Clerk Elin Shore accepted custody at the gate. Each container was confirmed full, without a partial notation. These are posted accepted receipts, not expected procurement deliveries. No other opening adjustment or accepted inbound movement for A or B occurred before cutoff. The completeness statement is restricted to the named interval and lots. It does not establish any opening quantity for D or repair the C import anomaly.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 51, "end_character": 692, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-x0nfkf9z"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P03`

> [J02] A departure, delivery, and return. OUT-A at 11:00 transferred five full crates to carrier Jun Vale. The customer accepted four crates and declined the fifth. At 16:00 Jun returned the still-sealed fifth crate; Elin accepted it inside the fenced return cage. The entire five-crate departure remains recorded, followed by the separate one-crate return. There were no other A departures or returns that day. At 17:00 seven units already on a W1 shelf were quarantined. They remained inside the inventory boundary. A reviewer must therefore distinguish dispatched quantity, delivered quantity, returned quantity, on-hand, and available stock. None of these labels can be substituted merely because they refer to the same order.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 694, "end_character": 1423, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-x0nfkf9z"}`.

- [input/sources/05-custody-register.md](input/sources/05-custody-register.md) — `P04`

> [K03] Bounded completeness. The register and journal list all accepted A and B movements for the stated day. This permits absence of further A or B movements to be used in exact book arithmetic. It does not establish complete D custody, complete C physical reconciliation, or complete warehouse activity over other dates. The A physical count conflict remains unresolved despite complete movement records. Completeness of one evidence type is not an assertion that every other evidence type agrees. A report that says every lot was reconciled therefore needs an argument beyond the limited A/B movement inventory and must confront the explicit unresolved cases.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1377, "end_character": 2038, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "54ba3d90c6fd73c04b139b20f2cc369e144f6050697949c27f883d4209ad2830", "artifact_directory": "extraction/D00007/attempt-ly8ukxxe"}`.

- [input/sources/07-bin-and-exception-register.md](input/sources/07-bin-and-exception-register.md) — `P03`

> [BIN02] Quarantine ticket Q-A-7. At 17:00 Elin attached a hold label to seven loose A units on shelf A1 after noticing cosmetic sleeve marks. The ticket states that those seven units remain physically in W1 and are excluded from availability pending review. It does not order disposal, destruction, shipment, or a transfer to another lot. The label applies to individual units, not seven crates. No later release from quarantine occurred before cutoff. The physical count sheets both expressly included the held units. The record supports a status deduction from available A stock without decrementing A book on-hand.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 712, "end_character": 1329, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "17864baef381443926666ff2acbb425f97ab919bb09877291086a640ba22e3f9", "artifact_directory": "extraction/D00009/attempt-2lly49hx"}`.

### Rules

- Use R01 exact full-container conversion, R02 actual custody movements and R03 same-lot availability where applicable.
- R04/K03 completeness covers A/B movements for the stated day only; equal-authority counts remain conflicting and missing D/C evidence is not negative fact.

### Assumptions

- The synthetic source authority and finite warehouse boundary are accepted as stated; no source authenticity outside the fixture is certified.

### Reasoning

- 1. A book on-hand is 148 after all complete movements.
- 2. Seven quarantined A units stay on site but R03 excludes them from availability; BIN02 records no release. Availability is 148 minus 7 = 141.

### Limits

- Results concern the specified lots, warehouse boundary and 18:00 cutoff on 14 April 2032. Book arithmetic does not select the true physical A count or resolve D acceptance.
- Formal checks prove encoded targets only; unsupported physical facts are not inferred from missing evidence.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim04` in module `Audit` (refutes): `Audit.availableA ≠ 148`.
  [Model](models/Audit.lean) · [Executed check](checks/Target014.lean) · [Actual proof log](logs/target-014.log)

### Recommendation

Report 141 available A units while keeping book on-hand 148.

## C08-ERR-05

### Exact report claim

`input/report.md#C08-ERR-05`

> **C08-ERR-05.** Lot B book on-hand was 34 units after all three requested cartons shipped.

### Verification question

Did all three requested B cartons ship, leaving book on-hand 34?

### Source evidence

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P02`

> [J01] Opening and receipts. At 08:00 lot A opened with 100 units and lot B with 40 units. At 09:00 receipt IN-A accepted eight sealed full crates of A. At 09:30 receipt IN-B accepted two sealed full cartons of B. Clerk Elin Shore accepted custody at the gate. Each container was confirmed full, without a partial notation. These are posted accepted receipts, not expected procurement deliveries. No other opening adjustment or accepted inbound movement for A or B occurred before cutoff. The completeness statement is restricted to the named interval and lots. It does not establish any opening quantity for D or repair the C import anomaly.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 51, "end_character": 692, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-x0nfkf9z"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P04`

> [J03] B request and actual handoff. OUT-B requested three cartons, but the signed carrier handoff at 12:00 records two full cartons. The remaining carton stayed on shelf B4 because its packaging label was missing. At 15:00 that unfilled order quantity was canceled. It never crossed the warehouse boundary. A separate next-day order reserved eight other B units, distinct from both the dispatched cartons and the canceled request. There was no B return and no need to invent one: the canceled quantity never left. The A quarantine affects no B stock. The B journal contains no other completed inbound, outbound, or return movements within the cutoff interval.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1425, "end_character": 2084, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-x0nfkf9z"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P02`

> [R01] Unit definitions and boundary. The inventory boundary consists of rooms W1 and W2 and the fenced return cage at the invented North Quay warehouse. The cutoff is 18:00 on 14 April 2032. All quantities are exact integer individual sleeves, called units. A sealed full crate contains twelve units. A sealed full carton contains six units. A pallet has no fixed conversion. A partial-container label overrides the standard full-container quantity; an empty container contributes zero. All names and transactions in this packet are invented. These rules define the finite exercise and do not prescribe real shipping procedures.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 664, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P03`

> [R02] Movement semantics. Opening stock plus accepted inbound movements minus completed outbound movements plus accepted returns determines book on-hand. A printed ticket, order, reservation, or pick request changes no physical inventory merely by existing. Departure occurs at the signed actual custody handoff across the boundary. Customer delivery is a separate later event. A carrier can hold inventory that has already departed but is not yet delivered. Return increases on-hand when the receiving custodian accepts the goods back across the boundary. Returned goods in the fenced cage are inside the boundary even before reshelving. An accepted return is a separate movement, not a reason to erase the original departure.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 666, "end_character": 1393, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

- [input/sources/05-custody-register.md](input/sources/05-custody-register.md) — `P04`

> [K03] Bounded completeness. The register and journal list all accepted A and B movements for the stated day. This permits absence of further A or B movements to be used in exact book arithmetic. It does not establish complete D custody, complete C physical reconciliation, or complete warehouse activity over other dates. The A physical count conflict remains unresolved despite complete movement records. Completeness of one evidence type is not an assertion that every other evidence type agrees. A report that says every lot was reconciled therefore needs an argument beyond the limited A/B movement inventory and must confront the explicit unresolved cases.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1377, "end_character": 2038, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "54ba3d90c6fd73c04b139b20f2cc369e144f6050697949c27f883d4209ad2830", "artifact_directory": "extraction/D00007/attempt-ly8ukxxe"}`.

- [input/sources/06-shipping-tickets-scan.pdf.md](input/sources/06-shipping-tickets-scan.pdf.md) — `pdf-page-0004-reviewed-0001`

> SYNTHETIC NORTH QUAY SHIPPING FORM
> [T04] Movement OUT-B; 14 April 2032; clock 12:00; lot B.
> Quantity boxes: 3 cartons requested; 2 full cartons handed over. Status: Carrier Jun
> Vale signed actual handoff.
> The request box was printed before loading and shows three cartons. The signed actual
> box shows two. The remaining carton stayed on shelf because its label was missing. At
> 15:00 the unfilled remainder was canceled. No customer return occurred for that
> carton. The two actually transferred cartons were delivered, but the original three-
> carton order was not fully delivered.
> [T04-CHAIN] This form belongs to the registered source packet. The warehouse boundary
> includes W1, W2, and the fenced return cage. Read planned quantities separately from
> actual signed handoffs. Standard full-container quantities follow the supplied stock
> rules. Carrier custody is distinct from customer delivery. Preserve lot identity in
> every calculation; quantities from another lot cannot repair this form. Any partial-
> container notation would override the standard full conversion. A source quotation
> should retain this original PDF path and marker rather than presenting an OCR excerpt
> as an independently signed record.
> [T04-LIMIT] The form supports only its named movement and stages. It does not certify
> all warehouse inventory or resolve independent physical count differences. A
> signature name is an invented evidence field within this exercise, not a claim about
> real handwriting authentication. Missing attachments must remain missing in the audit
> reasoning. Reviewers should explain how the movement changes the relevant balance
> before relying on an aggregate total.

Original: [input/originals/D00008.pdf](input/originals/D00008.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 4, "origin": {"format": "pdf", "page": 4, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0004-raster.png", "tsv_artifact": "pdf-page-0004.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.65679095528456, "minimum_word_confidence": 65.657257, "confidence_threshold": 85.0, "low_confidence_words": 4, "word_count": 246, "original": "input/originals/D00008.pdf", "original_sha256": "e64921cc43741a187a1063655d55e820e43a91c3f6152d0671af4fce81f7fe58", "artifact_directory": "extraction/D00008/attempt-5bvezmai", "source_anchor": "pdf-page-0004", "root_source_anchor": "pdf-page-0004", "reviewer": "blind-inventory-auditor", "reason": "Compared original raster page; corrected marker and clock OCR errors; material quantity, container, actual handoff and custody text visually verified.", "reviewed_at": "2026-11-04T15:04:21.953190+00:00", "transcription_snapshot": "input/manual-transcriptions/D00008/653097fa4c7e85eb684393bda9dd0a3959fec379a0851eefccc17e303dbea4da.txt", "transcription_file_sha256": "10e99572a3bd9fb6e15426d1069925eeb7e516a18cc3c2aa41bfa9b3fb21c681", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

### Rules

- Use R01 exact full-container conversion, R02 actual custody movements and R03 same-lot availability where applicable.
- R04/K03 completeness covers A/B movements for the stated day only; equal-authority counts remain conflicting and missing D/C evidence is not negative fact.

### Assumptions

- The synthetic source authority and finite warehouse boundary are accepted as stated; no source authenticity outside the fixture is certified.

### Reasoning

- 1. Only two full cartons crossed the signed actual handoff; the third remained on the shelf and was canceled.
- 2. Book B is 40 + 12 - 12 = 40. Subtracting requested rather than actual cartons produces the erroneous 34.

### Limits

- Results concern the specified lots, warehouse boundary and 18:00 cutoff on 14 April 2032. Book arithmetic does not select the true physical A count or resolve D acceptance.
- Native pages 1–4 were visually checked and corrected through retained manual transcriptions; page 5 retains quantity/acceptance uncertainty.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim05` in module `Audit` (refutes): `Audit.bookB ≠ 34 ∧ Audit.deliveredB ≠ Audit.requestedB`.
  [Model](models/Audit.lean) · [Executed check](checks/Target015.lean) · [Actual proof log](logs/target-015.log)

### Recommendation

Report 40 book B units; only two cartons shipped.

## C08-ERR-06

### Exact report claim

`input/report.md#C08-ERR-06`

> **C08-ERR-06.** Lot B available stock was 32 units.

### Verification question

Is B available stock 32 units after its separate reservation?

### Source evidence

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P04`

> [R03] Lot identity and availability. Lots A, B, C, and D are separate even though their sleeves share a catalog description. An excess in one lot cannot repair a deficit in another. Available stock is book on-hand minus quarantined units minus separately reserved units, with no overlapping deductions. The A quarantine contains seven units. The B reservation contains eight different units. Quarantine and reservation change internal status without transferring custody. Physical presence, book balance, and available quantity are different predicates. A physical count may disagree with a journal-derived balance, and the disagreement must remain visible rather than silently redefining one quantity to match the other.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1395, "end_character": 2116, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P02`

> [J01] Opening and receipts. At 08:00 lot A opened with 100 units and lot B with 40 units. At 09:00 receipt IN-A accepted eight sealed full crates of A. At 09:30 receipt IN-B accepted two sealed full cartons of B. Clerk Elin Shore accepted custody at the gate. Each container was confirmed full, without a partial notation. These are posted accepted receipts, not expected procurement deliveries. No other opening adjustment or accepted inbound movement for A or B occurred before cutoff. The completeness statement is restricted to the named interval and lots. It does not establish any opening quantity for D or repair the C import anomaly.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 51, "end_character": 692, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-x0nfkf9z"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P04`

> [J03] B request and actual handoff. OUT-B requested three cartons, but the signed carrier handoff at 12:00 records two full cartons. The remaining carton stayed on shelf B4 because its packaging label was missing. At 15:00 that unfilled order quantity was canceled. It never crossed the warehouse boundary. A separate next-day order reserved eight other B units, distinct from both the dispatched cartons and the canceled request. There was no B return and no need to invent one: the canceled quantity never left. The A quarantine affects no B stock. The B journal contains no other completed inbound, outbound, or return movements within the cutoff interval.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1425, "end_character": 2084, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-x0nfkf9z"}`.

- [input/sources/05-custody-register.md](input/sources/05-custody-register.md) — `P04`

> [K03] Bounded completeness. The register and journal list all accepted A and B movements for the stated day. This permits absence of further A or B movements to be used in exact book arithmetic. It does not establish complete D custody, complete C physical reconciliation, or complete warehouse activity over other dates. The A physical count conflict remains unresolved despite complete movement records. Completeness of one evidence type is not an assertion that every other evidence type agrees. A report that says every lot was reconciled therefore needs an argument beyond the limited A/B movement inventory and must confront the explicit unresolved cases.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1377, "end_character": 2038, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "54ba3d90c6fd73c04b139b20f2cc369e144f6050697949c27f883d4209ad2830", "artifact_directory": "extraction/D00007/attempt-ly8ukxxe"}`.

- [input/sources/07-bin-and-exception-register.md](input/sources/07-bin-and-exception-register.md) — `P04`

> [BIN03] Reservation ticket RES-B-8. The next-day customer order reserves eight B units located on shelf B2. The units were not among the two cartons loaded for OUT-B and were not the canceled third carton on B4. The reservation was still active at cutoff. The operator may not release those units to another order without canceling or changing the reservation record, but no such change occurred that day. These facts justify treating the reservation as a distinct deduction when calculating available B stock. They do not establish an outbound movement, a customer delivery, or physical absence from the B count boundary.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1331, "end_character": 1953, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "17864baef381443926666ff2acbb425f97ab919bb09877291086a640ba22e3f9", "artifact_directory": "extraction/D00009/attempt-2lly49hx"}`.

### Rules

- Use R01 exact full-container conversion, R02 actual custody movements and R03 same-lot availability where applicable.
- R04/K03 completeness covers A/B movements for the stated day only; equal-authority counts remain conflicting and missing D/C evidence is not negative fact.

### Assumptions

- The synthetic source authority and finite warehouse boundary are accepted as stated; no source authenticity outside the fixture is certified.

### Reasoning

- 1. Complete B movements give 40 book on-hand.
- 2. The separate eight B units are still reserved at cutoff, so availability is 40 minus 8 = 32. A quarantine does not enter this calculation.

### Limits

- Results concern the specified lots, warehouse boundary and 18:00 cutoff on 14 April 2032. Book arithmetic does not select the true physical A count or resolve D acceptance.
- Formal checks prove encoded targets only; unsupported physical facts are not inferred from missing evidence.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim06` in module `Audit` (supports): `Audit.availableB = 32`.
  [Model](models/Audit.lean) · [Executed check](checks/Target016.lean) · [Actual proof log](logs/target-016.log)

### Recommendation

Retain 32 available B units, distinct from physical/book 40.

## C08-ERR-07

### Exact report claim

`input/report.md#C08-ERR-07`

> **C08-ERR-07.** All 60 A units dispatched were delivered to the customer.

### Verification question

Were all sixty dispatched A units delivered to the customer?

### Source evidence

- [input/sources/06-shipping-tickets-scan.pdf.md](input/sources/06-shipping-tickets-scan.pdf.md) — `pdf-page-0003-reviewed-0001`

> SYNTHETIC NORTH QUAY SHIPPING FORM
> [T03] Movement OUT-A / RET-A; 14 April 2032; clock 11:00 / 16:00; lot A.
> Quantity boxes: 5 full crates out; 1 full crate returned. Status: Carrier Jun Vale /
> receiver Elin Shore.
> The carrier accepted five crates before departure. The customer accepted four. The
> fifth remained sealed in the vehicle and returned that afternoon. Elin signed the
> return after placing it inside the fenced cage. The full departure and the separate
> return are both operative entries. Erasing the departure and adding a return would
> count the same reversal twice.
> [T03-CHAIN] This form belongs to the registered source packet. The warehouse boundary
> includes W1, W2, and the fenced return cage. Read planned quantities separately from
> actual signed handoffs. Standard full-container quantities follow the supplied stock
> rules. Carrier custody is distinct from customer delivery. Preserve lot identity in
> every calculation; quantities from another lot cannot repair this form. Any partial-
> container notation would override the standard full conversion. A source quotation
> should retain this original PDF path and marker rather than presenting an OCR excerpt
> as an independently signed record.
> [T03-LIMIT] The form supports only its named movement and stages. It does not certify
> all warehouse inventory or resolve independent physical count differences. A
> signature name is an invented evidence field within this exercise, not a claim about
> real handwriting authentication. Missing attachments must remain missing in the audit
> reasoning. Reviewers should explain how the movement changes the relevant balance
> before relying on an aggregate total.

Original: [input/originals/D00008.pdf](input/originals/D00008.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 3, "origin": {"format": "pdf", "page": 3, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0003-raster.png", "tsv_artifact": "pdf-page-0003.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.59391616867471, "minimum_word_confidence": 44.648014, "confidence_threshold": 85.0, "low_confidence_words": 3, "word_count": 249, "original": "input/originals/D00008.pdf", "original_sha256": "e64921cc43741a187a1063655d55e820e43a91c3f6152d0671af4fce81f7fe58", "artifact_directory": "extraction/D00008/attempt-5bvezmai", "source_anchor": "pdf-page-0003", "root_source_anchor": "pdf-page-0003", "reviewer": "blind-inventory-auditor", "reason": "Compared original raster page; corrected marker and clock OCR errors; material quantity, container, actual handoff and custody text visually verified.", "reviewed_at": "2026-11-04T15:04:21.811157+00:00", "transcription_snapshot": "input/manual-transcriptions/D00008/74d057c1ffd7a573949b5264432bbf95d0ac166f21a1a683072c9f16d09c7d65.txt", "transcription_file_sha256": "8cb046c528b21f24a3e2768bfed2e1a4d71a489c47e9007ea0be72fbf2bfc611", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P03`

> [J02] A departure, delivery, and return. OUT-A at 11:00 transferred five full crates to carrier Jun Vale. The customer accepted four crates and declined the fifth. At 16:00 Jun returned the still-sealed fifth crate; Elin accepted it inside the fenced return cage. The entire five-crate departure remains recorded, followed by the separate one-crate return. There were no other A departures or returns that day. At 17:00 seven units already on a W1 shelf were quarantined. They remained inside the inventory boundary. A reviewer must therefore distinguish dispatched quantity, delivered quantity, returned quantity, on-hand, and available stock. None of these labels can be substituted merely because they refer to the same order.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 694, "end_character": 1423, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-x0nfkf9z"}`.

- [input/sources/04-receiving-messages.md](input/sources/04-receiving-messages.md) — `P03`

> [M02] A completion confirmation. The customer accepted four A crates and declined one. The carrier returned the declined crate to North Quay before cutoff, and the warehouse acknowledged acceptance inside the cage. Thus every crate that departed has a documented later disposition, but the customer did not receive all five. A claim that the order was completely delivered differs from a claim that the movement chain can be traced. The return closes custody for the fifth crate while preserving the distinction between delivery and return. A reviewer should quote the relevant stage and quantity instead of using the vague term completed without defining what completed means.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 692, "end_character": 1369, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "5902f74c3a28ac0e3f3d0e49dc8503a2d0417d6a3658bde4c64ba768051d0c17", "artifact_directory": "extraction/D00006/attempt-noaji46d"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P02`

> [R01] Unit definitions and boundary. The inventory boundary consists of rooms W1 and W2 and the fenced return cage at the invented North Quay warehouse. The cutoff is 18:00 on 14 April 2032. All quantities are exact integer individual sleeves, called units. A sealed full crate contains twelve units. A sealed full carton contains six units. A pallet has no fixed conversion. A partial-container label overrides the standard full-container quantity; an empty container contributes zero. All names and transactions in this packet are invented. These rules define the finite exercise and do not prescribe real shipping procedures.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 664, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P03`

> [R02] Movement semantics. Opening stock plus accepted inbound movements minus completed outbound movements plus accepted returns determines book on-hand. A printed ticket, order, reservation, or pick request changes no physical inventory merely by existing. Departure occurs at the signed actual custody handoff across the boundary. Customer delivery is a separate later event. A carrier can hold inventory that has already departed but is not yet delivered. Return increases on-hand when the receiving custodian accepts the goods back across the boundary. Returned goods in the fenced cage are inside the boundary even before reshelving. An accepted return is a separate movement, not a reason to erase the original departure.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 666, "end_character": 1393, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

### Rules

- Use R01 exact full-container conversion, R02 actual custody movements and R03 same-lot availability where applicable.
- R04/K03 completeness covers A/B movements for the stated day only; equal-authority counts remain conflicting and missing D/C evidence is not negative fact.

### Assumptions

- The synthetic source authority and finite warehouse boundary are accepted as stated; no source authenticity outside the fixture is certified.

### Reasoning

- 1. Five crates departed, but the customer accepted only four and refused the fifth.
- 2. Four crates are 48 delivered units; the twelve-unit fifth crate returned. Traced custody does not mean full customer delivery.

### Limits

- Results concern the specified lots, warehouse boundary and 18:00 cutoff on 14 April 2032. Book arithmetic does not select the true physical A count or resolve D acceptance.
- Native pages 1–4 were visually checked and corrected through retained manual transcriptions; page 5 retains quantity/acceptance uncertainty.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim07` in module `Audit` (refutes): `Audit.deliveredA ≠ Audit.dispatchedA`.
  [Model](models/Audit.lean) · [Executed check](checks/Target017.lean) · [Actual proof log](logs/target-017.log)

### Recommendation

Report 60 dispatched, 48 delivered and 12 returned A units.

## C08-ERR-08

### Exact report claim

`input/report.md#C08-ERR-08`

> **C08-ERR-08.** The B customer order was completely delivered.

### Verification question

Was the original three-carton B customer order completely delivered?

### Source evidence

- [input/sources/06-shipping-tickets-scan.pdf.md](input/sources/06-shipping-tickets-scan.pdf.md) — `pdf-page-0004-reviewed-0001`

> SYNTHETIC NORTH QUAY SHIPPING FORM
> [T04] Movement OUT-B; 14 April 2032; clock 12:00; lot B.
> Quantity boxes: 3 cartons requested; 2 full cartons handed over. Status: Carrier Jun
> Vale signed actual handoff.
> The request box was printed before loading and shows three cartons. The signed actual
> box shows two. The remaining carton stayed on shelf because its label was missing. At
> 15:00 the unfilled remainder was canceled. No customer return occurred for that
> carton. The two actually transferred cartons were delivered, but the original three-
> carton order was not fully delivered.
> [T04-CHAIN] This form belongs to the registered source packet. The warehouse boundary
> includes W1, W2, and the fenced return cage. Read planned quantities separately from
> actual signed handoffs. Standard full-container quantities follow the supplied stock
> rules. Carrier custody is distinct from customer delivery. Preserve lot identity in
> every calculation; quantities from another lot cannot repair this form. Any partial-
> container notation would override the standard full conversion. A source quotation
> should retain this original PDF path and marker rather than presenting an OCR excerpt
> as an independently signed record.
> [T04-LIMIT] The form supports only its named movement and stages. It does not certify
> all warehouse inventory or resolve independent physical count differences. A
> signature name is an invented evidence field within this exercise, not a claim about
> real handwriting authentication. Missing attachments must remain missing in the audit
> reasoning. Reviewers should explain how the movement changes the relevant balance
> before relying on an aggregate total.

Original: [input/originals/D00008.pdf](input/originals/D00008.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 4, "origin": {"format": "pdf", "page": 4, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0004-raster.png", "tsv_artifact": "pdf-page-0004.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.65679095528456, "minimum_word_confidence": 65.657257, "confidence_threshold": 85.0, "low_confidence_words": 4, "word_count": 246, "original": "input/originals/D00008.pdf", "original_sha256": "e64921cc43741a187a1063655d55e820e43a91c3f6152d0671af4fce81f7fe58", "artifact_directory": "extraction/D00008/attempt-5bvezmai", "source_anchor": "pdf-page-0004", "root_source_anchor": "pdf-page-0004", "reviewer": "blind-inventory-auditor", "reason": "Compared original raster page; corrected marker and clock OCR errors; material quantity, container, actual handoff and custody text visually verified.", "reviewed_at": "2026-11-04T15:04:21.953190+00:00", "transcription_snapshot": "input/manual-transcriptions/D00008/653097fa4c7e85eb684393bda9dd0a3959fec379a0851eefccc17e303dbea4da.txt", "transcription_file_sha256": "10e99572a3bd9fb6e15426d1069925eeb7e516a18cc3c2aa41bfa9b3fb21c681", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P04`

> [J03] B request and actual handoff. OUT-B requested three cartons, but the signed carrier handoff at 12:00 records two full cartons. The remaining carton stayed on shelf B4 because its packaging label was missing. At 15:00 that unfilled order quantity was canceled. It never crossed the warehouse boundary. A separate next-day order reserved eight other B units, distinct from both the dispatched cartons and the canceled request. There was no B return and no need to invent one: the canceled quantity never left. The A quarantine affects no B stock. The B journal contains no other completed inbound, outbound, or return movements within the cutoff interval.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1425, "end_character": 2084, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-x0nfkf9z"}`.

- [input/sources/04-receiving-messages.md](input/sources/04-receiving-messages.md) — `P04`

> [M03] B order closure. The customer confirms receiving the two cartons actually transferred to the carrier. The third requested carton remained at the warehouse and was canceled. All handed-over cartons were delivered, but the original three-carton order was not fully delivered. These statements concern different denominators and are consistent. Cancellation closes unfilled demand without moving stock. It does not prove a customer return, loss, or hidden replacement shipment. The separate eight-unit reservation remains an allocation within the warehouse and must not be confused with the canceled carton. Each statement retains its lot and order identity.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1371, "end_character": 2032, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "5902f74c3a28ac0e3f3d0e49dc8503a2d0417d6a3658bde4c64ba768051d0c17", "artifact_directory": "extraction/D00006/attempt-noaji46d"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P02`

> [R01] Unit definitions and boundary. The inventory boundary consists of rooms W1 and W2 and the fenced return cage at the invented North Quay warehouse. The cutoff is 18:00 on 14 April 2032. All quantities are exact integer individual sleeves, called units. A sealed full crate contains twelve units. A sealed full carton contains six units. A pallet has no fixed conversion. A partial-container label overrides the standard full-container quantity; an empty container contributes zero. All names and transactions in this packet are invented. These rules define the finite exercise and do not prescribe real shipping procedures.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 664, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P03`

> [R02] Movement semantics. Opening stock plus accepted inbound movements minus completed outbound movements plus accepted returns determines book on-hand. A printed ticket, order, reservation, or pick request changes no physical inventory merely by existing. Departure occurs at the signed actual custody handoff across the boundary. Customer delivery is a separate later event. A carrier can hold inventory that has already departed but is not yet delivered. Return increases on-hand when the receiving custodian accepts the goods back across the boundary. Returned goods in the fenced cage are inside the boundary even before reshelving. An accepted return is a separate movement, not a reason to erase the original departure.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 666, "end_character": 1393, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

### Rules

- Use R01 exact full-container conversion, R02 actual custody movements and R03 same-lot availability where applicable.
- R04/K03 completeness covers A/B movements for the stated day only; equal-authority counts remain conflicting and missing D/C evidence is not negative fact.

### Assumptions

- The synthetic source authority and finite warehouse boundary are accepted as stated; no source authenticity outside the fixture is certified.

### Reasoning

- 1. M03 confirms delivery of the two actual handed-over cartons only.
- 2. The third requested carton was canceled without leaving. Two delivered cartons do not fulfill the original three-carton denominator.

### Limits

- Results concern the specified lots, warehouse boundary and 18:00 cutoff on 14 April 2032. Book arithmetic does not select the true physical A count or resolve D acceptance.
- Native pages 1–4 were visually checked and corrected through retained manual transcriptions; page 5 retains quantity/acceptance uncertainty.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim08` in module `Audit` (refutes): `Audit.deliveredB ≠ Audit.requestedB`.
  [Model](models/Audit.lean) · [Executed check](checks/Target018.lean) · [Actual proof log](logs/target-018.log)

### Recommendation

State that all actually shipped B cartons arrived, while the original order was not fully delivered.

## C08-ERR-09

### Exact report claim

`input/report.md#C08-ERR-09`

> **C08-ERR-09.** The physical A count was exactly 148 units.

### Verification question

Can the true physical A count at the common cutoff and boundary be fixed at exactly 148?

### Source evidence

- [input/sources/03-signed-counts.md](input/sources/03-signed-counts.md) — `P02`

> [N01] Elin Shore signed COUNT-A-1 at the 18:00 cutoff. The stated count is: Lot A, all W1 shelves and fenced return cage, total 148 units. It includes the seven quarantined units and the returned sealed crate. Open shelves were counted by individual units; unopened crates used the verified standard conversion. No damaged, returned, or reserved goods were excluded. A witness initial appears, but the witness did not supply an independent count. The sheet is accepted as signed evidence within this synthetic packet, not as an infallible world axiom. Its numerical agreement with book arithmetic does not automatically invalidate another equally authoritative observation.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 33, "end_character": 706, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "902b530d21257c2ef30042baaa46dbc1fd5d2d6e8576e8d8c18fdc3c1b8d28af", "artifact_directory": "extraction/D00005/attempt-91hpqtsz"}`.

- [input/sources/03-signed-counts.md](input/sources/03-signed-counts.md) — `P03`

> [N02] Tomas Reed independently signed COUNT-A-2 for the same 18:00 cutoff, same lot, and same boundary. The stated total is 147 units. The sheet expressly includes quarantine and the return cage. Reed has the same authority as Elin for this count. A margin note mentions a loose sleeve under a bin but does not state whether it was counted. That incomplete note cannot be used to rewrite the signed total. No signed reconciliation, recount, or authorized cancellation resolves the discrepancy. Both count sheets remain active evidence. Neither the order of their filenames nor the auditor's preferred arithmetic gives one count source priority over the other.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 708, "end_character": 1367, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "902b530d21257c2ef30042baaa46dbc1fd5d2d6e8576e8d8c18fdc3c1b8d28af", "artifact_directory": "extraction/D00005/attempt-91hpqtsz"}`.

- [input/sources/03-signed-counts.md](input/sources/03-signed-counts.md) — `P04`

> [N03] A separate B control sheet records 40 units physically inside the boundary, including its eight reserved units. It does not count C or D. Agreement between this B count and B journal arithmetic does not resolve the A discrepancy or the C import problem. No one signed a statement that all lots were reconciled. The A difference is one unit rather than a rounding difference because units are exact integers. A reviewer should distinguish a claim about what each signed sheet records from a claim selecting the true physical A total. The first can be well supported even when the second has conflicting evidence.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1369, "end_character": 1986, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "902b530d21257c2ef30042baaa46dbc1fd5d2d6e8576e8d8c18fdc3c1b8d28af", "artifact_directory": "extraction/D00005/attempt-91hpqtsz"}`.

- [input/sources/03-signed-counts.md](input/sources/03-signed-counts.md) — `P05`

> [N04] Count custody. The count sheets were transcribed into this source from synthetic signed forms and checked for matching lot, cutoff, and boundary labels. Their recorded signature names are evidence inside the invented exercise; no real-world handwriting examination is claimed. The transcriber was not authorized to correct observed quantities. The source does not establish which observer made a mistake or whether a sleeve moved during counting. A physical recount and a signed reconciliation would address that uncertainty. Until then, retaining both observations is more faithful than erasing a disagreeing one or deriving unrelated conclusions from inconsistent premises.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 1988, "end_character": 2669, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "902b530d21257c2ef30042baaa46dbc1fd5d2d6e8576e8d8c18fdc3c1b8d28af", "artifact_directory": "extraction/D00005/attempt-91hpqtsz"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P05`

> [R04] Evidence scope. Signed actual transfer receipts take precedence over unsigned planned quantities for determining completed custody movements. The journal and register are complete for A and B movements only within the stated day. No such completeness applies to D. Equal-authority physical counts of the same boundary and cutoff remain competing evidence unless a recount or authorized correction resolves them. A later filename does not give precedence. A pale or obscured numeral in a scan requires visual review and corroboration. An OCR guess is not a signed quantity. If available evidence does not establish a unique accepted amount, report the missing argument without inventing a number or asserting that the shipment necessarily failed.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2118, "end_character": 2869, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

- [input/sources/07-bin-and-exception-register.md](input/sources/07-bin-and-exception-register.md) — `P05`

> [BIN04] Exception ownership. Inventory reviewer Mira Cole opened unresolved exception EX-A for the one-unit disagreement between the signed A counts. She requested a recount but supplied no completed recount in this packet. Reviewer Leon Hart opened EX-C for the imported C journal deficit and requested the original unit mapping file. The request names a possible conversion issue but contains no approved correction amount. The two exceptions have different evidence needs: EX-A needs reconciliation of competing observations, while EX-C needs reconstruction of a possibly incorrect journal entry. Neither can be closed by adding unrelated B stock or by assuming a favorable D quantity.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 1955, "end_character": 2643, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "17864baef381443926666ff2acbb425f97ab919bb09877291086a640ba22e3f9", "artifact_directory": "extraction/D00009/attempt-2lly49hx"}`.

### Rules

- Use R01 exact full-container conversion, R02 actual custody movements and R03 same-lot availability where applicable.
- R04/K03 completeness covers A/B movements for the stated day only; equal-authority counts remain conflicting and missing D/C evidence is not negative fact.

### Assumptions

- The synthetic source authority and finite warehouse boundary are accepted as stated; no source authenticity outside the fixture is certified.

### Reasoning

- 1. Elin records 148 while Tomas records 147 for the identical lot, cutoff and included quarantine/cage.
- 2. Both have equal authority and neither is canceled. Agreement of the book calculation with one count does not adjudicate the other.

### Limits

- Results concern the specified lots, warehouse boundary and 18:00 cutoff on 14 April 2032. Book arithmetic does not select the true physical A count or resolve D acceptance.
- Formal checks prove encoded targets only; unsupported physical facts are not inferred from missing evidence.

### Result

Semantic state: **both**; argument status: **disputed**; formal status: **blocked**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Obtain a signed recount or authorized reconciliation; report both observations meanwhile.

## C08-ERR-10

### Exact report claim

`input/report.md#C08-ERR-10`

> **C08-ERR-10.** The physical C shortage is exactly one unit.

### Verification question

Does a minus-one C journal balance establish exactly one physically missing unit?

### Source evidence

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P05`

> [J04] C import anomaly. The imported C opening book balance is zero. At 10:10 an operator posted an outbound movement of nine units; at 10:20 an inbound movement of eight units was posted. The imported book balance is therefore minus one. This is a signed-integer ledger result, not a negative number of physical objects. An unsigned correction proposal mentions a possible carton-versus-unit import error, but no approved correction is supplied. Physical reconciliation for C is incomplete, and no physical count accompanies the journal. Preserve the anomaly and the missing correction argument. A book deficit alone does not prove a physical shortage, fraud, destruction, or a correct repair amount.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2086, "end_character": 2787, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-x0nfkf9z"}`.

- [input/sources/07-bin-and-exception-register.md](input/sources/07-bin-and-exception-register.md) — `P05`

> [BIN04] Exception ownership. Inventory reviewer Mira Cole opened unresolved exception EX-A for the one-unit disagreement between the signed A counts. She requested a recount but supplied no completed recount in this packet. Reviewer Leon Hart opened EX-C for the imported C journal deficit and requested the original unit mapping file. The request names a possible conversion issue but contains no approved correction amount. The two exceptions have different evidence needs: EX-A needs reconciliation of competing observations, while EX-C needs reconstruction of a possibly incorrect journal entry. Neither can be closed by adding unrelated B stock or by assuming a favorable D quantity.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 1955, "end_character": 2643, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "17864baef381443926666ff2acbb425f97ab919bb09877291086a640ba22e3f9", "artifact_directory": "extraction/D00009/attempt-2lly49hx"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P04`

> [R03] Lot identity and availability. Lots A, B, C, and D are separate even though their sleeves share a catalog description. An excess in one lot cannot repair a deficit in another. Available stock is book on-hand minus quarantined units minus separately reserved units, with no overlapping deductions. The A quarantine contains seven units. The B reservation contains eight different units. Quarantine and reservation change internal status without transferring custody. Physical presence, book balance, and available quantity are different predicates. A physical count may disagree with a journal-derived balance, and the disagreement must remain visible rather than silently redefining one quantity to match the other.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1395, "end_character": 2116, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

### Rules

- Use R01 exact full-container conversion, R02 actual custody movements and R03 same-lot availability where applicable.
- R04/K03 completeness covers A/B movements for the stated day only; equal-authority counts remain conflicting and missing D/C evidence is not negative fact.

### Assumptions

- The synthetic source authority and finite warehouse boundary are accepted as stated; no source authenticity outside the fixture is certified.

### Reasoning

- 1. The signed-integer ledger is 0 - 9 + 8 = -1.
- 2. J04 expressly lacks a physical count and approved import correction. A possible unit-mapping error is unresolved. The missing bridge from book anomaly to physical shortage prevents either a one-unit shortage finding or its negation.

### Limits

- Results concern the specified lots, warehouse boundary and 18:00 cutoff on 14 April 2032. Book arithmetic does not select the true physical A count or resolve D acceptance.
- Formal checks prove encoded targets only; unsupported physical facts are not inferred from missing evidence.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **blocked**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Report the -1 book anomaly; request the unit mapping, approved correction and physical reconciliation.

## C08-ERR-11

### Exact report claim

`input/report.md#C08-ERR-11`

> **C08-ERR-11.** Exactly 78 D units were accepted by the receiver, conclusively established by the scanned line.

### Verification question

Does the pale D field conclusively establish that exactly 78 units were accepted?

### Source evidence

- [input/sources/06-shipping-tickets-scan.pdf.md](input/sources/06-shipping-tickets-scan.pdf.md) — `pdf-page-0005`

> SYNTHETIC NORTH QUAY SHIPPING FORM
> [T@5] Movement D-17; 14 April 2032; clock 13:30; lot D
> Quantity boxes: Quantity requires reading of the pale field. Status: Carrier initials
> only; receiver acceptance blank.
> The numerical field is pale. A receiver proposes 74 in an unsigned message, while a
> carrier message proposes 78. Neither is a jointly signed correction. The ticket
> identity and lot remain legible, so the uncertainty concerns the quantity and
> completed acceptance. A guessed numeral cannot supply a missing receiver signature or
> settle the competing quantities.
> [T05-CHAIN] This form belongs to the registered source packet. The warehouse boundary
> includes W1, W2, and the fenced return cage. Read planned quantities separately from
> actual signed handoffs. Standard full-container quantities follow the supplied stock
> rules. Carrier custody is distinct from customer delivery. Preserve lot identity in
> every calculation; quantities from another lot cannot repair this form. Any partial-
> container notation would override the standard full conversion. A source quotation
> should retain this original PDF path and marker rather than presenting an OCR excerpt
> as an independently signed record.
> [T@5-LIMIT] The form supports only its named movement and stages. It does not certify
> all warehouse inventory or resolve independent physical count differences. A
> signature name is an invented evidence field within this exercise, not a claim about
> real handwriting authentication. Missing attachments must remain missing in the audit
> reasoning. Reviewers should explain how the movement changes the relevant balance
> before relying on an aggregate total.

Original: [input/originals/D00008.pdf](input/originals/D00008.pdf); extraction: tesseract-tsv.
Coordinates: `{"kind": "ocr", "page": 5, "origin": {"format": "pdf", "page": 5, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0005-raster.png", "tsv_artifact": "pdf-page-0005.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.48176571369294, "minimum_word_confidence": 3.835678, "confidence_threshold": 85.0, "low_confidence_words": 4, "word_count": 241, "original": "input/originals/D00008.pdf", "original_sha256": "e64921cc43741a187a1063655d55e820e43a91c3f6152d0671af4fce81f7fe58", "artifact_directory": "extraction/D00008/attempt-5bvezmai"}`.

Extraction uncertainty: OCR is a probabilistic transcription; quote matching verifies the recognized text only. Visually compare every material quotation with the original image.; Low-confidence words: 4; review original bounding boxes before relying on text.

- [input/sources/04-receiving-messages.md](input/sources/04-receiving-messages.md) — `P02`

> [M01] The unresolved D transfer. A receiver message tentatively proposes 74 units for transfer D-17, but it is unsigned and marked provisional. A carrier message says that the faint copy looks like 78. Neither is a signed correction. The original scanned quantity line is pale, and its second digit is hard to read. No customer acceptance signature appears beside that quantity. There is no original carbon copy or later authenticated reconciliation in the packet. The two interpretations are not a license to select the convenient value. Even a legible planned quantity would not automatically establish the quantity actually accepted by the receiver.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 38, "end_character": 690, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "5902f74c3a28ac0e3f3d0e49dc8503a2d0417d6a3658bde4c64ba768051d0c17", "artifact_directory": "extraction/D00006/attempt-noaji46d"}`.

- [input/sources/04-receiving-messages.md](input/sources/04-receiving-messages.md) — `P05`

> [M04] Missing supporting material. An email index lists next-day D recount photographs, but no photographs or recount attachment are supplied. The index proves the existence of the listing, not the content or result of the absent attachment. Vehicle photographs mentioned by the carrier are likewise unavailable. A useful finding identifies precisely which missing record could resolve the uncertain quantity. Missing evidence does not itself establish that the carrier short-shipped, that the customer miscounted, or that the document was forged. No external retrieval is authorized by this finite packet; an audit should retain the bounded evidence gap.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2034, "end_character": 2689, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "5902f74c3a28ac0e3f3d0e49dc8503a2d0417d6a3658bde4c64ba768051d0c17", "artifact_directory": "extraction/D00006/attempt-noaji46d"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P05`

> [R04] Evidence scope. Signed actual transfer receipts take precedence over unsigned planned quantities for determining completed custody movements. The journal and register are complete for A and B movements only within the stated day. No such completeness applies to D. Equal-authority physical counts of the same boundary and cutoff remain competing evidence unless a recount or authorized correction resolves them. A later filename does not give precedence. A pale or obscured numeral in a scan requires visual review and corroboration. An OCR guess is not a signed quantity. If available evidence does not establish a unique accepted amount, report the missing argument without inventing a number or asserting that the shipment necessarily failed.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2118, "end_character": 2869, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

- [input/sources/05-custody-register.md](input/sources/05-custody-register.md) — `P05`

> [K04] Handling disputed quantities. If an auditor cannot confidently read a numerical field, the next step is to inspect the image and the supplied corroborating records, not to convert OCR confidence into physical certainty. A faithful result may identify the likely reading while withholding a claim about accepted quantity. Competing unsigned messages do not have the authority of a completed receipt signed by both parties. This distinction also applies when a document contains a clear planned number but an incomplete actual handoff box. The field's semantic role, signature status, and custody stage matter as much as its digits.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2040, "end_character": 2676, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "54ba3d90c6fd73c04b139b20f2cc369e144f6050697949c27f883d4209ad2830", "artifact_directory": "extraction/D00007/attempt-ly8ukxxe"}`.

- [input/sources/07-bin-and-exception-register.md](input/sources/07-bin-and-exception-register.md) — `P06`

> [BIN05] D evidence request. The receiving coordinator requested an authenticated copy of the D acceptance box and the missing next-day recount attachment. The response log records those requests as outstanding at the cutoff used for this packet. It does not establish whether the documents exist elsewhere or what they would say. The coordinator retained both tentative quantity messages rather than promoting either into a signed actual receipt. A visual reading of the pale printed number can clarify what appears on the form, but it cannot by itself establish customer acceptance. Any later closure must identify the newly supplied evidence, its authority, and the exact quantity it resolves.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 11, "start_character": 2645, "end_character": 3340, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "17864baef381443926666ff2acbb425f97ab919bb09877291086a640ba22e3f9", "artifact_directory": "extraction/D00009/attempt-2lly49hx"}`.

### Rules

- Use R01 exact full-container conversion, R02 actual custody movements and R03 same-lot availability where applicable.
- R04/K03 completeness covers A/B movements for the stated day only; equal-authority counts remain conflicting and missing D/C evidence is not negative fact.

### Assumptions

- The synthetic source authority and finite warehouse boundary are accepted as stated; no source authenticity outside the fixture is certified.

### Reasoning

- 1. All five original raster pages were inspected. The pale final line on page 5 visually appears to read 78, but OCR omitted it; the receiver acceptance box is blank.
- 2. M01 provides provisional unsigned 74 and 78 suggestions, no signed correction or authenticated reconciliation. Even perfect legibility of a planned field would not establish actual accepted quantity.
- 3. No unique accepted D quantity is established, and the absence of acceptance evidence does not prove the shipment failed.

### Limits

- Results concern the specified lots, warehouse boundary and 18:00 cutoff on 14 April 2032. Book arithmetic does not select the true physical A count or resolve D acceptance.
- Native pages 1–4 were visually checked and corrected through retained manual transcriptions; page 5 retains quantity/acceptance uncertainty.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **blocked**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Request authenticated acceptance/correction and the missing recount attachment; keep accepted quantity undetermined.

## C08-ERR-12

### Exact report claim

`input/report.md#C08-ERR-12`

> **C08-ERR-12.** Every warehouse lot was reconciled at cutoff.

### Verification question

Was every warehouse lot reconciled at cutoff, including C and the unresolved A count?

### Source evidence

- [input/sources/05-custody-register.md](input/sources/05-custody-register.md) — `P04`

> [K03] Bounded completeness. The register and journal list all accepted A and B movements for the stated day. This permits absence of further A or B movements to be used in exact book arithmetic. It does not establish complete D custody, complete C physical reconciliation, or complete warehouse activity over other dates. The A physical count conflict remains unresolved despite complete movement records. Completeness of one evidence type is not an assertion that every other evidence type agrees. A report that says every lot was reconciled therefore needs an argument beyond the limited A/B movement inventory and must confront the explicit unresolved cases.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1377, "end_character": 2038, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "54ba3d90c6fd73c04b139b20f2cc369e144f6050697949c27f883d4209ad2830", "artifact_directory": "extraction/D00007/attempt-ly8ukxxe"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P05`

> [J04] C import anomaly. The imported C opening book balance is zero. At 10:10 an operator posted an outbound movement of nine units; at 10:20 an inbound movement of eight units was posted. The imported book balance is therefore minus one. This is a signed-integer ledger result, not a negative number of physical objects. An unsigned correction proposal mentions a possible carton-versus-unit import error, but no approved correction is supplied. Physical reconciliation for C is incomplete, and no physical count accompanies the journal. Preserve the anomaly and the missing correction argument. A book deficit alone does not prove a physical shortage, fraud, destruction, or a correct repair amount.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2086, "end_character": 2787, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-x0nfkf9z"}`.

- [input/sources/03-signed-counts.md](input/sources/03-signed-counts.md) — `P03`

> [N02] Tomas Reed independently signed COUNT-A-2 for the same 18:00 cutoff, same lot, and same boundary. The stated total is 147 units. The sheet expressly includes quarantine and the return cage. Reed has the same authority as Elin for this count. A margin note mentions a loose sleeve under a bin but does not state whether it was counted. That incomplete note cannot be used to rewrite the signed total. No signed reconciliation, recount, or authorized cancellation resolves the discrepancy. Both count sheets remain active evidence. Neither the order of their filenames nor the auditor's preferred arithmetic gives one count source priority over the other.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 708, "end_character": 1367, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "902b530d21257c2ef30042baaa46dbc1fd5d2d6e8576e8d8c18fdc3c1b8d28af", "artifact_directory": "extraction/D00005/attempt-91hpqtsz"}`.

- [input/sources/07-bin-and-exception-register.md](input/sources/07-bin-and-exception-register.md) — `P05`

> [BIN04] Exception ownership. Inventory reviewer Mira Cole opened unresolved exception EX-A for the one-unit disagreement between the signed A counts. She requested a recount but supplied no completed recount in this packet. Reviewer Leon Hart opened EX-C for the imported C journal deficit and requested the original unit mapping file. The request names a possible conversion issue but contains no approved correction amount. The two exceptions have different evidence needs: EX-A needs reconciliation of competing observations, while EX-C needs reconstruction of a possibly incorrect journal entry. Neither can be closed by adding unrelated B stock or by assuming a favorable D quantity.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 1955, "end_character": 2643, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "17864baef381443926666ff2acbb425f97ab919bb09877291086a640ba22e3f9", "artifact_directory": "extraction/D00009/attempt-2lly49hx"}`.

### Rules

- Use R01 exact full-container conversion, R02 actual custody movements and R03 same-lot availability where applicable.
- R04/K03 completeness covers A/B movements for the stated day only; equal-authority counts remain conflicting and missing D/C evidence is not negative fact.

### Assumptions

- The synthetic source authority and finite warehouse boundary are accepted as stated; no source authenticity outside the fixture is certified.

### Reasoning

- 1. J04 explicitly states C physical reconciliation is incomplete; BIN04 records its unresolved exception.
- 2. C belongs to the named lot domain and is a direct counterexample to every-lot reconciliation. The unresolved A count independently defeats blanket closure.

### Limits

- Results concern the specified lots, warehouse boundary and 18:00 cutoff on 14 April 2032. Book arithmetic does not select the true physical A count or resolve D acceptance.
- Formal checks prove encoded targets only; unsupported physical facts are not inferred from missing evidence.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim12` in module `Audit` (refutes): `∀ (reconciled : Audit.Lot → Prop), ¬ reconciled Audit.Lot.c → ¬ (∀ lot, reconciled lot)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target019.lean) · [Actual proof log](logs/target-019.log)

### Recommendation

Withdraw the universal statement and list unresolved A, C and D questions separately.

## C08-ERR-13

### Exact report claim

`input/report.md#C08-ERR-13`

> **C08-ERR-13.** Subtracting the A quarantine from B stock gives B availability.

### Verification question

Does subtracting A quarantine from B book stock yield B availability?

### Source evidence

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P04`

> [R03] Lot identity and availability. Lots A, B, C, and D are separate even though their sleeves share a catalog description. An excess in one lot cannot repair a deficit in another. Available stock is book on-hand minus quarantined units minus separately reserved units, with no overlapping deductions. The A quarantine contains seven units. The B reservation contains eight different units. Quarantine and reservation change internal status without transferring custody. Physical presence, book balance, and available quantity are different predicates. A physical count may disagree with a journal-derived balance, and the disagreement must remain visible rather than silently redefining one quantity to match the other.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1395, "end_character": 2116, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P04`

> [J03] B request and actual handoff. OUT-B requested three cartons, but the signed carrier handoff at 12:00 records two full cartons. The remaining carton stayed on shelf B4 because its packaging label was missing. At 15:00 that unfilled order quantity was canceled. It never crossed the warehouse boundary. A separate next-day order reserved eight other B units, distinct from both the dispatched cartons and the canceled request. There was no B return and no need to invent one: the canceled quantity never left. The A quarantine affects no B stock. The B journal contains no other completed inbound, outbound, or return movements within the cutoff interval.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1425, "end_character": 2084, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-x0nfkf9z"}`.

- [input/sources/07-bin-and-exception-register.md](input/sources/07-bin-and-exception-register.md) — `P03`

> [BIN02] Quarantine ticket Q-A-7. At 17:00 Elin attached a hold label to seven loose A units on shelf A1 after noticing cosmetic sleeve marks. The ticket states that those seven units remain physically in W1 and are excluded from availability pending review. It does not order disposal, destruction, shipment, or a transfer to another lot. The label applies to individual units, not seven crates. No later release from quarantine occurred before cutoff. The physical count sheets both expressly included the held units. The record supports a status deduction from available A stock without decrementing A book on-hand.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 712, "end_character": 1329, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "17864baef381443926666ff2acbb425f97ab919bb09877291086a640ba22e3f9", "artifact_directory": "extraction/D00009/attempt-2lly49hx"}`.

- [input/sources/07-bin-and-exception-register.md](input/sources/07-bin-and-exception-register.md) — `P04`

> [BIN03] Reservation ticket RES-B-8. The next-day customer order reserves eight B units located on shelf B2. The units were not among the two cartons loaded for OUT-B and were not the canceled third carton on B4. The reservation was still active at cutoff. The operator may not release those units to another order without canceling or changing the reservation record, but no such change occurred that day. These facts justify treating the reservation as a distinct deduction when calculating available B stock. They do not establish an outbound movement, a customer delivery, or physical absence from the B count boundary.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1331, "end_character": 1953, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "17864baef381443926666ff2acbb425f97ab919bb09877291086a640ba22e3f9", "artifact_directory": "extraction/D00009/attempt-2lly49hx"}`.

### Rules

- Use R01 exact full-container conversion, R02 actual custody movements and R03 same-lot availability where applicable.
- R04/K03 completeness covers A/B movements for the stated day only; equal-authority counts remain conflicting and missing D/C evidence is not negative fact.

### Assumptions

- The synthetic source authority and finite warehouse boundary are accepted as stated; no source authenticity outside the fixture is certified.

### Reasoning

- 1. Lots are distinct; A holds seven quarantined units and B separately reserves eight different units.
- 2. B availability is 40 - 8 = 32. The proposed cross-lot subtraction 40 - 7 = 33 differs, and violates the lot-identity rule.

### Limits

- Results concern the specified lots, warehouse boundary and 18:00 cutoff on 14 April 2032. Book arithmetic does not select the true physical A count or resolve D acceptance.
- Formal checks prove encoded targets only; unsupported physical facts are not inferred from missing evidence.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim13` in module `Audit` (refutes): `Audit.bookB - 7 ≠ Audit.availableB`.
  [Model](models/Audit.lean) · [Executed check](checks/Target020.lean) · [Actual proof log](logs/target-020.log)

### Recommendation

Deduct B's own eight reserved units; keep A quarantine assigned to A.

## C08-ERR-14

### Exact report claim

`input/report.md#C08-ERR-14`

> **C08-ERR-14.** The return workflow is elegantly designed.

### Verification question

Is there a supplied operational definition that can decide whether the return workflow is elegantly designed?

### Source evidence

- [input/sources/05-custody-register.md](input/sources/05-custody-register.md) — `P02`

> [K01] Roles. Elin Shore may accept inbound movements and returns at North Quay. Jun Vale may accept carrier custody but cannot amend warehouse physical counts. Tomas Reed may perform an independent count but cannot retroactively alter a transfer quantity without an authorized countersigned correction. These assignments apply only to this invented day. A correct signature identity is one part of the evidence: the document must still identify the lot, movement, time, and actual quantity. A carrier signature is not a customer delivery signature. Similarly, an order clerk signature can approve a request without establishing that the requested goods physically left.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 41, "end_character": 710, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "54ba3d90c6fd73c04b139b20f2cc369e144f6050697949c27f883d4209ad2830", "artifact_directory": "extraction/D00007/attempt-ly8ukxxe"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P03`

> [R02] Movement semantics. Opening stock plus accepted inbound movements minus completed outbound movements plus accepted returns determines book on-hand. A printed ticket, order, reservation, or pick request changes no physical inventory merely by existing. Departure occurs at the signed actual custody handoff across the boundary. Customer delivery is a separate later event. A carrier can hold inventory that has already departed but is not yet delivered. Return increases on-hand when the receiving custodian accepts the goods back across the boundary. Returned goods in the fenced cage are inside the boundary even before reshelving. An accepted return is a separate movement, not a reason to erase the original departure.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 666, "end_character": 1393, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-f44k0ga1"}`.

### Rules

- No source defines an objective criterion for elegance.

### Assumptions

- The synthetic source authority and finite warehouse boundary are accepted as stated; no source authenticity outside the fixture is certified.

### Reasoning

- 1. K01 assigns custody roles and R02 defines movement semantics.
- 2. Neither provides a criterion for elegance. Operational correctness or traceability does not mathematically establish an aesthetic judgment.

### Limits

- Results concern the specified lots, warehouse boundary and 18:00 cutoff on 14 April 2032. Book arithmetic does not select the true physical A count or resolve D acceptance.
- Formal checks prove encoded targets only; unsupported physical facts are not inferred from missing evidence.

### Result

Semantic state: **not_applicable**; argument status: **nonformal**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Label elegance as an opinion or supply an agreed assessment criterion.
