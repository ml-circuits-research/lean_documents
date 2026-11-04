import Std
namespace Audit

-- All money results are integer euro cents. Exact conversion input is not truncated.
def roundTenThousandthsToCents (n : Nat) : Nat := (n + 50) / 100
def p13Exact : Nat := 27777775 * 9
def p13Cents : Nat := roundTenThousandthsToCents p13Exact
def p14Cents : Nat := roundTenThousandthsToCents 249999940

-- UTC minute origin for version/authority events is 2029-06-01 00:00.
def revision (receiptMinute : Int) : Nat := if receiptMinute < 0 then 1 else 2
def threshold (r : Nat) : Nat := if r = 1 then 2000000 else 2500000
def competitionRequired (r cents : Nat) : Bool := decide (threshold r ≤ cents)

def rackAggregates : Bool := true && true && true && decide ((2 : Nat) ≤ 19) && decide ((19 : Nat) ≤ 2 + 29)
def rackKnownBeforeFirst : Bool := true
def rackCents : Nat := 1240000 + 1260000

theorem claim01 : rackAggregates = true ∧ rackKnownBeforeFirst = true ∧ competitionRequired 2 rackCents = true ∧ (1240000 : Nat) < 2500000 ∧ (1260000 : Nat) < 2500000 := by decide
theorem claim02 : rackCents = 2500000 := by decide
theorem claim03 : p13Exact = 249999975 ∧ p13Cents = 2500000 ∧ competitionRequired 2 p13Cents = true := by decide
theorem claim04 : p13Exact < 250000000 ∧ ¬ (p13Cents < 2500000) := by decide
theorem claim05 : p14Cents = 2499999 ∧ p14Cents ≠ 2500000 ∧ competitionRequired 2 p14Cents = false := by decide

def delegatedApproval (categoryCovered : Bool) (cents approval commitment : Nat) : Bool :=
  categoryCovered && decide (cents ≤ 1500000) && decide (approval ≤ 21180) &&
  decide (approval < commitment)

theorem claim06 : delegatedApproval true 1490000 21180 21181 = true ∧ (21180 : Nat) < 21181 := by decide
theorem claim07 : (1500000 : Nat) ≤ 1500000 ∧ delegatedApproval true 1500000 21181 21190 = false := by decide

theorem claim08 : revision (-1) = 1 ∧ revision (-1) ≠ 2 := by decide
def r17Certificate : Bool := false
def r17Exception : Bool := false
theorem claim09 : competitionRequired (revision (-1)) 2250000 = true ∧ r17Certificate = false ∧ r17Exception = false := by decide
theorem claim10 : revision 0 = 2 ∧ competitionRequired (revision 0) 2250000 = false ∧ (2000000 : Nat) ≤ 2250000 := by decide

def emergency (active : Bool) (declaration review : Option Nat) (commitment : Nat) : Bool :=
  match declaration, review with
  | some d, some r => active && decide (d < commitment) && decide (commitment ≤ r) && decide (r ≤ commitment + 2880)
  | _, _ => false

def e19Emergency : Bool := emergency true (some 30825) (some 33720) 30840
def e19Approval : Bool := decide ((30825 : Nat) < 30840)
theorem claim11 : e19Emergency = true ∧ (33720 - 30840 : Nat) = 2880 ∧ e19Approval = true := by decide
theorem claim12 : emergency true none none 30840 = false := by decide

-- Alternative interpretations of the missing norm, not factual annex contents.
inductive CompatibilityTest where
  | warranty | physical
  deriving DecidableEq

def onlyCompatible (test : CompatibilityTest) (soleCertified rivalPassesBench : Bool) : Bool :=
  match test with
  | .warranty => soleCertified
  | .physical => !rivalPassesBench

theorem compatibilityAlternatives : onlyCompatible .warranty true true = true ∧ onlyCompatible .physical true true = false := by decide

-- Attributions concern the identical P-21 director approval at June 27 10:00 UTC.
def maraAffirms : Bool := true
def tomasDenies : Bool := true
theorem claim15Conflict : maraAffirms = true ∧ tomasDenies = true := by decide

structure PaymentWorld where
  signedInvoice : Bool
  deliveryAccepted : Bool
  paid : Bool
  deriving DecidableEq

def possiblePaid : PaymentWorld := ⟨true, true, true⟩
def possibleUnpaid : PaymentWorld := ⟨true, true, false⟩
theorem claim16Alternatives : possiblePaid.signedInvoice = true ∧ possibleUnpaid.signedInvoice = true ∧ possiblePaid.deliveryAccepted = true ∧ possibleUnpaid.deliveryAccepted = true ∧ possiblePaid.paid = true ∧ possibleUnpaid.paid = false := by decide

inductive CoveredPurchase where
  | p11 | p12 | p13 | p14 | p15 | p16 | r17 | r18 | e19
  deriving DecidableEq

def covered : List CoveredPurchase := [.p11, .p12, .p13, .p14, .p15, .p16, .r17, .r18, .e19]
def required (p : CoveredPurchase) : Bool :=
  match p with
  | .p11 | .p12 => competitionRequired 2 rackCents
  | .p13 => competitionRequired 2 p13Cents
  | .p14 => competitionRequired 2 p14Cents
  | .p15 => competitionRequired 2 1490000
  | .p16 => competitionRequired 2 1500000
  | .r17 => competitionRequired 1 2250000
  | .r18 => competitionRequired 2 2250000
  | .e19 => competitionRequired 2 3100000

-- Only certificate facts used by witnesses are modeled; below-threshold cases need none.
def rackCertificate : Bool := false
def rackException : Bool := false

def competitionSatisfied (p : CoveredPurchase) : Bool :=
  match p with
  | .p11 | .p12 => !required p || rackCertificate || rackException
  | .p13 => true
  | .p14 | .p15 | .p16 | .r18 => !required p
  | .r17 => !required p || r17Certificate || r17Exception
  | .e19 => !required p || e19Emergency

def approvalValid (p : CoveredPurchase) : Bool :=
  match p with
  | .p15 => delegatedApproval true 1490000 21180 21181
  | .p16 => delegatedApproval true 1500000 21181 21190
  | .e19 => e19Approval
  | _ => true

def compliant (p : CoveredPurchase) : Bool :=
  competitionSatisfied p && approvalValid p

theorem claim17Witnesses : CoveredPurchase.p16 ∈ covered ∧ approvalValid .p16 = false ∧ compliant .p16 = false ∧ CoveredPurchase.p11 ∈ covered ∧ required .p11 = true ∧ rackCertificate = false ∧ rackException = false ∧ compliant .p11 = false := by decide

theorem claim17UniversalFalse : ¬ (∀ p, p ∈ covered → compliant p = true) := by
  intro h
  have bad := h CoveredPurchase.p16 (by decide)
  have no : compliant .p16 = false := by decide
  rw [no] at bad
  cases bad
end Audit
