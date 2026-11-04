import Audit
#check @Audit.deadline203Refuted
#print axioms Audit.deadline203Refuted
example : (Audit.standardDue Audit.c203 ≠ some (Audit.at17 16) ∧ Audit.standardDue Audit.c203 = some (Audit.at17 17)) := Audit.deadline203Refuted
