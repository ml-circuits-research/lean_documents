import Audit
#check @Audit.claim06Countermodels
#print axioms Audit.claim06Countermodels
example : (Audit.possibleApproved.packageContainsRegister = false ∧ Audit.possibleUnapproved.packageContainsRegister = false ∧ Audit.possibleApproved.approvalBeforeProposedStart = true ∧ Audit.possibleUnapproved.approvalBeforeProposedStart = false) := Audit.claim06Countermodels
