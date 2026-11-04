import Audit
#check @Audit.claim02
#print axioms Audit.claim02
example : (∀ t : Int, 2880 ≤ t → t ≤ 4319 → Audit.revision t = 2) := Audit.claim02
