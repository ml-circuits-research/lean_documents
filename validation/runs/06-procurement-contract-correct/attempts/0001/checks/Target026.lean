import Audit
#check @Audit.r18NoCompetition
#print axioms Audit.r18NoCompetition
example : (Audit.revisionAt 0 = 2 ∧ 2250000 < Audit.threshold (Audit.revisionAt 0) ∧ Audit.competitionSatisfied 2 2250000 false false = true) := Audit.r18NoCompetition
