import Audit
#check @Audit.acknowledgementTimely
#print axioms Audit.acknowledgementTimely
example : (Audit.acknowledgementA - Audit.detectionA = 12 ∧ Audit.timely Audit.detectionA Audit.acknowledgementA 15) := Audit.acknowledgementTimely
