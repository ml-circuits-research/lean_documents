import Campaign
#check @Campaign.eligibleExactly
#print axioms Campaign.eligibleExactly
example : (∀ x : Campaign.Dispatch, Campaign.eligible x ↔ x = Campaign.Dispatch.a ∨ x = Campaign.Dispatch.b) := Campaign.eligibleExactly
