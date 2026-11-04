import Audit
#check @Audit.n60KnownAuthorized
#print axioms Audit.n60KnownAuthorized
example : (Audit.ordinaryRoute Audit.n60 = true ∧ Audit.authorized Audit.n60 = true) := Audit.n60KnownAuthorized
