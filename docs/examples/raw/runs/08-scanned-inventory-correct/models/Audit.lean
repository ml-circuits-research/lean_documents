import Std
namespace Audit
-- Units are exact individual sleeves; ledgers use signed integers.
def unitsPerCrate : Int := 12
def unitsPerCarton : Int := 6
def inboundA : Int := 8 * unitsPerCrate
def inboundB : Int := 2 * unitsPerCarton
def departedA : Int := 5 * unitsPerCrate
def deliveredA : Int := 4 * unitsPerCrate
def returnedA : Int := unitsPerCrate
def departedB : Int := 2 * unitsPerCarton
def requestedB : Int := 3 * unitsPerCarton
def deliveredB : Int := 2 * unitsPerCarton

def book (opening inbound outbound returned : Int) : Int := opening + inbound - outbound + returned
def available (onHand quarantined reserved : Int) : Int := onHand - quarantined - reserved
def bookA : Int := book 100 inboundA departedA returnedA
def bookB : Int := book 40 inboundB departedB 0
def availableA : Int := available bookA 7 0
def availableB : Int := available bookB 0 8

theorem claim01 : inboundA = 96 := by decide
theorem claim02 : inboundB = 12 := by decide
theorem claim03 : bookA = 148 := by decide
theorem claim04 : availableA = 141 := by decide
theorem claim05 : bookB = 40 := by decide
theorem claim06 : availableB = 32 := by decide
theorem claim07 : deliveredA = 48 ∧ returnedA = 12 := by decide
theorem claim08 : requestedB = 18 ∧ deliveredB = 12 ∧ deliveredB < requestedB := by decide

inductive Lot where
  | A | B | C | D
  deriving DecidableEq
structure CountRecord where
  issuer : String
  lot : Lot
  scope : String
  cutoff : String
  amount : Int
  deriving DecidableEq

def elinCount : CountRecord := ⟨"Elin Shore", .A, "W1 shelves and fenced return cage; quarantine included", "2032-04-14 18:00", 148⟩
def reedCount : CountRecord := ⟨"Tomas Reed", .A, "W1 shelves and fenced return cage; quarantine included", "2032-04-14 18:00", 147⟩
theorem claim09 : elinCount.lot = reedCount.lot ∧ elinCount.scope = reedCount.scope ∧ elinCount.cutoff = reedCount.cutoff ∧ elinCount.issuer ≠ reedCount.issuer ∧ elinCount.amount = 148 ∧ reedCount.amount = 147 ∧ elinCount.amount ≠ reedCount.amount := by decide

def importedC : Int := 0 - 9 + 8
theorem claim10 : importedC = -1 := by decide

-- Hypothetical accepted quantities: the packet does not establish either one.
structure DCompletion where
  suppliedReceiverSigned : Bool
  receiverProposal : Nat
  carrierProposal : Nat
  actualAccepted : Nat
  deriving DecidableEq

def possibleD74 : DCompletion := ⟨false, 74, 78, 74⟩
def possibleD78 : DCompletion := ⟨false, 74, 78, 78⟩
theorem claim11Alternatives : possibleD74.suppliedReceiverSigned = false ∧ possibleD78.suppliedReceiverSigned = false ∧ possibleD74.receiverProposal = possibleD78.receiverProposal ∧ possibleD74.carrierProposal = possibleD78.carrierProposal ∧ possibleD74.actualAccepted ≠ possibleD78.actualAccepted := by decide

def completeMovementLots : List Lot := [.A, .B]
theorem claim12 : Lot.A ∈ completeMovementLots ∧ Lot.B ∈ completeMovementLots ∧ Lot.D ∉ completeMovementLots := by decide

structure StockState where
  onHand : Int
  reserved : Int
  deriving DecidableEq

def reserve (s : StockState) (q : Int) : StockState := ⟨s.onHand, s.reserved + q⟩
theorem claim13 : ∀ s q, (reserve s q).onHand = s.onHand ∧ (reserve s q).reserved = s.reserved + q := by
  intro s q
  exact ⟨rfl, rfl⟩

inductive CorrectionEvidence where
  | unsignedProposal | approvedCorrection
  deriving DecidableEq

def suppliedCCorrections : List CorrectionEvidence := [.unsignedProposal]
theorem claim14 : CorrectionEvidence.unsignedProposal ∈ suppliedCCorrections ∧ CorrectionEvidence.approvedCorrection ∉ suppliedCCorrections := by decide
end Audit
