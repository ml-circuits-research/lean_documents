import Audit
#check @Audit.populationLowerBound
#print axioms Audit.populationLowerBound
example : (∀ unknownExceptions : Nat, unknownExceptions ≤ 16 → 2 ≤ Audit.populationExceptions unknownExceptions) := Audit.populationLowerBound
