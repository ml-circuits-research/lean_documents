# Claim coverage

## Registered claim coverage

Coverage: **complete_registration**; 5 reviewed anchors; 4 audited and 0 deferred claims.

Registration reconciles declared claims and reviewed report anchors; it does not establish semantic completeness, faithful decomposition, or that declared searches were actually performed.

- `R1`: claims — One principal atomic conclusion is registered; its material premises and inference are separately covered in argument_audit.report_items.
- `R2`: claims — One principal atomic conclusion is registered; its material premises and inference are separately covered in argument_audit.report_items.
- `R3`: claims — One principal atomic conclusion is registered; its material premises and inference are separately covered in argument_audit.report_items.
- `R4`: claims — One principal atomic conclusion is registered; its material premises and inference are separately covered in argument_audit.report_items.
- `document-preamble`: non_claim — The title identifies the report and makes no substantive stock or historical assertion.

## Document extraction coverage

| Document | Source | State |
|---|---|---|
| D00001 | input/report.md | ready |
| D00002 | input/sources/stock.html.md | ready |

## Claim outcomes

| Claim | Semantic state | Argument status | Formal status |
|---|---|---|---|
| C1 | supported | sufficient | proved |
| C2 | refuted | unsound_argument | refuted |
| C3 | supported | unsound_argument | proved |
| C4 | undetermined | invalid_inference | auxiliary |

Coverage enumerates submitted findings; it does not establish that every report claim was identified.
