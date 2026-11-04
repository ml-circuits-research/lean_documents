import Audit
#check @Audit.rackObligation
#print axioms Audit.rackObligation
example : (Audit.rackAggregates = true ∧ Audit.rackTotal = 2500000 ∧ Audit.threshold (Audit.revisionAt 540) ≤ Audit.rackTotal ∧ Audit.competitionSatisfied 2 Audit.rackTotal false false = false) := Audit.rackObligation
