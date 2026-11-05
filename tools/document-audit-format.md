# Readable document audit pilot

Use `tools/document_audit.py` for the readable-document workspace. Internal JSON holds precise records; human-facing documents are generated Markdown prose, evidence tables and links. Do not hand-format recursive field trees or print JSON into the human documents. Only the selected report and supplied source documents are audit evidence.

## Commands

```sh
python3 tools/document_audit.py prepare --report REPORT.md --sources SOURCE_DIRECTORY --temp-root RUN/work
python3 tools/document_audit.py record --workspace WORKSPACE --claim-id C-01 --step registration --document claim-work/C-01/registration.json --input input/report.md --output claim-work/C-01/registration.json
python3 tools/document_audit.py check --workspace WORKSPACE --lean /absolute/path/to/lean
python3 tools/document_audit.py render --workspace WORKSPACE
python3 tools/document_audit.py inspect --workspace WORKSPACE --machine
```

Preparation prints the fresh workspace path. Sources are copied under `input/sources/1/` for the first supplied source directory. This pilot accepts text reports and sources. Readable headings such as `## R01 — Valuation` and `## S01 — Transaction terms` define anchors; text before the first anchored heading is `document-preamble`. Exact quotes must occur in the corresponding substantive section. The Lean version defaults to 4.24.0; `check --lean-version VERSION` pins another available version explicitly.

## Claim coverage

Edit the generated `claims.json`, preserving all initial anchor quotes. Its structure is:

```json
{
  "schema_version": 1,
  "anchors": [
    {"anchor": "document-preamble", "quote": "EXACT PRESERVED PREAMBLE", "classification": "non_claim", "reason": "A document title, not a substantive finding."},
    {"anchor": "R01", "quote": "EXACT PRESERVED SECTION", "classification": "claims", "reason": "Contains the first material claim."}
  ],
  "claims": [
    {"claim_id": "C-01", "report_anchor": "R01", "report_quote": "EXACT ATOMIC REPORT CLAIM", "disposition": "audited", "reason": "The proposition is within the supplied review scope."}
  ]
}
```

Every anchor must be classified `claims` or `non_claim`, with a reason. Register every material proposition; an explicit `deferred` claim needs a specific reason and must not appear as a completed finding. A true premise must not be presented as a supported verdict on a false compound conclusion: use the exact atomic quote and retain larger context in the analysis. Do not use the report as independent evidence.

## Individual findings

Author one `findings/C-01.json` per audited claim. Use these canonical fields:

```json
{
  "claim_id": "C-01",
  "title": "A concise business title, such as Implied equity valuation",
  "report_anchor": "R01",
  "report_quote": "EXACT REGISTERED ATOMIC CLAIM",
  "question": "The concrete verification question inferred from this claim.",
  "executive_summary": {
    "conclusion": "What this individual audit found, in plain language.",
    "how_verified": "The concrete evidence comparison, calculation or actual check and its result.",
    "limits": "The material scope, missing information and assumptions."
  },
  "evidence": [
    {"path": "input/sources/1/terms.md", "anchor": "S01", "quote": "EXACT SOURCE QUOTE", "explanation": "How this passage supports, contradicts or limits this particular claim."}
  ],
  "rules": ["The applicable source-backed rule or calculation convention."],
  "assumptions": ["An explicit assumption; use an empty array if none."],
  "reasoning": ["Connected explanation linking the evidence and rule to the result."],
  "argument_audit": ["Check the report premise, citation and inference separately. Quote the author argument in prose and explain its supported or unsupported steps."],
  "limits": ["Detailed limitations without converting missing support to falsity."],
  "formalization": "Why the selected formal target is justified, its precise source-to-symbol correspondence, or why documentary verification is appropriate.",
  "proofs": [],
  "semantic_state": "undetermined",
  "argument_status": "insufficient_support",
  "formal_status": "not_attempted"
}
```

Only the documented fields are allowed; unknown fields are rejected rather than silently omitted. `title` is optional but encouraged: use a concise business title such as Implied equity valuation, Allocation mandate or Compliance clearance. Explanatory fields `rules`, `assumptions`, `reasoning`, `argument_audit`, `limits` and `formalization` must be strings or arrays of prose strings, never nested objects. All supported material prose appears in the human template.

Semantic states are `supported`, `refuted`, `both`, `undetermined`, `not_applicable`. Argument statuses are `sufficient`, `insufficient_support`, `invalid_inference`, `unsound_argument`, `disputed`, `nonformal`. Formal statuses are `proved`, `refuted`, `auxiliary`, `not_attempted`, `blocked`. Argument status concerns the argument actually supplied: a bare conclusion without citations or a derivation has `insufficient_support`, even when independent source checking refutes that conclusion. Reserve `invalid_inference` and `unsound_argument` for an identifiable expressed inference or premise, and distinguish the auditor’s reconstructed argument from the author’s argument.

For an actually checked formal target, each proof is `{ "module": "Model", "theorem": "Model.result", "target": "EXACT LEAN PROPOSITION", "relation": "supports", "claim_id": "C-01" }`, with relation `supports`, `refutes` or `auxiliary`. Models live under `models/`. An auxiliary theorem about an invalid inference does not prove that the underlying event is false. For a nonformal or unobserved event, keep proofs empty and give an explicit formalization rationale. Every finding needs a concrete executive verification explanation; no generic boilerplate, raw paths or Markdown links belong in these three summary strings.

## Five individually recorded steps

Perform and record `registration`, `evidence`, `analysis`, `verification`, `verdict` for each claim as the work happens. Each authored phase data document has this compact structure:

```json
{
  "title": "A descriptive title for this individual action",
  "purpose": "Why this step was needed for the particular claim.",
  "method": "What was actually read, compared, calculated or executed.",
  "observations": [
    {"source": "input/sources/1/terms.md", "quote": "Relevant exact passage", "use": "Its concrete use in this step."}
  ],
  "result": "The observed result of this step, not a planned outcome.",
  "limits": "The actual limits of this result.",
  "status": "completed",
  "command": "The actual command, only when a command was executed."
}
```

`observations` may alternatively be connected prose or an array of prose strings. `status` defaults to `completed`; use `blocked` or `failed` honestly when appropriate. Do not invent executed commands. For example, execute a calculation and capture its real output before recording a verification that claims that calculation.

`record` reads the authored JSON, captures the current UTC timestamp and actual byte snapshots of the supplied `--input`/`--output` files, retains an immutable individual trace record, and generates readable `.md` counterparts for both phase documents and trace records. Completed steps require inputs and outputs. Every step needs at least one output path unique to that claim, not just a shared all-claims document. The final verdict's outputs **must include the exact current `findings/C-01.json`**. Record the current finding only after its actual evidence, analysis and verification are complete.

For individual formal verification before the final global check, call `markdown_proofs.check_models` in Python with the actual workspace, repository-local Lean path and this claim's proof references. Import it from `skills/evidence-to-proof-review/scripts`. It executes real Lean and returns log/check paths in memory, retaining Markdown execution logs, `.lean` exact-target checks and compiled artifacts in `proof-attempts/`. Include the actual command in the phase document and the real returned logs/checks in `--output`. The global `check` subsequently revalidates all findings and executes their proof targets again; its shared result never substitutes for individual recorded verification.

If earlier work changes, record the affected downstream steps again. Preserve prior records and snapshots. Do not reconstruct fictitious past chronology from final files.

## Human document templates and delivery

Phase documents open with a descriptive title and purpose paragraph, followed by a source/quote/use table under **What was examined**, narrative **Work performed**, **Result**, **Limits**, and a readable retained-artifact link table. Finding documents add the exact claim, question, source-backed reasoning, separate report-argument review and formal scope. They do not recursively enumerate internal data fields or show JSON objects to the reader.

The final `render` generates all human counterparts and `audit-report.md`, using per-claim executive conclusions, concrete verification explanations and limits. Internal JSON remains available to the validator but is not the document presented in the UI. Historical human snapshots are retained unchanged. Transport artifact `sha256` values identify the displayed human snapshot bytes; canonical data paths and hashes are separate internal fields.

Run `check`, then `render`. A failed or stale validation cannot yield a current delivery. The report has a saved hash binding to the actual validation record, so later harmless renderer styling changes do not invalidate previous report bytes. `inspect --machine` emits UI transport containing authored partial findings, individual phases, validation integrity and report freshness; partial artifacts are never labelled completed merely because they exist. Source authenticity, model correspondence and adequacy of prose still require explicit review.

## Document language

Choose the document language when creating a workspace: `prepare --language en` (default) or `prepare --language ro`. The manifest preserves that choice and its integrity binding. Write all authored titles, explanations and executive summaries in the selected language. Canonical JSON field names and enum values remain English. The helper localizes its own headings, table labels and explanatory text only; it never translates source quotes, proof targets, commands or authored analysis. Existing workspaces without a language field retain English templates. Do not change a prepared workspace language after review starts; create a separate audit for the other language.
