import Audit
#check @Audit.claim09
#print axioms Audit.claim09
example : (Audit.elinCount.lot = Audit.reedCount.lot ∧ Audit.elinCount.scope = Audit.reedCount.scope ∧ Audit.elinCount.cutoff = Audit.reedCount.cutoff ∧ Audit.elinCount.issuer ≠ Audit.reedCount.issuer ∧ Audit.elinCount.amount = 148 ∧ Audit.reedCount.amount = 147 ∧ Audit.elinCount.amount ≠ Audit.reedCount.amount) := Audit.claim09
