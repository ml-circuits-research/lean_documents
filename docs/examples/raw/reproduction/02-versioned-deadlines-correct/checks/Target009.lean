import Audit
#check @Audit.claim01
#print axioms Audit.claim01
example : (Audit.revision Audit.d201 = .one ∧ Audit.standardDeadline Audit.d201 = some 15420 ∧ Audit.d201.submitted = 15420 ∧ Audit.d201.submitted ≤ 15420) := Audit.claim01
