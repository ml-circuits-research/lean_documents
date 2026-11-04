# Evidence-to-Proof Review

Audit findings in a supplied report against source documents. Produce clear evidence-backed arguments, scoped formal proofs or refutations where justified, and explicit findings about missing or insufficient support.

Start with the [HTML documentation](docs/index.html), [implementation plan](docs/implementation.html), and [sixteen synthetic dossiers](examples/README.md). Each dossier includes both a correct report and a deliberately flawed report for separate audits.

The implemented [skill](skills/evidence-to-proof-review/SKILL.md) audits supplied findings with a coding agent and deterministic validation helpers. See [executed validation](docs/validation.html) for completed audit runs, real Lean logs, and limits. The extended engine supports UTF-8 text, DOCX, searchable/scanned PDF and image OCR, with coordinates, uncertainty, disk-backed indexing, resumable batches and source-change invalidation. See [formats and operation](docs/extensions.html).

Use the skill by giving a coding agent its SKILL.md path, the report and all source paths. A review brief is optional: the agent infers and declares criteria from each finding and the sources. Each request gets a private temporary workspace. The helpers do not replace semantic analysis by the agent.

Run helper tests with `AUDIT_TEST_LEAN=/path/to/lean python3 -m unittest discover -s tests -v`. Each run pins its Lean version; the regression suite currently uses Lean 4.24.0; the distribution URL and SHA-256 are recorded in [toolchain.json](validation/toolchain.json).

All repository artifacts are in English; conversation with the user is in Romanian. See [AGENTS.md](AGENTS.md).

The skill folder is self-contained. The method requires the agent’s document/file tools and an actual Lean executable. The documented agent-native route does not require the Python helpers. For the automated helper route, run `python3 skills/evidence-to-proof-review/scripts/audit.py doctor --lean /absolute/path/to/lean`. Those helpers require Python (plus SQLite FTS5 for indexing) and Lean with Lake for proofs. Built-in PDF/OCR adapters use Poppler/Tesseract; other available agent tools can supply provenance-preserving extractions. Each run pins its installed stable Lean 4 version; 4.24.0 is the executed regression version. No pip package or repository examples are needed at runtime. See [requirements](skills/evidence-to-proof-review/references/requirements.md).

New runs enforce [audit contract v2](skills/evidence-to-proof-review/references/audit-contract-v2.md): reviewed report passages, reconciled claim coverage, independently checked report arguments, bounded support searches, and per-proof source correspondence. See the [general method](docs/general-method.html) and [v2 validation](docs/general-validation.html). Historical bundles remain labelled legacy and do not inherit these new guarantees.

Study the [offline example catalog](docs/examples/index.html): both reports for each of 16 dossiers, 34 audit snapshots including source revisions, intermediate files, exact Lean targets, logs and independent-review limits. The published data under docs/examples is intended for GitHub; tmp/ remains ignored and retained.

See the [flexibility review](docs/flexibility-review.html) for the fact/method layer, independent argument checks, optional agent-native execution, extraction import, reusable Lean modules and executed portability tests.

Start with [one finding, two verdicts](docs/examples/start-here.html), continue through [native-source correction and changed verdicts](docs/examples/revision-walkthrough.html), then inspect the [executed capability matrix](docs/examples/capabilities.html). The catalog distinguishes 12 v2 helper audit snapshots, 2 agent-native audits and 20 historical legacy audits. The latest expansion adds 8 actual audits and reuses 2 earlier mixed demonstrations after input-identity checks.
