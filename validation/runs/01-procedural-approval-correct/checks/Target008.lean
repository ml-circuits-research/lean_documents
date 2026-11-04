import Audit
#check @Audit.c02
#print axioms Audit.c02
example : (Audit.c102.approval = none ∧ Audit.RecordKind.request ≠ Audit.RecordKind.approval) := Audit.c02
