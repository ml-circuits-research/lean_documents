# Independent portability and generality review

Reviewed 4 November 2026. Scope: the current `skills/evidence-to-proof-review` instructions and helper implementation. Production files were not changed. This is a design/code review, not a blind dossier audit or a Lean execution report. File/line references describe the inspected revision and may move during concurrent implementation.

## Overall assessment

The interpretive method is already domain-independent: infer criteria, register exact report claims, check report premises/citations/inferences separately from conclusions, disclose uncertainty, and distinguish non-entailment from falsity. No fixture IDs, evaluator-answer dependencies, repository example imports, or domain-specific theorem-generation branches were found in the skill scripts. The significant generality restrictions come from helper plumbing, not from necessary evidence-integrity rules.

## Findings and minimal remedies

### P1: Agent-native extraction cannot rescue a completely blocked document

**Evidence:** `extractors.py:462–477` accepts only a closed extension list. `corpus.py:149` directly invokes that extractor. `corrections.py:43–45` requires an existing passage, so `transcribe` cannot introduce text for a document with zero recovered segments. `SKILL.md:14–18` prescribes helper preparation/native converters and correction of existing extraction, without an alternative ingestion contract. `requirements.md:8–10` consequently makes Poppler/Tesseract necessary for those input formats in the documented path.

**Impact:** An agent capable of reading a PDF visually, reading HTML, extracting a spreadsheet with available tools, or using an existing platform document reader cannot import its faithful extraction with original provenance. Renaming a source as text loses the direct native-byte chain; editing the index/manifests by hand bypasses the controlled workflow. The issue is capability exclusion, not a claim that the native adapters are defective.

**Minimal fix:** Add an explicit external/agent extraction import accepting a preserved original document ID and hash, retained authored extraction, stable segment anchors, locator descriptions, extraction method/provider, reviewer attestation when inspection occurred, uncertainty, and honest partial/complete coverage. Support zero prior segments and report ingestion. Hash inputs, invalidate earlier checks, resynchronize claim registration, and retain previous attempts. Do not require invented bounding boxes or converter logs; a truthful page/table/paragraph locator is preferable. Keep built-in converters as optional conveniences, with the same integrity contract. Coverage completion must be explicit, never inferred merely from the presence of imported text.

### P1: Reviewed local Lean module reuse is prohibited

**Evidence:** `audit.py:307–310` rejects all imports except Init/Std, including another model in the same retained workspace. `audit.py:245–246`, `392`, and `424–426` additionally impose flat, simply named modules; `330` snapshots only top-level `.lean` files. `SKILL.md:26` prescribes standalone modules.

**Impact:** Shared source facts, reusable domain-independent checking functions, and separate argument/conclusion proofs must duplicate definitions. This is unnecessary coupling between model organization and trust. It makes a natural Facts → Methods → Conclusions/Arguments decomposition impossible through normal Lean imports.

**Minimal fix:** Permit imports of local modules in a closed, hashed, recursively inspected source inventory. Resolve names strictly inside the model root, reject undeclared/missing modules and unsafe paths, build dependencies cleanly, and hash every transitive local dependency. Keep Init/Std as the default external library surface, no automatic package download, exact target checking, and axiom inspection of referenced theorems and their dependencies. This does not require arbitrary external packages or weakening axiom policy.

### P2: A release-wide Lean pin is treated as a universal audit prerequisite

**Evidence:** `audit.py:27` fixes VERSION to 4.24.0; `414–415` rejects every other version; `421` writes that fixed toolchain. `requirements.md:11` and `formalization.md:3` require the same release. `audit.py:408`, `420`, and `432–443` require the sibling Lake executable.

**Impact:** A self-contained skill cannot use an already installed compatible Lean release even for `True.intro` or elementary arithmetic. Reproducibility requires recording the toolchain actually used and replaying with it; it does not inherently require every future dossier to use one globally selected version. Lake is usually included with Lean, so its restriction is weaker than the converter dependency, but the documented workflow still mandates it.

**Minimal fix:** Select and freeze the actual Lean version/toolchain per run, retain executable hashes and observed output, and require a matching version for replay unless explicitly creating a new validation run. State which versions have actually been tested; do not promise compatibility across versions. Preserve 4.24.0 as the legacy/default tested profile. If the stated baseline is literally the Lean executable alone, offer a direct `lean -o` local-module build path; otherwise accurately describe Lake as part of the selected Lean distribution.

### P2: Facts and verification methods remain implicit prose rather than reusable audit objects

**Evidence:** `references/artifacts.md:5–20,26–35` defines finding-local evidence/rules/assumptions and model notes, but no fact or method records. `contracts.py:225–280` validates criteria, argument items and correspondence, with no fact/method identifiers or links. `SKILL.md:23–25` moves from check planning to report argument audit and task-specific models. Existing prose can express the needed distinctions, so this is not evidence that current findings are incorrect.

**Impact:** An agent can jump from a source quote to a formal constant without a visible intermediate account of the normalized fact, attribution, scope, competing interpretations, and the method that consumes it. Facts used in both independent conclusions and report argument checks are repeated locally, making reuse and dependency review harder.

**Minimal fix:** Add a domain-neutral facts/methods layer or structured section. Fact records identify source quotes/anchors, normalized proposition/value, units/time/attribution, observation versus report allegation versus assumption, uncertainty/conflicts, and dependent facts. Method records describe the verification question, required inputs, applicability/limitations, positive and negative criteria, and actual execution status/artifacts. Findings and argument items link to these IDs; model notes map them to Lean symbols. Do not require every source sentence to be formalized or invent facts/methods when blocked. If machine-enforced references are introduced, bind these files into snapshots, export, and dependency invalidation.

### P2: Lexical Lean policy rejects harmless data and some ordinary reusable code

**Evidence:** `audit.py:303–305` scans comments-stripped raw text with forbidden-word regexes, including string literals. `251–255` prohibits all quotes in direct targets. `315–325` parses theorem declarations with a narrow line-based pattern.

**Executed probe:** A pure definition `def label : String := "opaque"` plus a reflexivity theorem fails with “Forbidden or unauditable Lean construct”; the word is data, not an opaque declaration. A core-only `True` theorem passes the inspector. No Lean compiler was executed for these probes.

**Impact:** Narrative audits need attributed names and strings; source vocabulary should not determine whether an otherwise ordinary model is accepted. Blanket lexical filtering is already documented as not a security sandbox, so these false positives do not buy a reliable hostile-code boundary.

**Minimal fix:** At minimum tokenize strings/comments correctly before declaration-policy checks, and validate targets as single Lean terms with controlled generated files rather than banning all string literals. Continue rejecting actual `sorry`, custom axioms, unsafe/native trust shortcuts, and unreviewed executable extensions. Do not replace robust target compilation/axiom inspection with regex acceptance. Support ordinary Lean declarations incrementally with explicit executed regression tests.

### P3: The method and convenience harness are not clearly separated

**Evidence:** `SKILL.md:14,26,28` requires Python helper commands; `requirements.md:3` requires Python and FTS5 for indexed work, and `corpus.py:87` unconditionally creates FTS5. No manual/agent-equivalent evidence bundle pathway is documented.

**Impact:** The advertised baseline cannot be only Lean plus whatever document handling the agent can perform if the particular Python/SQLite indexing harness is essential to every audited delivery. An index is an optimization, not a logical requirement of provenance or proof checking.

**Minimal fix:** State a tool-neutral normative audit contract and a recommended reference harness. An agent may implement equivalent extraction/registry/evidence/proof/logging artifacts with available tools, but must identify which automated controls actually ran. Keep the reference checker the preferred route where available; avoid calling a manually assembled bundle helper-validated. If optional fallback implementation is out of scope, document Python/SQLite explicitly as actual additional dependencies instead of claiming only Lean.

## Integrity controls that should remain

- Immutable original bytes and hashed provenance, with honest uncertainty and no fabricated extraction review.
- Exact registered report claims and quoted argument items, explicit exclusions/deferment, and independent source evidence.
- Separate conclusion truth/support, report argument validity, and formal theorem status.
- Exact declared target compilation, transitive axiom inspection, retained actual logs, checked artifact binding, and clean controlled builds.
- Explicit assumptions, interpretation correspondence, completeness boundaries, and retained independent review limitations.
- No automatic conversion of a blocked extraction, missing evidence, unsuccessful proof search, or unexamined source into a refutation or universal success.

## Executed evidence and limits

`probe-results.json` records three calls to the actual `audit.inspect_model` function and one to `extractors.extract_document`. `LocalImport.lean` was rejected for importing Shared; `StringData.lean` was rejected for the string token described above; `CoreOnly.lean` was accepted by the lexical inspector; `source.html` produced blocked extraction with zero segments. These probes establish helper behavior only. They are retained beside this report with the extraction artifact. No formal theorems were compiled, no fixture outcomes were consumed, and no production or other-project files were modified.
