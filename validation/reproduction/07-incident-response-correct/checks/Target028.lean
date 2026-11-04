import Audit
#check @Audit.executiveTimely
#print axioms Audit.executiveTimely
example : (Audit.uncontainedA 60 ∧ Audit.executiveDelivered = 72 ∧ Audit.executiveDelivered - 60 = 12 ∧ Audit.timely 60 Audit.executiveDelivered 15) := Audit.executiveTimely
