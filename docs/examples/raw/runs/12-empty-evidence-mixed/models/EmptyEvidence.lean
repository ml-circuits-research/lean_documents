namespace EmptyEvidence
-- Transcribed from the inspected zero-byte source. No event facts are encoded.
def sourceText : String := ""
def observations : List Bool := []
def admissible (passed : Bool) : Prop := observations.all (fun recorded => recorded == passed) = true

theorem zeroCharacters : sourceText.length = 0 := by decide
theorem bothPossible : admissible true ∧ admissible false := by
  constructor <;> rfl
theorem missingRecordDoesNotImplyFailure : ¬ (∀ passed : Bool, admissible passed → passed = false) := by
  intro h
  have wrong : true = false := h true (by rfl)
  cases wrong
end EmptyEvidence
