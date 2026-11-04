# Independent post-implementation review

Reviewed 4 November 2026. Scope: `agent_extraction.py`, related `corpus.py` changes, and flexible Lean versions, nested local imports, and string lexing in `audit.py`. This review did not read evaluator outcomes or modify production. It is not a new complete audit or proof compilation. References describe the implementation inspected during concurrent development.

## Findings

### P2: Refreshing identical original bytes leaves agent-extracted documents permanently pending

`corpus.refresh` updates the selected document to `pending` even when the replacement has the same original hash (`corpus.py:373–374`). `resume` then skips the document because `tools.agent_extraction.original_sha256` still matches (`corpus.py:147–151`). The skip does not restore the imported coverage status. A repeated import cannot repair this: `agent_extraction.py:110–113` treats the matching canonical bundle hash as an unconditional no-op.

**Executed reproduction:** prepare an HTML source, import a complete agent extraction, and refresh that source using the very same file. The original run is ready, but the revised run is pending. `resume(retry=True)` leaves it pending, and importing the identical bundle returns `changed: false` while leaving it pending. See `post-review-hmwxy43w/results.json`; all inputs, bundle and revised workspaces are retained under that directory.

**Effect:** Coverage incorrectly reports an unprocessed document, and formal delivery requires an unnecessary incomplete-coverage acknowledgement. A caller cannot restore the accurately complete state through ordinary retry or unchanged reimport. This is an availability/coverage correctness bug, not an unsound proof success.

**Minimal fix:** Make same-original refresh an explicit no-op, or preserve/restore ready versus partial from the hash-matching agent extraction coverage. If the helper intentionally creates a new revision even for identical bytes, its effective extraction must retain the prior status. Add complete and partial imported-document regression tests for identical refresh followed by retry and repeated import.

### P3: Nested Lean proof links are still broken in the report argument renderer

`contracts.py:355` emits `models/{p['module']}.lean`. For a valid module `domain.Totals`, the file is now `models/domain/Totals.lean`, but argument-item and independent-reasoning proof links target `models/domain.Totals.lean`. `audit.py` correctly maps the same module in the later proof section, so the final report contains inconsistent links.

**Minimal fix:** Use the same validated dotted-module-to-path conversion in both renderers. Assert that every rendered local proof URL for a nested module resolves to an exported file, including report argument links. This is a rendering defect, not a failure of the Lean target check.

## Reviewed controls that remain effective by code inspection

- Import begins with corpus integrity verification, matches the selected original snapshot hash, and requires that hash in the bundle. Locators cannot overwrite reserved original/hash/artifact metadata. The module does not execute tool names or command text supplied in metadata.
- Imported source, report and brief documents retain their existing roles. The independent-source contract still rejects report/brief paths and byte-identical copies of the selected report as independent evidence (`contracts.py:121–136`). Import does not create a new source role.
- Every imported segment receives uncertainty, even when the caller supplies an empty uncertainty list. Direct formal verdicts require accepted original-source/segment hash bindings. Source-linked auxiliary evidence and quoted report argument items are also reviewed by the expanded gate.
- Complete imported coverage is explicitly attributed to the bundle; it does not itself establish transcription fidelity. Changed imported evidence archives prior results, extraction reviews and semantic review, and requires review of all existing findings. Changed original hashes disable imported projections during refresh.
- Recovery remains conservative: it retains the interrupted state, reconstructs from intact originals and catalog, invalidates prior results, and does not silently claim that an old agent extraction was re-executed. Agent extractions moved into recovery history must be imported again explicitly; this is conservative behavior rather than automatic preservation.
- Recursive model inventory binds nested source files, rejects escaping symlinks, compiled objects and toolchain-name shadowing. Local imports are limited to that inventory. Clean Lake builds and exact target assertions remain in place, with axiom inspection for every inspected theorem and all referenced targets.
- The actual selected Lean version is checked against immutable per-run policy. Mismatches retain observed and required versions without a formal success. Literal masking no longer treats ordinary forbidden words inside strings as commands; executable interpolated strings remain rejected.

## Validation scope and limits

The independent executed probe in this review covers the identical-refresh state machine only. The nested link defect was established directly from the renderer and path contract. No Lean compilation was executed by this reviewer in this pass; parent-reported test results are not presented here as independently reproduced. No new false-success path was found in the inspected hash, role, uncertainty, target or axiom boundaries. That limited negative finding is not a security certification: the documented reviewed-code and semantic-correspondence boundaries still apply.
