# Synthetic audit dossiers

These twelve dossiers prepare validation of the skill that audits findings in supplied reports. They are synthetic examples, not real legal, audit, or literary assessments. Executed validation is stored separately under `validation/runs/`; these source dossiers remain test inputs, not proof outputs.

The first ten dossiers contain a brief, source documents and a fixture manifest. Dossiers 11 and 12 deliberately omit a brief; all runtime inputs receive hashed manifests. Each dossier supplies `report.md` with deliberate errors mixed with correct claims, and `report-correct.md` with carefully scoped claims. Audit the two variants separately. A correct report may correctly acknowledge uncertainty; this is not a demand to prove unknown events.

| Dossier | Primary challenge |
| --- | --- |
| [01-procedural-approval](01-procedural-approval/README.md) | Prior approval, emergency exception, explicit absence versus unknown |
| [02-versioned-deadlines](02-versioned-deadlines/README.md) | Effective versions, calendar boundaries, missing annex |
| [03-audit-arithmetic](03-audit-arithmetic/README.md) | Exact arithmetic, sampling, misquotation, missing support |
| [04-narrative-continuity](04-narrative-continuity/README.md) | World rules, story time, fallible testimony, nonformal judgments |
| [05-conflicting-evidence](05-conflicting-evidence/README.md) | Conflicts, circular support, missing premises, untrusted instructions |

| [06-procurement-contract](06-procurement-contract/README.md) | Split purchases, exchange rates, rounding, delegation expiry, native DOCX/PDF and scanned attestations |
| [07-incident-response](07-incident-response/README.md) | Time zones, SLA pauses, maintenance exceptions, conflicting and missing incident records |
| [08-scanned-inventory](08-scanned-inventory/README.md) | Physical quantities, returns, cancelled movements, conflicting counts and faint scanned evidence |
| [09-multiversion-safety](09-multiversion-safety/README.md) | Versioned rules, table extraction, exceptions, test-group completeness and unsupported assurance |
| [10-distributed-assurance](10-distributed-assurance/README.md) | 67 source files, late exceptions, revoked authority, missing node evidence and global claims |

For each run, provide all sources, exactly one selected report, and the brief only when supplied. Do not provide the alternate report, fixture README, or evaluator expectations to the auditing agent. Manifest hashes identify packaged bytes; they do not establish authenticity.

The [evaluator register](evaluator/README.md) is separate. The current [independent fixture review](../docs/fixture-review.md) records the initial editorial validation; actual skill execution is recorded separately in validation/. See the [HTML implementation plan](../docs/implementation.html) for the approval boundary and validation stages.

| [11-report-derived-criteria](11-report-derived-criteria/README.md) | Infer criteria without a brief; verify citations and author arguments independently of conclusions |
| [12-empty-evidence](12-empty-evidence/README.md) | Zero-byte evidence, explicit support gaps, and formal non-entailment without fabricated quotations |

Explore the [published study catalog](../docs/examples/index.html), including raw snapshots, intermediate decisions, models and actual logs. See the [independent coverage review](../docs/general-validation.html) for tested cases and remaining limits.
