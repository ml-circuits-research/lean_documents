import Audit
#check @Audit.claim06
#print axioms Audit.claim06
example : (Audit.d204.kind = .restricted ∧ Audit.revision Audit.d204 = .two ∧ Audit.standardDeadline Audit.d204 = none) := Audit.claim06
