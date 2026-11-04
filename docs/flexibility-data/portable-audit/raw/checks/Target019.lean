import Stock.Audit
#check @StockAudit.noHistoricalEntailment
#print axioms StockAudit.noHistoricalEntailment
example : (¬ EvidenceLogic.Entails Stock.currentEvidence Stock.noPriorClearance) := StockAudit.noHistoricalEntailment
