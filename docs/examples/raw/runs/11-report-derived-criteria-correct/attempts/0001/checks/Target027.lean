import Campaign
#check @Campaign.populationAlternatives
#print axioms Campaign.populationAlternatives
example : (Campaign.populationCompletion 0 = 50000 ∧ Campaign.populationCompletion 1 = 50036 ∧ Campaign.populationCompletion 0 ≠ Campaign.populationCompletion 1) := Campaign.populationAlternatives
