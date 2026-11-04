import Audit
#check @Audit.claim04MissingPremise
#print axioms Audit.claim04MissingPremise
example : (Audit.policy true false false ∧ Audit.policy true false true ∧ ¬ ((Audit.policy true false false ∧ true = true) → false = true)) := Audit.claim04MissingPremise
