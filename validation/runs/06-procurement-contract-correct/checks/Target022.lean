import Audit
#check @Audit.p15Approval
#print axioms Audit.p15Approval
example : (Audit.validDana true 1490000 Audit.expiry (Audit.expiry + 1)) := Audit.p15Approval
