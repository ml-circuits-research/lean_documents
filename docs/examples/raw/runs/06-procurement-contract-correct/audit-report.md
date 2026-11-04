# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

[Semantic correspondence review](semantic-review.md)

Extraction inventory: 9 documents; 1 pending, partial or blocked. See [ingestion details](ingestion.json) and [coverage](coverage.md).

## C06-C01

### Exact report claim

`input/report.md#C06-C01`

> **C06-C01.** P-11 and P-12 aggregate as one known requirement of EUR 25,000.00, so competition was required under revision 2 unless an exception applied; the complete register records no competition or exception. Sources: P02, P03, L02, F04.

### Verification question

Do P-11/P-12 meet every aggregation condition and lack the required competition or exception?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0006`

> The applicable competitive-purchase threshold is inclusive: a normalized purchase value equal to the threshold requires competition unless an established exception applies. Revision 1 uses EUR 20,000.00. Revision 2 uses EUR 25,000.00. Below the applicable threshold, this standard does not require competitive solicitation, although a valid order approval is still required. Competition means inviting at least three independent qualified suppliers, giving each the same specification, recording the responses or documented nonresponses, and signing a comparison before order commitment. A supplier's quote, a market-price screenshot, or an existing relationship is not by itself the prescribed competition. A competition certificate expressly marked complete attests that these steps occurred; a quotation folder without that certificate does not automatically attest them.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0008`

> Two or more purchases aggregate when they concern the same funded project, the same supplier legal entity, and components of one operational requirement committed within an inclusive thirty-calendar-date window. The first commitment date is day one, and the last included date is first date plus twenty-nine calendar days. Different order numbers, cost-center labels, delivery pallets, or invoice dates do not split an otherwise common operational requirement. Purchases do not aggregate merely because the suppliers have similar names or serve the same laboratory. A documented change to a genuinely independent operational requirement can rebut aggregation, but relabeling a single installation cannot. For an aggregate, the competitive threshold applies to the combined normalized value before the first commitment if the full requirement was already known then.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[8]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

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
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-ld2896xv"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L01`

> ## [L01]
> 
> This register is complete for commitment amounts, approval events, competitive-solicitation certificates, emergency declarations, retrospective reviews, and exception determinations for P-11, P-12, P-13, P-14, P-15, P-16, R-17, R-18, and E-19 from May 1 through June 30, 2029. An explicit entry “none” means the named event did not occur in that coverage, rather than that a page was omitted. That completeness does not cover P-21, E-20, payment events, or anyone's subjective assessment. The recorded original requirements for these entries were fully known at the times stated. All amounts described as normalized include unavoidable charges, exclude recoverable VAT, and already reflect the specified single final rounding unless an entry instead supplies the exact unrounded currency inputs.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 168, "end_character": 973, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L02`

> ## [L02]
> 
> P-11 and P-12 buy the two halves of one sensor-rack installation for project TIDE-4 from the same legal supplier, Pelican Instruments Ltd. The combined requirement and both prices were approved as a technical specification on May 28. Accepted requisition R-11 was received June 1 at 09:00 UTC. P-11 was committed June 3 for normalized EUR 12,400.00; P-12 was committed June 20 for normalized EUR 12,600.00. The two orders have different cost-center suffixes and delivery pallets, but neither changes the shared functional requirement. Director order approvals were granted June 2 and June 19 respectively. Competitive-solicitation certificate: none. Emergency declaration: none. Other competition exception determination: none.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 992, "end_character": 1729, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

- [input/sources/reconciliation-correspondence.md](input/sources/reconciliation-correspondence.md) — `F04`

> ## [F04]
> 
> The project leader asked why the sensor-rack requirement appeared as two orders. The buyer answered that one pallet needed early delivery while the second could follow on June 20, and that accounting preferred two cost-center suffixes for allocation. The buyer did not claim that the requirements were independent or unknown at first commitment. The underlying May 28 specification already listed both halves. This correspondence corroborates the aggregation facts in L02 without creating a new exception. The director's approvals show permission to commit money, but neither document purports to be a competition certificate or emergency declaration.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2195, "end_character": 2856, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "2b5e3cc9824253cabb8493b6702e9b725dbbb3e61b2d9b5003be58748edcc535", "artifact_directory": "extraction/D00008/attempt-5lhazxlb"}`.

### Rules

- P03 aggregates same project, same legal supplier and one operational requirement within thirty inclusive dates when fully known before first commitment.
- P02 applies the inclusive revision-2 EUR 25000 threshold; L01 closes competition/exception events for these orders.

### Assumptions

- The supplied synthetic records and operative clauses are faithfully transcribed; source authenticity and external procurement law are outside the audit.
- Use exact euro cents after prescribed single rounding and exact UTC minute timestamps. Named source coverage, not general document omission, governs negative event facts.

### Reasoning

- 1. L02 identifies TIDE-4, Pelican Instruments Ltd and two halves of one installation; F04 confirms that different pallets and labels do not create independent requirements.
- 2. Both prices and the full specification were known May 28, before June 3. June 20 minus June 3 is 17 dates, within the 29-date offset limit.
- 3. Receipt June 1 09:00 selects revision 2. 12400+12600=25000 exactly, meeting its inclusive threshold.
- 4. L02 explicitly records competition certificate, emergency declaration and other exception determination as none under L01 completeness. Director spending approvals do not supply competition.

### Limits

- The conclusion is limited to the named synthetic requirement, operative rule and May-June 2029 coverage; it does not authenticate real-world events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.rackObligation` in module `Audit` (supports): `Audit.rackAggregates = true ∧ Audit.rackTotal = 2500000 ∧ Audit.threshold (Audit.revisionAt 540) ≤ Audit.rackTotal ∧ Audit.competitionSatisfied 2 Audit.rackTotal false false = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target017.lean) · [Actual proof log](logs/target-017.log)

### Recommendation

Retain the qualified finding and its precise source references.

## C06-C02

### Exact report claim

`input/report.md#C06-C02`

> **C06-C02.** The combined normalized value of P-11 and P-12 is EUR 25,000.00, using their supplied EUR 12,400.00 and EUR 12,600.00 normalized values. Sources: L02, P04.

### Verification question

Is the combined normalized value exactly EUR 25000?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0010`

> Normalized purchase value is an exact euro amount rounded once to euro cents after the following calculation. Add all unavoidable consideration for the requirement, including freight and installation. Subtract only unconditional rebates already binding at commitment. Exclude separately stated recoverable VAT. Convert the resulting transaction-currency amount using the fixed contractual exchange rate in the approved requisition schedule; this rate, not a later market quote, controls. Carry the conversion as an exact rational number, then round to the nearest cent, with exact half-cent ties rounded upward for these nonnegative amounts. Do not round each intermediate component, truncate fractional cents, round down to a whole euro, or test the threshold against the unrounded result. The synthetic contracts permit fractional transaction-currency cents, so an amount with three decimal places is not automatically a transcription error.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[10]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L01`

> ## [L01]
> 
> This register is complete for commitment amounts, approval events, competitive-solicitation certificates, emergency declarations, retrospective reviews, and exception determinations for P-11, P-12, P-13, P-14, P-15, P-16, R-17, R-18, and E-19 from May 1 through June 30, 2029. An explicit entry “none” means the named event did not occur in that coverage, rather than that a page was omitted. That completeness does not cover P-21, E-20, payment events, or anyone's subjective assessment. The recorded original requirements for these entries were fully known at the times stated. All amounts described as normalized include unavoidable charges, exclude recoverable VAT, and already reflect the specified single final rounding unless an entry instead supplies the exact unrounded currency inputs.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 168, "end_character": 973, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L02`

> ## [L02]
> 
> P-11 and P-12 buy the two halves of one sensor-rack installation for project TIDE-4 from the same legal supplier, Pelican Instruments Ltd. The combined requirement and both prices were approved as a technical specification on May 28. Accepted requisition R-11 was received June 1 at 09:00 UTC. P-11 was committed June 3 for normalized EUR 12,400.00; P-12 was committed June 20 for normalized EUR 12,600.00. The two orders have different cost-center suffixes and delivery pallets, but neither changes the shared functional requirement. Director order approvals were granted June 2 and June 19 respectively. Competitive-solicitation certificate: none. Emergency declaration: none. Other competition exception determination: none.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 992, "end_character": 1729, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

### Rules

- Use supplied already-normalized values exactly once; no further component rounding or VAT adjustment.

### Assumptions

- The supplied synthetic records and operative clauses are faithfully transcribed; source authenticity and external procurement law are outside the audit.
- Use exact euro cents after prescribed single rounding and exact UTC minute timestamps. Named source coverage, not general document omission, governs negative event facts.

### Reasoning

- 1. L01 explains normalized values already include charges and final rounding; L02 gives 1240000 and 1260000 cents.
- 2. Their exact sum is 2500000 cents, or EUR 25000.00.
- 3. No supplied adjustment contradicts those normalized entries.

### Limits

- The conclusion is limited to the named synthetic requirement, operative rule and May-June 2029 coverage; it does not authenticate real-world events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.rackSum` in module `Audit` (supports): `Audit.rackTotal = 2500000`.
  [Model](models/Audit.lean) · [Executed check](checks/Target018.lean) · [Actual proof log](logs/target-018.log)

### Recommendation

Retain the qualified finding and its precise source references.

## C06-C03

### Exact report claim

`input/report.md#C06-C03`

> **C06-C03.** P-13 normalizes to EUR 25,000.00 after converting exact USD 27,777.775 at 0.900000 and rounding once to cents; it reaches the competition threshold, and the register records a completed competition certificate. Sources: P02, P04, V05, L03, F01.

### Verification question

Does P-13 normalize to the threshold, and is timely completed competition recorded?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0006`

> The applicable competitive-purchase threshold is inclusive: a normalized purchase value equal to the threshold requires competition unless an established exception applies. Revision 1 uses EUR 20,000.00. Revision 2 uses EUR 25,000.00. Below the applicable threshold, this standard does not require competitive solicitation, although a valid order approval is still required. Competition means inviting at least three independent qualified suppliers, giving each the same specification, recording the responses or documented nonresponses, and signing a comparison before order commitment. A supplier's quote, a market-price screenshot, or an existing relationship is not by itself the prescribed competition. A competition certificate expressly marked complete attests that these steps occurred; a quotation folder without that certificate does not automatically attest them.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0010`

> Normalized purchase value is an exact euro amount rounded once to euro cents after the following calculation. Add all unavoidable consideration for the requirement, including freight and installation. Subtract only unconditional rebates already binding at commitment. Exclude separately stated recoverable VAT. Convert the resulting transaction-currency amount using the fixed contractual exchange rate in the approved requisition schedule; this rate, not a later market quote, controls. Carry the conversion as an exact rational number, then round to the nearest cent, with exact half-cent ties rounded upward for these nonnegative amounts. Do not round each intermediate component, truncate fractional cents, round down to a whole euro, or test the threshold against the unrounded result. The synthetic contracts permit fractional transaction-currency cents, so an amount with three decimal places is not automatically a transcription error.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[10]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

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
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-ld2896xv"}`.

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
Coordinates: `{"kind": "pdf", "page": 6, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0006.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-ld2896xv"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L01`

> ## [L01]
> 
> This register is complete for commitment amounts, approval events, competitive-solicitation certificates, emergency declarations, retrospective reviews, and exception determinations for P-11, P-12, P-13, P-14, P-15, P-16, R-17, R-18, and E-19 from May 1 through June 30, 2029. An explicit entry “none” means the named event did not occur in that coverage, rather than that a page was omitted. That completeness does not cover P-21, E-20, payment events, or anyone's subjective assessment. The recorded original requirements for these entries were fully known at the times stated. All amounts described as normalized include unavoidable charges, exclude recoverable VAT, and already reflect the specified single final rounding unless an entry instead supplies the exact unrounded currency inputs.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 168, "end_character": 973, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L03`

> ## [L03]
> 
> P-13 was received June 4 and committed June 12. Its exact contractual USD amount and fixed conversion rate are in V05. No other purchase aggregates with it. A complete three-supplier competition certificate was signed June 10, and a director order approval was granted June 11. The buyer's worksheet retained the exact rational converted value before the final cent rounding; the public purchase dashboard displayed the rounded normalized amount. P-14, a separate requirement received June 5, has an exact unrounded EUR consideration of 24,999.994 and was committed June 12. It has no other charges, rebates, VAT included, or aggregating purchase. A director approved it June 11; no competition certificate or exception exists for P-14.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1748, "end_character": 2494, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

- [input/sources/reconciliation-correspondence.md](input/sources/reconciliation-correspondence.md) — `F01`

> ## [F01]
> 
> Finance analyst Nia West reconciled P-13 on June 18. Her working note multiplies USD 27,777.775 by the fixed rate 0.900000 and obtains exact EUR 24,999.9975 before cent rounding. The note applies the prescribed single final nearest-cent rounding and records EUR 25,000.00 as the normalized value. It explicitly warns that comparing the unrounded amount with EUR 25,000.00 would apply the threshold at the wrong stage. The note is arithmetic corroboration, not a replacement for the operative rounding clause. It does not claim that every amount beginning with the digits 24,999 is below the threshold after normalization.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 161, "end_character": 792, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "2b5e3cc9824253cabb8493b6702e9b725dbbb3e61b2d9b5003be58748edcc535", "artifact_directory": "extraction/D00008/attempt-5lhazxlb"}`.

### Rules

- P04 requires exact rational conversion at contractual rate, then nearest-cent rounding with ties upward. Threshold applies after rounding.
- P02 treats a complete competition certificate as attesting prescribed competition before commitment.

### Assumptions

- The supplied synthetic records and operative clauses are faithfully transcribed; source authenticity and external procurement law are outside the audit.
- Use exact euro cents after prescribed single rounding and exact UTC minute timestamps. Named source coverage, not general document omission, governs negative event facts.

### Reasoning

- 1. V05 supplies exact USD 27777.775 and 0.9 EUR/USD, with no extra charges, rebates or VAT adjustments.
- 2. 27777775/1000 ×9/10 =249999975/10000 EUR =24999.9975 EUR; its cent value 2499999.75 rounds to 2500000 cents.
- 3. Receipt June 4 selects revision 2 and the rounded value equals its inclusive EUR 25000 threshold.
- 4. L03 records a complete three-supplier certificate June 10 before June 12 commitment, corroborating competition; F01 independently agrees with the arithmetic.

### Limits

- The conclusion is limited to the named synthetic requirement, operative rule and May-June 2029 coverage; it does not authenticate real-world events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.p13Normalization` in module `Audit` (supports): `Audit.p13Num = 249999975 ∧ Audit.p13Den = 10000 ∧ Audit.p13Cents = 2500000 ∧ Audit.threshold 2 ≤ Audit.p13Cents ∧ (9 : Nat) < 11 ∧ Audit.competitionSatisfied 2 Audit.p13Cents true false = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target019.lean) · [Actual proof log](logs/target-019.log)

### Recommendation

Retain the qualified finding and its precise source references.

## C06-C04

### Exact report claim

`input/report.md#C06-C04`

> **C06-C04.** The pre-rounded P-13 value is EUR 24,999.9975, but testing that intermediate amount against the threshold would use the wrong stage of the prescribed calculation. Sources: P02, P04, V05, F01.

### Verification question

Is the stated intermediate value exact, and would testing it before cent rounding misapply P04?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0006`

> The applicable competitive-purchase threshold is inclusive: a normalized purchase value equal to the threshold requires competition unless an established exception applies. Revision 1 uses EUR 20,000.00. Revision 2 uses EUR 25,000.00. Below the applicable threshold, this standard does not require competitive solicitation, although a valid order approval is still required. Competition means inviting at least three independent qualified suppliers, giving each the same specification, recording the responses or documented nonresponses, and signing a comparison before order commitment. A supplier's quote, a market-price screenshot, or an existing relationship is not by itself the prescribed competition. A competition certificate expressly marked complete attests that these steps occurred; a quotation folder without that certificate does not automatically attest them.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0010`

> Normalized purchase value is an exact euro amount rounded once to euro cents after the following calculation. Add all unavoidable consideration for the requirement, including freight and installation. Subtract only unconditional rebates already binding at commitment. Exclude separately stated recoverable VAT. Convert the resulting transaction-currency amount using the fixed contractual exchange rate in the approved requisition schedule; this rate, not a later market quote, controls. Carry the conversion as an exact rational number, then round to the nearest cent, with exact half-cent ties rounded upward for these nonnegative amounts. Do not round each intermediate component, truncate fractional cents, round down to a whole euro, or test the threshold against the unrounded result. The synthetic contracts permit fractional transaction-currency cents, so an amount with three decimal places is not automatically a transcription error.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[10]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

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
Coordinates: `{"kind": "pdf", "page": 6, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0006.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-ld2896xv"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/reconciliation-correspondence.md](input/sources/reconciliation-correspondence.md) — `F01`

> ## [F01]
> 
> Finance analyst Nia West reconciled P-13 on June 18. Her working note multiplies USD 27,777.775 by the fixed rate 0.900000 and obtains exact EUR 24,999.9975 before cent rounding. The note applies the prescribed single final nearest-cent rounding and records EUR 25,000.00 as the normalized value. It explicitly warns that comparing the unrounded amount with EUR 25,000.00 would apply the threshold at the wrong stage. The note is arithmetic corroboration, not a replacement for the operative rounding clause. It does not claim that every amount beginning with the digits 24,999 is below the threshold after normalization.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 161, "end_character": 792, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "2b5e3cc9824253cabb8493b6702e9b725dbbb3e61b2d9b5003be58748edcc535", "artifact_directory": "extraction/D00008/attempt-5lhazxlb"}`.

### Rules

- P04 explicitly forbids threshold testing against the unrounded conversion; use normalized cents.

### Assumptions

- The supplied synthetic records and operative clauses are faithfully transcribed; source authenticity and external procurement law are outside the audit.
- Use exact euro cents after prescribed single rounding and exact UTC minute timestamps. Named source coverage, not general document omission, governs negative event facts.

### Reasoning

- 1. The exact conversion is 249999975/10000 EUR, or EUR 24999.9975.
- 2. That rational amount is less than EUR 25000, but its rounded normalized amount is exactly EUR 25000.
- 3. The Lean result checks both comparisons. Their divergence identifies why the early threshold test is invalid; F01 expressly warns against it.

### Limits

- The conclusion is limited to the named synthetic requirement, operative rule and May-June 2029 coverage; it does not authenticate real-world events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.p13Intermediate` in module `Audit` (supports): `Audit.p13Num = 249999975 ∧ Audit.p13Den = 10000 ∧ Audit.p13Num < 25000 * Audit.p13Den ∧ ¬ Audit.p13Cents < Audit.threshold 2`.
  [Model](models/Audit.lean) · [Executed check](checks/Target020.lean) · [Actual proof log](logs/target-020.log)

### Recommendation

Retain the qualified finding and its precise source references.

## C06-C05

### Exact report claim

`input/report.md#C06-C05`

> **C06-C05.** P-14 rounds from EUR 24,999.994 to EUR 24,999.99 and, with no aggregating purchase, remains below the revision 2 competition threshold. Sources: P02, P04, L03, F02.

### Verification question

Does P-14 round down to EUR 24999.99 and remain below its applicable threshold without aggregation?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0006`

> The applicable competitive-purchase threshold is inclusive: a normalized purchase value equal to the threshold requires competition unless an established exception applies. Revision 1 uses EUR 20,000.00. Revision 2 uses EUR 25,000.00. Below the applicable threshold, this standard does not require competitive solicitation, although a valid order approval is still required. Competition means inviting at least three independent qualified suppliers, giving each the same specification, recording the responses or documented nonresponses, and signing a comparison before order commitment. A supplier's quote, a market-price screenshot, or an existing relationship is not by itself the prescribed competition. A competition certificate expressly marked complete attests that these steps occurred; a quotation folder without that certificate does not automatically attest them.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0008`

> Two or more purchases aggregate when they concern the same funded project, the same supplier legal entity, and components of one operational requirement committed within an inclusive thirty-calendar-date window. The first commitment date is day one, and the last included date is first date plus twenty-nine calendar days. Different order numbers, cost-center labels, delivery pallets, or invoice dates do not split an otherwise common operational requirement. Purchases do not aggregate merely because the suppliers have similar names or serve the same laboratory. A documented change to a genuinely independent operational requirement can rebut aggregation, but relabeling a single installation cannot. For an aggregate, the competitive threshold applies to the combined normalized value before the first commitment if the full requirement was already known then.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[8]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0010`

> Normalized purchase value is an exact euro amount rounded once to euro cents after the following calculation. Add all unavoidable consideration for the requirement, including freight and installation. Subtract only unconditional rebates already binding at commitment. Exclude separately stated recoverable VAT. Convert the resulting transaction-currency amount using the fixed contractual exchange rate in the approved requisition schedule; this rate, not a later market quote, controls. Carry the conversion as an exact rational number, then round to the nearest cent, with exact half-cent ties rounded upward for these nonnegative amounts. Do not round each intermediate component, truncate fractional cents, round down to a whole euro, or test the threshold against the unrounded result. The synthetic contracts permit fractional transaction-currency cents, so an amount with three decimal places is not automatically a transcription error.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[10]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

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
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-ld2896xv"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L03`

> ## [L03]
> 
> P-13 was received June 4 and committed June 12. Its exact contractual USD amount and fixed conversion rate are in V05. No other purchase aggregates with it. A complete three-supplier competition certificate was signed June 10, and a director order approval was granted June 11. The buyer's worksheet retained the exact rational converted value before the final cent rounding; the public purchase dashboard displayed the rounded normalized amount. P-14, a separate requirement received June 5, has an exact unrounded EUR consideration of 24,999.994 and was committed June 12. It has no other charges, rebates, VAT included, or aggregating purchase. A director approved it June 11; no competition certificate or exception exists for P-14.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1748, "end_character": 2494, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

- [input/sources/reconciliation-correspondence.md](input/sources/reconciliation-correspondence.md) — `F02`

> ## [F02]
> 
> For P-14 the same worksheet takes EUR 24,999.994 and rounds to EUR 24,999.99, because the fractional part lies below the half-cent boundary. The worksheet states that the two purchases are separate operational requirements and do not aggregate. For P-22 it multiplies total consideration CHF 19,000.00, including freight, by 1.040000 to obtain EUR 19,760.00. A proposed loyalty credit remains discretionary and is not subtracted. P-22 is included to document how the cost definition treats freight and contingent discounts; no supplied report finding depends on whether P-22 has a competition obligation, and its approval history is not part of L01's closed coverage.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 811, "end_character": 1488, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "2b5e3cc9824253cabb8493b6702e9b725dbbb3e61b2d9b5003be58748edcc535", "artifact_directory": "extraction/D00008/attempt-5lhazxlb"}`.

### Rules

- Apply final nearest-cent rounding, not truncation as a general rule; no aggregation exists according to L03/F02.

### Assumptions

- The supplied synthetic records and operative clauses are faithfully transcribed; source authenticity and external procurement law are outside the audit.
- Use exact euro cents after prescribed single rounding and exact UTC minute timestamps. Named source coverage, not general document omission, governs negative event facts.

### Reasoning

- 1. P14 exact EUR 24999.994 gives 2499999.4 cents; .4 is below the .5 upward-rounding boundary.
- 2. The prescribed result is 2499999 cents. June 5 receipt selects revision 2, whose 2500000-cent threshold is greater by one cent.
- 3. L03 and F02 explicitly rule out another aggregating purchase. Lack of competition therefore does not breach P02 here; approval remains a separate requirement.

### Limits

- The conclusion is limited to the named synthetic requirement, operative rule and May-June 2029 coverage; it does not authenticate real-world events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.p14Normalization` in module `Audit` (supports): `Audit.roundCents 24999994 1000 = 2499999 ∧ Audit.roundCents 24999994 1000 < Audit.threshold 2`.
  [Model](models/Audit.lean) · [Executed check](checks/Target021.lean) · [Actual proof log](logs/target-021.log)

### Recommendation

Retain the qualified finding and its precise source references.

## C06-C06

### Exact report claim

`input/report.md#C06-C06`

> **C06-C06.** Dana validly approved the EUR 14,900.00 consumables purchase P-15 at the inclusive 17:00 expiry instant, before its 17:01 commitment. Sources: P05, D01, D02, D03, L04.

### Verification question

Was Dana authorized when approving P15 at 17:00, notwithstanding the 17:01 commitment?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0012`

> A purchase requires a written approval identifying the order, value, and supplier, granted strictly before commitment by a person whose authority covers the value and category at the approval instant. Authority limits are inclusive unless a delegation says otherwise. The procurement director has standing authority for all monetary values in this dossier. A delegated manager has only the category, amount, and time range expressly stated in the delegation. An approval at the delegation's inclusive expiry instant is valid if all other conditions hold; a later commitment does not itself invalidate that approval. An approval granted after expiry is not rescued by the fact that the requisition was submitted earlier. Manager approval and completion of competitive solicitation are separate requirements: satisfying one does not imply the other.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[12]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D01`

> ## [D01]
> 
> The procurement director delegates authority to manager Dana Cole for laboratory consumables with normalized purchase value no greater than EUR 15,000.00 per independent requirement. The authority begins at 2029-06-01 00:00 UTC and expires at 2029-06-15 17:00 UTC, inclusive. The amount limit is inclusive. The delegation does not cover instrument acquisitions, emergency declarations, competition waivers, or approval of an aggregate whose combined requirement exceeds the limit. Dana may approve qualifying purchases during this interval even if operational commitment follows after expiry, provided approval still strictly precedes commitment and no approval condition is violated. The authority is measured when the approval is granted, not when a request enters Dana's inbox.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 149, "end_character": 939, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-pws495wo"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D02`

> ## [D02]
> 
> The authority register is complete for Dana's delegation and amendments during June 2029. It contains no extension, renewal, oral-authority confirmation, substitute delegation, or suspension. The stated expiry therefore remains controlling. This authority completeness is deliberately narrow: it does not purport to list every procurement approval by every employee. P-15 and P-16 approval events are established by their transaction register entries, while the director's standing authority comes from P05. The laboratory team may continue using Dana as a contact person after expiry, but a person's presence in a directory or continued employment does not renew a formal monetary delegation.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 958, "end_character": 1661, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-pws495wo"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D03`

> ## [D03]
> 
> An administrative reminder sent to the purchasing team on June 14 says that the last authorized minute is the minute displayed as 17:00 UTC on June 15. It expressly excludes approvals displayed as 17:01 UTC or later. The timestamps in this dossier are stipulated exact minute events, not uncertain minute-long intervals; neither an implied grace period nor an unrecorded earlier click should be assumed. The reminder also separates value authority from timing authority. An amount exactly at EUR 15,000.00 satisfies the monetary ceiling, but satisfaction of that ceiling does not compensate for a late approval. Conversely, approval at the expiry instant is not late merely because the first second of a later commitment occurs afterward.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1680, "end_character": 2428, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-pws495wo"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L04`

> ## [L04]
> 
> P-15 is laboratory consumables with normalized value EUR 14,900.00, accepted June 9. Manager Dana Cole granted the written order approval at exactly 2029-06-15 17:00 UTC. Commitment was at 17:01 UTC on the same day. P-16 is separate laboratory consumables with normalized value EUR 15,000.00, accepted June 9. Dana granted its written order approval at 2029-06-15 17:01 UTC, and commitment followed at 17:10 UTC. No director or alternative delegate approved P-16 at any time in this register's coverage, and no later document purports to ratify it retroactively. Neither purchase aggregates with another requirement; each is below the revision 2 competition threshold.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2513, "end_character": 3191, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

### Rules

- P05 measures authority at approval, requires strictly pre-commitment approval, and does not invalidate it merely because commitment follows expiry.
- D01 covers consumables ≤EUR 15000 through June 15 17:00 inclusive; D02 has no amendments.

### Assumptions

- The supplied synthetic records and operative clauses are faithfully transcribed; source authenticity and external procurement law are outside the audit.
- Use exact euro cents after prescribed single rounding and exact UTC minute timestamps. Named source coverage, not general document omission, governs negative event facts.

### Reasoning

- 1. P15 is consumables worth EUR 14900, inside Dana category and inclusive monetary ceiling.
- 2. The exact approval at June 15 17:00 equals, rather than exceeds, the stated expiry. D03 expressly includes that minute.
- 3. Commitment at 17:01 is strictly later, so all stated authority and chronology requirements hold. The Lean predicate checks category, value, expiry and ordering.

### Limits

- The conclusion is limited to the named synthetic requirement, operative rule and May-June 2029 coverage; it does not authenticate real-world events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.p15Approval` in module `Audit` (supports): `Audit.validDana true 1490000 Audit.expiry (Audit.expiry + 1)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target022.lean) · [Actual proof log](logs/target-022.log)

### Recommendation

Retain the qualified finding and its precise source references.

## C06-C07

### Exact report claim

`input/report.md#C06-C07`

> **C06-C07.** P-16 met Dana's monetary ceiling but its 17:01 approval was after her delegation expired; the complete register records no alternative approval, so the order lacked a valid pre-commitment approval. Sources: P05, D01, D02, D03, L04.

### Verification question

Does P16 fail approval validity despite satisfying the monetary ceiling?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0012`

> A purchase requires a written approval identifying the order, value, and supplier, granted strictly before commitment by a person whose authority covers the value and category at the approval instant. Authority limits are inclusive unless a delegation says otherwise. The procurement director has standing authority for all monetary values in this dossier. A delegated manager has only the category, amount, and time range expressly stated in the delegation. An approval at the delegation's inclusive expiry instant is valid if all other conditions hold; a later commitment does not itself invalidate that approval. An approval granted after expiry is not rescued by the fact that the requisition was submitted earlier. Manager approval and completion of competitive solicitation are separate requirements: satisfying one does not imply the other.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[12]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D01`

> ## [D01]
> 
> The procurement director delegates authority to manager Dana Cole for laboratory consumables with normalized purchase value no greater than EUR 15,000.00 per independent requirement. The authority begins at 2029-06-01 00:00 UTC and expires at 2029-06-15 17:00 UTC, inclusive. The amount limit is inclusive. The delegation does not cover instrument acquisitions, emergency declarations, competition waivers, or approval of an aggregate whose combined requirement exceeds the limit. Dana may approve qualifying purchases during this interval even if operational commitment follows after expiry, provided approval still strictly precedes commitment and no approval condition is violated. The authority is measured when the approval is granted, not when a request enters Dana's inbox.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 149, "end_character": 939, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-pws495wo"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D02`

> ## [D02]
> 
> The authority register is complete for Dana's delegation and amendments during June 2029. It contains no extension, renewal, oral-authority confirmation, substitute delegation, or suspension. The stated expiry therefore remains controlling. This authority completeness is deliberately narrow: it does not purport to list every procurement approval by every employee. P-15 and P-16 approval events are established by their transaction register entries, while the director's standing authority comes from P05. The laboratory team may continue using Dana as a contact person after expiry, but a person's presence in a directory or continued employment does not renew a formal monetary delegation.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 958, "end_character": 1661, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-pws495wo"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D03`

> ## [D03]
> 
> An administrative reminder sent to the purchasing team on June 14 says that the last authorized minute is the minute displayed as 17:00 UTC on June 15. It expressly excludes approvals displayed as 17:01 UTC or later. The timestamps in this dossier are stipulated exact minute events, not uncertain minute-long intervals; neither an implied grace period nor an unrecorded earlier click should be assumed. The reminder also separates value authority from timing authority. An amount exactly at EUR 15,000.00 satisfies the monetary ceiling, but satisfaction of that ceiling does not compensate for a late approval. Conversely, approval at the expiry instant is not late merely because the first second of a later commitment occurs afterward.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1680, "end_character": 2428, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-pws495wo"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D04`

> ## [D04]
> 
> The director's standing authority includes instruments and consumables above Dana's limit, but the director has not delegated emergency-waiver decisions to Dana. A routine manager signature on a purchase order therefore cannot establish the urgent-safety declaration or its retrospective review. Documents combining several decisions must name each decision expressly. A reviewer can assess a valid approval and a missing competition certificate independently, because neither is a substitute for the other. The register's declaration that P-16 has no alternative approval is an event statement in the explicit coverage L01, not an inference from the fact that the folder happened to contain only Dana's signature page.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2447, "end_character": 3176, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-pws495wo"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L01`

> ## [L01]
> 
> This register is complete for commitment amounts, approval events, competitive-solicitation certificates, emergency declarations, retrospective reviews, and exception determinations for P-11, P-12, P-13, P-14, P-15, P-16, R-17, R-18, and E-19 from May 1 through June 30, 2029. An explicit entry “none” means the named event did not occur in that coverage, rather than that a page was omitted. That completeness does not cover P-21, E-20, payment events, or anyone's subjective assessment. The recorded original requirements for these entries were fully known at the times stated. All amounts described as normalized include unavoidable charges, exclude recoverable VAT, and already reflect the specified single final rounding unless an entry instead supplies the exact unrounded currency inputs.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 168, "end_character": 973, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L04`

> ## [L04]
> 
> P-15 is laboratory consumables with normalized value EUR 14,900.00, accepted June 9. Manager Dana Cole granted the written order approval at exactly 2029-06-15 17:00 UTC. Commitment was at 17:01 UTC on the same day. P-16 is separate laboratory consumables with normalized value EUR 15,000.00, accepted June 9. Dana granted its written order approval at 2029-06-15 17:01 UTC, and commitment followed at 17:10 UTC. No director or alternative delegate approved P-16 at any time in this register's coverage, and no later document purports to ratify it retroactively. Neither purchase aggregates with another requirement; each is below the revision 2 competition threshold.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2513, "end_character": 3191, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

### Rules

- Value, category, time and precommitment order are conjunctive conditions; satisfying a monetary ceiling cannot cure expired authority.
- L01/L04 close alternative approvals for P16; D02 closes delegation extensions.

### Assumptions

- The supplied synthetic records and operative clauses are faithfully transcribed; source authenticity and external procurement law are outside the audit.
- Use exact euro cents after prescribed single rounding and exact UTC minute timestamps. Named source coverage, not general document omission, governs negative event facts.

### Reasoning

- 1. EUR 15000 exactly meets the value ceiling and consumables is in scope.
- 2. June 15 17:01 approval exceeds the last authorized minute17:00; no grace period or earlier click may be invented.
- 3. The17:10 commitment is later, but that does not repair expired authority at 17:01.
- 4. L04 expressly excludes any director or alternate approval in the complete period, so the only recorded approval is invalid and no valid approval exists in scope.

### Limits

- The conclusion is limited to the named synthetic requirement, operative rule and May-June 2029 coverage; it does not authenticate real-world events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.p16ApprovalFailure` in module `Audit` (supports): `1500000 ≤ 1500000 ∧ ¬ Audit.validDana true 1500000 (Audit.expiry + 1) (Audit.expiry + 10) ∧ Audit.p16ValidApproval = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target023.lean) · [Actual proof log](logs/target-023.log)

### Recommendation

Retain the qualified finding and its precise source references.

## C06-C08

### Exact report claim

`input/report.md#C06-C08`

> **C06-C08.** R-17 retains revision 1 because accepted receipt preceded the boundary; its June 3 contact and cost-center correction did not materially change scope. Sources: V01, V02, V03.

### Verification question

Does R17 retain revision 1 despite June 3 clerical correction and later commitment?

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
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-ld2896xv"}`.

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
Coordinates: `{"kind": "pdf", "page": 3, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0003.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-ld2896xv"}`.

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
Coordinates: `{"kind": "pdf", "page": 4, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0004.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-ld2896xv"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L05`

> ## [L05]
> 
> R-17 and R-18 have the receipts and unchanged scopes recorded in V03 and V04. Each was committed June 10 after a valid director order approval on June 9. Competitive-solicitation certificate for R-17: none. Exception determination for R-17: none. Competitive-solicitation certificate for R-18: none. Exception determination for R-18: none. E-19 is a separate safety-pump requirement received June 21 for normalized EUR 31,000.00 and committed at 2029-06-22 10:00 UTC. A director's instrument granted order approval and made the emergency declaration at 09:45 that morning. The complete emergency details appear in X01 and X02; no competition certificate exists for E-19.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 3210, "end_character": 3890, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

### Rules

- V01 keeps earlier accepted requisitions under revision 1 for original scope. V02 requires added function or increased consideration for a material amendment.

### Assumptions

- The supplied synthetic records and operative clauses are faithfully transcribed; source authenticity and external procurement law are outside the audit.
- Use exact euro cents after prescribed single rounding and exact UTC minute timestamps. Named source coverage, not general document omission, governs negative event facts.

### Reasoning

- 1. V03 exact accepted receipt May 31 23:59 is one minute before June 1 00:00, so revision 1 applies.
- 2. The contact and cost-center spelling changed, but specification, supplier, price, quantity and function remained unchanged; there is no addition or price increase.
- 3. V02 expressly treats such corrections as nonmaterial. Current-version dashboard and June 10 commitment do not change governing revision.

### Limits

- The conclusion is limited to the named synthetic requirement, operative rule and May-June 2029 coverage; it does not authenticate real-world events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.r17Version` in module `Audit` (supports): `Audit.revisionAt (-1) = 1 ∧ Audit.r17AddedRequirement = false ∧ Audit.r17PriceIncrease = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target024.lean) · [Actual proof log](logs/target-024.log)

### Recommendation

Retain the qualified finding and its precise source references.

## C06-C09

### Exact report claim

`input/report.md#C06-C09`

> **C06-C09.** R-17 exceeded the retained EUR 20,000.00 threshold, and the complete register records neither a competition certificate nor an exception; its separate director order approval does not cure that omission. Sources: P02, V01, V03, L05.

### Verification question

Does R17 fail required competition under its retained revision despite director approval?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0006`

> The applicable competitive-purchase threshold is inclusive: a normalized purchase value equal to the threshold requires competition unless an established exception applies. Revision 1 uses EUR 20,000.00. Revision 2 uses EUR 25,000.00. Below the applicable threshold, this standard does not require competitive solicitation, although a valid order approval is still required. Competition means inviting at least three independent qualified suppliers, giving each the same specification, recording the responses or documented nonresponses, and signing a comparison before order commitment. A supplier's quote, a market-price screenshot, or an existing relationship is not by itself the prescribed competition. A competition certificate expressly marked complete attests that these steps occurred; a quotation folder without that certificate does not automatically attest them.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0012`

> A purchase requires a written approval identifying the order, value, and supplier, granted strictly before commitment by a person whose authority covers the value and category at the approval instant. Authority limits are inclusive unless a delegation says otherwise. The procurement director has standing authority for all monetary values in this dossier. A delegated manager has only the category, amount, and time range expressly stated in the delegation. An approval at the delegation's inclusive expiry instant is valid if all other conditions hold; a later commitment does not itself invalidate that approval. An approval granted after expiry is not rescued by the fact that the requisition was submitted earlier. Manager approval and completion of competitive solicitation are separate requirements: satisfying one does not imply the other.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[12]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0018`

> The standard defines compliance as the conjunction of the applicable competition requirement or a fully established competition exception, and valid pre-commitment order approval. The dossier's explicitly complete transaction register may establish event absence within its named coverage. Other files, including incoming correspondence and partial scans, have no general completeness status. Conflicting signed attestations remain attributable statements until an authorized correction or adjudication resolves them. Signature authentication establishes who signed, not that the statement is necessarily true. The standard supplies no metric for describing a transaction as prudent, fair, strategically wise, or commercially elegant. Those descriptions are separate judgments rather than consequences of a threshold calculation.
> 

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[18]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

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
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-ld2896xv"}`.

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
Coordinates: `{"kind": "pdf", "page": 4, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0004.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-ld2896xv"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L01`

> ## [L01]
> 
> This register is complete for commitment amounts, approval events, competitive-solicitation certificates, emergency declarations, retrospective reviews, and exception determinations for P-11, P-12, P-13, P-14, P-15, P-16, R-17, R-18, and E-19 from May 1 through June 30, 2029. An explicit entry “none” means the named event did not occur in that coverage, rather than that a page was omitted. That completeness does not cover P-21, E-20, payment events, or anyone's subjective assessment. The recorded original requirements for these entries were fully known at the times stated. All amounts described as normalized include unavoidable charges, exclude recoverable VAT, and already reflect the specified single final rounding unless an entry instead supplies the exact unrounded currency inputs.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 168, "end_character": 973, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L05`

> ## [L05]
> 
> R-17 and R-18 have the receipts and unchanged scopes recorded in V03 and V04. Each was committed June 10 after a valid director order approval on June 9. Competitive-solicitation certificate for R-17: none. Exception determination for R-17: none. Competitive-solicitation certificate for R-18: none. Exception determination for R-18: none. E-19 is a separate safety-pump requirement received June 21 for normalized EUR 31,000.00 and committed at 2029-06-22 10:00 UTC. A director's instrument granted order approval and made the emergency declaration at 09:45 that morning. The complete emergency details appear in X01 and X02; no competition certificate exists for E-19.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 3210, "end_character": 3890, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

### Rules

- Revision1 inclusive threshold is EUR 20000. P05/P08 require competition or established exception separately from valid order approval.

### Assumptions

- The supplied synthetic records and operative clauses are faithfully transcribed; source authenticity and external procurement law are outside the audit.
- Use exact euro cents after prescribed single rounding and exact UTC minute timestamps. Named source coverage, not general document omission, governs negative event facts.

### Reasoning

- 1. R17 remains revision 1 and costs EUR 22500, greater than its EUR 20000 threshold.
- 2. L05 explicitly records no competition certificate and no exception, within L01 complete coverage.
- 3. Its June 9 director approval before June 10 commitment satisfies a different requirement. The compliance conjunction still fails its competition limb.

### Limits

- The conclusion is limited to the named synthetic requirement, operative rule and May-June 2029 coverage; it does not authenticate real-world events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.r17CompetitionFailure` in module `Audit` (supports): `Audit.threshold (Audit.revisionAt (-1)) < 2250000 ∧ Audit.competitionSatisfied 1 2250000 false false = false ∧ Audit.compliant (Audit.competitionSatisfied 1 2250000 false false) true = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target025.lean) · [Actual proof log](logs/target-025.log)

### Recommendation

Retain the qualified finding and its precise source references.

## C06-C10

### Exact report claim

`input/report.md#C06-C10`

> **C06-C10.** R-18 was received exactly at the revision 2 boundary and, at EUR 22,500.00 without aggregation, did not require competition under that revision. Sources: P02, V01, V04, L05.

### Verification question

Does R18 avoid a competition obligation under revision 2 at the exact receipt boundary?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0006`

> The applicable competitive-purchase threshold is inclusive: a normalized purchase value equal to the threshold requires competition unless an established exception applies. Revision 1 uses EUR 20,000.00. Revision 2 uses EUR 25,000.00. Below the applicable threshold, this standard does not require competitive solicitation, although a valid order approval is still required. Competition means inviting at least three independent qualified suppliers, giving each the same specification, recording the responses or documented nonresponses, and signing a comparison before order commitment. A supplier's quote, a market-price screenshot, or an existing relationship is not by itself the prescribed competition. A competition certificate expressly marked complete attests that these steps occurred; a quotation folder without that certificate does not automatically attest them.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0008`

> Two or more purchases aggregate when they concern the same funded project, the same supplier legal entity, and components of one operational requirement committed within an inclusive thirty-calendar-date window. The first commitment date is day one, and the last included date is first date plus twenty-nine calendar days. Different order numbers, cost-center labels, delivery pallets, or invoice dates do not split an otherwise common operational requirement. Purchases do not aggregate merely because the suppliers have similar names or serve the same laboratory. A documented change to a genuinely independent operational requirement can rebut aggregation, but relabeling a single installation cannot. For an aggregate, the competitive threshold applies to the combined normalized value before the first commitment if the full requirement was already known then.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[8]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

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
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-ld2896xv"}`.

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
Coordinates: `{"kind": "pdf", "page": 5, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0005.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-ld2896xv"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L05`

> ## [L05]
> 
> R-17 and R-18 have the receipts and unchanged scopes recorded in V03 and V04. Each was committed June 10 after a valid director order approval on June 9. Competitive-solicitation certificate for R-17: none. Exception determination for R-17: none. Competitive-solicitation certificate for R-18: none. Exception determination for R-18: none. E-19 is a separate safety-pump requirement received June 21 for normalized EUR 31,000.00 and committed at 2029-06-22 10:00 UTC. A director's instrument granted order approval and made the emergency declaration at 09:45 that morning. The complete emergency details appear in X01 and X02; no competition certificate exists for E-19.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 3210, "end_character": 3890, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

### Rules

- V01 includes exact boundary in revision 2. Apply normalized independent requirement value to its EUR 25000 threshold.

### Assumptions

- The supplied synthetic records and operative clauses are faithfully transcribed; source authenticity and external procurement law are outside the audit.
- Use exact euro cents after prescribed single rounding and exact UTC minute timestamps. Named source coverage, not general document omission, governs negative event facts.

### Reasoning

- 1. V04 fixes accepted receipt June 1 00:00 exactly, not a rounded earlier timestamp; revision 2 applies.
- 2. EUR 22500 is normalized and no other purchase aggregates or materially amends this requirement.
- 3. 2250000 cents is less than2500000, so P02 does not require competition. This does not exempt the independent approval requirement, which L05 records as satisfied.

### Limits

- The conclusion is limited to the named synthetic requirement, operative rule and May-June 2029 coverage; it does not authenticate real-world events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.r18NoCompetition` in module `Audit` (supports): `Audit.revisionAt 0 = 2 ∧ 2250000 < Audit.threshold (Audit.revisionAt 0) ∧ Audit.competitionSatisfied 2 2250000 false false = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target026.lean) · [Actual proof log](logs/target-026.log)

### Recommendation

Retain the qualified finding and its precise source references.

## C06-C11

### Exact report claim

`input/report.md#C06-C11`

> **C06-C11.** E-19 satisfied the urgent-safety competition exception: active incident, director declaration before commitment, and retrospective review exactly forty-eight hours afterward; its instrument separately granted order approval. Sources: P06, L05, X01, X02.

### Verification question

Does E19 satisfy all urgent-safety exception conditions and separate order approval?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0012`

> A purchase requires a written approval identifying the order, value, and supplier, granted strictly before commitment by a person whose authority covers the value and category at the approval instant. Authority limits are inclusive unless a delegation says otherwise. The procurement director has standing authority for all monetary values in this dossier. A delegated manager has only the category, amount, and time range expressly stated in the delegation. An approval at the delegation's inclusive expiry instant is valid if all other conditions hold; a later commitment does not itself invalidate that approval. An approval granted after expiry is not rescued by the fact that the requisition was submitted earlier. Manager approval and completion of competitive solicitation are separate requirements: satisfying one does not imply the other.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[12]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0014`

> The urgent-safety exception waives only competitive solicitation. It requires a confirmed active safety incident, a director's written emergency declaration identifying the affected requirement strictly before the first commitment, and a director's retrospective review completed at or after that commitment and no later than forty-eight hours afterward. Exactly forty-eight hours is within the limit. An urgent email or a genuine incident alone is insufficient. The declaration must describe the risk addressed by the purchase; mere inconvenience, deferred research, or an expiring quote does not establish the incident condition. A separately valid order approval remains necessary. Neither an emergency declaration nor a later review is automatically an order approval unless the same signed instrument expressly contains both decisions.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[14]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L01`

> ## [L01]
> 
> This register is complete for commitment amounts, approval events, competitive-solicitation certificates, emergency declarations, retrospective reviews, and exception determinations for P-11, P-12, P-13, P-14, P-15, P-16, R-17, R-18, and E-19 from May 1 through June 30, 2029. An explicit entry “none” means the named event did not occur in that coverage, rather than that a page was omitted. That completeness does not cover P-21, E-20, payment events, or anyone's subjective assessment. The recorded original requirements for these entries were fully known at the times stated. All amounts described as normalized include unavoidable charges, exclude recoverable VAT, and already reflect the specified single final rounding unless an entry instead supplies the exact unrounded currency inputs.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 168, "end_character": 973, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L05`

> ## [L05]
> 
> R-17 and R-18 have the receipts and unchanged scopes recorded in V03 and V04. Each was committed June 10 after a valid director order approval on June 9. Competitive-solicitation certificate for R-17: none. Exception determination for R-17: none. Competitive-solicitation certificate for R-18: none. Exception determination for R-18: none. E-19 is a separate safety-pump requirement received June 21 for normalized EUR 31,000.00 and committed at 2029-06-22 10:00 UTC. A director's instrument granted order approval and made the emergency declaration at 09:45 that morning. The complete emergency details appear in X01 and X02; no competition certificate exists for E-19.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 3210, "end_character": 3890, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X01`

> ## [X01]
> 
> Incident S-19 was a confirmed active safety incident at the eastern wet laboratory on June 22. The failure of a circulation pump created a documented risk of dangerous reagent overheating while shutdown equipment was being prepared. The safety officer confirmed that the risk was active at 09:30 UTC and identified the replacement pump requirement E-19 as the immediate control. This confirmation concerns a real incident within the synthetic story, not merely an operator's belief or a claim that delay would disrupt research. No fact in this file connects E-19 to the sensor-rack purchases P-11 or P-12; the pump incident cannot supply a missing exception for those earlier commitments.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 153, "end_character": 851, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-2lc2fbwi"}`.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X02`

> ## [X02]
> 
> At 2029-06-22 09:45 UTC, the director signed instrument EM-19, naming the active incident, pump requirement, supplier, and EUR 31,000.00 value. The instrument expressly grants order approval and makes the urgent-safety emergency declaration. E-19 commitment occurred at 10:00 UTC. The director completed and signed the retrospective review at 2029-06-24 10:00 UTC. That review recorded the procurement steps and confirmed that the purchase addressed S-19. There is no uncertainty in either timestamp. The retrospective interval is measured from commitment, not from the earlier incident confirmation or declaration. The record does not suggest that urgency alone would have satisfied the exception without the declaration and timely review.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 870, "end_character": 1620, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-2lc2fbwi"}`.

### Rules

- P06 requires confirmed active safety incident, specified director declaration before commitment and review from commitment through48 h inclusive. Order approval remains separately necessary.

### Assumptions

- The supplied synthetic records and operative clauses are faithfully transcribed; source authenticity and external procurement law are outside the audit.
- Use exact euro cents after prescribed single rounding and exact UTC minute timestamps. Named source coverage, not general document omission, governs negative event facts.

### Reasoning

- 1. X01 confirms active overheating risk at 09:30 and links E19 to its immediate control, not merely delayed research.
- 2. EM19 atJune22 09:45 identifies incident, requirement, supplier and amount, and expressly contains both declaration and order approval. Commitment follows at 10:00.
- 3. Review June 24 10:00 is exactly two dates after commitment, 2880 minutes=48 hours, within the inclusive limit.
- 4. The model checks declaration-before-commitment and the full interval; source wording independently supplies the dual decisions and director authority.

### Limits

- The conclusion is limited to the named synthetic requirement, operative rule and May-June 2029 coverage; it does not authenticate real-world events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.e19Exception` in module `Audit` (supports): `Audit.urgentException true true true Audit.e19Declaration Audit.e19Commitment Audit.e19Review ∧ Audit.e19Review - Audit.e19Commitment = 48 * 60 ∧ Audit.e19Declaration < Audit.e19Commitment`.
  [Model](models/Audit.lean) · [Executed check](checks/Target027.lean) · [Actual proof log](logs/target-027.log)

### Recommendation

Retain the qualified finding and its precise source references.

## C06-C12

### Exact report claim

`input/report.md#C06-C12`

> **C06-C12.** Urgency alone would not establish the urgent-safety exception: P06 also requires the director declaration and timely retrospective review, both independently present for E-19. Sources: P06, X01, X02.

### Verification question

Is urgency alone insufficient even though E19 has the additional required facts?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0014`

> The urgent-safety exception waives only competitive solicitation. It requires a confirmed active safety incident, a director's written emergency declaration identifying the affected requirement strictly before the first commitment, and a director's retrospective review completed at or after that commitment and no later than forty-eight hours afterward. Exactly forty-eight hours is within the limit. An urgent email or a genuine incident alone is insufficient. The declaration must describe the risk addressed by the purchase; mere inconvenience, deferred research, or an expiring quote does not establish the incident condition. A separately valid order approval remains necessary. Neither an emergency declaration nor a later review is automatically an order approval unless the same signed instrument expressly contains both decisions.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[14]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L05`

> ## [L05]
> 
> R-17 and R-18 have the receipts and unchanged scopes recorded in V03 and V04. Each was committed June 10 after a valid director order approval on June 9. Competitive-solicitation certificate for R-17: none. Exception determination for R-17: none. Competitive-solicitation certificate for R-18: none. Exception determination for R-18: none. E-19 is a separate safety-pump requirement received June 21 for normalized EUR 31,000.00 and committed at 2029-06-22 10:00 UTC. A director's instrument granted order approval and made the emergency declaration at 09:45 that morning. The complete emergency details appear in X01 and X02; no competition certificate exists for E-19.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 3210, "end_character": 3890, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X01`

> ## [X01]
> 
> Incident S-19 was a confirmed active safety incident at the eastern wet laboratory on June 22. The failure of a circulation pump created a documented risk of dangerous reagent overheating while shutdown equipment was being prepared. The safety officer confirmed that the risk was active at 09:30 UTC and identified the replacement pump requirement E-19 as the immediate control. This confirmation concerns a real incident within the synthetic story, not merely an operator's belief or a claim that delay would disrupt research. No fact in this file connects E-19 to the sensor-rack purchases P-11 or P-12; the pump incident cannot supply a missing exception for those earlier commitments.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 153, "end_character": 851, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-2lc2fbwi"}`.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X02`

> ## [X02]
> 
> At 2029-06-22 09:45 UTC, the director signed instrument EM-19, naming the active incident, pump requirement, supplier, and EUR 31,000.00 value. The instrument expressly grants order approval and makes the urgent-safety emergency declaration. E-19 commitment occurred at 10:00 UTC. The director completed and signed the retrospective review at 2029-06-24 10:00 UTC. That review recorded the procurement steps and confirmed that the purchase addressed S-19. There is no uncertainty in either timestamp. The retrospective interval is measured from commitment, not from the earlier incident confirmation or declaration. The record does not suggest that urgency alone would have satisfied the exception without the declaration and timely review.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 870, "end_character": 1620, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-2lc2fbwi"}`.

### Rules

- The exception is a conjunction, not a rule activeIncident→exception. P06 expressly excludes incident-only or urgent-email sufficiency.

### Assumptions

- The supplied synthetic records and operative clauses are faithfully transcribed; source authenticity and external procurement law are outside the audit.
- Use exact euro cents after prescribed single rounding and exact UTC minute timestamps. Named source coverage, not general document omission, governs negative event facts.

### Reasoning

- 1. P06 adds declaration and review to the active-incident condition.
- 2. A model with active incident true but declaration and review absent fails the exception, demonstrating the missing-premise inference.
- 3. For actual E19, X02 independently supplies both additional conditions with09:45<10:00 and exactly48 h review; the separate checked e19Exception target confirms that finite chronology.

### Limits

- The conclusion is limited to the named synthetic requirement, operative rule and May-June 2029 coverage; it does not authenticate real-world events.
- The countermodel does not deny the actual declaration or review; it concerns urgency-only sufficiency. Actual E19 conditions are sourced separately and checked in C06-C11.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **auxiliary**.

### Formal evidence

- `Audit.urgencyInsufficient` in module `Audit` (auxiliary): `¬ Audit.urgentException true false false Audit.e19Declaration Audit.e19Commitment Audit.e19Review`.
  [Model](models/Audit.lean) · [Executed check](checks/Target028.lean) · [Actual proof log](logs/target-028.log)

### Recommendation

Retain the qualified finding and its precise source references.

## C06-C13

### Exact report claim

`input/report.md#C06-C13`

> **C06-C13.** E-20's proprietary-compatibility exception remains unestablished because the supplied package omits Annex Q and a final determination; sole warranty certification does not resolve the unspecified governing test. Sources: P07, V06, X03, X04, X05.

### Verification question

Does the supplied sole-warranty evidence fail to establish E20 proprietary compatibility under missing Annex Q?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0016`

> The proprietary-compatibility exception may waive competition when the required component has an only compatible source within the meaning of Annex Q. Annex Q supplies the governing compatibility test, required certification, and treatment of technically workable substitute components. This operative clause does not say whether compatibility is determined by physical interoperability, warranty certification, or another test. Evidence that one vendor is the sole certified vendor does not automatically resolve the unspecified Annex Q standard. Annex Q is a normative attachment, and its absence does not mean its conditions are waived, satisfied, or impossible to satisfy. The dossier's declaration that an attachment is missing concerns the supplied package, not every copy that might exist elsewhere.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[16]", "paragraph_index_in_story": 16, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

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
Coordinates: `{"kind": "pdf", "page": 7, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0007.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-ld2896xv"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X03`

> ## [X03]
> 
> E-20 is a June 25 requirement for an underwater connector assembly with normalized value EUR 28,000.00. No competitive solicitation was conducted, and no urgent-safety incident or emergency declaration is claimed for it. A valid director order approval exists, but the file contains only a proposed proprietary-compatibility exception, not a final Annex Q determination. Pelican Instruments is the only vendor certified by the existing system warranty provider. A separate engineering note demonstrates that a rival connector can physically mate with the interface and pass an electrical bench test. Neither note reproduces Annex Q or claims authority to interpret its governing definition. The proposition that only one source is compatible therefore depends on the missing standard rather than on arithmetic.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1639, "end_character": 2459, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-2lc2fbwi"}`.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X04`

> ## [X04]
> 
> The warranty provider's letter limits its statement to the current certification list. It says it has not assessed the rival component for warranty eligibility. The rival vendor's test report limits its statement to mechanical fit and bench electrical behavior, excluding saltwater durability and warranty acceptance. These are different propositions, not directly contradictory claims about one clearly defined compatibility test. The purchasing team asked whether the standard means functional interchangeability or warranty-certified interchangeability; no answer is in the transferred package. A conclusion that E-20 certainly qualifies, or certainly cannot qualify, would require a supplied interpretation or Annex Q text that the current evidence lacks.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2478, "end_character": 3247, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-2lc2fbwi"}`.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X05`

> ## [X05]
> 
> The exception file is complete for what the purchasing team transferred to the review package, but it is not a universal inventory of evidence held by suppliers, warranty administrators, or other Harbor departments. The absence of Annex Q is expressly acknowledged by the transition inventory. The file does not report that Annex Q was revoked, waived, blank, or impossible to obtain. The director's order approval for E-20 establishes spending authority only; it does not purport to resolve the compatibility question or to convert a proposed exception into an established exception. A prudent reviewer may request the annex and final determination without claiming that the underlying purchase is necessarily unlawful or that a compatibility exception is necessarily false.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 3266, "end_character": 4051, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-2lc2fbwi"}`.

### Rules

- P07 reserves governing test and certification treatment to Annex Q and rejects automatic inference from sole certification. Attachment absence does not make conditions waived or false.

### Assumptions

- The supplied synthetic records and operative clauses are faithfully transcribed; source authenticity and external procurement law are outside the audit.
- Use exact euro cents after prescribed single rounding and exact UTC minute timestamps. Named source coverage, not general document omission, governs negative event facts.

### Reasoning

- 1. X03 reports only a proposed exception, although a separate director order approval exists; no final Annex Q determination is supplied.
- 2. V06 explicitly says Annex Q and an adopted interpretation are missing. X05 limits completeness to transferred package, not all possible records.
- 3. Sole warranty certification would support a warranty-based only-source test; a physical-interoperability test would differ because the rival passes fit/bench tests. Neither is supplied as the actual governing test.
- 4. The auxiliary model checks those divergent hypothetical readings, supporting the report support-gap finding without declaring the real exception false.

### Limits

- The conclusion is limited to the named synthetic requirement, operative rule and May-June 2029 coverage; it does not authenticate real-world events.
- These are illustrative alternative definitions, not a reconstruction of Annex Q. The actual governing test, required certification and final exception decision remain unavailable.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **auxiliary**.

### Formal evidence

- `Audit.compatibilityOpen` in module `Audit` (auxiliary): `Audit.onlyCompatible Audit.CompatibilityTest.warranty = true ∧ Audit.onlyCompatible Audit.CompatibilityTest.physical = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target029.lean) · [Actual proof log](logs/target-029.log)

### Recommendation

Obtain Annex Q and the applicable final determination; retain uncertainty meanwhile.

## C06-C14

### Exact report claim

`input/report.md#C06-C14`

> **C06-C14.** The rival connector's bench test also does not establish that E-20 is disqualified: functionality and warranty certification address different predicates, while Annex Q supplies the missing governing definition. Sources: P07, V06, X03, X04.

### Verification question

Does the rival bench result fail to establish that E20 cannot qualify?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0016`

> The proprietary-compatibility exception may waive competition when the required component has an only compatible source within the meaning of Annex Q. Annex Q supplies the governing compatibility test, required certification, and treatment of technically workable substitute components. This operative clause does not say whether compatibility is determined by physical interoperability, warranty certification, or another test. Evidence that one vendor is the sole certified vendor does not automatically resolve the unspecified Annex Q standard. Annex Q is a normative attachment, and its absence does not mean its conditions are waived, satisfied, or impossible to satisfy. The dossier's declaration that an attachment is missing concerns the supplied package, not every copy that might exist elsewhere.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[16]", "paragraph_index_in_story": 16, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

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
Coordinates: `{"kind": "pdf", "page": 7, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0007.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-ld2896xv"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X03`

> ## [X03]
> 
> E-20 is a June 25 requirement for an underwater connector assembly with normalized value EUR 28,000.00. No competitive solicitation was conducted, and no urgent-safety incident or emergency declaration is claimed for it. A valid director order approval exists, but the file contains only a proposed proprietary-compatibility exception, not a final Annex Q determination. Pelican Instruments is the only vendor certified by the existing system warranty provider. A separate engineering note demonstrates that a rival connector can physically mate with the interface and pass an electrical bench test. Neither note reproduces Annex Q or claims authority to interpret its governing definition. The proposition that only one source is compatible therefore depends on the missing standard rather than on arithmetic.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1639, "end_character": 2459, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-2lc2fbwi"}`.

- [input/sources/exception-file.md](input/sources/exception-file.md) — `X04`

> ## [X04]
> 
> The warranty provider's letter limits its statement to the current certification list. It says it has not assessed the rival component for warranty eligibility. The rival vendor's test report limits its statement to mechanical fit and bench electrical behavior, excluding saltwater durability and warranty acceptance. These are different propositions, not directly contradictory claims about one clearly defined compatibility test. The purchasing team asked whether the standard means functional interchangeability or warranty-certified interchangeability; no answer is in the transferred package. A conclusion that E-20 certainly qualifies, or certainly cannot qualify, would require a supplied interpretation or Annex Q text that the current evidence lacks.

Original: [input/originals/D00005.md](input/originals/D00005.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2478, "end_character": 3247, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00005.md", "original_sha256": "50fa064b64c998354572ea7622387d6439535fe4df2d6a361901e138be03a74b", "artifact_directory": "extraction/D00005/attempt-2lc2fbwi"}`.

### Rules

- Different predicates cannot be treated as direct contradiction or substituted for an unspecified governing compatibility criterion.

### Assumptions

- The supplied synthetic records and operative clauses are faithfully transcribed; source authenticity and external procurement law are outside the audit.
- Use exact euro cents after prescribed single rounding and exact UTC minute timestamps. Named source coverage, not general document omission, governs negative event facts.

### Reasoning

- 1. X04 limits the rival report to mechanical fit and electrical bench behavior, excluding durability and warranty acceptance.
- 2. The warranty letter concerns certification only and has not assessed rival warranty eligibility. Thus the two sources address different predicates.
- 3. If Annex Q required sole warranty-certified interchangeability, a bench-functional rival might not defeat exclusivity; if it required physical compatibility, it might. The finite alternative-test model makes that divergence explicit.
- 4. Without Annex Q, neither certain qualification nor certain disqualification follows. The correct report describes failure of disqualification evidence, not actual eligibility.

### Limits

- The conclusion is limited to the named synthetic requirement, operative rule and May-June 2029 coverage; it does not authenticate real-world events.
- No claim is made that either hypothetical reading exhausts possible Annex Q definitions.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **auxiliary**.

### Formal evidence

- `Audit.compatibilityOpen` in module `Audit` (auxiliary): `Audit.onlyCompatible Audit.CompatibilityTest.warranty = true ∧ Audit.onlyCompatible Audit.CompatibilityTest.physical = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target029.lean) · [Actual proof log](logs/target-029.log)

### Recommendation

Obtain Annex Q and a scoped compatibility assessment before deciding eligibility.

## C06-C15

### Exact report claim

`input/report.md#C06-C15`

> **C06-C15.** The P-21 approval evidence conflicts: Mara asserts a 10:00 approval and Tomas explicitly denies that event; neither statement is retracted, and no supplied authoritative record resolves them. Sources: A01, A02, A03, L01.

### Verification question

Do the P21 attestations conflict about one approval event without an authoritative supplied resolution?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0018`

> The standard defines compliance as the conjunction of the applicable competition requirement or a fully established competition exception, and valid pre-commitment order approval. The dossier's explicitly complete transaction register may establish event absence within its named coverage. Other files, including incoming correspondence and partial scans, have no general completeness status. Conflicting signed attestations remain attributable statements until an authorized correction or adjudication resolves them. Signature authentication establishes who signed, not that the statement is necessarily true. The standard supplies no metric for describing a transaction as prudent, fair, strategically wise, or commercially elegant. Those descriptions are separate judgments rather than consequences of a threshold calculation.
> 

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[18]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

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
Coordinates: `{"kind": "ocr", "page": 2, "origin": {"format": "pdf", "page": 2, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0002-raster.png", "tsv_artifact": "pdf-page-0002.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.7743488556701, "minimum_word_confidence": 78.718094, "confidence_threshold": 85.0, "low_confidence_words": 2, "word_count": 97, "original": "input/originals/D00003.pdf", "original_sha256": "f7fd20aa2be7a439af133f37c3f045a9d3ce14b786760ec8c806c2e8abcf07f8", "artifact_directory": "extraction/D00003/attempt-7ddoffon", "source_anchor": "pdf-page-0002", "root_source_anchor": "pdf-page-0002", "reviewer": "audit_02m", "reason": "Visually inspected original PDF page raster; corrected OCR semantic marker, minute digits and register reference where required; entire material passage compared with page.", "reviewed_at": "2026-11-04T15:03:34.990337+00:00", "transcription_snapshot": "input/manual-transcriptions/D00003/f2c73ff169fa72a87f8a86ce29319fba80b81b376e3a4b6229800b78686ff70a.txt", "transcription_file_sha256": "35768ae655a05f73e910cd3e329dc75463071a611525aeed414aaa2f34535a38", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

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
Coordinates: `{"kind": "ocr", "page": 3, "origin": {"format": "pdf", "page": 3, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0003-raster.png", "tsv_artifact": "pdf-page-0003.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 93.84218948623854, "minimum_word_confidence": 0.0, "confidence_threshold": 85.0, "low_confidence_words": 4, "word_count": 109, "original": "input/originals/D00003.pdf", "original_sha256": "f7fd20aa2be7a439af133f37c3f045a9d3ce14b786760ec8c806c2e8abcf07f8", "artifact_directory": "extraction/D00003/attempt-7ddoffon", "source_anchor": "pdf-page-0003", "root_source_anchor": "pdf-page-0003", "reviewer": "audit_02m", "reason": "Visually inspected original PDF page raster; corrected OCR semantic marker, minute digits and register reference where required; entire material passage compared with page.", "reviewed_at": "2026-11-04T15:03:35.134756+00:00", "transcription_snapshot": "input/manual-transcriptions/D00003/74d057c1ffd7a573949b5264432bbf95d0ac166f21a1a683072c9f16d09c7d65.txt", "transcription_file_sha256": "1bb87ea08d1b8f4dafa7bc70dce45a7d9057d73a66cd9d063ab39c18e29ce0d8", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

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
Coordinates: `{"kind": "ocr", "page": 4, "origin": {"format": "pdf", "page": 4, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0004-raster.png", "tsv_artifact": "pdf-page-0004.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.67376844339621, "minimum_word_confidence": 65.073479, "confidence_threshold": 85.0, "low_confidence_words": 2, "word_count": 106, "original": "input/originals/D00003.pdf", "original_sha256": "f7fd20aa2be7a439af133f37c3f045a9d3ce14b786760ec8c806c2e8abcf07f8", "artifact_directory": "extraction/D00003/attempt-7ddoffon", "source_anchor": "pdf-page-0004", "root_source_anchor": "pdf-page-0004", "reviewer": "audit_02m", "reason": "Visually inspected original PDF page raster; corrected OCR semantic marker, minute digits and register reference where required; entire material passage compared with page.", "reviewed_at": "2026-11-04T15:03:35.280489+00:00", "transcription_snapshot": "input/manual-transcriptions/D00003/653097fa4c7e85eb684393bda9dd0a3959fec379a0851eefccc17e303dbea4da.txt", "transcription_file_sha256": "8fb79403566e4e68d553034c72b964919a57a2a9e20b95369b9729a709f0fe95", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L01`

> ## [L01]
> 
> This register is complete for commitment amounts, approval events, competitive-solicitation certificates, emergency declarations, retrospective reviews, and exception determinations for P-11, P-12, P-13, P-14, P-15, P-16, R-17, R-18, and E-19 from May 1 through June 30, 2029. An explicit entry “none” means the named event did not occur in that coverage, rather than that a page was omitted. That completeness does not cover P-21, E-20, payment events, or anyone's subjective assessment. The recorded original requirements for these entries were fully known at the times stated. All amounts described as normalized include unavoidable charges, exclude recoverable VAT, and already reflect the specified single final rounding unless an entry instead supplies the exact unrounded currency inputs.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 168, "end_character": 973, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

### Rules

- P08 preserves attributed testimony until authorized correction/adjudication; authenticated signatures do not make asserted contents necessarily true. L01 excludes P21 completeness.

### Assumptions

- The supplied synthetic records and operative clauses are faithfully transcribed; source authenticity and external procurement law are outside the audit.
- Use exact euro cents after prescribed single rounding and exact UTC minute timestamps. Named source coverage, not general document omission, governs negative event facts.

### Reasoning

- 1. Visually reviewed A01 states Mara saw director written approval June 27 at 10:00 before 10:30 commitment. A02 explicitly says that same10:00 event did not occur and no director approval occurred by 11:00.
- 2. Both concern P21, the same morning and timezone. The model records identical event coordinates with opposite assertion polarity, not unconditional opposite world facts.
- 3. A03 stipulates both signatures authentic, neither retracted, and no priority, adjudication, corrected register or original instrument resolves the dispute.
- 4. OCR token errors were corrected only through hash-bound reviewed transcriptions; Tomas signed at 14:30, which provides no precedence rule. The report accurately describes conflict; actual approval remains unresolved.

### Limits

- The conclusion is limited to the named synthetic requirement, operative rule and May-June 2029 coverage; it does not authenticate real-world events.
- The meta-claim of conflicting evidence is supported. The approval event itself has opposing testimony and is not settled by signature authenticity or the later statement.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.approvalConflict` in module `Audit` (supports): `Audit.mara.order = Audit.tomas.order ∧ Audit.mara.dateOffset = Audit.tomas.dateOffset ∧ Audit.mara.approvalMinute = Audit.tomas.approvalMinute ∧ Audit.mara.asserted ≠ Audit.tomas.asserted ∧ Audit.mara.retracted = false ∧ Audit.tomas.retracted = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target031.lean) · [Actual proof log](logs/target-031.log)

### Recommendation

Retain the qualified finding and its precise source references.

## C06-C16

### Exact report claim

`input/report.md#C06-C16`

> **C06-C16.** The supplied P-21 invoice and delivery acceptance establish neither payment nor nonpayment; the finance reply says settlement cannot be determined without the missing bank reconciliation. Sources: P01, A04, F03.

### Verification question

Do P21 invoice and delivery records leave payment unresolved?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0004`

> Harbor Research Cooperative purchases components for an offshore research laboratory. This standard distinguishes a requisition, an approval, an order commitment, delivery acceptance, an invoice, and payment. A requisition records a proposed need. An approval authorizes a specified transaction within the approving person's authority. An order commitment binds Harbor to purchase. Delivery acceptance confirms receipt or technical acceptance. An invoice requests payment. None of these events automatically establishes that any other event occurred. The assessment period is 1 May through 30 June 2029, and all times in this standard and the transaction records are UTC. No external procurement law forms part of this fictional agreement.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

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
Coordinates: `{"kind": "ocr", "page": 5, "origin": {"format": "pdf", "page": 5, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0005-raster.png", "tsv_artifact": "pdf-page-0005.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 94.91212301063828, "minimum_word_confidence": 28.830444, "confidence_threshold": 85.0, "low_confidence_words": 3, "word_count": 94, "original": "input/originals/D00003.pdf", "original_sha256": "f7fd20aa2be7a439af133f37c3f045a9d3ce14b786760ec8c806c2e8abcf07f8", "artifact_directory": "extraction/D00003/attempt-7ddoffon", "source_anchor": "pdf-page-0005", "root_source_anchor": "pdf-page-0005", "reviewer": "audit_02m", "reason": "Visually inspected original PDF page raster; corrected OCR semantic marker, minute digits and register reference where required; entire material passage compared with page.", "reviewed_at": "2026-11-04T15:03:35.426916+00:00", "transcription_snapshot": "input/manual-transcriptions/D00003/88f7763d0ec10b10cfbc90b82a9857fe4d8abdb2e5ba545eef5bc49b897e29bd.txt", "transcription_file_sha256": "64eda6f7c9f8621cc75471f06ad1f8be5d19439e1ff546f59a773d544ab814b9", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/reconciliation-correspondence.md](input/sources/reconciliation-correspondence.md) — `F03`

> ## [F03]
> 
> The accounts-payable packet contains a signed supplier invoice for P-21 and a warehouse delivery acceptance. The invoice confirms the supplier's request for EUR 8,000.00 payment and names the order. The warehouse acceptance confirms that the specified package arrived. Neither document states that Harbor paid. A finance reply says the bank reconciliation extract for June 27–30 was not transferred, and the analyst cannot confirm or deny payment from the supplied packet. A report that equates the invoice signature with settlement would therefore rely on a missing event premise, rather than on contradictory affirmative evidence that payment did not occur.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1507, "end_character": 2176, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "2b5e3cc9824253cabb8493b6702e9b725dbbb3e61b2d9b5003be58748edcc535", "artifact_directory": "extraction/D00008/attempt-5lhazxlb"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L01`

> ## [L01]
> 
> This register is complete for commitment amounts, approval events, competitive-solicitation certificates, emergency declarations, retrospective reviews, and exception determinations for P-11, P-12, P-13, P-14, P-15, P-16, R-17, R-18, and E-19 from May 1 through June 30, 2029. An explicit entry “none” means the named event did not occur in that coverage, rather than that a page was omitted. That completeness does not cover P-21, E-20, payment events, or anyone's subjective assessment. The recorded original requirements for these entries were fully known at the times stated. All amounts described as normalized include unavoidable charges, exclude recoverable VAT, and already reflect the specified single final rounding unless an entry instead supplies the exact unrounded currency inputs.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 168, "end_character": 973, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

### Rules

- P01 separates invoice, acceptance, commitment and payment; no automatic event implication. L01 excludes payment-event completeness.

### Assumptions

- The supplied synthetic records and operative clauses are faithfully transcribed; source authenticity and external procurement law are outside the audit.
- Use exact euro cents after prescribed single rounding and exact UTC minute timestamps. Named source coverage, not general document omission, governs negative event facts.

### Reasoning

- 1. F03 supplies invoice requesting EUR 8000 and acceptance confirming arrival; neither states payment. A04 supplies no bank/payment entry.
- 2. Finance explicitly cannot confirm or deny settlement without missing June 27-30 bank reconciliation.
- 3. The auxiliary model holds invoice and delivery true while allowing paid=true or paid=false. This is a non-entailment witness, not an actual payment decision.
- 4. Resolving P21 approval disagreement would still not supply the missing settlement event.

### Limits

- The conclusion is limited to the named synthetic requirement, operative rule and May-June 2029 coverage; it does not authenticate real-world events.
- Payment and nonpayment remain undetermined. The model does not claim that either happened; it isolates absent linkage evidence.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **auxiliary**.

### Formal evidence

- `Audit.paymentOpen` in module `Audit` (auxiliary): `∀ paid : Bool, ∃ w : Audit.PaymentWorld, w.invoice = true ∧ w.delivery = true ∧ w.paid = paid`.
  [Model](models/Audit.lean) · [Executed check](checks/Target032.lean) · [Actual proof log](logs/target-032.log)

### Recommendation

Obtain the bank reconciliation and settlement record before deciding payment.

## C06-C17

### Exact report claim

`input/report.md#C06-C17`

> **C06-C17.** The complete register contains objective compliance failures: P-11/P-12 lack required aggregate competition, R-17 lacks required revision 1 competition, and P-16 lacks valid approval. Sources: P02, P03, P05, P08, L01, L02, L04, L05.

### Verification question

Are all three named objective compliance failures established within complete coverage?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0006`

> The applicable competitive-purchase threshold is inclusive: a normalized purchase value equal to the threshold requires competition unless an established exception applies. Revision 1 uses EUR 20,000.00. Revision 2 uses EUR 25,000.00. Below the applicable threshold, this standard does not require competitive solicitation, although a valid order approval is still required. Competition means inviting at least three independent qualified suppliers, giving each the same specification, recording the responses or documented nonresponses, and signing a comparison before order commitment. A supplier's quote, a market-price screenshot, or an existing relationship is not by itself the prescribed competition. A competition certificate expressly marked complete attests that these steps occurred; a quotation folder without that certificate does not automatically attest them.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0008`

> Two or more purchases aggregate when they concern the same funded project, the same supplier legal entity, and components of one operational requirement committed within an inclusive thirty-calendar-date window. The first commitment date is day one, and the last included date is first date plus twenty-nine calendar days. Different order numbers, cost-center labels, delivery pallets, or invoice dates do not split an otherwise common operational requirement. Purchases do not aggregate merely because the suppliers have similar names or serve the same laboratory. A documented change to a genuinely independent operational requirement can rebut aggregation, but relabeling a single installation cannot. For an aggregate, the competitive threshold applies to the combined normalized value before the first commitment if the full requirement was already known then.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[8]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0012`

> A purchase requires a written approval identifying the order, value, and supplier, granted strictly before commitment by a person whose authority covers the value and category at the approval instant. Authority limits are inclusive unless a delegation says otherwise. The procurement director has standing authority for all monetary values in this dossier. A delegated manager has only the category, amount, and time range expressly stated in the delegation. An approval at the delegation's inclusive expiry instant is valid if all other conditions hold; a later commitment does not itself invalidate that approval. An approval granted after expiry is not rescued by the fact that the requisition was submitted earlier. Manager approval and completion of competitive solicitation are separate requirements: satisfying one does not imply the other.

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[12]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0018`

> The standard defines compliance as the conjunction of the applicable competition requirement or a fully established competition exception, and valid pre-commitment order approval. The dossier's explicitly complete transaction register may establish event absence within its named coverage. Other files, including incoming correspondence and partial scans, have no general completeness status. Conflicting signed attestations remain attributable statements until an authorized correction or adjudication resolves them. Signature authentication establishes who signed, not that the statement is necessarily true. The standard supplies no metric for describing a transaction as prudent, fair, strategically wise, or commercially elegant. Those descriptions are separate judgments rather than consequences of a threshold calculation.
> 

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[18]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

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
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-ld2896xv"}`.

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
Coordinates: `{"kind": "pdf", "page": 4, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0004.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00009.pdf", "original_sha256": "c8d035848c7a222831ccf4792210e8700fe89bf4a86e4be34b70de667175a10d", "artifact_directory": "extraction/D00009/attempt-ld2896xv"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L01`

> ## [L01]
> 
> This register is complete for commitment amounts, approval events, competitive-solicitation certificates, emergency declarations, retrospective reviews, and exception determinations for P-11, P-12, P-13, P-14, P-15, P-16, R-17, R-18, and E-19 from May 1 through June 30, 2029. An explicit entry “none” means the named event did not occur in that coverage, rather than that a page was omitted. That completeness does not cover P-21, E-20, payment events, or anyone's subjective assessment. The recorded original requirements for these entries were fully known at the times stated. All amounts described as normalized include unavoidable charges, exclude recoverable VAT, and already reflect the specified single final rounding unless an entry instead supplies the exact unrounded currency inputs.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 168, "end_character": 973, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L02`

> ## [L02]
> 
> P-11 and P-12 buy the two halves of one sensor-rack installation for project TIDE-4 from the same legal supplier, Pelican Instruments Ltd. The combined requirement and both prices were approved as a technical specification on May 28. Accepted requisition R-11 was received June 1 at 09:00 UTC. P-11 was committed June 3 for normalized EUR 12,400.00; P-12 was committed June 20 for normalized EUR 12,600.00. The two orders have different cost-center suffixes and delivery pallets, but neither changes the shared functional requirement. Director order approvals were granted June 2 and June 19 respectively. Competitive-solicitation certificate: none. Emergency declaration: none. Other competition exception determination: none.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 992, "end_character": 1729, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L04`

> ## [L04]
> 
> P-15 is laboratory consumables with normalized value EUR 14,900.00, accepted June 9. Manager Dana Cole granted the written order approval at exactly 2029-06-15 17:00 UTC. Commitment was at 17:01 UTC on the same day. P-16 is separate laboratory consumables with normalized value EUR 15,000.00, accepted June 9. Dana granted its written order approval at 2029-06-15 17:01 UTC, and commitment followed at 17:10 UTC. No director or alternative delegate approved P-16 at any time in this register's coverage, and no later document purports to ratify it retroactively. Neither purchase aggregates with another requirement; each is below the revision 2 competition threshold.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2513, "end_character": 3191, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

- [input/sources/purchase-register.md](input/sources/purchase-register.md) — `L05`

> ## [L05]
> 
> R-17 and R-18 have the receipts and unchanged scopes recorded in V03 and V04. Each was committed June 10 after a valid director order approval on June 9. Competitive-solicitation certificate for R-17: none. Exception determination for R-17: none. Competitive-solicitation certificate for R-18: none. Exception determination for R-18: none. E-19 is a separate safety-pump requirement received June 21 for normalized EUR 31,000.00 and committed at 2029-06-22 10:00 UTC. A director's instrument granted order approval and made the emergency declaration at 09:45 that morning. The complete emergency details appear in X01 and X02; no competition certificate exists for E-19.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 3210, "end_character": 3890, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "0a73cfa5b770b081a5335b326920130f9edfd4c6c843797412e27b3172c29108", "artifact_directory": "extraction/D00007/attempt-lrogyf9g"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D01`

> ## [D01]
> 
> The procurement director delegates authority to manager Dana Cole for laboratory consumables with normalized purchase value no greater than EUR 15,000.00 per independent requirement. The authority begins at 2029-06-01 00:00 UTC and expires at 2029-06-15 17:00 UTC, inclusive. The amount limit is inclusive. The delegation does not cover instrument acquisitions, emergency declarations, competition waivers, or approval of an aggregate whose combined requirement exceeds the limit. Dana may approve qualifying purchases during this interval even if operational commitment follows after expiry, provided approval still strictly precedes commitment and no approval condition is violated. The authority is measured when the approval is granted, not when a request enters Dana's inbox.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 149, "end_character": 939, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-pws495wo"}`.

- [input/sources/delegation-notice.md](input/sources/delegation-notice.md) — `D02`

> ## [D02]
> 
> The authority register is complete for Dana's delegation and amendments during June 2029. It contains no extension, renewal, oral-authority confirmation, substitute delegation, or suspension. The stated expiry therefore remains controlling. This authority completeness is deliberately narrow: it does not purport to list every procurement approval by every employee. P-15 and P-16 approval events are established by their transaction register entries, while the director's standing authority comes from P05. The laboratory team may continue using Dana as a contact person after expiry, but a person's presence in a directory or continued employment does not renew a formal monetary delegation.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 958, "end_character": 1661, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "70e6f8d94fc43cfe9cf239a68869f50e63c1df59786623aeb9dcc744c5c9d447", "artifact_directory": "extraction/D00004/attempt-pws495wo"}`.

### Rules

- P08 compliance requires applicable competition/exception and valid precommitment approval. L01 permits explicit-none event absence only for named covered entries.

### Assumptions

- The supplied synthetic records and operative clauses are faithfully transcribed; source authenticity and external procurement law are outside the audit.
- Use exact euro cents after prescribed single rounding and exact UTC minute timestamps. Named source coverage, not general document omission, governs negative event facts.

### Reasoning

- 1. P11/P12 known aggregate equals revision 2 threshold and lacks recorded competition/exception; director approval cannot cure it.
- 2. R17 retained revision 1 value exceeds threshold and lacks competition/exception despite director approval.
- 3. P16 is below competition threshold but Dana approved after expiry and complete coverage excludes alternatives.
- 4. Each witness satisfies the domain and fails a specified compliance limb. The checked conjunction proves all three finite failures without generalizing to E20, P21 or payments.

### Limits

- The conclusion is limited to the named synthetic requirement, operative rule and May-June 2029 coverage; it does not authenticate real-world events.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.objectiveFailures` in module `Audit` (supports): `Audit.compliant (Audit.competitionSatisfied 2 Audit.rackTotal false false) true = false ∧ Audit.compliant (Audit.competitionSatisfied 1 2250000 false false) true = false ∧ Audit.compliant (Audit.competitionSatisfied 2 1500000 false false) false = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target033.lean) · [Actual proof log](logs/target-033.log)

### Recommendation

Retain the qualified finding and its precise source references.

## C06-C18

### Exact report claim

`input/report.md#C06-C18`

> **C06-C18.** The management description of E-19 as prudent and commercially elegant is an attributed opinion; the supplied standard provides no metric for formally establishing those adjectives. Sources: P08, F05.

### Verification question

Does the report accurately identify the management description as opinion without a supplied formal metric?

### Source evidence

- [input/sources/procurement-standard.docx.md](input/sources/procurement-standard.docx.md) — `docx-p-0018`

> The standard defines compliance as the conjunction of the applicable competition requirement or a fully established competition exception, and valid pre-commitment order approval. The dossier's explicitly complete transaction register may establish event absence within its named coverage. Other files, including incoming correspondence and partial scans, have no general completeness status. Conflicting signed attestations remain attributable statements until an authorized correction or adjudication resolves them. Signature authentication establishes who signed, not that the statement is necessarily true. The standard supplies no metric for describing a transaction as prudent, fair, strategically wise, or commercially elegant. Those descriptions are separate judgments rather than consequences of a threshold calculation.
> 

Original: [input/originals/D00006.docx](input/originals/D00006.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[18]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00006.docx", "original_sha256": "ed054f952c7f1ca8d513691fa0c4460a7c7de9e6c59320c1b21fb22abfbcacfa", "artifact_directory": "extraction/D00006/attempt-jcq39qna"}`.

- [input/sources/reconciliation-correspondence.md](input/sources/reconciliation-correspondence.md) — `F05`

> ## [F05]
> 
> An internal retrospective comment describes the emergency pump purchase as “prudent and commercially elegant.” The comment provides no decision model, risk utility scale, price benchmark, or evaluative definition. It is an attributed management opinion and does not alter the objective timing of EM-19 or the retrospective review. The same meeting asks the audit team to distinguish correct mathematical calculations, valid authority, established exceptions, missing documents, and disputed testimony. That discussion records stakeholder interests; it does not add a new operative rule, resolve the P-21 contradiction, or supply Annex Q. The fictional standard and its explicit transition clauses remain the controlling rules for the finite dossier.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 2875, "end_character": 3634, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "2b5e3cc9824253cabb8493b6702e9b725dbbb3e61b2d9b5003be58748edcc535", "artifact_directory": "extraction/D00008/attempt-5lhazxlb"}`.

### Rules

- P08 expressly supplies no metric for prudent or commercially elegant; formal compliance calculations do not entail those judgments.

### Assumptions

- The supplied synthetic records and operative clauses are faithfully transcribed; source authenticity and external procurement law are outside the audit.
- Use exact euro cents after prescribed single rounding and exact UTC minute timestamps. Named source coverage, not general document omission, governs negative event facts.

### Reasoning

- 1. F05 attributes the words to an internal management retrospective, with no decision model, utility scale, benchmark or definition.
- 2. P08 explicitly separates such judgments from objective compliance.
- 3. The report accurately characterizes that source and limitation. Its qualified meta-claim is supported; the underlying aesthetic/prudential merits are nonformal and receive no Lean target.

### Limits

- The conclusion is limited to the named synthetic requirement, operative rule and May-June 2029 coverage; it does not authenticate real-world events.
- No truth value is assigned to the underlying prudence or commercial-elegance opinion.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Retain attribution; define an evaluative framework and relevant evidence if management wants those adjectives assessed.
