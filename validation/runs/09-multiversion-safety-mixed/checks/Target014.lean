import Audit
#check @Audit.claim04
#print axioms Audit.claim04
example : (¬ (∀ u, Audit.normal u = true → Audit.within u = true)) := Audit.claim04
