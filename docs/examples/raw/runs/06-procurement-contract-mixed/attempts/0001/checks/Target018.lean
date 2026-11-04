import Audit
#check @Audit.claim01
#print axioms Audit.claim01
example : (Audit.rackAggregates = true ∧ Audit.rackKnownBeforeFirst = true ∧ Audit.competitionRequired 2 Audit.rackCents = true ∧ (1240000 : Nat) < 2500000 ∧ (1260000 : Nat) < 2500000) := Audit.claim01
