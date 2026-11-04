import Audit
#check @Audit.claim4
#print axioms Audit.claim4
example : (¬ (Audit.currentReceipt.minute ≤ Audit.receiptDeadline)) := Audit.claim4
