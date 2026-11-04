import Audit
#check @Audit.claim2
#print axioms Audit.claim2
example : (¬ (Audit.currentLedger.chargeA ≤ Audit.individualCap)) := Audit.claim2
