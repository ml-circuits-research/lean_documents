# Portable HTML stock dossier

Teaching purpose: audit a report with no separate brief, import an unsupported HTML source using original coordinates and actual inspection, distinguish counted stock from all recorded stock, audit false argument premises separately from true conclusions, and preserve historical uncertainty. The copied self-contained skill uses real Lean.

## Exact inputs

- [Source HTML](sources/stock.html): the sole source, preserved byte for byte from the earlier portability input.
- [Correct report](report-correct.md): the existing companion report, preserved byte for byte.
- [Mixed report with deliberate errors](report-mixed.md): the original selected portability report, preserved byte for byte.
- No review brief is supplied. Criteria come from the selected report and source rules.

Select exactly one report and the source. The alternate report, this README, [companion note](companion-note.md), provenance and outcome records are teaching metadata, not audit evidence. The correct report's old “future comparison” note describes the earlier audit and is intentionally retained unchanged.

## Executed audits and provenance

[Exact hashes and input-to-run mapping](provenance.json) distinguish reuse from new work. The mixed report reuses the already executed v2 audit in [the published raw bundle](../../docs/flexibility-data/portable-audit/raw/audit-report.md); its report/source originals have identical SHA-256 values to this dossier. It was not rerun. The existing source-first/model review had fixture-design familiarity and is not a blind benchmark.

The correct report was actually audited in [tmp/paired-current-g17n2r00/claim-audit-76p4zp3_](../../tmp/paired-current-g17n2r00/claim-audit-76p4zp3_/audit-report.md), using a fresh copy of the current skill under [tmp/paired-current-g17n2r00/skill](../../tmp/paired-current-g17n2r00/skill/SKILL.md). HTML initially remained blocked by the built-in adapter; a fresh import extracted all nine text segments, then all material quotes were compared to the actual original 14-line HTML. The source review records do not claim browser rendering. Original report bracket labels R1–R4 remain unchanged; extraction assigns actual anchors P03–P06. Seven atomic conclusions were registered.

The helper v2 gate and Lean 4.24.0 passed 17 declaration/target checks (six exact report targets). All seven conclusions are supported; six have direct formal targets and the no-records statement is documentary only. The report does not explicitly derive C2/C6, so their argument support gaps remain visible. Only `propext` occurs in the checked dependency set.

[Exported correct audit](../../tmp/paired-current-g17n2r00/portable-correct-export-final/audit-report.md) retains original bytes, extraction attempts, registrations, models, actual proof logs and self-review. [Machine-readable results](../../tmp/paired-current-g17n2r00/example-13-results.json) list both variants and their outcomes. Initial fixture-familiar self-review was followed by a separate coordinator source-first reconstruction and final model review. The C3 whole-report-context correction was incorporated before the final helper check and export. Both reviewers knew the fixture purpose; this is nonblind review. No evaluator-only expected outcomes were read.
