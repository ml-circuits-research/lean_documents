# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

[Semantic correspondence review](semantic-review.md)

Extraction inventory: 9 documents; 1 pending, partial or blocked. See [ingestion details](ingestion.json) and [coverage](coverage.md).

## C06-01

### Exact report claim

`input/report.md#C06-01`

> **C06-01.** P-11 and P-12 did not require competition because each individual order was below EUR 25,000.00. Sources: P02, P03, L02, F04.

### Verification question

Do P-11 and P-12 avoid competition merely because each order is individually below EUR 25,000, once the inclusive 30-date aggregation rule and prior knowledge of the combined requirement are applied?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0006`

> The applicable competitive-purchase threshold is inclusive: a normalized purchase value equal to the threshold requires competition unless an established exception applies. Revision 1 uses EUR 20,000.00. Revision 2 uses EUR 25,000.00. Below the applicable threshold, this standard does not require competitive solicitation, although a valid order approval is still required. Competition means inviting at least three independent qualified suppliers, giving each the same specification, recording the responses or documented nonresponses, and signing a comparison before order commitment. A supplier's quote, a market-price screenshot, or an existing relationship is not by itself the prescribed competition. A competition certificate expressly marked complete attests that these steps occurred; a quotation folder without that certificate does not automatically attest them.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0008`

> Two or more purchases aggregate when they concern the same funded project, the same supplier legal entity, and components of one operational requirement committed within an inclusive thirty-calendar-date window. The first commitment date is day one, and the last included date is first date plus twenty-nine calendar days. Different order numbers, cost-center labels, delivery pallets, or invoice dates do not split an otherwise common operational requirement. Purchases do not aggregate merely because the suppliers have similar names or serve the same laboratory. A documented change to a genuinely independent operational requirement can rebut aggregation, but relabeling a single installation cannot. For an aggregate, the competitive threshold applies to the combined normalized value before the first commitment if the full requirement was already known then.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[8]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L01`

> ## [L01]
> 
> This register is complete for commitment amounts, approval events, competitive-solicitation certificates, emergency declarations, retrospective reviews, and exception determinations for P-11, P-12, P-13, P-14, P-15, P-16, R-17, R-18, and E-19 from May 1 through June 30, 2029. An explicit entry “none” means the named event did not occur in that coverage, rather than that a page was omitted. That completeness does not cover P-21, E-20, payment events, or anyone's subjective assessment. The recorded original requirements for these entries were fully known at the times stated. All amounts described as normalized include unavoidable charges, exclude recoverable VAT, and already reflect the specified single final rounding unless an entry instead supplies the exact unrounded currency inputs.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 168, "end_character": 973, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L02`

> ## [L02]
> 
> P-11 and P-12 buy the two halves of one sensor-rack installation for project TIDE-4 from the same legal supplier, Pelican Instruments Ltd. The combined requirement and both prices were approved as a technical specification on May 28. Accepted requisition R-11 was received June 1 at 09:00 UTC. P-11 was committed June 3 for normalized EUR 12,400.00; P-12 was committed June 20 for normalized EUR 12,600.00. The two orders have different cost-center suffixes and delivery pallets, but neither changes the shared functional requirement. Director order approvals were granted June 2 and June 19 respectively. Competitive-solicitation certificate: none. Emergency declaration: none. Other competition exception determination: none.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 992, "end_character": 1729, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

- [input/sources/reconciliation-correspondence.md](input/sources/reconciliation-correspondence.md) — `F04`

> ## [F04]
> 
> The project leader asked why the sensor-rack requirement appeared as two orders. The buyer answered that one pallet needed early delivery while the second could follow on June 20, and that accounting preferred two cost-center suffixes for allocation. The buyer did not claim that the requirements were independent or unknown at first commitment. The underlying May 28 specification already listed both halves. This correspondence corroborates the aggregation facts in L02 without creating a new exception. The director's approvals show permission to commit money, but neither document purports to be a competition certificate or emergency declaration.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2195, "end_character": 2856, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "2b5e3cc9824253cabb8493b6702e9b725dbbb3e61b2d9b5003be58748edcc535", "artifact_directory": "extraction/D00008/attempt-suocatu5"}`.

- [input/sources/revision-amendment.pdf.md](input/sources/revision-amendment.pdf.md) — `pdf-page-0002`

> [V01]
> Revision 2 takes effect at 2029-06-01 00:00 UTC. An accepted requisition received before
> that instant remains under revision 1 for its original scope, even if approval, supplier
> selection, commitment, delivery, or invoicing occurs later. An accepted requisition received
> at the exact boundary or afterward uses revision 2. Accepted receipt is the central intake
> service’s timestamp, not the time when an employee drafted an email or a buyer opened a
> task. This amendment changes the threshold but does not retroactively invalidate approvals
> valid under the retained revision. A dashboard field showing the presently published
> standard is not a record of which version governs an individual requisition.

Original: [input/originals/D00009.pdf](input/originals/D00009.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-3230ujwt"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

### Rules

- P03 aggregates the same project, legal supplier and single operational requirement within first commitment date through first+29 dates; known full requirements are threshold-tested together before first commitment.
- P02 requires competition at an inclusive threshold unless an established exception applies. Accepted June 1 receipt invokes revision 2 under V01.

### Assumptions

- Use the supplied fictional HPS clauses and exact documentary inputs within their stated May-June 2029 scope; source authenticity beyond explicit stipulations is not independently established.
- Source-to-symbol transcription is scoped to the cited paragraphs/pages and actual extraction/visual reviews; independently checked numeric/date conversions are retained in arithmetic-check.md.

### Reasoning

- 1. The individual amounts EUR 12,400 and EUR 12,600 are each below EUR 25,000; that premise is true.
- 2. L02 establishes one TIDE-4 sensor rack, the same legal supplier and both halves known in the May 28 specification. F04 confirms differing pallets/cost centers are logistical/accounting labels, not independent requirements.
- 3. Commitments June 3 and June 20 differ by 17 dates; the latter is window day 18 and lies inside the inclusive thirty-date window.
- 4. P03 therefore applies the combined EUR 25,000 value before the first commitment. Equality triggers revision 2 competition; L02 records no certificate, emergency declaration or other exception.
- 5. The no-competition conclusion is refuted because it tests the wrong unit of purchase, despite the true individual amounts.

### Limits

- The aggregation result is specific to this documented pair and its known shared requirement; supplier similarity or merely serving one laboratory would not suffice.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim01` in module `Audit` (refutes): `Audit.rackAggregates = true ∧ Audit.rackKnownBeforeFirst = true ∧ Audit.competitionRequired 2 Audit.rackCents = true ∧ (1240000 : Nat) < 2500000 ∧ (1260000 : Nat) < 2500000`.
  [Model](models/Audit.lean) · [Executed check](checks/Target018.lean) · [Actual proof log](logs/target-018.log)

### Recommendation

Replace the conclusion with an inclusive EUR 25,000 aggregate competition obligation, and record the missing covered certificate/exception separately from valid spending approvals.

## C06-02

### Exact report claim

`input/report.md#C06-02`

> **C06-02.** The combined normalized value of P-11 and P-12 is exactly EUR 25,000.00. Sources: L02, P04.

### Verification question

Is the combined normalized P-11/P-12 value exactly EUR 25,000.00 under P04 without adding, subtracting or rerounding undocumented amounts?

### Source evidence

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L01`

> ## [L01]
> 
> This register is complete for commitment amounts, approval events, competitive-solicitation certificates, emergency declarations, retrospective reviews, and exception determinations for P-11, P-12, P-13, P-14, P-15, P-16, R-17, R-18, and E-19 from May 1 through June 30, 2029. An explicit entry “none” means the named event did not occur in that coverage, rather than that a page was omitted. That completeness does not cover P-21, E-20, payment events, or anyone's subjective assessment. The recorded original requirements for these entries were fully known at the times stated. All amounts described as normalized include unavoidable charges, exclude recoverable VAT, and already reflect the specified single final rounding unless an entry instead supplies the exact unrounded currency inputs.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 168, "end_character": 973, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L02`

> ## [L02]
> 
> P-11 and P-12 buy the two halves of one sensor-rack installation for project TIDE-4 from the same legal supplier, Pelican Instruments Ltd. The combined requirement and both prices were approved as a technical specification on May 28. Accepted requisition R-11 was received June 1 at 09:00 UTC. P-11 was committed June 3 for normalized EUR 12,400.00; P-12 was committed June 20 for normalized EUR 12,600.00. The two orders have different cost-center suffixes and delivery pallets, but neither changes the shared functional requirement. Director order approvals were granted June 2 and June 19 respectively. Competitive-solicitation certificate: none. Emergency declaration: none. Other competition exception determination: none.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 992, "end_character": 1729, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0010`

> Normalized purchase value is an exact euro amount rounded once to euro cents after the following calculation. Add all unavoidable consideration for the requirement, including freight and installation. Subtract only unconditional rebates already binding at commitment. Exclude separately stated recoverable VAT. Convert the resulting transaction-currency amount using the fixed contractual exchange rate in the approved requisition schedule; this rate, not a later market quote, controls. Carry the conversion as an exact rational number, then round to the nearest cent, with exact half-cent ties rounded upward for these nonnegative amounts. Do not round each intermediate component, truncate fractional cents, round down to a whole euro, or test the threshold against the unrounded result. The synthetic contracts permit fractional transaction-currency cents, so an amount with three decimal places is not automatically a transcription error.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[10]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

### Rules

- L01 defines the stated normalized values as including unavoidable charges, excluding recoverable VAT and already finally rounded. Sum the two stated normalized values once.

### Assumptions

- Use the supplied fictional HPS clauses and exact documentary inputs within their stated May-June 2029 scope; source authenticity beyond explicit stipulations is not independently established.
- Source-to-symbol transcription is scoped to the cited paragraphs/pages and actual extraction/visual reviews; independently checked numeric/date conversions are retained in arithmetic-check.md.

### Reasoning

- 1. L02 provides normalized EUR 12,400.00 and EUR 12,600.00.
- 2. In integer cents, 1,240,000 + 1,260,000 = 2,500,000, exactly EUR 25,000.00. No extra fee, rebate or conversion is supplied for these amounts.
- 3. The checked arithmetic supports the exact combined-value assertion; aggregation applicability is independently explained in C06-01.

### Limits

- The calculation does not independently authenticate prices or certify compliance.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim02` in module `Audit` (supports): `Audit.rackCents = 2500000`.
  [Model](models/Audit.lean) · [Executed check](checks/Target019.lean) · [Actual proof log](logs/target-019.log)

### Recommendation

Retain the exact amount and normalized-value scope.

## C06-03

### Exact report claim

`input/report.md#C06-03`

> **C06-03.** P-13 reaches the revision 2 competition threshold after the required final cent rounding. Sources: P02, P04, V05, L03, F01.

### Verification question

Does P-13 exact USD consideration at its fixed contractual rate reach the revision 2 inclusive competition threshold after the required single final cent rounding?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0006`

> The applicable competitive-purchase threshold is inclusive: a normalized purchase value equal to the threshold requires competition unless an established exception applies. Revision 1 uses EUR 20,000.00. Revision 2 uses EUR 25,000.00. Below the applicable threshold, this standard does not require competitive solicitation, although a valid order approval is still required. Competition means inviting at least three independent qualified suppliers, giving each the same specification, recording the responses or documented nonresponses, and signing a comparison before order commitment. A supplier's quote, a market-price screenshot, or an existing relationship is not by itself the prescribed competition. A competition certificate expressly marked complete attests that these steps occurred; a quotation folder without that certificate does not automatically attest them.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0010`

> Normalized purchase value is an exact euro amount rounded once to euro cents after the following calculation. Add all unavoidable consideration for the requirement, including freight and installation. Subtract only unconditional rebates already binding at commitment. Exclude separately stated recoverable VAT. Convert the resulting transaction-currency amount using the fixed contractual exchange rate in the approved requisition schedule; this rate, not a later market quote, controls. Carry the conversion as an exact rational number, then round to the nearest cent, with exact half-cent ties rounded upward for these nonnegative amounts. Do not round each intermediate component, truncate fractional cents, round down to a whole euro, or test the threshold against the unrounded result. The synthetic contracts permit fractional transaction-currency cents, so an amount with three decimal places is not automatically a transcription error.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[10]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/revision-amendment.pdf.md](input/sources/revision-amendment.pdf.md) — `pdf-page-0002`

> [V01]
> Revision 2 takes effect at 2029-06-01 00:00 UTC. An accepted requisition received before
> that instant remains under revision 1 for its original scope, even if approval, supplier
> selection, commitment, delivery, or invoicing occurs later. An accepted requisition received
> at the exact boundary or afterward uses revision 2. Accepted receipt is the central intake
> service’s timestamp, not the time when an employee drafted an email or a buyer opened a
> task. This amendment changes the threshold but does not retroactively invalidate approvals
> valid under the retained revision. A dashboard field showing the presently published
> standard is not a record of which version governs an individual requisition.

Original: [input/originals/D00009.pdf](input/originals/D00009.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-3230ujwt"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/revision-amendment.pdf.md](input/sources/revision-amendment.pdf.md) — `pdf-page-0006`

> [V05]
> The requisition currency schedule fixes USD-to-EUR at exactly 0.900000 euros per US dollar
> for P-13 and CHF-to-EUR at exactly 1.040000 euros per Swiss franc for P-22. These are
> synthetic contractual rates for this assessment and are not claims about an actual exchange
> market. P-13 permits a transaction amount of USD 27,777.775, has no freight charge, and has
> no unconditional rebate or separately included VAT. P-22 specifies CHF 18,000.00 equipment
> plus CHF 1,000.00 unavoidable freight. Its possible year-end loyalty credit is discretionary
> and is not an unconditional rebate at commitment. Later accounting software may display only
> two currency decimals, but those displays do not amend these exact contractual inputs.

Original: [input/originals/D00009.pdf](input/originals/D00009.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 6, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0006.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-3230ujwt"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L03`

> ## [L03]
> 
> P-13 was received June 4 and committed June 12. Its exact contractual USD amount and fixed conversion rate are in V05. No other purchase aggregates with it. A complete three-supplier competition certificate was signed June 10, and a director order approval was granted June 11. The buyer's worksheet retained the exact rational converted value before the final cent rounding; the public purchase dashboard displayed the rounded normalized amount. P-14, a separate requirement received June 5, has an exact unrounded EUR consideration of 24,999.994 and was committed June 12. It has no other charges, rebates, VAT included, or aggregating purchase. A director approved it June 11; no competition certificate or exception exists for P-14.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1748, "end_character": 2494, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

- [input/sources/reconciliation-correspondence.md](input/sources/reconciliation-correspondence.md) — `F01`

> ## [F01]
> 
> Finance analyst Nia West reconciled P-13 on June 18. Her working note multiplies USD 27,777.775 by the fixed rate 0.900000 and obtains exact EUR 24,999.9975 before cent rounding. The note applies the prescribed single final nearest-cent rounding and records EUR 25,000.00 as the normalized value. It explicitly warns that comparing the unrounded amount with EUR 25,000.00 would apply the threshold at the wrong stage. The note is arithmetic corroboration, not a replacement for the operative rounding clause. It does not claim that every amount beginning with the digits 24,999 is below the threshold after normalization.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 161, "end_character": 792, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "2b5e3cc9824253cabb8493b6702e9b725dbbb3e61b2d9b5003be58748edcc535", "artifact_directory": "extraction/D00008/attempt-suocatu5"}`.

### Rules

- P04 requires exact rational conversion followed by a single nearest-cent rounding, ties upward; threshold comparison uses that normalized value.
- V05 fixes USD/EUR at 0.900000; June 4 receipt uses revision 2 and its inclusive EUR 25,000 threshold.

### Assumptions

- Use the supplied fictional HPS clauses and exact documentary inputs within their stated May-June 2029 scope; source authenticity beyond explicit stipulations is not independently established.
- Source-to-symbol transcription is scoped to the cited paragraphs/pages and actual extraction/visual reviews; independently checked numeric/date conversions are retained in arithmetic-check.md.

### Reasoning

- 1. V05 fixes USD 27,777.775 with no extra freight, rebate or separately included VAT. The original PDF page 6 was visually inspected.
- 2. The exact rational multiplication 27,777.775 × 0.9 gives EUR 24,999.9975, represented as 249999975 ten-thousandths.
- 3. Single final rounding gives 2,500,000 cents, EUR 25,000.00. This equals the inclusive revision 2 threshold and requires competition.
- 4. F01 independently corroborates that arithmetic; L03 also records that the required complete competition certificate and director approval actually exist.

### Limits

- This proves threshold classification after the sourced normalization, not a general theorem about arbitrary exchange rates or substantive procurement quality.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim03` in module `Audit` (supports): `Audit.p13Exact = 249999975 ∧ Audit.p13Cents = 2500000 ∧ Audit.competitionRequired 2 Audit.p13Cents = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target020.lean) · [Actual proof log](logs/target-020.log)

### Recommendation

Retain and show both the exact intermediate value and the final normalized value.

## C06-04

### Exact report claim

`input/report.md#C06-04`

> **C06-04.** P-13 is below the competition threshold because its exact converted amount is EUR 24,999.9975 before rounding. Sources: P02, P04, V05, F01.

### Verification question

Can P-13 be classified below threshold using exact EUR 24,999.9975 before final rounding, when P04 prescribes threshold comparison after normalization?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0006`

> The applicable competitive-purchase threshold is inclusive: a normalized purchase value equal to the threshold requires competition unless an established exception applies. Revision 1 uses EUR 20,000.00. Revision 2 uses EUR 25,000.00. Below the applicable threshold, this standard does not require competitive solicitation, although a valid order approval is still required. Competition means inviting at least three independent qualified suppliers, giving each the same specification, recording the responses or documented nonresponses, and signing a comparison before order commitment. A supplier's quote, a market-price screenshot, or an existing relationship is not by itself the prescribed competition. A competition certificate expressly marked complete attests that these steps occurred; a quotation folder without that certificate does not automatically attest them.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0010`

> Normalized purchase value is an exact euro amount rounded once to euro cents after the following calculation. Add all unavoidable consideration for the requirement, including freight and installation. Subtract only unconditional rebates already binding at commitment. Exclude separately stated recoverable VAT. Convert the resulting transaction-currency amount using the fixed contractual exchange rate in the approved requisition schedule; this rate, not a later market quote, controls. Carry the conversion as an exact rational number, then round to the nearest cent, with exact half-cent ties rounded upward for these nonnegative amounts. Do not round each intermediate component, truncate fractional cents, round down to a whole euro, or test the threshold against the unrounded result. The synthetic contracts permit fractional transaction-currency cents, so an amount with three decimal places is not automatically a transcription error.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[10]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/revision-amendment.pdf.md](input/sources/revision-amendment.pdf.md) — `pdf-page-0006`

> [V05]
> The requisition currency schedule fixes USD-to-EUR at exactly 0.900000 euros per US dollar
> for P-13 and CHF-to-EUR at exactly 1.040000 euros per Swiss franc for P-22. These are
> synthetic contractual rates for this assessment and are not claims about an actual exchange
> market. P-13 permits a transaction amount of USD 27,777.775, has no freight charge, and has
> no unconditional rebate or separately included VAT. P-22 specifies CHF 18,000.00 equipment
> plus CHF 1,000.00 unavoidable freight. Its possible year-end loyalty credit is discretionary
> and is not an unconditional rebate at commitment. Later accounting software may display only
> two currency decimals, but those displays do not amend these exact contractual inputs.

Original: [input/originals/D00009.pdf](input/originals/D00009.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 6, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0006.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-3230ujwt"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L03`

> ## [L03]
> 
> P-13 was received June 4 and committed June 12. Its exact contractual USD amount and fixed conversion rate are in V05. No other purchase aggregates with it. A complete three-supplier competition certificate was signed June 10, and a director order approval was granted June 11. The buyer's worksheet retained the exact rational converted value before the final cent rounding; the public purchase dashboard displayed the rounded normalized amount. P-14, a separate requirement received June 5, has an exact unrounded EUR consideration of 24,999.994 and was committed June 12. It has no other charges, rebates, VAT included, or aggregating purchase. A director approved it June 11; no competition certificate or exception exists for P-14.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1748, "end_character": 2494, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

- [input/sources/reconciliation-correspondence.md](input/sources/reconciliation-correspondence.md) — `F01`

> ## [F01]
> 
> Finance analyst Nia West reconciled P-13 on June 18. Her working note multiplies USD 27,777.775 by the fixed rate 0.900000 and obtains exact EUR 24,999.9975 before cent rounding. The note applies the prescribed single final nearest-cent rounding and records EUR 25,000.00 as the normalized value. It explicitly warns that comparing the unrounded amount with EUR 25,000.00 would apply the threshold at the wrong stage. The note is arithmetic corroboration, not a replacement for the operative rounding clause. It does not claim that every amount beginning with the digits 24,999 is below the threshold after normalization.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 161, "end_character": 792, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "2b5e3cc9824253cabb8493b6702e9b725dbbb3e61b2d9b5003be58748edcc535", "artifact_directory": "extraction/D00008/attempt-suocatu5"}`.

### Rules

- P04 explicitly forbids testing the unrounded result against the threshold. P02 equality after normalization triggers competition.

### Assumptions

- Use the supplied fictional HPS clauses and exact documentary inputs within their stated May-June 2029 scope; source authenticity beyond explicit stipulations is not independently established.
- Source-to-symbol transcription is scoped to the cited paragraphs/pages and actual extraction/visual reviews; independently checked numeric/date conversions are retained in arithmetic-check.md.

### Reasoning

- 1. The report accurately states the unrounded rational amount: EUR 24,999.9975 is less than EUR 25,000.
- 2. But that amount is not the prescribed threshold input. Final nearest-cent rounding produces EUR 25,000.00.
- 3. The normalized result is not below the threshold, so the report conclusion is false and its comparison uses the wrong calculation stage. F01 explicitly warns against that step.

### Limits

- The exact pre-rounding number itself is not refuted; only its use to establish below-threshold status and that resulting status fail.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim04` in module `Audit` (refutes): `Audit.p13Exact < 250000000 ∧ ¬ (Audit.p13Cents < 2500000)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target021.lean) · [Actual proof log](logs/target-021.log)

### Recommendation

Replace the conclusion with threshold equality after required rounding.

## C06-05

### Exact report claim

`input/report.md#C06-05`

> **C06-05.** P-14 requires competition because rounding EUR 24,999.994 gives EUR 25,000.00. Sources: P02, P04, L03, F02.

### Verification question

Does EUR 24,999.994 for the independent P-14 requirement round to EUR 25,000.00 and trigger revision 2 competition?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0006`

> The applicable competitive-purchase threshold is inclusive: a normalized purchase value equal to the threshold requires competition unless an established exception applies. Revision 1 uses EUR 20,000.00. Revision 2 uses EUR 25,000.00. Below the applicable threshold, this standard does not require competitive solicitation, although a valid order approval is still required. Competition means inviting at least three independent qualified suppliers, giving each the same specification, recording the responses or documented nonresponses, and signing a comparison before order commitment. A supplier's quote, a market-price screenshot, or an existing relationship is not by itself the prescribed competition. A competition certificate expressly marked complete attests that these steps occurred; a quotation folder without that certificate does not automatically attest them.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0010`

> Normalized purchase value is an exact euro amount rounded once to euro cents after the following calculation. Add all unavoidable consideration for the requirement, including freight and installation. Subtract only unconditional rebates already binding at commitment. Exclude separately stated recoverable VAT. Convert the resulting transaction-currency amount using the fixed contractual exchange rate in the approved requisition schedule; this rate, not a later market quote, controls. Carry the conversion as an exact rational number, then round to the nearest cent, with exact half-cent ties rounded upward for these nonnegative amounts. Do not round each intermediate component, truncate fractional cents, round down to a whole euro, or test the threshold against the unrounded result. The synthetic contracts permit fractional transaction-currency cents, so an amount with three decimal places is not automatically a transcription error.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[10]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/revision-amendment.pdf.md](input/sources/revision-amendment.pdf.md) — `pdf-page-0002`

> [V01]
> Revision 2 takes effect at 2029-06-01 00:00 UTC. An accepted requisition received before
> that instant remains under revision 1 for its original scope, even if approval, supplier
> selection, commitment, delivery, or invoicing occurs later. An accepted requisition received
> at the exact boundary or afterward uses revision 2. Accepted receipt is the central intake
> service’s timestamp, not the time when an employee drafted an email or a buyer opened a
> task. This amendment changes the threshold but does not retroactively invalidate approvals
> valid under the retained revision. A dashboard field showing the presently published
> standard is not a record of which version governs an individual requisition.

Original: [input/originals/D00009.pdf](input/originals/D00009.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-3230ujwt"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L03`

> ## [L03]
> 
> P-13 was received June 4 and committed June 12. Its exact contractual USD amount and fixed conversion rate are in V05. No other purchase aggregates with it. A complete three-supplier competition certificate was signed June 10, and a director order approval was granted June 11. The buyer's worksheet retained the exact rational converted value before the final cent rounding; the public purchase dashboard displayed the rounded normalized amount. P-14, a separate requirement received June 5, has an exact unrounded EUR consideration of 24,999.994 and was committed June 12. It has no other charges, rebates, VAT included, or aggregating purchase. A director approved it June 11; no competition certificate or exception exists for P-14.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1748, "end_character": 2494, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

- [input/sources/reconciliation-correspondence.md](input/sources/reconciliation-correspondence.md) — `F02`

> ## [F02]
> 
> For P-14 the same worksheet takes EUR 24,999.994 and rounds to EUR 24,999.99, because the fractional part lies below the half-cent boundary. The worksheet states that the two purchases are separate operational requirements and do not aggregate. For P-22 it multiplies total consideration CHF 19,000.00, including freight, by 1.040000 to obtain EUR 19,760.00. A proposed loyalty credit remains discretionary and is not subtracted. P-22 is included to document how the cost definition treats freight and contingent discounts; no supplied report finding depends on whether P-22 has a competition obligation, and its approval history is not part of L01's closed coverage.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 811, "end_character": 1488, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "2b5e3cc9824253cabb8493b6702e9b725dbbb3e61b2d9b5003be58748edcc535", "artifact_directory": "extraction/D00008/attempt-suocatu5"}`.

### Rules

- Nearest-cent half-up rounding changes 24,999.994 to 24,999.99 because the remainder after cents is 0.004, below a half-cent. Revision 2 threshold is inclusive EUR 25,000.

### Assumptions

- Use the supplied fictional HPS clauses and exact documentary inputs within their stated May-June 2029 scope; source authenticity beyond explicit stipulations is not independently established.
- Source-to-symbol transcription is scoped to the cited paragraphs/pages and actual extraction/visual reviews; independently checked numeric/date conversions are retained in arithmetic-check.md.

### Reasoning

- 1. L03 states exact unrounded EUR 24,999.994, no other consideration/VAT/rebates and no aggregating requirement; accepted June 5 receipt invokes revision 2.
- 2. The correct final rounding yields 2,499,999 cents, corroborated explicitly by F02. It does not yield 2,500,000 cents.
- 3. The normalized value is one cent below threshold, so P-14 does not require competition under P02. Both the stated rounding and its obligation conclusion fail.

### Limits

- A valid pre-commitment approval remains necessary even when competition is not required; L03 supplies it.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim05` in module `Audit` (refutes): `Audit.p14Cents = 2499999 ∧ Audit.p14Cents ≠ 2500000 ∧ Audit.competitionRequired 2 Audit.p14Cents = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target022.lean) · [Actual proof log](logs/target-022.log)

### Recommendation

Correct the normalized value to EUR 24,999.99 and remove the asserted competition obligation.

## C06-06

### Exact report claim

`input/report.md#C06-06`

> **C06-06.** Dana Cole validly approved P-15 within her delegation, even though commitment occurred one minute after the delegation expired. Sources: P05, D01, D02, D03, L04.

### Verification question

Was Dana Cole P-15 approval valid at the inclusive delegation expiry, despite commitment one minute later?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0012`

> A purchase requires a written approval identifying the order, value, and supplier, granted strictly before commitment by a person whose authority covers the value and category at the approval instant. Authority limits are inclusive unless a delegation says otherwise. The procurement director has standing authority for all monetary values in this dossier. A delegated manager has only the category, amount, and time range expressly stated in the delegation. An approval at the delegation's inclusive expiry instant is valid if all other conditions hold; a later commitment does not itself invalidate that approval. An approval granted after expiry is not rescued by the fact that the requisition was submitted earlier. Manager approval and completion of competitive solicitation are separate requirements: satisfying one does not imply the other.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[12]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D01`

> ## [D01]
> 
> The procurement director delegates authority to manager Dana Cole for laboratory consumables with normalized purchase value no greater than EUR 15,000.00 per independent requirement. The authority begins at 2029-06-01 00:00 UTC and expires at 2029-06-15 17:00 UTC, inclusive. The amount limit is inclusive. The delegation does not cover instrument acquisitions, emergency declarations, competition waivers, or approval of an aggregate whose combined requirement exceeds the limit. Dana may approve qualifying purchases during this interval even if operational commitment follows after expiry, provided approval still strictly precedes commitment and no approval condition is violated. The authority is measured when the approval is granted, not when a request enters Dana's inbox.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 149, "end_character": 939, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-jht5vv9n"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D02`

> ## [D02]
> 
> The authority register is complete for Dana's delegation and amendments during June 2029. It contains no extension, renewal, oral-authority confirmation, substitute delegation, or suspension. The stated expiry therefore remains controlling. This authority completeness is deliberately narrow: it does not purport to list every procurement approval by every employee. P-15 and P-16 approval events are established by their transaction register entries, while the director's standing authority comes from P05. The laboratory team may continue using Dana as a contact person after expiry, but a person's presence in a directory or continued employment does not renew a formal monetary delegation.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 958, "end_character": 1661, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-jht5vv9n"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D03`

> ## [D03]
> 
> An administrative reminder sent to the purchasing team on June 14 says that the last authorized minute is the minute displayed as 17:00 UTC on June 15. It expressly excludes approvals displayed as 17:01 UTC or later. The timestamps in this dossier are stipulated exact minute events, not uncertain minute-long intervals; neither an implied grace period nor an unrecorded earlier click should be assumed. The reminder also separates value authority from timing authority. An amount exactly at EUR 15,000.00 satisfies the monetary ceiling, but satisfaction of that ceiling does not compensate for a late approval. Conversely, approval at the expiry instant is not late merely because the first second of a later commitment occurs afterward.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1680, "end_character": 2428, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-jht5vv9n"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L01`

> ## [L01]
> 
> This register is complete for commitment amounts, approval events, competitive-solicitation certificates, emergency declarations, retrospective reviews, and exception determinations for P-11, P-12, P-13, P-14, P-15, P-16, R-17, R-18, and E-19 from May 1 through June 30, 2029. An explicit entry “none” means the named event did not occur in that coverage, rather than that a page was omitted. That completeness does not cover P-21, E-20, payment events, or anyone's subjective assessment. The recorded original requirements for these entries were fully known at the times stated. All amounts described as normalized include unavoidable charges, exclude recoverable VAT, and already reflect the specified single final rounding unless an entry instead supplies the exact unrounded currency inputs.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 168, "end_character": 973, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L04`

> ## [L04]
> 
> P-15 is laboratory consumables with normalized value EUR 14,900.00, accepted June 9. Manager Dana Cole granted the written order approval at exactly 2029-06-15 17:00 UTC. Commitment was at 17:01 UTC on the same day. P-16 is separate laboratory consumables with normalized value EUR 15,000.00, accepted June 9. Dana granted its written order approval at 2029-06-15 17:01 UTC, and commitment followed at 17:10 UTC. No director or alternative delegate approved P-16 at any time in this register's coverage, and no later document purports to ratify it retroactively. Neither purchase aggregates with another requirement; each is below the revision 2 competition threshold.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2513, "end_character": 3191, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

### Rules

- P05/D01 measure category, amount and authority time at approval; the delegation expiry is inclusive and later commitment does not invalidate prior approval. Approval must strictly precede commitment.

### Assumptions

- Use the supplied fictional HPS clauses and exact documentary inputs within their stated May-June 2029 scope; source authenticity beyond explicit stipulations is not independently established.
- Source-to-symbol transcription is scoped to the cited paragraphs/pages and actual extraction/visual reviews; independently checked numeric/date conversions are retained in arithmetic-check.md.

### Reasoning

- 1. P-15 is independent laboratory consumables for EUR 14,900, within Dana covered category and inclusive EUR 15,000 ceiling.
- 2. Approval occurred June 15 at exactly 17:00, the last authorized minute; D02 records no delegation change and D03 confirms exact-minute semantics.
- 3. Commitment at 17:01 is later than approval. Authority need not persist until commitment under the explicit rule.
- 4. All applicable approval conditions hold, so the report assertion and its qualification are supported.

### Limits

- This validates the P-15 approval event only, not a general authority extension after 17:00 or an emergency waiver.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim06` in module `Audit` (supports): `Audit.delegatedApproval true 1490000 21180 21181 = true ∧ (21180 : Nat) < 21181`.
  [Model](models/Audit.lean) · [Executed check](checks/Target023.lean) · [Actual proof log](logs/target-023.log)

### Recommendation

Retain the conclusion and identify approval time as the controlling authority instant.

## C06-07

### Exact report claim

`input/report.md#C06-07`

> **C06-07.** Dana Cole validly approved P-16 because EUR 15,000.00 is within her inclusive monetary limit. Sources: P05, D01, D02, D03, L04.

### Verification question

Did P-16 approval at June 15 17:01 satisfy Dana delegation merely because the amount exactly met her EUR 15,000 ceiling?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0012`

> A purchase requires a written approval identifying the order, value, and supplier, granted strictly before commitment by a person whose authority covers the value and category at the approval instant. Authority limits are inclusive unless a delegation says otherwise. The procurement director has standing authority for all monetary values in this dossier. A delegated manager has only the category, amount, and time range expressly stated in the delegation. An approval at the delegation's inclusive expiry instant is valid if all other conditions hold; a later commitment does not itself invalidate that approval. An approval granted after expiry is not rescued by the fact that the requisition was submitted earlier. Manager approval and completion of competitive solicitation are separate requirements: satisfying one does not imply the other.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[12]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D01`

> ## [D01]
> 
> The procurement director delegates authority to manager Dana Cole for laboratory consumables with normalized purchase value no greater than EUR 15,000.00 per independent requirement. The authority begins at 2029-06-01 00:00 UTC and expires at 2029-06-15 17:00 UTC, inclusive. The amount limit is inclusive. The delegation does not cover instrument acquisitions, emergency declarations, competition waivers, or approval of an aggregate whose combined requirement exceeds the limit. Dana may approve qualifying purchases during this interval even if operational commitment follows after expiry, provided approval still strictly precedes commitment and no approval condition is violated. The authority is measured when the approval is granted, not when a request enters Dana's inbox.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 149, "end_character": 939, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-jht5vv9n"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D02`

> ## [D02]
> 
> The authority register is complete for Dana's delegation and amendments during June 2029. It contains no extension, renewal, oral-authority confirmation, substitute delegation, or suspension. The stated expiry therefore remains controlling. This authority completeness is deliberately narrow: it does not purport to list every procurement approval by every employee. P-15 and P-16 approval events are established by their transaction register entries, while the director's standing authority comes from P05. The laboratory team may continue using Dana as a contact person after expiry, but a person's presence in a directory or continued employment does not renew a formal monetary delegation.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 958, "end_character": 1661, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-jht5vv9n"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D03`

> ## [D03]
> 
> An administrative reminder sent to the purchasing team on June 14 says that the last authorized minute is the minute displayed as 17:00 UTC on June 15. It expressly excludes approvals displayed as 17:01 UTC or later. The timestamps in this dossier are stipulated exact minute events, not uncertain minute-long intervals; neither an implied grace period nor an unrecorded earlier click should be assumed. The reminder also separates value authority from timing authority. An amount exactly at EUR 15,000.00 satisfies the monetary ceiling, but satisfaction of that ceiling does not compensate for a late approval. Conversely, approval at the expiry instant is not late merely because the first second of a later commitment occurs afterward.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1680, "end_character": 2428, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-jht5vv9n"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D04`

> ## [D04]
> 
> The director's standing authority includes instruments and consumables above Dana's limit, but the director has not delegated emergency-waiver decisions to Dana. A routine manager signature on a purchase order therefore cannot establish the urgent-safety declaration or its retrospective review. Documents combining several decisions must name each decision expressly. A reviewer can assess a valid approval and a missing competition certificate independently, because neither is a substitute for the other. The register's declaration that P-16 has no alternative approval is an event statement in the explicit coverage L01, not an inference from the fact that the folder happened to contain only Dana's signature page.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2447, "end_character": 3176, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-jht5vv9n"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L01`

> ## [L01]
> 
> This register is complete for commitment amounts, approval events, competitive-solicitation certificates, emergency declarations, retrospective reviews, and exception determinations for P-11, P-12, P-13, P-14, P-15, P-16, R-17, R-18, and E-19 from May 1 through June 30, 2029. An explicit entry “none” means the named event did not occur in that coverage, rather than that a page was omitted. That completeness does not cover P-21, E-20, payment events, or anyone's subjective assessment. The recorded original requirements for these entries were fully known at the times stated. All amounts described as normalized include unavoidable charges, exclude recoverable VAT, and already reflect the specified single final rounding unless an entry instead supplies the exact unrounded currency inputs.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 168, "end_character": 973, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L04`

> ## [L04]
> 
> P-15 is laboratory consumables with normalized value EUR 14,900.00, accepted June 9. Manager Dana Cole granted the written order approval at exactly 2029-06-15 17:00 UTC. Commitment was at 17:01 UTC on the same day. P-16 is separate laboratory consumables with normalized value EUR 15,000.00, accepted June 9. Dana granted its written order approval at 2029-06-15 17:01 UTC, and commitment followed at 17:10 UTC. No director or alternative delegate approved P-16 at any time in this register's coverage, and no later document purports to ratify it retroactively. Neither purchase aggregates with another requirement; each is below the revision 2 competition threshold.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2513, "end_character": 3191, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

### Rules

- Value authority and time authority are conjunctive. D03 expressly excludes 17:01 or later approvals despite an inclusive monetary ceiling. L04 and L01 establish absence of an alternative approval within complete coverage.

### Assumptions

- Use the supplied fictional HPS clauses and exact documentary inputs within their stated May-June 2029 scope; source authenticity beyond explicit stipulations is not independently established.
- Source-to-symbol transcription is scoped to the cited paragraphs/pages and actual extraction/visual reviews; independently checked numeric/date conversions are retained in arithmetic-check.md.

### Reasoning

- 1. P-16 laboratory-consumables category and EUR 15,000 value satisfy Dana category and monetary conditions.
- 2. Her actual approval is at 17:01, one minute after inclusive 17:00 expiry. D02 records no extension or substitute authority.
- 3. Approval before 17:10 commitment cannot cure expired authority at the approval instant. The complete transaction register expressly records no director or alternative delegate approval and no retroactive ratification.
- 4. The reported valid approval is refuted: a true monetary premise does not satisfy the independently failed time condition.

### Limits

- The conclusion uses explicit covered event absence and exact timestamps; it is not inferred merely from a missing signature page.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim07` in module `Audit` (refutes): `(1500000 : Nat) ≤ 1500000 ∧ Audit.delegatedApproval true 1500000 21181 21190 = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target024.lean) · [Actual proof log](logs/target-024.log)

### Recommendation

Record invalid delegated approval and identify the missing valid alternative approval, without treating the monetary ceiling itself as exceeded.

## C06-08

### Exact report claim

`input/report.md#C06-08`

> **C06-08.** R-17 is governed by revision 2 because its June 3 amendment and June 10 commitment occurred after the new revision took effect. Sources: V01, V02, V03.

### Verification question

Does R-17 unchanged original requirement switch to revision 2 because a clerical amendment and commitment occurred after June 1?

### Source evidence

- [input/sources/revision-amendment.pdf.md](input/sources/revision-amendment.pdf.md) — `pdf-page-0002`

> [V01]
> Revision 2 takes effect at 2029-06-01 00:00 UTC. An accepted requisition received before
> that instant remains under revision 1 for its original scope, even if approval, supplier
> selection, commitment, delivery, or invoicing occurs later. An accepted requisition received
> at the exact boundary or afterward uses revision 2. Accepted receipt is the central intake
> service’s timestamp, not the time when an employee drafted an email or a buyer opened a
> task. This amendment changes the threshold but does not retroactively invalidate approvals
> valid under the retained revision. A dashboard field showing the presently published
> standard is not a record of which version governs an individual requisition.

Original: [input/originals/D00009.pdf](input/originals/D00009.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-3230ujwt"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/revision-amendment.pdf.md](input/sources/revision-amendment.pdf.md) — `pdf-page-0003`

> [V02]
> A material scope amendment accepted on or after 2029-06-01 is governed by revision 2 only
> for the additional independently priced requirement introduced by that amendment. It does
> not erase competition obligations for the unchanged original requirement. A change is
> material when it adds a distinct functional requirement or increases unavoidable
> consideration; correcting a contact name or an internal billing code is not material. If an
> original and added requirement satisfy the aggregation rule, the buyer must document the
> aggregation analysis rather than presume that a new request number prevents it. The files
> for the two grandfathering examples state expressly that neither contains an added
> requirement, a price increase, or a genuine material amendment.

Original: [input/originals/D00009.pdf](input/originals/D00009.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 3, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0003.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-3230ujwt"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/revision-amendment.pdf.md](input/sources/revision-amendment.pdf.md) — `pdf-page-0004`

> [V03]
> Accepted requisition R-17 concerns one instrument purchase at EUR 22,500.00. Intake receipt
> occurred at 2029-05-31 23:59 UTC. A June 3 clerical amendment changed the internal contact
> from the field technician to the warehouse supervisor and corrected a cost-center spelling.
> The approved schedule states that the specification, supplier, price, quantity, and
> functional requirement remained unchanged. Commitment occurred on June 10. The amendment did
> not create an additional purchase and does not constitute a material scope amendment under
> V02. The current-version dashboard displayed revision 2 on the day of commitment because
> revision 2 was then the standard’s published version.

Original: [input/originals/D00009.pdf](input/originals/D00009.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 4, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0004.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-3230ujwt"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L05`

> ## [L05]
> 
> R-17 and R-18 have the receipts and unchanged scopes recorded in V03 and V04. Each was committed June 10 after a valid director order approval on June 9. Competitive-solicitation certificate for R-17: none. Exception determination for R-17: none. Competitive-solicitation certificate for R-18: none. Exception determination for R-18: none. E-19 is a separate safety-pump requirement received June 21 for normalized EUR 31,000.00 and committed at 2029-06-22 10:00 UTC. A director's instrument granted order approval and made the emergency declaration at 09:45 that morning. The complete emergency details appear in X01 and X02; no competition certificate exists for E-19.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 3210, "end_character": 3890, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

### Rules

- V01 retains revision 1 for original scope accepted before June 1 00:00. V02 applies revision 2 only to additional independently priced requirements introduced by material changes; clerical contact/billing corrections are not material.

### Assumptions

- Use the supplied fictional HPS clauses and exact documentary inputs within their stated May-June 2029 scope; source authenticity beyond explicit stipulations is not independently established.
- Source-to-symbol transcription is scoped to the cited paragraphs/pages and actual extraction/visual reviews; independently checked numeric/date conversions are retained in arithmetic-check.md.

### Reasoning

- 1. R-17 receipt is May 31 23:59, exactly one minute before transition.
- 2. V03 explicitly says the June 3 amendment changed contact/cost-center spelling only; specification, supplier, price, quantity and functional requirement remained unchanged.
- 3. Neither June 10 commitment nor a current-version dashboard label changes the retained revision. No additional requirement invokes V02.
- 4. Revision 1 governs the original requirement, directly contradicting the revision 2 claim and both stated switching reasons.

### Limits

- The result is about unchanged original scope; a genuine separately priced added requirement could require separate V02 analysis.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim08` in module `Audit` (refutes): `Audit.revision (-1) = 1 ∧ Audit.revision (-1) ≠ 2`.
  [Model](models/Audit.lean) · [Executed check](checks/Target025.lean) · [Actual proof log](logs/target-025.log)

### Recommendation

Use revision 1 for R-17 and preserve the distinction between clerical and material amendments.

## C06-09

### Exact report claim

`input/report.md#C06-09`

> **C06-09.** R-17 required competition at EUR 22,500.00, but the complete register records no competition certificate or exception. Sources: P02, V01, V03, L05.

### Verification question

Does R-17 require competition at normalized EUR 22,500 under retained revision 1, and does complete coverage establish no certificate or exception?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0006`

> The applicable competitive-purchase threshold is inclusive: a normalized purchase value equal to the threshold requires competition unless an established exception applies. Revision 1 uses EUR 20,000.00. Revision 2 uses EUR 25,000.00. Below the applicable threshold, this standard does not require competitive solicitation, although a valid order approval is still required. Competition means inviting at least three independent qualified suppliers, giving each the same specification, recording the responses or documented nonresponses, and signing a comparison before order commitment. A supplier's quote, a market-price screenshot, or an existing relationship is not by itself the prescribed competition. A competition certificate expressly marked complete attests that these steps occurred; a quotation folder without that certificate does not automatically attest them.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/revision-amendment.pdf.md](input/sources/revision-amendment.pdf.md) — `pdf-page-0002`

> [V01]
> Revision 2 takes effect at 2029-06-01 00:00 UTC. An accepted requisition received before
> that instant remains under revision 1 for its original scope, even if approval, supplier
> selection, commitment, delivery, or invoicing occurs later. An accepted requisition received
> at the exact boundary or afterward uses revision 2. Accepted receipt is the central intake
> service’s timestamp, not the time when an employee drafted an email or a buyer opened a
> task. This amendment changes the threshold but does not retroactively invalidate approvals
> valid under the retained revision. A dashboard field showing the presently published
> standard is not a record of which version governs an individual requisition.

Original: [input/originals/D00009.pdf](input/originals/D00009.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-3230ujwt"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/revision-amendment.pdf.md](input/sources/revision-amendment.pdf.md) — `pdf-page-0004`

> [V03]
> Accepted requisition R-17 concerns one instrument purchase at EUR 22,500.00. Intake receipt
> occurred at 2029-05-31 23:59 UTC. A June 3 clerical amendment changed the internal contact
> from the field technician to the warehouse supervisor and corrected a cost-center spelling.
> The approved schedule states that the specification, supplier, price, quantity, and
> functional requirement remained unchanged. Commitment occurred on June 10. The amendment did
> not create an additional purchase and does not constitute a material scope amendment under
> V02. The current-version dashboard displayed revision 2 on the day of commitment because
> revision 2 was then the standard’s published version.

Original: [input/originals/D00009.pdf](input/originals/D00009.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 4, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0004.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-3230ujwt"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L01`

> ## [L01]
> 
> This register is complete for commitment amounts, approval events, competitive-solicitation certificates, emergency declarations, retrospective reviews, and exception determinations for P-11, P-12, P-13, P-14, P-15, P-16, R-17, R-18, and E-19 from May 1 through June 30, 2029. An explicit entry “none” means the named event did not occur in that coverage, rather than that a page was omitted. That completeness does not cover P-21, E-20, payment events, or anyone's subjective assessment. The recorded original requirements for these entries were fully known at the times stated. All amounts described as normalized include unavoidable charges, exclude recoverable VAT, and already reflect the specified single final rounding unless an entry instead supplies the exact unrounded currency inputs.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 168, "end_character": 973, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L05`

> ## [L05]
> 
> R-17 and R-18 have the receipts and unchanged scopes recorded in V03 and V04. Each was committed June 10 after a valid director order approval on June 9. Competitive-solicitation certificate for R-17: none. Exception determination for R-17: none. Competitive-solicitation certificate for R-18: none. Exception determination for R-18: none. E-19 is a separate safety-pump requirement received June 21 for normalized EUR 31,000.00 and committed at 2029-06-22 10:00 UTC. A director's instrument granted order approval and made the emergency declaration at 09:45 that morning. The complete emergency details appear in X01 and X02; no competition certificate exists for E-19.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 3210, "end_character": 3890, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

### Rules

- Revision 1 inclusive threshold is EUR 20,000. L01 completeness covers R-17 competitive certificates and exception determinations; explicit none is event absence in that coverage.

### Assumptions

- Use the supplied fictional HPS clauses and exact documentary inputs within their stated May-June 2029 scope; source authenticity beyond explicit stipulations is not independently established.
- Source-to-symbol transcription is scoped to the cited paragraphs/pages and actual extraction/visual reviews; independently checked numeric/date conversions are retained in arithmetic-check.md.

### Reasoning

- 1. R-17 pre-boundary receipt and unchanged scope retain revision 1. EUR 22,500 exceeds EUR 20,000.
- 2. L05 expressly records competitive-solicitation certificate: none and exception determination: none for R-17.
- 3. The valid June 9 director approval satisfies a separate requirement, but cannot substitute for competition or a fully established exception. Both report components are supported.

### Limits

- Negative event conclusions extend only to the named complete R-17 domain and May-June period; they do not create completeness for E-20/P-21 or payment.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim09` in module `Audit` (supports): `Audit.competitionRequired (Audit.revision (-1)) 2250000 = true ∧ Audit.r17Certificate = false ∧ Audit.r17Exception = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target026.lean) · [Actual proof log](logs/target-026.log)

### Recommendation

Retain the finding and distinguish its competition failure from its valid spending approval.

## C06-10

### Exact report claim

`input/report.md#C06-10`

> **C06-10.** R-18 required competition because its EUR 22,500.00 value exceeds the revision 1 threshold. Sources: P02, V01, V04, L05.

### Verification question

Does R-18 original requirement use revision 1 merely because its EUR 22,500 exceeds that older threshold, despite exact boundary receipt?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0006`

> The applicable competitive-purchase threshold is inclusive: a normalized purchase value equal to the threshold requires competition unless an established exception applies. Revision 1 uses EUR 20,000.00. Revision 2 uses EUR 25,000.00. Below the applicable threshold, this standard does not require competitive solicitation, although a valid order approval is still required. Competition means inviting at least three independent qualified suppliers, giving each the same specification, recording the responses or documented nonresponses, and signing a comparison before order commitment. A supplier's quote, a market-price screenshot, or an existing relationship is not by itself the prescribed competition. A competition certificate expressly marked complete attests that these steps occurred; a quotation folder without that certificate does not automatically attest them.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/revision-amendment.pdf.md](input/sources/revision-amendment.pdf.md) — `pdf-page-0002`

> [V01]
> Revision 2 takes effect at 2029-06-01 00:00 UTC. An accepted requisition received before
> that instant remains under revision 1 for its original scope, even if approval, supplier
> selection, commitment, delivery, or invoicing occurs later. An accepted requisition received
> at the exact boundary or afterward uses revision 2. Accepted receipt is the central intake
> service’s timestamp, not the time when an employee drafted an email or a buyer opened a
> task. This amendment changes the threshold but does not retroactively invalidate approvals
> valid under the retained revision. A dashboard field showing the presently published
> standard is not a record of which version governs an individual requisition.

Original: [input/originals/D00009.pdf](input/originals/D00009.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-3230ujwt"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/revision-amendment.pdf.md](input/sources/revision-amendment.pdf.md) — `pdf-page-0005`

> [V04]
> Accepted requisition R-18 concerns one distinct instrument purchase at EUR 22,500.00.
> Central intake receipt occurred at 2029-06-01 00:00 UTC. The receipt is exact to the minute
> and is not a rounded display of an earlier time. Commitment occurred on June 10. No other
> purchase in this dossier belongs to its operational requirement, and no material amendment
> or aggregation relationship is recorded. The amount is already normalized in euros,
> excluding recoverable VAT and including freight. The boundary timestamp, rather than the
> identical commitment day or identical value shared with R-17, determines the applicable
> revision for this original requirement.

Original: [input/originals/D00009.pdf](input/originals/D00009.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 5, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0005.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-3230ujwt"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L05`

> ## [L05]
> 
> R-17 and R-18 have the receipts and unchanged scopes recorded in V03 and V04. Each was committed June 10 after a valid director order approval on June 9. Competitive-solicitation certificate for R-17: none. Exception determination for R-17: none. Competitive-solicitation certificate for R-18: none. Exception determination for R-18: none. E-19 is a separate safety-pump requirement received June 21 for normalized EUR 31,000.00 and committed at 2029-06-22 10:00 UTC. A director's instrument granted order approval and made the emergency declaration at 09:45 that morning. The complete emergency details appear in X01 and X02; no competition certificate exists for E-19.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 3210, "end_character": 3890, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

### Rules

- V01 assigns accepted receipt at the exact boundary to revision 2. The applicable threshold must be selected before comparing the amount.

### Assumptions

- Use the supplied fictional HPS clauses and exact documentary inputs within their stated May-June 2029 scope; source authenticity beyond explicit stipulations is not independently established.
- Source-to-symbol transcription is scoped to the cited paragraphs/pages and actual extraction/visual reviews; independently checked numeric/date conversions are retained in arithmetic-check.md.

### Reasoning

- 1. V04 gives exact receipt June 1 00:00, not a rounded earlier time, and no aggregation relationship or material added requirement.
- 2. Thus revision 2 applies. EUR 22,500 is below its EUR 25,000 threshold, although above revision 1 EUR 20,000.
- 3. The comparison with the older threshold is numerically true but normatively inapplicable. R-18 does not require competition under the supplied standard.

### Limits

- Identical values and commitment dates do not make R-17 and R-18 share a revision; their accepted receipt timestamps differ across the explicit boundary.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim10` in module `Audit` (refutes): `Audit.revision 0 = 2 ∧ Audit.competitionRequired (Audit.revision 0) 2250000 = false ∧ (2000000 : Nat) ≤ 2250000`.
  [Model](models/Audit.lean) · [Executed check](checks/Target027.lean) · [Actual proof log](logs/target-027.log)

### Recommendation

Apply revision 2 and remove the asserted competition obligation for R-18.

## C06-11

### Exact report claim

`input/report.md#C06-11`

> **C06-11.** E-19 satisfied the urgent-safety exception, including a retrospective review exactly forty-eight hours after commitment. Sources: P06, L05, X01, X02.

### Verification question

Did actual E-19 satisfy every urgent-safety exception condition, including a review at the inclusive forty-eight-hour limit after commitment?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0012`

> A purchase requires a written approval identifying the order, value, and supplier, granted strictly before commitment by a person whose authority covers the value and category at the approval instant. Authority limits are inclusive unless a delegation says otherwise. The procurement director has standing authority for all monetary values in this dossier. A delegated manager has only the category, amount, and time range expressly stated in the delegation. An approval at the delegation's inclusive expiry instant is valid if all other conditions hold; a later commitment does not itself invalidate that approval. An approval granted after expiry is not rescued by the fact that the requisition was submitted earlier. Manager approval and completion of competitive solicitation are separate requirements: satisfying one does not imply the other.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[12]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0014`

> The urgent-safety exception waives only competitive solicitation. It requires a confirmed active safety incident, a director's written emergency declaration identifying the affected requirement strictly before the first commitment, and a director's retrospective review completed at or after that commitment and no later than forty-eight hours afterward. Exactly forty-eight hours is within the limit. An urgent email or a genuine incident alone is insufficient. The declaration must describe the risk addressed by the purchase; mere inconvenience, deferred research, or an expiring quote does not establish the incident condition. A separately valid order approval remains necessary. Neither an emergency declaration nor a later review is automatically an order approval unless the same signed instrument expressly contains both decisions.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[14]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L05`

> ## [L05]
> 
> R-17 and R-18 have the receipts and unchanged scopes recorded in V03 and V04. Each was committed June 10 after a valid director order approval on June 9. Competitive-solicitation certificate for R-17: none. Exception determination for R-17: none. Competitive-solicitation certificate for R-18: none. Exception determination for R-18: none. E-19 is a separate safety-pump requirement received June 21 for normalized EUR 31,000.00 and committed at 2029-06-22 10:00 UTC. A director's instrument granted order approval and made the emergency declaration at 09:45 that morning. The complete emergency details appear in X01 and X02; no competition certificate exists for E-19.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 3210, "end_character": 3890, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X01`

> ## [X01]
> 
> Incident S-19 was a confirmed active safety incident at the eastern wet laboratory on June 22. The failure of a circulation pump created a documented risk of dangerous reagent overheating while shutdown equipment was being prepared. The safety officer confirmed that the risk was active at 09:30 UTC and identified the replacement pump requirement E-19 as the immediate control. This confirmation concerns a real incident within the synthetic story, not merely an operator's belief or a claim that delay would disrupt research. No fact in this file connects E-19 to the sensor-rack purchases P-11 or P-12; the pump incident cannot supply a missing exception for those earlier commitments.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 153, "end_character": 851, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-oumqo1ga"}`.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X02`

> ## [X02]
> 
> At 2029-06-22 09:45 UTC, the director signed instrument EM-19, naming the active incident, pump requirement, supplier, and EUR 31,000.00 value. The instrument expressly grants order approval and makes the urgent-safety emergency declaration. E-19 commitment occurred at 10:00 UTC. The director completed and signed the retrospective review at 2029-06-24 10:00 UTC. That review recorded the procurement steps and confirmed that the purchase addressed S-19. There is no uncertainty in either timestamp. The retrospective interval is measured from commitment, not from the earlier incident confirmation or declaration. The record does not suggest that urgency alone would have satisfied the exception without the declaration and timely review.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 870, "end_character": 1620, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-oumqo1ga"}`.

### Rules

- P06 requires confirmed active safety incident, director written declaration strictly before commitment, and director review in the inclusive interval from commitment to +48 hours; order approval remains a separate requirement.

### Assumptions

- Use the supplied fictional HPS clauses and exact documentary inputs within their stated May-June 2029 scope; source authenticity beyond explicit stipulations is not independently established.
- Source-to-symbol transcription is scoped to the cited paragraphs/pages and actual extraction/visual reviews; independently checked numeric/date conversions are retained in arithmetic-check.md.

### Reasoning

- 1. X01 establishes confirmed active reagent-overheating safety incident S-19 and identifies E-19 as the immediate control; it is not mere delay inconvenience.
- 2. X02 records EM-19 at June 22 09:45 expressly making both declaration and order approval and identifying incident, requirement, supplier and EUR 31,000. Commitment is 10:00, so declaration and approval precede it by 15 minutes.
- 3. Review at June 24 10:00 is 2880 minutes after commitment, exactly forty-eight hours. P06 expressly includes equality and measures from commitment, not earlier declaration.
- 4. Every exception condition holds and separate approval is explicit. The claimed exception and endpoint timing are supported.

### Limits

- The exception waives competition only; it neither establishes prudence nor excuses unrelated earlier sensor-rack purchases.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim11` in module `Audit` (supports): `Audit.e19Emergency = true ∧ (33720 - 30840 : Nat) = 2880 ∧ Audit.e19Approval = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target028.lean) · [Actual proof log](logs/target-028.log)

### Recommendation

Retain with all three conjuncts and the express separate order-approval decision.

## C06-12

### Exact report claim

`input/report.md#C06-12`

> **C06-12.** The confirmed urgency of E-19 would have been sufficient for the urgent-safety exception without the director declaration or retrospective review. Sources: P06, X01, X02.

### Verification question

Under P06, would confirmed E-19 urgency alone satisfy the exception in the counterfactual absence of both director declaration and retrospective review?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0014`

> The urgent-safety exception waives only competitive solicitation. It requires a confirmed active safety incident, a director's written emergency declaration identifying the affected requirement strictly before the first commitment, and a director's retrospective review completed at or after that commitment and no later than forty-eight hours afterward. Exactly forty-eight hours is within the limit. An urgent email or a genuine incident alone is insufficient. The declaration must describe the risk addressed by the purchase; mere inconvenience, deferred research, or an expiring quote does not establish the incident condition. A separately valid order approval remains necessary. Neither an emergency declaration nor a later review is automatically an order approval unless the same signed instrument expressly contains both decisions.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[14]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X01`

> ## [X01]
> 
> Incident S-19 was a confirmed active safety incident at the eastern wet laboratory on June 22. The failure of a circulation pump created a documented risk of dangerous reagent overheating while shutdown equipment was being prepared. The safety officer confirmed that the risk was active at 09:30 UTC and identified the replacement pump requirement E-19 as the immediate control. This confirmation concerns a real incident within the synthetic story, not merely an operator's belief or a claim that delay would disrupt research. No fact in this file connects E-19 to the sensor-rack purchases P-11 or P-12; the pump incident cannot supply a missing exception for those earlier commitments.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 153, "end_character": 851, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-oumqo1ga"}`.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X02`

> ## [X02]
> 
> At 2029-06-22 09:45 UTC, the director signed instrument EM-19, naming the active incident, pump requirement, supplier, and EUR 31,000.00 value. The instrument expressly grants order approval and makes the urgent-safety emergency declaration. E-19 commitment occurred at 10:00 UTC. The director completed and signed the retrospective review at 2029-06-24 10:00 UTC. That review recorded the procurement steps and confirmed that the purchase addressed S-19. There is no uncertainty in either timestamp. The retrospective interval is measured from commitment, not from the earlier incident confirmation or declaration. The record does not suggest that urgency alone would have satisfied the exception without the declaration and timely review.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 870, "end_character": 1620, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-oumqo1ga"}`.

### Rules

- P06 requires all three conditions and explicitly states a genuine incident alone is insufficient. A counterfactual omitting required conjuncts cannot inherit the actual complete exception.

### Assumptions

- Use the supplied fictional HPS clauses and exact documentary inputs within their stated May-June 2029 scope; source authenticity beyond explicit stipulations is not independently established.
- Source-to-symbol transcription is scoped to the cited paragraphs/pages and actual extraction/visual reviews; independently checked numeric/date conversions are retained in arithmetic-check.md.

### Reasoning

- 1. Actual X01 confirms urgency, and actual X02 supplies the other two conditions.
- 2. The report asks whether urgency would suffice without those conditions. P06 expressly denies that sufficiency.
- 3. In the scoped hypothetical model, incident=true but declaration and review absent yields exception=false. This is a counterexample to urgency-alone sufficiency, and direct refutation of the report counterfactual rule claim.

### Limits

- The theorem does not assert that actual E-19 lacked declaration/review or failed the exception; actual E-19 is supported in C06-11.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim12` in module `Audit` (refutes): `Audit.emergency true none none 30840 = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target029.lean) · [Actual proof log](logs/target-029.log)

### Recommendation

Replace the counterfactual with the conjunctive rule: urgency is necessary here but insufficient alone.

## C06-13

### Exact report claim

`input/report.md#C06-13`

> **C06-13.** E-20 qualifies for the proprietary-compatibility exception because Pelican is the only warranty-certified vendor. Sources: P07, V06, X03, X04, X05.

### Verification question

Does sole current warranty-certified vendor status establish E-20 proprietary-compatibility exception without the governing Annex Q test, certification rules and final determination?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0016`

> The proprietary-compatibility exception may waive competition when the required component has an only compatible source within the meaning of Annex Q. Annex Q supplies the governing compatibility test, required certification, and treatment of technically workable substitute components. This operative clause does not say whether compatibility is determined by physical interoperability, warranty certification, or another test. Evidence that one vendor is the sole certified vendor does not automatically resolve the unspecified Annex Q standard. Annex Q is a normative attachment, and its absence does not mean its conditions are waived, satisfied, or impossible to satisfy. The dossier's declaration that an attachment is missing concerns the supplied package, not every copy that might exist elsewhere.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[16]", "paragraph_index_in_story": 16, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/revision-amendment.pdf.md](input/sources/revision-amendment.pdf.md) — `pdf-page-0007`

> [V06]
> The transition package contains the full operative standard, this amendment, the named
> purchase register, delegation notice, exception file, attestation scans, and reconciliation
> correspondence. Annex Q was not supplied. The transition package does not contain a separate
> Annex Q deadline, compatibility checklist, certification rule, or written interpretation
> adopted by the director. In particular, the administrative phrase "all attachments
> transferred except Q" is a complete inventory statement about this package; it is not an
> assertion that no employee holds Annex Q or that no procurement event occurred outside the
> explicitly complete transaction coverage. This distinction remains relevant when a report
> attempts to infer event absence from a missing attachment.

Original: [input/originals/D00009.pdf](input/originals/D00009.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 7, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0007.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-3230ujwt"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X03`

> ## [X03]
> 
> E-20 is a June 25 requirement for an underwater connector assembly with normalized value EUR 28,000.00. No competitive solicitation was conducted, and no urgent-safety incident or emergency declaration is claimed for it. A valid director order approval exists, but the file contains only a proposed proprietary-compatibility exception, not a final Annex Q determination. Pelican Instruments is the only vendor certified by the existing system warranty provider. A separate engineering note demonstrates that a rival connector can physically mate with the interface and pass an electrical bench test. Neither note reproduces Annex Q or claims authority to interpret its governing definition. The proposition that only one source is compatible therefore depends on the missing standard rather than on arithmetic.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1639, "end_character": 2459, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-oumqo1ga"}`.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X04`

> ## [X04]
> 
> The warranty provider's letter limits its statement to the current certification list. It says it has not assessed the rival component for warranty eligibility. The rival vendor's test report limits its statement to mechanical fit and bench electrical behavior, excluding saltwater durability and warranty acceptance. These are different propositions, not directly contradictory claims about one clearly defined compatibility test. The purchasing team asked whether the standard means functional interchangeability or warranty-certified interchangeability; no answer is in the transferred package. A conclusion that E-20 certainly qualifies, or certainly cannot qualify, would require a supplied interpretation or Annex Q text that the current evidence lacks.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2478, "end_character": 3247, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-oumqo1ga"}`.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X05`

> ## [X05]
> 
> The exception file is complete for what the purchasing team transferred to the review package, but it is not a universal inventory of evidence held by suppliers, warranty administrators, or other Harbor departments. The absence of Annex Q is expressly acknowledged by the transition inventory. The file does not report that Annex Q was revoked, waived, blank, or impossible to obtain. The director's order approval for E-20 establishes spending authority only; it does not purport to resolve the compatibility question or to convert a proposed exception into an established exception. A prudent reviewer may request the annex and final determination without claiming that the underlying purchase is necessarily unlawful or that a compatibility exception is necessarily false.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 3266, "end_character": 4051, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-oumqo1ga"}`.

### Rules

- P07 reserves the definition of compatibility, certification and substitutes to Annex Q. Missing Annex Q does not mean conditions are waived, satisfied or impossible. Spending approval is distinct from a competition exception.

### Assumptions

- Treat X03/X04 as scoped technical/certification evidence and V06/X05 as package-level inventory only. Alternative tests are hypothetical, not invented operative rules.

### Reasoning

- 1. X03 supports the factual premise that Pelican is the sole currently warranty-certified vendor and records a proposed exception only.
- 2. X04 limits the warranty evidence to its current certification list and says the rival was not assessed for warranty eligibility. Neither source has authority to define Annex Q.
- 3. V06/X05 establish that Annex Q and a director-adopted interpretation are not supplied; no final Annex Q determination is in the file.
- 4. A warranty-only reading and physical-interchangeability reading give opposite only-compatible-source answers on the known evidence. The auxiliary theorem demonstrates definition dependence, not actual annex content or complete exception qualification.
- 5. The positive qualification claim has insufficient support. It is not disproved merely because Annex Q is missing.

### Limits

- The two candidate tests illustrate missing normative meaning; neither is asserted as the operative Annex Q, and other required certification steps may exist. No actual exception verdict follows.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **auxiliary**.

### Formal evidence

- `Audit.compatibilityAlternatives` in module `Audit` (auxiliary): `Audit.onlyCompatible .warranty true true = true ∧ Audit.onlyCompatible .physical true true = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target030.lean) · [Actual proof log](logs/target-030.log)

### Recommendation

Obtain Annex Q, any adopted interpretation and the final scoped exception determination before claiming qualification.

## C06-14

### Exact report claim

`input/report.md#C06-14`

> **C06-14.** E-20 cannot qualify for the proprietary-compatibility exception because the rival connector passes a physical-fit and electrical bench test. Sources: P07, V06, X03, X04.

### Verification question

Does the rival connector passing mechanical-fit and electrical bench tests rule out E-20 proprietary exception without knowing Annex Q compatibility criteria?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0016`

> The proprietary-compatibility exception may waive competition when the required component has an only compatible source within the meaning of Annex Q. Annex Q supplies the governing compatibility test, required certification, and treatment of technically workable substitute components. This operative clause does not say whether compatibility is determined by physical interoperability, warranty certification, or another test. Evidence that one vendor is the sole certified vendor does not automatically resolve the unspecified Annex Q standard. Annex Q is a normative attachment, and its absence does not mean its conditions are waived, satisfied, or impossible to satisfy. The dossier's declaration that an attachment is missing concerns the supplied package, not every copy that might exist elsewhere.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[16]", "paragraph_index_in_story": 16, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/revision-amendment.pdf.md](input/sources/revision-amendment.pdf.md) — `pdf-page-0007`

> [V06]
> The transition package contains the full operative standard, this amendment, the named
> purchase register, delegation notice, exception file, attestation scans, and reconciliation
> correspondence. Annex Q was not supplied. The transition package does not contain a separate
> Annex Q deadline, compatibility checklist, certification rule, or written interpretation
> adopted by the director. In particular, the administrative phrase "all attachments
> transferred except Q" is a complete inventory statement about this package; it is not an
> assertion that no employee holds Annex Q or that no procurement event occurred outside the
> explicitly complete transaction coverage. This distinction remains relevant when a report
> attempts to infer event absence from a missing attachment.

Original: [input/originals/D00009.pdf](input/originals/D00009.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 7, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0007.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-3230ujwt"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X03`

> ## [X03]
> 
> E-20 is a June 25 requirement for an underwater connector assembly with normalized value EUR 28,000.00. No competitive solicitation was conducted, and no urgent-safety incident or emergency declaration is claimed for it. A valid director order approval exists, but the file contains only a proposed proprietary-compatibility exception, not a final Annex Q determination. Pelican Instruments is the only vendor certified by the existing system warranty provider. A separate engineering note demonstrates that a rival connector can physically mate with the interface and pass an electrical bench test. Neither note reproduces Annex Q or claims authority to interpret its governing definition. The proposition that only one source is compatible therefore depends on the missing standard rather than on arithmetic.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1639, "end_character": 2459, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-oumqo1ga"}`.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X04`

> ## [X04]
> 
> The warranty provider's letter limits its statement to the current certification list. It says it has not assessed the rival component for warranty eligibility. The rival vendor's test report limits its statement to mechanical fit and bench electrical behavior, excluding saltwater durability and warranty acceptance. These are different propositions, not directly contradictory claims about one clearly defined compatibility test. The purchasing team asked whether the standard means functional interchangeability or warranty-certified interchangeability; no answer is in the transferred package. A conclusion that E-20 certainly qualifies, or certainly cannot qualify, would require a supplied interpretation or Annex Q text that the current evidence lacks.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2478, "end_character": 3247, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-oumqo1ga"}`.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X05`

> ## [X05]
> 
> The exception file is complete for what the purchasing team transferred to the review package, but it is not a universal inventory of evidence held by suppliers, warranty administrators, or other Harbor departments. The absence of Annex Q is expressly acknowledged by the transition inventory. The file does not report that Annex Q was revoked, waived, blank, or impossible to obtain. The director's order approval for E-20 establishes spending authority only; it does not purport to resolve the compatibility question or to convert a proposed exception into an established exception. A prudent reviewer may request the annex and final determination without claiming that the underlying purchase is necessarily unlawful or that a compatibility exception is necessarily false.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 3266, "end_character": 4051, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-oumqo1ga"}`.

### Rules

- The governing compatibility test comes from Annex Q, not automatically from a physical/electrical bench test. Different scoped technical propositions are not contradictory testimony about a single defined criterion.

### Assumptions

- No physical or warranty test is silently chosen as controlling; X04 limitations are retained.

### Reasoning

- 1. The rival bench-test success is affirmative evidence of mechanical/electrical behavior, but X04 excludes saltwater durability and warranty acceptance.
- 2. Pelican sole current certification and rival bench success can both be true. Their coexistence does not settle which concept Annex Q requires.
- 3. Under a hypothetical warranty criterion the known evidence can support sole-source status; under a physical criterion it does not. Neither reading is established by the missing annex.
- 4. Therefore the categorical cannot-qualify conclusion is also insufficiently supported; missing definition blocks both blanket qualification and blanket disqualification.

### Limits

- This is missing normative information, not a conflict between mutually negating witnesses and not proof that the exception is true. Bench success alone does not establish every relevant technical dimension.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **auxiliary**.

### Formal evidence

- `Audit.compatibilityAlternatives` in module `Audit` (auxiliary): `Audit.onlyCompatible .warranty true true = true ∧ Audit.onlyCompatible .physical true true = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target030.lean) · [Actual proof log](logs/target-030.log)

### Recommendation

State the evidence under its actual test scope and defer the categorical exception verdict until Annex Q and a final determination are available.

## C06-15

### Exact report claim

`input/report.md#C06-15`

> **C06-15.** The director granted P-21 order approval at 10:00 UTC on June 27. Sources: A01, A02, A03, L01.

### Verification question

What establishes or denies the exact P-21 director approval event at June 27 10:00 UTC, given authentic but unreconciled signed attestations and exclusion from L01 completeness?

### Source evidence

- [input/sources/approval-attestations.scan.pdf.md](input/sources/approval-attestations.scan.pdf.md) — `pdf-page-0002-reviewed-0001`

> [A01]
> Purchasing officer Mara Voss signed an attestation on June 28 at 14:00 UTC. The
> signed statement reads: "For P-21, the director granted the written order approval at
> 10:00 UTC on June 27, before the 10:30 commitment. I examined the signed approval at
> the purchasing desk." The attestation identifies the order, date, person, and
> approval event unambiguously. It does not merely say that approval was requested or
> that Mara expected approval. This statement is positive testimony about the event.
> The scan records the statement and its signature; it does not provide the allegedly
> examined approval document itself.

Original: [input/originals/D00003.pdf](input/originals/D00003.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 2, "origin": {"format": "pdf", "page": 2, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0002-raster.png", "tsv_artifact": "pdf-page-0002.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.7743488556701, "minimum_word_confidence": 78.718094, "confidence_threshold": 85.0, "low_confidence_words": 2, "word_count": 97, "original": "input/originals/D00003.pdf", "original_sha256": "f7fd20aa2be7a439af133f37c3f045a9d3ce14b786760ec8c806c2e8abcf07f8", "artifact_directory": "extraction/D00003/attempt-615zq58t", "source_anchor": "pdf-page-0002", "root_source_anchor": "pdf-page-0002", "reviewer": "audit_01m", "reason": "Viewed original preserved page-2 raster with view_image. The marker is A01 and the granted approval time is 10:00 UTC, not OCR AQ1 or 10:0@. All other paragraph wording compared against the readable original; original OCR retained.", "reviewed_at": "2026-11-04T15:03:19.959530+00:00", "transcription_snapshot": "input/manual-transcriptions/D00003/f2c73ff169fa72a87f8a86ce29319fba80b81b376e3a4b6229800b78686ff70a.txt", "transcription_file_sha256": "35768ae655a05f73e910cd3e329dc75463071a611525aeed414aaa2f34535a38", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/approval-attestations.scan.pdf.md](input/sources/approval-attestations.scan.pdf.md) — `pdf-page-0003-reviewed-0001`

> [A02]
> Records officer Tomas Reed signed a second attestation on June 28 at 14:30 UTC. It
> reads: "The director granted no approval for P-21 at or before 11:00 UTC on June 27.
> In particular, the reported 10:00 approval did not occur." This is an explicit denial
> of the same pre-commitment approval event asserted by Mara, not an observation that
> Tomas failed to locate one attachment. Tomas says he was the approval-session
> recorder but supplies no complete session transcript. The statement does not deny
> that the order was committed at 10:30, which both witnesses accept. It also does not
> suggest that a different person had delegated authority to approve P-21.

Original: [input/originals/D00003.pdf](input/originals/D00003.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 3, "origin": {"format": "pdf", "page": 3, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0003-raster.png", "tsv_artifact": "pdf-page-0003.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 93.84218948623854, "minimum_word_confidence": 0.0, "confidence_threshold": 85.0, "low_confidence_words": 4, "word_count": 109, "original": "input/originals/D00003.pdf", "original_sha256": "f7fd20aa2be7a439af133f37c3f045a9d3ce14b786760ec8c806c2e8abcf07f8", "artifact_directory": "extraction/D00003/attempt-615zq58t", "source_anchor": "pdf-page-0003", "root_source_anchor": "pdf-page-0003", "reviewer": "audit_01m", "reason": "Actually viewed original preserved page-3 raster with view_image. Marker is A02, attestation issue time is 14:30 UTC (not OCR 14:38), and denial cutoff is 11:00 UTC (not 11:0@). The explicit denial of the 10:00 approval was compared word by word; original OCR retained.", "reviewed_at": "2026-11-04T15:03:33.420352+00:00", "transcription_snapshot": "input/manual-transcriptions/D00003/74d057c1ffd7a573949b5264432bbf95d0ac166f21a1a683072c9f16d09c7d65.txt", "transcription_file_sha256": "1bb87ea08d1b8f4dafa7bc70dce45a7d9057d73a66cd9d063ab39c18e29ce0d8", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/approval-attestations.scan.pdf.md](input/sources/approval-attestations.scan.pdf.md) — `pdf-page-0004-reviewed-0001`

> [A03]
> The authenticity of both signatures is stipulated for this synthetic dossier. Neither
> witness has retracted the signed statement. No priority rule, adjudication, amended
> register, or original approval instrument resolving the disagreement is supplied.
> P-21 is deliberately outside the complete transaction coverage of L01. Both
> statements concern the same order and same June 27 morning, so they cannot be
> reconciled by moving one to a different order, date, or timezone. Their contradiction
> concerns approval occurrence. An audit should not transform both attributed
> statements into unconditional world facts from which arbitrary conclusions could be
> derived; nor does signature authenticity make one statement automatically
> authoritative over the other.

Original: [input/originals/D00003.pdf](input/originals/D00003.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 4, "origin": {"format": "pdf", "page": 4, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0004-raster.png", "tsv_artifact": "pdf-page-0004.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.67376844339621, "minimum_word_confidence": 65.073479, "confidence_threshold": 85.0, "low_confidence_words": 2, "word_count": 106, "original": "input/originals/D00003.pdf", "original_sha256": "f7fd20aa2be7a439af133f37c3f045a9d3ce14b786760ec8c806c2e8abcf07f8", "artifact_directory": "extraction/D00003/attempt-615zq58t", "source_anchor": "pdf-page-0004", "root_source_anchor": "pdf-page-0004", "reviewer": "audit_01m", "reason": "Actually viewed original preserved page-4 raster with view_image. Marker is A03 and named register coverage is L01, not OCR AQ3/L@1. Entire paragraph about signature authenticity, no resolution and identical event scope was visually compared; original OCR retained.", "reviewed_at": "2026-11-04T15:03:33.532257+00:00", "transcription_snapshot": "input/manual-transcriptions/D00003/653097fa4c7e85eb684393bda9dd0a3959fec379a0851eefccc17e303dbea4da.txt", "transcription_file_sha256": "8fb79403566e4e68d553034c72b964919a57a2a9e20b95369b9729a709f0fe95", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0018`

> The standard defines compliance as the conjunction of the applicable competition requirement or a fully established competition exception, and valid pre-commitment order approval. The dossier's explicitly complete transaction register may establish event absence within its named coverage. Other files, including incoming correspondence and partial scans, have no general completeness status. Conflicting signed attestations remain attributable statements until an authorized correction or adjudication resolves them. Signature authentication establishes who signed, not that the statement is necessarily true. The standard supplies no metric for describing a transaction as prudent, fair, strategically wise, or commercially elegant. Those descriptions are separate judgments rather than consequences of a threshold calculation.
> 

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[18]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L01`

> ## [L01]
> 
> This register is complete for commitment amounts, approval events, competitive-solicitation certificates, emergency declarations, retrospective reviews, and exception determinations for P-11, P-12, P-13, P-14, P-15, P-16, R-17, R-18, and E-19 from May 1 through June 30, 2029. An explicit entry “none” means the named event did not occur in that coverage, rather than that a page was omitted. That completeness does not cover P-21, E-20, payment events, or anyone's subjective assessment. The recorded original requirements for these entries were fully known at the times stated. All amounts described as normalized include unavoidable charges, exclude recoverable VAT, and already reflect the specified single final rounding unless an entry instead supplies the exact unrounded currency inputs.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 168, "end_character": 973, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

### Rules

- P08 preserves conflicting signed statements until authorized resolution. A03 stipulates signature authenticity but no priority, retraction or adjudication; L01 explicitly excludes P-21.

### Assumptions

- Actual scan pages 2-4 were visually inspected; corrected material characters must be preserved through the controlled transcription record, not silently altered in raw OCR.
- Treat signed statements as testimony only; do not extend L01 closed coverage to P-21.

### Reasoning

- 1. Supporting testimony: visually checked A01 has Mara Voss affirm that the director granted written P-21 order approval at 10:00 before 10:30 commitment and that she examined the document.
- 2. Countertestimony: visually checked A02 has Tomas Reed deny any director approval at/before 11:00 and explicitly deny the reported 10:00 event. This is not merely failure to find an attachment.
- 3. A03 fixes identical order/day and authentic signatures; no source precedence or resolving document is supplied. The record cannot be reconciled by shifting date, person, order or timezone.
- 4. Both support and direct denial remain attributable evidence. The auxiliary model records the opposing testimonies and does not assert both event propositions as world facts. Actual approval is unresolved.

### Limits

- Signature authenticity is stipulated by A03 rather than cryptographically tested by this audit, and does not establish statement truth. Manual visual comparison resolves OCR transcription issues but not the substantive witness disagreement.

### Result

Semantic state: **both**; argument status: **disputed**; formal status: **auxiliary**.

### Formal evidence

- `Audit.claim15Conflict` in module `Audit` (auxiliary): `Audit.maraAffirms = true ∧ Audit.tomasDenies = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target032.lean) · [Actual proof log](logs/target-032.log)

### Recommendation

Display both named accounts and obtain the original approval instrument or an authorized adjudication; do not choose a witness by issue time or signature alone.

## C06-16

### Exact report claim

`input/report.md#C06-16`

> **C06-16.** Harbor paid the P-21 invoice because the packet includes a signed invoice and delivery acceptance. Sources: P01, A04, F03.

### Verification question

Do a signed P-21 invoice and delivery acceptance establish that Harbor paid, when settlement evidence and bank reconciliation were not supplied?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0004`

> Harbor Research Cooperative purchases components for an offshore research laboratory. This standard distinguishes a requisition, an approval, an order commitment, delivery acceptance, an invoice, and payment. A requisition records a proposed need. An approval authorizes a specified transaction within the approving person's authority. An order commitment binds Harbor to purchase. Delivery acceptance confirms receipt or technical acceptance. An invoice requests payment. None of these events automatically establishes that any other event occurred. The assessment period is 1 May through 30 June 2029, and all times in this standard and the transaction records are UTC. No external procurement law forms part of this fictional agreement.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/approval-attestations.scan.pdf.md](input/sources/approval-attestations.scan.pdf.md) — `pdf-page-0005-reviewed-0001`

> [A04]
> P-21 has normalized value EUR 8,000.00 and does not aggregate with another
> requirement. Its commitment record states 2029-06-27 10:30 UTC and identifies the
> supplier. Competition is therefore not the disputed issue. The provided attestation
> packet contains no invoice-payment entry, bank statement, or payment authorization.
> Even if a reviewer resolved the approval disagreement later, that resolution would
> not establish payment. The scans are faithful document reproductions prepared for
> this synthetic fixture. Their visual signatures are textual signature labels, not
> copied real signatures, and their evidentiary content is limited to the attributed
> assertions printed above.

Original: [input/originals/D00003.pdf](input/originals/D00003.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 5, "origin": {"format": "pdf", "page": 5, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0005-raster.png", "tsv_artifact": "pdf-page-0005.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 94.91212301063828, "minimum_word_confidence": 28.830444, "confidence_threshold": 85.0, "low_confidence_words": 3, "word_count": 94, "original": "input/originals/D00003.pdf", "original_sha256": "f7fd20aa2be7a439af133f37c3f045a9d3ce14b786760ec8c806c2e8abcf07f8", "artifact_directory": "extraction/D00003/attempt-615zq58t", "source_anchor": "pdf-page-0005", "root_source_anchor": "pdf-page-0005", "reviewer": "audit_01m", "reason": "Actually viewed original preserved page-5 raster with view_image. Marker is A04, not OCR AQ4. EUR 8,000.00, June 27 10:30 commitment and all negative payment-evidence wording were compared against the original; original OCR retained.", "reviewed_at": "2026-11-04T15:03:33.646113+00:00", "transcription_snapshot": "input/manual-transcriptions/D00003/88f7763d0ec10b10cfbc90b82a9857fe4d8abdb2e5ba545eef5bc49b897e29bd.txt", "transcription_file_sha256": "64eda6f7c9f8621cc75471f06ad1f8be5d19439e1ff546f59a773d544ab814b9", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/reconciliation-correspondence.md](input/sources/reconciliation-correspondence.md) — `F03`

> ## [F03]
> 
> The accounts-payable packet contains a signed supplier invoice for P-21 and a warehouse delivery acceptance. The invoice confirms the supplier's request for EUR 8,000.00 payment and names the order. The warehouse acceptance confirms that the specified package arrived. Neither document states that Harbor paid. A finance reply says the bank reconciliation extract for June 27–30 was not transferred, and the analyst cannot confirm or deny payment from the supplied packet. A report that equates the invoice signature with settlement would therefore rely on a missing event premise, rather than on contradictory affirmative evidence that payment did not occur.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1507, "end_character": 2176, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "2b5e3cc9824253cabb8493b6702e9b725dbbb3e61b2d9b5003be58748edcc535", "artifact_directory": "extraction/D00008/attempt-suocatu5"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L01`

> ## [L01]
> 
> This register is complete for commitment amounts, approval events, competitive-solicitation certificates, emergency declarations, retrospective reviews, and exception determinations for P-11, P-12, P-13, P-14, P-15, P-16, R-17, R-18, and E-19 from May 1 through June 30, 2029. An explicit entry “none” means the named event did not occur in that coverage, rather than that a page was omitted. That completeness does not cover P-21, E-20, payment events, or anyone's subjective assessment. The recorded original requirements for these entries were fully known at the times stated. All amounts described as normalized include unavoidable charges, exclude recoverable VAT, and already reflect the specified single final rounding unless an entry instead supplies the exact unrounded currency inputs.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 168, "end_character": 973, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

### Rules

- P01 distinguishes payment request, delivery acceptance and payment; none automatically establishes another event. L01 explicitly excludes payment history. Missing payment evidence is not a negative settlement fact.

### Assumptions

- The observed invoice and acceptance are accepted as documentary facts; possible paid/unpaid worlds are explanatory countermodels, not actual event findings.

### Reasoning

- 1. F03 establishes a signed invoice requesting EUR 8,000 and a warehouse acceptance confirming delivery. Neither states settlement.
- 2. F03 explicitly says the bank reconciliation was not transferred and finance cannot confirm or deny payment. A04 confirms no payment entry, bank statement or payment authorization in the scan packet.
- 3. The proposed payment inference lacks the settlement event premise. A paid and an unpaid hypothetical history both preserve the supplied invoice and delivery facts.
- 4. The auxiliary countermodel shows failure of entailment. The actual payment claim is undetermined, not refuted by invented nonpayment evidence.

### Limits

- No bank record was inspected and no historical payment/nonpayment conclusion is proved. Resolving the separate approval conflict would still not establish settlement.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **auxiliary**.

### Formal evidence

- `Audit.claim16Alternatives` in module `Audit` (auxiliary): `Audit.possiblePaid.signedInvoice = true ∧ Audit.possibleUnpaid.signedInvoice = true ∧ Audit.possiblePaid.deliveryAccepted = true ∧ Audit.possibleUnpaid.deliveryAccepted = true ∧ Audit.possiblePaid.paid = true ∧ Audit.possibleUnpaid.paid = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target033.lean) · [Actual proof log](logs/target-033.log)

### Recommendation

Replace the asserted payment with confirmed invoice/delivery facts and request settlement or bank-reconciliation evidence.

## C06-17

### Exact report claim

`input/report.md#C06-17`

> **C06-17.** Every purchase in the complete register met both the applicable competition obligation and valid-approval requirement. Sources: P02, P03, P05, P08, L01, L02, L04, L05.

### Verification question

Did every one of the nine explicitly L01-covered purchases satisfy both its applicable competition limb and valid pre-commitment approval limb?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0006`

> The applicable competitive-purchase threshold is inclusive: a normalized purchase value equal to the threshold requires competition unless an established exception applies. Revision 1 uses EUR 20,000.00. Revision 2 uses EUR 25,000.00. Below the applicable threshold, this standard does not require competitive solicitation, although a valid order approval is still required. Competition means inviting at least three independent qualified suppliers, giving each the same specification, recording the responses or documented nonresponses, and signing a comparison before order commitment. A supplier's quote, a market-price screenshot, or an existing relationship is not by itself the prescribed competition. A competition certificate expressly marked complete attests that these steps occurred; a quotation folder without that certificate does not automatically attest them.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0008`

> Two or more purchases aggregate when they concern the same funded project, the same supplier legal entity, and components of one operational requirement committed within an inclusive thirty-calendar-date window. The first commitment date is day one, and the last included date is first date plus twenty-nine calendar days. Different order numbers, cost-center labels, delivery pallets, or invoice dates do not split an otherwise common operational requirement. Purchases do not aggregate merely because the suppliers have similar names or serve the same laboratory. A documented change to a genuinely independent operational requirement can rebut aggregation, but relabeling a single installation cannot. For an aggregate, the competitive threshold applies to the combined normalized value before the first commitment if the full requirement was already known then.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[8]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0012`

> A purchase requires a written approval identifying the order, value, and supplier, granted strictly before commitment by a person whose authority covers the value and category at the approval instant. Authority limits are inclusive unless a delegation says otherwise. The procurement director has standing authority for all monetary values in this dossier. A delegated manager has only the category, amount, and time range expressly stated in the delegation. An approval at the delegation's inclusive expiry instant is valid if all other conditions hold; a later commitment does not itself invalidate that approval. An approval granted after expiry is not rescued by the fact that the requisition was submitted earlier. Manager approval and completion of competitive solicitation are separate requirements: satisfying one does not imply the other.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[12]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0018`

> The standard defines compliance as the conjunction of the applicable competition requirement or a fully established competition exception, and valid pre-commitment order approval. The dossier's explicitly complete transaction register may establish event absence within its named coverage. Other files, including incoming correspondence and partial scans, have no general completeness status. Conflicting signed attestations remain attributable statements until an authorized correction or adjudication resolves them. Signature authentication establishes who signed, not that the statement is necessarily true. The standard supplies no metric for describing a transaction as prudent, fair, strategically wise, or commercially elegant. Those descriptions are separate judgments rather than consequences of a threshold calculation.
> 

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[18]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/revision-amendment.pdf.md](input/sources/revision-amendment.pdf.md) — `pdf-page-0002`

> [V01]
> Revision 2 takes effect at 2029-06-01 00:00 UTC. An accepted requisition received before
> that instant remains under revision 1 for its original scope, even if approval, supplier
> selection, commitment, delivery, or invoicing occurs later. An accepted requisition received
> at the exact boundary or afterward uses revision 2. Accepted receipt is the central intake
> service’s timestamp, not the time when an employee drafted an email or a buyer opened a
> task. This amendment changes the threshold but does not retroactively invalidate approvals
> valid under the retained revision. A dashboard field showing the presently published
> standard is not a record of which version governs an individual requisition.

Original: [input/originals/D00009.pdf](input/originals/D00009.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-3230ujwt"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L01`

> ## [L01]
> 
> This register is complete for commitment amounts, approval events, competitive-solicitation certificates, emergency declarations, retrospective reviews, and exception determinations for P-11, P-12, P-13, P-14, P-15, P-16, R-17, R-18, and E-19 from May 1 through June 30, 2029. An explicit entry “none” means the named event did not occur in that coverage, rather than that a page was omitted. That completeness does not cover P-21, E-20, payment events, or anyone's subjective assessment. The recorded original requirements for these entries were fully known at the times stated. All amounts described as normalized include unavoidable charges, exclude recoverable VAT, and already reflect the specified single final rounding unless an entry instead supplies the exact unrounded currency inputs.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 168, "end_character": 973, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L02`

> ## [L02]
> 
> P-11 and P-12 buy the two halves of one sensor-rack installation for project TIDE-4 from the same legal supplier, Pelican Instruments Ltd. The combined requirement and both prices were approved as a technical specification on May 28. Accepted requisition R-11 was received June 1 at 09:00 UTC. P-11 was committed June 3 for normalized EUR 12,400.00; P-12 was committed June 20 for normalized EUR 12,600.00. The two orders have different cost-center suffixes and delivery pallets, but neither changes the shared functional requirement. Director order approvals were granted June 2 and June 19 respectively. Competitive-solicitation certificate: none. Emergency declaration: none. Other competition exception determination: none.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 992, "end_character": 1729, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L03`

> ## [L03]
> 
> P-13 was received June 4 and committed June 12. Its exact contractual USD amount and fixed conversion rate are in V05. No other purchase aggregates with it. A complete three-supplier competition certificate was signed June 10, and a director order approval was granted June 11. The buyer's worksheet retained the exact rational converted value before the final cent rounding; the public purchase dashboard displayed the rounded normalized amount. P-14, a separate requirement received June 5, has an exact unrounded EUR consideration of 24,999.994 and was committed June 12. It has no other charges, rebates, VAT included, or aggregating purchase. A director approved it June 11; no competition certificate or exception exists for P-14.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1748, "end_character": 2494, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L04`

> ## [L04]
> 
> P-15 is laboratory consumables with normalized value EUR 14,900.00, accepted June 9. Manager Dana Cole granted the written order approval at exactly 2029-06-15 17:00 UTC. Commitment was at 17:01 UTC on the same day. P-16 is separate laboratory consumables with normalized value EUR 15,000.00, accepted June 9. Dana granted its written order approval at 2029-06-15 17:01 UTC, and commitment followed at 17:10 UTC. No director or alternative delegate approved P-16 at any time in this register's coverage, and no later document purports to ratify it retroactively. Neither purchase aggregates with another requirement; each is below the revision 2 competition threshold.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2513, "end_character": 3191, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L05`

> ## [L05]
> 
> R-17 and R-18 have the receipts and unchanged scopes recorded in V03 and V04. Each was committed June 10 after a valid director order approval on June 9. Competitive-solicitation certificate for R-17: none. Exception determination for R-17: none. Competitive-solicitation certificate for R-18: none. Exception determination for R-18: none. E-19 is a separate safety-pump requirement received June 21 for normalized EUR 31,000.00 and committed at 2029-06-22 10:00 UTC. A director's instrument granted order approval and made the emergency declaration at 09:45 that morning. The complete emergency details appear in X01 and X02; no competition certificate exists for E-19.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 3210, "end_character": 3890, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-1mq3dmx9"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D01`

> ## [D01]
> 
> The procurement director delegates authority to manager Dana Cole for laboratory consumables with normalized purchase value no greater than EUR 15,000.00 per independent requirement. The authority begins at 2029-06-01 00:00 UTC and expires at 2029-06-15 17:00 UTC, inclusive. The amount limit is inclusive. The delegation does not cover instrument acquisitions, emergency declarations, competition waivers, or approval of an aggregate whose combined requirement exceeds the limit. Dana may approve qualifying purchases during this interval even if operational commitment follows after expiry, provided approval still strictly precedes commitment and no approval condition is violated. The authority is measured when the approval is granted, not when a request enters Dana's inbox.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 149, "end_character": 939, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-jht5vv9n"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D02`

> ## [D02]
> 
> The authority register is complete for Dana's delegation and amendments during June 2029. It contains no extension, renewal, oral-authority confirmation, substitute delegation, or suspension. The stated expiry therefore remains controlling. This authority completeness is deliberately narrow: it does not purport to list every procurement approval by every employee. P-15 and P-16 approval events are established by their transaction register entries, while the director's standing authority comes from P05. The laboratory team may continue using Dana as a contact person after expiry, but a person's presence in a directory or continued employment does not renew a formal monetary delegation.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 958, "end_character": 1661, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-jht5vv9n"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D03`

> ## [D03]
> 
> An administrative reminder sent to the purchasing team on June 14 says that the last authorized minute is the minute displayed as 17:00 UTC on June 15. It expressly excludes approvals displayed as 17:01 UTC or later. The timestamps in this dossier are stipulated exact minute events, not uncertain minute-long intervals; neither an implied grace period nor an unrecorded earlier click should be assumed. The reminder also separates value authority from timing authority. An amount exactly at EUR 15,000.00 satisfies the monetary ceiling, but satisfaction of that ceiling does not compensate for a late approval. Conversely, approval at the expiry instant is not late merely because the first second of a later commitment occurs afterward.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1680, "end_character": 2428, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-jht5vv9n"}`.

### Rules

- P08 defines compliance conjunctively: satisfy applicable competition or a fully established exception, and possess valid pre-commitment approval. A universal claim fails on a single in-scope actual counterexample.
- L01 complete domain is exactly P-11/P-12/P-13/P-14/P-15/P-16/R-17/R-18/E-19; it excludes E-20/P-21/payment.

### Assumptions

- Use the supplied fictional HPS clauses and exact documentary inputs within their stated May-June 2029 scope; source authenticity beyond explicit stipulations is not independently established.
- Source-to-symbol transcription is scoped to the cited paragraphs/pages and actual extraction/visual reviews; independently checked numeric/date conversions are retained in arithmetic-check.md.

### Reasoning

- 1. P-16 belongs to L01 and has Dana approval one minute after expiry, with no director/alternative approval in complete coverage. Therefore its valid-approval limb fails even though it is below competition threshold.
- 2. P-11/P-12 also belong to L01: their known aggregate equals revision 2 threshold, and L02 explicitly records no competition certificate or exception, despite valid director approvals.
- 3. R-17 independently requires revision 1 competition with no covered certificate or exception.
- 4. The exact universal claim is refuted by P-16 alone; the model proves both its membership and failure, then the negation of universal compliance. It also verifies P-11 as a separate competition-limb counterexample.
- 5. Unresolved E-20 compatibility and P-21 testimony are unnecessary to this refutation and are not incorrectly placed inside L01 coverage.

### Limits

- This disproves all-covered-purchase compliance, not compliance of every individual purchase. The model does not authenticate records or generalize completeness to other orders/events.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim17Witnesses` in module `Audit` (refutes): `Audit.CoveredPurchase.p16 ∈ Audit.covered ∧ Audit.approvalValid .p16 = false ∧ Audit.compliant .p16 = false ∧ Audit.CoveredPurchase.p11 ∈ Audit.covered ∧ Audit.required .p11 = true ∧ Audit.rackCertificate = false ∧ Audit.rackException = false ∧ Audit.compliant .p11 = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target034.lean) · [Actual proof log](logs/target-034.log)

- `Audit.claim17UniversalFalse` in module `Audit` (refutes): `¬ (∀ p, p ∈ Audit.covered → Audit.compliant p = true)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target035.lean) · [Actual proof log](logs/target-035.log)

### Recommendation

Replace the blanket statement with purchase-specific results, explicitly naming P-16 approval failure and the P-11/P-12 and R-17 competition failures.

## C06-18

### Exact report claim

`input/report.md#C06-18`

> **C06-18.** The emergency pump purchase was prudent and commercially elegant. Sources: P08, F05.

### Verification question

Can the supplied standard and attributed retrospective comment establish that the emergency pump purchase was prudent and commercially elegant under a defined operational criterion?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0018`

> The standard defines compliance as the conjunction of the applicable competition requirement or a fully established competition exception, and valid pre-commitment order approval. The dossier's explicitly complete transaction register may establish event absence within its named coverage. Other files, including incoming correspondence and partial scans, have no general completeness status. Conflicting signed attestations remain attributable statements until an authorized correction or adjudication resolves them. Signature authentication establishes who signed, not that the statement is necessarily true. The standard supplies no metric for describing a transaction as prudent, fair, strategically wise, or commercially elegant. Those descriptions are separate judgments rather than consequences of a threshold calculation.
> 

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[18]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/reconciliation-correspondence.md](input/sources/reconciliation-correspondence.md) — `F05`

> ## [F05]
> 
> An internal retrospective comment describes the emergency pump purchase as “prudent and commercially elegant.” The comment provides no decision model, risk utility scale, price benchmark, or evaluative definition. It is an attributed management opinion and does not alter the objective timing of EM-19 or the retrospective review. The same meeting asks the audit team to distinguish correct mathematical calculations, valid authority, established exceptions, missing documents, and disputed testimony. That discussion records stakeholder interests; it does not add a new operative rule, resolve the P-21 contradiction, or supply Annex Q. The fictional standard and its explicit transition clauses remain the controlling rules for the finite dossier.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 2875, "end_character": 3634, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "2b5e3cc9824253cabb8493b6702e9b725dbbb3e61b2d9b5003be58748edcc535", "artifact_directory": "extraction/D00008/attempt-suocatu5"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0014`

> The urgent-safety exception waives only competitive solicitation. It requires a confirmed active safety incident, a director's written emergency declaration identifying the affected requirement strictly before the first commitment, and a director's retrospective review completed at or after that commitment and no later than forty-eight hours afterward. Exactly forty-eight hours is within the limit. An urgent email or a genuine incident alone is insufficient. The declaration must describe the risk addressed by the purchase; mere inconvenience, deferred research, or an expiring quote does not establish the incident condition. A separately valid order approval remains necessary. Neither an emergency declaration nor a later review is automatically an order approval unless the same signed instrument expressly contains both decisions.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[14]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-hcbsj2cp"}`.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X02`

> ## [X02]
> 
> At 2029-06-22 09:45 UTC, the director signed instrument EM-19, naming the active incident, pump requirement, supplier, and EUR 31,000.00 value. The instrument expressly grants order approval and makes the urgent-safety emergency declaration. E-19 commitment occurred at 10:00 UTC. The director completed and signed the retrospective review at 2029-06-24 10:00 UTC. That review recorded the procurement steps and confirmed that the purchase addressed S-19. There is no uncertainty in either timestamp. The retrospective interval is measured from commitment, not from the earlier incident confirmation or declaration. The record does not suggest that urgency alone would have satisfied the exception without the declaration and timely review.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 870, "end_character": 1620, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-oumqo1ga"}`.

### Rules

- P08 explicitly supplies no prudence or commercial-elegance metric. Compliance and a timely emergency process do not themselves define qualitative merit.

### Assumptions

- No unstated utility model, market benchmark or procurement custom is introduced.

### Reasoning

- 1. F05 attributes the description to an internal retrospective opinion and supplies no decision model, risk utility scale, price benchmark or evaluative definition.
- 2. P08 separates these evaluations from objective threshold/timing calculations. Actual E-19 exception compliance does not entail either adjective.
- 3. The two qualitative components remain outside formal assessment under the supplied mandate; no proof of their truth or falsity is manufactured.

### Limits

- This is an undefined evaluative criterion, not evidence that the purchase was imprudent or commercially inelegant. The sourced management opinion can be reported as attributed opinion.

### Result

Semantic state: **not_applicable**; argument status: **nonformal**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Attribute the opinion explicitly or agree a measurable decision criterion and supporting evidence before making a formal evaluation.
