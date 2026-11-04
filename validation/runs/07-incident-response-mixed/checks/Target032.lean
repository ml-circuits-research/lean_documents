import Audit
#check @Audit.gapAlternatives
#print axioms Audit.gapAlternatives
example : (Audit.possibleNoExfiltration.gapSamplesAvailable = false ∧ Audit.possibleExfiltration.gapSamplesAvailable = false ∧ Audit.possibleNoExfiltration.retainedListedAlarms = false ∧ Audit.possibleExfiltration.retainedListedAlarms = false ∧ Audit.possibleNoExfiltration.exfiltrationDuringGap = false ∧ Audit.possibleExfiltration.exfiltrationDuringGap = true) := Audit.gapAlternatives
