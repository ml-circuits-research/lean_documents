import Audit
#check @Audit.claim03
#print axioms Audit.claim03
example : (Audit.standardDeadline Audit.d202 = some 28380 ∧ 28380 < Audit.d202.submitted) := Audit.claim03
