import Audit
#check @Audit.claim13
#print axioms Audit.claim13
example : (∀ s q, (Audit.reserve s q).onHand = s.onHand ∧ (Audit.reserve s q).reserved = s.reserved + q) := Audit.claim13
