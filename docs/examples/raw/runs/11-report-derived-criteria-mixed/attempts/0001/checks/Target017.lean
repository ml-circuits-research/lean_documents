import Audit
#check @Audit.headroom
#print axioms Audit.headroom
example : (Audit.balance = 5000 ∧ Audit.balance ≠ 6000) := Audit.headroom
