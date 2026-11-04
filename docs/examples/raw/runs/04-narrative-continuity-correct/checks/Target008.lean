import Audit
#check @Audit.revivalAndNoonLife
#print axioms Audit.revivalAndNoonLife
example : (Audit.revivalTime = Audit.instant 8 Audit.dawn ∧ Audit.AliveAt (Audit.instant 8 Audit.dawn) ∧ Audit.AliveAt (Audit.instant 8 Audit.noon) ∧ Audit.instant 8 Audit.dawn < Audit.instant 8 Audit.noon) := Audit.revivalAndNoonLife
