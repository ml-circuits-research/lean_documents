namespace Audit

structure Ledger where
  chargeA : Nat
  chargeB : Nat
  chargeC : Nat
  deriving DecidableEq

structure Receipt where
  transfer : String
  date : String
  minute : Nat
  deriving DecidableEq

-- Current source fields are reviewed documentary assumptions, not authenticated facts.
def currentLedger : Ledger := ⟨60, 40, 45⟩
def currentReceipt : Receipt := ⟨"T7", "2026-11-04", 1000⟩
def individualCap : Nat := 50
def receiptDeadline : Nat := 990

theorem claim1 : Audit.currentLedger.chargeA + Audit.currentLedger.chargeB + Audit.currentLedger.chargeC ≠ 130 := by decide

theorem claim2 : ¬ (Audit.currentLedger.chargeA ≤ Audit.individualCap) := by decide

theorem claim3 : Audit.currentReceipt.transfer = "T7" ∧ Audit.currentReceipt.date = "2026-11-04" ∧ Audit.currentReceipt.minute = 1000 := by decide

theorem claim4 : ¬ (Audit.currentReceipt.minute ≤ Audit.receiptDeadline) := by decide

theorem claim5 : ¬ (∀ q s : Bool, q = true → (q = true ∧ s = true)) := by
  intro h
  have hs := h true false rfl
  cases hs.2

theorem claim6 : Audit.currentLedger.chargeB = 40 := by decide

end Audit
