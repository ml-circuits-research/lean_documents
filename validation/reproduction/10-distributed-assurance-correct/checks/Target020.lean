import Audit
#check @Audit.n57Exception
#print axioms Audit.n57Exception
example : (Audit.boardWindow Audit.n57.node Audit.n57.time = true ∧ Audit.n57.approvalTime = some (Audit.minuteAt 22 9 0) ∧ Audit.boardWindow Audit.n57.node (Audit.minuteAt 22 9 0) = true ∧ Audit.ordinaryRoute Audit.n57 = false ∧ Audit.boardRoute Audit.n57 = true ∧ Audit.authorized Audit.n57 = true) := Audit.n57Exception
