import Audit
#check @Audit.restrictedDeadlineOpen
#print axioms Audit.restrictedDeadlineOpen
example : (Audit.standardDue Audit.c204 = none ∧ ∃ early late : Nat, early = Audit.at17 18 ∧ late ≠ Audit.at17 18 ∧ ¬ Audit.timely Audit.c204.submission early ∧ Audit.timely Audit.c204.submission late) := Audit.restrictedDeadlineOpen
