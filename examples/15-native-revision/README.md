# Native document revision and audit invalidation

This entirely synthetic dossier demonstrates an evidence-backed audit of an existing report. It includes two supplied report variants, a native DOCX policy, a searchable PDF charge ledger, and an actual image-only PDF receipt. No separate review brief is supplied: the auditor infers verification questions from each report finding and source rule.

Use exactly one report and the `sources/` directory as initial audit input. Keep `masters/`, this README, the builder, the alternate report, and `revisions/` outside that input set. The builder's text masters are generation inputs, not additional documentary witnesses. The replacement ledger is deliberately outside the initial sources.

| File | Role |
| --- | --- |
| `sources/01-policy.docx` | Governing charge, receipt and approval rules; DOCX XML paragraph provenance |
| `sources/02-ledger.pdf` | Revision 1 searchable ledger: A=60, B=40, C=20 whole credits |
| `sources/03-receipt-scan.pdf` | Image-only receipt: transfer T7, receipt 16:40, dispatch 16:10 |
| `report.md` | Deliberately mixed report with erroneous and correct findings |
| `report-correct.md` | Carefully scoped report correct against revision 1 only |
| `revisions/02-ledger-r2.pdf` | Replacement ledger: C changes 20→45, explicitly superseding revision 1 |
| `masters/` | Deterministic source-generation text, excluded from evidence |
| `manifest.json` | Fixture-byte inventory; not an authenticity certificate |

The existing filename `report-correct.md` identifies the initially correct variant. Its unchanged total 120 becomes false against the replacement ledger's total 145. Neither report is silently edited during revision. Missing security status never becomes a negative event fact. Policy P4 supplies necessary approval conditions; it does not declare that both approvals are sufficient for every aspect of eligibility.

## Rebuild the input fixture

From the repository root:

```bash
python3 examples/15-native-revision/build_fixture.py
```

The builder uses the repository's deterministic standard-library PDF/DOCX writers and Pillow for the scanned page. It does not run a semantic audit or fabricate proof results. The source binary hashes were verified stable across rebuilding in the executed demonstration environment. Fonts and Pillow are environmental dependencies for identical scan bytes on another machine.

## Executed workflow

The authored audits are explicitly **nonblind**: the author created this fixture and then audited both variants separately. Independent source-first review, if present in the exported artifacts, is a separate check by another agent; it does not retroactively make authoring blind. Actual run paths, verdict transitions and command records are listed in the [retained run summary](../../tmp/native-revision-build/summary.json). The four exports are under `tmp/native-revision-exports/`; these retained local artifacts are separate from the input fixture and from any published walkthrough.

The actual workflow prepared indexed v2 workspaces in bounded batches, resumed extraction, reviewed every supplied passage, and executed Lean 4.24.0. OCR really misread the scan's `T7` as `17`. After rendering and inspecting the original with an image viewer, the auditor used the controlled `transcribe` operation. Both the erroneous OCR and the hash-bound reviewed transcription remain available. The scan stays marked `partial`; acknowledgement of the known limitation is not a declaration that machine OCR is perfect.

The initial corrected-report preparation processed 2 of 4 documents; its actual resume processed the remaining 2. The other variant used batches 2+1+1. DOCX source coordinates refer to XML paragraphs; PDF coordinates are word boxes; OCR confidence and pixels remain tool output. The DOCX XML and both original ledger PDF renderings were also inspected before extraction acceptance was recorded.

Each audit registers all 7 conclusion findings under contract v2. Report premises, citations and inferences are quoted and assessed separately as argument obligations. The title is explicitly non-claim. Typed Lean `Ledger` and `Receipt` records preserve source amounts, transfer identity, date and receipt minute. Exact target checks and actual axiom logs remain in each run. The Boolean proof is auxiliary: it refutes quality-only sufficiency without pretending to prove an absent security event.

After initial checks, `refresh` created retained child workspaces for replacement document `D00003`. Before authoring any new judgments, both `check` and `render` were actually attempted and rejected for each revised run because old R1 evidence no longer matched the new source. The preserved `stale-rejections.json` contains commands, exit codes and stderr. All technical results were invalidated. The auditor then renewed source acceptance, reviewed the affected claims, updated model parameters, acknowledged the revision hash, reran Lean, and rendered/exported the revised audit.

## Declared dependency and verdict transitions

The complete document-dependency declaration is a reviewed semantic assumption, not automatically discovered truth. It includes bounded support searches as well as direct evidence.

| Finding | Documents | Refresh effect and rationale |
| --- | --- | --- |
| R1 total | D00002 policy, D00003 ledger | Affected. Initial 120 becomes 145. Mixed 130 remains refuted; initially correct 120 changes from supported/proved to refuted. The unchanged report's C=20 premise is now contradicted by the superseding ledger. |
| R2 charge-A cap | D00002, D00003 | Conservatively affected at document granularity; A=60 and cap=50 remain unchanged, so verdict stays the same after review. |
| R3 receipt timestamp | D00004 receipt | Semantically unaffected. Reviewed transfer/date/time tuple is unchanged. All technical targets are nevertheless rechecked. |
| R4 receipt deadline | D00002, D00004 | Semantically unaffected. Receipt16:40 remains after cutoff 16:30; the approval cutoff 17:00 is a different rule. |
| R5 release support | D00002, D00003, D00004 | Affected and reviewed. Quality at 16:00 and missing security status remain unchanged; actual eligibility remains unresolved and the unsupported-certainty defect persists. |
| R6 charge-B amount | D00003 | Affected and reviewed. B=40 remains supported; absent report justification remains a support-gap finding. |
| R7 exemplary criterion | D00002, D00003, D00004 | Conservatively affected because the bounded search includes the whole package. No grading scale is introduced; the evaluative/absence-of-rubric verdict stays unchanged. |

No external theorem replay checker was configured; actual Lean compilation, exact-target validation and axiom checks are the executed formal assurance. Documentary transcription, criteria inference, dependency completeness and source-to-symbol fidelity remain review responsibilities.
