import Std
namespace Audit
-- Integer cents unless explicitly encoded as numerator/denominator euros.
def roundCents (num den : Nat) : Nat := (num * 200 + den) / (den * 2)
def threshold (revision : Nat) : Nat := if revision = 1 then 2000000 else 2500000
def revisionAt (receiptMinute : Int) : Nat := if receiptMinute < 0 then 1 else 2
-- Origin: 2029-06-01 00:00 UTC. Same-project/supplier/requirement facts are explicit L02 facts.
def rackAggregates : Bool := true && true && true && decide (19 ≤ 2 + 29) && decide ((-4 : Int) < 2)
def rackTotal : Nat := 1240000 + 1260000
def competitionSatisfied (rev value : Nat) (certificate exception : Bool) : Bool :=
  decide (value < threshold rev) || certificate || exception
def compliant (competition approval : Bool) : Bool := competition && approval

theorem rackObligation : rackAggregates = true ∧ rackTotal = 2500000 ∧ threshold (revisionAt 540) ≤ rackTotal ∧ competitionSatisfied 2 rackTotal false false = false := by decide
theorem rackSum : rackTotal = 2500000 := by decide
-- V05 exact USD 27777775/1000 times 9/10 euros/USD.
def p13Num : Nat := 27777775 * 9
def p13Den : Nat := 1000 * 10
def p13Cents : Nat := roundCents p13Num p13Den
theorem p13Normalization : p13Num = 249999975 ∧ p13Den = 10000 ∧ p13Cents = 2500000 ∧ threshold 2 ≤ p13Cents ∧ (9 : Nat) < 11 ∧ competitionSatisfied 2 p13Cents true false = true := by decide
theorem p13Intermediate : p13Num = 249999975 ∧ p13Den = 10000 ∧ p13Num < 25000 * p13Den ∧ ¬ p13Cents < threshold 2 := by decide
theorem p14Normalization : roundCents 24999994 1000 = 2499999 ∧ roundCents 24999994 1000 < threshold 2 := by decide

-- D01-D03 category, value and expiry are all required at the approval instant.
def expiry : Nat := 14 * 1440 + 1020
abbrev validDana (consumables : Bool) (value approval commitment : Nat) : Prop :=
  consumables = true ∧ value ≤ 1500000 ∧ approval ≤ expiry ∧ approval < commitment
-- Nat approval offsets are at/after the delegation's June 1 start.
theorem p15Approval : validDana true 1490000 expiry (expiry + 1) := by decide
def p16ValidApproval : Bool := decide (validDana true 1500000 (expiry + 1) (expiry + 10)) || false
theorem p16ApprovalFailure : 1500000 ≤ 1500000 ∧ ¬ validDana true 1500000 (expiry + 1) (expiry + 10) ∧ p16ValidApproval = false := by decide

def r17AddedRequirement : Bool := false
def r17PriceIncrease : Bool := false
theorem r17Version : revisionAt (-1) = 1 ∧ r17AddedRequirement = false ∧ r17PriceIncrease = false := by decide
theorem r17CompetitionFailure : threshold (revisionAt (-1)) < 2250000 ∧ competitionSatisfied 1 2250000 false false = false ∧ compliant (competitionSatisfied 1 2250000 false false) true = false := by decide
theorem r18NoCompetition : revisionAt 0 = 2 ∧ 2250000 < threshold (revisionAt 0) ∧ competitionSatisfied 2 2250000 false false = true := by decide

def e19Declaration : Nat := 21 * 1440 + 585
def e19Commitment : Nat := 21 * 1440 + 600
def e19Review : Nat := 23 * 1440 + 600
abbrev urgentException (active declarationExists reviewExists : Bool) (declaration commitment review : Nat) : Prop :=
  active = true ∧ declarationExists = true ∧ reviewExists = true ∧ declaration < commitment ∧ commitment ≤ review ∧ review ≤ commitment + 48 * 60
theorem e19Exception : urgentException true true true e19Declaration e19Commitment e19Review ∧ e19Review - e19Commitment = 48 * 60 ∧ e19Declaration < e19Commitment := by decide
theorem urgencyInsufficient : ¬ urgentException true false false e19Declaration e19Commitment e19Review := by decide

inductive CompatibilityTest where
  | warranty | physical
  deriving DecidableEq
-- Two possible governing tests, not an assertion about the missing Annex Q.
def onlyCompatible : CompatibilityTest → Bool
  | .warranty => true
  | .physical => false
theorem compatibilityOpen : onlyCompatible .warranty = true ∧ onlyCompatible .physical = false := by decide

structure ApprovalStatement where
  order : Nat
  dateOffset : Nat
  approvalMinute : Nat
  asserted : Bool
  retracted : Bool
  deriving DecidableEq
def mara : ApprovalStatement := ⟨21, 26, 600, true, false⟩
def tomas : ApprovalStatement := ⟨21, 26, 600, false, false⟩
theorem approvalConflict : mara.order = tomas.order ∧ mara.dateOffset = tomas.dateOffset ∧ mara.approvalMinute = tomas.approvalMinute ∧ mara.asserted ≠ tomas.asserted ∧ mara.retracted = false ∧ tomas.retracted = false := by decide

structure PaymentWorld where
  invoice : Bool
  delivery : Bool
  paid : Bool
theorem paymentOpen : ∀ paid : Bool, ∃ w : PaymentWorld, w.invoice = true ∧ w.delivery = true ∧ w.paid = paid := by
  intro paid
  exact ⟨⟨true, true, paid⟩, rfl, rfl, rfl⟩

theorem objectiveFailures : compliant (competitionSatisfied 2 rackTotal false false) true = false ∧ compliant (competitionSatisfied 1 2250000 false false) true = false ∧ compliant (competitionSatisfied 2 1500000 false false) false = false := by decide
end Audit
