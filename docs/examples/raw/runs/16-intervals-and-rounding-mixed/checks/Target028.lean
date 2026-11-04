import IntervalModel
#check @Settlement.positiveNot100
#print axioms Settlement.positiveNot100
example : (Settlement.roundCents 1005 ≠ 100) := Settlement.positiveNot100
