# Independent native/corpus implementation review

Date: 4 November 2026. Scope: implementation correctness, not semantic dossier audits or evaluator comparison.

## Inspected scope

Read the current audit.py, corpus.py, extractors.py, and corrections.py implementations and their relevant unit/integration tests. Examined input and extraction fingerprint validation, result freshness, indexed evidence lookup, review acknowledgements, interrupted ingestion recovery, bounded batches, refreshed-document invalidation, manual-transcription overlays, native extraction uncertainty, and optional checker failure reporting. The final inspected file fingerprints are retained in reviewed-file-hashes.json.

No evaluator outcomes or dossier semantic-review artifacts were read for this task. No active dossier workspace was changed. All reproductions and executed test output are retained beneath tmp/extension-code-review/. The reviewer initially made no code edits and reported both reproduced defects to the coordinator. The coordinator subsequently authorized this reviewer to make the narrow corpus retry fix and its regression tests; the coordinator separately implemented the DOCX revision fix. Accordingly, testing of the corpus repair is author verification, while the DOCX repair was independently rechecked by this reviewer.

## Defect 1: retry removed manual-transcription overlays — repaired

Original reproduction: run repro_manual_retry.py. It prepares a real two-page PDF with max_pages=1, records a caller-attributed manual transcription of page one, then resumes with retry=True and max_pages=2.

Observed before repair: ingestion became complete and corpus.verify passed, but the reviewed anchor disappeared from the segment index, derived Markdown, and search results. Its authored snapshot survived as an unindexed artifact. This silently broke previously recorded reviewed evidence and forced repeated manual work. It did not itself reuse an old successful proof: changed fingerprints would reject that proof.

Evidence: manual-retry-k4k7wqmw/result.json and its retained audit workspace. Root cause was unconditional replacement of the document's complete segment/chunk set and derived text in corpus.resume.

Repair: same-original-hash retries now append and reindex existing manual-transcription segments after the new machine extraction, preserving their distinct anchors, quotes, original coordinates, original artifact directory, uncertainty, authored snapshots, and hash-bound review records. New raw extraction artifacts are not rewritten to impersonate manual source review. Anchor collisions fail explicitly. Refreshed documents whose original hash changed do not inherit the old transcription; invalidation.json lists invalidated manual anchors, document warnings disclose their exclusion, and snapshots plus the parent workspace remain retained.

Post-repair reproduction: manual-retry-al_u963n/result.json shows the reviewed passage and derived anchor retained, one search match, and complete ingestion. Added tests also cover chained manual transcriptions, collision rejection without passage overwrite, stale proof-result rejection, and changed-original refresh exclusion.

## Defect 2: DOCX tracked row deletion bypassed uncertainty review — repaired by coordinator

Original reproduction: run repro_docx_row_revision.py. Its DOCX table contains a row-level w:trPr/w:del marker and a cell stating “Approval was denied.” The original extractor inspected paragraph descendants for revisions but did not propagate row-property revisions to cell paragraphs.

Observed before repair: the document was ready, the cell had an empty uncertainty list, and assert_reviewable accepted a direct formal finding without original-source review. This could treat deleted or inserted row text as unqualified current documentary evidence.

Evidence: docx-row-revision-8uc7utgz/result.json. The coordinator repaired revision detection/propagation in table, row, and cell properties, with regression coverage.

Independent post-repair reproduction: docx-row-revision-k71s6smx/result.json now reports partial ingestion and explicit tracked-table-row uncertainty. After supplying a coverage acknowledgement solely to isolate the second gate, assert_reviewable still rejected the direct formal finding for missing original-source review. That separate gate result is in docx-row-revision-k71s6smx/post-acknowledgement-gate.json. No accepted revision was automatically invented.

## Executed checks

- selected-tests.log: 15 selected existing behavioral tests passed, zero failures/errors/skips. They covered bounded resume, changed extraction rejection, missing integrity lock, incomplete coverage accounting, hash-bound source/report review, dependency invalidation, tracked paragraph/object extraction, OCR low confidence, PDF page limits, manual proof archival, corrected-report parent linkage, failed optional checker rejection, and actual Lean check/render/export/stale-result handling.
- fix-tests.log: 7 focused corpus tests passed, zero failures/errors/skips. Three were added for this repair: retained overlays and stale results, collision rejection, and changed-original refresh. Existing PDF retry, no-op resume, refresh with executed proofs, and interrupted-state recovery tests also passed.
- Both original defect reproductions were rerun after repair; their before/after directories remain separate.
- Actual Poppler extraction and Lean execution were used where the selected tests exercise them. The selected actual Lean tests used the available 4.24.0 toolchain. The deliberately rejecting checker is a negative-control executable, not a successful independent proof checker.

The small test runners are retained as run_selected_tests.py and run_fix_tests.py; their machine-readable summaries are selected-tests-result.json and fix-tests-result.json. These 22 selected test executions are not a claim that the complete repository suite was rerun by this reviewer.

## Gate assessment and limits

The reviewed current implementation rejects altered original/input/index bytes and altered raw extraction artifacts against their stored manifests. Exact quotation checks distinguish indexed passages from arbitrary text. The execution fingerprint includes source manifest, models, findings, extraction lock, review/coverage/revision records, and manual-transcription journal. Thus changing those records after a successful check requires a new check. Source refresh archives prior technical outputs and requires current-manifest revision review; absent or incomplete dependency maps conservatively invalidate all findings.

Incomplete extraction remains separate from correctness. Explicit coverage acknowledgements document omitted/partial material; they do not make it extracted. Material uncertain source and report passages used for direct formal findings require a hash-bound source-review record. Auxiliary and documentary findings are not automatically promoted to direct formal truth. These gates record a reviewer's attestation; they cannot prove that visual inspection occurred or that the interpretation is sound.

Optional replay failure produces failed status and blocks delivery; its method is described as replay through the same Lean kernel, not independent-kernel verification. No successful external checker was run in this review, and no hostile-code sandbox claim was assessed.

Bounded batches stop between documents, while extraction subprocesses have their own timeouts and PDF page limits. This is not a strict whole-document wall-clock or memory budget. Recovery is explicit and retains interrupted derived state; it is not a transaction spanning all filesystem and SQLite writes. General extraction completeness, arbitrary DOCX rendering semantics, OCR correctness, source authenticity, semantic adequacy of dependency declarations, and general benchmark reliability remain outside these tests.

Both reproduced defects are resolved in the reviewed code. No additional material defect was established within this focused review; this is not an exhaustive correctness guarantee.
