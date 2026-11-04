import Audit
#check @Audit.bAcknowledgement
#print axioms Audit.bAcknowledgement
example : (Audit.startB = 200 ∧ Audit.acknowledgementB - Audit.startB = 25 ∧ Audit.timely Audit.startB Audit.acknowledgementB 30) := Audit.bAcknowledgement
