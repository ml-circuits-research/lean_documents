import Audit
#check @Audit.claim08
#print axioms Audit.claim08
example : (Audit.PauseEvidence.request ∈ Audit.suppliedPauseEvidence ∧ Audit.PauseEvidence.approval ∉ Audit.suppliedPauseEvidence) := Audit.claim08
