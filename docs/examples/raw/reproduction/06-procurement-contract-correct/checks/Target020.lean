import Audit
#check @Audit.p13Intermediate
#print axioms Audit.p13Intermediate
example : (Audit.p13Num = 249999975 ∧ Audit.p13Den = 10000 ∧ Audit.p13Num < 25000 * Audit.p13Den ∧ ¬ Audit.p13Cents < Audit.threshold 2) := Audit.p13Intermediate
