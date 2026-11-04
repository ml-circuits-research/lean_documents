import Audit
#check @Audit.claim08
#print axioms Audit.claim08
example : (Audit.n03ChannelBAvailable = false ∧ Audit.n03Second = .aborted ∧ Audit.n03Third = .absent ∧ Audit.validMeasurement Audit.n03Third = none) := Audit.claim08
