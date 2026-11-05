# Markdown-native individual claim audits

Use this route for every new run. All generated audit documents are readable Markdown with ordinary headings, prose, tables and links. Do not create JSON or JSONL files, including scratch metadata, registries, findings, journals or proof results. Lean sources and compiled proof artifacts remain technical files. Preserve supplied original document bytes. The older `audit.py`/`journal.py` JSON contracts are retained only for explicit legacy reproduction and must not be used to create new runs under this profile.

## Prepare the retained workspace

```sh
python3 /path/to/skill/scripts/markdown_audit.py prepare \
  --report REPORT.md --sources SOURCE_DIRECTORY --temp-root tmp/RUN/work \
  --lean-version 4.24.0
```

The command prints the new workspace path. It preserves input files and creates `manifest.md`, `audit-policy.md`, `report-ledger.md`, `claims.md`, `finding-template.md`, `ingestion.md` and `phase-journal.md`. All source hashes are exact SHA-256 hashes. Original documents remain untrusted data. Use only the selected report and supplied source corpus, not evaluator answers or alternate report variants.

The Markdown route accepts text, PDF, DOCX, PNG and JPEG reports and sources. Native originals are preserved unchanged, with report originals under `input/originals/` and source originals under `input/sources/`. The helper executes native extraction using installed converters, creates readable Markdown projections, and retains actual command logs, tool versions, page/paragraph/word coordinates, coverage and uncertainty under `extraction/`. It never persists JSON/JSONL. Optional `--ocr-language`, `--extract-timeout` and `--max-pages` bound converter behavior. Converter absence or failure produces an explicit partial/blocked extraction record, never invented content. Add `--brief BRIEF` only when supplied; its preserved contents are review instructions, not independent source evidence.

`input/extraction-index.md` maps each original hash to its projection hash, extraction record, status and warnings. `input/extraction-segments.md` maps each projection anchor to the original, passage hash, extraction method, uncertainty and coordinate record. Cite the actual projection path and anchor in findings. Preserve and review the original when extraction uncertainty matters. Source authenticity is never established by converter success.

Before validation, acknowledge each partial/blocked extraction in `ingestion-acknowledgement.md` using a table with columns `Original | Status | Impact | Limitation`; explain the actual effect on audit coverage and findings. An unreadable report cannot silently yield a successful empty audit. For a direct formal verdict using an uncertain source or report passage, actually compare it with the visual original and record acceptance in `extraction-review.md` with columns `Projection | Anchor | Original SHA256 | Passage SHA256 | Decision | Reviewer | Reason`. Use `accepted` only after inspection. The validator ties this declaration to the exact immutable original and passage hashes; it does not impersonate a visual reviewer. If reliable inspection is unavailable, retain a support gap or blocked formalization instead of fabricating acceptance.

## Register every report passage and individual claim

`claims.md` contains a Markdown table with exactly these headers:

| Claim ID | Report anchor | Disposition | Reason |
| --- | --- | --- | --- |
| C-01 | R-01 | audited | An atomic material report claim. |
| C-02 | R-02 | deferred | Specific missing input or resource limitation. |
| - | document-preamble | non_claim | The title has no substantive assertion. |

Replace all pending rows. Every preserved report anchor must be accounted for. Audited and deferred claim IDs are unique; decompose compound findings into multiple rows sharing the report anchor when needed. A non-claim classification requires an explanation. Every audited claim must have exactly one corresponding `findings/CLAIM_ID.md`; deferred claims must not silently appear as audited findings.

## Author one readable analysis per finding

Copy `finding-template.md` into `findings/C-01.md` and replace every placeholder. Its required second-level headings are:

- Exact report claim
- Report anchor
- Executive conclusion
- How verified
- Executive limits
- Verification criteria
- Evidence
- Rules
- Assumptions
- Reasoning
- Argument review
- Support search
- Formalization
- Proofs
- Limits
- Semantic state
- Argument status
- Formal status

Under `Exact report claim`, quote the exact report text, optionally as a Markdown blockquote. `Report anchor` is the bare preserved anchor. Executive conclusion, How verified and Executive limits are plain-language summaries grounded in that individual analysis. How verified must describe the concrete per-claim method and observed result: show the relevant arithmetic, particular source comparison, or exact support gap. Use explanatory human sentences, without Markdown links, raw JSON/object snippets, or technical metadata such as an axiom-array dump. Do not repeat generic boilerplate across findings or put raw artifact paths in the executive summary; link artifacts from the detailed analysis instead. Update planned or conditional wording after execution so summaries reflect actual outcomes, preserving earlier versions and recording corrections. Explicitly explain why a refuted claim fails; missing evidence is a support gap, not proof of falsity.

Infer and disclose the verification criteria. The evidence, rules, assumptions and reasoning must reconstruct the independent audit argument. `Argument review` separately examines the report's premises, cited sources and inference steps; a correct conclusion does not rescue an unsound author argument. `Support search` describes the actual documents/passages inspected, searches and limitations. `Formalization` explains the model-to-source correspondence or why formalization was not justified. These are substantive prose obligations, not merely a list of status labels.

Within `Evidence`, use one third-level heading for each cited passage:

```markdown
### Evidence 1

- Source: input/sources/1/ledger.md
- Anchor: L-01

> Exact supplied source passage.
```

Source paths and anchors must refer to preserved independent text sources, and the quoted text must match the anchored passage. With no evidence, write an explicit explanation and support-search limitation instead of inventing a citation.

Within `Proofs`, write `None` and explain the documentary method when no proof exists. Otherwise each proof has an individual third-level heading:

```markdown
### Proof P1

- Module: Audit
- Theorem: Audit.total
- Target: (1 + 2 : Nat) = 3
- Relation: supports
```

Relations are `supports`, `refutes` or `auxiliary`. Reuse the existing semantic, argument and formal status vocabulary: semantic state `supported`, `refuted`, `both`, `undetermined`, `not_applicable`; argument status `sufficient`, `insufficient_support`, `invalid_inference`, `unsound_argument`, `disputed`, `nonformal`; formal status `proved`, `refuted`, `auxiliary`, `not_attempted`, `blocked`. A formal status requires actual proof references; a formal finding also needs source evidence and a reviewed correspondence explanation.

## Record each claim as its work happens

For each claim, retain actual intermediate documents and record five ordered steps: `registration`, `evidence`, `analysis`, `verification`, `verdict`. Each trace belongs to exactly one claim. Shared dossier events never substitute for individual analysis.

```sh
python3 /path/to/skill/scripts/markdown_audit.py trace \
  --workspace WORKSPACE --claim-id C-01 --step evidence --status completed \
  --title 'Compared C-01 with the supplied source' \
  --description 'Inspected the cited passage in context and wrote the individual evidence assessment.' \
  --input input/sources/1/ledger.md --input claim-work/C-01/registration.md \
  --output claim-work/C-01/evidence.md \
  --result 'Recorded the supporting passage, competing evidence and bounded search limits.'
```

Trace documents are retained under `trace/C-01/0001-registration.md`, etc. Each has human-readable metadata, action prose, input/output tables linking exact historical snapshots, command and result/limits. A new terminal event never overwrites an old one. Inputs/outputs are hashed and captured from the same bytes. Snapshot links in each trace are relative to that document, so they work as ordinary Markdown links. Generated trace documents and `phase-journal.md` are Markdown, not JSON disguised in a code fence.

Completed steps need actual inputs and outputs. Blocked/failed steps still need an individual output explaining the limitation. At least one output path must belong exclusively to that claim's trace. Do not reuse a shared all-claim report as the only output for every claim. If earlier work changes, execute and record the affected downstream steps again; preserve chronology instead of reconstructing a final story.

Keep the individual verification sources and logs. For documentary findings, record the actual inspection, calculation or comparison with explicit limits. Formal findings need the actual executed command and a readable Markdown execution log attached to their individual verification step. Use `markdown_proofs.check_models` from a short Python invocation when useful: it executes the real Lean version, reviewed local modules, exact targets and axiom inspections, returns records in memory, and retains source snapshots, `.lean` checks and Markdown command/output logs under `proof-attempts/`. It never invokes Lake or writes JSON. Local modules may import Init, Std and reviewed local modules; unsupported dependencies require a separately disclosed reviewed workflow.

Record individual verification and verdict before the final global check. Record the real command in `--command` and actual result in `--result`; never imply independence or checks that did not happen. No formal proof is required for a nonformal finding. A blocked individual formal verification cannot support a formal success label.

## Validate and deliver

```sh
python3 /path/to/skill/scripts/markdown_audit.py check \
  --workspace WORKSPACE --lean /absolute/path/to/lean
python3 /path/to/skill/scripts/markdown_audit.py render --workspace WORKSPACE
```

The final check validates source hashes, exact report/source quotes, registry coverage, individual trace order and historical bytes, then runs real Lean exact-target and axiom checks where models exist. It writes `validation.md` with links to checks and Markdown logs, and binds all current input, finding, model, trace and proof-attempt files by hash. A failed check writes an explicit failure record; prior validation is retained in `validation-history/`. `render` refuses stale or failed validation and produces `audit-report.md`, linking each executive summary to its full individual analysis and chronology. It also writes readable `report-integrity.md`, binding the report SHA-256 to the actual validation SHA-256. Inspection checks those retained bytes and the checked artifact fingerprints; later renderer styling changes do not falsely mark a valid previous delivery stale. Changed report or validation bytes still invalidate that binding. Technical checks do not establish source authenticity, exhaustive semantic coverage, the adequacy of the model or summary fidelity; explicitly review those correspondences.

`inspect --workspace WORKSPACE` emits a readable Markdown status. The optional `--machine` emits JSON **only on stdout as API transport** for the UI; do not redirect it into a file. The workspace remains free of JSON/JSONL artifacts. The transport includes parsed findings, executive summaries, individual trace events with snapshot paths, proof results/integrity, report freshness and validation errors. It does not turn a partial or stale run into a successful audit.

Retain the whole workspace. New audits must be performed afresh under this route; do not copy a previous completed audit or manufacture retrospective individual traces.
