import Audit
#check @Audit.n01Authorized
#print axioms Audit.n01Authorized
example : (Audit.northAlias Audit.n01.time = Audit.Principal.ada ∧ Audit.revisionB Audit.n01.time = true ∧ Audit.ordinaryRoute Audit.n01 = true ∧ Audit.authorized Audit.n01 = true) := Audit.n01Authorized
