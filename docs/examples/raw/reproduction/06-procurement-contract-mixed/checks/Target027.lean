import Audit
#check @Audit.claim10
#print axioms Audit.claim10
example : (Audit.revision 0 = 2 ∧ Audit.competitionRequired (Audit.revision 0) 2250000 = false ∧ (2000000 : Nat) ≤ 2250000) := Audit.claim10
