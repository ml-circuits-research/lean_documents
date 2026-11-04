import Audit
#check @Audit.settlement
#print axioms Audit.settlement
example : (Audit.eligibleTotal = 30000 ∧ Audit.eligibleTotal ≠ 39000) := Audit.settlement
