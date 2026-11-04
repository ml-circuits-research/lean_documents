import Stock.Audit
#check @StockAudit.signatureInsufficient
#print axioms StockAudit.signatureInsufficient
example : (Stock.b ∈ Stock.rows ∧ Stock.b.signed = true ∧ ¬ Stock.eligible Stock.b) := StockAudit.signatureInsufficient
