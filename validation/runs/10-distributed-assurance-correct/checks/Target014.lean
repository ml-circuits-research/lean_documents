import Audit
#check @Audit.sixtyNodes
#print axioms Audit.sixtyNodes
example : (Audit.nodes.length = 60 ∧ Audit.nodes.Nodup ∧ Audit.nodes.head? = some 1 ∧ Audit.nodes.getLast? = some 60) := Audit.sixtyNodes
