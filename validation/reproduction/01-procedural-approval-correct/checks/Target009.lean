import Audit
#check @Audit.c03
#print axioms Audit.c03
example : (Audit.Emergency Audit.c102 ∧ Audit.c102.incident = true ∧ (605 < 615) ∧ (2055 = 615 + 1440)) := Audit.c03
