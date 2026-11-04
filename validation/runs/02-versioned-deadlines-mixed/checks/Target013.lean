import Audit
#check @Audit.timely201
#print axioms Audit.timely201
example : (Audit.standardDue Audit.c201 = some (Audit.at17 10) ∧ Audit.timely Audit.c201.submission (Audit.at17 10)) := Audit.timely201
