import Audit
#check @Audit.claim14
#print axioms Audit.claim14
example : (Audit.CorrectionEvidence.unsignedProposal ∈ Audit.suppliedCCorrections ∧ Audit.CorrectionEvidence.approvedCorrection ∉ Audit.suppliedCCorrections) := Audit.claim14
