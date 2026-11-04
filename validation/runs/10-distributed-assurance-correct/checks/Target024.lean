import Audit
#check @Audit.n59Open
#print axioms Audit.n59Open
example : (Audit.authorized (Audit.n59Completion true) = true ∧ Audit.authorized (Audit.n59Completion false) = false) := Audit.n59Open
