# Do the charges and receipt agree?

A laboratory transfer has a charge ledger, receipt scan and approval policy. Check the report, then see which claims need a fresh review if the ledger changes.

**Question:** Are the reported charges, arrival time and approval claims supported by the original documents?

Upload the DOCX policy, original PDF ledger and scanned PDF receipt in sources/, plus one report. Choose either [the careful report](report-correct.md) or [the report with deliberate errors](report.md) and audit it separately against all files in [sources/](sources/). No separate brief is needed; derive the questions from the report and source rules.

The audit can check charge totals and caps, physical arrival deadlines and the evidence for release approval. It reviews the supplied report, including its reasons and citations; it does not write the original report.

The replacement ledger in revisions/ is a separate follow-up input. Existing audit conclusions cannot be reused unchanged after a source revision; OCR needs checking against the scan.

These are fictional examples. Keep this guide, the alternate report, metadata, generation files and evaluator material outside the audit input. Evaluator expectations are withheld during a blind audit; the selected report and source documents are always available.

Historical execution records are indexed under [validation/runs](../../validation/runs/). This guide does not constitute a new validation run. Original reports and sources retain their bytes so they can be matched to prior results. New runs belong under `tmp/audit-runs/`, with a separate directory for each report.
