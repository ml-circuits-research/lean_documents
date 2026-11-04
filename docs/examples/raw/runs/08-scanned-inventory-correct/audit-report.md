# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

[Semantic correspondence review](semantic-review.md)

Extraction inventory: 9 documents; 1 pending, partial or blocked. See [ingestion details](ingestion.json) and [coverage](coverage.md).

## C08-OK-01

### Exact report claim

`input/report.md#C08-OK-01`

> **C08-OK-01.** Lot A accepted inbound quantity was 96 units.
> 
> Citations: sources/06-shipping-tickets-scan.pdf#[T01]; sources/01-stock-rules.md#[R01].

### Verification question

Did the accepted Lot A inbound movement contain exactly 96 individual units?

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
Coordinates: `{"kind": "ocr", "page": 1, "origin": {"format": "pdf", "page": 1, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0001-raster.png", "tsv_artifact": "pdf-page-0001.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.25485498297871, "minimum_word_confidence": 45.506126, "confidence_threshold": 85.0, "low_confidence_words": 5, "word_count": 235, "original": "input/originals/D00008.pdf", "original_sha256": "e64921cc43741a187a1063655d55e820e43a91c3f6152d0671af4fce81f7fe58", "artifact_directory": "extraction/D00008/attempt-5dzca71r", "source_anchor": "pdf-page-0001", "root_source_anchor": "pdf-page-0001", "reviewer": "audit_01m", "reason": "Actually inspected original scan page 1 raster with view_image. Corrected visible T01 and CHAIN/LIMIT marker characters, time characters and terminal lot punctuation as needed. Full/crate/carton counts, signed custody stage and negations were compared with the original.", "reviewed_at": "2026-11-04T15:16:58.267861+00:00", "transcription_snapshot": "input/manual-transcriptions/D00008/27a8dd0b9c08462610f0237b36aebddc5203fb42d149a2cf510126e2ed638151.txt", "transcription_file_sha256": "72e3f904601c4f0cb37fa5e793512cff0066e4cfcec41fbcb65926e95cba5a26", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P02`

> [R01] Unit definitions and boundary. The inventory boundary consists of rooms W1 and W2 and the fenced return cage at the invented North Quay warehouse. The cutoff is 18:00 on 14 April 2032. All quantities are exact integer individual sleeves, called units. A sealed full crate contains twelve units. A sealed full carton contains six units. A pallet has no fixed conversion. A partial-container label overrides the standard full-container quantity; an empty container contributes zero. All names and transactions in this packet are invented. These rules define the finite exercise and do not prescribe real shipping procedures.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 664, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P03`

> [R02] Movement semantics. Opening stock plus accepted inbound movements minus completed outbound movements plus accepted returns determines book on-hand. A printed ticket, order, reservation, or pick request changes no physical inventory merely by existing. Departure occurs at the signed actual custody handoff across the boundary. Customer delivery is a separate later event. A carrier can hold inventory that has already departed but is not yet delivered. Return increases on-hand when the receiving custodian accepts the goods back across the boundary. Returned goods in the fenced cage are inside the boundary even before reshelving. An accepted return is a separate movement, not a reason to erase the original departure.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 666, "end_character": 1393, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P02`

> [J01] Opening and receipts. At 08:00 lot A opened with 100 units and lot B with 40 units. At 09:00 receipt IN-A accepted eight sealed full crates of A. At 09:30 receipt IN-B accepted two sealed full cartons of B. Clerk Elin Shore accepted custody at the gate. Each container was confirmed full, without a partial notation. These are posted accepted receipts, not expected procurement deliveries. No other opening adjustment or accepted inbound movement for A or B occurred before cutoff. The completeness statement is restricted to the named interval and lots. It does not establish any opening quantity for D or repair the C import anomaly.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 51, "end_character": 692, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-dbfkr6yd"}`.

- [input/sources/05-custody-register.md](input/sources/05-custody-register.md) — `P02`

> [K01] Roles. Elin Shore may accept inbound movements and returns at North Quay. Jun Vale may accept carrier custody but cannot amend warehouse physical counts. Tomas Reed may perform an independent count but cannot retroactively alter a transfer quantity without an authorized countersigned correction. These assignments apply only to this invented day. A correct signature identity is one part of the evidence: the document must still identify the lot, movement, time, and actual quantity. A carrier signature is not a customer delivery signature. Similarly, an order clerk signature can approve a request without establishing that the requested goods physically left.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 41, "end_character": 710, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "54ba3d90c6fd73c04b139b20f2cc369e144f6050697949c27f883d4209ad2830", "artifact_directory": "extraction/D00007/attempt-c0z4297u"}`.

### Rules

- R01 assigns twelve units to a sealed full crate. R02 counts accepted custody, not an expected order; K01 authorizes Elin to receive.

### Assumptions

- Use the supplied synthetic day, lot identities and exact individual-unit conversions. Accept the explicitly complete A/B movement journal only for its named boundary and interval.
- The legible material scan fields were actually viewed and corroborated; manual reviewed anchors preserve original-source hashes and raw OCR. No real handwriting authentication or external event inspection is claimed.

### Reasoning

- 1. Visually inspected T01 records eight sealed full A crates accepted by Elin at 09:00, with no partial/damaged/empty override. J01 independently records the posted accepted receipt.
- 2. Eight times twelve gives 96 units, preserving crate factor and lotA identity.
- 3. The source proves a completed inbound movement within this synthetic journal, not mere planned procurement.

### Limits

- The result concerns this named accepted movement only, not all physical stock or unrelated lotD.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim01` in module `Audit` (supports): `Audit.inboundA = 96`.
  [Model](models/Audit.lean) · [Executed check](checks/Target015.lean) · [Actual proof log](logs/target-015.log)

### Recommendation

Retain the 96-unit accepted inbound finding and original scan marker T01.

## C08-OK-02

### Exact report claim

`input/report.md#C08-OK-02`

> **C08-OK-02.** Lot B accepted inbound quantity was 12 units.
> 
> Citations: sources/06-shipping-tickets-scan.pdf#[T02]; sources/01-stock-rules.md#[R01].

### Verification question

Did the accepted Lot B inbound movement contain exactly 12 units, using carton rather than crate conversion?

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
Coordinates: `{"kind": "ocr", "page": 2, "origin": {"format": "pdf", "page": 2, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0002-raster.png", "tsv_artifact": "pdf-page-0002.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 94.90358588559322, "minimum_word_confidence": 8.591576, "confidence_threshold": 85.0, "low_confidence_words": 4, "word_count": 236, "original": "input/originals/D00008.pdf", "original_sha256": "e64921cc43741a187a1063655d55e820e43a91c3f6152d0671af4fce81f7fe58", "artifact_directory": "extraction/D00008/attempt-5dzca71r", "source_anchor": "pdf-page-0002", "root_source_anchor": "pdf-page-0002", "reviewer": "audit_01m", "reason": "Actually inspected original scan page 2 raster with view_image. Corrected visible T02 and CHAIN/LIMIT marker characters, time characters and terminal lot punctuation as needed. Full/crate/carton counts, signed custody stage and negations were compared with the original.", "reviewed_at": "2026-11-04T15:16:58.371557+00:00", "transcription_snapshot": "input/manual-transcriptions/D00008/f2c73ff169fa72a87f8a86ce29319fba80b81b376e3a4b6229800b78686ff70a.txt", "transcription_file_sha256": "62466a0a4466eabee04c4d14d61bc57708d7a1914a5dd71fb33fc3cfbd93898d", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P02`

> [R01] Unit definitions and boundary. The inventory boundary consists of rooms W1 and W2 and the fenced return cage at the invented North Quay warehouse. The cutoff is 18:00 on 14 April 2032. All quantities are exact integer individual sleeves, called units. A sealed full crate contains twelve units. A sealed full carton contains six units. A pallet has no fixed conversion. A partial-container label overrides the standard full-container quantity; an empty container contributes zero. All names and transactions in this packet are invented. These rules define the finite exercise and do not prescribe real shipping procedures.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 664, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P02`

> [J01] Opening and receipts. At 08:00 lot A opened with 100 units and lot B with 40 units. At 09:00 receipt IN-A accepted eight sealed full crates of A. At 09:30 receipt IN-B accepted two sealed full cartons of B. Clerk Elin Shore accepted custody at the gate. Each container was confirmed full, without a partial notation. These are posted accepted receipts, not expected procurement deliveries. No other opening adjustment or accepted inbound movement for A or B occurred before cutoff. The completeness statement is restricted to the named interval and lots. It does not establish any opening quantity for D or repair the C import anomaly.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 51, "end_character": 692, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-dbfkr6yd"}`.

- [input/sources/05-custody-register.md](input/sources/05-custody-register.md) — `P02`

> [K01] Roles. Elin Shore may accept inbound movements and returns at North Quay. Jun Vale may accept carrier custody but cannot amend warehouse physical counts. Tomas Reed may perform an independent count but cannot retroactively alter a transfer quantity without an authorized countersigned correction. These assignments apply only to this invented day. A correct signature identity is one part of the evidence: the document must still identify the lot, movement, time, and actual quantity. A carrier signature is not a customer delivery signature. Similarly, an order clerk signature can approve a request without establishing that the requested goods physically left.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 41, "end_character": 710, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "54ba3d90c6fd73c04b139b20f2cc369e144f6050697949c27f883d4209ad2830", "artifact_directory": "extraction/D00007/attempt-c0z4297u"}`.

### Rules

- A sealed full carton is six units under R01; lot identity and container type control.

### Assumptions

- Use the supplied synthetic day, lot identities and exact individual-unit conversions. Accept the explicitly complete A/B movement journal only for its named boundary and interval.
- The legible material scan fields were actually viewed and corroborated; manual reviewed anchors preserve original-source hashes and raw OCR. No real handwriting authentication or external event inspection is claimed.

### Reasoning

- 1. T02 visually records two sealed full B cartons accepted by Elin, confirmed by J01; no partial override appears.
- 2. Two times six equals 12. Applying twelve-unit crate conversion would misread the source container type.

### Limits

- This receipt is distinct from the separate eight-unit next-day reservation.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim02` in module `Audit` (supports): `Audit.inboundB = 12`.
  [Model](models/Audit.lean) · [Executed check](checks/Target016.lean) · [Actual proof log](logs/target-016.log)

### Recommendation

Retain 12 accepted B units and identify the six-unit carton factor.

## C08-OK-03

### Exact report claim

`input/report.md#C08-OK-03`

> **C08-OK-03.** Lot A book on-hand at cutoff was 148 units.
> 
> Citations: sources/02-opening-and-journal.md#[J01]; sources/02-opening-and-journal.md#[J02]; sources/01-stock-rules.md#[R02].

### Verification question

Does the complete A movement journal produce 148 book on-hand units at 18:00 on April 14?

### Source evidence

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P03`

> [R02] Movement semantics. Opening stock plus accepted inbound movements minus completed outbound movements plus accepted returns determines book on-hand. A printed ticket, order, reservation, or pick request changes no physical inventory merely by existing. Departure occurs at the signed actual custody handoff across the boundary. Customer delivery is a separate later event. A carrier can hold inventory that has already departed but is not yet delivered. Return increases on-hand when the receiving custodian accepts the goods back across the boundary. Returned goods in the fenced cage are inside the boundary even before reshelving. An accepted return is a separate movement, not a reason to erase the original departure.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 666, "end_character": 1393, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P05`

> [R04] Evidence scope. Signed actual transfer receipts take precedence over unsigned planned quantities for determining completed custody movements. The journal and register are complete for A and B movements only within the stated day. No such completeness applies to D. Equal-authority physical counts of the same boundary and cutoff remain competing evidence unless a recount or authorized correction resolves them. A later filename does not give precedence. A pale or obscured numeral in a scan requires visual review and corroboration. An OCR guess is not a signed quantity. If available evidence does not establish a unique accepted amount, report the missing argument without inventing a number or asserting that the shipment necessarily failed.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2118, "end_character": 2869, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P02`

> [J01] Opening and receipts. At 08:00 lot A opened with 100 units and lot B with 40 units. At 09:00 receipt IN-A accepted eight sealed full crates of A. At 09:30 receipt IN-B accepted two sealed full cartons of B. Clerk Elin Shore accepted custody at the gate. Each container was confirmed full, without a partial notation. These are posted accepted receipts, not expected procurement deliveries. No other opening adjustment or accepted inbound movement for A or B occurred before cutoff. The completeness statement is restricted to the named interval and lots. It does not establish any opening quantity for D or repair the C import anomaly.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 51, "end_character": 692, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-dbfkr6yd"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P03`

> [J02] A departure, delivery, and return. OUT-A at 11:00 transferred five full crates to carrier Jun Vale. The customer accepted four crates and declined the fifth. At 16:00 Jun returned the still-sealed fifth crate; Elin accepted it inside the fenced return cage. The entire five-crate departure remains recorded, followed by the separate one-crate return. There were no other A departures or returns that day. At 17:00 seven units already on a W1 shelf were quarantined. They remained inside the inventory boundary. A reviewer must therefore distinguish dispatched quantity, delivered quantity, returned quantity, on-hand, and available stock. None of these labels can be substituted merely because they refer to the same order.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 694, "end_character": 1423, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-dbfkr6yd"}`.

- [input/sources/05-custody-register.md](input/sources/05-custody-register.md) — `P04`

> [K03] Bounded completeness. The register and journal list all accepted A and B movements for the stated day. This permits absence of further A or B movements to be used in exact book arithmetic. It does not establish complete D custody, complete C physical reconciliation, or complete warehouse activity over other dates. The A physical count conflict remains unresolved despite complete movement records. Completeness of one evidence type is not an assertion that every other evidence type agrees. A report that says every lot was reconciled therefore needs an argument beyond the limited A/B movement inventory and must confront the explicit unresolved cases.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1377, "end_character": 2038, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "54ba3d90c6fd73c04b139b20f2cc369e144f6050697949c27f883d4209ad2830", "artifact_directory": "extraction/D00007/attempt-c0z4297u"}`.

- [input/sources/07-bin-and-exception-register.md](input/sources/07-bin-and-exception-register.md) — `P02`

> [BIN01] Shelf trace. The opening A stock occupied shelves A1 and A2. The eight received crates were placed on A3 after acceptance at the gate. The five outbound crates were selected from the received containers and opening full-container stock, but that selection does not change lot identity or the aggregate arithmetic. The returned crate was placed in cage position R2 and remained there until cutoff. The movement from gate to shelf, or from gate to the internal cage, is an internal relocation after acceptance. It must not create a second receipt. The bin register therefore uses location changes as custody context rather than additive inventory movements.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 47, "end_character": 710, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "17864baef381443926666ff2acbb425f97ab919bb09877291086a640ba22e3f9", "artifact_directory": "extraction/D00009/attempt-4g00o254"}`.

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
Coordinates: `{"kind": "ocr", "page": 1, "origin": {"format": "pdf", "page": 1, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0001-raster.png", "tsv_artifact": "pdf-page-0001.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.25485498297871, "minimum_word_confidence": 45.506126, "confidence_threshold": 85.0, "low_confidence_words": 5, "word_count": 235, "original": "input/originals/D00008.pdf", "original_sha256": "e64921cc43741a187a1063655d55e820e43a91c3f6152d0671af4fce81f7fe58", "artifact_directory": "extraction/D00008/attempt-5dzca71r", "source_anchor": "pdf-page-0001", "root_source_anchor": "pdf-page-0001", "reviewer": "audit_01m", "reason": "Actually inspected original scan page 1 raster with view_image. Corrected visible T01 and CHAIN/LIMIT marker characters, time characters and terminal lot punctuation as needed. Full/crate/carton counts, signed custody stage and negations were compared with the original.", "reviewed_at": "2026-11-04T15:16:58.267861+00:00", "transcription_snapshot": "input/manual-transcriptions/D00008/27a8dd0b9c08462610f0237b36aebddc5203fb42d149a2cf510126e2ed638151.txt", "transcription_file_sha256": "72e3f904601c4f0cb37fa5e793512cff0066e4cfcec41fbcb65926e95cba5a26", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

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
Coordinates: `{"kind": "ocr", "page": 3, "origin": {"format": "pdf", "page": 3, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0003-raster.png", "tsv_artifact": "pdf-page-0003.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.59391616867471, "minimum_word_confidence": 44.648014, "confidence_threshold": 85.0, "low_confidence_words": 3, "word_count": 249, "original": "input/originals/D00008.pdf", "original_sha256": "e64921cc43741a187a1063655d55e820e43a91c3f6152d0671af4fce81f7fe58", "artifact_directory": "extraction/D00008/attempt-5dzca71r", "source_anchor": "pdf-page-0003", "root_source_anchor": "pdf-page-0003", "reviewer": "audit_01m", "reason": "Actually inspected original scan page 3 raster with view_image. Corrected visible T03 and CHAIN/LIMIT marker characters, time characters and terminal lot punctuation as needed. Full/crate/carton counts, signed custody stage and negations were compared with the original.", "reviewed_at": "2026-11-04T15:16:58.474217+00:00", "transcription_snapshot": "input/manual-transcriptions/D00008/74d057c1ffd7a573949b5264432bbf95d0ac166f21a1a683072c9f16d09c7d65.txt", "transcription_file_sha256": "8cb046c528b21f24a3e2768bfed2e1a4d71a489c47e9007ea0be72fbf2bfc611", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

### Rules

- Book on-hand is opening plus accepted inbound minus actual departure plus accepted return. K03/R04 bound movement completeness to A/B that day; cage acceptance is inside the boundary.

### Assumptions

- Use the supplied synthetic day, lot identities and exact individual-unit conversions. Accept the explicitly complete A/B movement journal only for its named boundary and interval.
- The legible material scan fields were actually viewed and corroborated; manual reviewed anchors preserve original-source hashes and raw OCR. No real handwriting authentication or external event inspection is claimed.

### Reasoning

- 1. A opens 100, accepts 96 inbound, departs 60 in five full crates, then separately accepts 12 returned units inside the fenced cage before cutoff.
- 2. The signed ledger calculation 100+96-60+12 equals 148. The original five-crate departure is retained rather than erased when one crate returns.
- 3. Internal gate-to-shelf/cage movement creates no second receipt, and quarantine creates no departure. The report is explicitly a book result.

### Limits

- A physical counts separately conflict at 148 and 147; agreement with one observation does not resolve or override the other.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim03` in module `Audit` (supports): `Audit.bookA = 148`.
  [Model](models/Audit.lean) · [Executed check](checks/Target017.lean) · [Actual proof log](logs/target-017.log)

### Recommendation

Retain 148 as book on-hand and display the physical-count discrepancy separately.

## C08-OK-04

### Exact report claim

`input/report.md#C08-OK-04`

> **C08-OK-04.** Lot A available book stock was 141 units.
> 
> Citations: sources/01-stock-rules.md#[R03]; sources/02-opening-and-journal.md#[J02].

### Verification question

Is A available book stock 141 after the separately specified quarantine deduction from book on-hand 148?

### Source evidence

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P04`

> [R03] Lot identity and availability. Lots A, B, C, and D are separate even though their sleeves share a catalog description. An excess in one lot cannot repair a deficit in another. Available stock is book on-hand minus quarantined units minus separately reserved units, with no overlapping deductions. The A quarantine contains seven units. The B reservation contains eight different units. Quarantine and reservation change internal status without transferring custody. Physical presence, book balance, and available quantity are different predicates. A physical count may disagree with a journal-derived balance, and the disagreement must remain visible rather than silently redefining one quantity to match the other.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1395, "end_character": 2116, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P03`

> [J02] A departure, delivery, and return. OUT-A at 11:00 transferred five full crates to carrier Jun Vale. The customer accepted four crates and declined the fifth. At 16:00 Jun returned the still-sealed fifth crate; Elin accepted it inside the fenced return cage. The entire five-crate departure remains recorded, followed by the separate one-crate return. There were no other A departures or returns that day. At 17:00 seven units already on a W1 shelf were quarantined. They remained inside the inventory boundary. A reviewer must therefore distinguish dispatched quantity, delivered quantity, returned quantity, on-hand, and available stock. None of these labels can be substituted merely because they refer to the same order.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 694, "end_character": 1423, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-dbfkr6yd"}`.

- [input/sources/07-bin-and-exception-register.md](input/sources/07-bin-and-exception-register.md) — `P03`

> [BIN02] Quarantine ticket Q-A-7. At 17:00 Elin attached a hold label to seven loose A units on shelf A1 after noticing cosmetic sleeve marks. The ticket states that those seven units remain physically in W1 and are excluded from availability pending review. It does not order disposal, destruction, shipment, or a transfer to another lot. The label applies to individual units, not seven crates. No later release from quarantine occurred before cutoff. The physical count sheets both expressly included the held units. The record supports a status deduction from available A stock without decrementing A book on-hand.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 712, "end_character": 1329, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "17864baef381443926666ff2acbb425f97ab919bb09877291086a640ba22e3f9", "artifact_directory": "extraction/D00009/attempt-4g00o254"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P02`

> [J01] Opening and receipts. At 08:00 lot A opened with 100 units and lot B with 40 units. At 09:00 receipt IN-A accepted eight sealed full crates of A. At 09:30 receipt IN-B accepted two sealed full cartons of B. Clerk Elin Shore accepted custody at the gate. Each container was confirmed full, without a partial notation. These are posted accepted receipts, not expected procurement deliveries. No other opening adjustment or accepted inbound movement for A or B occurred before cutoff. The completeness statement is restricted to the named interval and lots. It does not establish any opening quantity for D or repair the C import anomaly.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 51, "end_character": 692, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-dbfkr6yd"}`.

- [input/sources/05-custody-register.md](input/sources/05-custody-register.md) — `P04`

> [K03] Bounded completeness. The register and journal list all accepted A and B movements for the stated day. This permits absence of further A or B movements to be used in exact book arithmetic. It does not establish complete D custody, complete C physical reconciliation, or complete warehouse activity over other dates. The A physical count conflict remains unresolved despite complete movement records. Completeness of one evidence type is not an assertion that every other evidence type agrees. A report that says every lot was reconciled therefore needs an argument beyond the limited A/B movement inventory and must confront the explicit unresolved cases.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1377, "end_character": 2038, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "54ba3d90c6fd73c04b139b20f2cc369e144f6050697949c27f883d4209ad2830", "artifact_directory": "extraction/D00007/attempt-c0z4297u"}`.

### Rules

- R03 availability subtracts quarantined and separately reserved quantities without overlap; quarantine does not transfer custody.

### Assumptions

- R03 and the supplied bin tickets are interpreted as the applicable finite A/B deduction schedule; no undocumented extra holds or reservations are invented.

### Reasoning

- 1. The complete movement arithmetic gives A book 148. J02/BIN02 identify exactly seven loose A units quarantined onW1 shelf, still inside the boundary and not released before cutoff.
- 2. The applicable A status schedule deducts seven units, giving 148-7=141 available book stock.
- 3. The deduction is individual units, not seven crates, and does not reduce book on-hand itself.

### Limits

- This is book-derived availability under the supplied deduction schedule; it does not settle the disputed physical total.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim04` in module `Audit` (supports): `Audit.availableA = 141`.
  [Model](models/Audit.lean) · [Executed check](checks/Target018.lean) · [Actual proof log](logs/target-018.log)

### Recommendation

Retain 141 available and keep 148 book and seven quarantined as distinct fields.

## C08-OK-05

### Exact report claim

`input/report.md#C08-OK-05`

> **C08-OK-05.** Lot B book on-hand was 40 units.
> 
> Citations: sources/02-opening-and-journal.md#[J01]; sources/02-opening-and-journal.md#[J03].

### Verification question

Does B book on-hand remain 40 after its accepted receipt, actual two-carton departure and canceled unfilled request?

### Source evidence

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P02`

> [R01] Unit definitions and boundary. The inventory boundary consists of rooms W1 and W2 and the fenced return cage at the invented North Quay warehouse. The cutoff is 18:00 on 14 April 2032. All quantities are exact integer individual sleeves, called units. A sealed full crate contains twelve units. A sealed full carton contains six units. A pallet has no fixed conversion. A partial-container label overrides the standard full-container quantity; an empty container contributes zero. All names and transactions in this packet are invented. These rules define the finite exercise and do not prescribe real shipping procedures.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 664, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P03`

> [R02] Movement semantics. Opening stock plus accepted inbound movements minus completed outbound movements plus accepted returns determines book on-hand. A printed ticket, order, reservation, or pick request changes no physical inventory merely by existing. Departure occurs at the signed actual custody handoff across the boundary. Customer delivery is a separate later event. A carrier can hold inventory that has already departed but is not yet delivered. Return increases on-hand when the receiving custodian accepts the goods back across the boundary. Returned goods in the fenced cage are inside the boundary even before reshelving. An accepted return is a separate movement, not a reason to erase the original departure.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 666, "end_character": 1393, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P02`

> [J01] Opening and receipts. At 08:00 lot A opened with 100 units and lot B with 40 units. At 09:00 receipt IN-A accepted eight sealed full crates of A. At 09:30 receipt IN-B accepted two sealed full cartons of B. Clerk Elin Shore accepted custody at the gate. Each container was confirmed full, without a partial notation. These are posted accepted receipts, not expected procurement deliveries. No other opening adjustment or accepted inbound movement for A or B occurred before cutoff. The completeness statement is restricted to the named interval and lots. It does not establish any opening quantity for D or repair the C import anomaly.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 51, "end_character": 692, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-dbfkr6yd"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P04`

> [J03] B request and actual handoff. OUT-B requested three cartons, but the signed carrier handoff at 12:00 records two full cartons. The remaining carton stayed on shelf B4 because its packaging label was missing. At 15:00 that unfilled order quantity was canceled. It never crossed the warehouse boundary. A separate next-day order reserved eight other B units, distinct from both the dispatched cartons and the canceled request. There was no B return and no need to invent one: the canceled quantity never left. The A quarantine affects no B stock. The B journal contains no other completed inbound, outbound, or return movements within the cutoff interval.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1425, "end_character": 2084, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-dbfkr6yd"}`.

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
Coordinates: `{"kind": "ocr", "page": 2, "origin": {"format": "pdf", "page": 2, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0002-raster.png", "tsv_artifact": "pdf-page-0002.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 94.90358588559322, "minimum_word_confidence": 8.591576, "confidence_threshold": 85.0, "low_confidence_words": 4, "word_count": 236, "original": "input/originals/D00008.pdf", "original_sha256": "e64921cc43741a187a1063655d55e820e43a91c3f6152d0671af4fce81f7fe58", "artifact_directory": "extraction/D00008/attempt-5dzca71r", "source_anchor": "pdf-page-0002", "root_source_anchor": "pdf-page-0002", "reviewer": "audit_01m", "reason": "Actually inspected original scan page 2 raster with view_image. Corrected visible T02 and CHAIN/LIMIT marker characters, time characters and terminal lot punctuation as needed. Full/crate/carton counts, signed custody stage and negations were compared with the original.", "reviewed_at": "2026-11-04T15:16:58.371557+00:00", "transcription_snapshot": "input/manual-transcriptions/D00008/f2c73ff169fa72a87f8a86ce29319fba80b81b376e3a4b6229800b78686ff70a.txt", "transcription_file_sha256": "62466a0a4466eabee04c4d14d61bc57708d7a1914a5dd71fb33fc3cfbd93898d", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

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
Coordinates: `{"kind": "ocr", "page": 4, "origin": {"format": "pdf", "page": 4, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0004-raster.png", "tsv_artifact": "pdf-page-0004.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.65679095528456, "minimum_word_confidence": 65.657257, "confidence_threshold": 85.0, "low_confidence_words": 4, "word_count": 246, "original": "input/originals/D00008.pdf", "original_sha256": "e64921cc43741a187a1063655d55e820e43a91c3f6152d0671af4fce81f7fe58", "artifact_directory": "extraction/D00008/attempt-5dzca71r", "source_anchor": "pdf-page-0004", "root_source_anchor": "pdf-page-0004", "reviewer": "audit_01m", "reason": "Actually inspected original scan page 4 raster with view_image. Corrected visible T04 and CHAIN/LIMIT marker characters, time characters and terminal lot punctuation as needed. Full/crate/carton counts, signed custody stage and negations were compared with the original.", "reviewed_at": "2026-11-04T15:16:58.578605+00:00", "transcription_snapshot": "input/manual-transcriptions/D00008/653097fa4c7e85eb684393bda9dd0a3959fec379a0851eefccc17e303dbea4da.txt", "transcription_file_sha256": "10e99572a3bd9fb6e15426d1069925eeb7e516a18cc3c2aa41bfa9b3fb21c681", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/05-custody-register.md](input/sources/05-custody-register.md) — `P04`

> [K03] Bounded completeness. The register and journal list all accepted A and B movements for the stated day. This permits absence of further A or B movements to be used in exact book arithmetic. It does not establish complete D custody, complete C physical reconciliation, or complete warehouse activity over other dates. The A physical count conflict remains unresolved despite complete movement records. Completeness of one evidence type is not an assertion that every other evidence type agrees. A report that says every lot was reconciled therefore needs an argument beyond the limited A/B movement inventory and must confront the explicit unresolved cases.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1377, "end_character": 2038, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "54ba3d90c6fd73c04b139b20f2cc369e144f6050697949c27f883d4209ad2830", "artifact_directory": "extraction/D00007/attempt-c0z4297u"}`.

### Rules

- Actual signed handoff controls movement under R02/R04. A canceled requested quantity that never departed is neither a departure nor return.

### Assumptions

- Use the supplied synthetic day, lot identities and exact individual-unit conversions. Accept the explicitly complete A/B movement journal only for its named boundary and interval.
- The legible material scan fields were actually viewed and corroborated; manual reviewed anchors preserve original-source hashes and raw OCR. No real handwriting authentication or external event inspection is claimed.

### Reasoning

- 1. B opens 40, receives two full cartons=12, and actually hands over two full cartons=12; J03 records no return or other B movement.
- 2. The third requested carton stayed on the shelf. Its cancellation requires no invented 12/6-unit return or subtraction.
- 3. Book calculation 40+12-12+0 equals 40.

### Limits

- The separate eight-unit reservation changes availability, not book on-hand; B agreement does not reconcile A/C/D.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim05` in module `Audit` (supports): `Audit.bookB = 40`.
  [Model](models/Audit.lean) · [Executed check](checks/Target019.lean) · [Actual proof log](logs/target-019.log)

### Recommendation

Retain 40 book units and distinguish canceled demand from completed custody movements.

## C08-OK-06

### Exact report claim

`input/report.md#C08-OK-06`

> **C08-OK-06.** Lot B available stock was 32 units.
> 
> Citations: sources/01-stock-rules.md#[R03]; sources/02-opening-and-journal.md#[J03].

### Verification question

Is B available book stock 32 after its separate active eight-unit reservation?

### Source evidence

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P04`

> [R03] Lot identity and availability. Lots A, B, C, and D are separate even though their sleeves share a catalog description. An excess in one lot cannot repair a deficit in another. Available stock is book on-hand minus quarantined units minus separately reserved units, with no overlapping deductions. The A quarantine contains seven units. The B reservation contains eight different units. Quarantine and reservation change internal status without transferring custody. Physical presence, book balance, and available quantity are different predicates. A physical count may disagree with a journal-derived balance, and the disagreement must remain visible rather than silently redefining one quantity to match the other.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1395, "end_character": 2116, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P04`

> [J03] B request and actual handoff. OUT-B requested three cartons, but the signed carrier handoff at 12:00 records two full cartons. The remaining carton stayed on shelf B4 because its packaging label was missing. At 15:00 that unfilled order quantity was canceled. It never crossed the warehouse boundary. A separate next-day order reserved eight other B units, distinct from both the dispatched cartons and the canceled request. There was no B return and no need to invent one: the canceled quantity never left. The A quarantine affects no B stock. The B journal contains no other completed inbound, outbound, or return movements within the cutoff interval.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1425, "end_character": 2084, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-dbfkr6yd"}`.

- [input/sources/07-bin-and-exception-register.md](input/sources/07-bin-and-exception-register.md) — `P04`

> [BIN03] Reservation ticket RES-B-8. The next-day customer order reserves eight B units located on shelf B2. The units were not among the two cartons loaded for OUT-B and were not the canceled third carton on B4. The reservation was still active at cutoff. The operator may not release those units to another order without canceling or changing the reservation record, but no such change occurred that day. These facts justify treating the reservation as a distinct deduction when calculating available B stock. They do not establish an outbound movement, a customer delivery, or physical absence from the B count boundary.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1331, "end_character": 1953, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "17864baef381443926666ff2acbb425f97ab919bb09877291086a640ba22e3f9", "artifact_directory": "extraction/D00009/attempt-4g00o254"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P02`

> [J01] Opening and receipts. At 08:00 lot A opened with 100 units and lot B with 40 units. At 09:00 receipt IN-A accepted eight sealed full crates of A. At 09:30 receipt IN-B accepted two sealed full cartons of B. Clerk Elin Shore accepted custody at the gate. Each container was confirmed full, without a partial notation. These are posted accepted receipts, not expected procurement deliveries. No other opening adjustment or accepted inbound movement for A or B occurred before cutoff. The completeness statement is restricted to the named interval and lots. It does not establish any opening quantity for D or repair the C import anomaly.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 51, "end_character": 692, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-dbfkr6yd"}`.

- [input/sources/05-custody-register.md](input/sources/05-custody-register.md) — `P04`

> [K03] Bounded completeness. The register and journal list all accepted A and B movements for the stated day. This permits absence of further A or B movements to be used in exact book arithmetic. It does not establish complete D custody, complete C physical reconciliation, or complete warehouse activity over other dates. The A physical count conflict remains unresolved despite complete movement records. Completeness of one evidence type is not an assertion that every other evidence type agrees. A report that says every lot was reconciled therefore needs an argument beyond the limited A/B movement inventory and must confront the explicit unresolved cases.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1377, "end_character": 2038, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "54ba3d90c6fd73c04b139b20f2cc369e144f6050697949c27f883d4209ad2830", "artifact_directory": "extraction/D00007/attempt-c0z4297u"}`.

### Rules

- Availability equals book minus applicable nonoverlapping status deductions. Reservation remains internal allocation.

### Assumptions

- Use the R03/BIN03 applicable finite status schedule; no undocumented B quarantine or extra reservation is introduced.

### Reasoning

- 1. B book balance is 40. BIN03 identifies eight reserved B units still on shelfB2, distinct from both the dispatched cartons and canceled request, and still active at cutoff.
- 2. The applicable status deduction is eight units, giving 40-8=32 available. The A quarantine has no B effect.

### Limits

- Reserved units remain physically/book on hand; this does not establish shipment to the next-day customer.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim06` in module `Audit` (supports): `Audit.availableB = 32`.
  [Model](models/Audit.lean) · [Executed check](checks/Target020.lean) · [Actual proof log](logs/target-020.log)

### Recommendation

Retain 32 available and 40 book units with the eight-unit reservation separately shown.

## C08-OK-07

### Exact report claim

`input/report.md#C08-OK-07`

> **C08-OK-07.** The A customer accepted 48 units and the warehouse accepted a 12-unit return.
> 
> Citations: sources/06-shipping-tickets-scan.pdf#[T03]; sources/01-stock-rules.md#[R01].

### Verification question

Did the A customer accept 48 units while the warehouse separately accepted a 12-unit return before cutoff?

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
Coordinates: `{"kind": "ocr", "page": 3, "origin": {"format": "pdf", "page": 3, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0003-raster.png", "tsv_artifact": "pdf-page-0003.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.59391616867471, "minimum_word_confidence": 44.648014, "confidence_threshold": 85.0, "low_confidence_words": 3, "word_count": 249, "original": "input/originals/D00008.pdf", "original_sha256": "e64921cc43741a187a1063655d55e820e43a91c3f6152d0671af4fce81f7fe58", "artifact_directory": "extraction/D00008/attempt-5dzca71r", "source_anchor": "pdf-page-0003", "root_source_anchor": "pdf-page-0003", "reviewer": "audit_01m", "reason": "Actually inspected original scan page 3 raster with view_image. Corrected visible T03 and CHAIN/LIMIT marker characters, time characters and terminal lot punctuation as needed. Full/crate/carton counts, signed custody stage and negations were compared with the original.", "reviewed_at": "2026-11-04T15:16:58.474217+00:00", "transcription_snapshot": "input/manual-transcriptions/D00008/74d057c1ffd7a573949b5264432bbf95d0ac166f21a1a683072c9f16d09c7d65.txt", "transcription_file_sha256": "8cb046c528b21f24a3e2768bfed2e1a4d71a489c47e9007ea0be72fbf2bfc611", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P02`

> [R01] Unit definitions and boundary. The inventory boundary consists of rooms W1 and W2 and the fenced return cage at the invented North Quay warehouse. The cutoff is 18:00 on 14 April 2032. All quantities are exact integer individual sleeves, called units. A sealed full crate contains twelve units. A sealed full carton contains six units. A pallet has no fixed conversion. A partial-container label overrides the standard full-container quantity; an empty container contributes zero. All names and transactions in this packet are invented. These rules define the finite exercise and do not prescribe real shipping procedures.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 664, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P03`

> [R02] Movement semantics. Opening stock plus accepted inbound movements minus completed outbound movements plus accepted returns determines book on-hand. A printed ticket, order, reservation, or pick request changes no physical inventory merely by existing. Departure occurs at the signed actual custody handoff across the boundary. Customer delivery is a separate later event. A carrier can hold inventory that has already departed but is not yet delivered. Return increases on-hand when the receiving custodian accepts the goods back across the boundary. Returned goods in the fenced cage are inside the boundary even before reshelving. An accepted return is a separate movement, not a reason to erase the original departure.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 666, "end_character": 1393, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P03`

> [J02] A departure, delivery, and return. OUT-A at 11:00 transferred five full crates to carrier Jun Vale. The customer accepted four crates and declined the fifth. At 16:00 Jun returned the still-sealed fifth crate; Elin accepted it inside the fenced return cage. The entire five-crate departure remains recorded, followed by the separate one-crate return. There were no other A departures or returns that day. At 17:00 seven units already on a W1 shelf were quarantined. They remained inside the inventory boundary. A reviewer must therefore distinguish dispatched quantity, delivered quantity, returned quantity, on-hand, and available stock. None of these labels can be substituted merely because they refer to the same order.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 694, "end_character": 1423, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-dbfkr6yd"}`.

- [input/sources/04-receiving-messages.md](input/sources/04-receiving-messages.md) — `P03`

> [M02] A completion confirmation. The customer accepted four A crates and declined one. The carrier returned the declined crate to North Quay before cutoff, and the warehouse acknowledged acceptance inside the cage. Thus every crate that departed has a documented later disposition, but the customer did not receive all five. A claim that the order was completely delivered differs from a claim that the movement chain can be traced. The return closes custody for the fifth crate while preserving the distinction between delivery and return. A reviewer should quote the relevant stage and quantity instead of using the vague term completed without defining what completed means.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 692, "end_character": 1369, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "5902f74c3a28ac0e3f3d0e49dc8503a2d0417d6a3658bde4c64ba768051d0c17", "artifact_directory": "extraction/D00006/attempt-astyrkdq"}`.

- [input/sources/05-custody-register.md](input/sources/05-custody-register.md) — `P02`

> [K01] Roles. Elin Shore may accept inbound movements and returns at North Quay. Jun Vale may accept carrier custody but cannot amend warehouse physical counts. Tomas Reed may perform an independent count but cannot retroactively alter a transfer quantity without an authorized countersigned correction. These assignments apply only to this invented day. A correct signature identity is one part of the evidence: the document must still identify the lot, movement, time, and actual quantity. A carrier signature is not a customer delivery signature. Similarly, an order clerk signature can approve a request without establishing that the requested goods physically left.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 41, "end_character": 710, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "54ba3d90c6fd73c04b139b20f2cc369e144f6050697949c27f883d4209ad2830", "artifact_directory": "extraction/D00007/attempt-c0z4297u"}`.

### Rules

- Four full crates convert to 48 units; one full crate to 12. Customer delivery and warehouse return are distinct custody stages.

### Assumptions

- Use the supplied synthetic day, lot identities and exact individual-unit conversions. Accept the explicitly complete A/B movement journal only for its named boundary and interval.
- The legible material scan fields were actually viewed and corroborated; manual reviewed anchors preserve original-source hashes and raw OCR. No real handwriting authentication or external event inspection is claimed.

### Reasoning

- 1. T03/J02/M02 say five crates departed, customer accepted four, and the still-sealed fifth was returned and accepted by Elin inside the cage at 16:00.
- 2. Customer acceptance is 4×12=48; warehouse return acceptance is 1×12=12.
- 3. All departing crates have a documented later disposition, but the original five-crate order was not fully delivered to the customer.

### Limits

- A closed custody chain is not equivalent to full customer delivery; the return does not erase the original departure.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim07` in module `Audit` (supports): `Audit.deliveredA = 48 ∧ Audit.returnedA = 12`.
  [Model](models/Audit.lean) · [Executed check](checks/Target021.lean) · [Actual proof log](logs/target-021.log)

### Recommendation

Retain the two stage-specific quantities and signatory roles.

## C08-OK-08

### Exact report claim

`input/report.md#C08-OK-08`

> **C08-OK-08.** The B order was not fully delivered: twelve of eighteen requested units were delivered.
> 
> Citations: sources/06-shipping-tickets-scan.pdf#[T04]; sources/04-receiving-messages.md#[M03].

### Verification question

Was only 12 of the original 18 requested B units delivered, so the original order was not fully delivered despite all handed-over cartons arriving?

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
Coordinates: `{"kind": "ocr", "page": 4, "origin": {"format": "pdf", "page": 4, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0004-raster.png", "tsv_artifact": "pdf-page-0004.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.65679095528456, "minimum_word_confidence": 65.657257, "confidence_threshold": 85.0, "low_confidence_words": 4, "word_count": 246, "original": "input/originals/D00008.pdf", "original_sha256": "e64921cc43741a187a1063655d55e820e43a91c3f6152d0671af4fce81f7fe58", "artifact_directory": "extraction/D00008/attempt-5dzca71r", "source_anchor": "pdf-page-0004", "root_source_anchor": "pdf-page-0004", "reviewer": "audit_01m", "reason": "Actually inspected original scan page 4 raster with view_image. Corrected visible T04 and CHAIN/LIMIT marker characters, time characters and terminal lot punctuation as needed. Full/crate/carton counts, signed custody stage and negations were compared with the original.", "reviewed_at": "2026-11-04T15:16:58.578605+00:00", "transcription_snapshot": "input/manual-transcriptions/D00008/653097fa4c7e85eb684393bda9dd0a3959fec379a0851eefccc17e303dbea4da.txt", "transcription_file_sha256": "10e99572a3bd9fb6e15426d1069925eeb7e516a18cc3c2aa41bfa9b3fb21c681", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P02`

> [R01] Unit definitions and boundary. The inventory boundary consists of rooms W1 and W2 and the fenced return cage at the invented North Quay warehouse. The cutoff is 18:00 on 14 April 2032. All quantities are exact integer individual sleeves, called units. A sealed full crate contains twelve units. A sealed full carton contains six units. A pallet has no fixed conversion. A partial-container label overrides the standard full-container quantity; an empty container contributes zero. All names and transactions in this packet are invented. These rules define the finite exercise and do not prescribe real shipping procedures.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 664, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P03`

> [R02] Movement semantics. Opening stock plus accepted inbound movements minus completed outbound movements plus accepted returns determines book on-hand. A printed ticket, order, reservation, or pick request changes no physical inventory merely by existing. Departure occurs at the signed actual custody handoff across the boundary. Customer delivery is a separate later event. A carrier can hold inventory that has already departed but is not yet delivered. Return increases on-hand when the receiving custodian accepts the goods back across the boundary. Returned goods in the fenced cage are inside the boundary even before reshelving. An accepted return is a separate movement, not a reason to erase the original departure.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 666, "end_character": 1393, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P04`

> [J03] B request and actual handoff. OUT-B requested three cartons, but the signed carrier handoff at 12:00 records two full cartons. The remaining carton stayed on shelf B4 because its packaging label was missing. At 15:00 that unfilled order quantity was canceled. It never crossed the warehouse boundary. A separate next-day order reserved eight other B units, distinct from both the dispatched cartons and the canceled request. There was no B return and no need to invent one: the canceled quantity never left. The A quarantine affects no B stock. The B journal contains no other completed inbound, outbound, or return movements within the cutoff interval.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1425, "end_character": 2084, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-dbfkr6yd"}`.

- [input/sources/04-receiving-messages.md](input/sources/04-receiving-messages.md) — `P04`

> [M03] B order closure. The customer confirms receiving the two cartons actually transferred to the carrier. The third requested carton remained at the warehouse and was canceled. All handed-over cartons were delivered, but the original three-carton order was not fully delivered. These statements concern different denominators and are consistent. Cancellation closes unfilled demand without moving stock. It does not prove a customer return, loss, or hidden replacement shipment. The separate eight-unit reservation remains an allocation within the warehouse and must not be confused with the canceled carton. Each statement retains its lot and order identity.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1371, "end_character": 2032, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "5902f74c3a28ac0e3f3d0e49dc8503a2d0417d6a3658bde4c64ba768051d0c17", "artifact_directory": "extraction/D00006/attempt-astyrkdq"}`.

### Rules

- The denominator for full original-order delivery is requested quantity, not merely the smaller actual handoff. Requests/cancellations do not move stock.

### Assumptions

- Use the supplied synthetic day, lot identities and exact individual-unit conversions. Accept the explicitly complete A/B movement journal only for its named boundary and interval.
- The legible material scan fields were actually viewed and corroborated; manual reviewed anchors preserve original-source hashes and raw OCR. No real handwriting authentication or external event inspection is claimed.

### Reasoning

- 1. The request was three cartons=18; signed actual handoff and customer confirmation cover two full cartons=12.
- 2. The third carton remained at the warehouse and was canceled, not returned or secretly replaced.
- 3. 12<18 proves the original order was not fully delivered. This is consistent with every actually dispatched carton being delivered.

### Limits

- The finding does not allege carrier loss or customer return; it compares clearly identified stages and denominators.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim08` in module `Audit` (supports): `Audit.requestedB = 18 ∧ Audit.deliveredB = 12 ∧ Audit.deliveredB < Audit.requestedB`.
  [Model](models/Audit.lean) · [Executed check](checks/Target022.lean) · [Actual proof log](logs/target-022.log)

### Recommendation

Retain the incomplete-original-order conclusion and clarify that dispatched goods were all delivered.

## C08-OK-09

### Exact report claim

`input/report.md#C08-OK-09`

> **C08-OK-09.** The supplied A physical counts conflict, recording 148 and 147 for the same scope.
> 
> Citations: sources/03-signed-counts.md#[N01]; sources/03-signed-counts.md#[N02].

### Verification question

Do the supplied equally authoritative A count sheets record contradictory totals 148 and 147 for the same lot, scope and 18:00 cutoff?

### Source evidence

- [input/sources/03-signed-counts.md](input/sources/03-signed-counts.md) — `P02`

> [N01] Elin Shore signed COUNT-A-1 at the 18:00 cutoff. The stated count is: Lot A, all W1 shelves and fenced return cage, total 148 units. It includes the seven quarantined units and the returned sealed crate. Open shelves were counted by individual units; unopened crates used the verified standard conversion. No damaged, returned, or reserved goods were excluded. A witness initial appears, but the witness did not supply an independent count. The sheet is accepted as signed evidence within this synthetic packet, not as an infallible world axiom. Its numerical agreement with book arithmetic does not automatically invalidate another equally authoritative observation.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 33, "end_character": 706, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "902b530d21257c2ef30042baaa46dbc1fd5d2d6e8576e8d8c18fdc3c1b8d28af", "artifact_directory": "extraction/D00005/attempt-ghb9uk9o"}`.

- [input/sources/03-signed-counts.md](input/sources/03-signed-counts.md) — `P03`

> [N02] Tomas Reed independently signed COUNT-A-2 for the same 18:00 cutoff, same lot, and same boundary. The stated total is 147 units. The sheet expressly includes quarantine and the return cage. Reed has the same authority as Elin for this count. A margin note mentions a loose sleeve under a bin but does not state whether it was counted. That incomplete note cannot be used to rewrite the signed total. No signed reconciliation, recount, or authorized cancellation resolves the discrepancy. Both count sheets remain active evidence. Neither the order of their filenames nor the auditor's preferred arithmetic gives one count source priority over the other.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 708, "end_character": 1367, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "902b530d21257c2ef30042baaa46dbc1fd5d2d6e8576e8d8c18fdc3c1b8d28af", "artifact_directory": "extraction/D00005/attempt-ghb9uk9o"}`.

- [input/sources/03-signed-counts.md](input/sources/03-signed-counts.md) — `P04`

> [N03] A separate B control sheet records 40 units physically inside the boundary, including its eight reserved units. It does not count C or D. Agreement between this B count and B journal arithmetic does not resolve the A discrepancy or the C import problem. No one signed a statement that all lots were reconciled. The A difference is one unit rather than a rounding difference because units are exact integers. A reviewer should distinguish a claim about what each signed sheet records from a claim selecting the true physical A total. The first can be well supported even when the second has conflicting evidence.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1369, "end_character": 1986, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "902b530d21257c2ef30042baaa46dbc1fd5d2d6e8576e8d8c18fdc3c1b8d28af", "artifact_directory": "extraction/D00005/attempt-ghb9uk9o"}`.

- [input/sources/03-signed-counts.md](input/sources/03-signed-counts.md) — `P05`

> [N04] Count custody. The count sheets were transcribed into this source from synthetic signed forms and checked for matching lot, cutoff, and boundary labels. Their recorded signature names are evidence inside the invented exercise; no real-world handwriting examination is claimed. The transcriber was not authorized to correct observed quantities. The source does not establish which observer made a mistake or whether a sleeve moved during counting. A physical recount and a signed reconciliation would address that uncertainty. Until then, retaining both observations is more faithful than erasing a disagreeing one or deriving unrelated conclusions from inconsistent premises.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 1988, "end_character": 2669, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "902b530d21257c2ef30042baaa46dbc1fd5d2d6e8576e8d8c18fdc3c1b8d28af", "artifact_directory": "extraction/D00005/attempt-ghb9uk9o"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P04`

> [R03] Lot identity and availability. Lots A, B, C, and D are separate even though their sleeves share a catalog description. An excess in one lot cannot repair a deficit in another. Available stock is book on-hand minus quarantined units minus separately reserved units, with no overlapping deductions. The A quarantine contains seven units. The B reservation contains eight different units. Quarantine and reservation change internal status without transferring custody. Physical presence, book balance, and available quantity are different predicates. A physical count may disagree with a journal-derived balance, and the disagreement must remain visible rather than silently redefining one quantity to match the other.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1395, "end_character": 2116, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P05`

> [R04] Evidence scope. Signed actual transfer receipts take precedence over unsigned planned quantities for determining completed custody movements. The journal and register are complete for A and B movements only within the stated day. No such completeness applies to D. Equal-authority physical counts of the same boundary and cutoff remain competing evidence unless a recount or authorized correction resolves them. A later filename does not give precedence. A pale or obscured numeral in a scan requires visual review and corroboration. An OCR guess is not a signed quantity. If available evidence does not establish a unique accepted amount, report the missing argument without inventing a number or asserting that the shipment necessarily failed.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2118, "end_character": 2869, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/07-bin-and-exception-register.md](input/sources/07-bin-and-exception-register.md) — `P05`

> [BIN04] Exception ownership. Inventory reviewer Mira Cole opened unresolved exception EX-A for the one-unit disagreement between the signed A counts. She requested a recount but supplied no completed recount in this packet. Reviewer Leon Hart opened EX-C for the imported C journal deficit and requested the original unit mapping file. The request names a possible conversion issue but contains no approved correction amount. The two exceptions have different evidence needs: EX-A needs reconciliation of competing observations, while EX-C needs reconstruction of a possibly incorrect journal entry. Neither can be closed by adding unrelated B stock or by assuming a favorable D quantity.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 1955, "end_character": 2643, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "17864baef381443926666ff2acbb425f97ab919bb09877291086a640ba22e3f9", "artifact_directory": "extraction/D00009/attempt-4g00o254"}`.

### Rules

- Equal-authority same-scope observations remain competing evidence without a recount/authorized correction; journal arithmetic and filename order confer no priority.

### Assumptions

- Count signatures and scope labels are accepted as supplied documentary attributions, not infallible world-state facts.

### Reasoning

- 1. N01 attributes 148 to Elin and N02 attributes 147 to Tomas at the same cutoff, lot and boundary, both including quarantine and return cage.
- 2. The exact integer totals differ by one; the loose-sleeve margin note does not revise the signed total. No reconciliation/recount/cancellation is supplied.
- 3. The report claims only that the supplied counts conflict, which is directly supported. The formal theorem concerns attributed records, not simultaneous contradictory physical totals.

### Limits

- The true physical A count remains unresolved. Supported evidence-of-conflict is not the same semantic claim as asserting one physical total.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim09` in module `Audit` (supports): `Audit.elinCount.lot = Audit.reedCount.lot ∧ Audit.elinCount.scope = Audit.reedCount.scope ∧ Audit.elinCount.cutoff = Audit.reedCount.cutoff ∧ Audit.elinCount.issuer ≠ Audit.reedCount.issuer ∧ Audit.elinCount.amount = 148 ∧ Audit.reedCount.amount = 147 ∧ Audit.elinCount.amount ≠ Audit.reedCount.amount`.
  [Model](models/Audit.lean) · [Executed check](checks/Target023.lean) · [Actual proof log](logs/target-023.log)

### Recommendation

Retain both attributed observations and request a recount/signed reconciliation without choosing by book agreement.

## C08-OK-10

### Exact report claim

`input/report.md#C08-OK-10`

> **C08-OK-10.** The imported C book balance is minus one after postings of minus nine and plus eight from zero.
> 
> Citations: sources/02-opening-and-journal.md#[J04].

### Verification question

Does the imported C signed ledger compute minus one from opening zero, outbound nine and inbound eight?

### Source evidence

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P05`

> [J04] C import anomaly. The imported C opening book balance is zero. At 10:10 an operator posted an outbound movement of nine units; at 10:20 an inbound movement of eight units was posted. The imported book balance is therefore minus one. This is a signed-integer ledger result, not a negative number of physical objects. An unsigned correction proposal mentions a possible carton-versus-unit import error, but no approved correction is supplied. Physical reconciliation for C is incomplete, and no physical count accompanies the journal. Preserve the anomaly and the missing correction argument. A book deficit alone does not prove a physical shortage, fraud, destruction, or a correct repair amount.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2086, "end_character": 2787, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-dbfkr6yd"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P04`

> [R03] Lot identity and availability. Lots A, B, C, and D are separate even though their sleeves share a catalog description. An excess in one lot cannot repair a deficit in another. Available stock is book on-hand minus quarantined units minus separately reserved units, with no overlapping deductions. The A quarantine contains seven units. The B reservation contains eight different units. Quarantine and reservation change internal status without transferring custody. Physical presence, book balance, and available quantity are different predicates. A physical count may disagree with a journal-derived balance, and the disagreement must remain visible rather than silently redefining one quantity to match the other.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1395, "end_character": 2116, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/07-bin-and-exception-register.md](input/sources/07-bin-and-exception-register.md) — `P05`

> [BIN04] Exception ownership. Inventory reviewer Mira Cole opened unresolved exception EX-A for the one-unit disagreement between the signed A counts. She requested a recount but supplied no completed recount in this packet. Reviewer Leon Hart opened EX-C for the imported C journal deficit and requested the original unit mapping file. The request names a possible conversion issue but contains no approved correction amount. The two exceptions have different evidence needs: EX-A needs reconciliation of competing observations, while EX-C needs reconstruction of a possibly incorrect journal entry. Neither can be closed by adding unrelated B stock or by assuming a favorable D quantity.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 1955, "end_character": 2643, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "17864baef381443926666ff2acbb425f97ab919bb09877291086a640ba22e3f9", "artifact_directory": "extraction/D00009/attempt-4g00o254"}`.

### Rules

- Book arithmetic is signed integer arithmetic; lots cannot offset each other. A negative ledger result does not describe negative physical objects or prove a correct repair.

### Assumptions

- The theorem assesses the supplied imported postings as written; it does not certify their original business correctness.

### Reasoning

- 1. J04 gives imported opening 0, posting-9 at 10:10 and posting+8 at 10:20.
- 2. Exact signed calculation 0-9+8=-1 preserves the recorded anomaly rather than truncating tozero or adding another lot.
- 3. The report carefully says imported book balance, so it is supported without a C physical count.

### Limits

- No physical shortage, fraud, destruction, unit-mapping correction or adjustment amount is established.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim10` in module `Audit` (supports): `Audit.importedC = -1`.
  [Model](models/Audit.lean) · [Executed check](checks/Target024.lean) · [Actual proof log](logs/target-024.log)

### Recommendation

Retain the imported minus-one anomaly and seek the original mapping plus an authorized correction.

## C08-OK-11

### Exact report claim

`input/report.md#C08-OK-11`

> **C08-OK-11.** The D accepted quantity remains unresolved because the receiver has not signed and messages propose different amounts.
> 
> Citations: sources/06-shipping-tickets-scan.pdf#[T05]; sources/04-receiving-messages.md#[M01].

### Verification question

Does the supplied D packet leave actual accepted quantity unresolved, with a blank receiver signature and competing provisional 74/78 proposals?

### Source evidence

- [input/sources/06-shipping-tickets-scan.pdf.md](input/sources/06-shipping-tickets-scan.pdf.md) — `pdf-page-0005-reviewed-0001`

> SYNTHETIC NORTH QUAY SHIPPING FORM
> [T05] Movement D-17; 14 April 2032; clock 13:30; lot D.
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
> [T05-LIMIT] The form supports only its named movement and stages. It does not certify
> all warehouse inventory or resolve independent physical count differences. A
> signature name is an invented evidence field within this exercise, not a claim about
> real handwriting authentication. Missing attachments must remain missing in the audit
> reasoning. Reviewers should explain how the movement changes the relevant balance
> before relying on an aggregate total.

Original: [input/originals/D00008.pdf](input/originals/D00008.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 5, "origin": {"format": "pdf", "page": 5, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0005-raster.png", "tsv_artifact": "pdf-page-0005.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.48176571369294, "minimum_word_confidence": 3.835678, "confidence_threshold": 85.0, "low_confidence_words": 4, "word_count": 241, "original": "input/originals/D00008.pdf", "original_sha256": "e64921cc43741a187a1063655d55e820e43a91c3f6152d0671af4fce81f7fe58", "artifact_directory": "extraction/D00008/attempt-5dzca71r", "source_anchor": "pdf-page-0005", "root_source_anchor": "pdf-page-0005", "reviewer": "audit_01m", "reason": "Actually inspected original scan page 5 raster with view_image. Corrected visible T05 and CHAIN/LIMIT marker characters, time characters and terminal lot punctuation as needed. Full/crate/carton counts, signed custody stage and negations were compared with the original. This transcription covers the legible main printed text. The additional pale bottom T05-QTY field is not transcribed or accepted as a settled accepted quantity; visual appearance is consistent with 78, but no receiver signature exists and competing proposals remain. The main text expressly preserves that uncertainty.", "reviewed_at": "2026-11-04T15:16:58.684959+00:00", "transcription_snapshot": "input/manual-transcriptions/D00008/88f7763d0ec10b10cfbc90b82a9857fe4d8abdb2e5ba545eef5bc49b897e29bd.txt", "transcription_file_sha256": "6f2ccb26f0199a1efb92028049bb5598153da8eedf58a3bbf992099d4564e3db", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/04-receiving-messages.md](input/sources/04-receiving-messages.md) — `P02`

> [M01] The unresolved D transfer. A receiver message tentatively proposes 74 units for transfer D-17, but it is unsigned and marked provisional. A carrier message says that the faint copy looks like 78. Neither is a signed correction. The original scanned quantity line is pale, and its second digit is hard to read. No customer acceptance signature appears beside that quantity. There is no original carbon copy or later authenticated reconciliation in the packet. The two interpretations are not a license to select the convenient value. Even a legible planned quantity would not automatically establish the quantity actually accepted by the receiver.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 38, "end_character": 690, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "5902f74c3a28ac0e3f3d0e49dc8503a2d0417d6a3658bde4c64ba768051d0c17", "artifact_directory": "extraction/D00006/attempt-astyrkdq"}`.

- [input/sources/04-receiving-messages.md](input/sources/04-receiving-messages.md) — `P05`

> [M04] Missing supporting material. An email index lists next-day D recount photographs, but no photographs or recount attachment are supplied. The index proves the existence of the listing, not the content or result of the absent attachment. Vehicle photographs mentioned by the carrier are likewise unavailable. A useful finding identifies precisely which missing record could resolve the uncertain quantity. Missing evidence does not itself establish that the carrier short-shipped, that the customer miscounted, or that the document was forged. No external retrieval is authorized by this finite packet; an audit should retain the bounded evidence gap.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2034, "end_character": 2689, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "5902f74c3a28ac0e3f3d0e49dc8503a2d0417d6a3658bde4c64ba768051d0c17", "artifact_directory": "extraction/D00006/attempt-astyrkdq"}`.

- [input/sources/05-custody-register.md](input/sources/05-custody-register.md) — `P05`

> [K04] Handling disputed quantities. If an auditor cannot confidently read a numerical field, the next step is to inspect the image and the supplied corroborating records, not to convert OCR confidence into physical certainty. A faithful result may identify the likely reading while withholding a claim about accepted quantity. Competing unsigned messages do not have the authority of a completed receipt signed by both parties. This distinction also applies when a document contains a clear planned number but an incomplete actual handoff box. The field's semantic role, signature status, and custody stage matter as much as its digits.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2040, "end_character": 2676, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "54ba3d90c6fd73c04b139b20f2cc369e144f6050697949c27f883d4209ad2830", "artifact_directory": "extraction/D00007/attempt-c0z4297u"}`.

- [input/sources/07-bin-and-exception-register.md](input/sources/07-bin-and-exception-register.md) — `P06`

> [BIN05] D evidence request. The receiving coordinator requested an authenticated copy of the D acceptance box and the missing next-day recount attachment. The response log records those requests as outstanding at the cutoff used for this packet. It does not establish whether the documents exist elsewhere or what they would say. The coordinator retained both tentative quantity messages rather than promoting either into a signed actual receipt. A visual reading of the pale printed number can clarify what appears on the form, but it cannot by itself establish customer acceptance. Any later closure must identify the newly supplied evidence, its authority, and the exact quantity it resolves.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 11, "start_character": 2645, "end_character": 3340, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "17864baef381443926666ff2acbb425f97ab919bb09877291086a640ba22e3f9", "artifact_directory": "extraction/D00009/attempt-4g00o254"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P05`

> [R04] Evidence scope. Signed actual transfer receipts take precedence over unsigned planned quantities for determining completed custody movements. The journal and register are complete for A and B movements only within the stated day. No such completeness applies to D. Equal-authority physical counts of the same boundary and cutoff remain competing evidence unless a recount or authorized correction resolves them. A later filename does not give precedence. A pale or obscured numeral in a scan requires visual review and corroboration. An OCR guess is not a signed quantity. If available evidence does not establish a unique accepted amount, report the missing argument without inventing a number or asserting that the shipment necessarily failed.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2118, "end_character": 2869, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

### Rules

- A guessed/legible planned numeral is not a signed actual acceptance. D lacks complete custody evidence; unsigned proposals and absent photographs do not settle the event.

### Assumptions

- The proposed 74/78 quantities are evidence of proposals only. The auxiliary completions are hypothetical, not a transcription of the pale field as fact.

### Reasoning

- 1. The original page 5 was visually inspected: lot/ticket identity and blank receiver acceptance are clear; the pale bottom quantity appears compatible with 78 but is not used as an accepted amount.
- 2. M01 supplies tentative receiver 74 and carrier 78, neither an authenticated correction. M04/BIN05 provide no original carbon copy, supplied recount or completed evidence response.
- 3. Possible completed histories with 74 or 78 accepted preserve the same unsigned supplied evidence. The auxiliary theorem demonstrates nonuniqueness without asserting either value or limiting all possible outcomes to those two.
- 4. Thus the report's evidence-limit claim is supported. Its unsigned statement is read as referring to the supplied acceptance box, not an assertion about all possible records elsewhere.

### Limits

- No actual D accepted quantity, failed shipment, forgery or short-shipping conclusion follows. Visual uncertainty and missing event authority are distinct limits.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **auxiliary**.

### Formal evidence

- `Audit.claim11Alternatives` in module `Audit` (auxiliary): `Audit.possibleD74.suppliedReceiverSigned = false ∧ Audit.possibleD78.suppliedReceiverSigned = false ∧ Audit.possibleD74.receiverProposal = Audit.possibleD78.receiverProposal ∧ Audit.possibleD74.carrierProposal = Audit.possibleD78.carrierProposal ∧ Audit.possibleD74.actualAccepted ≠ Audit.possibleD78.actualAccepted`.
  [Model](models/Audit.lean) · [Executed check](checks/Target025.lean) · [Actual proof log](logs/target-025.log)

### Recommendation

Retain unresolved accepted quantity and obtain an authenticated acceptance record and missing recount evidence.

## C08-OK-12

### Exact report claim

`input/report.md#C08-OK-12`

> **C08-OK-12.** Movement completeness is asserted for A and B that day, not for D.
> 
> Citations: sources/05-custody-register.md#[K03].

### Verification question

Is supplied movement completeness explicitly restricted to A andB for the stated day, without comparable completeness forD?

### Source evidence

- [input/sources/05-custody-register.md](input/sources/05-custody-register.md) — `P04`

> [K03] Bounded completeness. The register and journal list all accepted A and B movements for the stated day. This permits absence of further A or B movements to be used in exact book arithmetic. It does not establish complete D custody, complete C physical reconciliation, or complete warehouse activity over other dates. The A physical count conflict remains unresolved despite complete movement records. Completeness of one evidence type is not an assertion that every other evidence type agrees. A report that says every lot was reconciled therefore needs an argument beyond the limited A/B movement inventory and must confront the explicit unresolved cases.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1377, "end_character": 2038, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "54ba3d90c6fd73c04b139b20f2cc369e144f6050697949c27f883d4209ad2830", "artifact_directory": "extraction/D00007/attempt-c0z4297u"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P05`

> [R04] Evidence scope. Signed actual transfer receipts take precedence over unsigned planned quantities for determining completed custody movements. The journal and register are complete for A and B movements only within the stated day. No such completeness applies to D. Equal-authority physical counts of the same boundary and cutoff remain competing evidence unless a recount or authorized correction resolves them. A later filename does not give precedence. A pale or obscured numeral in a scan requires visual review and corroboration. An OCR guess is not a signed quantity. If available evidence does not establish a unique accepted amount, report the missing argument without inventing a number or asserting that the shipment necessarily failed.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2118, "end_character": 2869, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P02`

> [J01] Opening and receipts. At 08:00 lot A opened with 100 units and lot B with 40 units. At 09:00 receipt IN-A accepted eight sealed full crates of A. At 09:30 receipt IN-B accepted two sealed full cartons of B. Clerk Elin Shore accepted custody at the gate. Each container was confirmed full, without a partial notation. These are posted accepted receipts, not expected procurement deliveries. No other opening adjustment or accepted inbound movement for A or B occurred before cutoff. The completeness statement is restricted to the named interval and lots. It does not establish any opening quantity for D or repair the C import anomaly.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 51, "end_character": 692, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-dbfkr6yd"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P04`

> [J03] B request and actual handoff. OUT-B requested three cartons, but the signed carrier handoff at 12:00 records two full cartons. The remaining carton stayed on shelf B4 because its packaging label was missing. At 15:00 that unfilled order quantity was canceled. It never crossed the warehouse boundary. A separate next-day order reserved eight other B units, distinct from both the dispatched cartons and the canceled request. There was no B return and no need to invent one: the canceled quantity never left. The A quarantine affects no B stock. The B journal contains no other completed inbound, outbound, or return movements within the cutoff interval.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1425, "end_character": 2084, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-dbfkr6yd"}`.

- [input/sources/07-bin-and-exception-register.md](input/sources/07-bin-and-exception-register.md) — `P06`

> [BIN05] D evidence request. The receiving coordinator requested an authenticated copy of the D acceptance box and the missing next-day recount attachment. The response log records those requests as outstanding at the cutoff used for this packet. It does not establish whether the documents exist elsewhere or what they would say. The coordinator retained both tentative quantity messages rather than promoting either into a signed actual receipt. A visual reading of the pale printed number can clarify what appears on the form, but it cannot by itself establish customer acceptance. Any later closure must identify the newly supplied evidence, its authority, and the exact quantity it resolves.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 11, "start_character": 2645, "end_character": 3340, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "17864baef381443926666ff2acbb425f97ab919bb09877291086a640ba22e3f9", "artifact_directory": "extraction/D00009/attempt-4g00o254"}`.

### Rules

- Completeness is a named domain/date/evidence-type assertion and must not expand from movements into physical reconciliation or other lots.

### Assumptions

- The finite list encodes the source's scope assertion, not an independently verified completeness theorem about real records.

### Reasoning

- 1. K03/R04 explicitly certify all A/B movements within that day and explicitly deny extending that status toD.
- 2. The finite documented completeness list therefore contains A/B and excludesD.
- 3. This supports exact A/B book arithmetic but leaves A physical conflict and C/D unresolved matters visible.

### Limits

- Exclusion from a completeness declaration is not evidence that no D movement occurred or that every other warehouse fact is unreliable.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim12` in module `Audit` (supports): `Audit.Lot.A ∈ Audit.completeMovementLots ∧ Audit.Lot.B ∈ Audit.completeMovementLots ∧ Audit.Lot.D ∉ Audit.completeMovementLots`.
  [Model](models/Audit.lean) · [Executed check](checks/Target026.lean) · [Actual proof log](logs/target-026.log)

### Recommendation

Retain the bounded A/B-day coverage statement.

## C08-OK-13

### Exact report claim

`input/report.md#C08-OK-13`

> **C08-OK-13.** A reservation changes allocation without transferring stock across the boundary.
> 
> Citations: sources/01-stock-rules.md#[R02]; sources/01-stock-rules.md#[R03].

### Verification question

Under the supplied stock rules, does a reservation alter allocation while leaving boundary-crossing book stock unchanged?

### Source evidence

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P03`

> [R02] Movement semantics. Opening stock plus accepted inbound movements minus completed outbound movements plus accepted returns determines book on-hand. A printed ticket, order, reservation, or pick request changes no physical inventory merely by existing. Departure occurs at the signed actual custody handoff across the boundary. Customer delivery is a separate later event. A carrier can hold inventory that has already departed but is not yet delivered. Return increases on-hand when the receiving custodian accepts the goods back across the boundary. Returned goods in the fenced cage are inside the boundary even before reshelving. An accepted return is a separate movement, not a reason to erase the original departure.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 666, "end_character": 1393, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P04`

> [R03] Lot identity and availability. Lots A, B, C, and D are separate even though their sleeves share a catalog description. An excess in one lot cannot repair a deficit in another. Available stock is book on-hand minus quarantined units minus separately reserved units, with no overlapping deductions. The A quarantine contains seven units. The B reservation contains eight different units. Quarantine and reservation change internal status without transferring custody. Physical presence, book balance, and available quantity are different predicates. A physical count may disagree with a journal-derived balance, and the disagreement must remain visible rather than silently redefining one quantity to match the other.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1395, "end_character": 2116, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P04`

> [J03] B request and actual handoff. OUT-B requested three cartons, but the signed carrier handoff at 12:00 records two full cartons. The remaining carton stayed on shelf B4 because its packaging label was missing. At 15:00 that unfilled order quantity was canceled. It never crossed the warehouse boundary. A separate next-day order reserved eight other B units, distinct from both the dispatched cartons and the canceled request. There was no B return and no need to invent one: the canceled quantity never left. The A quarantine affects no B stock. The B journal contains no other completed inbound, outbound, or return movements within the cutoff interval.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1425, "end_character": 2084, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-dbfkr6yd"}`.

- [input/sources/07-bin-and-exception-register.md](input/sources/07-bin-and-exception-register.md) — `P04`

> [BIN03] Reservation ticket RES-B-8. The next-day customer order reserves eight B units located on shelf B2. The units were not among the two cartons loaded for OUT-B and were not the canceled third carton on B4. The reservation was still active at cutoff. The operator may not release those units to another order without canceling or changing the reservation record, but no such change occurred that day. These facts justify treating the reservation as a distinct deduction when calculating available B stock. They do not establish an outbound movement, a customer delivery, or physical absence from the B count boundary.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1331, "end_character": 1953, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "17864baef381443926666ff2acbb425f97ab919bb09877291086a640ba22e3f9", "artifact_directory": "extraction/D00009/attempt-4g00o254"}`.

### Rules

- R02 distinguishes reservation/request from custody movement; R03/BIN03 make reservation an internal availability deduction.

### Assumptions

- Use the supplied synthetic day, lot identities and exact individual-unit conversions. Accept the explicitly complete A/B movement journal only for its named boundary and interval.
- The legible material scan fields were actually viewed and corroborated; manual reviewed anchors preserve original-source hashes and raw OCR. No real handwriting authentication or external event inspection is claimed.

### Reasoning

- 1. R02 explicitly says a reservation does not move inventory merely by existing; R03 defines its internal-status role.
- 2. BIN03 supplies the concrete B example: eight units remain physically on shelfB2, with no departure/delivery or physical absence.
- 3. The modeled reservation transition changes the reserved field while preserving on-hand for any represented state, supporting the report's rule-level claim.

### Limits

- The invariant does not authorize arbitrary reservation quantities or imply that every physical action called a reservation outside this fictional rule is movement-free.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim13` in module `Audit` (supports): `∀ s q, (Audit.reserve s q).onHand = s.onHand ∧ (Audit.reserve s q).reserved = s.reserved + q`.
  [Model](models/Audit.lean) · [Executed check](checks/Target027.lean) · [Actual proof log](logs/target-027.log)

### Recommendation

Retain and keep reservation allocation separate from actual shipment.

## C08-OK-14

### Exact report claim

`input/report.md#C08-OK-14`

> **C08-OK-14.** No supplied approved correction resolves the C import anomaly.
> 
> Citations: sources/02-opening-and-journal.md#[J04].

### Verification question

Does the supplied packet lack an approved correction resolving the C import anomaly, despite an unsigned proposal and evidence request?

### Source evidence

- [input/sources/02-opening-and-journal.md](input/sources/02-opening-and-journal.md) — `P05`

> [J04] C import anomaly. The imported C opening book balance is zero. At 10:10 an operator posted an outbound movement of nine units; at 10:20 an inbound movement of eight units was posted. The imported book balance is therefore minus one. This is a signed-integer ledger result, not a negative number of physical objects. An unsigned correction proposal mentions a possible carton-versus-unit import error, but no approved correction is supplied. Physical reconciliation for C is incomplete, and no physical count accompanies the journal. Preserve the anomaly and the missing correction argument. A book deficit alone does not prove a physical shortage, fraud, destruction, or a correct repair amount.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2086, "end_character": 2787, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "078c5054d9619a84cb3b541752c2da469621999938351e49f6f1bfa9e3d24189", "artifact_directory": "extraction/D00004/attempt-dbfkr6yd"}`.

- [input/sources/07-bin-and-exception-register.md](input/sources/07-bin-and-exception-register.md) — `P05`

> [BIN04] Exception ownership. Inventory reviewer Mira Cole opened unresolved exception EX-A for the one-unit disagreement between the signed A counts. She requested a recount but supplied no completed recount in this packet. Reviewer Leon Hart opened EX-C for the imported C journal deficit and requested the original unit mapping file. The request names a possible conversion issue but contains no approved correction amount. The two exceptions have different evidence needs: EX-A needs reconciliation of competing observations, while EX-C needs reconstruction of a possibly incorrect journal entry. Neither can be closed by adding unrelated B stock or by assuming a favorable D quantity.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 1955, "end_character": 2643, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "17864baef381443926666ff2acbb425f97ab919bb09877291086a640ba22e3f9", "artifact_directory": "extraction/D00009/attempt-4g00o254"}`.

- [input/sources/01-stock-rules.md](input/sources/01-stock-rules.md) — `P04`

> [R03] Lot identity and availability. Lots A, B, C, and D are separate even though their sleeves share a catalog description. An excess in one lot cannot repair a deficit in another. Available stock is book on-hand minus quarantined units minus separately reserved units, with no overlapping deductions. The A quarantine contains seven units. The B reservation contains eight different units. Quarantine and reservation change internal status without transferring custody. Physical presence, book balance, and available quantity are different predicates. A physical count may disagree with a journal-derived balance, and the disagreement must remain visible rather than silently redefining one quantity to match the other.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1395, "end_character": 2116, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "a3640b68ad4016c357f8b669551f2c7df3541f78391a59f025df47f766662f53", "artifact_directory": "extraction/D00003/attempt-klhw47mo"}`.

### Rules

- An unsigned hypothesis or request is not an authorized correction. The claim is about supplied evidence only, not all records that could exist elsewhere.

### Assumptions

- The no-approved-correction statement is scoped to the complete supplied packet, not historical universality.

### Reasoning

- 1. J04 explicitly records a possible carton/unit error as an unsigned proposal and says no approved correction is supplied.
- 2. BIN04 records an outstanding request for original mapping and no approved correction amount. No other supplied source resolves it.
- 3. The finite evidence list therefore contains a proposal and lacks approved correction, supporting the exact scoped report assertion.

### Limits

- This does not prove an approved correction never existed elsewhere, or that a proposed mapping explanation is false. The correct repair amount is unknown.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim14` in module `Audit` (supports): `Audit.CorrectionEvidence.unsignedProposal ∈ Audit.suppliedCCorrections ∧ Audit.CorrectionEvidence.approvedCorrection ∉ Audit.suppliedCCorrections`.
  [Model](models/Audit.lean) · [Executed check](checks/Target028.lean) · [Actual proof log](logs/target-028.log)

### Recommendation

Retain the support gap and await original mapping plus authorized correction.
