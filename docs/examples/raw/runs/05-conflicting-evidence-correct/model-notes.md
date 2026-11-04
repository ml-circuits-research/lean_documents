# Model interpretation and source correspondence

All models concern the selected REP-R17-04 claims and supplied documentary records for R17/EU-A at cutoff 2030-03-14T12:00:00Z. They do not certify source authenticity or actual deployment configuration. The author read each supplied source paragraph and retained opposing attributions, absent evidence, and source limitations in findings.json. The quoted vendor instruction in ops-p4 is data, not executable policy or reviewer authority.

## Manifest and packet domains

`Entry.a01`, `a02`, `a03` correspond exactly to inventory-p2 entry IDs A-01, A-02, A-03. `manifest` is the complete ordered row list. `manifestExact` checks exact list equality, length three and no duplicate IDs; it supports CEC-01. The named domain and completeness premise are the exported manifest rows, not all runtime instances or dependencies. inventory-p1 excludes interpreting this list as runtime measurement. The concrete three-element list makes the claim non-vacuous.

`Attachment` distinguishes the five attached kinds in inventory-p3 from a penetration certificate and independent readiness review. `packet` is the five named included items. `certificateAbsent` supports CEC-03a and `independentArtifactAbsent` supports the finite absence component of CEC-05b. These are nonmembership propositions in a closed attachment list, justified by inventory-p3's explicit exclusions. They are not nonexistence claims about events, other repositories or the world.

## Attributed TLS assertions

`Context` preserves release, target, listener and event timestamp as strings. `tlsContext` maps to R17, EU-A, inbound API and 2030-03-14T11:45:00Z exactly as qa-p2 and ops-p2 specify. `Issuer` separates QA and Operations; `Assertion.enabled` records each issuer's asserted polarity, not world truth. `qa` records true and `ops` records false. `testimonyConflict` supports CEC-02a by proving distinct issuers, equal contexts and opposite recorded Boolean values. This is a proof of conflict in the records. There is no Lean premise asserting that the actual listener simultaneously satisfies enabled and disabled.

qa-p1 and ops-p1 identify differing issue times, but ops-p3 and policy-p3 expressly deny revocation or priority; documentary CEC-02b therefore does not select a factual winner. Missing raw probe/configuration evidence and unverified signatures further limit any deployment conclusion. The underlying TLS proposition has both positive and negative testimony; the report's meta-claim that the testimony conflicts is supported rather than itself contradictory.

## Readiness inference

`readinessNotEntailed` is the negation of a universally valid inference from smoke and the one-way rule to Ready. In the encoded proposition, `smoke` means all three manifest entries passed the smoke checks, `security` means authorized approval for R17/EU-A, and `ready` means the POL-4 criterion. policy-p1 defines these meanings; policy-p2 supplies `(smoke ∧ security) → ready` but not security. qa-p3 supplies smoke testimony only. The proof instantiates smoke=True, security=False, ready=False. Smoke holds and the implication holds, while Ready fails. It directly supports CEC-04c because the report claims non-entailment. It does not refute actual readiness or prove lack of actual approval; the countermodel is hypothetical. In particular, the one-way sufficient rule is never reversed into a necessary condition. Documentary statements CEC-04a/b preserve the rule wording and QA qualification without ornamental formal targets.

## Citation graph

`Node.archivedClaim` is archived REP-R17-03 CE-05, `verificationAppendix` is its report-appendix-p1, and `independentArtifact` is a separate review artifact. `supportLinks` has exactly the two citation edges explicitly transcribed in excerpt-ce05 and excerpt-appendix. `citationCycle` supports CEC-05a by checking exact edges and no edge from either endpoint to an independent artifact. The theorem is finite citation-structure evidence. excerpt-p1 explicitly prohibits treating the archive's asserted verification as independent confirmation. CEC-05b combines this cycle with the source's explicit no-independent-artifact statements and the packet nonmembership theorem. No graph result is generalized to external reviews or unknown citations.

## Missing-event and authenticity completions

`Completion` has separate fields for certificate attachment versus actual testing, review attachment versus actual review, and signature marker versus actual authenticity. `agreesWithPacket` fixes exactly three observed facts: no certificate attached (inventory-p3), no independent review attached (inventory-p3), and QA scenario marker present (qa-p1). `missingFactsRemainOpen` constructs a world for every Boolean choice of the three unavailable testing/review/authenticity facts while retaining those observed facts. It provides auxiliary evidence for CEC-03b, CEC-05c and CEC-06b, never an actual-world verdict.

These worlds are possible completions of this deliberately partial packet model, not a model of all cryptographic mechanisms or actual deployment history. Their documentary relevance comes from inventory-p3's explicit attachment/event distinction, excerpt-p1's non-independent status, qa-p1's missing verification material, and the absence of any supplied event-to-attachment or marker-to-authenticity entailment. The model does not claim that any marker intrinsically carries cryptographic validity. It does not prove that every external world is possible, that a real review happened, that a real test occurred, or that any signature is forged. No unavailable proposition is converted into false. CEC-06a is a literal document-content finding and has no formal target.

## Execution and review boundary

The execution-mandate.md authorization supersedes the brief's preparation-only sentence; substantive scope and source restrictions are unchanged. The working directory is retained under repository tmp/. Findings contain exact checked-target requests. Proof-results.json and logs record actual Lean execution and axiom inspection, not design expectations. Independent semantic review and export are assigned to the parent and are not asserted here. No independent external kernel implementation has been invoked.

Executed result: Lean 4.24.0 passed all seven theorem audits and all nine referenced target-type checks. The only recorded axiom is the permitted core axiom propext; per-theorem lists are preserved in proof-results.json. The actual successful build, theorem checks and version are preserved in proof-results.json and logs/.
