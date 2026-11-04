import Audit
#check @Audit.conditionalReadiness
#print axioms Audit.conditionalReadiness
example : (∀ (Smoke Security Ready : Prop), ((Smoke ∧ Security) → Ready) → Smoke → Security → Ready) := Audit.conditionalReadiness
