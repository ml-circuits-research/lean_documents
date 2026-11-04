import IntervalModel
#check @Settlement.overlap30
#print axioms Settlement.overlap30
example : (Settlement.unionMinutes 180 [Settlement.a, Settlement.b] = 30) := Settlement.overlap30
