import Audit
#check @Audit.claim02Conflict
#print axioms Audit.claim02Conflict
example : (Audit.qa.scope = Audit.ops.scope ∧ Audit.qa.issuer ≠ Audit.ops.issuer ∧ Audit.qa.assertsEnabled = true ∧ Audit.ops.assertsEnabled = false) := Audit.claim02Conflict
