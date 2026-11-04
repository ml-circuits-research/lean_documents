import Audit
#check @Audit.p13Normalization
#print axioms Audit.p13Normalization
example : (Audit.p13Num = 249999975 ∧ Audit.p13Den = 10000 ∧ Audit.p13Cents = 2500000 ∧ Audit.threshold 2 ≤ Audit.p13Cents ∧ (9 : Nat) < 11 ∧ Audit.competitionSatisfied 2 Audit.p13Cents true false = true) := Audit.p13Normalization
