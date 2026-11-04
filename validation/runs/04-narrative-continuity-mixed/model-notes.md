# Model interpretation and source correspondence

## World, time and trust
All propositions concern fictional Mira during story days 1–10. The authoritative chronology and world rules are accepted as the mandate specifies. They are source transcriptions, not independently authenticated observations. Time is an order-preserving coordinate `tick day phase = (day - 1) * 24 + phase`, with dawn=6, noon=12, evening=18, and end day 10 coded as start day 11. These phase codes preserve the required order; the source does not assert exact dawn clock hours. We use only named instants, date extraction, and relative interval membership. Universal temporal refutations use a supplied concrete counterexample; they do not require completeness of this integer grid.

## Source-to-symbol legend
- T-01 maps day 5 dawn to `deathTime = 102` and identifies the physical key handover.
- T-02 maps day 8 dawn to `revivalTime = 174` and confirms life thereafter through `endTime = 240`.
- R-01 and the complete R-02 catalog justify `DeadAt t := deathTime ≤ t ∧ t < revivalTime` on the relevant bounded interval. Outside days 1–10 this model is not an assertion about the world.
- F-01/F-02 map `keyStoryTime = tick 2 12 = 36`, independently of `narrationFrameTime = tick 7 18 = 162`. F-02 explicitly says Mira was alive at that handover.
- `ConfirmedAliveAt` collects only positive supplied life facts: the handover instant, or the explicit T-02 post-revival interval. It is not an exhaustive life-state catalog; its negation must not be interpreted as death.
- D-01 maps `miraSpeech` to speaker `Person.mira`, `tick 9 12 = 204`, and `Utterance.neverDied`, whose exact lexical meaning is “I never died.” Speech has no coercion or inference into world truth.
- `recordedDeaths = [deathTime]` is positive evidence only. No death-catalog completeness is assumed or needed to refute no-death claims.
- `revivals = [revivalTime]` is complete specifically for Mira during days 1–10 because R-02 explicitly says so. No other absence inference is authorized.

## Targets and correspondence
- `claim01` supports C04-01 by checking the handover instant and its explicit positive life fact. This computational transcription check does not independently discover or authenticate that fact.
- `claim02` refutes C04-02 conditionally on the sourced attendance requirement. Its arbitrary proposition `attendance` denotes the asserted physical meeting occurrence. The sole hypothesis `attendance → ¬ DeadAt (tick 6 12)` follows from physical attendance requiring life and life/death exclusivity. The theorem uses the supported dead state at that instant to derive `¬ attendance`. It neither identifies eligibility with actual presence nor assumes the conclusion. The implication is nonvacuously satisfiable when attendance is false; the death interval itself is supported by the recorded death, rule, and complete revival catalog.
- `claim03` refutes C04-03 by showing the explicitly recorded exchange's day number is not 7. The source explanation, not arithmetic alone, identifies which event is the chapter exchange.
- `claim04` supports C04-04 as an attributed utterance occurrence, never its truth.
- `claim05` refutes C04-05 using a recorded death strictly before day 9 starts. `NeverDiedBefore9` is the necessary restriction of the report's universal absence claim to recorded deaths. Failure of this restriction directly refutes the broader claim; no completeness is asserted. Day 5 precedes both the beginning and noon of day 9, so those readings have the same counterexample.
- `claim06` supports C04-06 by placing day 8 noon inside T-02's explicit living interval.
- `claim07` refutes C04-07 through the witness day 8 noon, an actual named instant inside the universal claim's interval. `AlwaysDeadAfter5` is its restriction to encoded instants, sufficient for a direct refutation. The result does not claim a complete discretization of story time.
- No formal target is asserted for C04-08: Ivo's archive location is unestablished, not false. No formal target is asserted for C04-09: the supplied rules provide no operational aesthetic criterion.
- `claim10` supports C04-10 by inspecting every element of the expressly complete revival catalog and excluding the queried open interval.

## Alternative readings and limitations
D-01 is character speech, not an alternate authoritative history. The false content does not produce contradictory world axioms. F-01's narration date does not relocate F-02's flashback event. No ghost, dream, impersonator, off-page revival, or metaphor repairs a physical attendance assertion under the brief. No subjective aesthetic standard is invented. No fact concerning Ivo's day 6 location follows from his presence at day 2 and day 9. Model review must keep these evidence levels distinct.

## Execution
The source uses Lean core only, ordinary definitions and theorem proofs, with no custom axiom, sorry, admit, external process, or native-evaluation bypass. The helper performs actual compilation, exact-type assertion checks, and theorem axiom inspection. Actual outcomes are in proof-results.json and logs, not inferred from these notes. No independent external kernel validation or independent semantic review is claimed by this author.

Final execution passed using Lean 4.24.0. The referenced proofs use no axioms except accepted core `propext` for claim05 and claim10. Exact targets and dependency inspections are retained in proof-results.json; see author-review.md for technical repairs and the absence of independent semantic/kernel review.
