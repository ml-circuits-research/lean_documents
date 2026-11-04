# Agent-native spending dossier

Teaching purpose: execute the same evidence/argument obligations with a coding agent and core Lean alone, without a Python audit gate. Separate a supported conclusion from a false general premise, refute an actual wrong conclusion, and demonstrate approval uncertainty using two compatible worlds. Shared evidence-logic definitions are optional; the new correct run uses only small task-specific definitions.

## Exact inputs

- [Source spending record](sources/source.md): the sole source.
- [Correct report](report-correct.md): preserved existing correct companion.
- [Mixed report with deliberate errors](report-mixed.md): preserved earlier selected report.
- No separate brief is supplied; infer criteria from report findings and S1–S3.

All three inputs retain their original bytes from `tmp/agent-native-audit-AwYPQy`. Select one report and the source only. This README, the alternate report, [companion note](companion-note.md), provenance and results are metadata, not evidence. The correct report's historical “not the selected audit input” title refers to the earlier mixed run and remains unchanged.

## Executed audits and provenance

[Hash mapping](provenance.json) verifies exact source/report identity for reuse. The mixed audit at [its retained original run](../../tmp/agent-native-audit-AwYPQy/audit-report.md) already compiled five exact targets using Lean 4.24.0 and received a separately recorded source-first review and replay. Its results are reused, not rerun. The original narrative claim/argument mapping is agent-native assurance, not a helper-v2 validation certificate.

The correct report was actually audited in [tmp/paired-current-g17n2r00/agent-native-correct](../../tmp/paired-current-g17n2r00/agent-native-correct/audit-report.md). Two conclusions were registered in a v2-equivalent agent-reviewed mapping. Three exact Lean target assertions and axiom checks passed with exit 0 and no axiom dependencies. The initial failed elaboration is retained in `attempts/0001`; only the corrected final output is a proof.

Both correct conclusions are supported: 9 is at most 10, and the supplied record admits both approval states. The second is an epistemic limitation, not a claim that approval did not occur. It has no report derivation and retains an argument support-gap observation.

The run retains original inputs, hashes, ledgers, findings, criteria, methods, source-to-model notes, exact targets and actual Lean logs. Python was used only for serialization of authored records; no Python audit validator, proof gate or Lake build was executed. [Execution record](../../tmp/paired-current-g17n2r00/agent-native-correct/run.json) and [machine-readable results](../../tmp/paired-current-g17n2r00/example-14-results.json) disclose executed versus agent-reviewed checks. Initial fixture-familiar self-review was followed by separate coordinator source-first/model review and an actual independent Lean replay (exit 0, three exact targets, no axioms). Both reviewers knew the fixture purpose; this is nonblind review. No evaluator-only expected outcomes were read.

The final [agent-native archive](../../tmp/paired-current-g17n2r00/agent-native-correct-bundle/audit-report.md) retains the final notes, both successful Lean logs, independent review, and the failed first attempt. Its SHA-256 bundle manifest is an archive inventory, not a Python audit-gate certificate.
