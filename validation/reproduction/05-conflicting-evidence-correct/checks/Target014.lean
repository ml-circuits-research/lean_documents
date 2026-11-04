import Audit
#check @Audit.independentArtifactAbsent
#print axioms Audit.independentArtifactAbsent
example : (Audit.Attachment.independentReview ∉ Audit.packet) := Audit.independentArtifactAbsent
