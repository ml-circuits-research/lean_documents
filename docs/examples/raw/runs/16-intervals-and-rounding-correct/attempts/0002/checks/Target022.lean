import IntervalModel
#check @Settlement.touching_union
#print axioms Settlement.touching_union
example : (∀ (lo mid hi minute : Nat), lo ≤ mid → mid ≤ hi → (((lo ≤ minute ∧ minute < mid) ∨ (mid ≤ minute ∧ minute < hi)) ↔ (lo ≤ minute ∧ minute < hi))) := Settlement.touching_union
