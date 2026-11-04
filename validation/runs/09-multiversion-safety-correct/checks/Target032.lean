import Audit
#check @Audit.claim14
#print axioms Audit.claim14
example : (∀ temp, Audit.baseLimit 1 .hot temp = none ∧ Audit.baseLimit 2 .hot temp = none) := Audit.claim14
