import Audit
#check @Audit.populationLowerBound
#print axioms Audit.populationLowerBound
example : (∀ unsampledMissing : Nat, unsampledMissing ≤ 16 → 2 ≤ Audit.populationExceptions unsampledMissing ∧ Audit.populationExceptions unsampledMissing ≤ 18) := Audit.populationLowerBound
