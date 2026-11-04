import IntervalModel
#check @Settlement.empty_interval
#print axioms Settlement.empty_interval
example : (∀ (point minute : Nat), ¬ (point ≤ minute ∧ minute < point)) := Settlement.empty_interval
