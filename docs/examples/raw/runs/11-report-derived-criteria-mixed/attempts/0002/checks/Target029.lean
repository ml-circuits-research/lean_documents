import Audit
#check @Audit.eligibleMembers
#print axioms Audit.eligibleMembers
example : (Audit.eligible Audit.a ∧ Audit.eligible Audit.b ∧ ¬ Audit.eligible Audit.c ∧ ¬ Audit.eligible Audit.d) := Audit.eligibleMembers
