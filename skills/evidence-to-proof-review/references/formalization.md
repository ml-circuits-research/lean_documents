# Formalization and trust boundary

Use Lean 4.24.0 for this release, core libraries only. The version is pinned for reproducibility, not advertised as latest. No custom axioms, `sorry`, `admit`, native computation trust shortcuts, custom elaborators, or kernel bypasses are permitted in published models. Write ordinary typed data and pure definitions; keep assumptions visible and source-linked. Even an axiom-free theorem can have circular hypotheses, so source/target review remains mandatory.

Select the smallest adequate model:

- Finite records/lists for counts, exact integer currency, bounded domains, and explicit witnesses.
- Predicates for triggers, obligations and exceptions; never reverse a one-way implication.
- Integer time offsets with an explained origin for deadlines. Record calendar/working-day conventions, time zone and strict versus inclusive boundaries. Independently verify date-to-offset transcription.
- State transitions for procedural or narrative continuity. Persistence and impossible transitions require actual domain rules.
- Attributed evidence records for positive, negative, unknown and conflicting support. The record is data, not unconditional truth.
- Separate interpretations when the text is ambiguous. Conditional results stay conditional; divergent readings block an unconditional verdict.
- Countermodels for failure of entailment, explicitly distinguished from counterexamples to actual world claims.

Each model needs `model-notes.md` documenting symbol meanings, exact source mappings, domains, assumptions, alternative interpretations, and theorem-to-claim relationships. Concrete input values are transcriptions, not guaranteed authentic observations.

For each proof reference, specify module, fully qualified theorem, intended Lean target, and relation `supports`, `refutes`, or `auxiliary`. The checker must compile an assertion that this theorem has the supplied target type, not merely search its name in output. Audit `#print axioms` for every referenced theorem, including dependencies. Standard core axioms `propext`, `Classical.choice`, and `Quot.sound` may be accepted and must be listed; additional axioms fail the initial policy.

Check non-vacuity when the conclusion presupposes an event or nonempty population. Do not globalize inconsistent evidence. A finite satisfiability witness can help detect vacuity or inconsistent assumptions; general consistency is not decidable by this workflow.

Lean success says that the target follows in the formal system. Semantic review says whether that target and its data faithfully represent the finding. Neither establishes source authenticity. A timeout or missing Lean executable is not a refutation.

The official [proof-validation reference](https://lean-lang.org/doc/reference/latest/ValidatingProofs/) explains axiom inspection and additional rechecking. `lean4checker` availability is optional and must be recorded honestly; replay through Lean's kernel is not an independent kernel implementation. This release does not claim external-checker validation. Unreviewed generated Lean is executable code; the lexical policy is not a security sandbox.
