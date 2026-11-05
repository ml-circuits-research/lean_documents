# Try an example

Open the local review interface at **http://127.0.0.1:8787** and choose a scenario. Each example supplies a report to check and the documents that support or challenge it. The result is an audit of the report’s claims, reasons and citations.

Start with the shopping receipt, deposit, parcel or electricity examples (17–20) for familiar three-claim exercises. These newly prepared inputs require fresh executed validation. The expense, payment totals and small stock-register examples are also short. The larger purchasing, incident and equipment examples include more documents and exceptions.

| Example | Question |
| --- | --- |
| [01. Was the work approved?](01-procedural-approval/README.md) | Did each operation have the approval required when it started? |
| [02. Was the submission on time?](02-versioned-deadlines/README.md) | Does the report use the right deadline for each application? |
| [03. Do the payment totals add up?](03-audit-arithmetic/README.md) | Are the totals and approval claims supported by the four payment records? |
| [04. Does the story timeline make sense?](04-narrative-continuity/README.md) | Does the review place each scene and character correctly in time? |
| [05. Is the software ready to release?](05-conflicting-evidence/README.md) | Does the report have enough evidence for its release-readiness claims? |
| [06. Were the purchases properly approved?](06-procurement-contract/README.md) | Does the purchasing review apply the right amounts, authority and exceptions? |
| [07. Did the team respond in time?](07-incident-response/README.md) | Does the incident report calculate the right response and notification deadlines? |
| [08. How much stock is available?](08-scanned-inventory/README.md) | Do the reported stock and delivery quantities agree with the records? |
| [09. Did the equipment pass its tests?](09-multiversion-safety/README.md) | Does the report support each test result and release claim? |
| [10. Did every site have permission?](10-distributed-assurance/README.md) | Can the report justify its permission claims for the recorded releases? |
| [11. Which deliveries can be paid?](11-report-derived-criteria/README.md) | Does the report correctly identify the costs and dispatches eligible for settlement? |
| [12. What can an empty file tell us?](12-empty-evidence/README.md) | Can either clearance outcome be established from an empty source file? |
| [13. Which stock should be counted?](13-portable-html/README.md) | Does the report count the right rows and apply the release rule correctly? |
| [14. Is this expense within budget?](14-agent-native/README.md) | Does the recorded expense fit the budget, and what is known about approval? |
| [15. Do the charges and receipt agree?](15-native-revision/README.md) | Are the reported charges, arrival time and approval claims supported by the original documents? |
| [16. Is the service bill calculated correctly?](16-intervals-and-rounding/README.md) | Does the report count paused time once and round each charge under the stated rule? |

| [17. Does the shopping receipt add up?](17-shopping-receipt/README.md) | Does the receipt support the reported total, change and payment status? |
| [18. Is the deposit refund calculated correctly?](18-rental-deposit/README.md) | Does the calculation establish the refund amount, deadline and actual payment? |
| [19. Did the parcel arrive on time?](19-parcel-delivery/README.md) | Does the summary correctly describe delivery timing and the condition of the contents? |
| [20. Is the electricity bill correct?](20-household-electricity/README.md) | Do the readings and tariff support the usage, charge and payment claims? |

Each scenario has a careful report and a report with deliberate errors. Audit them in separate runs using the same original sources. Missing evidence can be a useful finding without proving that a claim is false. A supported conclusion can still have an unsupported argument.

All scenarios are fictional. Supply only the selected report, its `sources/` directory (including nested files), and an optional `brief.md`. Keep evaluator expectations, the alternate report and historical results out of blind audit inputs. The `example.json` files provide the interface titles, descriptions and input paths.

Historical run artifacts have one entry point: [validation/runs](../validation/runs/). Consult their actual proof logs and review notes for executed checks, review independence and legacy-format limitations. A scenario description or a report labeled careful is not itself proof of validation.

New audit and reproduction runs go in distinct directories beneath `tmp/audit-runs/`. Retain each run’s inputs, evidence, findings and actual proof logs so its conclusions can be inspected.
