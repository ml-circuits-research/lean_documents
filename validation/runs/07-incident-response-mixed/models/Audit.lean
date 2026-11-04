import Std
namespace Audit
-- All times are signed UTC minute offsets from 2030-10-27 00:00 UTC.
def utc (localMinute offsetMinute : Int) : Int := localMinute - offsetMinute
def aRaw : Int := utc 90 120
def aDetection : Int := utc 120 120
def aAcknowledgement : Int := utc 132 120
def aContainment : Int := utc 200 60
def aElapsed : Int := aContainment - aDetection
def revision (detection : Int) : Nat := if detection < 0 then 1 else 2
def cap (r : Nat) : Int := if r = 1 then 60 else 45

def pauseConditions : Bool := decide ((25 : Int) < 30 ∧ 65 < 70 ∧ 0 ≤ 30 ∧ 30 ≤ 60 ∧ 60 ≤ 70 ∧ 70 ≤ 110 ∧ 110 ≤ 140)
def rawPauseA : Int := (60 - 30) + (110 - 70)
def excludedA : Int := min rawPauseA (cap (revision aDetection))
def activeA : Int := aElapsed - excludedA

theorem claim01 : aDetection = 0 := by decide
theorem claim02 : aElapsed = 140 ∧ aElapsed ≠ 80 := by decide
theorem claim03 : aAcknowledgement - aDetection = 12 ∧ aAcknowledgement ≤ aDetection + 15 := by decide
theorem claim04 : activeA = 95 ∧ activeA ≠ 80 := by decide
theorem claim05 : ¬ (activeA ≤ 90) ∧ activeA - 90 = 5 := by decide
theorem claim06 : pauseConditions = true ∧ rawPauseA = 70 ∧ excludedA = 45 ∧ excludedA < rawPauseA := by decide

inductive Priority where
  | p1 | p2
  deriving DecidableEq

def effectiveAcknowledgementStart (p : Priority) (operationMatches : Bool) (detection windowStart windowEnd : Int) : Int :=
  if p = .p2 ∧ operationMatches = true ∧ windowStart ≤ detection ∧ detection < windowEnd
    then windowEnd else detection

def aEffectiveStart : Int := effectiveAcknowledgementStart .p1 false aDetection 0 180
def bDetection : Int := utc 250 60
def bAcknowledgement : Int := utc 285 60
def bEffectiveStart : Int := effectiveAcknowledgementStart .p2 true bDetection 170 200

theorem claim07 : aEffectiveStart = 0 ∧ aEffectiveStart ≠ 180 := by decide
theorem claim08 : (170 : Int) ≤ bDetection ∧ bDetection < 200 ∧ bEffectiveStart = 200 ∧ bAcknowledgement - bEffectiveStart = 25 ∧ bAcknowledgement ≤ bEffectiveStart + 30 := by decide
theorem claim09 : bAcknowledgement - bDetection = 35 ∧ bAcknowledgement ≤ bEffectiveStart + 30 := by decide

structure Notification where
  queued : Int
  delivered : Int
  deriving DecidableEq

def technical : Notification := ⟨8, 11⟩
def commander : Notification := ⟨18, 22⟩
def executiveDelivery : Int := 72
-- T02 is a positive authoritative record of continuous uncontained state.
def aUncontainedAt (minute : Int) : Bool := decide (aDetection ≤ minute ∧ minute < aContainment)
theorem claim10 : technical.queued ≤ aDetection + 10 ∧ ¬ (technical.delivered ≤ aDetection + 10) ∧ technical.delivered = 11 := by decide
theorem claim11 : commander.delivered = 22 ∧ ¬ (commander.delivered ≤ aDetection + 20) := by decide
theorem claim12 : aUncontainedAt (aDetection + 60) = true ∧ executiveDelivery - (aDetection + 60) = 12 ∧ executiveDelivery ≤ aDetection + 75 := by decide
theorem claim13 : aRaw = -30 ∧ aDetection = 0 ∧ revision aDetection = 2 ∧ revision aDetection ≠ 1 := by decide
def cDetection : Int := utc 110 120
theorem claim14 : cDetection = -10 ∧ revision cDetection = 1 := by decide

-- Attributed propositions, not incompatible unconditional incident-state facts.
def eliseAffirmsIsolation0500 : Bool := true
def pavelDeniesIsolation0500 : Bool := true
theorem claim15Conflict : eliseAffirmsIsolation0500 = true ∧ pavelDeniesIsolation0500 = true := by decide

structure MonitoringWorld where
  gapSamplesAvailable : Bool
  retainedListedAlarms : Bool
  exfiltrationDuringGap : Bool
  deriving DecidableEq

def possibleNoExfiltration : MonitoringWorld := ⟨false, false, false⟩
def possibleExfiltration : MonitoringWorld := ⟨false, false, true⟩
theorem gapAlternatives : possibleNoExfiltration.gapSamplesAvailable = false ∧ possibleExfiltration.gapSamplesAvailable = false ∧ possibleNoExfiltration.retainedListedAlarms = false ∧ possibleExfiltration.retainedListedAlarms = false ∧ possibleNoExfiltration.exfiltrationDuringGap = false ∧ possibleExfiltration.exfiltrationDuringGap = true := by decide
end Audit
