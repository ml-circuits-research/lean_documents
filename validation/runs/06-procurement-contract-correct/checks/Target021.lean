import Audit
#check @Audit.p14Normalization
#print axioms Audit.p14Normalization
example : (Audit.roundCents 24999994 1000 = 2499999 ∧ Audit.roundCents 24999994 1000 < Audit.threshold 2) := Audit.p14Normalization
