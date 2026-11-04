import Audit
#check @Audit.technicalLate
#print axioms Audit.technicalLate
example : (Audit.technicalQueued = 8 ∧ Audit.technicalDelivered = 11 ∧ ¬ Audit.timely Audit.detectionA Audit.technicalDelivered 10 ∧ Audit.technicalDelivered - (Audit.detectionA + 10) = 1) := Audit.technicalLate
