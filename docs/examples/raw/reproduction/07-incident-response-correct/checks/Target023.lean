import Audit
#check @Audit.noMaintenanceForA
#print axioms Audit.noMaintenanceForA
example : (Audit.effectiveStart 1 false Audit.detectionA 0 180 = Audit.detectionA ∧ Audit.effectiveStart 1 true Audit.detectionA 0 180 = Audit.detectionA) := Audit.noMaintenanceForA
