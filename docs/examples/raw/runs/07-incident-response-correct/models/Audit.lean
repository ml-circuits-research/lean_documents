import Std
namespace Audit
-- UTC integer-minute origin 2030-10-27 00:00; numerical offsets are literal.
def utc (localMinute offsetMinute : Int) : Int := localMinute - offsetMinute
def warningA : Int := utc 90 120
def detectionA : Int := utc 120 120
def containmentA : Int := utc 200 60
def acknowledgementA : Int := utc 132 120
def detectionB : Int := utc 250 60
def acknowledgementB : Int := utc 285 60
def detectionC : Int := utc 110 120
def revision (detection : Int) : Nat := if detection < 0 then 1 else 2
def pauseCap (rev : Nat) : Int := if rev = 1 then 60 else 45
structure Pause where
  approved : Int
  starts : Int
  ends : Int
  dependency : Bool
abbrev validPause (p : Pause) : Prop := p.dependency = true ∧ p.approved < p.starts ∧ detectionA ≤ p.starts ∧ p.starts ≤ p.ends ∧ p.ends ≤ containmentA
def pause1 : Pause := ⟨25, 30, 60, true⟩
def pause2 : Pause := ⟨65, 70, 110, true⟩
def pauseMinutes : Int := (pause1.ends - pause1.starts) + (pause2.ends - pause2.starts)
def excludedA : Int := min pauseMinutes (pauseCap (revision detectionA))
def elapsedA : Int := containmentA - detectionA
def activeA : Int := elapsedA - excludedA
abbrev timely (start delivered allowance : Int) : Prop := start ≤ delivered ∧ delivered ≤ start + allowance

theorem qualifyingDetection : warningA = -30 ∧ detectionA = 0 ∧ warningA < detectionA := by decide
theorem elapsedInterval : detectionA = 0 ∧ containmentA = 140 ∧ elapsedA = 140 := by decide
theorem acknowledgementTimely : acknowledgementA - detectionA = 12 ∧ timely detectionA acknowledgementA 15 := by decide
theorem activeInterval : elapsedA = 140 ∧ excludedA = 45 ∧ activeA = 95 := by decide
theorem containmentLate : 90 < activeA ∧ activeA - 90 = 5 ∧ timely detectionA acknowledgementA 15 := by decide
theorem approvedPausesCapped : validPause pause1 ∧ validPause pause2 ∧ pause1.ends ≤ pause2.starts ∧ pauseMinutes = 70 ∧ excludedA = 45 := by decide

-- R07/M02: only matching P2 inside [begin,end) defers acknowledgement.
def effectiveStart (priority : Nat) (operationMatches : Bool) (det beginWindow endWindow : Int) : Int :=
  if priority = 2 ∧ operationMatches = true ∧ beginWindow ≤ det ∧ det < endWindow then endWindow else det

theorem noMaintenanceForA : effectiveStart 1 false detectionA 0 180 = detectionA ∧ effectiveStart 1 true detectionA 0 180 = detectionA := by decide
def startB : Int := effectiveStart 2 true detectionB 170 200
theorem bAcknowledgement : startB = 200 ∧ acknowledgementB - startB = 25 ∧ timely startB acknowledgementB 30 := by decide
theorem bRawVersusEffective : acknowledgementB - detectionB = 35 ∧ acknowledgementB - startB = 25 ∧ timely startB acknowledgementB 30 := by decide

def technicalQueued : Int := 8
def technicalDelivered : Int := 11
def commanderDelivered : Int := 22
def executiveDelivered : Int := 72
-- T02 positively certifies continuous noncontainment throughout this interval.
abbrev uncontainedA (t : Int) : Prop := detectionA ≤ t ∧ t < containmentA
theorem technicalLate : technicalQueued = 8 ∧ technicalDelivered = 11 ∧ ¬ timely detectionA technicalDelivered 10 ∧ technicalDelivered - (detectionA + 10) = 1 := by decide
theorem commanderLate : ¬ timely detectionA commanderDelivered 20 ∧ commanderDelivered - (detectionA + 20) = 2 := by decide
theorem executiveTimely : uncontainedA 60 ∧ executiveDelivered = 72 ∧ executiveDelivered - 60 = 12 ∧ timely 60 executiveDelivered 15 := by decide
theorem aRevision : revision detectionA = 2 ∧ warningA < 0 ∧ detectionA = 0 := by decide
theorem cRevision : detectionC = -10 ∧ revision detectionC = 1 := by decide

structure Testimony where
  incident : Nat
  minute : Int
  fullyIsolated : Bool
  retracted : Bool
  deriving DecidableEq
def elise : Testimony := ⟨3, 300, true, false⟩
def pavel : Testimony := ⟨3, 300, false, false⟩
theorem cConflict : elise.incident = pavel.incident ∧ elise.minute = pavel.minute ∧ elise.fullyIsolated ≠ pavel.fullyIsolated ∧ elise.retracted = false ∧ pavel.retracted = false := by decide
structure MonitoringWorld where
  retainedGapSamples : Bool
  listedAlarmsOutsideGap : Bool
  exfiltrationInGap : Bool
theorem gapUnderdetermined : ∀ event : Bool, ∃ w : MonitoringWorld, w.retainedGapSamples = false ∧ w.listedAlarmsOutsideGap = false ∧ w.exfiltrationInGap = event := by
  intro event
  exact ⟨⟨false, false, event⟩, rfl, rfl, rfl⟩
end Audit
