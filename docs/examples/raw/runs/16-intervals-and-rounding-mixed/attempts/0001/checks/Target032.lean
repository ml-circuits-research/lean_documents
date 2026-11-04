import IntervalModel
#check @Settlement.historicalAlternatives
#print axioms Settlement.historicalAlternatives
example : ((¬ Settlement.historicalThresholdMet 0) ∧ Settlement.historicalThresholdMet 3) := Settlement.historicalAlternatives
