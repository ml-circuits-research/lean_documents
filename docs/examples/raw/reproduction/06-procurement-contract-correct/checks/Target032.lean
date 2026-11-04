import Audit
#check @Audit.paymentOpen
#print axioms Audit.paymentOpen
example : (∀ paid : Bool, ∃ w : Audit.PaymentWorld, w.invoice = true ∧ w.delivery = true ∧ w.paid = paid) := Audit.paymentOpen
