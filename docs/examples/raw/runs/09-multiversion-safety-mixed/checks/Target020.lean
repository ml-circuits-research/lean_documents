import Audit
#check @Audit.claim11
#print axioms Audit.claim11
example : (¬ (∀ c b f s : Bool, Audit.release true c b f s = true)) := Audit.claim11
