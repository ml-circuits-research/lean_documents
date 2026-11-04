import Audit
#check @Audit.claim08
#print axioms Audit.claim08
example : (Audit.standard Audit.c102 = false ∧ Audit.emergency Audit.c102 = true ∧ Audit.authorized Audit.c102 = true) := Audit.claim08
