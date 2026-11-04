import Audit
#check @Audit.daySixNoPhysicalAttendance
#print axioms Audit.daySixNoPhysicalAttendance
example : (∀ attends : Prop, (attends → Audit.AliveAt (Audit.instant 6 Audit.noon)) → ¬ attends) := Audit.daySixNoPhysicalAttendance
