import Audit
#check @Audit.keyExchangeAlive
#print axioms Audit.keyExchangeAlive
example : (Audit.AliveAt (Audit.instant 2 Audit.noon)) := Audit.keyExchangeAlive
