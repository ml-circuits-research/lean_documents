import Std
namespace Audit
inductive Entry where
  | a01 | a02 | a03
  deriving DecidableEq, Repr
-- Complete finite manifest from inventory-p2, not a universe of deployments.
def manifest : List Entry := [.a01, .a02, .a03]
theorem manifestExact : manifest.length = 3 ∧ manifest.Nodup ∧ manifest = [Entry.a01, Entry.a02, Entry.a03] := by decide

inductive Issuer where
  | qa | operations
  deriving DecidableEq
structure Context where
  release : String
  target : String
  listener : String
  instant : String
  deriving DecidableEq
def tlsContext : Context := ⟨"R17", "EU-A", "inbound API", "2030-03-14T11:45:00Z"⟩
structure Assertion where
  issuer : Issuer
  context : Context
  enabled : Bool
  deriving DecidableEq
def qa : Assertion := ⟨.qa, tlsContext, true⟩
def ops : Assertion := ⟨.operations, tlsContext, false⟩
-- These are attributed assertions, not global propositions about the deployed listener.
theorem testimonyConflict : qa.issuer ≠ ops.issuer ∧ qa.context = ops.context ∧ qa.enabled = true ∧ ops.enabled = false ∧ qa.enabled ≠ ops.enabled := by decide

inductive Attachment where
  | inventory | qa | operations | policy | archive | penetrationCertificate | independentReview
  deriving DecidableEq
def packet : List Attachment := [.inventory, .qa, .operations, .policy, .archive]
theorem certificateAbsent : Attachment.penetrationCertificate ∉ packet := by decide
theorem independentArtifactAbsent : Attachment.independentReview ∉ packet := by decide

-- An inference that worked for every world would have to work for True/False/False.
theorem readinessNotEntailed : ¬ (∀ smoke security ready : Prop, smoke → ((smoke ∧ security) → ready) → ready) := by
  intro inference
  exact inference True False False True.intro (fun h => h.2)

inductive Node where
  | archivedClaim | verificationAppendix | independentArtifact
  deriving DecidableEq
def supportLinks : List (Node × Node) := [(.archivedClaim, .verificationAppendix), (.verificationAppendix, .archivedClaim)]
theorem citationCycle : supportLinks = [(Node.archivedClaim, Node.verificationAppendix), (Node.verificationAppendix, Node.archivedClaim)] ∧ (Node.archivedClaim, Node.independentArtifact) ∉ supportLinks ∧ (Node.verificationAppendix, Node.independentArtifact) ∉ supportLinks := by decide

-- Possible completions of missing event/authenticity data. No actual event is asserted.
structure Completion where
  certificateAttached : Bool
  testOccurred : Bool
  reviewAttached : Bool
  reviewOccurred : Bool
  signatureMarker : Bool
  signatureAuthentic : Bool
abbrev agreesWithPacket (w : Completion) : Prop :=
  w.certificateAttached = false ∧ w.reviewAttached = false ∧ w.signatureMarker = true
theorem missingFactsRemainOpen : ∀ tested reviewed authentic : Bool, ∃ w : Completion, agreesWithPacket w ∧ w.testOccurred = tested ∧ w.reviewOccurred = reviewed ∧ w.signatureAuthentic = authentic := by
  intro tested reviewed authentic
  exact ⟨⟨false, tested, false, reviewed, true, authentic⟩, ⟨rfl, rfl, rfl⟩, rfl, rfl, rfl⟩
end Audit
