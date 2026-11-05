# Recorded phase chronology

Every new audit records its actual actions in append-only `phases.jsonl`. For a debug UI run with a containing audit root and a `workspace/` child, place the journal at `AUDIT_ROOT/phases.jsonl` and use `--workspace AUDIT_ROOT/workspace --journal-root AUDIT_ROOT`. Recorded artifact paths always resolve relative to the journal directory (the audit root when `--journal-root` is supplied). CLI `--input` and `--output` arguments resolve relative to the workspace, then are recorded relative to the journal directory. The default standalone helper location is `WORKSPACE/phases.jsonl`; choose one authoritative journal per run and retain it on delivery.

Record `started` before a phase's work, `completed` only after its stated scope is finished, and `failed` or `blocked` when appropriate. Use `note` for intermediate actions or explicit limitations. Repeat phases for revisions; order is append order with UTC timestamps, not a fixed pipeline. For each meaningful action, describe what was done and why, link affected claim IDs, identify consumed and produced artifacts and record the result. Record searches, model revisions and reviewer disagreements as they occur. Do not create successful events for unexecuted phases, backdate events, reconstruct invented history from file modification times, or convert a support gap to a false conclusion.

Each JSON line follows [the event schema](../schemas/phase-event.schema.json) and has these fields:

- `schema_version`: integer `1`.
- `event_id`: unique nonempty string (the helper emits a UUID).
- `timestamp`: ISO 8601 UTC timestamp.
- `phase`: `intake`, `extraction`, `claims`, `evidence`, `modeling`, `verification`, `review`, or `reporting`.
- `status`: `started`, `completed`, `failed`, `blocked`, or `note`.
- `title`, `description`: nonempty English strings describing the actual action and scope.
- `claim_ids`: array of stable claim IDs; empty for whole-run actions or before registration.
- `inputs`, `outputs`: arrays of `{ "path": "journal-relative/file", "sha256": "64 lowercase hex characters", "snapshot": "phase-artifacts/DIGEST/filename" }`. The optional `snapshot` field identifies retained historical bytes; new helper events always include it, while older events without it remain valid and are explicitly reported as having unavailable historical snapshots. Hash exact bytes when recording the event. References must be files inside the journal root; directories, escaping paths and external symlinks are rejected.
- Optional `command`, `result`: strings containing the actual command and outcome; omit when inapplicable. Do not include credentials.

Example invocation (substitute existing artifacts and actual action details):

```sh
python3 /path/to/skill/scripts/journal.py append \
  --workspace AUDIT_ROOT/workspace --journal-root AUDIT_ROOT \
  --phase evidence --status completed --title 'Reviewed source support for C-01' \
  --description 'Compared the registered claim with the cited source and recorded the search scope and limitations.' \
  --claim-id C-01 --input claims.json --output support-search.json
python3 /path/to/skill/scripts/journal.py validate \
  --workspace AUDIT_ROOT/workspace --journal-root AUDIT_ROOT
```

The dependency-free helper calculates real hashes, validates existing event structure before append, and never rewrites history. Use a single writer per journal; coordinate concurrent reviewers through the main agent. Validation reports historical hash differences as `artifact_changes`, because mutable artifacts can legitimately evolve. New helper appends stream each artifact into a content-addressed snapshot under `phase-artifacts/<sha256>/<basename>` before recording its reference. The snapshot and digest come from the same byte stream. Existing snapshots are never silently replaced. Validation requires every recorded snapshot to exist and match its digest; corruption or missing snapshots fails validation. Older references without `snapshot` are reported in `unavailable_snapshots`; their digest alone cannot recover historical bytes. Preview `snapshot` when available, preserving the original `path` label. Missing or changed current artifacts are visible, not silently accepted as identical. Structural errors, duplicate IDs and decreasing timestamps fail validation. A hash is not proof of semantic correctness or authenticity, and the journal is not a tamper-proof ledger.

`audit.py prepare` records its successful workspace preparation as an intake event. The `check` and `render` CLI commands append started/completed or failed events with their effective full CLI invocation. Verification completion links and snapshots `proof-results.json`, `environment.lock`, generated `checks/**/*.lean` and actual `logs/**/*.log`, excluding build caches; `--journal-root` selects the containing root. These helper events cover only actual helper execution. They do not assert that an agent analyzed claims, reviewed evidence, built adequate models or performed independent review. Direct Python calls to `check`/`render` do not emit CLI events. Record those operations explicitly if used. Preparation creates its default workspace journal; when adopting a containing audit root, retain that nested journal and begin root events explicitly. Consumers may aggregate nested journals by resolving references relative to each journal directory and deduplicating event IDs. A preparation failure before returning a workspace cannot emit a workspace event; record it in the already-created containing audit root when available.

A historical bundle without a journal has `legacy_unknown` chronology, not an empty successful audit. Later recorded actions on that bundle establish only those actions; earlier phases remain unknown. UI views must distinguish recorded events from artifact-based legacy observations. For agent-native execution, append equivalent JSON lines using available tools, actual UTC time and real byte hashes; disclose unavailable hashing or logging and do not fabricate valid-looking events. Preserve raw tool logs separately and reference them from events.

## Individual claim traces for new runs

Prepare every new audit with `audit.py prepare --require-claim-traces`. This writes `require_claim_traces: true` into the immutable input policy, for both plain-text and indexed ingestion. Older workspaces without this marker remain explicitly `legacy_unenforced`; rechecking them does not manufacture missing historical analysis. Do not retrofit a completed run with a reconstructed trace. Start a fresh audit when the individual chronology is required.

For **each finding separately**, record these `claim_step` values in actual execution order: `registration`, `evidence`, `analysis`, `verification`, `verdict`. The optional event field `claim_step` is selected with `journal.py append --claim-step STEP` and requires exactly one `--claim-id`. Shared phase events are useful context but never satisfy an individual trace. Record starts as work begins and terminal events immediately after each step, not after the entire dossier is finished. Preserve concrete intermediate outputs under a claim-specific directory such as `claim-work/C-01/`; each step must have at least one output path belonging exclusively to that claim's trace. A single shared all-claim file is insufficient.

A completed individual step requires nonempty `inputs` and `outputs` with actual historical snapshots, plus `--result` explaining its observed outcome. A blocked or failed step still requires an individual output artifact containing the concrete limitation and an explicit `result`; it must never be relabelled as successful. For an intentionally inapplicable formal method, complete the appropriate documentary verification and disclose why formalization was not attempted, or use a blocked verification with an explicit limitation. No formal proof is required for nonformal findings.

For example, after actually inspecting the relevant source and writing the claim's evidence analysis:

```sh
python3 /path/to/skill/scripts/journal.py append \
  --workspace WORKSPACE --journal-root AUDIT_ROOT \
  --phase evidence --claim-step evidence --claim-id C-01 --status completed \
  --title 'Compared C-01 with its cited source' \
  --description 'Inspected the cited passage in context and recorded competing evidence and search limits.' \
  --input input/sources/source.md --input claim-work/C-01/registration.json \
  --output claim-work/C-01/evidence.md \
  --result 'The evidence assessment and bounded search are recorded in the individual artifact.'
```

The individual `analysis` output explains the claim's premises, source rules, assumptions, reasoning, counterevidence, inference defects and limits. The `verification` output records what was actually checked, including failed attempts. For a finding with formal proof references, its latest verification must be completed and include the actual `command` plus a retained `.log` output; execute its Lean targets before the final global `audit.py check`. Retain individual check sources and logs outside the helper's replaceable `checks/` and `logs/` directories, for example in `claim-work/C-01/`. Global helper events supplement these individual checks and cannot replace them.

The `verdict` output records the explained result and its executive summary. Every finding in `findings.json` must include:

```json
"executive_summary": {
  "conclusion": "Plain-language statement of what the audit found about this claim.",
  "how_verified": "Specific evidence, reasoning and checks actually used for this claim.",
  "limits": "Material assumptions, support gaps and scope limits."
}
```

Ground these three nonempty strings in the individual analysis; this is a readable synopsis, not a different conclusion. Review this correspondence explicitly. Mechanical validation checks structure, artifacts and chronology, not the truth or adequacy of the prose.

After recording the individual verdicts, run the final helper check with the same `--journal-root`, then render/export with that root. Strict-profile check, render and export require all five terminal steps per finding. If a step is revised, repeat downstream work and record fresh terminal events: a later evidence revision cannot silently retain an earlier verdict. Blocked and failed limitations remain visible in `proof-results.json` under `claim_trace_contract.limitations`. Do not add proof references to findings whose individual verification is blocked or lacks a real command and log. The automatic helper check occurs after individual trace validation, so its global event is never used to satisfy the preexisting individual verification obligation.
