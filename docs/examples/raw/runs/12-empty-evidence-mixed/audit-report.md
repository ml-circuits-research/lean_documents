# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

## Registered claim coverage

Coverage: **complete_registration**; 3 reviewed anchors; 2 audited and 0 deferred claims.

Registration reconciles declared claims and reviewed report anchors; it does not establish semantic completeness, faithful decomposition, or that declared searches were actually performed.

- `document-preamble`: non_claim — Document title only.
- `E-01`: claims — Contains the material conclusion and its explanation assessed here.
- `E-02`: claims — Contains the material conclusion and its explanation assessed here.
[Semantic correspondence review](semantic-review.md)

## E-01

### Exact report claim

`input/report.md#E-01`

> Supplier Orion passed clearance.

### Verification question

What does the sole supplied empty source establish about this exact assertion?

### Source evidence

No source evidence attached; see the bounded search record and its limits.


### E-01: criteria and report argument audit

Criteria origin: **inferred**. Scope: The sole supplied source file and supplier Orion; no time period supplied.

Does the statement concern the empty supplied file or an actual clearance event?

- Decision criterion: For file content use inspected bytes; for entailment require all admissible completions to agree.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **not_provided**.

Independent audit reasoning:

- The dossier supplies no event fact establishing a pass.

No independent source evidence is cited; see the bounded search and its limits.

No linked evidence or proof.

Audited claim dependencies: None declared.

Formalization rationale: Finite evidence model with both Bool completions; do not infer a real-world event from no observations.


Declared bounded support search: Inspected all bytes of the sole source empty.txt and found zero UTF-8 characters.

Queries: No text queries; see inspection scope.

No passages inspected: The sole supplied source was inspected but is zero bytes, so it has no source anchors to cite.

The dossier supplies no event fact establishing a pass.

Search limits: No outside records were supplied or searched; absence is bounded to this empty dossier.

### Rules

- Use the inspected source contents and ordinary open-world inference; no event-completeness rule was supplied.

### Assumptions

- The supplied source set is the authorized search scope; no external evidence is assumed.

### Reasoning

- The dossier supplies no event fact establishing a pass.

### Limits

- The model neither authenticates the source nor determines actual clearance.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **not_attempted**.

### Formal evidence

No formal proof was checked for this finding; see its formalization rationale where provided.

### Recommendation

Replace the event assertion with an explicit insufficient-support finding or supply clearance evidence.

## E-02

### Exact report claim

`input/report.md#E-02`

> Supplier Orion failed clearance because no clearance is recorded in the supplied dossier.

### Verification question

What does the sole supplied empty source establish about this exact assertion?

### Source evidence

No source evidence attached; see the bounded search record and its limits.


### E-02: criteria and report argument audit

Criteria origin: **inferred**. Scope: The sole supplied source file and supplier Orion; no time period supplied.

Does the statement concern the empty supplied file or an actual clearance event?

- Decision criterion: For file content use inspected bytes; for entailment require all admissible completions to agree.

Missing definitions: None declared.

Alternatives: None declared.

Report justification outcome: **invalid**.

Report inference at `E-02`:

> Supplier Orion failed clearance because no clearance is recorded in the supplied dossier.

Assessment: **contradicted**. A passing clearance with no recorded assertion satisfies the empty dossier, so absence of a record does not imply failed clearance. Actual clearance remains unknown.

[proof 0: EmptyEvidence.missingRecordDoesNotImplyFailure](models/EmptyEvidence.lean)

Independent audit reasoning:

- A passing clearance with no recorded assertion satisfies the empty dossier, so absence of a record does not imply failed clearance. Actual clearance remains unknown.

No independent source evidence is cited; see the bounded search and its limits.

[proof 0: EmptyEvidence.missingRecordDoesNotImplyFailure](models/EmptyEvidence.lean)

Audited claim dependencies: None declared.

Formalization rationale: Finite evidence model with both Bool completions; do not infer a real-world event from no observations.

- Proof 0 source-to-target correspondence: A passing clearance with no recorded assertion satisfies the empty dossier, so absence of a record does not imply failed clearance. Actual clearance remains unknown. See model-notes.md for the empty-source mapping.

Declared bounded support search: Inspected all bytes of the sole source empty.txt and found zero UTF-8 characters.

Queries: No text queries; see inspection scope.

No passages inspected: The sole supplied source was inspected but is zero bytes, so it has no source anchors to cite.

A passing clearance with no recorded assertion satisfies the empty dossier, so absence of a record does not imply failed clearance. Actual clearance remains unknown.

Search limits: No outside records were supplied or searched; absence is bounded to this empty dossier.

### Rules

- Use the inspected source contents and ordinary open-world inference; no event-completeness rule was supplied.

### Assumptions

- The supplied source set is the authorized search scope; no external evidence is assumed.

### Reasoning

- A passing clearance with no recorded assertion satisfies the empty dossier, so absence of a record does not imply failed clearance. Actual clearance remains unknown.

### Limits

- The model neither authenticates the source nor determines actual clearance.

### Result

Semantic state: **undetermined**; argument status: **invalid_inference**; formal status: **auxiliary**.

### Formal evidence

- `EmptyEvidence.missingRecordDoesNotImplyFailure` in module `EmptyEvidence` (auxiliary): `¬ (∀ passed : Bool, EmptyEvidence.admissible passed → passed = false)`.
  [Model](models/EmptyEvidence.lean) · [Executed check](checks/Target004.lean) · [Actual proof log](logs/target-004.log)

### Recommendation

Replace the event assertion with an explicit insufficient-support finding or supply clearance evidence.
