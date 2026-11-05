# How much stock is available?

A warehouse reconciles deliveries, returns, reservations and signed counts. Check whether its stock report uses the right quantities and units.

**Question:** Do the reported stock and delivery quantities agree with the records?

Upload stock rules, movement journals, count sheets, receiving messages and scanned shipping tickets. Choose either [the careful report](report-correct.md) or [the report with deliberate errors](report.md) and audit it separately against all files in [sources/](sources/). Include `brief.md` for the supplied review conventions.

The audit can check crate-to-unit conversions, stock balances, reserved or quarantined goods and accepted delivery quantities. It reviews the supplied report, including its reasons and citations; it does not write the original report.

Faint scans and conflicting counts can leave quantities unresolved. Proposed corrections must not silently replace the original record.

These are fictional examples. Keep this guide, the alternate report, metadata, generation files and evaluator material outside the audit input. Evaluator expectations are withheld during a blind audit; the selected report and source documents are always available.

Historical execution records are indexed under [validation/runs](../../validation/runs/). This guide does not constitute a new validation run. Original reports and sources retain their bytes so they can be matched to prior results. New runs belong under `tmp/audit-runs/`, with a separate directory for each report.
