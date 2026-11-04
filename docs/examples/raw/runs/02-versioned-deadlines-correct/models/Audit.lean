import Std
namespace Audit
inductive Revision where
  | one | two
  deriving DecidableEq
inductive CaseClass where
  | standard | restricted
  deriving DecidableEq
structure Case where
  received : Nat
  assigned : Nat
  submitted : Nat
  kind : CaseClass
  deriving DecidableEq

def boundary : Nat := 14400

def revision (c : Case) : Revision :=
  if c.received < boundary then .one else .two

def days (r : Revision) : Nat :=
  match r with
  | .one => 10
  | .two => 7

-- None means this standard rule is inapplicable, not that no actual deadline exists.
def standardDeadline (c : Case) : Option Nat :=
  match c.kind with
  | .restricted => none
  | .standard => some ((c.received / 1440 + days (revision c)) * 1440 + 1020)

def d201 : Case := ⟨540, 14880, 15420, .standard⟩
def d202 : Case := ⟨14399, 14910, 28381, .standard⟩
def d203 : Case := ⟨14400, 14925, 25500, .standard⟩
def d204 : Case := ⟨16440, 16500, 31200, .restricted⟩

def withAssignment (c : Case) (a : Nat) : Case := { c with assigned := a }

theorem claim01 : revision d201 = .one ∧ standardDeadline d201 = some 15420 ∧ d201.submitted = 15420 ∧ d201.submitted ≤ 15420 := by decide
theorem claim02 : revision d202 = .one ∧ d202.received + 1 = boundary ∧ (∀ a, revision (withAssignment d202 a) = .one) := by
  refine ⟨by decide, by decide, ?_⟩
  intro a
  rfl
theorem claim03 : standardDeadline d202 = some 28380 ∧ 28380 < d202.submitted := by decide
theorem claim04 : d203.received = boundary ∧ revision d203 = .two ∧ standardDeadline d203 = some 25500 ∧ d203.submitted = 25500 ∧ d203.submitted ≤ 25500 := by decide

def activeAtExport : Revision := .two
def dashboard (_c : Case) : Revision := activeAtExport
theorem claim05 : dashboard d201 = .two ∧ dashboard d202 = .two ∧ dashboard d203 = .two ∧ dashboard d204 = .two ∧ dashboard d201 ≠ revision d201 ∧ dashboard d202 ≠ revision d202 := by decide
theorem claim06 : d204.kind = .restricted ∧ revision d204 = .two ∧ standardDeadline d204 = none := by decide

-- Hypothetical completions, not purported contents of the missing annex.
structure Completion where
  annexTransferred : Bool
  due : Nat
  deriving DecidableEq

def timelyCompletion : Completion := ⟨false, 31260⟩
def lateCompletion : Completion := ⟨false, 29820⟩
theorem claim07Alternatives : timelyCompletion.annexTransferred = false ∧ lateCompletion.annexTransferred = false ∧ timelyCompletion.due ≠ lateCompletion.due ∧ d204.submitted ≤ timelyCompletion.due ∧ lateCompletion.due < d204.submitted := by decide

inductive PauseEvidence where
  | request | approval
  deriving DecidableEq

def suppliedPauseEvidence : List PauseEvidence := [.request]
theorem claim08 : PauseEvidence.request ∈ suppliedPauseEvidence ∧ PauseEvidence.approval ∉ suppliedPauseEvidence := by decide
end Audit
