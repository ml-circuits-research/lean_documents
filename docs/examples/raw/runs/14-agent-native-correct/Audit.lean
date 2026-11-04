namespace SpendingCorrect

structure World where
  amount : Nat
  approved : Bool

-- Source S1 records 9 integral units; S3 leaves approval unconstrained.
def evidence (w : World) : Prop := w.amount = 9
-- Source S2 is an inclusive upper bound.
def withinBudget (w : World) : Prop := w.amount ≤ 10
def approved (w : World) : Prop := w.approved = true

theorem budget : (∃ w, evidence w) ∧ ∀ w, evidence w → withinBudget w := by
  constructor
  · exact ⟨⟨9, false⟩, rfl⟩
  · intro w h
    change w.amount = 9 at h
    change w.amount ≤ 10
    rw [h]
    decide

theorem approvalOpen : ∃ yes no, evidence yes ∧ evidence no ∧ approved yes ∧ ¬ approved no := by
  exact ⟨⟨9, true⟩, ⟨9, false⟩, rfl, rfl, rfl, by change ¬ (false = true); decide⟩

theorem approvalNeither :
    ¬ (∀ w, evidence w → approved w) ∧ ¬ (∀ w, evidence w → ¬ approved w) := by
  obtain ⟨yes, no, hy, hn, ay, an⟩ := approvalOpen
  exact ⟨fun h => an (h no hn), fun h => (h yes hy) ay⟩

-- Each delivered proof is checked at its exact intended target and audited for axioms.
example : (∃ w, evidence w) ∧ ∀ w, evidence w → withinBudget w := budget
example : ∃ yes no, evidence yes ∧ evidence no ∧ approved yes ∧ ¬ approved no := approvalOpen
example : ¬ (∀ w, evidence w → approved w) ∧ ¬ (∀ w, evidence w → ¬ approved w) := approvalNeither
#print axioms budget
#print axioms approvalOpen
#print axioms approvalNeither
end SpendingCorrect
