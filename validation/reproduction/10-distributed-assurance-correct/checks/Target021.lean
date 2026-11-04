import Audit
#check @Audit.n58NotCovered
#print axioms Audit.n58NotCovered
example : (Audit.boardWindow 58 (Audit.minuteAt 22 10 0) = false) := Audit.n58NotCovered
