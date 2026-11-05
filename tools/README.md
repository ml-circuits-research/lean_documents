# Local report review workspace

Start the dependency-free Node.js server:

```sh
node tools/pilot.mjs
```

Open http://127.0.0.1:8787. The current examples are in `examples/pilot/`; execution artifacts are retained under `tmp/readable-pilot/`. The server uses built-in Node.js modules. Real writing and auditing require the configured Codex CLI, Python 3 and the repository-local Lean toolchain.

## Navigate the documents

The left tree contains examples. Each example contains its input files and its reports. Each report contains its findings; a finding can be expanded to its evidence, recorded work and Lean source. Selecting a node opens its content in the right pane. Normal source citations within documents remain clickable. Finding nodes carry an icon and an explicit semantic status: Supported, Refuted, Undetermined, Conflicting or Not applicable. Draft verdicts remain Pending until the audit finishes. Opening and closing a branch is independent of document selection, and automatic updates preserve branch state.

There are no popup readers, tabs, refresh controls or previous-verification histories. The display updates automatically. A new verification replaces the previous verification for that same supplied report. Distinct report documents remain separate report nodes.

## Work on an example

Choose English or Romanian when creating an example. The language is retained in its metadata and controls authored explanations and document templates. Uploaded originals are preserved byte-for-byte.

At the example level, add source documents or upload a supplied report. The red Stop control stops the example's active verification or report-writing processes and removes its queued work. Stopped work is not labelled verified.

Create report launches the separate [investment-report-writer skill](../skills/investment-report-writer/SKILL.md) through the real Codex CLI. A grounded report uses the supplied sources and states unresolved evidence. The deliberate-errors mode produces a local test report with intentional mistakes, recorded separately in generation notes. No mode authorizes invented underlying evidence or source quotations.

A successfully drafted report is added as a new report node. It is not certified by its author. Select it and run Verify report to invoke the independent audit skill. The auditor receives only that report and its preserved source documents, never the report writer's generation notes or intended errors.

## Understand the records

Internal JSON stores typed claim, evidence, execution and integrity records. Dedicated templates generate complete human documents using prose, comparison tables and descriptive links. JSON is not displayed as a recursive tree. See the [readable document contract](document-audit-format.md).

Each finding retains its own source review, reasoning, formalization, executed checks and conclusion. Real Lean source, exact checked targets, compiler output and declared axioms are accessible from the tree and document citations. Formal results establish the encoded targets under the stated source assumptions; they do not authenticate documents or establish an unknown real-world approval.

Current audits live under `tmp/readable-pilot/runs/`. Report-writing jobs live under `tmp/readable-pilot/report-jobs/`; their `generation-notes.md` and execution records are kept separate from the source corpus. Example metadata is in `example.md`. Source digests are checked before a generated report is published, so an input change during drafting cannot silently publish a result against different documents.

The server binds to loopback, checks Host and Origin, and confines file access to the selected example, audit or drafting job. Uploads are limited to 90 MB per request. `PORT` changes the port, and `CODEX_BIN` overrides the real executable. Explicit test executors are labelled simulated and use isolated directories.

## Validation

```sh
node tools/test-markdown-server.mjs
node tools/test-report-generation.mjs
node tools/test-audit-workspace.mjs investment-approval
node tools/test-audit-workspace.mjs investment-approval-ro
python3 -m unittest discover -s tests -p 'test_document_audit.py' -v
python3 tools/validate-readable-examples.py --output tmp/readable-pilot/example-validation.md
```

Server tests use controlled isolated inputs. Proof tests execute real Lean. Browser tests read the running application without creating examples or mutating audit documents. Their artifacts remain under `tmp/` for inspection. The read-only example validator checks the seven added dossiers in both languages, both current report variants, retained source snapshots, individual phases, proof targets and logs. It returns a failure while any required run is pending or incomplete and writes a readable summary; it does not substitute structural validity for semantic review.

## Current examples

| Example | Main verification problem |
| --- | --- |
| Investment approval (English and Romanian) | Valuation, allocation limit and missing clearance evidence. |
| Acquisition financing | Net debt, the leverage ceiling and lender approval authority. |
| Project funding release | Matching cash, milestone acceptance and board approval. |
| Annual IT budget | Recurring and one-off costs, VAT, annual allocation and delegated approval. |
| ThermalLoop research funding | Eligible costs, independent replication and an unknown ethics determination. |
| The Last Crossing | Elapsed time, inconsistent testimony and an unstated motive. |
| The Name on the Crate | Names versus people, incompatible locations and an unknown motive. |
| The House at Low Tide | Exact verse-line counts, repeated openings and unsupported universal reception. |

The seven added dossiers each have English and Romanian editions, with two separate supplied reports in each edition. A correct report can accurately identify a failed covenant or an evidence gap: “correct” describes its claims, not approval of the transaction. The auditor receives only the selected report and sources. Evaluator expectations and independent review notes remain outside the source corpus. Formal checks concern the supplied facts and declared reading conventions, not document authenticity, literary quality or actual reader psychology.
