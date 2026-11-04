import Audit
#check @Audit.sampleRate
#print axioms Audit.sampleRate
example : (0 < Audit.sample.length ∧ Audit.exceptions.length * 100 = Audit.sample.length * 50) := Audit.sampleRate
