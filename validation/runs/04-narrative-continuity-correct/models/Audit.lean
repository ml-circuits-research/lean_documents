import Std

namespace Audit

def dawn : Nat := 0
def noon : Nat := 1
def evening : Nat := 2
def instant (day phase : Nat) : Nat := 3 * day + phase

def beginning : Nat := instant 1 dawn
def ending : Nat := instant 10 evening
def deathTime : Nat := instant 5 dawn
def revivalTime : Nat := instant 8 dawn

def AliveAt (time : Nat) : Prop :=
  (beginning ≤ time ∧ time < deathTime) ∨
  (revivalTime ≤ time ∧ time ≤ ending)

def DeadAt (time : Nat) : Prop := deathTime ≤ time ∧ time < revivalTime

theorem keyExchangeAlive : AliveAt (instant 2 noon) := by
  simp [AliveAt, DeadAt, instant, beginning, ending, deathTime, revivalTime, dawn, noon, evening]

theorem daySixDead : DeadAt (instant 6 noon) ∧ ¬ AliveAt (instant 6 noon) := by
  simp [AliveAt, DeadAt, instant, beginning, ending, deathTime, revivalTime, dawn, noon, evening]

theorem daySixNoPhysicalAttendance : ∀ attends : Prop, (attends → AliveAt (instant 6 noon)) → ¬ attends := by
  intro attends requiredAlive attendance
  exact daySixDead.2 (requiredAlive attendance)

theorem revivalAndNoonLife : revivalTime = instant 8 dawn ∧ AliveAt (instant 8 dawn) ∧ AliveAt (instant 8 noon) ∧ instant 8 dawn < instant 8 noon := by
  simp [AliveAt, DeadAt, instant, beginning, ending, deathTime, revivalTime, dawn, noon, evening]

end Audit
