import Stock.Audit
#check @StockAudit.allRows60
#print axioms StockAudit.allRows60
example : ((Stock.rows.map Stock.Row.quantity).sum = 60) := StockAudit.allRows60
