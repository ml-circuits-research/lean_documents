import Audit
#check @Audit.claim10
#print axioms Audit.claim10
example : (Audit.technical.queued ≤ Audit.aDetection + 10 ∧ ¬ (Audit.technical.delivered ≤ Audit.aDetection + 10) ∧ Audit.technical.delivered = 11) := Audit.claim10
