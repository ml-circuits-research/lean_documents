import Std
namespace Audit
-- Each Nat n in nodes denotes the exact identity Nnn, not an event count.
def nodes : List Nat := (List.range 60).map Nat.succ
theorem sixtyNodes : nodes.length = 60 ∧ nodes.Nodup ∧ nodes.head? = some 1 ∧ nodes.getLast? = some 60 := by decide
-- Common dossier-clock minutes from September1 00:00; no timezone assumption is needed.
def minuteAt (day hour minute : Nat) : Nat := (day - 1) * 1440 + hour * 60 + minute
inductive Principal where
  | ada | ben | cora | devon | emil
  deriving DecidableEq

def northAlias (t : Nat) : Principal := if t < minuteAt 21 0 0 then .ada else .ben
def active (p : Principal) (t : Nat) : Bool :=
  match p with
  | .ada => decide (t < minuteAt 31 0 0)
  | .ben => decide (minuteAt 22 0 0 ≤ t ∧ t < minuteAt 31 0 0)
  | _ => false

def revisionB (t : Nat) : Bool := decide (minuteAt 15 0 0 ≤ t)
def scope (p : Principal) (node t : Nat) : Bool :=
  match p with
  | .cora => decide (1 ≤ node ∧ node ≤ 60 ∧ t < minuteAt 31 0 0)
  | .devon => decide (41 ≤ node ∧ node ≤ 50 ∧ minuteAt 18 0 0 ≤ t ∧ t ≤ minuteAt 25 23 59)
  | .emil => decide (1 ≤ node ∧ node ≤ 60 ∧ t < minuteAt 15 0 0)
  | _ => false
structure Release where
  node : Nat
  time : Nat
  operator : Principal
  approver : Principal
  approvalTime : Option Nat
  signedApproval : Bool
  approvalScope : Bool
  permit : Bool
  deriving DecidableEq
-- EX01 modifies ordinary approval and permit only for N57 inside this exact window.
def boardWindow (node t : Nat) : Bool := decide (node = 57 ∧ minuteAt 22 9 0 ≤ t ∧ t ≤ minuteAt 22 12 0)
def boardRoute (r : Release) : Bool := boardWindow r.node r.time && active r.operator r.time && r.signedApproval && decide (r.approver = .emil) &&
  (match r.approvalTime with
  | some t => boardWindow r.node t && decide (t ≤ r.time)
  | none => false)
-- Approval scope is either computed from a stated timestamp or explicitly attested valid.
def ordinaryRoute (r : Release) : Bool := active r.operator r.time && r.signedApproval && r.approvalScope && (if revisionB r.time then decide (r.approver ≠ .emil) && r.permit else decide (r.approver = .emil))

def authorized (r : Release) : Bool := ordinaryRoute r || boardRoute r

def n04 : Release := ⟨4, minuteAt 14 10 0, .ada, .emil, some (minuteAt 14 9 0), true, scope .emil 4 (minuteAt 14 9 0), false⟩
def n01 : Release := ⟨1, minuteAt 19 10 0, .ada, .cora, some (minuteAt 19 9 0), true, scope .cora 1 (minuteAt 19 9 0), true⟩
def n57 : Release := ⟨57, minuteAt 22 10 0, .ada, .emil, some (minuteAt 22 9 0), true, false, false⟩
def n58 : Release := ⟨58, minuteAt 22 10 0, .ada, .cora, none, true, true, false⟩
def n60 : Release := ⟨60, minuteAt 20 10 0, .ada, .cora, none, true, true, true⟩

theorem historicalAuthorized : revisionB n04.time = false ∧ n04.permit = false ∧ ordinaryRoute n04 = true ∧ authorized n04 = true := by decide
def n09PermitAt (t : Nat) : Bool := decide (t ≤ minuteAt 19 23 59) || decide (minuteAt 20 0 0 ≤ t ∧ t ≤ minuteAt 20 23 59)
theorem n09PermitFailure : minuteAt 19 23 59 < minuteAt 21 10 0 ∧ minuteAt 20 23 59 < minuteAt 21 10 0 ∧ n09PermitAt (minuteAt 21 10 0) = false := by decide
theorem aliasBeforeActivation : northAlias (minuteAt 21 10 0) = Principal.ben ∧ active (northAlias (minuteAt 21 10 0)) (minuteAt 21 10 0) = false := by decide
theorem devonN41 : scope Principal.devon 41 (minuteAt 20 9 0) = true := by decide
theorem devonN51 : scope Principal.devon 51 (minuteAt 20 9 0) = false := by decide
theorem n57Exception : boardWindow n57.node n57.time = true ∧ n57.approvalTime = some (minuteAt 22 9 0) ∧ boardWindow n57.node (minuteAt 22 9 0) = true ∧ ordinaryRoute n57 = false ∧ boardRoute n57 = true ∧ authorized n57 = true := by decide
theorem n58NotCovered : boardWindow 58 (minuteAt 22 10 0) = false := by decide
theorem n58Unauthorized : minuteAt 22 9 0 < n58.time ∧ n58.time < minuteAt 22 11 0 ∧ authorized n58 = false ∧ 58 ∈ nodes := by decide
-- Any release-domain containing this actual recorded witness fails the universal claim.
theorem universalCounterexample : ∀ recorded : List Release, n58 ∈ recorded → ¬ (∀ r ∈ recorded, authorized r = true) := by
  intro recorded member universal
  have claim := universal n58 member
  have negative : authorized n58 = false := by decide
  rw [negative] at claim
  cases claim

def n59Completion (permit : Bool) : Release := ⟨59, minuteAt 22 10 0, .ada, .cora, none, true, true, permit⟩
theorem n59Open : authorized (n59Completion true) = true ∧ authorized (n59Completion false) = false := by decide
theorem n60KnownAuthorized : ordinaryRoute n60 = true ∧ authorized n60 = true := by decide

theorem n01Authorized : northAlias n01.time = Principal.ada ∧ revisionB n01.time = true ∧ ordinaryRoute n01 = true ∧ authorized n01 = true := by decide
end Audit
