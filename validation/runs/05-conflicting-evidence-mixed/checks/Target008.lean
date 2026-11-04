import Audit
#check @Audit.claim01
#print axioms Audit.claim01
example : (Audit.manifestIds.length = 3 ∧ Audit.manifestIds.Nodup) := Audit.claim01
