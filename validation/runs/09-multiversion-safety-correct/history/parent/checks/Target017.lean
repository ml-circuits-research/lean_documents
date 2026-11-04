import Audit
#check @Audit.claim01Arithmetic
#print axioms Audit.claim01Arithmetic
example : (Audit.l01.length = 3 ∧ Audit.within Audit.l01 120 = true ∧ Audit.maximum Audit.l01 = 118 ∧ Audit.maximum Audit.l01 < 120 ∧ 120 - Audit.maximum Audit.l01 = 2) := Audit.claim01Arithmetic
