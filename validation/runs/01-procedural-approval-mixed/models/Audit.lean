import Std
namespace Audit

-- Covered register events only; None represents an explicit covered absence.
structure Operation where
  start : Int
  approval : Option Int
  activeIncident : Bool
  declaration : Option Int
  countersignature : Option Int
  deriving DecidableEq

def standard (o : Operation) : Bool :=
  match o.approval with
  | none => false
  | some a => a < o.start

def emergency (o : Operation) : Bool :=
  match o.declaration, o.countersignature with
  | some d, some c => o.activeIncident && decide (d < o.start) &&
      decide (o.start ≤ c) && decide (c ≤ o.start + 1440)
  | _, _ => false

def authorized (o : Operation) : Bool := standard o || emergency o

def c101 : Operation := ⟨540, some 520, false, none, none⟩
def c102 : Operation := ⟨615, none, true, some 605, some 2055⟩
def c103 : Operation := ⟨690, some 690, false, none, none⟩
def c104 : Operation := ⟨800, none, false, none, none⟩

inductive EventKind where
  | request | approval
  deriving DecidableEq

def c102Request : EventKind := .request

theorem claim01 : standard c101 = true ∧ (520 : Int) < 540 := by decide
theorem claim02 : standard c102 = false ∧ c102Request ≠ EventKind.approval := by decide
theorem claim03 : emergency c102 = true ∧ (2055 - 615 : Int) = 1440 := by decide
theorem claim04 : standard c103 = false ∧ ¬ ((690 : Int) < 690) := by decide
theorem claim05 : c104.start = 800 ∧ standard c104 = false ∧ emergency c104 = false ∧ authorized c104 = false := by decide
theorem claim08 : standard c102 = false ∧ emergency c102 = true ∧ authorized c102 = true := by decide

-- Possible worlds for PA-06, not assertions that either world actually occurred.
structure HandoffWorld where
  packageContainsRegister : Bool
  approvalBeforeProposedStart : Bool
  deriving DecidableEq

def possibleApproved : HandoffWorld := ⟨false, true⟩
def possibleUnapproved : HandoffWorld := ⟨false, false⟩
theorem claim06Countermodels : possibleApproved.packageContainsRegister = false ∧
    possibleUnapproved.packageContainsRegister = false ∧
    possibleApproved.approvalBeforeProposedStart = true ∧
    possibleUnapproved.approvalBeforeProposedStart = false := by decide

-- Attributed witness assertions, never contradictory unconditional event axioms.
def miraAffirmsStart0900 : Bool := true
def leonDeniesStart0900 : Bool := true
theorem claim07Conflict : miraAffirmsStart0900 = true ∧ leonDeniesStart0900 = true := by decide

inductive PackageItem where
  | request | miraNote | leonNote | externalApprovalRegister
  deriving DecidableEq

def handoffPackage : List PackageItem := [.request, .miraNote, .leonNote]
theorem claim10 : PackageItem.externalApprovalRegister ∉ handoffPackage := by decide
end Audit
