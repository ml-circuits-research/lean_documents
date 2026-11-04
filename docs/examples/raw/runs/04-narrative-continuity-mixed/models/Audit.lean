import Init

namespace Audit

-- Integer hours measured from the beginning of day 1. Only named story
-- instants and interval ordering are used; no hourly event completeness claim.
def tick (day hour : Nat) : Nat := (day - 1) * 24 + hour
def deathTime : Nat := tick 5 6
def revivalTime : Nat := tick 8 6
def endTime : Nat := tick 11 0

-- R-01 with T-01, T-02 and complete R-02 yields this dead interval.
def DeadAt (t : Nat) : Prop := deathTime ≤ t ∧ t < revivalTime
-- Positive life facts only; this predicate is NOT an exhaustive living catalog.
def ConfirmedAliveAt (t : Nat) : Prop :=
  t = tick 2 12 ∨ (revivalTime ≤ t ∧ t ≤ endTime)

def keyStoryTime : Nat := tick 2 12
def narrationFrameTime : Nat := tick 7 18

inductive Person where
  | mira | ivo
  deriving DecidableEq
inductive Utterance where
  | neverDied
  deriving DecidableEq
structure Speech where
  speaker : Person
  time : Nat
  words : Utterance
  deriving DecidableEq
-- Speech data has no coercion to a world-fact predicate.
def miraSpeech : Speech := ⟨.mira, tick 9 12, .neverDied⟩

-- Positive death evidence suffices to refute a universal absence assertion;
-- this list carries NO assertion of completeness for other deaths.
def recordedDeaths : List Nat := [deathTime]
-- Complete only for Mira during days 1 through 10 (R-02).
def revivals : List Nat := [revivalTime]

def NeverDiedBefore9 : Prop :=
  ∀ t ∈ recordedDeaths, ¬ t < tick 9 0

def AlwaysDeadAfter5 : Prop :=
  ∀ t : Nat, deathTime < t → t ≤ endTime → DeadAt t

def NoRevivalBefore6 : Prop :=
  ∀ t ∈ revivals, ¬ (deathTime < t ∧ t < tick 6 12)

theorem claim01 : keyStoryTime = tick 2 12 ∧ ConfirmedAliveAt keyStoryTime := by
  exact ⟨rfl, Or.inl rfl⟩

-- Physical attendance requires life; life and death are exclusive.
-- The only hypothesis is the independently sourced necessary condition.
theorem claim02 : ∀ (attendance : Prop),
    (attendance → ¬ DeadAt (tick 6 12)) → ¬ attendance := by
  intro attendance requiresNotDead occurs
  exact (requiresNotDead occurs) (by unfold DeadAt deathTime revivalTime tick; decide)

theorem claim03 : ¬ keyStoryTime / 24 + 1 = 7 := by decide

theorem claim04 : miraSpeech.speaker = Person.mira ∧
    miraSpeech.time = tick 9 12 ∧ miraSpeech.words = Utterance.neverDied := by
  exact ⟨rfl, rfl, rfl⟩

theorem claim05 : ¬ NeverDiedBefore9 := by
  intro never
  exact never deathTime (by simp [recordedDeaths]) (by decide)

theorem claim06 : ConfirmedAliveAt (tick 8 12) := by
  exact Or.inr (by decide)

theorem claim07 : ¬ AlwaysDeadAfter5 := by
  intro always
  have dead := always (tick 8 12) (by decide) (by decide)
  have living : ¬ DeadAt (tick 8 12) := by unfold DeadAt deathTime revivalTime tick; decide
  exact living dead

theorem claim10 : NoRevivalBefore6 := by
  intro t member
  have same : t = revivalTime := by simpa [revivals] using member
  subst t
  decide

end Audit
