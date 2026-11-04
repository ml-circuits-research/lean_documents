import Audit
#check @Audit.claim1
#print axioms Audit.claim1
example : (Audit.currentLedger.chargeA + Audit.currentLedger.chargeB + Audit.currentLedger.chargeC ≠ 130) := Audit.claim1
