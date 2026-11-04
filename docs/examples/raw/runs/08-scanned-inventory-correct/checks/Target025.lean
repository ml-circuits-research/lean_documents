import Audit
#check @Audit.claim11Alternatives
#print axioms Audit.claim11Alternatives
example : (Audit.possibleD74.suppliedReceiverSigned = false ∧ Audit.possibleD78.suppliedReceiverSigned = false ∧ Audit.possibleD74.receiverProposal = Audit.possibleD78.receiverProposal ∧ Audit.possibleD74.carrierProposal = Audit.possibleD78.carrierProposal ∧ Audit.possibleD74.actualAccepted ≠ Audit.possibleD78.actualAccepted) := Audit.claim11Alternatives
