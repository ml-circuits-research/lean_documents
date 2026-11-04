import Audit
#check @Audit.sampleExceptionRate
#print axioms Audit.sampleExceptionRate
example : (Audit.sample.length = 4 ∧ Audit.exceptionCount = 2 ∧ Audit.exceptionCount * 100 = 50 * Audit.sample.length) := Audit.sampleExceptionRate
