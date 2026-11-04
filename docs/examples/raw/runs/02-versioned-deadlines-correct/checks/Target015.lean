import Audit
#check @Audit.claim07Alternatives
#print axioms Audit.claim07Alternatives
example : (Audit.timelyCompletion.annexTransferred = false ∧ Audit.lateCompletion.annexTransferred = false ∧ Audit.timelyCompletion.due ≠ Audit.lateCompletion.due ∧ Audit.d204.submitted ≤ Audit.timelyCompletion.due ∧ Audit.lateCompletion.due < Audit.d204.submitted) := Audit.claim07Alternatives
