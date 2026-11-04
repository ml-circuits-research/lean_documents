import Audit
#check @Audit.passInsufficient
#print axioms Audit.passInsufficient
example : (Audit.d ∈ Audit.cohort ∧ Audit.d.passed = true ∧ ¬ Audit.eligible Audit.d) := Audit.passInsufficient
