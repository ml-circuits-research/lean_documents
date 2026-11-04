import Audit
#check @Audit.claim13
#print axioms Audit.claim13
example : ((Audit.Serial.n01, Audit.Signer.sera) ∈ Audit.releaseSignatures ∧ (Audit.Serial.e17, Audit.Signer.sera) ∈ Audit.releaseSignatures ∧ (Audit.Serial.c01, Audit.Signer.sera) ∈ Audit.releaseSignatures ∧ Audit.authorizedReleaseSigner .sera = true) := Audit.claim13
