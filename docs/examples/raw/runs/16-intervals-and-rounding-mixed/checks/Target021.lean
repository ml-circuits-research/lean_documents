import IntervalModel
#check @Settlement.touchingNot41
#print axioms Settlement.touchingNot41
example : (Settlement.unionMinutes 180 [Settlement.a, Settlement.b, Settlement.c] ≠ 41) := Settlement.touchingNot41
