import Audit
#check @Audit.claim11
#print axioms Audit.claim11
example : (Audit.releaseRoute true false true true true = false ∧ ¬ (∀ calibration channels faults signature, Audit.releaseRoute true calibration channels faults signature = true)) := Audit.claim11
