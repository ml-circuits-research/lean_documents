import Audit
#check @Audit.timely203
#print axioms Audit.timely203
example : (Audit.standardDue Audit.c203 = some (Audit.at17 17) ∧ Audit.timely Audit.c203.submission (Audit.at17 17)) := Audit.timely203
