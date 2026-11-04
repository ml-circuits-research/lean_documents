namespace Audit
inductive Route where
  | r1 | r2
  deriving DecidableEq
inductive Destination where
  | north | south | east
  deriving DecidableEq
structure Dispatch where
  amount : Int
  route : Route
  released : Int
  declaration : Option Int
  approved : Int
  passed : Bool
  destination : Destination
  deriving DecidableEq

def a : Dispatch := ⟨12000, .r1, 5, none, 4, true, .north⟩
def b : Dispatch := ⟨18000, .r2, 12, some 11, 15, true, .south⟩
def c : Dispatch := ⟨9000, .r2, 12, some 11, 16, true, .north⟩
def d : Dispatch := ⟨11000, .r1, 15, none, 14, true, .east⟩
def cohort : List Dispatch := [a,b,c,d]
def window (day : Int) : Prop := 10 ≤ day ∧ day ≤ 14
instance (day : Int) : Decidable (window day) := inferInstanceAs (Decidable (10 ≤ day ∧ day ≤ 14))
def ordinary (x : Dispatch) : Prop := x.approved < x.released
instance (x : Dispatch) : Decidable (ordinary x) := inferInstanceAs (Decidable (x.approved < x.released))
def exception (x : Dispatch) : Prop :=
  x.route = .r2 ∧ window x.released ∧
  (match x.declaration with
   | none => False
   | some day => day ≤ x.released ∧ x.released ≤ day + 2) ∧
  x.released ≤ x.approved ∧ x.approved ≤ x.released + 3
instance (x : Dispatch) : Decidable (exception x) := by
  unfold exception
  cases x.declaration <;> infer_instance
def compliant (x : Dispatch) : Prop := ordinary x ∨ exception x
instance (x : Dispatch) : Decidable (compliant x) := inferInstanceAs (Decidable (ordinary x ∨ exception x))
def listed (dest : Destination) : Prop := dest = .north ∨ dest = .south
instance (dest : Destination) : Decidable (listed dest) := inferInstanceAs (Decidable (dest = .north ∨ dest = .south))
def eligible (x : Dispatch) : Prop := compliant x ∧ x.passed = true ∧ listed x.destination
instance (x : Dispatch) : Decidable (eligible x) := inferInstanceAs (Decidable (compliant x ∧ x.passed = true ∧ listed x.destination))
def total : Int := (cohort.map Dispatch.amount).sum
def balance : Int := 55000 - total
def eligibleTotal : Int := ((cohort.filter (fun x => decide (eligible x))).map Dispatch.amount).sum

theorem expenditure : total = 50000 := by decide
theorem headroom : balance = 5000 ∧ balance ≠ 6000 := by decide
theorem bApproval : compliant b := by decide
theorem bException : ¬ ordinary b ∧ exception b := by decide
theorem cApproval : ¬ compliant c := by decide
theorem cDelay : c.approved - c.released = 4 := by decide
theorem bEligible : eligible b := by decide
theorem passInsufficient : d ∈ cohort ∧ d.passed = true ∧ ¬ eligible d := by decide
theorem notAllPrior : ¬ (∀ x ∈ cohort, ordinary x) := by decide
theorem releaseWindow : ¬ window 15 := by decide
theorem settlement : eligibleTotal = 30000 ∧ eligibleTotal ≠ 39000 := by decide
theorem eligibleMembers : eligible a ∧ eligible b ∧ ¬ eligible c ∧ ¬ eligible d := by decide

-- Statements are attributed records, never simultaneous event axioms.
inductive Record where
  | receiving | incident
  deriving DecidableEq
def saysAccepted : Record → Bool
  | .receiving => true
  | .incident => false
theorem recordConflict : saysAccepted .receiving = true ∧ saysAccepted .incident = false := by decide

-- Unobserved values are deliberately independent of the fixed cohort facts.
structure Extension where
  laterIncidents : Nat
  otherAmounts : List Int
def compatible (w : Extension) : Prop := w.otherAmounts.length = 36
instance (w : Extension) : Decidable (compatible w) := inferInstanceAs (Decidable (w.otherAmounts.length = 36))
def quiet : Extension := ⟨0, List.replicate 36 0⟩
def incident : Extension := ⟨1, List.replicate 36 0⟩
def extraAmount : Extension := ⟨0, 1 :: List.replicate 35 0⟩
def populationTotal (w : Extension) : Int := total + w.otherAmounts.sum
theorem laterNonentailment : compatible quiet ∧ compatible incident ∧ quiet.laterIncidents = 0 ∧ incident.laterIncidents ≠ 0 := by decide
theorem populationNonentailment : compatible quiet ∧ compatible extraAmount ∧ populationTotal quiet = 50000 ∧ populationTotal extraAmount ≠ 50000 := by decide
end Audit
