# Synthetic procedural approval dossier

This entirely synthetic dossier concerns fictional Cedar Operations. It is an audit fixture, not a statement about a real organization or legal compliance. All people, identifiers, policies, and records are invented.

Inputs are `brief.md`, one selected report (`report.md` or `report-correct.md`), and every Markdown file in `sources/`. `manifest.json` records SHA-256 hashes of those exact UTF-8 files. Paragraph anchors and claim identifiers are stable identifiers. File order carries no evidentiary precedence.

The question is whether a report accurately describes the supplied approval procedure and five recorded operations. The material includes a closed register with explicit negative entries, an explicitly incomplete external handoff, and unresolved conflicting attestations. Expected targets are intentionally outside this dossier, under `examples/evaluator/`; they are not inputs to a blind audit. No Lean proof, refutation, or runtime result is supplied or asserted.

Run two independent audits over the same source corpus: the mixed/erroneous `report.md` and the cautious `report-correct.md`. Both are supplied audit inputs, not requested generated outputs. The selected report must always be visible to the auditor. Only evaluator expectations are withheld for a blind audit. The manifest includes both variants; select exactly one per run.
