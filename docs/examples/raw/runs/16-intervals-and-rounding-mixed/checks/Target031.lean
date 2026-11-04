import IntervalModel
#check @Settlement.aggregateIs101
#print axioms Settlement.aggregateIs101
example : (Settlement.roundCents Settlement.invoiceLines.sum = 101) := Settlement.aggregateIs101
