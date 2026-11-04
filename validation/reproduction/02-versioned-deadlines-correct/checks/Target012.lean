import Audit
#check @Audit.claim04
#print axioms Audit.claim04
example : (Audit.d203.received = Audit.boundary ∧ Audit.revision Audit.d203 = .two ∧ Audit.standardDeadline Audit.d203 = some 25500 ∧ Audit.d203.submitted = 25500 ∧ Audit.d203.submitted ≤ 25500) := Audit.claim04
