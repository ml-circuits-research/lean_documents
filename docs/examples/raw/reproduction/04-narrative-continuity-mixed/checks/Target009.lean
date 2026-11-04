import Audit
#check @Audit.claim01
#print axioms Audit.claim01
example : (Audit.keyStoryTime = Audit.tick 2 12 ∧ Audit.ConfirmedAliveAt Audit.keyStoryTime) := Audit.claim01
