import Audit
#check @Audit.claim03
#print axioms Audit.claim03
example : (Audit.baseLimit 2 .normal 20 = some 100 ∧ Audit.n01.length = 3 ∧ Audit.within Audit.n01 100 = true) := Audit.claim03
