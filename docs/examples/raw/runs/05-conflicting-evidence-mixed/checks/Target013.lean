import Audit
#check @Audit.claim05Cycle
#print axioms Audit.claim05Cycle
example : ((Audit.CitationNode.reportClaim, Audit.CitationNode.appendix) ∈ Audit.citationEdges ∧ (Audit.CitationNode.appendix, Audit.CitationNode.reportClaim) ∈ Audit.citationEdges ∧ Audit.CitationNode.independentReview ∉ Audit.suppliedReviewArtifacts) := Audit.claim05Cycle
