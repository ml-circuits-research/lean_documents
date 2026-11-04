# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

[Semantic correspondence review](semantic-review.md)

Extraction inventory: 69 documents; 0 pending, partial or blocked. See [ingestion details](ingestion.json) and [coverage](coverage.md).

## C10-ERR-01

### Exact report claim

`input/report.md#C10-ERR-01`

> **C10-ERR-01.** Every recorded September release was authorized.

### Verification question

Was every recorded September release authorized, including N58-R1?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P03`

> [G02] Authorization by revision. Policy revision B becomes effective at 00:00 on 15 September. A release at or after that instant requires an active operator credential at release time, a signed approval by a principal with scope over that node at approval time, and an unrevoked permit covering the release. Before that instant, revision A requires an active operator credential and signed local-supervisor approval; no central permit is required. Event time controls historical applicability. Report date, file modification date, and discovery date do not replace the operative timestamp. Successful technical handoff does not itself establish administrative authorization.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 656, "end_character": 1331, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-bd1j4xxu"}`.

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P04`

> [G03] Hierarchy and identity. Resolve aliases through the dated identity registry. A reused display name does not transfer the former principal's credential. Supersession replaces only the named scope from its stated effective instant. A valid board exception can modify the ordinary route if its node, time, and other conditions match. The board's power to grant exceptions does not establish that a requested exception was granted. Ordinary approval authority does not include authority to rewrite policy. Filename ordering creates no precedence. The applicable hierarchy must be assembled before deciding whether the ordinary permit requirement governs a particular release.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1333, "end_character": 2010, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-bd1j4xxu"}`.

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P05`

> [G04] Missing and contrary evidence. A missing permit attachment in an expressly incomplete history establishes a missing argument, not proof that no permit existed. A complete bounded permit history can establish absence within its specified interval. An explicitly revoked permit with a statement that no replacement existed is different from an empty search result. One documented unauthorized release refutes a global claim that all recorded releases were authorized, even if other cases remain unknown. Completeness of the node domain does not establish completeness of all release events. A claim of exactly one event needs event-history evidence, not merely a valid authorization for one known event.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2012, "end_character": 2719, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-bd1j4xxu"}`.

- [input/sources/03-policy-transition.md](input/sources/03-policy-transition.md) — `P04`

> [PV03] N58 permit revocation took effect at 09:00 on 22 September. Its release occurred at 10:00, and the signed revocation was indexed at 11:00. The index timestamp does not postpone the explicit effective time. The complete permit history says no replacement existed at 10:00. No board exception applies to N58. This supplies a concrete unauthorized release and an independent counterexample to a global authorization claim. It does not require inferring absence from a retrieval failure. Technical bundle handoff succeeded, but that fact does not reverse the administrative revocation.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1148, "end_character": 1736, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "49b4f99dd0f7f83a36ca549e0f2e026d83bfef78f82c5b46f4aed7d84b70e6f3", "artifact_directory": "extraction/D00006/attempt-rab6abi1"}`.

- [input/sources/records/058-n58.md](input/sources/records/058-n58.md) — `P02`

> [N58-01] Release N58-R1 occurred on 22 September at 10:00 with active Ada and valid Cora approval. The node permit had been revoked effective 09:00, before release, although its index entry appeared at 11:00. The complete permit history says no replacement existed at 10:00. No board exception covers N58. The record explicitly identifies this release as unauthorized under revision B. This counterexample remains decisive for a global claim even if other nodes have incomplete evidence. Successful administrative handoff is a separate fact.

Original: [input/originals/D00067.md](input/originals/D00067.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 577, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00067.md", "original_sha256": "f9efcebda7ad09423ba369c0c5456d8b70e40fecf276d4d9ce4d14dd79e5f7e9", "artifact_directory": "extraction/D00067/attempt-51ocy3vs"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P03`

> [EX02] This grant changes only the ordinary central-approval and permit requirements for the specified N57 window. The request mentioned N58, but the board deliberately excluded it from the final grant. The signed final scope prevails over the earlier proposal. Its location after the operational records does not diminish authority, and its filename creates no independent precedence. An assessor who discovers it must revisit any provisional N57 conclusion made from the general rule alone. Full-corpus rule discovery matters because the exception is separate from the record whose authorization it changes.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 612, "end_character": 1221, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-y_23t1fp"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P04`

> [EX03] The board-exception register is complete for September and contains only this grant. No second board exception covers N58 or N51. This bounded completeness can support an absence conclusion about board grants for those nodes during that interval. It says nothing about later periods or all imaginable documents. The incomplete N59 permit history supports a different conclusion: its missing permit remains unknown. The audit should identify exactly which completeness premise licenses a negative fact, rather than treating every unsuccessful search as equivalent evidence of absence.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1223, "end_character": 1813, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-y_23t1fp"}`.

### Rules

- Select policy by release event time under G02; match dated alias, credential, approval scope and effective permit/exception under G03.
- G04 licenses negative facts only with an applicable complete history or explicit contrary evidence; identity completeness is not event completeness.
- G05 requires dependency review for changed source snapshots; no source supplies an aesthetic criterion.

### Assumptions

- Accept the synthetic signed-source authority and stated completeness within their exact named scope. No world-wide completeness or source authenticity is inferred.

### Reasoning

- 1. N58-R1 is a recorded release on September 22 at 10:00, within revision B and the report's September domain.
- 2. Its permit was effectively revoked at 09:00; the complete history excludes a replacement and the final exception excludes N58.
- 3. Although credentials and Cora approval were valid, the permit conjunct failed. This concrete recorded event refutes the universal regardless of other unknown cases.

### Limits

- Findings concern named September 2034 events and source-defined roles; unknown N59 permits and N60 events remain unknown.
- Formal targets check reviewed necessary conditions and finite witnesses, not every unspecified event or the authenticity of original signatures. Source paragraph quotations preserve native original paths and semantic markers.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim01` in module `Audit` (refutes): `Audit.n58Authorized = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target011.lean) · [Actual proof log](logs/target-011.log)

### Recommendation

Withdraw the universal; identify N58 as an explicit counterexample.

## C10-ERR-02

### Exact report claim

`input/report.md#C10-ERR-02`

> **C10-ERR-02.** N04 historical release was unauthorized because it had no central permit.

### Verification question

Did the historical N04 release fail because there was no central permit?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P03`

> [G02] Authorization by revision. Policy revision B becomes effective at 00:00 on 15 September. A release at or after that instant requires an active operator credential at release time, a signed approval by a principal with scope over that node at approval time, and an unrevoked permit covering the release. Before that instant, revision A requires an active operator credential and signed local-supervisor approval; no central permit is required. Event time controls historical applicability. Report date, file modification date, and discovery date do not replace the operative timestamp. Successful technical handoff does not itself establish administrative authorization.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 656, "end_character": 1331, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-bd1j4xxu"}`.

- [input/sources/03-policy-transition.md](input/sources/03-policy-transition.md) — `P02`

> [PV01] Revision A governs the N04 release on 14 September. Active Ada and local-supervisor Emil approval satisfy its route without a central permit. A report written after revision B takes effect does not retroactively impose that newer rule. The historical event and any later release of the same node are separate objects. This source defines applicability; the operational record provides the event details. The reviewer should cite both when explaining the historical authorization claim rather than assume that a current-policy headline applies to every date.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 45, "end_character": 609, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "49b4f99dd0f7f83a36ca549e0f2e026d83bfef78f82c5b46f4aed7d84b70e6f3", "artifact_directory": "extraction/D00006/attempt-rab6abi1"}`.

- [input/sources/records/004-n04.md](input/sources/records/004-n04.md) — `P02`

> [N04-01] Historical release N04-R1 occurred on 14 September at 10:00 under revision A. Ada's credential was active, and local supervisor Emil signed approval at 09:00. No central permit existed because that historical route did not require one. The named release history is complete. The later report date does not change event time. The release satisfied its applicable route. This conclusion says nothing about a hypothetical later release of the same node, which would need its own date, operator, approval, and permit assessment.

Original: [input/originals/D00013.md](input/originals/D00013.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 569, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00013.md", "original_sha256": "8ae3d6603a916a292b6c6a9d677540daf14dd0608e55371979277a5198f3265b", "artifact_directory": "extraction/D00013/attempt-i0vd8n27"}`.

- [input/sources/01-alias-register.md](input/sources/01-alias-register.md) — `P02`

> [AL01] Principal Ada Quill has immutable identifier P-AQ. Alias north-operator identifies Ada from 1 through 20 September inclusive. From 21 September the same alias identifies Ben Rook, P-BR. Ada uses aq-main from 21 September onward. Ada's credential is active throughout September. Ben's credential becomes active on 22 September. Therefore a 21 September north-operator signature names Ben before his activation, not Ada. The alias transfer and credential activation are distinct events. Copying an older alias mapping without its dates supplies the wrong principal for the later event.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 37, "end_character": 627, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "f07bfa3668571ccd931251b2f2b44f8c10a9f4323bdc0dac424f76b27fd1b52f", "artifact_directory": "extraction/D00004/attempt-7j0k77x1"}`.

- [input/sources/01-alias-register.md](input/sources/01-alias-register.md) — `P03`

> [AL02] Central approver Cora Vale, P-CV, has ordinary approval authority over N01 through N60 throughout September. Delegate Devon Ash, P-DA, has only the narrower scope in the native delegation instrument. Local supervisor Emil Pine, P-EP, has revision A local authority before 15 September. Emil has no ordinary revision B central approval authority. Cora, CV, and central-approver all name P-CV throughout the interval. A correct identity mapping alone does not prove approval scope, timing, or the validity of a permit. Those predicates require their own evidence.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 629, "end_character": 1197, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "f07bfa3668571ccd931251b2f2b44f8c10a9f4323bdc0dac424f76b27fd1b52f", "artifact_directory": "extraction/D00004/attempt-7j0k77x1"}`.

### Rules

- Select policy by release event time under G02; match dated alias, credential, approval scope and effective permit/exception under G03.
- G04 licenses negative facts only with an applicable complete history or explicit contrary evidence; identity completeness is not event completeness.
- G05 requires dependency review for changed source snapshots; no source supplies an aesthetic criterion.

### Assumptions

- Accept the synthetic signed-source authority and stated completeness within their exact named scope. No world-wide completeness or source authenticity is inferred.

### Reasoning

- 1. N04-R1 occurred September 14 before revision B.
- 2. Revision A requires active credential and Emil's signed local approval, both recorded; it does not require a central permit.
- 3. The later policy cannot be imposed retroactively merely because the report is later.

### Limits

- Findings concern named September 2034 events and source-defined roles; unknown N59 permits and N60 events remain unknown.
- Formal targets check reviewed necessary conditions and finite witnesses, not every unspecified event or the authenticity of original signatures. Source paragraph quotations preserve native original paths and semantic markers.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim02` in module `Audit` (refutes): `Audit.routeA true true = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target012.lean) · [Actual proof log](logs/target-012.log)

### Recommendation

Recognize the September 14 N04 event as authorized under revision A.

## C10-ERR-03

### Exact report claim

`input/report.md#C10-ERR-03`

> **C10-ERR-03.** N09 release on 21 September was authorized by superseded permit P09-v1.

### Verification question

Did archived P09-v1 authorize N09 at September 21 10:00?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P03`

> [G02] Authorization by revision. Policy revision B becomes effective at 00:00 on 15 September. A release at or after that instant requires an active operator credential at release time, a signed approval by a principal with scope over that node at approval time, and an unrevoked permit covering the release. Before that instant, revision A requires an active operator credential and signed local-supervisor approval; no central permit is required. Event time controls historical applicability. Report date, file modification date, and discovery date do not replace the operative timestamp. Successful technical handoff does not itself establish administrative authorization.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 656, "end_character": 1331, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-bd1j4xxu"}`.

- [input/sources/03-policy-transition.md](input/sources/03-policy-transition.md) — `P03`

> [PV02] N09 permit P09-v1 covered releases through 19 September at 23:59. P09-v2 took effect at 00:00 on 20 September and superseded v1 for later releases. Version 2 covered 20 September only. The N09 release at 10:00 on 21 September lies outside both operative windows. The complete N09 permit history states that no replacement or extension existed at that time. Preserving an old permit file does not preserve its operative authority. An auditor must retain its expiry and named supersession clause when quoting a favorable headline.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 611, "end_character": 1146, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "49b4f99dd0f7f83a36ca549e0f2e026d83bfef78f82c5b46f4aed7d84b70e6f3", "artifact_directory": "extraction/D00006/attempt-rab6abi1"}`.

- [input/sources/records/009-n09.md](input/sources/records/009-n09.md) — `P02`

> [N09-01] Release N09-R1 occurred on 21 September at 10:00. Ada signed as aq-main with an active credential, and Cora approval was valid. P09-v1 had expired and been superseded; P09-v2 covered only 20 September. The complete permit history states no extension or replacement existed at release. Therefore the release lacked an in-force permit under revision B. Both permit versions remain archived for traceability. Their presence in the packet does not mean both remain operative. Technical handoff succeeded despite the missing valid permit.

Original: [input/originals/D00018.md](input/originals/D00018.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 578, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00018.md", "original_sha256": "c81c27f0268253c07bb914ab61f28f5b45a1dc13911e14ed16455a66b2881d08", "artifact_directory": "extraction/D00018/attempt-y2h4u7o1"}`.

### Rules

- Select policy by release event time under G02; match dated alias, credential, approval scope and effective permit/exception under G03.
- G04 licenses negative facts only with an applicable complete history or explicit contrary evidence; identity completeness is not event completeness.
- G05 requires dependency review for changed source snapshots; no source supplies an aesthetic criterion.

### Assumptions

- Accept the synthetic signed-source authority and stated completeness within their exact named scope. No world-wide completeness or source authenticity is inferred.

### Reasoning

- 1. P09-v1 ended September 19 at 23:59 and was superseded September 20. P09-v2 covered September 20 only.
- 2. The September 21 release is outside both windows; complete history explicitly excludes extension/replacement. Archived existence is not operative authority.

### Limits

- Findings concern named September 2034 events and source-defined roles; unknown N59 permits and N60 events remain unknown.
- Formal targets check reviewed necessary conditions and finite witnesses, not every unspecified event or the authenticity of original signatures. Source paragraph quotations preserve native original paths and semantic markers.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim03` in module `Audit` (refutes): `Audit.p09Covers 21 = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target013.lean) · [Actual proof log](logs/target-013.log)

### Recommendation

Report the missing in-force permit for this specific release.

## C10-ERR-04

### Exact report claim

`input/report.md#C10-ERR-04`

> **C10-ERR-04.** The N21 north-operator signature on 21 September identifies credentialed Ada.

### Verification question

Does the September 21 north-operator signature identify credentialed Ada?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P04`

> [G03] Hierarchy and identity. Resolve aliases through the dated identity registry. A reused display name does not transfer the former principal's credential. Supersession replaces only the named scope from its stated effective instant. A valid board exception can modify the ordinary route if its node, time, and other conditions match. The board's power to grant exceptions does not establish that a requested exception was granted. Ordinary approval authority does not include authority to rewrite policy. Filename ordering creates no precedence. The applicable hierarchy must be assembled before deciding whether the ordinary permit requirement governs a particular release.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1333, "end_character": 2010, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-bd1j4xxu"}`.

- [input/sources/01-alias-register.md](input/sources/01-alias-register.md) — `P02`

> [AL01] Principal Ada Quill has immutable identifier P-AQ. Alias north-operator identifies Ada from 1 through 20 September inclusive. From 21 September the same alias identifies Ben Rook, P-BR. Ada uses aq-main from 21 September onward. Ada's credential is active throughout September. Ben's credential becomes active on 22 September. Therefore a 21 September north-operator signature names Ben before his activation, not Ada. The alias transfer and credential activation are distinct events. Copying an older alias mapping without its dates supplies the wrong principal for the later event.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 37, "end_character": 627, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "f07bfa3668571ccd931251b2f2b44f8c10a9f4323bdc0dac424f76b27fd1b52f", "artifact_directory": "extraction/D00004/attempt-7j0k77x1"}`.

- [input/sources/01-alias-register.md](input/sources/01-alias-register.md) — `P04`

> [AL03] The identity registrar signed this mapping and marked it complete for the named aliases during September. No supplied amendment changes the 21 September reassignment. An unsigned chat reference cannot amend the registry. The completeness assertion concerns those names and dates, not every possible identity in the world. The original source path and dated marker should accompany any extracted identity assertion. Searching only for a repeated display name deliberately misses the temporal distinction in this case. A reviewer must preserve the precise release date when linking the signature to a principal and credential.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1199, "end_character": 1830, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "f07bfa3668571ccd931251b2f2b44f8c10a9f4323bdc0dac424f76b27fd1b52f", "artifact_directory": "extraction/D00004/attempt-7j0k77x1"}`.

- [input/sources/records/021-n21.md](input/sources/records/021-n21.md) — `P02`

> [N21-01] Release N21-R1 occurred on 21 September at 10:00 and was signed as north-operator. The dated registry maps that alias to Ben on this date. His credential did not activate until 22 September. Cora approval and the node permit were valid, but the operator prerequisite failed. The identity history for this release is complete. An earlier north-operator signature by Ada cannot supply the identity or credential for this later signature. The failure is affirmative dated evidence, not merely an unspecified operator field.

Original: [input/originals/D00030.md](input/originals/D00030.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 565, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00030.md", "original_sha256": "951c437910474727128a851bc902672edc6ec94fc017611403480863a6a9ff56", "artifact_directory": "extraction/D00030/attempt-2y3otbrn"}`.

### Rules

- Select policy by release event time under G02; match dated alias, credential, approval scope and effective permit/exception under G03.
- G04 licenses negative facts only with an applicable complete history or explicit contrary evidence; identity completeness is not event completeness.
- G05 requires dependency review for changed source snapshots; no source supplies an aesthetic criterion.

### Assumptions

- Accept the synthetic signed-source authority and stated completeness within their exact named scope. No world-wide completeness or source authenticity is inferred.

### Reasoning

- 1. The dated complete alias register reassigns north-operator from Ada to Ben on September 21.
- 2. Ben activates only September 22; Ada's active credential and earlier alias usage cannot transfer to Ben's signature.

### Limits

- Findings concern named September 2034 events and source-defined roles; unknown N59 permits and N60 events remain unknown.
- Formal targets check reviewed necessary conditions and finite witnesses, not every unspecified event or the authenticity of original signatures. Source paragraph quotations preserve native original paths and semantic markers.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim04` in module `Audit` (refutes): `Audit.northOperator 21 ≠ Audit.Principal.ada`.
  [Model](models/Audit.lean) · [Executed check](checks/Target014.lean) · [Actual proof log](logs/target-014.log)

### Recommendation

Resolve the signature to Ben and record the inactive credential at that event.

## C10-ERR-05

### Exact report claim

`input/report.md#C10-ERR-05`

> **C10-ERR-05.** Devon approval of N41 on 20 September was within delegated scope.

### Verification question

Was Devon's N41 approval on September 20 at 09:00 within both node and time scope?

### Source evidence

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-p-0001`

> [AU01] SYNTHETIC SIGNED DELEGATION. Cora Vale grants Devon Ash ordinary revision B approval authority over nodes N41 through N50, effective 18 September 2034 at 00:00 through 25 September at 23:59 inclusive. The node and time restrictions are substantive. A genuine Devon signature outside this scope cannot authorize an approval. The instrument does not grant policy-amendment, exception-granting, credential-issuance, or permit-revocation powers. It also does not let Devon extend his own delegation. Both the node and approval timestamp must be checked against the table.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-p-0012`

> [AU02] AUTHENTICITY AND PROVENANCE. Cora signs under her standing central approval charter. The native document is the operative delegation, while requests and forwarded messages are historical correspondence. Creation time is distinct from effective time. A derived extraction must preserve all table columns and restrictions. Removing the node interval from a snippet can make a narrow grant appear global. The exercise assumes the stated signatures as synthetic source evidence; it does not claim real cryptographic or handwriting verification. Scope must still be assessed even when the signatory identity is accepted.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/01-alias-register.md](input/sources/01-alias-register.md) — `P03`

> [AL02] Central approver Cora Vale, P-CV, has ordinary approval authority over N01 through N60 throughout September. Delegate Devon Ash, P-DA, has only the narrower scope in the native delegation instrument. Local supervisor Emil Pine, P-EP, has revision A local authority before 15 September. Emil has no ordinary revision B central approval authority. Cora, CV, and central-approver all name P-CV throughout the interval. A correct identity mapping alone does not prove approval scope, timing, or the validity of a permit. Those predicates require their own evidence.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 629, "end_character": 1197, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "f07bfa3668571ccd931251b2f2b44f8c10a9f4323bdc0dac424f76b27fd1b52f", "artifact_directory": "extraction/D00004/attempt-7j0k77x1"}`.

- [input/sources/records/041-n41.md](input/sources/records/041-n41.md) — `P02`

> [N41-01] Release N41-R1 occurred on 20 September at 10:00. Ada signed as north-operator with an active credential. Devon signed approval at 09:00 under his N41-through-N50 delegation effective 18 through 25 September. The unrevoked node permit covered 20 September. Approval and permit histories are complete for this interval. The node number and approval date both fall within delegated scope. The record therefore meets the ordinary revision B route. Devon's signature must not be generalized to nodes outside that explicit range.

Original: [input/originals/D00050.md](input/originals/D00050.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 569, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00050.md", "original_sha256": "b6cdb48aa3d188d1880b4ac0c211bf836b4be4d5a484bbbde29154adda2a3a7d", "artifact_directory": "extraction/D00050/attempt-7_4dnuk5"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0001-c0001-p0001`

> Principal

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 2, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 1, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0001-c0002-p0001`

> Node scope

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 3, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 2, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0001-c0003-p0001`

> Effective start

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 3, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0001-c0004-p0001`

> Effective end

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 5, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 4, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0001-c0005-p0001`

> Power

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 5, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0002-c0001-p0001`

> Devon Ash / P-DA

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 7, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 1, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0002-c0002-p0001`

> N41 through N50 inclusive

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 2, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0002-c0003-p0001`

> 18 September 00:00

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 9, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 3, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0002-c0004-p0001`

> 25 September 23:59

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 4, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0002-c0005-p0001`

> Ordinary revision B approval only

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 11, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 5, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

### Rules

- Select policy by release event time under G02; match dated alias, credential, approval scope and effective permit/exception under G03.
- G04 licenses negative facts only with an applicable complete history or explicit contrary evidence; identity completeness is not event completeness.
- G05 requires dependency review for changed source snapshots; no source supplies an aesthetic criterion.

### Assumptions

- Accept the synthetic signed-source authority and stated completeness within their exact named scope. No world-wide completeness or source authenticity is inferred.

### Reasoning

- 1. The signed delegation covers N41–N50 inclusive from September 18 00:00 through September 25 23:59.
- 2. Node 41 is included and the September 20 approval is strictly inside the authorized interval.

### Limits

- Findings concern named September 2034 events and source-defined roles; unknown N59 permits and N60 events remain unknown.
- Formal targets check reviewed necessary conditions and finite witnesses, not every unspecified event or the authenticity of original signatures. Source paragraph quotations preserve native original paths and semantic markers.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim05` in module `Audit` (supports): `Audit.delegated 41 20 = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target015.lean) · [Actual proof log](logs/target-015.log)

### Recommendation

Retain the scoped approval finding without generalizing to N51.

## C10-ERR-06

### Exact report claim

`input/report.md#C10-ERR-06`

> **C10-ERR-06.** Devon genuine signature authorized N51 without a separate scope requirement.

### Verification question

Did Devon's genuine signature authorize N51 regardless of delegation scope?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P03`

> [G02] Authorization by revision. Policy revision B becomes effective at 00:00 on 15 September. A release at or after that instant requires an active operator credential at release time, a signed approval by a principal with scope over that node at approval time, and an unrevoked permit covering the release. Before that instant, revision A requires an active operator credential and signed local-supervisor approval; no central permit is required. Event time controls historical applicability. Report date, file modification date, and discovery date do not replace the operative timestamp. Successful technical handoff does not itself establish administrative authorization.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 656, "end_character": 1331, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-bd1j4xxu"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-p-0001`

> [AU01] SYNTHETIC SIGNED DELEGATION. Cora Vale grants Devon Ash ordinary revision B approval authority over nodes N41 through N50, effective 18 September 2034 at 00:00 through 25 September at 23:59 inclusive. The node and time restrictions are substantive. A genuine Devon signature outside this scope cannot authorize an approval. The instrument does not grant policy-amendment, exception-granting, credential-issuance, or permit-revocation powers. It also does not let Devon extend his own delegation. Both the node and approval timestamp must be checked against the table.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-p-0014`

> [AU04] DECLINED EXPANSION. Devon requested N51 scope on 20 September, and Cora declined the request pending further review. The delegation amendment history is complete through 30 September and contains no approved N51 expansion. Therefore the sole Devon approval for N51 lacks scope. This conclusion rests on an explicit range, a recorded denial, and a bounded complete amendment history, rather than mere failure to retrieve a document. The same reasoning must not be transferred to a permit history that is expressly incomplete. Strong negative evidence and missing evidence have different logical roles.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/97-request-correspondence.md](input/sources/97-request-correspondence.md) — `P03`

> [REQ02] Devon requested approval scope over N51. Cora declined. A later forwarded email subject reads delegation extension, but its body preserves the declined decision. The complete amendment registry contains no approved expansion during September. The subject line therefore cannot support an N51 authority claim. This correspondence agrees with the operative delegation instrument. A reviewer should cite the actual decision marker and explain why authentic correspondence about a request does not confer the requested power. A source fragment separated from its decision context is an inadequate authorization argument.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 637, "end_character": 1261, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "0f6f5493f82bd9be47fd10b33f21ca7cafd6c294c4ea1e02e97822c2e9762123", "artifact_directory": "extraction/D00008/attempt-dynonhqc"}`.

- [input/sources/records/051-n51.md](input/sources/records/051-n51.md) — `P02`

> [N51-01] Release N51-R1 occurred on 20 September at 10:00 with active Ada and a valid node permit. Devon signed the only approval at 09:00. His delegation covered N41 through N50; his N51 expansion request had been declined. The approval and amendment histories are complete, and no Cora approval or board exception applies. Thus approval lacked scope even though Devon's signature was genuine. A valid permit and authentic signature cannot replace a missing authority predicate in the release conjunction.

Original: [input/originals/D00060.md](input/originals/D00060.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 542, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00060.md", "original_sha256": "8b786848edfc820e1e3356db27b71039c54951bd850e43ee012361454095f055", "artifact_directory": "extraction/D00060/attempt-y9z6nlv_"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P04`

> [EX03] The board-exception register is complete for September and contains only this grant. No second board exception covers N58 or N51. This bounded completeness can support an absence conclusion about board grants for those nodes during that interval. It says nothing about later periods or all imaginable documents. The incomplete N59 permit history supports a different conclusion: its missing permit remains unknown. The audit should identify exactly which completeness premise licenses a negative fact, rather than treating every unsuccessful search as equivalent evidence of absence.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1223, "end_character": 1813, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-y_23t1fp"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0001-c0001-p0001`

> Principal

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 2, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 1, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0001-c0002-p0001`

> Node scope

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 3, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 2, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0001-c0003-p0001`

> Effective start

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 3, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0001-c0004-p0001`

> Effective end

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 5, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 4, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0001-c0005-p0001`

> Power

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[1]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 1, "cell": 5, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0002-c0001-p0001`

> Devon Ash / P-DA

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[1]/w:p[1]", "paragraph_index_in_story": 7, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 1, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0002-c0002-p0001`

> N41 through N50 inclusive

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[2]/w:p[1]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 2, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0002-c0003-p0001`

> 18 September 00:00

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[3]/w:p[1]", "paragraph_index_in_story": 9, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 3, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0002-c0004-p0001`

> 25 September 23:59

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[4]/w:p[1]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 4, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-table-0001-r0002-c0005-p0001`

> Ordinary revision B approval only

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:tbl[1]/w:tr[2]/w:tc[5]/w:p[1]", "paragraph_index_in_story": 11, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "table_index": 1, "row": 2, "cell": 5, "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

### Rules

- Select policy by release event time under G02; match dated alias, credential, approval scope and effective permit/exception under G03.
- G04 licenses negative facts only with an applicable complete history or explicit contrary evidence; identity completeness is not event completeness.
- G05 requires dependency review for changed source snapshots; no source supplies an aesthetic criterion.

### Assumptions

- Accept the synthetic signed-source authority and stated completeness within their exact named scope. No world-wide completeness or source authenticity is inferred.

### Reasoning

- 1. N51 is outside the inclusive N41–N50 grant, and its expansion request was expressly declined.
- 2. Complete approval/amendment histories exclude another approval; the board register excludes an exception. Authenticity cannot replace the required scoped-approval conjunct.

### Limits

- Findings concern named September 2034 events and source-defined roles; unknown N59 permits and N60 events remain unknown.
- Formal targets check reviewed necessary conditions and finite witnesses, not every unspecified event or the authenticity of original signatures. Source paragraph quotations preserve native original paths and semantic markers.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim06` in module `Audit` (refutes): `Audit.delegated 51 20 = false ∧ Audit.routeB true (Audit.delegated 51 20) true = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target016.lean) · [Actual proof log](logs/target-016.log)

### Recommendation

Record that this genuine approval lacked node authority.

## C10-ERR-07

### Exact report claim

`input/report.md#C10-ERR-07`

> **C10-ERR-07.** N57 release was unauthorized because ordinary central approval and permit were absent.

### Verification question

Was N57 unauthorized solely because ordinary central approval/permit were absent?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P04`

> [G03] Hierarchy and identity. Resolve aliases through the dated identity registry. A reused display name does not transfer the former principal's credential. Supersession replaces only the named scope from its stated effective instant. A valid board exception can modify the ordinary route if its node, time, and other conditions match. The board's power to grant exceptions does not establish that a requested exception was granted. Ordinary approval authority does not include authority to rewrite policy. Filename ordering creates no precedence. The applicable hierarchy must be assembled before deciding whether the ordinary permit requirement governs a particular release.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1333, "end_character": 2010, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-bd1j4xxu"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-p-0013`

> [AU03] EXCEPTION AUTHORITY. Only the governance board may issue a signed temporary policy exception for a named node and time window. Cora's ordinary approval authority does not include granting such an exception alone. The board issued one final signed exception in this packet. Its operative text is stored separately from the ordinary node records. A reviewer must locate that actual document and match all conditions. The existence of the power or a pending request does not imply that a grant covers every requested node. A complete search must include applicable rule documents beyond the initial operational retrieval chunk.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 13, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P02`

> [EX01] The governance board grants a temporary exception for node N57 only, effective 22 September 2034 from 09:00 through 12:00 inclusive. During that interval, an active operator credential and signed local approval by Emil satisfy the release route without an ordinary central permit. The board signed under its explicit exception-granting authority. The exception does not cover N58, change credential activation, or extend to other times. N57 release at 10:00 and Emil approval at 09:00 fall inside the stated scope. Every named condition is operative, not illustrative.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 35, "end_character": 610, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-y_23t1fp"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P03`

> [EX02] This grant changes only the ordinary central-approval and permit requirements for the specified N57 window. The request mentioned N58, but the board deliberately excluded it from the final grant. The signed final scope prevails over the earlier proposal. Its location after the operational records does not diminish authority, and its filename creates no independent precedence. An assessor who discovers it must revisit any provisional N57 conclusion made from the general rule alone. Full-corpus rule discovery matters because the exception is separate from the record whose authorization it changes.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 612, "end_character": 1221, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-y_23t1fp"}`.

- [input/sources/records/057-n57.md](input/sources/records/057-n57.md) — `P02`

> [N57-01] Release N57-R1 occurred on 22 September at 10:00 with active Ada signing as aq-main. Emil signed local approval at 09:00. No ordinary central permit is recorded. A reference states that a board maintenance exception governs this release; the operative signed document is elsewhere in the distributed packet. This record does not restate its conditions. The auditor must locate the final grant and compare node, time, credential, and supervisor conditions. Classification from the ordinary rule alone would omit a directly referenced applicable rule.

Original: [input/originals/D00066.md](input/originals/D00066.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 594, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00066.md", "original_sha256": "39862aa177c7d9a9ac22a0389176bfb7506d9771d2432d36759b95a009e4456a", "artifact_directory": "extraction/D00066/attempt-7lh1tr03"}`.

### Rules

- Select policy by release event time under G02; match dated alias, credential, approval scope and effective permit/exception under G03.
- G04 licenses negative facts only with an applicable complete history or explicit contrary evidence; identity completeness is not event completeness.
- G05 requires dependency review for changed source snapshots; no source supplies an aesthetic criterion.

### Assumptions

- Accept the synthetic signed-source authority and stated completeness within their exact named scope. No world-wide completeness or source authenticity is inferred.

### Reasoning

- 1. The final authorized board grant expressly replaces those ordinary requirements for N57 on September 22 09:00–12:00.
- 2. The 10:00 release matches node/time; active Ada and Emil's 09:00 local approval satisfy the exception conditions.
- 3. Using only the general rule ignores an incorporated cross-document exception.

### Limits

- Findings concern named September 2034 events and source-defined roles; unknown N59 permits and N60 events remain unknown.
- Formal targets check reviewed necessary conditions and finite witnesses, not every unspecified event or the authenticity of original signatures. Source paragraph quotations preserve native original paths and semantic markers.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim07` in module `Audit` (refutes): `Audit.exceptionRoute 57 22 10 true true = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target017.lean) · [Actual proof log](logs/target-017.log)

### Recommendation

Recognize this N57 release as authorized under the narrow board exception.

## C10-ERR-08

### Exact report claim

`input/report.md#C10-ERR-08`

> **C10-ERR-08.** The requested two-node exception authorized N58 as well as N57.

### Verification question

Did the two-node request itself extend the final exception to N58?

### Source evidence

- [input/sources/97-request-correspondence.md](input/sources/97-request-correspondence.md) — `P02`

> [REQ01] A supervisor requested a maintenance exception for both N57 and N58 on 21 September, proposing a two-day window. The board answered by issuing only the final signed grant stored separately. A request is not a grant, and no rule expands the final grant to match the original proposal. The correspondence remains in the packet to preserve decision history. Retrieving the proposal without its operative response can make the permission appear broader than it is. The final signed document, valid granting authority, and matched scope govern the release rather than an earlier request headline.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 635, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "0f6f5493f82bd9be47fd10b33f21ca7cafd6c294c4ea1e02e97822c2e9762123", "artifact_directory": "extraction/D00008/attempt-dynonhqc"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-p-0013`

> [AU03] EXCEPTION AUTHORITY. Only the governance board may issue a signed temporary policy exception for a named node and time window. Cora's ordinary approval authority does not include granting such an exception alone. The board issued one final signed exception in this packet. Its operative text is stored separately from the ordinary node records. A reviewer must locate that actual document and match all conditions. The existence of the power or a pending request does not imply that a grant covers every requested node. A complete search must include applicable rule documents beyond the initial operational retrieval chunk.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 13, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-ygv7nv1d"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P02`

> [EX01] The governance board grants a temporary exception for node N57 only, effective 22 September 2034 from 09:00 through 12:00 inclusive. During that interval, an active operator credential and signed local approval by Emil satisfy the release route without an ordinary central permit. The board signed under its explicit exception-granting authority. The exception does not cover N58, change credential activation, or extend to other times. N57 release at 10:00 and Emil approval at 09:00 fall inside the stated scope. Every named condition is operative, not illustrative.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 35, "end_character": 610, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-y_23t1fp"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P03`

> [EX02] This grant changes only the ordinary central-approval and permit requirements for the specified N57 window. The request mentioned N58, but the board deliberately excluded it from the final grant. The signed final scope prevails over the earlier proposal. Its location after the operational records does not diminish authority, and its filename creates no independent precedence. An assessor who discovers it must revisit any provisional N57 conclusion made from the general rule alone. Full-corpus rule discovery matters because the exception is separate from the record whose authorization it changes.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 612, "end_character": 1221, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-y_23t1fp"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P04`

> [EX03] The board-exception register is complete for September and contains only this grant. No second board exception covers N58 or N51. This bounded completeness can support an absence conclusion about board grants for those nodes during that interval. It says nothing about later periods or all imaginable documents. The incomplete N59 permit history supports a different conclusion: its missing permit remains unknown. The audit should identify exactly which completeness premise licenses a negative fact, rather than treating every unsuccessful search as equivalent evidence of absence.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1223, "end_character": 1813, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-y_23t1fp"}`.

- [input/sources/records/058-n58.md](input/sources/records/058-n58.md) — `P02`

> [N58-01] Release N58-R1 occurred on 22 September at 10:00 with active Ada and valid Cora approval. The node permit had been revoked effective 09:00, before release, although its index entry appeared at 11:00. The complete permit history says no replacement existed at 10:00. No board exception covers N58. The record explicitly identifies this release as unauthorized under revision B. This counterexample remains decisive for a global claim even if other nodes have incomplete evidence. Successful administrative handoff is a separate fact.

Original: [input/originals/D00067.md](input/originals/D00067.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 577, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00067.md", "original_sha256": "f9efcebda7ad09423ba369c0c5456d8b70e40fecf276d4d9ce4d14dd79e5f7e9", "artifact_directory": "extraction/D00067/attempt-51ocy3vs"}`.

### Rules

- Select policy by release event time under G02; match dated alias, credential, approval scope and effective permit/exception under G03.
- G04 licenses negative facts only with an applicable complete history or explicit contrary evidence; identity completeness is not event completeness.
- G05 requires dependency review for changed source snapshots; no source supplies an aesthetic criterion.

### Assumptions

- Accept the synthetic signed-source authority and stated completeness within their exact named scope. No world-wide completeness or source authenticity is inferred.

### Reasoning

- 1. The request proposed N57 and N58, but the final signed grant intentionally includes N57 only.
- 2. The board's power to grant and a request do not establish a grant. The complete board register excludes another N58 exception.

### Limits

- Findings concern named September 2034 events and source-defined roles; unknown N59 permits and N60 events remain unknown.
- Formal targets check reviewed necessary conditions and finite witnesses, not every unspecified event or the authenticity of original signatures. Source paragraph quotations preserve native original paths and semantic markers.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim08` in module `Audit` (refutes): `Audit.boardScope 58 22 10 = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target018.lean) · [Actual proof log](logs/target-018.log)

### Recommendation

Apply the final grant's N57-only scope.

## C10-ERR-09

### Exact report claim

`input/report.md#C10-ERR-09`

> **C10-ERR-09.** N58 revocation was ineffective at release because its index entry appeared at 11:00.

### Verification question

Was N58 revocation ineffective at its 10:00 release because indexing occurred at 11:00?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P03`

> [G02] Authorization by revision. Policy revision B becomes effective at 00:00 on 15 September. A release at or after that instant requires an active operator credential at release time, a signed approval by a principal with scope over that node at approval time, and an unrevoked permit covering the release. Before that instant, revision A requires an active operator credential and signed local-supervisor approval; no central permit is required. Event time controls historical applicability. Report date, file modification date, and discovery date do not replace the operative timestamp. Successful technical handoff does not itself establish administrative authorization.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 656, "end_character": 1331, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-bd1j4xxu"}`.

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P04`

> [G03] Hierarchy and identity. Resolve aliases through the dated identity registry. A reused display name does not transfer the former principal's credential. Supersession replaces only the named scope from its stated effective instant. A valid board exception can modify the ordinary route if its node, time, and other conditions match. The board's power to grant exceptions does not establish that a requested exception was granted. Ordinary approval authority does not include authority to rewrite policy. Filename ordering creates no precedence. The applicable hierarchy must be assembled before deciding whether the ordinary permit requirement governs a particular release.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1333, "end_character": 2010, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-bd1j4xxu"}`.

- [input/sources/03-policy-transition.md](input/sources/03-policy-transition.md) — `P04`

> [PV03] N58 permit revocation took effect at 09:00 on 22 September. Its release occurred at 10:00, and the signed revocation was indexed at 11:00. The index timestamp does not postpone the explicit effective time. The complete permit history says no replacement existed at 10:00. No board exception applies to N58. This supplies a concrete unauthorized release and an independent counterexample to a global authorization claim. It does not require inferring absence from a retrieval failure. Technical bundle handoff succeeded, but that fact does not reverse the administrative revocation.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1148, "end_character": 1736, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "49b4f99dd0f7f83a36ca549e0f2e026d83bfef78f82c5b46f4aed7d84b70e6f3", "artifact_directory": "extraction/D00006/attempt-rab6abi1"}`.

- [input/sources/records/058-n58.md](input/sources/records/058-n58.md) — `P02`

> [N58-01] Release N58-R1 occurred on 22 September at 10:00 with active Ada and valid Cora approval. The node permit had been revoked effective 09:00, before release, although its index entry appeared at 11:00. The complete permit history says no replacement existed at 10:00. No board exception covers N58. The record explicitly identifies this release as unauthorized under revision B. This counterexample remains decisive for a global claim even if other nodes have incomplete evidence. Successful administrative handoff is a separate fact.

Original: [input/originals/D00067.md](input/originals/D00067.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 577, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00067.md", "original_sha256": "f9efcebda7ad09423ba369c0c5456d8b70e40fecf276d4d9ce4d14dd79e5f7e9", "artifact_directory": "extraction/D00067/attempt-51ocy3vs"}`.

### Rules

- Select policy by release event time under G02; match dated alias, credential, approval scope and effective permit/exception under G03.
- G04 licenses negative facts only with an applicable complete history or explicit contrary evidence; identity completeness is not event completeness.
- G05 requires dependency review for changed source snapshots; no source supplies an aesthetic criterion.

### Assumptions

- Accept the synthetic signed-source authority and stated completeness within their exact named scope. No world-wide completeness or source authenticity is inferred.

### Reasoning

- 1. The signed revocation explicitly takes effect at 09:00, before release at 10:00.
- 2. Indexing at 11:00 is a later recording event, not the operative time. Complete history confirms no replacement.

### Limits

- Findings concern named September 2034 events and source-defined roles; unknown N59 permits and N60 events remain unknown.
- Formal targets check reviewed necessary conditions and finite witnesses, not every unspecified event or the authenticity of original signatures. Source paragraph quotations preserve native original paths and semantic markers.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim09` in module `Audit` (refutes): `(9 : Nat) < 10 ∧ 10 < 11`.
  [Model](models/Audit.lean) · [Executed check](checks/Target019.lean) · [Actual proof log](logs/target-019.log)

### Recommendation

Use the 09:00 effective time; retain the later index time only as provenance.

## C10-ERR-10

### Exact report claim

`input/report.md#C10-ERR-10`

> **C10-ERR-10.** N59 release was unauthorized because no permit was found in its attachment slot.

### Verification question

Does the absent N59 attachment establish that its release was unauthorized?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P05`

> [G04] Missing and contrary evidence. A missing permit attachment in an expressly incomplete history establishes a missing argument, not proof that no permit existed. A complete bounded permit history can establish absence within its specified interval. An explicitly revoked permit with a statement that no replacement existed is different from an empty search result. One documented unauthorized release refutes a global claim that all recorded releases were authorized, even if other cases remain unknown. Completeness of the node domain does not establish completeness of all release events. A claim of exactly one event needs event-history evidence, not merely a valid authorization for one known event.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2012, "end_character": 2719, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-bd1j4xxu"}`.

- [input/sources/records/059-n59.md](input/sources/records/059-n59.md) — `P02`

> [N59-01] Release N59-R1 occurred on 22 September at 10:00 with active Ada and valid Cora approval. The permit attachment is missing, and the permit history is expressly incomplete. No record states that a permit did not exist, and no revocation is supplied. Authorization is therefore unresolved from this packet. The useful finding is the missing permit argument, not a categorical unauthorized verdict. Identity-domain completeness does not repair this gap. The named release itself is documented; it is the permit prerequisite that lacks evidence.

Original: [input/originals/D00068.md](input/originals/D00068.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 586, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00068.md", "original_sha256": "1728ba1a1c8c8cf5b266060cedc4d913f897ea1d822f544d480b583416d65964", "artifact_directory": "extraction/D00068/attempt-vx92gh4h"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P04`

> [EX03] The board-exception register is complete for September and contains only this grant. No second board exception covers N58 or N51. This bounded completeness can support an absence conclusion about board grants for those nodes during that interval. It says nothing about later periods or all imaginable documents. The incomplete N59 permit history supports a different conclusion: its missing permit remains unknown. The audit should identify exactly which completeness premise licenses a negative fact, rather than treating every unsuccessful search as equivalent evidence of absence.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1223, "end_character": 1813, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-y_23t1fp"}`.

### Rules

- Select policy by release event time under G02; match dated alias, credential, approval scope and effective permit/exception under G03.
- G04 licenses negative facts only with an applicable complete history or explicit contrary evidence; identity completeness is not event completeness.
- G05 requires dependency review for changed source snapshots; no source supplies an aesthetic criterion.

### Assumptions

- Accept the synthetic signed-source authority and stated completeness within their exact named scope. No world-wide completeness or source authenticity is inferred.

### Reasoning

- 1. Active operator and valid Cora approval are documented, but the permit history is expressly incomplete.
- 2. No revocation, complete negative permit record, or other contrary fact is supplied. Full relevant corpus review finds the same unresolved gap, not proof of permit absence.

### Limits

- Findings concern named September 2034 events and source-defined roles; unknown N59 permits and N60 events remain unknown.
- Formal targets check reviewed necessary conditions and finite witnesses, not every unspecified event or the authenticity of original signatures. Source paragraph quotations preserve native original paths and semantic markers.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **blocked**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Request the covering permit/history; report authorization as unresolved rather than categorical failure.

## C10-ERR-11

### Exact report claim

`input/report.md#C10-ERR-11`

> **C10-ERR-11.** N60 had exactly one release throughout September.

### Verification question

Was N60-R1 the sole September release?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P02`

> [G01] Finite identity universe. The invented Lantern Relay service contains exactly sixty nodes, N01 through N60, during September 2034. The node registry is complete for identities, not automatically for all events or all permit histories. Each operational record states its own evidence completeness. A first retrieval window is not the full corpus. Universal assertions require every applicable node and exception, not extrapolation from the first files found. All services, principals, signatures, bundles, and incidents are synthetic; this packet does not prescribe administration of a real distributed service.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 38, "end_character": 654, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-bd1j4xxu"}`.

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P05`

> [G04] Missing and contrary evidence. A missing permit attachment in an expressly incomplete history establishes a missing argument, not proof that no permit existed. A complete bounded permit history can establish absence within its specified interval. An explicitly revoked permit with a statement that no replacement existed is different from an empty search result. One documented unauthorized release refutes a global claim that all recorded releases were authorized, even if other cases remain unknown. Completeness of the node domain does not establish completeness of all release events. A claim of exactly one event needs event-history evidence, not merely a valid authorization for one known event.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2012, "end_character": 2719, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-bd1j4xxu"}`.

- [input/sources/records/060-n60.md](input/sources/records/060-n60.md) — `P02`

> [N60-01] Release N60-R1 occurred on 20 September at 10:00 with active Ada, valid Cora approval, and an unrevoked covering permit. Its authorization records are complete. However, the event-history export is incomplete for 26 through 30 September because an archive connector was unavailable. The packet does not settle whether additional releases occurred during that gap. The known release can be supported as authorized while the assertion of exactly one release in the month remains unsupported. These claims have different completeness requirements.

Original: [input/originals/D00069.md](input/originals/D00069.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 589, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00069.md", "original_sha256": "73a0614627f28487ad0f6807e8055f81271f905e116b55d17de6594eb3e72dfc", "artifact_directory": "extraction/D00069/attempt-chyi2kml"}`.

- [input/sources/04-node-registry.pdf.md](input/sources/04-node-registry.pdf.md) — `pdf-page-0005`

> SYNTHETIC LANTERN RELAY IDENTITY REGISTRY
> [RG05] Sheet 5 enumerates node identities N49 through N60 inclusive. The five sheets jointly
> enumerate exactly N01 through N60 with no duplicates and no additional nodes in the
> September service boundary. Identity membership is the object of this register; it does not
> purport to list every release event or every permit revision.
> [RG05-CUSTODY] Registrar Iona Lake retained this signed synthetic index. The corresponding
> operational records provide named releases and their own bounded completeness statements.
> Reviewers must also inspect the dated alias registry, transition policy, delegation, request
> correspondence, and final board exception. A blank field in an identity index is not a
> permit revocation or proof that no release occurred. The index has no power to expand a
> delegation or change an effective date.
> [RG05-LIMIT] A universal node claim needs the full identity domain and evidence for its
> predicate. A universal release claim additionally needs event-domain completeness. This
> registry supplies the former, not the latter. It does not repair N60’s late-month event gap
> or N59’s permit gap. Keep the original PDF source and sheet marker when citing enumeration.
> All identities and signatures are invented for the evidence-audit exercise.

Original: [input/originals/D00007.pdf](input/originals/D00007.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 5, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0005.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00007.pdf", "original_sha256": "6fbabc6f1ab5af7659201499d292110b7f8e0da5dcf20a6864f09a6dedf439e8", "artifact_directory": "extraction/D00007/attempt-connzlg9"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

### Rules

- Select policy by release event time under G02; match dated alias, credential, approval scope and effective permit/exception under G03.
- G04 licenses negative facts only with an applicable complete history or explicit contrary evidence; identity completeness is not event completeness.
- G05 requires dependency review for changed source snapshots; no source supplies an aesthetic criterion.

### Assumptions

- Accept the synthetic signed-source authority and stated completeness within their exact named scope. No world-wide completeness or source authenticity is inferred.

### Reasoning

- 1. One September 20 authorized release is established, but the event-history export omits September 26–30.
- 2. Complete authorization evidence for the known event does not establish that no additional events occurred; the identity registry cannot repair the event gap.

### Limits

- Findings concern named September 2034 events and source-defined roles; unknown N59 permits and N60 events remain unknown.
- Formal targets check reviewed necessary conditions and finite witnesses, not every unspecified event or the authenticity of original signatures. Source paragraph quotations preserve native original paths and semantic markers.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **blocked**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Retain the known event and request the missing interval export before an exact monthly count.

## C10-ERR-12

### Exact report claim

`input/report.md#C10-ERR-12`

> **C10-ERR-12.** The sixty-node identity registry is a complete list of all September release events.

### Verification question

Is the sixty-node identity registry itself a complete list of September release events?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P02`

> [G01] Finite identity universe. The invented Lantern Relay service contains exactly sixty nodes, N01 through N60, during September 2034. The node registry is complete for identities, not automatically for all events or all permit histories. Each operational record states its own evidence completeness. A first retrieval window is not the full corpus. Universal assertions require every applicable node and exception, not extrapolation from the first files found. All services, principals, signatures, bundles, and incidents are synthetic; this packet does not prescribe administration of a real distributed service.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 38, "end_character": 654, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-bd1j4xxu"}`.

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P05`

> [G04] Missing and contrary evidence. A missing permit attachment in an expressly incomplete history establishes a missing argument, not proof that no permit existed. A complete bounded permit history can establish absence within its specified interval. An explicitly revoked permit with a statement that no replacement existed is different from an empty search result. One documented unauthorized release refutes a global claim that all recorded releases were authorized, even if other cases remain unknown. Completeness of the node domain does not establish completeness of all release events. A claim of exactly one event needs event-history evidence, not merely a valid authorization for one known event.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2012, "end_character": 2719, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-bd1j4xxu"}`.

- [input/sources/04-node-registry.pdf.md](input/sources/04-node-registry.pdf.md) — `pdf-page-0001`

> SYNTHETIC LANTERN RELAY IDENTITY REGISTRY
> [RG01] Sheet 1 enumerates node identities N01 through N12 inclusive. The five sheets jointly
> enumerate exactly N01 through N60 with no duplicates and no additional nodes in the
> September service boundary. Identity membership is the object of this register; it does not
> purport to list every release event or every permit revision.
> [RG01-CUSTODY] Registrar Iona Lake retained this signed synthetic index. The corresponding
> operational records provide named releases and their own bounded completeness statements.
> Reviewers must also inspect the dated alias registry, transition policy, delegation, request
> correspondence, and final board exception. A blank field in an identity index is not a
> permit revocation or proof that no release occurred. The index has no power to expand a
> delegation or change an effective date.
> [RG01-LIMIT] A universal node claim needs the full identity domain and evidence for its
> predicate. A universal release claim additionally needs event-domain completeness. This
> registry supplies the former, not the latter. It does not repair N60’s late-month event gap
> or N59’s permit gap. Keep the original PDF source and sheet marker when citing enumeration.
> All identities and signatures are invented for the evidence-audit exercise.

Original: [input/originals/D00007.pdf](input/originals/D00007.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 1, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0001.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00007.pdf", "original_sha256": "6fbabc6f1ab5af7659201499d292110b7f8e0da5dcf20a6864f09a6dedf439e8", "artifact_directory": "extraction/D00007/attempt-connzlg9"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/04-node-registry.pdf.md](input/sources/04-node-registry.pdf.md) — `pdf-page-0005`

> SYNTHETIC LANTERN RELAY IDENTITY REGISTRY
> [RG05] Sheet 5 enumerates node identities N49 through N60 inclusive. The five sheets jointly
> enumerate exactly N01 through N60 with no duplicates and no additional nodes in the
> September service boundary. Identity membership is the object of this register; it does not
> purport to list every release event or every permit revision.
> [RG05-CUSTODY] Registrar Iona Lake retained this signed synthetic index. The corresponding
> operational records provide named releases and their own bounded completeness statements.
> Reviewers must also inspect the dated alias registry, transition policy, delegation, request
> correspondence, and final board exception. A blank field in an identity index is not a
> permit revocation or proof that no release occurred. The index has no power to expand a
> delegation or change an effective date.
> [RG05-LIMIT] A universal node claim needs the full identity domain and evidence for its
> predicate. A universal release claim additionally needs event-domain completeness. This
> registry supplies the former, not the latter. It does not repair N60’s late-month event gap
> or N59’s permit gap. Keep the original PDF source and sheet marker when citing enumeration.
> All identities and signatures are invented for the evidence-audit exercise.

Original: [input/originals/D00007.pdf](input/originals/D00007.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 5, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0005.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00007.pdf", "original_sha256": "6fbabc6f1ab5af7659201499d292110b7f8e0da5dcf20a6864f09a6dedf439e8", "artifact_directory": "extraction/D00007/attempt-connzlg9"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/records/060-n60.md](input/sources/records/060-n60.md) — `P02`

> [N60-01] Release N60-R1 occurred on 20 September at 10:00 with active Ada, valid Cora approval, and an unrevoked covering permit. Its authorization records are complete. However, the event-history export is incomplete for 26 through 30 September because an archive connector was unavailable. The packet does not settle whether additional releases occurred during that gap. The known release can be supported as authorized while the assertion of exactly one release in the month remains unsupported. These claims have different completeness requirements.

Original: [input/originals/D00069.md](input/originals/D00069.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 589, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00069.md", "original_sha256": "73a0614627f28487ad0f6807e8055f81271f905e116b55d17de6594eb3e72dfc", "artifact_directory": "extraction/D00069/attempt-chyi2kml"}`.

### Rules

- Select policy by release event time under G02; match dated alias, credential, approval scope and effective permit/exception under G03.
- G04 licenses negative facts only with an applicable complete history or explicit contrary evidence; identity completeness is not event completeness.
- G05 requires dependency review for changed source snapshots; no source supplies an aesthetic criterion.

### Assumptions

- Accept the synthetic signed-source authority and stated completeness within their exact named scope. No world-wide completeness or source authenticity is inferred.

### Reasoning

- 1. The registry explicitly enumerates identities and disclaims event/permitting history; its stated object differs from the report's claimed object.
- 2. N60 independently documents an unresolved late-month event export. The artifact therefore cannot be described as the complete event list.
- 3. This refutes the characterization of the registry; it does not prove an additional N60 release occurred.

### Limits

- Findings concern named September 2034 events and source-defined roles; unknown N59 permits and N60 events remain unknown.
- Formal targets check reviewed necessary conditions and finite witnesses, not every unspecified event or the authenticity of original signatures. Source paragraph quotations preserve native original paths and semantic markers.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Describe identity completeness separately from event-history completeness; do not present the registry as an event ledger.

## C10-ERR-13

### Exact report claim

`input/report.md#C10-ERR-13`

> **C10-ERR-13.** An unchanged report hash alone permits reusing its audit after any source mutation.

### Verification question

Can an unchanged report hash alone authorize reusing an audit after any source mutation?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P06`

> [G05] Snapshot provenance. An audit result is bound to exact source bytes, report bytes, inventory, extraction assumptions, and reviewed formal premises. Reuse after a source change requires checking affected premises. An unchanged report hash or unchanged numerical value is insufficient if scope, authority, effective time, or exception text changes elsewhere. Preserve the original snapshot and logs. Reproduction belongs in a distinct repository tmp/ directory with a new source manifest and fingerprint. A prior proof must not be described as validation of changed inputs without reviewing its dependencies. This rule is evidence bookkeeping, not permission to overwrite the baseline corpus.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 11, "start_character": 2721, "end_character": 3417, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-bd1j4xxu"}`.

### Rules

- Select policy by release event time under G02; match dated alias, credential, approval scope and effective permit/exception under G03.
- G04 licenses negative facts only with an applicable complete history or explicit contrary evidence; identity completeness is not event completeness.
- G05 requires dependency review for changed source snapshots; no source supplies an aesthetic criterion.

### Assumptions

- Accept the synthetic signed-source authority and stated completeness within their exact named scope. No world-wide completeness or source authenticity is inferred.

### Reasoning

- 1. G05 binds results to source bytes, inventory, extraction assumptions and premises in addition to report bytes.
- 2. A case with report unchanged, source changed, and dependencies not reviewed violates the explicit review prerequisite.
- 3. The model supplies this counterexample to sufficiency; it does not mutate actual sources or claim a prior proof validates changed evidence.

### Limits

- Findings concern named September 2034 events and source-defined roles; unknown N59 permits and N60 events remain unknown.
- Formal targets check reviewed necessary conditions and finite witnesses, not every unspecified event or the authenticity of original signatures. Source paragraph quotations preserve native original paths and semantic markers.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim13` in module `Audit` (refutes): `∃ reportUnchanged : Bool, reportUnchanged = true ∧ Audit.reviewRequirement true false = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target020.lean) · [Actual proof log](logs/target-020.log)

### Recommendation

Review affected source dependencies and rerun required validation in a retained separate snapshot before reusing results.

## C10-ERR-14

### Exact report claim

`input/report.md#C10-ERR-14`

> **C10-ERR-14.** The distributed archive is pleasantly organized.

### Verification question

Is pleasantly organized a supplied formal property of this distributed archive?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P02`

> [G01] Finite identity universe. The invented Lantern Relay service contains exactly sixty nodes, N01 through N60, during September 2034. The node registry is complete for identities, not automatically for all events or all permit histories. Each operational record states its own evidence completeness. A first retrieval window is not the full corpus. Universal assertions require every applicable node and exception, not extrapolation from the first files found. All services, principals, signatures, bundles, and incidents are synthetic; this packet does not prescribe administration of a real distributed service.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 38, "end_character": 654, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-bd1j4xxu"}`.

### Rules

- Select policy by release event time under G02; match dated alias, credential, approval scope and effective permit/exception under G03.
- G04 licenses negative facts only with an applicable complete history or explicit contrary evidence; identity completeness is not event completeness.
- G05 requires dependency review for changed source snapshots; no source supplies an aesthetic criterion.

### Assumptions

- Accept the synthetic signed-source authority and stated completeness within their exact named scope. No world-wide completeness or source authenticity is inferred.

### Reasoning

- 1. G01 defines a finite identity universe and warns against partial retrieval.
- 2. It supplies no aesthetic or usability metric for pleasant organization. Documented structure alone cannot decide the evaluative assertion.

### Limits

- Findings concern named September 2034 events and source-defined roles; unknown N59 permits and N60 events remain unknown.
- Formal targets check reviewed necessary conditions and finite witnesses, not every unspecified event or the authenticity of original signatures. Source paragraph quotations preserve native original paths and semantic markers.

### Result

Semantic state: **not_applicable**; argument status: **nonformal**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Treat this as an opinion or define an assessment criterion.
