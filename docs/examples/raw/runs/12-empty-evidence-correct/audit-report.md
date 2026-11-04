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

> The sole supplied source file contains zero characters. This is a statement about the supplied file, not about whether clearance occurred.

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

- Direct inspection shows an empty UTF-8 file; this establishes only its content length.

No independent source evidence is cited; see the bounded search and its limits.

[proof 0: EmptyEvidence.zeroCharacters](models/EmptyEvidence.lean)

Audited claim dependencies: None declared.

Formalization rationale: Finite evidence model with both Bool completions; do not infer a real-world event from no observations.

- Proof 0 source-to-target correspondence: Direct inspection shows an empty UTF-8 file; this establishes only its content length. See model-notes.md for the empty-source mapping.

Declared bounded support search: Inspected all bytes of the sole source empty.txt and found zero UTF-8 characters.

Queries: No text queries; see inspection scope.

No passages inspected: The sole supplied source was inspected but is zero bytes, so it has no source anchors to cite.

Direct inspection shows an empty UTF-8 file; this establishes only its content length.

Search limits: No outside records were supplied or searched; absence is bounded to this empty dossier.

### Rules

- Use the inspected source contents and ordinary open-world inference; no event-completeness rule was supplied.

### Assumptions

- The supplied source set is the authorized search scope; no external evidence is assumed.

### Reasoning

- Direct inspection shows an empty UTF-8 file; this establishes only its content length.

### Limits

- The model neither authenticates the source nor determines actual clearance.

### Result

Semantic state: **supported**; argument status: **insufficient_support**; formal status: **proved**.

### Formal evidence

- `EmptyEvidence.zeroCharacters` in module `EmptyEvidence` (supports): `EmptyEvidence.sourceText.length = 0`.
  [Model](models/EmptyEvidence.lean) · [Executed check](checks/Target004.lean) · [Actual proof log](logs/target-004.log)

### Recommendation

Retain the scoped observation.

## E-02

### Exact report claim

`input/report.md#E-02`

> The supplied dossier does not establish whether supplier Orion passed clearance. There are no source statements or completeness rules restricting either outcome, so both a pass and a failure are compatible with the supplied evidence.

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

Report justification outcome: **sufficient**.

Report inference at `E-02`:

> The supplied dossier does not establish whether supplier Orion passed clearance. There are no source statements or completeness rules restricting either outcome, so both a pass and a failure are compatible with the supplied evidence.

Assessment: **verified**. With no supplied event assertion or completeness rule, pass and failure are both consistent with the entire supplied evidence.

[proof 0: EmptyEvidence.bothPossible](models/EmptyEvidence.lean)

Independent audit reasoning:

- With no supplied event assertion or completeness rule, pass and failure are both consistent with the entire supplied evidence.

No independent source evidence is cited; see the bounded search and its limits.

[proof 0: EmptyEvidence.bothPossible](models/EmptyEvidence.lean)

Audited claim dependencies: None declared.

Formalization rationale: Finite evidence model with both Bool completions; do not infer a real-world event from no observations.

- Proof 0 source-to-target correspondence: With no supplied event assertion or completeness rule, pass and failure are both consistent with the entire supplied evidence. See model-notes.md for the empty-source mapping.

Declared bounded support search: Inspected all bytes of the sole source empty.txt and found zero UTF-8 characters.

Queries: No text queries; see inspection scope.

No passages inspected: The sole supplied source was inspected but is zero bytes, so it has no source anchors to cite.

With no supplied event assertion or completeness rule, pass and failure are both consistent with the entire supplied evidence.

Search limits: No outside records were supplied or searched; absence is bounded to this empty dossier.

### Rules

- Use the inspected source contents and ordinary open-world inference; no event-completeness rule was supplied.

### Assumptions

- The supplied source set is the authorized search scope; no external evidence is assumed.

### Reasoning

- With no supplied event assertion or completeness rule, pass and failure are both consistent with the entire supplied evidence.

### Limits

- The model neither authenticates the source nor determines actual clearance.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `EmptyEvidence.bothPossible` in module `EmptyEvidence` (supports): `EmptyEvidence.admissible true ∧ EmptyEvidence.admissible false`.
  [Model](models/EmptyEvidence.lean) · [Executed check](checks/Target005.lean) · [Actual proof log](logs/target-005.log)

### Recommendation

Retain the scoped observation.
