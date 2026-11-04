import Audit
#check @Audit.claim02
#print axioms Audit.claim02
example : (Audit.standard Audit.c102 = false ∧ Audit.c102Request ≠ Audit.EventKind.approval) := Audit.claim02
