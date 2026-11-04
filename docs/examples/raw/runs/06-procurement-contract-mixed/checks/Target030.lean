import Audit
#check @Audit.compatibilityAlternatives
#print axioms Audit.compatibilityAlternatives
example : (Audit.onlyCompatible .warranty true true = true ∧ Audit.onlyCompatible .physical true true = false) := Audit.compatibilityAlternatives
