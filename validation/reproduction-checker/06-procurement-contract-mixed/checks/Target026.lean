import Audit
#check @Audit.claim09
#print axioms Audit.claim09
example : (Audit.competitionRequired (Audit.revision (-1)) 2250000 = true ∧ Audit.r17Certificate = false ∧ Audit.r17Exception = false) := Audit.claim09
