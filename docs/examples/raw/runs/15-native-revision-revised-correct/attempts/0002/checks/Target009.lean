import Audit
#check @Audit.claim3
#print axioms Audit.claim3
example : (Audit.currentReceipt.transfer = "T7" ∧ Audit.currentReceipt.date = "2026-11-04" ∧ Audit.currentReceipt.minute = 1000) := Audit.claim3
