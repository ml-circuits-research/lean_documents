import Audit
#check @Audit.claim13
#print axioms Audit.claim13
example : (Audit.aRaw = -30 ∧ Audit.aDetection = 0 ∧ Audit.revision Audit.aDetection = 2 ∧ Audit.revision Audit.aDetection ≠ 1) := Audit.claim13
