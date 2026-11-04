import Audit
#check @Audit.claim08
#print axioms Audit.claim08
example : ((170 : Int) ≤ Audit.bDetection ∧ Audit.bDetection < 200 ∧ Audit.bEffectiveStart = 200 ∧ Audit.bAcknowledgement - Audit.bEffectiveStart = 25 ∧ Audit.bAcknowledgement ≤ Audit.bEffectiveStart + 30) := Audit.claim08
