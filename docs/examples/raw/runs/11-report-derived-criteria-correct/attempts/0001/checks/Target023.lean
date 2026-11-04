import Campaign
#check @Campaign.laterAlternatives
#print axioms Campaign.laterAlternatives
example : (Campaign.laterCompatible 0 ∧ Campaign.laterCompatible 1 ∧ (0 : Nat) ≠ 1) := Campaign.laterAlternatives
