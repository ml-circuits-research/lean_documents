import Audit
#check @Audit.notAllPrior
#print axioms Audit.notAllPrior
example : (¬ (∀ x ∈ Audit.cohort, Audit.ordinary x)) := Audit.notAllPrior
