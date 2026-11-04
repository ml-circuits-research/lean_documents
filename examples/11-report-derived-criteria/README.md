# 11: report-derived review criteria

This entirely synthetic dossier exercises an audit of a supplied report against cross-document evidence without a separate review brief. Internal policy DP-7, all names, records, amounts, and dates are invented. The substantive reports already exist; the auditor's task is to audit their findings and arguments, not to generate the original report.

For each independent audit, supply exactly one of `report.md` and `report-correct.md` together with the five files in `sources/`. Both reports contain twelve numbered findings. Derive verification questions from every finding, including qualifications, source-attribution statements, and supplied arguments. The alternate report is not evidence. No `brief.md` exists or is required. Source documents carry their own applicable rules, dates, units, and scope.

`report.md` is the deliberately mixed report; `report-correct.md` is the cautious alternative. The examples combine arithmetic, a bounded temporal exception, citation fidelity, independent evaluation of a conclusion and its stated argument, missing evidence, an undefined qualitative criterion, chained eligibility dependencies, conflicting sources, and cohort-versus-population scope.

**Blind-review boundary:** do not give a blind auditor this README, the alternate report, or anything under `evaluator/`. Stage only the selected report and `sources/` into a distinct retained directory under repository `tmp/`. Evaluator-only design expectations are in `evaluator/expected-outcomes.md`; they are not source evidence and must remain withheld throughout blind review.

All numbers and policy predicates are finite and suitable for small Lean checks. A Lean proof over extracted facts establishes only the modeled proposition under its stated assumptions; it does not authenticate the records or resolve conflicting real-world evidence. Textual support gaps and undefined criteria remain valuable findings without being recast as proofs that the underlying substantive assertion is false.

This dossier contains authored source and report fixtures plus design expectations. It does not itself contain executed audits, Lean proofs, proof logs, or validation results. Validation must be performed separately for each variant, with actual logs preserved in its run directory.
