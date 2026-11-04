import Audit
#check @Audit.populationNonentailment
#print axioms Audit.populationNonentailment
example : (Audit.compatible Audit.quiet ∧ Audit.compatible Audit.extraAmount ∧ Audit.populationTotal Audit.quiet = 50000 ∧ Audit.populationTotal Audit.extraAmount ≠ 50000) := Audit.populationNonentailment
