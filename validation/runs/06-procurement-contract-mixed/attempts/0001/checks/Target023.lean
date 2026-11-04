import Audit
#check @Audit.claim06
#print axioms Audit.claim06
example : (Audit.delegatedApproval true 1490000 21180 21181 = true ∧ (21180 : Nat) < 21181) := Audit.claim06
