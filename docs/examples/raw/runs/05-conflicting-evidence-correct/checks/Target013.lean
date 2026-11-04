import Audit
#check @Audit.citationCycle
#print axioms Audit.citationCycle
example : (Audit.supportLinks = [(Audit.Node.archivedClaim, Audit.Node.verificationAppendix), (Audit.Node.verificationAppendix, Audit.Node.archivedClaim)] ∧ (Audit.Node.archivedClaim, Audit.Node.independentArtifact) ∉ Audit.supportLinks ∧ (Audit.Node.verificationAppendix, Audit.Node.independentArtifact) ∉ Audit.supportLinks) := Audit.citationCycle
