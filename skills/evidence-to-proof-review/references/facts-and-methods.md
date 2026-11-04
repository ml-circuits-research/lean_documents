# From documentary facts to verification methods

This is a semantic workflow, not a fixed domain ontology or a demand to translate every sentence into Lean. Build a reusable fact/rule map for the dossier, then select the portion needed by each finding and its report arguments. Choose the representation that fits the source: a table, `facts.jsonl`, typed Lean records, or a section of `model-notes.md`. Avoid duplicating the same data in several handwritten formats. Each material model premise must be traceable regardless of format.

## Extract before assuming

For each relevant assertion preserve:

- A stable fact/rule ID, its exact source span and original document identity.
- What is asserted, by whom, with polarity and modality. A quotation establishes that someone asserted a proposition, not automatically that it holds.
- Its role: observation, reported testimony, normative rule, definition, assumption, hypothetical or fictional statement.
- Entities, units, time, version, jurisdiction or narrative world, applicability conditions and exceptions.
- Extraction uncertainty, unresolved references, conflicting statements and plausible alternative interpretations.
- Its model representation, if used: symbol/field, value or predicate, and the source-to-symbol explanation.

Keep conflicting attributions separate. A factual event can remain unknown while the presence of two incompatible statements is directly demonstrable. Reject duplicated source representations as independent corroboration. Preserve negative evidence only within the scope that the source actually warrants.

The report is a separate input role. Extract its conclusion and its proposed premises, quotations, calculations, rules and inference steps. A cited source is a retrieval lead. Re-read it independently, including applicable exceptions and counterevidence. Other reports may be supplied as documentary assertions, but neither their conclusions nor their citations become proven premises merely by repetition.

## Define a method for each target

For each atomic conclusion and material argument obligation, record a method card in the review plan or formalization notes:

1. The exact question and scope, inferred from the claim when no brief exists.
2. Required data and rule IDs, dependencies and any unavailable premise.
3. The mathematical or documentary method, and why it matches this claim.
4. The support target, refutation target or counterexample, and interpretation alternatives where needed.
5. Applicability and consistency checks: population membership, units, exceptions, time/version, nonempty domains, compatible premises.
6. Which parts Lean checks, which parts remain source/interpretation judgments, and the outcome if a tool or proof attempt fails.

Do not default every audit to a Boolean table or a classifier. Those are useful only when their semantics justify them. Candidate methods include exact or symbolic arithmetic; finite enumeration; sets and relations; temporal intervals and state transitions; quantified propositions; algebraic properties; attribution graphs; policy priority with explicitly supplied rules; and model/countermodel constructions for entailment. Statistical claims require a justified statistical model and sampling premises. Causal claims require causal premises, not correlation alone. Qualitative claims need defined criteria or an explicit interpretive limitation. A missing standard is not permission to invent a threshold.

External calculation or search tools can discover candidate results. For a formal guarantee, reconstruct their certificate or argument in Lean and run the check; an external solver's success string is not a Lean proof. Domain libraries are optional conveniences, not the source of the report's premises.

## Audit the conclusion and its argument separately

Let `E` describe admissible interpretations of independently extracted evidence, `C` the conclusion, and `A` the premises actually offered by the report.

- Support asks whether `E` entails `C`, under named assumptions and with a consistency witness where appropriate.
- Refutation asks whether `E` entails `¬ C`, or supplies a relevant witness against a universal `C`.
- Argument validity asks whether `A` entails `C`. Also verify each material premise of `A` against `E`; validity alone does not make premises true.
- Non-entailment can be established by a model satisfying `A` and falsifying `C`; this need not describe the actual case.
- Formal underdetermination can be established by two models satisfying `E` with opposite truth values for `C`. A mere failed search or timed-out proof is a weaker result and must be labelled as such.

A supported conclusion can coexist with an invalid report argument. An invalid argument does not establish a false conclusion. A sound argument can establish only a conditional result if its material premises remain unverified. Keep these distinctions in both the human explanation and proof-to-claim mappings.

[EvidenceLogic.lean](../assets/EvidenceLogic.lean) is an optional core-Lean vocabulary for these relations, including non-vacuous support and explicit countermodels. It is not mandatory and does not automatically model a document. Copy it into the reviewed model tree only when helpful, define the source meanings, then prove the task-specific statements. Its abstract theorem about support says nothing about a dossier until the evidence interpretation has been independently checked.
