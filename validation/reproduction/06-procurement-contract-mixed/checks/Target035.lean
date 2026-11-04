import Audit
#check @Audit.claim17UniversalFalse
#print axioms Audit.claim17UniversalFalse
example : (¬ (∀ p, p ∈ Audit.covered → Audit.compliant p = true)) := Audit.claim17UniversalFalse
