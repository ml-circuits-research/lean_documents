import Audit
#check @Audit.aliasBeforeActivation
#print axioms Audit.aliasBeforeActivation
example : (Audit.northAlias (Audit.minuteAt 21 10 0) = Audit.Principal.ben ∧ Audit.active (Audit.northAlias (Audit.minuteAt 21 10 0)) (Audit.minuteAt 21 10 0) = false) := Audit.aliasBeforeActivation
