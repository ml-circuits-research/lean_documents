import Std

namespace Stock

inductive Status where
  | active | quarantined | archived
  deriving DecidableEq

structure Row where
  quantity : Nat
  status : Status
  signed : Bool
  deriving DecidableEq

-- Each row comes from its original HTML paragraph, lines 9 through 11.
def a : Row := ⟨18, .active, true⟩
def b : Row := ⟨27, .quarantined, true⟩
def c : Row := ⟨15, .archived, false⟩
def rows : List Row := [a, b, c]

-- Current-population completeness is asserted at original line 6 only.
def counted (row : Row) : Bool :=
  row.status == .active || row.status == .quarantined

def total : Nat := ((rows.filter counted).map Row.quantity).sum

abbrev eligible (row : Row) : Prop :=
  row.status = .active ∧ row.signed = true

-- True means an earlier clearance existed; neither value is asserted by sources.
abbrev currentEvidence (_history : Bool) : Prop := total = 45 ∧ eligible a

abbrev noPriorClearance (history : Bool) : Prop := history = false

end Stock
