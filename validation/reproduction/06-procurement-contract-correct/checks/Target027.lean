import Audit
#check @Audit.e19Exception
#print axioms Audit.e19Exception
example : (Audit.urgentException true true true Audit.e19Declaration Audit.e19Commitment Audit.e19Review ∧ Audit.e19Review - Audit.e19Commitment = 48 * 60 ∧ Audit.e19Declaration < Audit.e19Commitment) := Audit.e19Exception
