import Audit
#check @Audit.claim16Alternatives
#print axioms Audit.claim16Alternatives
example : (Audit.possiblePaid.signedInvoice = true ∧ Audit.possibleUnpaid.signedInvoice = true ∧ Audit.possiblePaid.deliveryAccepted = true ∧ Audit.possibleUnpaid.deliveryAccepted = true ∧ Audit.possiblePaid.paid = true ∧ Audit.possibleUnpaid.paid = false) := Audit.claim16Alternatives
