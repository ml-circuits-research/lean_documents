import Audit
#check @Audit.allInvoicesMatched
#print axioms Audit.allInvoicesMatched
example : (∀ p ∈ Audit.sample, p.matched = true) := Audit.allInvoicesMatched
