import Audit
#check @Audit.claim06
#print axioms Audit.claim06
example : (Audit.delegated 51 20 = false ∧ Audit.routeB true (Audit.delegated 51 20) true = false) := Audit.claim06
