import Audit
#check @Audit.claim05
#print axioms Audit.claim05
example : (Audit.dashboard Audit.d201 = .two ∧ Audit.dashboard Audit.d202 = .two ∧ Audit.dashboard Audit.d203 = .two ∧ Audit.dashboard Audit.d204 = .two ∧ Audit.dashboard Audit.d201 ≠ Audit.revision Audit.d201 ∧ Audit.dashboard Audit.d202 ≠ Audit.revision Audit.d202) := Audit.claim05
