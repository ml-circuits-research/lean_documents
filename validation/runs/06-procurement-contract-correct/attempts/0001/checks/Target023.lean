import Audit
#check @Audit.p16ApprovalFailure
#print axioms Audit.p16ApprovalFailure
example : (1500000 ≤ 1500000 ∧ ¬ Audit.validDana true 1500000 (Audit.expiry + 1) (Audit.expiry + 10) ∧ Audit.p16ValidApproval = false) := Audit.p16ApprovalFailure
