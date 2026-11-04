# Synthetic versioned deadlines dossier

All entities, workflow rules, dates, and records in this dossier are invented for audit preparation. The fixture is not legal or contractual advice.

The audit inputs are `brief.md`, one selected report (`report.md` or `report-correct.md`), and the four source Markdown files in `sources/`; `manifest.json` binds their bytes by SHA-256. Stable anchors identify paragraphs and claims. Read both rule versions and the amendment: later processing does not necessarily imply applicability of the later rule.

The dossier exercises a version boundary, leap-day calendar arithmetic, exclusive versus inclusive endpoints, a misleading system label, and a missing annex. Separate evaluator files outside this directory contain editorial targets and must not be supplied to a blind auditor. No Lean workflow has been run or verified for this dossier.

Run two independent audits over the same source corpus: the mixed/erroneous `report.md` and the cautious `report-correct.md`. Both are supplied audit inputs, not requested generated outputs. The selected report must always be visible to the auditor. Only evaluator expectations are withheld for a blind audit. The manifest includes both variants; select exactly one per run.
