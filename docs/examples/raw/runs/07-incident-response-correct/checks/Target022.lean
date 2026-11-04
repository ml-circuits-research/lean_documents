import Audit
#check @Audit.approvedPausesCapped
#print axioms Audit.approvedPausesCapped
example : (Audit.validPause Audit.pause1 ∧ Audit.validPause Audit.pause2 ∧ Audit.pause1.ends ≤ Audit.pause2.starts ∧ Audit.pauseMinutes = 70 ∧ Audit.excludedA = 45) := Audit.approvedPausesCapped
