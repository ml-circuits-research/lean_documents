import Audit
#check @Audit.daySixDead
#print axioms Audit.daySixDead
example : (Audit.DeadAt (Audit.instant 6 Audit.noon) ∧ ¬ Audit.AliveAt (Audit.instant 6 Audit.noon)) := Audit.daySixDead
