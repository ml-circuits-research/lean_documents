import Std

namespace Audit

structure Operation where
  start : Nat
  approval : Option Nat
  incident : Bool
  declaration : Option Nat
  countersignature : Option Nat
deriving DecidableEq

def Standard (o : Operation) : Prop :=
  match o.approval with
  | none => False
  | some t => t < o.start

def Emergency (o : Operation) : Prop :=
  o.incident = true ∧
  (match o.declaration with
   | none => False
   | some t => t < o.start) ∧
  (match o.countersignature with
   | none => False
   | some t => o.start ≤ t ∧ t ≤ o.start + 1440)

def Authorized (o : Operation) : Prop := Standard o ∨ Emergency o

def c101 : Operation := ⟨540, some 520, false, none, none⟩
def c102 : Operation := ⟨615, none, true, some 605, some 2055⟩
def c103 : Operation := ⟨690, some 690, false, none, none⟩
def c104 : Operation := ⟨800, none, false, none, none⟩

inductive RecordKind where
  | request | approval
deriving DecidableEq

theorem c01 : Standard c101 ∧ (520 < 540) := by simp [Standard, Emergency, Authorized, c101, c102, c103, c104]
theorem c02 : c102.approval = none ∧ RecordKind.request ≠ RecordKind.approval := by simp [Standard, Emergency, Authorized, c101, c102, c103, c104]
theorem c03 : Emergency c102 ∧ c102.incident = true ∧ (605 < 615) ∧ (2055 = 615 + 1440) := by simp [Standard, Emergency, Authorized, c101, c102, c103, c104]
theorem c04 : ¬ Standard c103 ∧ c103.approval = some c103.start ∧ c103.incident = false ∧ c103.declaration = none ∧ ¬ Emergency c103 := by simp [Standard, Emergency, Authorized, c101, c102, c103, c104]
theorem c05 : c104.start = 800 ∧ ¬ Authorized c104 := by simp [Standard, Emergency, Authorized, c101, c102, c103, c104]
theorem c08 : ¬ Standard c102 ∧ Emergency c102 ∧ Authorized c102 := by simp [Standard, Emergency, Authorized, c101, c102, c103, c104]

end Audit
