import Audit
#check @Audit.claim12
#print axioms Audit.claim12
example : (Audit.Lot.A ∈ Audit.completeMovementLots ∧ Audit.Lot.B ∈ Audit.completeMovementLots ∧ Audit.Lot.D ∉ Audit.completeMovementLots) := Audit.claim12
