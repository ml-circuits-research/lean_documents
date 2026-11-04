import IntervalModel
#check @Settlement.touching40
#print axioms Settlement.touching40
example : (Settlement.unionMinutes 180 [Settlement.a, Settlement.b, Settlement.c] = 40) := Settlement.touching40
