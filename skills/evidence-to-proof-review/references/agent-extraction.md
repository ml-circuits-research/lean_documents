# Agent-produced extraction import

The audit can receive any snapshotted document format. Built-in adapters are optional ways to obtain text; their absence does not mean the original document contains no relevant evidence. A blocked native extraction stays visible in the document inventory and retained attempt logs. An auditor can use available document readers, visual inspection, external converters, or other agent tools to produce a declared extraction. The tool must actually read the supplied original. Never fabricate citations, page numbers, or content to make an unsupported format appear supported.

For optional indexed automation, run:

```sh
python3 /path/to/skill/scripts/audit.py inventory --workspace WORKSPACE
python3 /path/to/skill/scripts/audit.py import-extraction --workspace WORKSPACE --document-id DOCUMENT_ID --bundle extraction.json
```

The Python API is `agent_extraction.import_extraction(workspace, document_id, bundle_path)` after preparing a workspace. The document must already exist in `input/catalog.json`; the role may be source, report, or brief. This helper uses Python's standard library and SQLite/FTS5. It does not require Poppler, Tesseract, or a converter for the original extension. It imports data only and never executes tool descriptions, commands, document instructions, or paths supplied in a bundle.

A purely agent-driven audit does not require these Python helpers. Retain the originals, actual extraction/tool outputs, hashes, coordinates, uncertainty, coverage, claim registration, source-to-proof correspondence, and actual Lean invocation/results in an auditable run folder. Do not claim the indexed helper's schema or integrity checks ran if they did not. Distinguish this independently maintained evidence record from helper-verified export bundles.

## Bundle contract

Save one UTF-8 JSON object. The schema intentionally has no output paths, executable commands, or artifact-copy directives. Original tool outputs can be retained separately in the run directory; the controlled importer archives the exact submitted bundle and its derived text itself.

```json
{
  "schema_version": 1,
  "original_sha256": "REPLACE_WITH_THE_CATALOG_ORIGINAL_SHA256",
  "method": {
    "name": "visual-transcription",
    "description": "Read the first paragraph in the supplied document using the stated viewer."
  },
  "tool": {"name": "ACTUAL_READER_NAME", "version": "ACTUAL_VERSION_OR_EXPLICIT_UNKNOWN"},
  "reviewer": "Extraction author or agent identity; this is not source-review acceptance",
  "coverage": {
    "status": "partial",
    "scope": "First paragraph only; remaining sections were not inspected.",
    "limitations": ["No claim of full document coverage or source authenticity."]
  },
  "segments": [
    {
      "anchor": "S-introduction-1",
      "quote": "REPLACE_WITH_EXACT_TRANSCRIBED_SOURCE_TEXT",
      "locator": {"kind": "section", "section": "Introduction, first paragraph"},
      "uncertainty": ["State any unreadable words, ambiguous structure, or visual uncertainty."]
    }
  ]
}
```

All displayed fields are required; unknown fields are rejected. `segments` and `coverage.limitations` must be nonempty. `uncertainty` may be empty but the importer always adds an explicit original-source review requirement. Quotes preserve their exact Unicode text, including whitespace; empty quotes and embedded HTML anchor definitions are rejected. Anchors must be unique, start with an ASCII letter, and contain only ASCII letters, digits, underscores, periods, colons, or hyphens, up to 200 characters.

`coverage.status` accepts `complete` or `partial`. Complete means only that the author declares the extraction scope to cover the document; it establishes neither semantic completeness nor transcription accuracy. Wholly unavailable documents remain blocked rather than receiving invented empty quotations. Partial imports require explicit coverage acknowledgement before audit export, just like other partial extractions.

Use coordinates that exist in the original source. Do not substitute synthetic positions in the generated Markdown. Supported locator shapes are:

| `kind` | Required coordinate fields |
| --- | --- |
| `line` | Positive integer `start_line`, `end_line`, inclusive and ordered |
| `page` | Positive integer `page` |
| `section` | Nonempty `section` description |
| `cell` | Nonempty `sheet` and `cell` identifiers |
| `sheet` | Nonempty `sheet` identifier |
| `timestamp` | Nonempty `timestamp` identifying the original media position |
| `byte` | Integer `start_byte` and `end_byte`, zero-based half-open nonempty interval |
| `other` | Nonempty `coordinate_system` and `coordinate` descriptions |

Each locator may additionally contain a nonempty `description`. The importer validates shape and numeric ranges, not whether a declared coordinate actually exists or faithfully locates a passage. That remains part of material source review. It adds the immutable original path/hash, extraction bundle hash, author attribution, and retained artifact directory.

## Material review and formal results

Import attribution does not count as acceptance. Even a complete extraction remains uncertain until the existing `extraction-review.json` mechanism records inspection of the original source. An acceptance record binds a path/anchor, `decision: "accepted"`, named `reviewer`, substantive `reason`, `source_sha256`, and `segment_sha256` (SHA-256 of the exact UTF-8 quotation). Describe what material visual or manual comparison actually occurred. The helper cannot establish that the caller performed it.

Direct proved/refuted findings require this review for uncertain source evidence, the report claim, quoted report premises/citations/inferences, and inspected support-search passages. Source evidence used with a proof and report argument items with `proof_refs` also require review. A purely logical auxiliary proof does not certify OCR accuracy or original-document fidelity. Record conditional assumptions and limits in the finding even after a successful Lean run.

## Retention, retries, and changes

Every effective import retains original bytes, previous extraction attempts, the exact new bundle, and prior derived text. It replaces the selected document's effective segments, rebuilds its chunks/FTS entries, synchronizes source/report ledgers, updates manifest and extraction integrity lock, and records extraction coverage. Imported report anchors enter v2 registration as pending when new or textually changed; existing claims remain for explicit reconciliation.

Native `resume` and `retry` preserve an imported projection, including partial imports. Reimporting a canonically identical bundle is a no-op. A source revision with different original bytes invalidates the old binding and does not retain the imported projection as current evidence. Explicit interrupted-workspace recovery rebuilds from originals and archives old extraction state; it does not silently reaccept earlier agent transcriptions.

An effective import archives prior proof results, logs, checks, semantic review, extraction acceptances, revision review, coverage acknowledgement, and export manifest. All existing findings require review again; they remain editable, with snapshots retained in history. Recreate coverage acknowledgement if necessary, review the material source, reconcile claims/findings, and record `revision-review.json` with the current manifest hash and all `invalidation.json` affected claim IDs. Then rerun actual proof checks and semantic review. Historical successful logs are evidence of earlier runs only.

The importer journals operations but does not claim transactionally atomic filesystem/SQLite updates across a process interruption. Integrity verification detects inconsistent state; use explicit recovery and inspect the retained journal rather than editing manifests to bless an interrupted import.
