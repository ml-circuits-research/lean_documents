
namespace SpendingAudit
open EvidenceLogic

structure World where
  amount : Nat
  approved : Bool

-- S1 fixes the recorded amount; S3 leaves approval unconstrained.
def dossier (w : World) : Prop := w.amount = 9
-- S2 supplies the budget rule. Amounts are nonnegative integral units.
def withinBudget (w : World) : Prop := w.amount ≤ 10
def positive (w : World) : Prop := 0 < w.amount
def approved (w : World) : Prop := w.approved = true

theorem budgetSupported : Supports dossier withinBudget := by
  constructor
  · exact ⟨⟨9, false⟩, rfl⟩
  · intro w h
    change w.amount ≤ 10
    change w.amount = 9 at h
    rw [h]
    decide

-- R1's universal rule fails at amount 11, while its actual conclusion is supported.
theorem positiveRuleRefuted : ¬ Entails positive withinBudget := by
  apply notEntailsOfCounterexample (world := World.mk 11 false)
  · change 0 < 11
    decide
  · change ¬ (11 ≤ 10)
    decide

theorem overBudgetRefuted : Refutes dossier (fun w => ¬ withinBudget w) := by
  exact ⟨budgetSupported.1, fun w h no => no (budgetSupported.2 w h)⟩

theorem approvalUnderdetermined : Underdetermined dossier approved := by
  exact ⟨⟨9, true⟩, ⟨9, false⟩, rfl, rfl, rfl, by change ¬ (false = true); decide⟩

theorem approvalNeither : ¬ Supports dossier approved ∧ ¬ Refutes dossier approved :=
  underdeterminedNeither approvalUnderdetermined

-- Exact target assertions and real axiom output, in the same checked file.
example : Supports dossier withinBudget := budgetSupported
example : ¬ Entails positive withinBudget := positiveRuleRefuted
example : Refutes dossier (fun w => ¬ withinBudget w) := overBudgetRefuted
example : Underdetermined dossier approved := approvalUnderdetermined
example : ¬ Supports dossier approved ∧ ¬ Refutes dossier approved := approvalNeither
#print axioms budgetSupported
#print axioms positiveRuleRefuted
#print axioms overBudgetRefuted
#print axioms approvalUnderdetermined
#print axioms approvalNeither
end SpendingAudit
