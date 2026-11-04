import Audit
#check @Audit.c04
#print axioms Audit.c04
example : (¬ Audit.Standard Audit.c103 ∧ Audit.c103.approval = some Audit.c103.start ∧ Audit.c103.incident = false ∧ Audit.c103.declaration = none ∧ ¬ Audit.Emergency Audit.c103) := Audit.c04
