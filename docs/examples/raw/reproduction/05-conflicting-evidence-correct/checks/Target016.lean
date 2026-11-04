import Audit
#check @Audit.missingFactsRemainOpen
#print axioms Audit.missingFactsRemainOpen
example : (∀ tested reviewed authentic : Bool, ∃ w : Audit.Completion, Audit.agreesWithPacket w ∧ w.testOccurred = tested ∧ w.reviewOccurred = reviewed ∧ w.signatureAuthentic = authentic) := Audit.missingFactsRemainOpen
