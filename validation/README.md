# Executed validation

Ten synthetic dossiers were audited in twenty separate current run bundles, one per supplied report variant. The initial five dossiers contain 81 original findings; five larger native-format dossiers add 156. All 237 current report findings are represented by 250 atomic audit findings. There are 211 checked theorem declarations and 429 declaration/target checks. These figures include auxiliary proofs; they are not a blanket certification of the reports or source truth.

Read the [HTML results](../docs/validation.html), [per-claim comparison](summary.json), [initial and extended review](review.md), and [extended source-first records](extended/semantic-review/review.json). Every exported run includes selected original documents, anchored evidence, arguments, model meanings, Lean sources, actual logs, coverage and review limits. Working directories remain under Git-ignored `tmp/`.

## Comparison and a corrected fixture

All 237 final grouped outcomes agree with editorial expectations after a transparent fixture correction. The first extended comparison was 155/156: the supposedly correct report 09 said its maximum was “118 milliseconds below 120”. Its auditor correctly withheld an unqualified verdict because that wording could mean a margin of 118 instead of a measured maximum of 118. The report was clarified to say maximum 118, below the 120 limit. Sources and expected semantic intentions did not change. A fresh report revision invalidated all fourteen findings; all were reconsidered, actual Lean checks rerun, and independent review repeated. The original disputed audit, old/new bytes, hashes and comparison remain in [the correction record](extended/fixture-corrections/09-report-wording/correction.json) and [original audit](extended/fixture-corrections/09-report-wording/original-audit/audit-report.md).

Agreement with editorial expectations is not a statistical reliability estimate or domain-expert certification. Evaluators can be wrong. Initial auditors did not receive expected outcomes or the alternate report. Some agents were reused across unrelated cases; none authored the expectations for a case it audited or audited both variants of that case. The later reviewer compared both variants, first saving its source interpretation before reading findings/models. Shared filesystem/model-family limits and prior knowledge of one OCR correction are explicit in the review record.

## Tools and implemented extensions

Lean 4.24.0 with core Init/Std is pinned in [toolchain provenance](toolchain.json). A compatible lean4checker was built and executed for additional selected fresh environment replays; it uses the same Lean kernel, not an independent implementation. [Checker provenance and logs](checker-toolchain.json) distinguish actual execution from availability. Most runs use standard Lean checks without that optional replay.

The [portable skill](../skills/evidence-to-proof-review/SKILL.md) needs Python with SQLite FTS5; its own scripts use only standard-library and sibling modules. DOCX is parsed locally through ZIP/XML. PDF uses Poppler; scanned PDF/PNG/JPEG use Tesseract and selected language data. Proofs need Lean and Lake. The [requirements](../skills/evidence-to-proof-review/references/requirements.md) and [format/scale documentation](../docs/extensions.html) explain installation prerequisites, coordinates, uncertainty, bounded/resumable processing and changed-source invalidation. No example/evaluator file is a runtime dependency.

Executed checks include [1,000-source ingestion/retrieval](extended/scale.json), [isolated copied-package operation](extended/portability.json), [stale-result rejection after changing a source](extended/invalidation.json), and [independent implementation review](extended/code-review/review.md). The latter found and verified repairs for retained manual transcriptions during retry and tracked DOCX row/cell changes. The [full test log](../tests/validation.log) contains 91 passed tests, with real Poppler, OCR and Lean checks where relevant, plus explicitly identified negative controls.

## Run a new audit

Give a coding agent the skill path, selected report, brief and authorized sources. The agent performs semantic interpretation, argument construction and formalization; the helpers do not autonomously understand documents.

```bash
python3 skills/evidence-to-proof-review/scripts/audit.py doctor --lean /absolute/path/to/lean
python3 skills/evidence-to-proof-review/scripts/audit.py prepare --indexed \
  --brief /path/to/brief.md --report /path/to/report.docx \
  --sources /path/to/source-directory --temp-root tmp
```

The command creates a unique retained workspace. Native OCR uncertainty or missing input produces explicit partial/blocked coverage, not a false conclusion. Visually corrected transcriptions retain original OCR and get distinct reviewed anchors. The agent writes the findings and models, runs check, obtains semantic review, renders the explained audit and exports the bundle.

## Reproduce

```bash
python3 validation/reproduce.py --lean /absolute/path/to/lean
python3 validation/evaluate.py --output validation/summary.json
AUDIT_TEST_LEAN=/absolute/path/to/lean python3 -m unittest discover -s tests -v
```

Reproduction verifies exported hashes, copies each run into a fresh retained `tmp/reproduction-*` directory, then executes the actual technical checks without evaluator answers. [Reproduction records](reproduction.json) link to exact commands/results in `reproduction/`. Optional replay can be requested for one bundle with `--only 06-procurement-contract-mixed --checker /path/to/compatible/lean4checker`; those outputs use `reproduction-checker/`.

Source authenticity, completeness beyond declared closed domains, semantic fidelity, legal authority and real-world safety remain separate from mathematical entailment. OCR confidence is not proof of correctness. The fixtures are synthetic; no real client corpus has been certified by these tests. All intermediate work, failed attempts and earlier report versions are retained for inspection.
