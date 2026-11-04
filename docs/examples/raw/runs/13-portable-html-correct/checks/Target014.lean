import Stock.Audit
#check @StockAudit.notCounted60
#print axioms StockAudit.notCounted60
example : (Stock.total ≠ 60) := StockAudit.notCounted60
