import Audit
#check @Audit.claim05
#print axioms Audit.claim05
example : (¬ (Audit.activeA ≤ 90) ∧ Audit.activeA - 90 = 5) := Audit.claim05
