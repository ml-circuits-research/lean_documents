import Stock.Data
import EvidenceLogic

namespace StockAudit

theorem counted45 : Stock.total = 45 := by decide

theorem notCounted60 : Stock.total ≠ 60 := by decide

theorem allRows60 : (Stock.rows.map Stock.Row.quantity).sum = 60 := by decide

theorem archivedExcluded : Stock.counted Stock.c = false := by decide

theorem aEligible : Stock.eligible Stock.a := by decide

theorem signatureInsufficient :
    Stock.b ∈ Stock.rows ∧ Stock.b.signed = true ∧ ¬ Stock.eligible Stock.b := by decide

theorem historyUnderdetermined :
    EvidenceLogic.Underdetermined Stock.currentEvidence Stock.noPriorClearance := by
  refine ⟨false, true, ?_, ?_, ?_, ?_⟩ <;> decide

theorem noHistoricalEntailment :
    ¬ EvidenceLogic.Entails Stock.currentEvidence Stock.noPriorClearance := by
  apply EvidenceLogic.notEntailsOfCounterexample (world := true)
  · decide
  · decide

end StockAudit
