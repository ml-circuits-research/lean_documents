import Audit
#check @Audit.gapUnderdetermined
#print axioms Audit.gapUnderdetermined
example : (∀ event : Bool, ∃ w : Audit.MonitoringWorld, w.retainedGapSamples = false ∧ w.listedAlarmsOutsideGap = false ∧ w.exfiltrationInGap = event) := Audit.gapUnderdetermined
