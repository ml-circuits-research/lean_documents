import Audit
#check @Audit.claim08
#print axioms Audit.claim08
example : (Audit.requestedB = 18 ∧ Audit.deliveredB = 12 ∧ Audit.deliveredB < Audit.requestedB) := Audit.claim08
