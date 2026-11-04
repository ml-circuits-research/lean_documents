import Audit
#check @Audit.objectiveFailures
#print axioms Audit.objectiveFailures
example : (Audit.compliant (Audit.competitionSatisfied 2 Audit.rackTotal false false) true = false ∧ Audit.compliant (Audit.competitionSatisfied 1 2250000 false false) true = false ∧ Audit.compliant (Audit.competitionSatisfied 2 1500000 false false) false = false) := Audit.objectiveFailures
