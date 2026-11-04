import Audit
#check @Audit.certificateAbsent
#print axioms Audit.certificateAbsent
example : (Audit.Attachment.penetrationCertificate ∉ Audit.packet) := Audit.certificateAbsent
