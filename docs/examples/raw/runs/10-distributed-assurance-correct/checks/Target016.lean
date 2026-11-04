import Audit
#check @Audit.n09PermitFailure
#print axioms Audit.n09PermitFailure
example : (Audit.minuteAt 19 23 59 < Audit.minuteAt 21 10 0 ∧ Audit.minuteAt 20 23 59 < Audit.minuteAt 21 10 0 ∧ Audit.n09PermitAt (Audit.minuteAt 21 10 0) = false) := Audit.n09PermitFailure
