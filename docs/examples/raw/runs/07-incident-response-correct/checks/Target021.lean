import Audit
#check @Audit.containmentLate
#print axioms Audit.containmentLate
example : (90 < Audit.activeA ∧ Audit.activeA - 90 = 5 ∧ Audit.timely Audit.detectionA Audit.acknowledgementA 15) := Audit.containmentLate
