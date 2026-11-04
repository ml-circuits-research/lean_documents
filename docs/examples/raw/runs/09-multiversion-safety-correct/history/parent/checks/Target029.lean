import Audit
#check @Audit.sufficientRoute
#print axioms Audit.sufficientRoute
example : (∀ (Route Demonstration : Prop), (Route → Demonstration) → Route → Demonstration) := Audit.sufficientRoute
