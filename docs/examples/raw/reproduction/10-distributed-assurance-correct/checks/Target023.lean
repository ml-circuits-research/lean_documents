import Audit
#check @Audit.universalCounterexample
#print axioms Audit.universalCounterexample
example : (∀ recorded : List Audit.Release, Audit.n58 ∈ recorded → ¬ (∀ r ∈ recorded, Audit.authorized r = true)) := Audit.universalCounterexample
