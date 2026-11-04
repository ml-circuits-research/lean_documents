import Audit
#check @Audit.manifestExact
#print axioms Audit.manifestExact
example : (Audit.manifest.length = 3 ∧ Audit.manifest.Nodup ∧ Audit.manifest = [Audit.Entry.a01, Audit.Entry.a02, Audit.Entry.a03]) := Audit.manifestExact
