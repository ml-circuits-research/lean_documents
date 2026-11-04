import Std

namespace Settlement

/-- Nonnegative integer minute offsets and explicit approval/case flags. -/
structure Pause where
  start : Nat
  stop : Nat
  approved : Bool
  inCase : Bool

def covers (p : Pause) (minute : Nat) : Bool :=
  p.approved && p.inCase && decide (p.start ≤ minute ∧ minute < p.stop)

/-- Enumerate the bounded gross window once, counting union membership once. -/
def unionMinutes (gross : Nat) (pauses : List Pause) : Nat :=
  ((List.range gross).filter (fun minute => pauses.any (fun p => covers p minute))).length

def a : Pause := ⟨20, 40, true, true⟩
def b : Pause := ⟨30, 50, true, true⟩
def c : Pause := ⟨50, 60, true, true⟩
def z : Pause := ⟨60, 60, true, true⟩
def x : Pause := ⟨70, 80, true, false⟩
def y : Pause := ⟨190, 200, true, true⟩
def inventory : List Pause := [a, b, c, z, x, y]
def actualGross : Nat := 180

def chargeable (gross : Nat) : Nat := gross - unionMinutes gross inventory
def meets (gross : Nat) : Prop := chargeable gross ≤ 140
instance (gross : Nat) : Decidable (meets gross) := inferInstanceAs (Decidable (chargeable gross ≤ 140))

/-- A generic half-open touching-boundary law, independent of dossier values. -/
theorem touching_union (lo mid hi minute : Nat) (ordered₁ : lo ≤ mid) (ordered₂ : mid ≤ hi) :
    ((lo ≤ minute ∧ minute < mid) ∨ (mid ≤ minute ∧ minute < hi)) ↔
      (lo ≤ minute ∧ minute < hi) := by omega

theorem empty_interval (point minute : Nat) : ¬ (point ≤ minute ∧ minute < point) := by omega

theorem overlap30 : unionMinutes 180 [a,b] = 30 := by decide
theorem overlapNot40 : unionMinutes 180 [a,b] ≠ 40 := by decide
theorem touching40 : unionMinutes 180 [a,b,c] = 40 := by decide
theorem touchingNot41 : unionMinutes 180 [a,b,c] ≠ 41 := by decide
theorem actual40 : unionMinutes actualGross inventory = 40 := by decide
theorem actualNot51 : unionMinutes actualGross inventory ≠ 51 := by decide
theorem exactDeadline : meets actualGross := by decide
theorem falseGross : actualGross ≠ 130 := by decide
theorem extensionFails : ¬ meets 181 := by decide

/-- Exact nearest-cent rounding for signed mills, with half ties away from zero. -/
def roundCents (mills : Int) : Int :=
  let magnitude := (mills.natAbs + 5) / 10
  if mills < 0 then -(Int.ofNat magnitude) else Int.ofNat magnitude

def invoiceLines : List Int := [1005, 1005, -1000]
def invoiceTotal : Int := (invoiceLines.map roundCents).sum

theorem positiveTie : roundCents 1005 = 101 := by decide
theorem positiveNot100 : roundCents 1005 ≠ 100 := by decide
theorem negativeTie : roundCents (-1005) = -101 := by decide
theorem negativeNot100 : roundCents (-1005) ≠ -100 := by decide
theorem invoice102 : invoiceTotal = 102 := by decide
theorem invoiceNot101 : invoiceTotal ≠ 101 := by decide
theorem aggregateIs101 : roundCents invoiceLines.sum = 101 := by decide

/-- A threshold model only; no prior-quarter count is asserted as actual. -/
def historicalThresholdMet (breaches : Nat) : Prop := 3 ≤ breaches

theorem historicalAlternatives : (¬ historicalThresholdMet 0) ∧ historicalThresholdMet 3 := by
  unfold historicalThresholdMet
  decide

end Settlement
