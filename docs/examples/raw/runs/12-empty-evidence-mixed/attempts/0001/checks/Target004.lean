import EmptyEvidence
#check @EmptyEvidence.missingRecordDoesNotImplyFailure
#print axioms EmptyEvidence.missingRecordDoesNotImplyFailure
example : (¬ (∀ passed : Bool, EmptyEvidence.admissible passed → passed = false)) := EmptyEvidence.missingRecordDoesNotImplyFailure
