import Audit
#check @Audit.e17Applicable
#print axioms Audit.e17Applicable
example : (∀ t : Int, 2880 ≤ t → t ≤ 4319 → Audit.limitAt .e17 .normal 20 t = some 110) := Audit.e17Applicable
