import IntervalModel
#check @Settlement.negativeTie
#print axioms Settlement.negativeTie
example : (Settlement.roundCents (-1005) = -101) := Settlement.negativeTie
