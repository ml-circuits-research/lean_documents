import Audit
#check @Audit.claim02
#print axioms Audit.claim02
example : (Audit.revision Audit.d202 = .one ∧ Audit.d202.received + 1 = Audit.boundary ∧ (∀ a, Audit.revision (Audit.withAssignment Audit.d202 a) = .one)) := Audit.claim02
