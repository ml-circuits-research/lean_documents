import Audit
#check @Audit.bRawVersusEffective
#print axioms Audit.bRawVersusEffective
example : (Audit.acknowledgementB - Audit.detectionB = 35 ∧ Audit.acknowledgementB - Audit.startB = 25 ∧ Audit.timely Audit.startB Audit.acknowledgementB 30) := Audit.bRawVersusEffective
