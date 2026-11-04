import Init
namespace Audit
-- R01; all inventory arithmetic uses signed integer individual units.
def crate : Int := 12
def carton : Int := 6
def inboundA : Int := 8 * crate
def inboundB : Int := 2 * carton
def dispatchedA : Int := 5 * crate
def deliveredA : Int := 4 * crate
def returnedA : Int := crate
def bookA : Int := 100 + inboundA - dispatchedA + returnedA
def availableA : Int := bookA - 7
def bookB : Int := 40 + inboundB - 2 * carton
def availableB : Int := bookB - 8
def requestedB : Int := 3 * carton
def deliveredB : Int := 2 * carton
inductive Lot where | a | b | c | d

theorem claim01 : inboundA = 96 := by decide
theorem claim02 : inboundB ≠ 24 := by decide
theorem claim03 : bookA ≠ 136 := by decide
theorem claim04 : availableA ≠ 148 := by decide
theorem claim05 : bookB ≠ 34 ∧ deliveredB ≠ requestedB := by decide
theorem claim06 : availableB = 32 := by decide
theorem claim07 : deliveredA ≠ dispatchedA := by decide
theorem claim08 : deliveredB ≠ requestedB := by decide
-- C's explicit incomplete reconciliation is the named factual premise.
theorem claim12 : ∀ (reconciled : Lot → Prop),
    ¬ reconciled .c → ¬ (∀ lot, reconciled lot) := by
  intro reconciled incomplete all
  exact incomplete (all .c)
theorem claim13 : bookB - 7 ≠ availableB := by decide
end Audit
