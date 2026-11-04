# Native, large and changing corpora

## Prepare and resume

```bash
python3 /path/to/skill/scripts/audit.py prepare --indexed \
  --brief brief.md --report report.docx --sources sources/ \
  --temp-root tmp --max-documents 20 --max-seconds 120
python3 /path/to/skill/scripts/audit.py resume --workspace WORKSPACE --max-documents 20
python3 /path/to/skill/scripts/audit.py inventory --workspace WORKSPACE
```

Preparation snapshots the complete file inventory before bounded extraction. `input/originals/` holds original bytes. `input/sources/`, `input/brief.md` and `input/report.md` hold derived anchored text. `input/index.sqlite3` stores documents, original-coordinate segments, overlapping retrieval chunks and a full-text index. `source-ledger.jsonl` is streamed from that index. Reports and briefs may themselves be native formats.

`ingestion.json` records every ready, pending, partial or blocked document, tools, warnings and actual batch progress. `--max-pages` limits PDF extraction explicitly; `resume --retry --max-pages N` retries incomplete documents with a larger limit. Batches commit document progress to disk. A normal budget stop is resumed without reparsing completed documents. `--max-seconds` is checked between documents, while converter commands have their own `--extract-timeout`; it is not a hard total wall-clock deadline.

A killed process may leave derived files out of sync with the prior manifest. Ordinary verification must reject this state. Explicit `resume --recover` first verifies the original bytes and catalogue against the prior manifest, archives interrupted derived state, and rebuilds from originals. It invalidates prior proof results and requires review again. Modified originals or a modified protected catalogue cannot be repaired by blessing new hashes.

## Retrieve with provenance

```bash
python3 /path/to/skill/scripts/audit.py search --workspace WORKSPACE --query 'exception OR supersedes' --limit 20 --offset 0
python3 /path/to/skill/scripts/audit.py show --workspace WORKSPACE --path input/sources/policy.pdf.md --anchor pdf-page-0003
```

Search uses SQLite FTS5, supports pagination, and records queries in `search-history.jsonl`. Results retain their parent passage and character offsets. Read full passages and the inventory to find cross-file exceptions, superseding versions and opposing evidence. Ranked retrieval is never proof of completeness. Unsupported FTS expressions fail explicitly.

## Review extraction and incomplete coverage

For every uncertain passage used in a direct formal finding, inspect the original (PDF page/image or DOCX XML structure) and record:

```json
{"reviews":[{"path":"input/sources/ticket.pdf.md","anchor":"pdf-page-0001","reviewer":"reviewing agent","decision":"accepted","reason":"Material quotation and numeric units compared with the original raster.","source_sha256":"SHA256_OF_ORIGINAL","segment_sha256":"SHA256_OF_FULL_EXTRACTED_SEGMENT_UTF8"}]}
```

Store this as `extraction-review.json`. Use the original hash and full segment text returned by `show`; do not hash only the excerpt. Both source and report extraction are checked. An acceptance is a documented reviewer action, not an automated OCR-quality certificate. If a number or negation remains ambiguous, do not accept it; keep the corresponding finding unresolved or nonformal. Never change the original snapshot to make a quotation match.

Incomplete ingestion must be resumed or explicitly acknowledged in `coverage-acknowledgement.json` with `documents` entries containing `document_id`, `reason` and `impact`. Explain which claims are limited and what remains unreviewed; do not use an acknowledgement as permission to assume missing data. Ready extraction does not imply every passage has received semantic review.

## Change a source without destroying history

```bash
python3 /path/to/skill/scripts/audit.py refresh --workspace WORKSPACE \
  --document-id D00005 --replacement revised-policy.pdf --temp-root tmp
```

`refresh` creates a new retained revision; the parent stays intact. Format changes require a new document rather than replacing a different format. All technical proof results are invalidated. By default every semantic finding is marked affected. An optional `dependencies.json` can declare `coverage: "complete"`, a `claims` map from every finding ID to document IDs, and `global_documents`. The map must include explicit evidence dependencies; otherwise conservative invalidation applies. Completeness remains an audited semantic assumption, especially for universal findings and missing-evidence claims.

Review changed source meaning, alternative interpretations, all affected claims and model parameters. Update findings/model files. Then write `revision-review.json` with `revision_manifest_sha256` for the new manifest and `reviewed_claims` covering every affected finding. A hash acknowledgement alone does not substitute for this review. Run actual Lean checks again before rendering or exporting.

## Correct a visibly misread passage

Inspect the original first. Store your corrected full passage in a UTF-8 file outside the protected input directory, then run:

```bash
python3 /path/to/skill/scripts/audit.py transcribe --workspace WORKSPACE \
  --path input/sources/scan.pdf.md --anchor pdf-page-0002 \
  --text-file reviewed-page.txt --reviewer "Named reviewer" \
  --reason "Compared the original page; corrected the visibly misread timestamp."
```

The command is an explicit attestation of visual inspection. It adds a distinct reviewed anchor, a retained transcription snapshot, and an attributed acceptance record. The original bytes and original OCR passage remain intact and searchable. They are alternative transcriptions of one source, not independent witnesses; a corrected OCR difference must not be reported as contradictory documentary testimony. Old word coordinates and confidence describe the original OCR, not the corrected wording. Cite the returned anchor, retain uncertainty about source authenticity, and recheck all affected findings. This does not change partial extraction to complete, and it archives previous technical results rather than pretending they remain current. Finish pending ingestion before transcribing. A retry on unchanged original bytes retains reviewed segments, their original coordinates and review bindings alongside the new raw extraction. An anchor collision is rejected explicitly. A source revision invalidates earlier transcriptions for that changed source; it records those anchors and keeps the parent and authored snapshots for inspection.

## Additional proof replay

```bash
python3 /path/to/skill/scripts/audit.py check --workspace WORKSPACE \
  --lean /absolute/path/to/lean \
  --checker /absolute/path/to/compatible/lean4checker --checker-timeout 300
```

The optional checker runs through Lake with `--fresh` on every audited model module. It replays the imported environment using Lean's kernel, including imported declarations. This is additional checking, not an independently implemented proof kernel. A requested replay that fails or times out fails that technical run; its real output is retained. Compatible executable provenance and hashes belong with the result. See the [official checker](https://github.com/leanprover/lean4checker); use a version compatible with the pinned Lean release rather than assuming its current head supports an older toolchain.
