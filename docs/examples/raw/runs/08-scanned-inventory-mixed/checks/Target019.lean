import Audit
#check @Audit.claim12
#print axioms Audit.claim12
example : (∀ (reconciled : Audit.Lot → Prop), ¬ reconciled Audit.Lot.c → ¬ (∀ lot, reconciled lot)) := Audit.claim12
