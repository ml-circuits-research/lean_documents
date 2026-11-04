# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

[Semantic correspondence review](semantic-review.md)

Extraction inventory: 69 documents; 0 pending, partial or blocked. See [ingestion details](ingestion.json) and [coverage](coverage.md).

## C10-OK-01

### Exact report claim

`input/report.md#C10-OK-01`

> **C10-OK-01.** The finite identity registry contains exactly sixty nodes N01 through N60.
> 
> Citations: sources/00-governance.md#[G01]; sources/04-node-registry.pdf#[RG01]; sources/04-node-registry.pdf#[RG05].

### Verification question

Does the complete finite identity registry contain exactly 60 nodes N01 through N60?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P02`

> [G01] Finite identity universe. The invented Lantern Relay service contains exactly sixty nodes, N01 through N60, during September 2034. The node registry is complete for identities, not automatically for all events or all permit histories. Each operational record states its own evidence completeness. A first retrieval window is not the full corpus. Universal assertions require every applicable node and exception, not extrapolation from the first files found. All services, principals, signatures, bundles, and incidents are synthetic; this packet does not prescribe administration of a real distributed service.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 38, "end_character": 654, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-wbqvz0qn"}`.

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
Coordinates: `{"kind": "pdf", "page": 1, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0001.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00007.pdf", "original_sha256": "6fbabc6f1ab5af7659201499d292110b7f8e0da5dcf20a6864f09a6dedf439e8", "artifact_directory": "extraction/D00007/attempt-y0b_3esl"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/04-node-registry.pdf.md](input/sources/04-node-registry.pdf.md) — `pdf-page-0002`

> SYNTHETIC LANTERN RELAY IDENTITY REGISTRY
> [RG02] Sheet 2 enumerates node identities N13 through N24 inclusive. The five sheets jointly
> enumerate exactly N01 through N60 with no duplicates and no additional nodes in the
> September service boundary. Identity membership is the object of this register; it does not
> purport to list every release event or every permit revision.
> [RG02-CUSTODY] Registrar Iona Lake retained this signed synthetic index. The corresponding
> operational records provide named releases and their own bounded completeness statements.
> Reviewers must also inspect the dated alias registry, transition policy, delegation, request
> correspondence, and final board exception. A blank field in an identity index is not a
> permit revocation or proof that no release occurred. The index has no power to expand a
> delegation or change an effective date.
> [RG02-LIMIT] A universal node claim needs the full identity domain and evidence for its
> predicate. A universal release claim additionally needs event-domain completeness. This
> registry supplies the former, not the latter. It does not repair N60’s late-month event gap
> or N59’s permit gap. Keep the original PDF source and sheet marker when citing enumeration.
> All identities and signatures are invented for the evidence-audit exercise.

Original: [input/originals/D00007.pdf](input/originals/D00007.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00007.pdf", "original_sha256": "6fbabc6f1ab5af7659201499d292110b7f8e0da5dcf20a6864f09a6dedf439e8", "artifact_directory": "extraction/D00007/attempt-y0b_3esl"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/04-node-registry.pdf.md](input/sources/04-node-registry.pdf.md) — `pdf-page-0003`

> SYNTHETIC LANTERN RELAY IDENTITY REGISTRY
> [RG03] Sheet 3 enumerates node identities N25 through N36 inclusive. The five sheets jointly
> enumerate exactly N01 through N60 with no duplicates and no additional nodes in the
> September service boundary. Identity membership is the object of this register; it does not
> purport to list every release event or every permit revision.
> [RG03-CUSTODY] Registrar Iona Lake retained this signed synthetic index. The corresponding
> operational records provide named releases and their own bounded completeness statements.
> Reviewers must also inspect the dated alias registry, transition policy, delegation, request
> correspondence, and final board exception. A blank field in an identity index is not a
> permit revocation or proof that no release occurred. The index has no power to expand a
> delegation or change an effective date.
> [RG03-LIMIT] A universal node claim needs the full identity domain and evidence for its
> predicate. A universal release claim additionally needs event-domain completeness. This
> registry supplies the former, not the latter. It does not repair N60’s late-month event gap
> or N59’s permit gap. Keep the original PDF source and sheet marker when citing enumeration.
> All identities and signatures are invented for the evidence-audit exercise.

Original: [input/originals/D00007.pdf](input/originals/D00007.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 3, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0003.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00007.pdf", "original_sha256": "6fbabc6f1ab5af7659201499d292110b7f8e0da5dcf20a6864f09a6dedf439e8", "artifact_directory": "extraction/D00007/attempt-y0b_3esl"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/04-node-registry.pdf.md](input/sources/04-node-registry.pdf.md) — `pdf-page-0004`

> SYNTHETIC LANTERN RELAY IDENTITY REGISTRY
> [RG04] Sheet 4 enumerates node identities N37 through N48 inclusive. The five sheets jointly
> enumerate exactly N01 through N60 with no duplicates and no additional nodes in the
> September service boundary. Identity membership is the object of this register; it does not
> purport to list every release event or every permit revision.
> [RG04-CUSTODY] Registrar Iona Lake retained this signed synthetic index. The corresponding
> operational records provide named releases and their own bounded completeness statements.
> Reviewers must also inspect the dated alias registry, transition policy, delegation, request
> correspondence, and final board exception. A blank field in an identity index is not a
> permit revocation or proof that no release occurred. The index has no power to expand a
> delegation or change an effective date.
> [RG04-LIMIT] A universal node claim needs the full identity domain and evidence for its
> predicate. A universal release claim additionally needs event-domain completeness. This
> registry supplies the former, not the latter. It does not repair N60’s late-month event gap
> or N59’s permit gap. Keep the original PDF source and sheet marker when citing enumeration.
> All identities and signatures are invented for the evidence-audit exercise.

Original: [input/originals/D00007.pdf](input/originals/D00007.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 4, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0004.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00007.pdf", "original_sha256": "6fbabc6f1ab5af7659201499d292110b7f8e0da5dcf20a6864f09a6dedf439e8", "artifact_directory": "extraction/D00007/attempt-y0b_3esl"}`.

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
Coordinates: `{"kind": "pdf", "page": 5, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0005.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00007.pdf", "original_sha256": "6fbabc6f1ab5af7659201499d292110b7f8e0da5dcf20a6864f09a6dedf439e8", "artifact_directory": "extraction/D00007/attempt-y0b_3esl"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

### Rules

- Use all five complete registry sheets for identity membership, without extending completeness to release or permit histories.

### Assumptions

- The synthetic signed source records are accepted as documentary premises, without a claim of external cryptographic authentication.
- All comparisons use the source September 2034 dates and common clock; distinct approval, release, effective and indexing times are preserved.
- Completeness is limited to the identity, permit, authority-amendment, board-grant or event domain explicitly named by each source.

### Reasoning

- 1. Visually inspected sheets enumerate contiguous ranges1–12,13–24,25–36,37–48,49–60, expressly with no duplicates or additional nodes.
- 2. Each range has12 identities; five ranges give60. The model enumerates1 through 60, checks length60, no duplicates and endpoints1/60.
- 3. All60 operational-record files were also read, but their existence is corroboration rather than a substitute for registry completeness.

### Limits

- The result concerns the named September 2034 node/release and reviewed source snapshot. It does not certify future service behavior or an exhaustive event history for all nodes.
- Identity enumeration does not establish exactly 60 release events or complete permit histories.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.sixtyNodes` in module `Audit` (supports): `Audit.nodes.length = 60 ∧ Audit.nodes.Nodup ∧ Audit.nodes.head? = some 1 ∧ Audit.nodes.getLast? = some 60`.
  [Model](models/Audit.lean) · [Executed check](checks/Target014.lean) · [Actual proof log](logs/target-014.log)

### Recommendation

Retain the finding and its source-defined scope.

## C10-OK-02

### Exact report claim

`input/report.md#C10-OK-02`

> **C10-OK-02.** N04 historical release was authorized under revision A without a central permit.
> 
> Citations: sources/records/004-n04.md#[N04-01]; sources/03-policy-transition.md#[PV01].

### Verification question

Was N04-R1 on September 14 authorized by revisionA despite no central permit?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P03`

> [G02] Authorization by revision. Policy revision B becomes effective at 00:00 on 15 September. A release at or after that instant requires an active operator credential at release time, a signed approval by a principal with scope over that node at approval time, and an unrevoked permit covering the release. Before that instant, revision A requires an active operator credential and signed local-supervisor approval; no central permit is required. Event time controls historical applicability. Report date, file modification date, and discovery date do not replace the operative timestamp. Successful technical handoff does not itself establish administrative authorization.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 656, "end_character": 1331, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-wbqvz0qn"}`.

- [input/sources/01-alias-register.md](input/sources/01-alias-register.md) — `P02`

> [AL01] Principal Ada Quill has immutable identifier P-AQ. Alias north-operator identifies Ada from 1 through 20 September inclusive. From 21 September the same alias identifies Ben Rook, P-BR. Ada uses aq-main from 21 September onward. Ada's credential is active throughout September. Ben's credential becomes active on 22 September. Therefore a 21 September north-operator signature names Ben before his activation, not Ada. The alias transfer and credential activation are distinct events. Copying an older alias mapping without its dates supplies the wrong principal for the later event.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 37, "end_character": 627, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "f07bfa3668571ccd931251b2f2b44f8c10a9f4323bdc0dac424f76b27fd1b52f", "artifact_directory": "extraction/D00004/attempt-hri0cwue"}`.

- [input/sources/01-alias-register.md](input/sources/01-alias-register.md) — `P03`

> [AL02] Central approver Cora Vale, P-CV, has ordinary approval authority over N01 through N60 throughout September. Delegate Devon Ash, P-DA, has only the narrower scope in the native delegation instrument. Local supervisor Emil Pine, P-EP, has revision A local authority before 15 September. Emil has no ordinary revision B central approval authority. Cora, CV, and central-approver all name P-CV throughout the interval. A correct identity mapping alone does not prove approval scope, timing, or the validity of a permit. Those predicates require their own evidence.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 629, "end_character": 1197, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "f07bfa3668571ccd931251b2f2b44f8c10a9f4323bdc0dac424f76b27fd1b52f", "artifact_directory": "extraction/D00004/attempt-hri0cwue"}`.

- [input/sources/03-policy-transition.md](input/sources/03-policy-transition.md) — `P02`

> [PV01] Revision A governs the N04 release on 14 September. Active Ada and local-supervisor Emil approval satisfy its route without a central permit. A report written after revision B takes effect does not retroactively impose that newer rule. The historical event and any later release of the same node are separate objects. This source defines applicability; the operational record provides the event details. The reviewer should cite both when explaining the historical authorization claim rather than assume that a current-policy headline applies to every date.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 45, "end_character": 609, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "49b4f99dd0f7f83a36ca549e0f2e026d83bfef78f82c5b46f4aed7d84b70e6f3", "artifact_directory": "extraction/D00006/attempt-np40ixtc"}`.

- [input/sources/records/004-n04.md](input/sources/records/004-n04.md) — `P02`

> [N04-01] Historical release N04-R1 occurred on 14 September at 10:00 under revision A. Ada's credential was active, and local supervisor Emil signed approval at 09:00. No central permit existed because that historical route did not require one. The named release history is complete. The later report date does not change event time. The release satisfied its applicable route. This conclusion says nothing about a hypothetical later release of the same node, which would need its own date, operator, approval, and permit assessment.

Original: [input/originals/D00013.md](input/originals/D00013.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 569, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00013.md", "original_sha256": "8ae3d6603a916a292b6c6a9d677540daf14dd0608e55371979277a5198f3265b", "artifact_directory": "extraction/D00013/attempt-ru7fbpa2"}`.

### Rules

- G02/PV01 apply revisionA before September 15 00:00, requiring active operator plus signed local-supervisor approval; central permit is not a premise.

### Assumptions

- The synthetic signed source records are accepted as documentary premises, without a claim of external cryptographic authentication.
- All comparisons use the source September 2034 dates and common clock; distinct approval, release, effective and indexing times are preserved.
- Completeness is limited to the identity, permit, authority-amendment, board-grant or event domain explicitly named by each source.

### Reasoning

- 1. N04-R1 occurred September 14 10:00, before the transition. Ada was active and Emil signed local approval at 09:00.
- 2. AL02 identifies Emil local authority for revisionA, and N04 confirms no central permit existed because that route did not require one.
- 3. The model selects the historical branch and proves authorization with permit=false. Later report date cannot import revisionB retroactively.

### Limits

- The result concerns the named September 2034 node/release and reviewed source snapshot. It does not certify future service behavior or an exhaustive event history for all nodes.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.historicalAuthorized` in module `Audit` (supports): `Audit.revisionB Audit.n04.time = false ∧ Audit.n04.permit = false ∧ Audit.ordinaryRoute Audit.n04 = true ∧ Audit.authorized Audit.n04 = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target015.lean) · [Actual proof log](logs/target-015.log)

### Recommendation

Retain the finding and its source-defined scope.

## C10-OK-03

### Exact report claim

`input/report.md#C10-OK-03`

> **C10-OK-03.** N09 release on 21 September lacked an in-force permit.
> 
> Citations: sources/records/009-n09.md#[N09-01]; sources/03-policy-transition.md#[PV02].

### Verification question

Did N09-R1 at September 21 10:00 lack any in-force permit?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P03`

> [G02] Authorization by revision. Policy revision B becomes effective at 00:00 on 15 September. A release at or after that instant requires an active operator credential at release time, a signed approval by a principal with scope over that node at approval time, and an unrevoked permit covering the release. Before that instant, revision A requires an active operator credential and signed local-supervisor approval; no central permit is required. Event time controls historical applicability. Report date, file modification date, and discovery date do not replace the operative timestamp. Successful technical handoff does not itself establish administrative authorization.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 656, "end_character": 1331, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-wbqvz0qn"}`.

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P05`

> [G04] Missing and contrary evidence. A missing permit attachment in an expressly incomplete history establishes a missing argument, not proof that no permit existed. A complete bounded permit history can establish absence within its specified interval. An explicitly revoked permit with a statement that no replacement existed is different from an empty search result. One documented unauthorized release refutes a global claim that all recorded releases were authorized, even if other cases remain unknown. Completeness of the node domain does not establish completeness of all release events. A claim of exactly one event needs event-history evidence, not merely a valid authorization for one known event.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2012, "end_character": 2719, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-wbqvz0qn"}`.

- [input/sources/03-policy-transition.md](input/sources/03-policy-transition.md) — `P03`

> [PV02] N09 permit P09-v1 covered releases through 19 September at 23:59. P09-v2 took effect at 00:00 on 20 September and superseded v1 for later releases. Version 2 covered 20 September only. The N09 release at 10:00 on 21 September lies outside both operative windows. The complete N09 permit history states that no replacement or extension existed at that time. Preserving an old permit file does not preserve its operative authority. An auditor must retain its expiry and named supersession clause when quoting a favorable headline.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 611, "end_character": 1146, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "49b4f99dd0f7f83a36ca549e0f2e026d83bfef78f82c5b46f4aed7d84b70e6f3", "artifact_directory": "extraction/D00006/attempt-np40ixtc"}`.

- [input/sources/records/009-n09.md](input/sources/records/009-n09.md) — `P02`

> [N09-01] Release N09-R1 occurred on 21 September at 10:00. Ada signed as aq-main with an active credential, and Cora approval was valid. P09-v1 had expired and been superseded; P09-v2 covered only 20 September. The complete permit history states no extension or replacement existed at release. Therefore the release lacked an in-force permit under revision B. Both permit versions remain archived for traceability. Their presence in the packet does not mean both remain operative. Technical handoff succeeded despite the missing valid permit.

Original: [input/originals/D00018.md](input/originals/D00018.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 578, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00018.md", "original_sha256": "c81c27f0268253c07bb914ab61f28f5b45a1dc13911e14ed16455a66b2881d08", "artifact_directory": "extraction/D00018/attempt-xfs63z_l"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P04`

> [EX03] The board-exception register is complete for September and contains only this grant. No second board exception covers N58 or N51. This bounded completeness can support an absence conclusion about board grants for those nodes during that interval. It says nothing about later periods or all imaginable documents. The incomplete N59 permit history supports a different conclusion: its missing permit remains unknown. The audit should identify exactly which completeness premise licenses a negative fact, rather than treating every unsuccessful search as equivalent evidence of absence.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1223, "end_character": 1813, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-4om_x9tp"}`.

### Rules

- Superseded/expired permits do not remain operative merely because archived. Complete named permit history licenses no-replacement conclusion.

### Assumptions

- The synthetic signed source records are accepted as documentary premises, without a claim of external cryptographic authentication.
- All comparisons use the source September 2034 dates and common clock; distinct approval, release, effective and indexing times are preserved.
- Completeness is limited to the identity, permit, authority-amendment, board-grant or event domain explicitly named by each source.

### Reasoning

- 1. PV02 ends v1 on September 19 23:59 and makes v2 effective September 20 00:00 for that day only.
- 2. Release September 21 10:00 is later than both final coverage bounds; the model evaluates both available windows false.
- 3. PV02/N09 explicitly close permit history and exclude any extension or replacement at release. Board-grant register EX03 supplies no relevant exception. This is affirmative bounded absence, not an empty search.

### Limits

- The result concerns the named September 2034 node/release and reviewed source snapshot. It does not certify future service behavior or an exhaustive event history for all nodes.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.n09PermitFailure` in module `Audit` (supports): `Audit.minuteAt 19 23 59 < Audit.minuteAt 21 10 0 ∧ Audit.minuteAt 20 23 59 < Audit.minuteAt 21 10 0 ∧ Audit.n09PermitAt (Audit.minuteAt 21 10 0) = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target016.lean) · [Actual proof log](logs/target-016.log)

### Recommendation

Retain the finding and its source-defined scope.

## C10-OK-04

### Exact report claim

`input/report.md#C10-OK-04`

> **C10-OK-04.** The north-operator alias identifies Ben on 21 September, before his credential activated.
> 
> Citations: sources/01-alias-register.md#[AL01]; sources/records/021-n21.md#[N21-01].

### Verification question

Does north-operator name Ben on September 21 before his September 22 activation?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P04`

> [G03] Hierarchy and identity. Resolve aliases through the dated identity registry. A reused display name does not transfer the former principal's credential. Supersession replaces only the named scope from its stated effective instant. A valid board exception can modify the ordinary route if its node, time, and other conditions match. The board's power to grant exceptions does not establish that a requested exception was granted. Ordinary approval authority does not include authority to rewrite policy. Filename ordering creates no precedence. The applicable hierarchy must be assembled before deciding whether the ordinary permit requirement governs a particular release.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1333, "end_character": 2010, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-wbqvz0qn"}`.

- [input/sources/01-alias-register.md](input/sources/01-alias-register.md) — `P02`

> [AL01] Principal Ada Quill has immutable identifier P-AQ. Alias north-operator identifies Ada from 1 through 20 September inclusive. From 21 September the same alias identifies Ben Rook, P-BR. Ada uses aq-main from 21 September onward. Ada's credential is active throughout September. Ben's credential becomes active on 22 September. Therefore a 21 September north-operator signature names Ben before his activation, not Ada. The alias transfer and credential activation are distinct events. Copying an older alias mapping without its dates supplies the wrong principal for the later event.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 37, "end_character": 627, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "f07bfa3668571ccd931251b2f2b44f8c10a9f4323bdc0dac424f76b27fd1b52f", "artifact_directory": "extraction/D00004/attempt-hri0cwue"}`.

- [input/sources/01-alias-register.md](input/sources/01-alias-register.md) — `P04`

> [AL03] The identity registrar signed this mapping and marked it complete for the named aliases during September. No supplied amendment changes the 21 September reassignment. An unsigned chat reference cannot amend the registry. The completeness assertion concerns those names and dates, not every possible identity in the world. The original source path and dated marker should accompany any extracted identity assertion. Searching only for a repeated display name deliberately misses the temporal distinction in this case. A reviewer must preserve the precise release date when linking the signature to a principal and credential.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1199, "end_character": 1830, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "f07bfa3668571ccd931251b2f2b44f8c10a9f4323bdc0dac424f76b27fd1b52f", "artifact_directory": "extraction/D00004/attempt-hri0cwue"}`.

- [input/sources/records/021-n21.md](input/sources/records/021-n21.md) — `P02`

> [N21-01] Release N21-R1 occurred on 21 September at 10:00 and was signed as north-operator. The dated registry maps that alias to Ben on this date. His credential did not activate until 22 September. Cora approval and the node permit were valid, but the operator prerequisite failed. The identity history for this release is complete. An earlier north-operator signature by Ada cannot supply the identity or credential for this later signature. The failure is affirmative dated evidence, not merely an unspecified operator field.

Original: [input/originals/D00030.md](input/originals/D00030.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 565, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00030.md", "original_sha256": "951c437910474727128a851bc902672edc6ec94fc017611403480863a6a9ff56", "artifact_directory": "extraction/D00030/attempt-1hjdli34"}`.

### Rules

- Dated alias identity and credential activation are separate predicates; an old holder credential does not transfer with a display name.

### Assumptions

- The synthetic signed source records are accepted as documentary premises, without a claim of external cryptographic authentication.
- All comparisons use the source September 2034 dates and common clock; distinct approval, release, effective and indexing times are preserved.
- Completeness is limited to the identity, permit, authority-amendment, board-grant or event domain explicitly named by each source.

### Reasoning

- 1. AL01 assigns north-operator to Ada through September 20 inclusive, then Ben from September 21. AL03 closes amendments for this alias/date.
- 2. N21 release signature at September 21 10:00 therefore names Ben, not Ada.
- 3. Ben activation begins September 22, so he is inactive at the release. The finite model checks the dated mapping and the failed credential predicate.

### Limits

- The result concerns the named September 2034 node/release and reviewed source snapshot. It does not certify future service behavior or an exhaustive event history for all nodes.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.aliasBeforeActivation` in module `Audit` (supports): `Audit.northAlias (Audit.minuteAt 21 10 0) = Audit.Principal.ben ∧ Audit.active (Audit.northAlias (Audit.minuteAt 21 10 0)) (Audit.minuteAt 21 10 0) = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target017.lean) · [Actual proof log](logs/target-017.log)

### Recommendation

Retain the finding and its source-defined scope.

## C10-OK-05

### Exact report claim

`input/report.md#C10-OK-05`

> **C10-OK-05.** Devon approval of N41 on 20 September lies within delegated node and time scope.
> 
> Citations: sources/02-delegation.docx#[AU01]; sources/records/041-n41.md#[N41-01].

### Verification question

Does Devon N41 approval at September 20 09:00 satisfy both delegation bounds?

### Source evidence

- [input/sources/01-alias-register.md](input/sources/01-alias-register.md) — `P03`

> [AL02] Central approver Cora Vale, P-CV, has ordinary approval authority over N01 through N60 throughout September. Delegate Devon Ash, P-DA, has only the narrower scope in the native delegation instrument. Local supervisor Emil Pine, P-EP, has revision A local authority before 15 September. Emil has no ordinary revision B central approval authority. Cora, CV, and central-approver all name P-CV throughout the interval. A correct identity mapping alone does not prove approval scope, timing, or the validity of a permit. Those predicates require their own evidence.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 629, "end_character": 1197, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "f07bfa3668571ccd931251b2f2b44f8c10a9f4323bdc0dac424f76b27fd1b52f", "artifact_directory": "extraction/D00004/attempt-hri0cwue"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-p-0001`

> [AU01] SYNTHETIC SIGNED DELEGATION. Cora Vale grants Devon Ash ordinary revision B approval authority over nodes N41 through N50, effective 18 September 2034 at 00:00 through 25 September at 23:59 inclusive. The node and time restrictions are substantive. A genuine Devon signature outside this scope cannot authorize an approval. The instrument does not grant policy-amendment, exception-granting, credential-issuance, or permit-revocation powers. It also does not let Devon extend his own delegation. Both the node and approval timestamp must be checked against the table.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-m18o933_"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-p-0012`

> [AU02] AUTHENTICITY AND PROVENANCE. Cora signs under her standing central approval charter. The native document is the operative delegation, while requests and forwarded messages are historical correspondence. Creation time is distinct from effective time. A derived extraction must preserve all table columns and restrictions. Removing the node interval from a snippet can make a narrow grant appear global. The exercise assumes the stated signatures as synthetic source evidence; it does not claim real cryptographic or handwriting verification. Scope must still be assessed even when the signatory identity is accepted.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[2]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-m18o933_"}`.

- [input/sources/records/041-n41.md](input/sources/records/041-n41.md) — `P02`

> [N41-01] Release N41-R1 occurred on 20 September at 10:00. Ada signed as north-operator with an active credential. Devon signed approval at 09:00 under his N41-through-N50 delegation effective 18 through 25 September. The unrevoked node permit covered 20 September. Approval and permit histories are complete for this interval. The node number and approval date both fall within delegated scope. The record therefore meets the ordinary revision B route. Devon's signature must not be generalized to nodes outside that explicit range.

Original: [input/originals/D00050.md](input/originals/D00050.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 569, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00050.md", "original_sha256": "b6cdb48aa3d188d1880b4ac0c211bf836b4be4d5a484bbbde29154adda2a3a7d", "artifact_directory": "extraction/D00050/attempt-c5rxl551"}`.

### Rules

- AU01 and its original DOCX table grant ordinary revisionB approval for N41-N50 inclusive from September 18 00:00 through September 25 23:59 inclusive.

### Assumptions

- The synthetic signed source records are accepted as documentary premises, without a claim of external cryptographic authentication.
- All comparisons use the source September 2034 dates and common clock; distinct approval, release, effective and indexing times are preserved.
- Completeness is limited to the identity, permit, authority-amendment, board-grant or event domain explicitly named by each source.

### Reasoning

- 1. N41 lies at the included lower node boundary. N41 record gives Devon approval September 20 09:00.
- 2. That instant lies after September 18 00:00 and before September 25 23:59. The complete original table and paragraph agree.
- 3. The model checks both node and time scope. This does not grant Devon policy-amendment or exception power.

### Limits

- The result concerns the named September 2034 node/release and reviewed source snapshot. It does not certify future service behavior or an exhaustive event history for all nodes.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.devonN41` in module `Audit` (supports): `Audit.scope Audit.Principal.devon 41 (Audit.minuteAt 20 9 0) = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target018.lean) · [Actual proof log](logs/target-018.log)

### Recommendation

Retain the finding and its source-defined scope.

## C10-OK-06

### Exact report claim

`input/report.md#C10-OK-06`

> **C10-OK-06.** Devon approval of N51 lacked delegated scope.
> 
> Citations: sources/02-delegation.docx#[AU04]; sources/records/051-n51.md#[N51-01].

### Verification question

Did Devon sole N51 approval lack scope despite authentic signature?

### Source evidence

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-p-0001`

> [AU01] SYNTHETIC SIGNED DELEGATION. Cora Vale grants Devon Ash ordinary revision B approval authority over nodes N41 through N50, effective 18 September 2034 at 00:00 through 25 September at 23:59 inclusive. The node and time restrictions are substantive. A genuine Devon signature outside this scope cannot authorize an approval. The instrument does not grant policy-amendment, exception-granting, credential-issuance, or permit-revocation powers. It also does not let Devon extend his own delegation. Both the node and approval timestamp must be checked against the table.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[1]", "paragraph_index_in_story": 1, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-m18o933_"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-p-0014`

> [AU04] DECLINED EXPANSION. Devon requested N51 scope on 20 September, and Cora declined the request pending further review. The delegation amendment history is complete through 30 September and contains no approved N51 expansion. Therefore the sole Devon approval for N51 lacks scope. This conclusion rests on an explicit range, a recorded denial, and a bounded complete amendment history, rather than mere failure to retrieve a document. The same reasoning must not be transferred to a permit history that is expressly incomplete. Strong negative evidence and missing evidence have different logical roles.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-m18o933_"}`.

- [input/sources/97-request-correspondence.md](input/sources/97-request-correspondence.md) — `P03`

> [REQ02] Devon requested approval scope over N51. Cora declined. A later forwarded email subject reads delegation extension, but its body preserves the declined decision. The complete amendment registry contains no approved expansion during September. The subject line therefore cannot support an N51 authority claim. This correspondence agrees with the operative delegation instrument. A reviewer should cite the actual decision marker and explain why authentic correspondence about a request does not confer the requested power. A source fragment separated from its decision context is an inadequate authorization argument.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 637, "end_character": 1261, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "0f6f5493f82bd9be47fd10b33f21ca7cafd6c294c4ea1e02e97822c2e9762123", "artifact_directory": "extraction/D00008/attempt-_68f__gq"}`.

- [input/sources/records/051-n51.md](input/sources/records/051-n51.md) — `P02`

> [N51-01] Release N51-R1 occurred on 20 September at 10:00 with active Ada and a valid node permit. Devon signed the only approval at 09:00. His delegation covered N41 through N50; his N51 expansion request had been declined. The approval and amendment histories are complete, and no Cora approval or board exception applies. Thus approval lacked scope even though Devon's signature was genuine. A valid permit and authentic signature cannot replace a missing authority predicate in the release conjunction.

Original: [input/originals/D00060.md](input/originals/D00060.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 542, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00060.md", "original_sha256": "8b786848edfc820e1e3356db27b71039c54951bd850e43ee012361454095f055", "artifact_directory": "extraction/D00060/attempt-5ouls4hd"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P04`

> [EX03] The board-exception register is complete for September and contains only this grant. No second board exception covers N58 or N51. This bounded completeness can support an absence conclusion about board grants for those nodes during that interval. It says nothing about later periods or all imaginable documents. The incomplete N59 permit history supports a different conclusion: its missing permit remains unknown. The audit should identify exactly which completeness premise licenses a negative fact, rather than treating every unsuccessful search as equivalent evidence of absence.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1223, "end_character": 1813, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-4om_x9tp"}`.

### Rules

- A signed approval requires node authority; denied expansion plus complete amendment history cannot be treated as a grant.

### Assumptions

- The synthetic signed source records are accepted as documentary premises, without a claim of external cryptographic authentication.
- All comparisons use the source September 2034 dates and common clock; distinct approval, release, effective and indexing times are preserved.
- Completeness is limited to the identity, permit, authority-amendment, board-grant or event domain explicitly named by each source.

### Reasoning

- 1. N51 lies above the delegated upper bound N50; approval September 20 being inside the time interval does not fix the node mismatch.
- 2. AU04 and REQ02 record a declined expansion and no approved amendment through September 30; a forwarded extension subject line preserves that denial.
- 3. N51 identifies Devon as sole approver with no Cora approval or board exception. The model checks the exact range failure, supported by explicit closed amendment/grant records.

### Limits

- The result concerns the named September 2034 node/release and reviewed source snapshot. It does not certify future service behavior or an exhaustive event history for all nodes.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.devonN51` in module `Audit` (supports): `Audit.scope Audit.Principal.devon 51 (Audit.minuteAt 20 9 0) = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target019.lean) · [Actual proof log](logs/target-019.log)

### Recommendation

Retain the finding and its source-defined scope.

## C10-OK-07

### Exact report claim

`input/report.md#C10-OK-07`

> **C10-OK-07.** N57 release at 10:00 on 22 September was authorized by the signed board exception.
> 
> Citations: sources/98-board-exception.md#[EX01]; sources/records/057-n57.md#[N57-01]; sources/02-delegation.docx#[AU03].

### Verification question

Was N57-R1 September 22 10:00 authorized through the final board exception?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P03`

> [G02] Authorization by revision. Policy revision B becomes effective at 00:00 on 15 September. A release at or after that instant requires an active operator credential at release time, a signed approval by a principal with scope over that node at approval time, and an unrevoked permit covering the release. Before that instant, revision A requires an active operator credential and signed local-supervisor approval; no central permit is required. Event time controls historical applicability. Report date, file modification date, and discovery date do not replace the operative timestamp. Successful technical handoff does not itself establish administrative authorization.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 656, "end_character": 1331, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-wbqvz0qn"}`.

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P04`

> [G03] Hierarchy and identity. Resolve aliases through the dated identity registry. A reused display name does not transfer the former principal's credential. Supersession replaces only the named scope from its stated effective instant. A valid board exception can modify the ordinary route if its node, time, and other conditions match. The board's power to grant exceptions does not establish that a requested exception was granted. Ordinary approval authority does not include authority to rewrite policy. Filename ordering creates no precedence. The applicable hierarchy must be assembled before deciding whether the ordinary permit requirement governs a particular release.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1333, "end_character": 2010, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-wbqvz0qn"}`.

- [input/sources/01-alias-register.md](input/sources/01-alias-register.md) — `P02`

> [AL01] Principal Ada Quill has immutable identifier P-AQ. Alias north-operator identifies Ada from 1 through 20 September inclusive. From 21 September the same alias identifies Ben Rook, P-BR. Ada uses aq-main from 21 September onward. Ada's credential is active throughout September. Ben's credential becomes active on 22 September. Therefore a 21 September north-operator signature names Ben before his activation, not Ada. The alias transfer and credential activation are distinct events. Copying an older alias mapping without its dates supplies the wrong principal for the later event.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 37, "end_character": 627, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "f07bfa3668571ccd931251b2f2b44f8c10a9f4323bdc0dac424f76b27fd1b52f", "artifact_directory": "extraction/D00004/attempt-hri0cwue"}`.

- [input/sources/01-alias-register.md](input/sources/01-alias-register.md) — `P03`

> [AL02] Central approver Cora Vale, P-CV, has ordinary approval authority over N01 through N60 throughout September. Delegate Devon Ash, P-DA, has only the narrower scope in the native delegation instrument. Local supervisor Emil Pine, P-EP, has revision A local authority before 15 September. Emil has no ordinary revision B central approval authority. Cora, CV, and central-approver all name P-CV throughout the interval. A correct identity mapping alone does not prove approval scope, timing, or the validity of a permit. Those predicates require their own evidence.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 629, "end_character": 1197, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "f07bfa3668571ccd931251b2f2b44f8c10a9f4323bdc0dac424f76b27fd1b52f", "artifact_directory": "extraction/D00004/attempt-hri0cwue"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-p-0013`

> [AU03] EXCEPTION AUTHORITY. Only the governance board may issue a signed temporary policy exception for a named node and time window. Cora's ordinary approval authority does not include granting such an exception alone. The board issued one final signed exception in this packet. Its operative text is stored separately from the ordinary node records. A reviewer must locate that actual document and match all conditions. The existence of the power or a pending request does not imply that a grant covers every requested node. A complete search must include applicable rule documents beyond the initial operational retrieval chunk.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 13, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-m18o933_"}`.

- [input/sources/records/057-n57.md](input/sources/records/057-n57.md) — `P02`

> [N57-01] Release N57-R1 occurred on 22 September at 10:00 with active Ada signing as aq-main. Emil signed local approval at 09:00. No ordinary central permit is recorded. A reference states that a board maintenance exception governs this release; the operative signed document is elsewhere in the distributed packet. This record does not restate its conditions. The auditor must locate the final grant and compare node, time, credential, and supervisor conditions. Classification from the ordinary rule alone would omit a directly referenced applicable rule.

Original: [input/originals/D00066.md](input/originals/D00066.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 594, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00066.md", "original_sha256": "39862aa177c7d9a9ac22a0389176bfb7506d9771d2432d36759b95a009e4456a", "artifact_directory": "extraction/D00066/attempt-jtil5roc"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P02`

> [EX01] The governance board grants a temporary exception for node N57 only, effective 22 September 2034 from 09:00 through 12:00 inclusive. During that interval, an active operator credential and signed local approval by Emil satisfy the release route without an ordinary central permit. The board signed under its explicit exception-granting authority. The exception does not cover N58, change credential activation, or extend to other times. N57 release at 10:00 and Emil approval at 09:00 fall inside the stated scope. Every named condition is operative, not illustrative.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 35, "end_character": 610, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-4om_x9tp"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P03`

> [EX02] This grant changes only the ordinary central-approval and permit requirements for the specified N57 window. The request mentioned N58, but the board deliberately excluded it from the final grant. The signed final scope prevails over the earlier proposal. Its location after the operational records does not diminish authority, and its filename creates no independent precedence. An assessor who discovers it must revisit any provisional N57 conclusion made from the general rule alone. Full-corpus rule discovery matters because the exception is separate from the record whose authorization it changes.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 612, "end_character": 1221, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-4om_x9tp"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P04`

> [EX03] The board-exception register is complete for September and contains only this grant. No second board exception covers N58 or N51. This bounded completeness can support an absence conclusion about board grants for those nodes during that interval. It says nothing about later periods or all imaginable documents. The incomplete N59 permit history supports a different conclusion: its missing permit remains unknown. The audit should identify exactly which completeness premise licenses a negative fact, rather than treating every unsuccessful search as equivalent evidence of absence.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1223, "end_character": 1813, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-4om_x9tp"}`.

### Rules

- Only the board grants policy exceptions; EX01 replaces central approval/permit for N57 in September 22 09:00–12:00 inclusive, retaining active operator and signed local Emil approval.

### Assumptions

- The synthetic signed source records are accepted as documentary premises, without a claim of external cryptographic authentication.
- All comparisons use the source September 2034 dates and common clock; distinct approval, release, effective and indexing times are preserved.
- Completeness is limited to the identity, permit, authority-amendment, board-grant or event domain explicitly named by each source.

### Reasoning

- 1. AU03 identifies actual granting authority; EX01 is the final signed grant rather than a request. It names N57 only.
- 2. N57 release 10:00 and Emil approval 09:00 both lie inside the included window. Ada signs as aq-main with active credential.
- 3. The ordinary route fails without a permit and ordinary central approval, but the scoped board route succeeds with every retained condition. The model explicitly checks both routes and final authorization.
- 4. No filename ordering or proposal text creates authority; EX02 operative scope controls.

### Limits

- The result concerns the named September 2034 node/release and reviewed source snapshot. It does not certify future service behavior or an exhaustive event history for all nodes.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.n57Exception` in module `Audit` (supports): `Audit.boardWindow Audit.n57.node Audit.n57.time = true ∧ Audit.n57.approvalTime = some (Audit.minuteAt 22 9 0) ∧ Audit.boardWindow Audit.n57.node (Audit.minuteAt 22 9 0) = true ∧ Audit.ordinaryRoute Audit.n57 = false ∧ Audit.boardRoute Audit.n57 = true ∧ Audit.authorized Audit.n57 = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target020.lean) · [Actual proof log](logs/target-020.log)

### Recommendation

Retain the finding and its source-defined scope.

## C10-OK-08

### Exact report claim

`input/report.md#C10-OK-08`

> **C10-OK-08.** The board exception does not cover N58.
> 
> Citations: sources/98-board-exception.md#[EX01]; sources/98-board-exception.md#[EX03].

### Verification question

Does the final board exception fail to cover N58?

### Source evidence

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-p-0013`

> [AU03] EXCEPTION AUTHORITY. Only the governance board may issue a signed temporary policy exception for a named node and time window. Cora's ordinary approval authority does not include granting such an exception alone. The board issued one final signed exception in this packet. Its operative text is stored separately from the ordinary node records. A reviewer must locate that actual document and match all conditions. The existence of the power or a pending request does not imply that a grant covers every requested node. A complete search must include applicable rule documents beyond the initial operational retrieval chunk.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 13, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-m18o933_"}`.

- [input/sources/97-request-correspondence.md](input/sources/97-request-correspondence.md) — `P02`

> [REQ01] A supervisor requested a maintenance exception for both N57 and N58 on 21 September, proposing a two-day window. The board answered by issuing only the final signed grant stored separately. A request is not a grant, and no rule expands the final grant to match the original proposal. The correspondence remains in the packet to preserve decision history. Retrieving the proposal without its operative response can make the permission appear broader than it is. The final signed document, valid granting authority, and matched scope govern the release rather than an earlier request headline.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 635, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "0f6f5493f82bd9be47fd10b33f21ca7cafd6c294c4ea1e02e97822c2e9762123", "artifact_directory": "extraction/D00008/attempt-_68f__gq"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P02`

> [EX01] The governance board grants a temporary exception for node N57 only, effective 22 September 2034 from 09:00 through 12:00 inclusive. During that interval, an active operator credential and signed local approval by Emil satisfy the release route without an ordinary central permit. The board signed under its explicit exception-granting authority. The exception does not cover N58, change credential activation, or extend to other times. N57 release at 10:00 and Emil approval at 09:00 fall inside the stated scope. Every named condition is operative, not illustrative.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 35, "end_character": 610, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-4om_x9tp"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P03`

> [EX02] This grant changes only the ordinary central-approval and permit requirements for the specified N57 window. The request mentioned N58, but the board deliberately excluded it from the final grant. The signed final scope prevails over the earlier proposal. Its location after the operational records does not diminish authority, and its filename creates no independent precedence. An assessor who discovers it must revisit any provisional N57 conclusion made from the general rule alone. Full-corpus rule discovery matters because the exception is separate from the record whose authorization it changes.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 612, "end_character": 1221, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-4om_x9tp"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P04`

> [EX03] The board-exception register is complete for September and contains only this grant. No second board exception covers N58 or N51. This bounded completeness can support an absence conclusion about board grants for those nodes during that interval. It says nothing about later periods or all imaginable documents. The incomplete N59 permit history supports a different conclusion: its missing permit remains unknown. The audit should identify exactly which completeness premise licenses a negative fact, rather than treating every unsuccessful search as equivalent evidence of absence.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1223, "end_character": 1813, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-4om_x9tp"}`.

### Rules

- Match actual signed node/time scope; request scope does not enlarge the grant. EX03 closes board grants only for September.

### Assumptions

- The synthetic signed source records are accepted as documentary premises, without a claim of external cryptographic authentication.
- All comparisons use the source September 2034 dates and common clock; distinct approval, release, effective and indexing times are preserved.
- Completeness is limited to the identity, permit, authority-amendment, board-grant or event domain explicitly named by each source.

### Reasoning

- 1. REQ01 requested both N57/N58, but EX01 says N57 only and expressly excludes N58.
- 2. EX02 confirms deliberate exclusion from the final grant; EX03 says there is only that grant and no second exception covers N58.
- 3. The model checks node 58 does not satisfy the actual grant even at the matching10:00 time.

### Limits

- The result concerns the named September 2034 node/release and reviewed source snapshot. It does not certify future service behavior or an exhaustive event history for all nodes.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.n58NotCovered` in module `Audit` (supports): `Audit.boardWindow 58 (Audit.minuteAt 22 10 0) = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target021.lean) · [Actual proof log](logs/target-021.log)

### Recommendation

Retain the finding and its source-defined scope.

## C10-OK-09

### Exact report claim

`input/report.md#C10-OK-09`

> **C10-OK-09.** N58 provides an explicit counterexample to universal recorded-release authorization.
> 
> Citations: sources/records/058-n58.md#[N58-01]; sources/03-policy-transition.md#[PV03].

### Verification question

Does N58-R1 directly refute authorization of every recorded release?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P03`

> [G02] Authorization by revision. Policy revision B becomes effective at 00:00 on 15 September. A release at or after that instant requires an active operator credential at release time, a signed approval by a principal with scope over that node at approval time, and an unrevoked permit covering the release. Before that instant, revision A requires an active operator credential and signed local-supervisor approval; no central permit is required. Event time controls historical applicability. Report date, file modification date, and discovery date do not replace the operative timestamp. Successful technical handoff does not itself establish administrative authorization.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 656, "end_character": 1331, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-wbqvz0qn"}`.

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P05`

> [G04] Missing and contrary evidence. A missing permit attachment in an expressly incomplete history establishes a missing argument, not proof that no permit existed. A complete bounded permit history can establish absence within its specified interval. An explicitly revoked permit with a statement that no replacement existed is different from an empty search result. One documented unauthorized release refutes a global claim that all recorded releases were authorized, even if other cases remain unknown. Completeness of the node domain does not establish completeness of all release events. A claim of exactly one event needs event-history evidence, not merely a valid authorization for one known event.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2012, "end_character": 2719, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-wbqvz0qn"}`.

- [input/sources/03-policy-transition.md](input/sources/03-policy-transition.md) — `P04`

> [PV03] N58 permit revocation took effect at 09:00 on 22 September. Its release occurred at 10:00, and the signed revocation was indexed at 11:00. The index timestamp does not postpone the explicit effective time. The complete permit history says no replacement existed at 10:00. No board exception applies to N58. This supplies a concrete unauthorized release and an independent counterexample to a global authorization claim. It does not require inferring absence from a retrieval failure. Technical bundle handoff succeeded, but that fact does not reverse the administrative revocation.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1148, "end_character": 1736, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "49b4f99dd0f7f83a36ca549e0f2e026d83bfef78f82c5b46f4aed7d84b70e6f3", "artifact_directory": "extraction/D00006/attempt-np40ixtc"}`.

- [input/sources/records/058-n58.md](input/sources/records/058-n58.md) — `P02`

> [N58-01] Release N58-R1 occurred on 22 September at 10:00 with active Ada and valid Cora approval. The node permit had been revoked effective 09:00, before release, although its index entry appeared at 11:00. The complete permit history says no replacement existed at 10:00. No board exception covers N58. The record explicitly identifies this release as unauthorized under revision B. This counterexample remains decisive for a global claim even if other nodes have incomplete evidence. Successful administrative handoff is a separate fact.

Original: [input/originals/D00067.md](input/originals/D00067.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 577, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00067.md", "original_sha256": "f9efcebda7ad09423ba369c0c5456d8b70e40fecf276d4d9ce4d14dd79e5f7e9", "artifact_directory": "extraction/D00067/attempt-eok2b9s4"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P02`

> [EX01] The governance board grants a temporary exception for node N57 only, effective 22 September 2034 from 09:00 through 12:00 inclusive. During that interval, an active operator credential and signed local approval by Emil satisfy the release route without an ordinary central permit. The board signed under its explicit exception-granting authority. The exception does not cover N58, change credential activation, or extend to other times. N57 release at 10:00 and Emil approval at 09:00 fall inside the stated scope. Every named condition is operative, not illustrative.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 35, "end_character": 610, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-4om_x9tp"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P04`

> [EX03] The board-exception register is complete for September and contains only this grant. No second board exception covers N58 or N51. This bounded completeness can support an absence conclusion about board grants for those nodes during that interval. It says nothing about later periods or all imaginable documents. The incomplete N59 permit history supports a different conclusion: its missing permit remains unknown. The audit should identify exactly which completeness premise licenses a negative fact, rather than treating every unsuccessful search as equivalent evidence of absence.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1223, "end_character": 1813, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-4om_x9tp"}`.

### Rules

- RevisionB requires active operator, scoped approval and unrevoked covering permit unless a valid exception applies. One in-domain counterexample refutes a universal statement even if other cases are unknown.

### Assumptions

- The synthetic signed source records are accepted as documentary premises, without a claim of external cryptographic authentication.
- All comparisons use the source September 2034 dates and common clock; distinct approval, release, effective and indexing times are preserved.
- Completeness is limited to the identity, permit, authority-amendment, board-grant or event domain explicitly named by each source.

### Reasoning

- 1. N58-R1 is a documented node 58 release September 22 10:00 within the complete identity universe. Ada and Cora prerequisites are satisfied.
- 2. PV03/N58 record revocation effective 09:00, no replacement at 10:00 and no exception. Indexing at 11:00 cannot postpone09:00 effect.
- 3. The model checks09:00<release 10:00<index11:00 and authorization=false despite the other prerequisites.
- 4. A second theorem proves that any recorded-release list containing this concrete witness cannot have every release authorized. It requires no exhaustive history for N59/N60 and never turns their unknown predicates false.

### Limits

- The result concerns the named September 2034 node/release and reviewed source snapshot. It does not certify future service behavior or an exhaustive event history for all nodes.
- The refuted proposition is universal authorization, not a claim that every release is unauthorized.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.n58Unauthorized` in module `Audit` (supports): `Audit.minuteAt 22 9 0 < Audit.n58.time ∧ Audit.n58.time < Audit.minuteAt 22 11 0 ∧ Audit.authorized Audit.n58 = false ∧ 58 ∈ Audit.nodes`.
  [Model](models/Audit.lean) · [Executed check](checks/Target022.lean) · [Actual proof log](logs/target-022.log)

- `Audit.universalCounterexample` in module `Audit` (supports): `∀ recorded : List Audit.Release, Audit.n58 ∈ recorded → ¬ (∀ r ∈ recorded, Audit.authorized r = true)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target023.lean) · [Actual proof log](logs/target-023.log)

### Recommendation

Retain the finding and its source-defined scope.

## C10-OK-10

### Exact report claim

`input/report.md#C10-OK-10`

> **C10-OK-10.** N59 authorization is unsupported because its permit history is missing and incomplete.
> 
> Citations: sources/records/059-n59.md#[N59-01]; sources/00-governance.md#[G04].

### Verification question

Is N59 authorization unresolved because its permit premise lacks evidence?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P03`

> [G02] Authorization by revision. Policy revision B becomes effective at 00:00 on 15 September. A release at or after that instant requires an active operator credential at release time, a signed approval by a principal with scope over that node at approval time, and an unrevoked permit covering the release. Before that instant, revision A requires an active operator credential and signed local-supervisor approval; no central permit is required. Event time controls historical applicability. Report date, file modification date, and discovery date do not replace the operative timestamp. Successful technical handoff does not itself establish administrative authorization.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 656, "end_character": 1331, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-wbqvz0qn"}`.

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P05`

> [G04] Missing and contrary evidence. A missing permit attachment in an expressly incomplete history establishes a missing argument, not proof that no permit existed. A complete bounded permit history can establish absence within its specified interval. An explicitly revoked permit with a statement that no replacement existed is different from an empty search result. One documented unauthorized release refutes a global claim that all recorded releases were authorized, even if other cases remain unknown. Completeness of the node domain does not establish completeness of all release events. A claim of exactly one event needs event-history evidence, not merely a valid authorization for one known event.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2012, "end_character": 2719, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-wbqvz0qn"}`.

- [input/sources/records/059-n59.md](input/sources/records/059-n59.md) — `P02`

> [N59-01] Release N59-R1 occurred on 22 September at 10:00 with active Ada and valid Cora approval. The permit attachment is missing, and the permit history is expressly incomplete. No record states that a permit did not exist, and no revocation is supplied. Authorization is therefore unresolved from this packet. The useful finding is the missing permit argument, not a categorical unauthorized verdict. Identity-domain completeness does not repair this gap. The named release itself is documented; it is the permit prerequisite that lacks evidence.

Original: [input/originals/D00068.md](input/originals/D00068.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 586, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00068.md", "original_sha256": "1728ba1a1c8c8cf5b266060cedc4d913f897ea1d822f544d480b583416d65964", "artifact_directory": "extraction/D00068/attempt-toumy2sn"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P04`

> [EX03] The board-exception register is complete for September and contains only this grant. No second board exception covers N58 or N51. This bounded completeness can support an absence conclusion about board grants for those nodes during that interval. It says nothing about later periods or all imaginable documents. The incomplete N59 permit history supports a different conclusion: its missing permit remains unknown. The audit should identify exactly which completeness premise licenses a negative fact, rather than treating every unsuccessful search as equivalent evidence of absence.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1223, "end_character": 1813, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-4om_x9tp"}`.

### Rules

- Expressly incomplete permit history cannot justify permit=false; identity-domain completeness and technical handoff are different predicates.

### Assumptions

- The synthetic signed source records are accepted as documentary premises, without a claim of external cryptographic authentication.
- All comparisons use the source September 2034 dates and common clock; distinct approval, release, effective and indexing times are preserved.
- Completeness is limited to the identity, permit, authority-amendment, board-grant or event domain explicitly named by each source.

### Reasoning

- 1. N59-R1 is documented with active Ada and valid Cora approval; the missing premise is its covering unrevoked permit.
- 2. N59 expressly says history incomplete, no record denies permit existence and no revocation is supplied.
- 3. With all known fields held fixed, a hypothetical covering permit produces authorization=true and its absence produces=false. The auxiliary model demonstrates non-entailment; neither hypothetical value is assigned to actual N59.

### Limits

- The result concerns the named September 2034 node/release and reviewed source snapshot. It does not certify future service behavior or an exhaustive event history for all nodes.
- The report correctly identifies a support gap. Actual N59 authorization remains undetermined, not refuted.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **auxiliary**.

### Formal evidence

- `Audit.n59Open` in module `Audit` (auxiliary): `Audit.authorized (Audit.n59Completion true) = true ∧ Audit.authorized (Audit.n59Completion false) = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target024.lean) · [Actual proof log](logs/target-024.log)

### Recommendation

Obtain the complete scoped permit history or a covering permit before resolving N59.

## C10-OK-11

### Exact report claim

`input/report.md#C10-OK-11`

> **C10-OK-11.** N60 named release R1 has a complete authorization argument, while its late-month event history is incomplete.
> 
> Citations: sources/records/060-n60.md#[N60-01].

### Verification question

Can N60-R1 be authorized while the count of late-month releases remains unresolved?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P03`

> [G02] Authorization by revision. Policy revision B becomes effective at 00:00 on 15 September. A release at or after that instant requires an active operator credential at release time, a signed approval by a principal with scope over that node at approval time, and an unrevoked permit covering the release. Before that instant, revision A requires an active operator credential and signed local-supervisor approval; no central permit is required. Event time controls historical applicability. Report date, file modification date, and discovery date do not replace the operative timestamp. Successful technical handoff does not itself establish administrative authorization.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 656, "end_character": 1331, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-wbqvz0qn"}`.

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P05`

> [G04] Missing and contrary evidence. A missing permit attachment in an expressly incomplete history establishes a missing argument, not proof that no permit existed. A complete bounded permit history can establish absence within its specified interval. An explicitly revoked permit with a statement that no replacement existed is different from an empty search result. One documented unauthorized release refutes a global claim that all recorded releases were authorized, even if other cases remain unknown. Completeness of the node domain does not establish completeness of all release events. A claim of exactly one event needs event-history evidence, not merely a valid authorization for one known event.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 9, "end_line": 9, "start_character": 2012, "end_character": 2719, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-wbqvz0qn"}`.

- [input/sources/records/060-n60.md](input/sources/records/060-n60.md) — `P02`

> [N60-01] Release N60-R1 occurred on 20 September at 10:00 with active Ada, valid Cora approval, and an unrevoked covering permit. Its authorization records are complete. However, the event-history export is incomplete for 26 through 30 September because an archive connector was unavailable. The packet does not settle whether additional releases occurred during that gap. The known release can be supported as authorized while the assertion of exactly one release in the month remains unsupported. These claims have different completeness requirements.

Original: [input/originals/D00069.md](input/originals/D00069.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 589, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00069.md", "original_sha256": "73a0614627f28487ad0f6807e8055f81271f905e116b55d17de6594eb3e72dfc", "artifact_directory": "extraction/D00069/attempt-a6sx8161"}`.

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
Coordinates: `{"kind": "pdf", "page": 5, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0005.bbox.xhtml", "total_pages": 5, "original": "input/originals/D00007.pdf", "original_sha256": "6fbabc6f1ab5af7659201499d292110b7f8e0da5dcf20a6864f09a6dedf439e8", "artifact_directory": "extraction/D00007/attempt-y0b_3esl"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

### Rules

- Authorization of a named event and completeness of the monthly event domain require different premises.

### Assumptions

- The synthetic signed source records are accepted as documentary premises, without a claim of external cryptographic authentication.
- All comparisons use the source September 2034 dates and common clock; distinct approval, release, effective and indexing times are preserved.
- Completeness is limited to the identity, permit, authority-amendment, board-grant or event domain explicitly named by each source.

### Reasoning

- 1. N60-R1 September 20 10:00 has active Ada, valid Cora approval and unrevoked covering permit; its authorization records are complete.
- 2. The model proves the ordinary route and named-event authorization from those facts.
- 3. The same source explicitly omits event-history coverage September 26–30 due to connector outage. That documented gap prevents inferring exactly one monthly release, but does not undermine the known release argument.

### Limits

- The result concerns the named September 2034 node/release and reviewed source snapshot. It does not certify future service behavior or an exhaustive event history for all nodes.
- The checked target supports only named R1 authorization. Late-month history incompleteness is documented; no event count or invented extra release is formalized.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.n60KnownAuthorized` in module `Audit` (supports): `Audit.ordinaryRoute Audit.n60 = true ∧ Audit.authorized Audit.n60 = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target025.lean) · [Actual proof log](logs/target-025.log)

### Recommendation

Retain the finding and its source-defined scope.

## C10-OK-12

### Exact report claim

`input/report.md#C10-OK-12`

> **C10-OK-12.** The proposal mentioning N58 did not include it in the final signed grant.
> 
> Citations: sources/97-request-correspondence.md#[REQ01]; sources/98-board-exception.md#[EX02].

### Verification question

Did the proposal mentioning N58 fail to include it in the final signed grant?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P04`

> [G03] Hierarchy and identity. Resolve aliases through the dated identity registry. A reused display name does not transfer the former principal's credential. Supersession replaces only the named scope from its stated effective instant. A valid board exception can modify the ordinary route if its node, time, and other conditions match. The board's power to grant exceptions does not establish that a requested exception was granted. Ordinary approval authority does not include authority to rewrite policy. Filename ordering creates no precedence. The applicable hierarchy must be assembled before deciding whether the ordinary permit requirement governs a particular release.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1333, "end_character": 2010, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-wbqvz0qn"}`.

- [input/sources/02-delegation.docx.md](input/sources/02-delegation.docx.md) — `docx-p-0013`

> [AU03] EXCEPTION AUTHORITY. Only the governance board may issue a signed temporary policy exception for a named node and time window. Cora's ordinary approval authority does not include granting such an exception alone. The board issued one final signed exception in this packet. Its operative text is stored separately from the ordinary node records. A reviewer must locate that actual document and match all conditions. The existence of the power or a pending request does not imply that a grant covers every requested node. A complete search must include applicable rule documents beyond the initial operational retrieval chunk.

Original: [input/originals/D00005.docx](input/originals/D00005.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[3]", "paragraph_index_in_story": 13, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00005.docx", "original_sha256": "2b54f8e40dd0e7fc417bc93bda7d56806f8b3dafd09d5e66d698a964a3145e82", "artifact_directory": "extraction/D00005/attempt-m18o933_"}`.

- [input/sources/97-request-correspondence.md](input/sources/97-request-correspondence.md) — `P02`

> [REQ01] A supervisor requested a maintenance exception for both N57 and N58 on 21 September, proposing a two-day window. The board answered by issuing only the final signed grant stored separately. A request is not a grant, and no rule expands the final grant to match the original proposal. The correspondence remains in the packet to preserve decision history. Retrieving the proposal without its operative response can make the permission appear broader than it is. The final signed document, valid granting authority, and matched scope govern the release rather than an earlier request headline.

Original: [input/originals/D00008.md](input/originals/D00008.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 635, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00008.md", "original_sha256": "0f6f5493f82bd9be47fd10b33f21ca7cafd6c294c4ea1e02e97822c2e9762123", "artifact_directory": "extraction/D00008/attempt-_68f__gq"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P02`

> [EX01] The governance board grants a temporary exception for node N57 only, effective 22 September 2034 from 09:00 through 12:00 inclusive. During that interval, an active operator credential and signed local approval by Emil satisfy the release route without an ordinary central permit. The board signed under its explicit exception-granting authority. The exception does not cover N58, change credential activation, or extend to other times. N57 release at 10:00 and Emil approval at 09:00 fall inside the stated scope. Every named condition is operative, not illustrative.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 35, "end_character": 610, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-4om_x9tp"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P03`

> [EX02] This grant changes only the ordinary central-approval and permit requirements for the specified N57 window. The request mentioned N58, but the board deliberately excluded it from the final grant. The signed final scope prevails over the earlier proposal. Its location after the operational records does not diminish authority, and its filename creates no independent precedence. An assessor who discovers it must revisit any provisional N57 conclusion made from the general rule alone. Full-corpus rule discovery matters because the exception is separate from the record whose authorization it changes.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 612, "end_character": 1221, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-4om_x9tp"}`.

- [input/sources/98-board-exception.md](input/sources/98-board-exception.md) — `P04`

> [EX03] The board-exception register is complete for September and contains only this grant. No second board exception covers N58 or N51. This bounded completeness can support an absence conclusion about board grants for those nodes during that interval. It says nothing about later periods or all imaginable documents. The incomplete N59 permit history supports a different conclusion: its missing permit remains unknown. The audit should identify exactly which completeness premise licenses a negative fact, rather than treating every unsuccessful search as equivalent evidence of absence.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 7, "end_line": 7, "start_character": 1223, "end_character": 1813, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "6c5c473e58889275577821b348c7d0c89df849d3cbdf554519cd7502f3933149", "artifact_directory": "extraction/D00009/attempt-4om_x9tp"}`.

### Rules

- Power to grant and a pending request are not an actual signed grant; final operative scope controls.

### Assumptions

- The synthetic signed source records are accepted as documentary premises, without a claim of external cryptographic authentication.
- All comparisons use the source September 2034 dates and common clock; distinct approval, release, effective and indexing times are preserved.
- Completeness is limited to the identity, permit, authority-amendment, board-grant or event domain explicitly named by each source.

### Reasoning

- 1. REQ01 preserves a two-node request and a proposed two-day period.
- 2. EX01 instead grants N57 only for a narrower September 22 window; EX02 expressly says N58 was deliberately excluded.
- 3. EX03 supplies complete September grant inventory with no separate N58 grant. The report describes the actual request/decision distinction accurately.

### Limits

- The result concerns the named September 2034 node/release and reviewed source snapshot. It does not certify future service behavior or an exhaustive event history for all nodes.
- This is documentary comparison of two source texts, not a claim about the merits of the board decision.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Retain the finding and its source-defined scope.

## C10-OK-13

### Exact report claim

`input/report.md#C10-OK-13`

> **C10-OK-13.** A source change requires checking affected premises before reusing an audit result.
> 
> Citations: sources/00-governance.md#[G05].

### Verification question

Does G05 require reviewing affected source premises before reusing an audit result?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P06`

> [G05] Snapshot provenance. An audit result is bound to exact source bytes, report bytes, inventory, extraction assumptions, and reviewed formal premises. Reuse after a source change requires checking affected premises. An unchanged report hash or unchanged numerical value is insufficient if scope, authority, effective time, or exception text changes elsewhere. Preserve the original snapshot and logs. Reproduction belongs in a distinct repository tmp/ directory with a new source manifest and fingerprint. A prior proof must not be described as validation of changed inputs without reviewing its dependencies. This rule is evidence bookkeeping, not permission to overwrite the baseline corpus.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 11, "start_character": 2721, "end_character": 3417, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-wbqvz0qn"}`.

### Rules

- G05 binds results to source/report bytes, inventory, extraction assumptions and reviewed formal premises; preserve baseline and create distinct reproduction snapshots.

### Assumptions

- The synthetic signed source records are accepted as documentary premises, without a claim of external cryptographic authentication.
- All comparisons use the source September 2034 dates and common clock; distinct approval, release, effective and indexing times are preserved.
- Completeness is limited to the identity, permit, authority-amendment, board-grant or event domain explicitly named by each source.

### Reasoning

- 1. G05 explicitly requires checking affected premises after source change, including scope, authority, effective time and exceptions.
- 2. Unchanged report hash or numeric input alone does not establish unchanged argument dependencies.
- 3. The supplied report accurately states this normative provenance requirement. This finding does not claim that a refresh/reproduction was executed in this audit.

### Limits

- The result concerns the named September 2034 node/release and reviewed source snapshot. It does not certify future service behavior or an exhaustive event history for all nodes.
- No changed-source validation is claimed; this run remains bound to its original protected snapshot and actual recorded checks.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Retain the finding and its source-defined scope.

## C10-OK-14

### Exact report claim

`input/report.md#C10-OK-14`

> **C10-OK-14.** The ordinary N01 release meets revision B authorization requirements.
> 
> Citations: sources/records/001-n01.md#[N01-01]; sources/00-governance.md#[G02].

### Verification question

Does ordinary N01-R1 meet every applicable revisionB authorization premise?

### Source evidence

- [input/sources/00-governance.md](input/sources/00-governance.md) — `P03`

> [G02] Authorization by revision. Policy revision B becomes effective at 00:00 on 15 September. A release at or after that instant requires an active operator credential at release time, a signed approval by a principal with scope over that node at approval time, and an unrevoked permit covering the release. Before that instant, revision A requires an active operator credential and signed local-supervisor approval; no central permit is required. Event time controls historical applicability. Report date, file modification date, and discovery date do not replace the operative timestamp. Successful technical handoff does not itself establish administrative authorization.

Original: [input/originals/D00003.md](input/originals/D00003.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 656, "end_character": 1331, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00003.md", "original_sha256": "e996791c20c230593946085b533896e3e7f06231ddd4867660dabfbd810622df", "artifact_directory": "extraction/D00003/attempt-wbqvz0qn"}`.

- [input/sources/01-alias-register.md](input/sources/01-alias-register.md) — `P02`

> [AL01] Principal Ada Quill has immutable identifier P-AQ. Alias north-operator identifies Ada from 1 through 20 September inclusive. From 21 September the same alias identifies Ben Rook, P-BR. Ada uses aq-main from 21 September onward. Ada's credential is active throughout September. Ben's credential becomes active on 22 September. Therefore a 21 September north-operator signature names Ben before his activation, not Ada. The alias transfer and credential activation are distinct events. Copying an older alias mapping without its dates supplies the wrong principal for the later event.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 37, "end_character": 627, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "f07bfa3668571ccd931251b2f2b44f8c10a9f4323bdc0dac424f76b27fd1b52f", "artifact_directory": "extraction/D00004/attempt-hri0cwue"}`.

- [input/sources/01-alias-register.md](input/sources/01-alias-register.md) — `P03`

> [AL02] Central approver Cora Vale, P-CV, has ordinary approval authority over N01 through N60 throughout September. Delegate Devon Ash, P-DA, has only the narrower scope in the native delegation instrument. Local supervisor Emil Pine, P-EP, has revision A local authority before 15 September. Emil has no ordinary revision B central approval authority. Cora, CV, and central-approver all name P-CV throughout the interval. A correct identity mapping alone does not prove approval scope, timing, or the validity of a permit. Those predicates require their own evidence.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 5, "end_line": 5, "start_character": 629, "end_character": 1197, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "f07bfa3668571ccd931251b2f2b44f8c10a9f4323bdc0dac424f76b27fd1b52f", "artifact_directory": "extraction/D00004/attempt-hri0cwue"}`.

- [input/sources/records/001-n01.md](input/sources/records/001-n01.md) — `P02`

> [N01-01] Release N01-R1 occurred on 19 September 2034 at 10:00 under revision B. Ada signed as north-operator while that alias mapped to P-AQ; her credential was active. Cora issued signed approval N01-A1 at 09:00 that day. Permit N01-P1 covered the full day and was unrevoked at release. Permit and approval histories are complete for the named interval. The signed handoff identifies the same node, preventing use of another node's permit. No exception is needed for this ordinary release.

Original: [input/originals/D00010.md](input/originals/D00010.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 3, "end_line": 3, "start_character": 36, "end_character": 527, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00010.md", "original_sha256": "8f42c9da075dcad99ebddcf8c8854f120f55abf8374f7d25bdf7fb8bd3f4282e", "artifact_directory": "extraction/D00010/attempt-n4tqn9mh"}`.

### Rules

- RevisionB uses active credential, valid scoped signed approval and covering unrevoked permit; dated aliases identify the operator.

### Assumptions

- The synthetic signed source records are accepted as documentary premises, without a claim of external cryptographic authentication.
- All comparisons use the source September 2034 dates and common clock; distinct approval, release, effective and indexing times are preserved.
- Completeness is limited to the identity, permit, authority-amendment, board-grant or event domain explicitly named by each source.

### Reasoning

- 1. N01-R1 occurs September 19 10:00, after revisionB boundary. north-operator still means Ada on that date and her credential is active.
- 2. Cora signed09:00 approval and has ordinary authority over all 60 nodes; the same-node full-day permit is unrevoked at release.
- 3. N01 explicitly closes permit/approval histories for the named interval. The model checks the conjunction and needs no board exception.

### Limits

- The result concerns the named September 2034 node/release and reviewed source snapshot. It does not certify future service behavior or an exhaustive event history for all nodes.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.n01Authorized` in module `Audit` (supports): `Audit.northAlias Audit.n01.time = Audit.Principal.ada ∧ Audit.revisionB Audit.n01.time = true ∧ Audit.ordinaryRoute Audit.n01 = true ∧ Audit.authorized Audit.n01 = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target026.lean) · [Actual proof log](logs/target-026.log)

### Recommendation

Retain the finding and its source-defined scope.
