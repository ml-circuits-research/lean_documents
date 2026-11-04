import Std
namespace Audit
inductive Serial where
  | l01 | n01 | n02 | n03 | e17 | c01 | x99
  deriving DecidableEq
inductive Profile where
  | normal | cold | hot
  deriving DecidableEq

def revision (minute : Int) : Nat := if minute < 0 then 1 else 2
def baseLimit (r : Nat) (p : Profile) (temp : Int) : Option Nat :=
  if p = .normal ∧ 10 ≤ temp ∧ temp ≤ 30 then
    if r = 1 then some 120 else some 100
  else if r = 2 ∧ p = .cold ∧ 0 ≤ temp ∧ temp ≤ 9 then some 150 else none

def exceptionApplies (s : Serial) (p : Profile) (temp minute : Int) : Bool :=
  decide (s = .e17 ∧ p = .normal ∧ 10 ≤ temp ∧ temp ≤ 30 ∧ 1980 ≤ minute ∧ minute ≤ 5400)
def limitAt (s : Serial) (p : Profile) (temp minute : Int) : Option Nat :=
  if exceptionApplies s p temp minute then some 110 else baseLimit (revision minute) p temp

def l01 : List Nat := [110, 115, 118]
def n01 : List Nat := [92, 95, 99]
def n02 : List Nat := [90, 97, 101]
def e17 : List Nat := [104, 108, 106]
def c01 : List Nat := [142, 145, 149]
def within (xs : List Nat) (limit : Nat) : Bool := xs.all (fun n => decide (n ≤ limit))
def maximum (xs : List Nat) : Nat := xs.foldl max 0

theorem claim01Arithmetic : l01.length = 3 ∧ within l01 120 = true ∧ maximum l01 = 118 ∧ maximum l01 < 120 ∧ 120 - maximum l01 = 2 := by decide
theorem claim02 : ∀ t : Int, 2880 ≤ t → t ≤ 4319 → revision t = 2 := by
  intro t lo hi
  have h : ¬ t < 0 := by omega
  simp [revision, h]
theorem claim03 : baseLimit 2 .normal 20 = some 100 ∧ n01.length = 3 ∧ within n01 100 = true := by decide
theorem claim04 : (101 : Nat) ∈ n02 ∧ 100 < (101 : Nat) ∧ within n02 100 = false := by decide
theorem e17Applicable : ∀ t : Int, 2880 ≤ t → t ≤ 4319 → limitAt .e17 .normal 20 t = some 110 := by
  intro t lo hi
  have hlo : 1980 ≤ t := by omega
  have hhi : t ≤ 5400 := by omega
  simp [limitAt, exceptionApplies, hlo, hhi]
theorem claim05 : e17.length = 3 ∧ within e17 110 = true ∧ maximum e17 = 108 := by decide
theorem claim06 : ∀ p temp t, exceptionApplies .n02 p temp t = false := by
  intro p temp t
  simp [exceptionApplies]
theorem claim07 : baseLimit 2 .cold 5 = some 150 ∧ c01.length = 3 ∧ within c01 150 = true := by decide

inductive Attempt where
  | measured (value : Nat) | aborted | absent | invalid (value : Nat)
  deriving DecidableEq

def validMeasurement (a : Attempt) : Option Nat :=
  match a with
  | .measured n => some n
  | _ => none

def n03First : Attempt := .measured 94
def n03Second : Attempt := .aborted
def n03Third : Attempt := .absent
def n03ChannelBAvailable : Bool := false
def x99 : Attempt := .invalid 85

theorem claim08 : n03ChannelBAvailable = false ∧ n03Second = .aborted ∧ n03Third = .absent ∧ validMeasurement n03Third = none := by decide
theorem claim09 : ∀ t : Int, 2880 ≤ t → t ≤ 4319 → (1439 : Int) < t := by
  intro t lo hi
  omega
theorem claim10 : x99 = .invalid 85 ∧ validMeasurement x99 = none := by decide

def releaseRoute (delay calibration channels faults signature : Bool) : Bool :=
  delay && calibration && channels && faults && signature
theorem claim11 : releaseRoute true false true true true = false ∧ ¬ (∀ calibration channels faults signature, releaseRoute true calibration channels faults signature = true) := by decide

theorem sufficientRoute (Route Demonstration : Prop) (rule : Route → Demonstration) (route : Route) : Demonstration := rule route
theorem converseNotEntailed : (False → True) ∧ ¬ (True → False) := by
  constructor
  · intro h
    exact h.elim
  · intro h
    exact h True.intro

inductive Signer where
  | sera | oren | mara
  deriving DecidableEq

def authorizedReleaseSigner (s : Signer) : Bool := s == .sera
def releaseSignatures : List (Serial × Signer) := [(.n01, .sera), (.e17, .sera), (.c01, .sera)]
theorem claim13 : (Serial.n01, Signer.sera) ∈ releaseSignatures ∧ (Serial.e17, Signer.sera) ∈ releaseSignatures ∧ (Serial.c01, Signer.sera) ∈ releaseSignatures ∧ authorizedReleaseSigner .sera = true := by decide
theorem claim14 : ∀ temp, baseLimit 1 .hot temp = none ∧ baseLimit 2 .hot temp = none := by
  intro temp
  simp [baseLimit]
end Audit
