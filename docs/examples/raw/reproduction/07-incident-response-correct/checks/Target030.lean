import Audit
#check @Audit.cRevision
#print axioms Audit.cRevision
example : (Audit.detectionC = -10 ∧ Audit.revision Audit.detectionC = 1) := Audit.cRevision
