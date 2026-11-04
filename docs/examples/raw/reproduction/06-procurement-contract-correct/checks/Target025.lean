import Audit
#check @Audit.r17CompetitionFailure
#print axioms Audit.r17CompetitionFailure
example : (Audit.threshold (Audit.revisionAt (-1)) < 2250000 ∧ Audit.competitionSatisfied 1 2250000 false false = false ∧ Audit.compliant (Audit.competitionSatisfied 1 2250000 false false) true = false) := Audit.r17CompetitionFailure
