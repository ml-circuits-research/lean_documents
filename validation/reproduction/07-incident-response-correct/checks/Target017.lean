import Audit
#check @Audit.qualifyingDetection
#print axioms Audit.qualifyingDetection
example : (Audit.warningA = -30 ∧ Audit.detectionA = 0 ∧ Audit.warningA < Audit.detectionA) := Audit.qualifyingDetection
