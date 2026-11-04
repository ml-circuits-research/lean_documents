import Audit
#check @Audit.n58Unauthorized
#print axioms Audit.n58Unauthorized
example : (Audit.minuteAt 22 9 0 < Audit.n58.time ∧ Audit.n58.time < Audit.minuteAt 22 11 0 ∧ Audit.authorized Audit.n58 = false ∧ 58 ∈ Audit.nodes) := Audit.n58Unauthorized
