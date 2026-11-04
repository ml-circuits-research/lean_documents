import Audit
#check @Audit.claim11
#print axioms Audit.claim11
example : (Audit.commander.delivered = 22 ∧ ¬ (Audit.commander.delivered ≤ Audit.aDetection + 20)) := Audit.claim11
