import Audit
#check @Audit.compatibilityOpen
#print axioms Audit.compatibilityOpen
example : (Audit.onlyCompatible Audit.CompatibilityTest.warranty = true ∧ Audit.onlyCompatible Audit.CompatibilityTest.physical = false) := Audit.compatibilityOpen
