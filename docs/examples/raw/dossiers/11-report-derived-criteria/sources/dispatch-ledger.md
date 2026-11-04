# Dispatch ledger snapshot L-7

[L-01] The campaign population contains 40 dispatches. The reviewed cohort consists of exactly A, B, C, and D. Only these four dispatches are included in this snapshot. The cohort comparison budget is 55000 euro cents. The snapshot was signed at the end of day 20.

[L-02] The following fields are complete and final through the cutoff for the reviewed cohort. “None” means that no declaration existed through that cutoff. Approval day is the only approval event for each listed dispatch. All four dispatches actually occurred.

| Dispatch | Amount (euro cents) | Route | Release day | Emergency declaration day | Approval day | Checksum | Destination |
| --- | ---: | --- | ---: | --- | ---: | --- | --- |
| A | 12000 | R1 | 5 | None | 4 | PASS | North |
| B | 18000 | R2 | 12 | 11 | 15 | PASS | South |
| C | 9000 | R2 | 12 | 11 | 16 | PASS | North |
| D | 11000 | R1 | 15 | None | 14 | PASS | East |

[L-03] Checksum PASS means that the byte checksum of the dispatched package matched the approved package checksum. This field describes package integrity only. It does not attest to approval timing, delivery acceptance, future reliability, or eligibility for settlement.
