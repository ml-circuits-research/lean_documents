import Audit
#check @Audit.populationCompletionAlternatives
#print axioms Audit.populationCompletionAlternatives
example : (Audit.populationExceptions 0 * 100 ≠ 50 * 20 ∧ Audit.populationExceptions 8 * 100 = 50 * 20 ∧ (0 : Nat) ≤ 16 ∧ (8 : Nat) ≤ 16) := Audit.populationCompletionAlternatives
