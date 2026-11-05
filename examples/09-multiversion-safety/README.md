# Did the equipment pass its tests?

An equipment reviewer compares laboratory tests with changing acceptance limits. Check whether each test uses the right rule and any applicable exception.

**Question:** Does the report support each test result and release claim?

Upload DOCX specifications and an exception, PDF test results, calibration records and release requirements. Choose either [the careful report](report-correct.md) or [the report with deliberate errors](report.md) and audit it separately against all files in [sources/](sources/). Include `brief.md` for the supplied review conventions.

The audit can check limits for each test date and temperature, repeated measurements, calibration validity and release approval. It reviews the supplied report, including its reasons and citations; it does not write the original report.

Passing one measured test does not establish that the entire device is safe. Missing measurements and unsupported operating conditions remain limits.

These are fictional examples. Keep this guide, the alternate report, metadata, generation files and evaluator material outside the audit input. Evaluator expectations are withheld during a blind audit; the selected report and source documents are always available.

Historical execution records are indexed under [validation/runs](../../validation/runs/). This guide does not constitute a new validation run. Original reports and sources retain their bytes so they can be matched to prior results. New runs belong under `tmp/audit-runs/`, with a separate directory for each report.
