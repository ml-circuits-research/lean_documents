import IntervalModel
#check @Settlement.negativeNot100
#print axioms Settlement.negativeNot100
example : (Settlement.roundCents (-1005) ≠ -100) := Settlement.negativeNot100
