import Audit
#check @Audit.approvalConflict
#print axioms Audit.approvalConflict
example : (Audit.mara.order = Audit.tomas.order ∧ Audit.mara.dateOffset = Audit.tomas.dateOffset ∧ Audit.mara.approvalMinute = Audit.tomas.approvalMinute ∧ Audit.mara.asserted ≠ Audit.tomas.asserted ∧ Audit.mara.retracted = false ∧ Audit.tomas.retracted = false) := Audit.approvalConflict
