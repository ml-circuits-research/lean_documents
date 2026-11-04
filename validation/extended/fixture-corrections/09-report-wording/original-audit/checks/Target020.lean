import Audit
#check @Audit.claim04
#print axioms Audit.claim04
example : ((101 : Nat) ∈ Audit.n02 ∧ 100 < (101 : Nat) ∧ Audit.within Audit.n02 100 = false) := Audit.claim04
