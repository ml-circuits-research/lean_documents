import Audit
#check @Audit.approvalCounterexample
#print axioms Audit.approvalCounterexample
example : (Audit.p03 ∈ Audit.sample ∧ Audit.p03.matched = true ∧ Audit.p03.approved = false ∧ ¬ (∀ p ∈ Audit.sample, p.approved = true)) := Audit.approvalCounterexample
