# Built-in extraction adapters and flexible alternatives

`extractors.extract_document(path, artifact_dir, *, ocr_language="eng", timeout=60, max_pages=None)` returns:

- `text`: separately generated, anchored Markdown; originals are preserved by the caller.
- `segments`: `anchor`, `quote`, `locator`, `method`, and `uncertainty` for each passage or explicitly empty extraction gap.
- `tools`: actual converter versions, Python version, and explicitly unavailable dependencies.
- `warnings`, `complete`, and `status` (`ready`, `partial`, or `blocked`).

Use a fresh artifact directory within a distinct retained repository `tmp/` run. The extractor does not delete artifacts. `complete` concerns recoverable extraction coverage; it does not authenticate the source or establish semantic correctness. `ready` does not certify OCR. Partial results retain the readable portions and name coverage gaps. Blocked results contain no readable passage. Each call writes `extraction.json`; converter commands, exit codes, errors, and timeouts are preserved as JSON logs.

## UTF-8 Markdown and text

Markdown/text/CSV inputs must decode as UTF-8, optionally with a UTF-8 BOM. Existing HTML anchors are retained. An unanchored preamble is retained under a collision-safe generated anchor. Unanchored passages use deterministic `P01`, `P02`, and subsequent IDs. Locators preserve original line numbers and offsets in Unicode code points after BOM removal, including original internal newline sequences. The extractor does not guess other encodings or execute document instructions. CSV is treated as literal text; no table schema or numeric interpretation is inferred.

## PDF

Requires Poppler `pdfinfo` and `pdftotext`; `pdfimages` detects raster-bearing pages. `pdftotext -bbox-layout` runs separately for each page. Page anchors are `pdf-page-0001`, etc. Native locators preserve page number, page dimensions, and every word's bounding box in PDF points with top-left origin. Raw XHTML and structured coordinates are retained. The quote reconstructs Poppler words in line order using one space between words and newlines between lines; it is not a byte-for-byte copy of the PDF's internal encoding or a guarantee of visual reading order.

Empty native text pages are rasterized with `pdftoppm` at 200 DPI and processed by Tesseract. Pages containing both native text and raster images retain native text and a separate `pdf-page-0001-ocr` supplement. The supplement may duplicate native text; auditors must not count it as independent evidence. If raster-image detection is unavailable, the adapter attempts OCR for every page to avoid silently omitting scanned content beneath a native header. Missing OCR coverage is reported as partial when native text remains usable, or blocked when nothing readable is recovered.

`max_pages` limits processed PDF pages and explicitly marks omitted pages and a partial result. Converter failure, encryption restrictions, timeouts, empty output, and missing tools remain explicit. Text extraction does not understand diagrams, reconstruct table semantics, or establish completeness of visual non-text content. Inspect the original whenever layout, graphics, tables, or reading order matter.

## PNG, JPEG, and scanned pages

Requires `tesseract` and the requested language model; PDF rasterization additionally requires `pdftoppm`. Tesseract TSV output is enabled through explicit configuration variables, without depending on a separately installed TSV configuration file. Raw TSV and original/raster images are retained.

Each OCR locator preserves page, language, segmentation mode, word boxes in pixels, word confidence, mean and minimum confidence for the page, and the count of words below the threshold of 85. Any low-confidence word produces a partial result and an explicit uncertainty notice. Empty OCR output is an unresolved gap: the adapter does not guess whether the image is blank or unreadable. Rasterized PDF coordinates can be mapped back using `pixel * 72 / 200`.

Every material OCR quotation requires visual comparison with the original, even if its confidence is high. Exact quote matching against OCR text proves only correspondence with the extracted transcription. Confidence values are tool scores, not calibrated probabilities that a proposition or transcription is correct.

## DOCX

The standard-library ZIP/XML adapter reads the main document in XML paragraph/table order, then header and footer members, footnotes, endnotes, and comments. Locators identify the original XML member, explicit XML path, paragraph index, and table/row/cell coordinates, with merged-cell information where present. Raw relevant XML members are retained. Header/footer and note ordering is story ordering, not rendered page placement; DOCX page coordinates and repeated header visibility are not inferred. `max_pages` does not limit DOCX XML stories and this is explicitly reported.

Tracked insertions and deletions, including table-row/cell revision properties, are retained in XML order and marked partial; the adapter never silently chooses an accepted revision. Comments retain attribution and are distinguished from main document assertions. Stored field results are extracted without evaluating field instructions. Hidden text, content controls, merged cells, and nested tables carry explicit interpretation notices.

Embedded objects, drawings, equations, text boxes, unsupported block/cell structures, and macros are not silently treated as complete prose. They produce gaps or uncertainties requiring original inspection. No embedded code or macro is executed. DTD/entity definitions are rejected; ZIP members are read directly rather than unpacked to user-controlled paths. Resource bounds are 100 MiB total declared uncompressed ZIP size and 20 MiB per parsed XML member; exceeding them is explicit, not silent truncation.

## Validation

`tests/test_extractors.py` creates independent synthetic UTF-8, DOCX, PDF, and raster inputs under retained `tmp/extractor-tests-*` directories. It exercises actual available Poppler and Tesseract tools, plus clearly identified unit-test failure simulations. Each run writes a capabilities inventory and reports any missing-tool skips explicitly. Successful tests of clean examples do not remove the need to inspect new documents and OCR uncertainty.

## Other formats and agent tools

The formats above describe optional bundled adapters, not the scope of the method. The agent may use its available document tools for another encoding, spreadsheet, HTML, transcript or other inspectable source. Preserve the original, actual coordinates, uncertainty and coverage, then use [agent extraction import](agent-extraction.md) or [agent-native execution](agent-native-workflow.md). An unavailable adapter is not evidence that the document is empty or that a claim is false.
