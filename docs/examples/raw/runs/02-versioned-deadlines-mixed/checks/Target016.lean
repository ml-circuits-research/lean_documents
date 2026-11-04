import Audit
#check @Audit.timely202Refuted
#print axioms Audit.timely202Refuted
example : (Audit.standardDue Audit.c202 = some (Audit.at17 19) ∧ ¬ Audit.timely Audit.c202.submission (Audit.at17 19)) := Audit.timely202Refuted
