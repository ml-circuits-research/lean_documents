import Stock.Audit
#check @StockAudit.archivedExcluded
#print axioms StockAudit.archivedExcluded
example : (Stock.counted Stock.c = false) := StockAudit.archivedExcluded
