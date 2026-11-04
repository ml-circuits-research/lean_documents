import Init
namespace Audit
inductive Unit where | l01 | n01 | n02 | n03 | e17 | c01
  deriving DecidableEq
-- Threshold selection is source-linked to event revision, profile and Annex X.
def threshold : Unit → Nat
  | .l01 => 120 | .e17 => 110 | .c01 => 150 | _ => 100
def observations : Unit → List Nat
  | .l01 => [110,115,118] | .n01 => [92,95,99] | .n02 => [90,97,101]
  | .e17 => [104,108,106] | .c01 => [142,145,149] | .n03 => [94]
def within (u : Unit) : Bool := (observations u).all (fun n => decide (n ≤ threshold u))
def normal (u : Unit) : Bool := u != .c01
def annexApplies (u : Unit) : Bool := u == .e17
-- Day ordinal within June; dates differ, so exact within-day time cannot reverse order.
def k2ExpiryDay : Nat := 1
def n03RunDay : Nat := 3
def x99Valid : Bool := false
def release (delay calibration channels faults signature : Bool) : Bool :=
  delay && calibration && channels && faults && signature

theorem claim01 : within .l01 = true := by decide
theorem claim02 : within .n02 = false := by decide
theorem claim03 : within .n01 = true := by decide
theorem claim04 : ¬ (∀ u, normal u = true → within u = true) := by
  intro all
  have wrong := all .n02 (by decide)
  contradiction
theorem claim05 : within .e17 = true := by decide
theorem claim06 : annexApplies .n02 = false := by decide
theorem claim07 : within .c01 = true := by decide
theorem claim09 : ¬ n03RunDay ≤ k2ExpiryDay := by decide
theorem claim10 : x99Valid ≠ true := by decide
theorem claim11 : ¬ (∀ c b f s : Bool, release true c b f s = true) := by
  intro sufficient
  have wrong := sufficient true true false true
  contradiction
end Audit
