import Std

namespace Audit

structure Payment where
  amount : Nat
  approved : Bool
  matched : Bool
  deriving DecidableEq

def p01 : Payment := ⟨120000, true, true⟩
def p02 : Payment := ⟨80000, true, true⟩
def p03 : Payment := ⟨50000, false, true⟩
def p04 : Payment := ⟨25000, false, true⟩
def sample : List Payment := [p01, p02, p03, p04]
def sampleTotal : Nat := (sample.map Payment.amount).sum
def budget : Nat := 300000
def exceptions : List Payment := sample.filter (fun p => !p.approved)
def exceptionCount : Nat := exceptions.length
def exceptionTotal : Nat := (exceptions.map Payment.amount).sum

theorem paymentTotal : sampleTotal = 275000 ∧ sampleTotal = 2750 * 100 := by decide

theorem budgetDifference : budget - sampleTotal = 25000 ∧ budget - sampleTotal ≠ 35000 ∧ sampleTotal ≤ budget := by decide

theorem sampleExceptionRate : sample.length = 4 ∧ exceptionCount = 2 ∧ exceptionCount * 100 = 50 * sample.length := by decide

theorem missingApprovalTotal : exceptionTotal = 75000 := by decide

theorem allInvoicesMatched : ∀ p ∈ sample, p.matched = true := by
  simp [sample, p01, p02, p03, p04]

theorem approvalCounterexample : p03 ∈ sample ∧ p03.matched = true ∧ p03.approved = false ∧ ¬ (∀ p ∈ sample, p.approved = true) := by
  simp [sample, p01, p02, p03, p04]

def populationExceptions (unknownExceptions : Nat) : Nat := exceptionCount + unknownExceptions

theorem populationCompletionAlternatives : populationExceptions 0 * 100 ≠ 50 * 20 ∧ populationExceptions 8 * 100 = 50 * 20 ∧ (0 : Nat) ≤ 16 ∧ (8 : Nat) ≤ 16 := by decide

theorem populationLowerBound : ∀ unknownExceptions : Nat, unknownExceptions ≤ 16 → 2 ≤ populationExceptions unknownExceptions := by
  intro unknownExceptions h
  change 2 ≤ 2 + unknownExceptions
  omega

end Audit
