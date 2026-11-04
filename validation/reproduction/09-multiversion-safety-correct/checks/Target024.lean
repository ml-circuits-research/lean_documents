import Audit
#check @Audit.claim07
#print axioms Audit.claim07
example : (Audit.baseLimit 2 .cold 5 = some 150 ∧ Audit.c01.length = 3 ∧ Audit.within Audit.c01 150 = true) := Audit.claim07
