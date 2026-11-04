import Audit
#check @Audit.commanderLate
#print axioms Audit.commanderLate
example : (¬ Audit.timely Audit.detectionA Audit.commanderDelivered 20 ∧ Audit.commanderDelivered - (Audit.detectionA + 20) = 2) := Audit.commanderLate
