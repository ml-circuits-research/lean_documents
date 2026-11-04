import Audit
#check @Audit.urgencyInsufficient
#print axioms Audit.urgencyInsufficient
example : (¬ Audit.urgentException true false false Audit.e19Declaration Audit.e19Commitment Audit.e19Review) := Audit.urgencyInsufficient
