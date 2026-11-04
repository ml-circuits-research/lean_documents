import Audit
#check @Audit.cApproval
#print axioms Audit.cApproval
example : (¬ Audit.compliant Audit.c) := Audit.cApproval
