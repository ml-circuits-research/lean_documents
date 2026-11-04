import Audit
#check @Audit.recordConflict
#print axioms Audit.recordConflict
example : (Audit.saysAccepted Audit.Record.receiving = true ∧ Audit.saysAccepted Audit.Record.incident = false) := Audit.recordConflict
