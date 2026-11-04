import Init
namespace Audit
-- G02 route conjunctions. Arguments are factual predicates, not missing defaults.
def routeA (credential localApproval : Bool) : Bool := credential && localApproval
def routeB (credential scopedApproval permit : Bool) : Bool := credential && scopedApproval && permit
-- Named N58 event: valid credential and Cora approval, affirmatively revoked permit.
def n58Authorized : Bool := routeB true true false
-- N09 release day 21 lies after both listed operative permit windows.
def p09Covers (day : Nat) : Bool := decide (day ≤ 19) || decide (day = 20)
inductive Principal where | ada | ben
  deriving DecidableEq
def northOperator (day : Nat) : Principal := if day ≤ 20 then .ada else .ben
-- Specific interior-date checks; boundaries in the source remain inclusive.
def delegated (node day : Nat) : Bool := decide (41 ≤ node ∧ node ≤ 50 ∧ 18 ≤ day ∧ day ≤ 25)
def boardScope (node day hour : Nat) : Bool := decide (node = 57 ∧ day = 22 ∧ 9 ≤ hour ∧ hour ≤ 12)
def exceptionRoute (node day hour : Nat) (credential localApproval : Bool) : Bool :=
  boardScope node day hour && credential && localApproval
-- Necessary source-review prerequisite, not a complete characterization of reuse.
def reviewRequirement (sourceChanged dependenciesReviewed : Bool) : Bool :=
  !sourceChanged || dependenciesReviewed

theorem claim01 : n58Authorized = false := by decide
theorem claim02 : routeA true true = true := by decide
theorem claim03 : p09Covers 21 = false := by decide
theorem claim04 : northOperator 21 ≠ Principal.ada := by decide
theorem claim05 : delegated 41 20 = true := by decide
theorem claim06 : delegated 51 20 = false ∧ routeB true (delegated 51 20) true = false := by decide
theorem claim07 : exceptionRoute 57 22 10 true true = true := by decide
theorem claim08 : boardScope 58 22 10 = false := by decide
theorem claim09 : (9 : Nat) < 10 ∧ 10 < 11 := by decide
theorem claim13 : ∃ reportUnchanged : Bool, reportUnchanged = true ∧ reviewRequirement true false = false := by
  exact ⟨true, rfl, rfl⟩
end Audit
