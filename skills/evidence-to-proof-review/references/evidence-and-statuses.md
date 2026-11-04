# Evidence and statuses

Preserve original source bytes, SHA-256, version, role, original path, extraction method, and an original-coordinate mapping. Hashes establish byte identity, not authenticity. For every extracted assertion retain quote, anchor, speaker, factual assertion/norm/hypothesis/fiction status, polarity, modality, time, jurisdiction or narrative world, applicable version, exceptions, uncertainty and alternative interpretations. Do not flatten speech into world truth.

The runtime finding vocabulary separates:

| Axis | Values | Meaning |
| --- | --- | --- |
| `semantic_state` | `supported`, `refuted`, `both`, `undetermined`, `not_applicable` | Documentary assessment of the exact claim under declared assumptions |
| `argument_status` | `sufficient`, `insufficient_support`, `invalid_inference`, `disputed`, `nonformal` | Quality of the report's justification in v2, separate from independent source support and historical truth |
| `formal_status` | `proved`, `refuted`, `auxiliary`, `not_attempted`, `blocked` | Relationship of checked Lean targets to the original claim |

Proof execution results are separate: tool unavailable, failed, timeout, and checked are recorded in `proof-results.json`. A semantic support judgment can have `not_attempted`; it is not thereby Lean certified. A claim with `undetermined` can have an `auxiliary` proof showing a countermodel to its proposed argument. A `both` claim can have an auxiliary proof of disagreement, never proofs that both incompatible event claims are true.

The public audit should display PROVED_IN_MODEL or REFUTED_IN_MODEL only for direct, checked targets whose source correspondence was reviewed. Otherwise explain documentary support/refutation, INSUFFICIENT_SUPPORT, CONFLICTING_EVIDENCE, UNDETERMINED, FORMALIZATION_BLOCKED, or NON_FORMAL_ASSESSMENT as appropriate. Do not hide a support gap behind a generic “unknown”.

For uncertainty, identify its origin: unavailable annex, unknown event, ambiguous definition, conflicting source, limited search, or incomplete computation. For closed-world reasoning, give the exact completeness statement and domain. A complete attachment inventory does not imply a complete event history.

Use the v2 `claims.json` registry seeded by preparation; classify every report passage and register atomic claims before auditing. Count every material claim, including unformalized ones. Record excluded questions with reasons. Partition large corpora on disk, preserve cross-document relationships, and invalidate dependent results whenever source hashes, interpretation, rules, or targets change.
