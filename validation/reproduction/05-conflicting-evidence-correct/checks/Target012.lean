import Audit
#check @Audit.readinessNotEntailed
#print axioms Audit.readinessNotEntailed
example : (¬ (∀ smoke security ready : Prop, smoke → ((smoke ∧ security) → ready) → ready)) := Audit.readinessNotEntailed
