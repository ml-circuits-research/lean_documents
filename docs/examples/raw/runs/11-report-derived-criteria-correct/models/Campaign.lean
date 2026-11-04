namespace Campaign
inductive Dispatch where | a | b | c | d deriving DecidableEq
open Dispatch
def amount : Dispatch → Int | a => 12000 | b => 18000 | c => 9000 | d => 11000
def release : Dispatch → Int | a => 5 | b => 12 | c => 12 | d => 15
def approval : Dispatch → Int | a => 4 | b => 15 | c => 16 | d => 14
def routeR2 : Dispatch → Bool | a => false | b => true | c => true | d => false
def declaration : Dispatch → Option Int | a => none | b => some 11 | c => some 11 | d => none
def checksum : Dispatch → Bool | _ => true
def listed : Dispatch → Bool | d => false | _ => true
def ordinary (x : Dispatch) : Prop := approval x < release x
def exception (x : Dispatch) : Prop := routeR2 x = true ∧ 10 ≤ release x ∧ release x ≤ 14 ∧
  match declaration x with
  | none => False
  | some t => t ≤ release x ∧ release x ≤ t + 2 ∧ release x ≤ approval x ∧ approval x ≤ release x + 3
instance (x : Dispatch) : Decidable (ordinary x) := inferInstanceAs (Decidable (approval x < release x))
instance (x : Dispatch) : Decidable (exception x) := by cases x <;> unfold exception routeR2 release declaration approval <;> infer_instance
def compliant (x : Dispatch) : Prop := ordinary x ∨ exception x
instance (x : Dispatch) : Decidable (compliant x) := by unfold compliant; infer_instance
def eligible (x : Dispatch) : Prop := compliant x ∧ checksum x = true ∧ listed x = true
instance (x : Dispatch) : Decidable (eligible x) := by unfold eligible; infer_instance
def cohortTotal : Int := amount a + amount b + amount c + amount d
def eligibleAmount (x : Dispatch) : Int := if eligible x then amount x else 0
def settlementTotal : Int := eligibleAmount a + eligibleAmount b + eligibleAmount c + eligibleAmount d

theorem total : cohortTotal = 50000 := by decide
theorem balance : (55000 : Int) - cohortTotal = 5000 := by decide
theorem bException : exception b := by decide
theorem bCompliant : compliant b := by decide
theorem cOrdinaryFails : ¬ ordinary c := by decide
theorem cExceptionFails : ¬ exception c := by decide
theorem cNoncompliant : ¬ compliant c := by decide
theorem bEligible : eligible b := by decide
theorem aEligible : eligible a := by decide
theorem cIneligible : ¬ eligible c := by decide
theorem dUnlisted : listed d = false := by decide
theorem dIneligible : ¬ eligible d := by decide
theorem eligibleExactly : ∀ x : Dispatch, eligible x ↔ x = a ∨ x = b := by intro x; cases x <;> decide
theorem settlement : settlementTotal = 30000 := by decide
theorem outsideWindow : ¬ ((10 : Int) ≤ 15 ∧ (15 : Int) ≤ 14) := by decide
-- Unobserved later incidents are deliberately not constrained by any source observation.
def laterCompatible (_ : Nat) : Prop := True
theorem laterAlternatives : laterCompatible 0 ∧ laterCompatible 1 ∧ (0 : Nat) ≠ 1 := by unfold laterCompatible; decide
-- Missing amounts have no supplied values; these nonnegative completions differ.
def populationCompletion (missingEach : Int) : Int := cohortTotal + 36 * missingEach
theorem populationAlternatives : populationCompletion 0 = 50000 ∧ populationCompletion 1 = 50036 ∧ populationCompletion 0 ≠ populationCompletion 1 := by decide
end Campaign
