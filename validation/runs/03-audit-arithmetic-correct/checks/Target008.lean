import Audit
#check @Audit.budgetDifference
#print axioms Audit.budgetDifference
example : (Audit.total Audit.sample ≤ Audit.budget ∧ Audit.budget - Audit.total Audit.sample = 25000) := Audit.budgetDifference
