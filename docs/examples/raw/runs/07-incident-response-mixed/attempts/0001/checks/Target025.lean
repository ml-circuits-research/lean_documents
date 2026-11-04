import Audit
#check @Audit.claim09
#print axioms Audit.claim09
example : (Audit.bAcknowledgement - Audit.bDetection = 35 ∧ Audit.bAcknowledgement ≤ Audit.bEffectiveStart + 30) := Audit.claim09
