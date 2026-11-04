import Audit
#check @Audit.claim06
#print axioms Audit.claim06
example : (Audit.pauseConditions = true ∧ Audit.rawPauseA = 70 ∧ Audit.excludedA = 45 ∧ Audit.excludedA < Audit.rawPauseA) := Audit.claim06
