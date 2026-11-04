# Internal dispatch policy DP-7

[P-01] This is an invented internal policy for a synthetic exercise. It makes no assertion about external law or industry standards. Days are integer indices in the campaign calendar, not business days. All comparisons are inclusive unless expressly stated otherwise. Amounts are integer euro cents. The review cutoff is the end of campaign day 20.

[P-02] Ordinarily, a dispatch has compliant approval if its approval day is strictly earlier than its release day. An approval on the release day does not satisfy the ordinary route.

[P-03] A dispatch also has compliant approval under the temporary exception if **all** of these conditions hold: its route is R2; its release day is between day 10 and day 14 inclusive; an emergency declaration exists on or before release; release is no more than two days after that declaration; and approval is on or after release but no more than three days after release. Either the ordinary route or this exception is sufficient for compliant approval. No other approval route applies to the reviewed cohort.

[P-04] A dispatch is eligible for settlement if and only if it has compliant approval under P-02 or P-03, its recorded checksum result is PASS, and its destination appears in the supplied destination list DL-7. These are three separate necessary conditions; together they are sufficient. Delivery acceptance is not a settlement condition.

[P-05] A budget balance means the comparison budget less the sum of dispatch amounts for the stated cohort. Eligible settlement amount means the sum of amounts for the cohort members satisfying P-04. Neither amount includes dispatches outside the stated cohort.

[P-06] DP-7 does not define a rating called “operationally robust” or a rule that checksum success implies compliant approval. No other rating standard is incorporated by reference.
