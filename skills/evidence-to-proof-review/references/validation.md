# Reproduction and evaluation

Use fresh retained workspaces under the repository's Git-ignored `tmp/` directory, one directory per audit or reproduction. Do not automatically delete them. A supplied report is always visible to its auditor. The expected answers, alternate report, prior audit results, and editorial fixture reviews are excluded from an initial blind audit. Shared filesystem access is not a security boundary: record the reviewer instructions and the resulting independence limit.

Prepare one run per report variant using the same source corpus. Ask a fresh agent to apply this skill using only the selected report, sources and brief only if supplied. It must produce the claim register, complete arguments, source mappings, and honest formal statuses. Run the technical helper, independently review meaning, reconcile differences, and only then compare the auditor's semantic outcomes with evaluator expectations. Correct the expectations if evidence establishes an error; preserve the comparison history.

On a curated suite with both correct and deliberately flawed supplied reports, measure claim coverage, semantic agreement, false refutations, false formal certainty, identification of insufficient support, quote integrity, and reproducibility separately. Expected `proof` is only a prospective formalization suggestion, not a requirement to force every documentary observation into Lean.

Negative checks must reject changed inputs, missing targets, misquoted evidence, incomplete proofs, custom axioms, and unsupported formal-success labels. An invalid report claim and an invalid proof artifact are different failures.

To reproduce an exported run, copy it to a new temporary directory and rerun `audit.py check` with the pinned Lean executable, then render. Keep original logs separate from reproduction logs. No evaluator file is needed to reproduce Lean proofs. External checker unavailable means unavailable, never passed.

For many documents, use disk-backed manifests and sequential or bounded parallel batches; explicitly record unprocessed inputs and their effect on coverage. Default proof execution budget is the helper's configured timeout; adjust deliberately and record the change. Do not claim unlimited computation or exhaustive semantic completeness.
