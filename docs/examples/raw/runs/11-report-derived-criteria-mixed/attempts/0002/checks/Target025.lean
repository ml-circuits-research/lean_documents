import Audit
#check @Audit.laterNonentailment
#print axioms Audit.laterNonentailment
example : (Audit.compatible Audit.quiet ∧ Audit.compatible Audit.incident ∧ Audit.quiet.laterIncidents = 0 ∧ Audit.incident.laterIncidents ≠ 0) := Audit.laterNonentailment
