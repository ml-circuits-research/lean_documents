# Synthetic report-audit dossiers

Start with the [guided finding walkthrough](../docs/examples/start-here.html), then the [source-revision walkthrough](../docs/examples/revision-walkthrough.html) and [capability matrix](../docs/examples/capabilities.html). The [full catalog](../docs/examples/index.html) includes original sources, report variants, intermediate files, models, exact-target checks and actual logs.

There are sixteen synthetic dossiers, each with a correct and a deliberately mixed report. Dossier 15 also re-audits the same two reports after a source revision; an originally correct report can then become outdated. No real-document accuracy or source-authenticity claim is implied.

## Current learning examples

| Dossier | What to study |
| --- | --- |
| [13-portable-html](13-portable-html/README.md) | Start here: portable HTML extraction, independent conclusion and argument checks, exact arithmetic, countermodels and reusable Lean modules. |
| [15-native-revision](15-native-revision/README.md) | Current-contract native DOCX/PDF/OCR audit, followed by a source correction, stale-result rejection, dependency review and revised verdicts. |
| [16-intervals-and-rounding](16-intervals-and-rounding/README.md) | Overlapping and touching SLA pauses, exact deadline boundaries and half-cent rounding, with scoped invoice and historical-evidence claims. |
| [14-agent-native](14-agent-native/README.md) | The same evidence obligations with Lean and agent tools alone: supported conclusions, false argument premises and formal underdetermination, without Python audit gates. |
| [11-report-derived-criteria](11-report-derived-criteria/README.md) | Report-derived criteria without a separate brief: arithmetic, bounded exceptions, citation fidelity, conclusion versus argument, dependencies, conflicts, and population scope. |
| [12-empty-evidence](12-empty-evidence/README.md) | An actually empty source file: distinguish a verified observation about zero bytes from unsupported clearance claims, without fabricated quotations or closed-world assumptions. |

## Historical domain examples

These first ten dossiers retain twenty legacy v1 audit bundles. Their actual proofs are useful historical evidence; publication or rechecking does not grant them the current v2 registration and argument guarantees.

| Dossier | Primary challenge |
| --- | --- |
| [01-procedural-approval](01-procedural-approval/README.md) | Approval timing, alternative emergency authorization, explicit negative records, an incomplete handoff, and conflicting attestations. |
| [02-versioned-deadlines](02-versioned-deadlines/README.md) | Version applicability, amendments, leap-day arithmetic, inclusive and exclusive deadlines, misleading labels, and a missing annex. |
| [03-audit-arithmetic](03-audit-arithmetic/README.md) | Integer arithmetic, denominators, budget balances, evidentiary completeness, and the difference between missing support and false conclusions. |
| [04-narrative-continuity](04-narrative-continuity/README.md) | Narrative chronology, flashbacks, identity and causal continuity, competing testimony, and claims beyond a finite fictional world. |
| [05-conflicting-evidence](05-conflicting-evidence/README.md) | Release authorization across conflicting attestations, source authority, inventory omissions, and a supplied verification excerpt. |
| [06-procurement-contract](06-procurement-contract/README.md) | Procurement rules and amendments across DOCX, searchable PDF, scanned attestations, purchase records, delegated authority, and exceptions. |
| [07-incident-response](07-incident-response/README.md) | Incident-response timing, maintenance authorization, notifications, monitoring coverage, and conflicting scanned containment attestations. |
| [08-scanned-inventory](08-scanned-inventory/README.md) | Inventory reconciliation and custody with a five-page image-only shipping PDF; a pale numeral and unsigned quantity remain distinct uncertainty problems. |
| [09-multiversion-safety](09-multiversion-safety/README.md) | Multiple native DOCX specifications and exception tables, PDF test runs, units, applicability, calibration authority, and unresolved faults. |
| [10-distributed-assurance](10-distributed-assurance/README.md) | Sixty operational records plus cross-document identity, delegated authority, rule transitions, board exceptions, and differently bounded completeness claims. |

## Inputs, independence and execution

Give the auditor all files in the selected dossier’s `sources/`, exactly one report, and a brief only if supplied. Reports are `report.md` / `report-correct.md`, except dossiers 13/14 use `report-mixed.md` for their mixed variant. Dossiers 11–16 deliberately omit a brief. In dossier 15, keep `revisions/` outside the initial corpus; use it only for the explicit later-source run.

Do not include the alternate report, README, fixture builders, authoring masters or evaluator outcomes as source evidence. The original selected report is always available to its auditor. Evaluator-only material, where present, is withheld from blind auditors.

Dossiers 13–16 are explicitly nonblind demonstrations: fixture authors execute audits and a separate coordinator reconstructs outcomes from sources and reviews model correspondence. Existing mixed runs 13/14 were reused only after original report/source hash identity was checked; their correct companions were actually audited separately. See the coverage matrix for current helper audits, agent-native checks, legacy records and implementation-only tests.

Working runs stay in Git-ignored `tmp/`. Byte-preserving study copies under `docs/examples/` are intended for GitHub and regenerate without temporary workspaces. Read each run’s independent review and assurance mode; the agent-native route does not claim a Python validator executed.
