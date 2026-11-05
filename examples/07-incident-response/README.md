# Did the team respond in time?

A service team reviews incidents across a clock change and planned maintenance. Check its response times and claims about what happened.

**Question:** Does the incident report calculate the right response and notification deadlines?

Upload a response playbook, incident and notification logs, maintenance permissions, monitoring coverage and scanned statements. Choose either [the careful report](report-correct.md) or [the report with deliberate errors](report.md) and audit it separately against all files in [sources/](sources/). Include `brief.md` for the supplied review conventions.

The audit can check time-zone conversion, approved pauses, delivered notifications and the applicable policy version. It reviews the supplied report, including its reasons and citations; it does not write the original report.

A monitoring gap cannot prove that a data transfer did or did not occur. Conflicting witness accounts must stay visible.

These are fictional examples. Keep this guide, the alternate report, metadata, generation files and evaluator material outside the audit input. Evaluator expectations are withheld during a blind audit; the selected report and source documents are always available.

Historical execution records are indexed under [validation/runs](../../validation/runs/). This guide does not constitute a new validation run. Original reports and sources retain their bytes so they can be matched to prior results. New runs belong under `tmp/audit-runs/`, with a separate directory for each report.
