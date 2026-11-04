import EmptyEvidence
#check @EmptyEvidence.bothPossible
#print axioms EmptyEvidence.bothPossible
example : (EmptyEvidence.admissible true ∧ EmptyEvidence.admissible false) := EmptyEvidence.bothPossible
