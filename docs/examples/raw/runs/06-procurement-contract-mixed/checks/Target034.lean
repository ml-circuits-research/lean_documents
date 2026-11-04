import Audit
#check @Audit.claim17Witnesses
#print axioms Audit.claim17Witnesses
example : (Audit.CoveredPurchase.p16 ∈ Audit.covered ∧ Audit.approvalValid .p16 = false ∧ Audit.compliant .p16 = false ∧ Audit.CoveredPurchase.p11 ∈ Audit.covered ∧ Audit.required .p11 = true ∧ Audit.rackCertificate = false ∧ Audit.rackException = false ∧ Audit.compliant .p11 = false) := Audit.claim17Witnesses
