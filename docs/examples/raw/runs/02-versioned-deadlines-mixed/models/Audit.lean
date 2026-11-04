import Std
namespace Audit
-- Source transcription: C01-C04; minute zero is 2028-02-20 00:00 UTC.
structure Case where
  receiptDay : Nat
  receiptMinute : Nat
  standard : Bool
  submission : Nat
  deriving DecidableEq

def at17 (day : Nat) : Nat := day * 1440 + 1020
def c201 : Case := ⟨0, 540, true, at17 10⟩
def c202 : Case := ⟨9, 1439, true, at17 19 + 1⟩
def c203 : Case := ⟨10, 0, true, at17 17⟩
def c204 : Case := ⟨11, 600, false, 21 * 1440 + 960⟩
-- V1-01/V2-01 select revision solely by accepted receipt, including the boundary.
def revision (c : Case) : Nat := if c.receiptDay * 1440 + c.receiptMinute < 10 * 1440 then 1 else 2
-- None denotes unavailable Annex R, not the absence of a deadline.
def standardDue (c : Case) : Option Nat :=
  if c.standard then some (at17 (c.receiptDay + if revision c = 1 then 10 else 7)) else none

abbrev timely (submission deadline : Nat) : Prop := submission ≤ deadline

theorem version201 : revision c201 = 1 := by decide
theorem deadline201 : standardDue c201 = some (at17 10) := by decide
theorem timely201 : standardDue c201 = some (at17 10) ∧ timely c201.submission (at17 10) := by decide
theorem version202Refuted : revision c202 ≠ 2 ∧ revision c202 = 1 := by decide
theorem deadline202 : standardDue c202 = some (at17 19) := by decide
theorem timely202Refuted : standardDue c202 = some (at17 19) ∧ ¬ timely c202.submission (at17 19) := by decide
theorem version203 : revision c203 = 2 := by decide
theorem timely203 : standardDue c203 = some (at17 17) ∧ timely c203.submission (at17 17) := by decide
theorem deadline203Refuted : standardDue c203 ≠ some (at17 16) ∧ standardDue c203 = some (at17 17) := by decide
-- These are hypothetical Annex R completions, not inferred actual deadlines.
-- Both preserve the same observed c204; supplied rules leave its Annex R duration open.
theorem restrictedDeadlineOpen : standardDue c204 = none ∧ ∃ early late : Nat, early = at17 18 ∧ late ≠ at17 18 ∧ ¬ timely c204.submission early ∧ timely c204.submission late := by
  constructor
  · decide
  · exact ⟨at17 18, at17 22, by decide, by decide, by decide, by decide⟩
end Audit
