import Audit
#check @Audit.claim03Alternatives
#print axioms Audit.claim03Alternatives
example : (Audit.possibleTest.certificateAttached = false ∧ Audit.possibleNoTest.certificateAttached = false ∧ Audit.possibleTest.testOccurredBeforeCutoff = true ∧ Audit.possibleNoTest.testOccurredBeforeCutoff = false) := Audit.claim03Alternatives
