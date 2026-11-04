import Audit
#check @Audit.budgetDifference
#print axioms Audit.budgetDifference
example : (Audit.budget - Audit.sampleTotal = 25000 ∧ Audit.budget - Audit.sampleTotal ≠ 35000 ∧ Audit.sampleTotal ≤ Audit.budget) := Audit.budgetDifference
