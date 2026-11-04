import Audit
#check @Audit.r17Version
#print axioms Audit.r17Version
example : (Audit.revisionAt (-1) = 1 ∧ Audit.r17AddedRequirement = false ∧ Audit.r17PriceIncrease = false) := Audit.r17Version
