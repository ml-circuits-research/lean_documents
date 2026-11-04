import Std
namespace Audit
-- L-02 gives exact integer cents and approval status at the cutoff.
structure Payment where
  id : String
  cents : Nat
  approved : Bool
  deriving DecidableEq

def p03ID : String := "P03"
def p04ID : String := "P04"

def sample : List Payment :=
  [⟨"P01", 120000, true⟩, ⟨"P02", 80000, true⟩,
   ⟨"P03", 50000, false⟩, ⟨"P04", 25000, false⟩]
def total (xs : List Payment) : Nat := (xs.map Payment.cents).sum
def exceptions : List Payment := sample.filter (fun p => !p.approved)
def exceptionIDs : List String := exceptions.map Payment.id
def budget : Nat := 300000
-- L-01 and M-01 identify 16 unsampled population entries, with unknown status.
def populationExceptions (unsampledMissing : Nat) : Nat := exceptions.length + unsampledMissing

theorem sampleTotal : total sample = 275000 := by decide
theorem budgetDifference : total sample ≤ budget ∧ budget - total sample = 25000 := by decide
theorem exactExceptions : sample.length = 4 ∧ exceptions.length = 2 ∧ exceptionIDs = [p03ID, p04ID] := by decide
theorem exceptionTotal : total exceptions = 75000 := by decide
-- Nonzero denominator and exact cross multiplication encode 50 percent.
theorem sampleRate : 0 < sample.length ∧ exceptions.length * 100 = sample.length * 50 := by decide
-- The lower bound holds for every possible assignment of the 16 unknown statuses.
theorem populationLowerBound : ∀ unsampledMissing : Nat, unsampledMissing ≤ 16 → 2 ≤ populationExceptions unsampledMissing ∧ populationExceptions unsampledMissing ≤ 18 := by
  intro unsampledMissing bound
  change 2 ≤ 2 + unsampledMissing ∧ 2 + unsampledMissing ≤ 18
  omega
end Audit
