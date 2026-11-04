import Audit
#check @Audit.historicalAuthorized
#print axioms Audit.historicalAuthorized
example : (Audit.revisionB Audit.n04.time = false ∧ Audit.n04.permit = false ∧ Audit.ordinaryRoute Audit.n04 = true ∧ Audit.authorized Audit.n04 = true) := Audit.historicalAuthorized
