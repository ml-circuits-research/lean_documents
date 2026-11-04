import Audit
#check @Audit.aRevision
#print axioms Audit.aRevision
example : (Audit.revision Audit.detectionA = 2 ∧ Audit.warningA < 0 ∧ Audit.detectionA = 0) := Audit.aRevision
