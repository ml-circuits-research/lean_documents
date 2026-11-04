# Campaign dispatch review

This report presents findings for the four-dispatch cohort at the end of campaign day 20, except where a finding expressly names a different period or population. Its findings themselves identify the questions to review; no separate review brief accompanies it.

**F11-OK-01 — Cohort expenditure.** The total amount of the reviewed cohort is 50000 euro cents. Argument: 12000 + 18000 + 9000 + 11000 = 50000. Citation: dispatch-ledger.md L-02.

**F11-OK-02 — Budget headroom.** The cohort budget balance is 5000 euro cents. Argument: 55000 − 50000 = 5000 under the stated balance definition. Citations: dispatch-ledger.md L-01–L-02; dispatch-policy.md P-05.

**F11-OK-03 — Approval of B.** B has compliant approval at cutoff under the temporary exception. Argument: route R2, release day 12 within days 10–14, declaration day 11 one day before release, and approval day 15 exactly three days after release satisfy every exception condition. Citations: dispatch-ledger.md L-02; dispatch-policy.md P-03.

**F11-OK-04 — Approval of C.** C has noncompliant approval at cutoff. Argument: approval day 16 is later than release day 12, so the ordinary route fails; it is four days after release, so the exception also fails. These are the only approval routes. Citations: dispatch-ledger.md L-02; dispatch-policy.md P-02–P-03.

**F11-OK-05 — Settlement eligibility of B.** B is eligible for settlement at cutoff. Argument: the temporary exception establishes compliant approval; the ledger records checksum PASS; and its destination South belongs to DL-7. These jointly satisfy P-04. Citations: dispatch-policy.md P-03–P-04; dispatch-ledger.md L-02; destination-list.md D-01.

**F11-OK-06 — What the ledger attests.** Ledger paragraph L-03 restricts the meaning of checksum PASS to package integrity. Citation: dispatch-ledger.md L-03.

**F11-OK-07 — Later reliability.** The supplied packet cannot establish whether B had zero reliability incidents during days 21–50. Argument: the reliability annex is not supplied and there are no observations for that period; this is an evidence limitation, not a finding that an incident occurred. Citations: packet-register.md K-01–K-02.

**F11-OK-08 — Overall rating.** The supplied packet provides no definition or rating rule for “operationally robust.” Citations: dispatch-policy.md P-06; packet-register.md K-03.

**F11-OK-09 — Delivery acceptance.** The supplied records conflict about B's acceptance at the end of day 12. Argument: R-01 records acceptance and R-02 denies it for the same event and instant; R-03 supplies no resolution. Citations: delivery-records.md R-01–R-03.

**F11-OK-10 — Exception window.** Release on day 15 is outside the temporary exception's release window. Argument: the latest permitted release day is 14. Citation: dispatch-policy.md P-03.

**F11-OK-11 — Eligible settlement amount.** The reviewed cohort's eligible settlement amount is 30000 euro cents. Argument: A has prior approval, PASS checksum, and listed destination North; B satisfies all three conditions as shown in the cited records; C fails approval timing; D's destination East is not listed. Therefore the eligible cohort members are exactly A and B, with amounts 12000 + 18000 = 30000. Citations: dispatch-policy.md P-02–P-05; dispatch-ledger.md L-02; destination-list.md D-01.

**F11-OK-12 — Population expenditure.** The supplied four-row ledger does not establish the total amount of all 40 campaign dispatches. Argument: the snapshot covers four named dispatches and supplies no amounts for the remaining 36. Citations: dispatch-ledger.md L-01–L-02; packet-register.md K-03.
