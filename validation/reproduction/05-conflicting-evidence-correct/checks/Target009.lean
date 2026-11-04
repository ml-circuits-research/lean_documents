import Audit
#check @Audit.testimonyConflict
#print axioms Audit.testimonyConflict
example : (Audit.qa.issuer ≠ Audit.ops.issuer ∧ Audit.qa.context = Audit.ops.context ∧ Audit.qa.enabled = true ∧ Audit.ops.enabled = false ∧ Audit.qa.enabled ≠ Audit.ops.enabled) := Audit.testimonyConflict
