import IntervalModel
#check @Settlement.overlapNot40
#print axioms Settlement.overlapNot40
example : (Settlement.unionMinutes 180 [Settlement.a, Settlement.b] ≠ 40) := Settlement.overlapNot40
