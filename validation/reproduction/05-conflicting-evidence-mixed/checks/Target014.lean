import Audit
#check @Audit.claim06Alternatives
#print axioms Audit.claim06Alternatives
example : (Audit.possibleVerified.markerPresent = true ∧ Audit.possibleUnverified.markerPresent = true ∧ Audit.possibleVerified.verificationArtifactSupplied = false ∧ Audit.possibleUnverified.verificationArtifactSupplied = false ∧ Audit.possibleVerified.verifiedBeforeCutoff = true ∧ Audit.possibleUnverified.verifiedBeforeCutoff = false) := Audit.claim06Alternatives
