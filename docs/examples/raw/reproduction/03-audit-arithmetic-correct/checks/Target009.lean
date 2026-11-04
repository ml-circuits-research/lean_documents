import Audit
#check @Audit.exactExceptions
#print axioms Audit.exactExceptions
example : (Audit.sample.length = 4 ∧ Audit.exceptions.length = 2 ∧ Audit.exceptionIDs = [Audit.p03ID, Audit.p04ID]) := Audit.exactExceptions
