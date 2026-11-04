import Audit
#check @Audit.cConflict
#print axioms Audit.cConflict
example : (Audit.elise.incident = Audit.pavel.incident ∧ Audit.elise.minute = Audit.pavel.minute ∧ Audit.elise.fullyIsolated ≠ Audit.pavel.fullyIsolated ∧ Audit.elise.retracted = false ∧ Audit.pavel.retracted = false) := Audit.cConflict
