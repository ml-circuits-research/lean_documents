import Audit
#check @Audit.claim02
#print axioms Audit.claim02
example : (∀ (attendance : Prop), (attendance → ¬ Audit.DeadAt (Audit.tick 6 12)) → ¬ attendance) := Audit.claim02
