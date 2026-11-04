import Stock.Audit
#check @StockAudit.historyUnderdetermined
#print axioms StockAudit.historyUnderdetermined
example : (EvidenceLogic.Underdetermined Stock.currentEvidence Stock.noPriorClearance) := StockAudit.historyUnderdetermined
