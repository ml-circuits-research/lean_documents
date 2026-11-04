# Narrative model interpretation

## Domain and time mapping

The domain is Mira's story state during days 1–10 only. Dates use exact integer story-day labels. `instant day phase = 3*day+phase`, with dawn=0, noon=1, evening=2, is an order-preserving encoding of the named instants; it is not an assertion about real clock durations. Its relevant values are day 2 noon=7, day 5 dawn=15, day 6 noon=19, day 8 dawn=24, and day 8 noon=25. The finite interval runs from day 1 dawn=3 through day 10 evening=32. B-02 supplies within-day ordering.

`deathTime = instant 5 dawn` transcribes T-01. `revivalTime = instant 8 dawn` transcribes T-02, independently corroborated by R-02's explicitly complete revival catalog for Mira in days 1–10. `AliveAt` gives the interval before the recorded death and the interval from recorded restoration through day 10. `DeadAt` gives the interval from death inclusive to revival exclusive. These are interpretations of the authoritative chronology and R-01's immediate death, persistence, exclusivity, and revival rules. They are not conclusions extracted automatically by Lean.

The source chronology is authoritative for the bounded interval. The encoding treats its recorded death as the life-to-death transition and the complete catalog's single revival as the restoring transition. The key-exchange claim also has direct documentary support from F-02's explicit statement that Mira is alive in the day 2 scene; no conclusion about unknown off-page events or other characters is needed.

## Theorem-to-claim mapping

- `keyExchangeAlive` checks that noon day 2 lies in the modeled living interval, supporting C04-OK-01 together with the source account of the actual key exchange.
- `daySixDead` checks both the modeled dead state and exclusion of the living state at noon day 6, supporting the first part of C04-OK-02. This uses the bounded no-other-revivals catalog, not ordinary source silence.
- `daySixNoPhysicalAttendance` encodes the exact necessary-condition argument for the second part of C04-OK-02: for any proposed attendance proposition, if attendance requires life then attendance is impossible at that instant. It does not assume actual attendance or infer a meeting from being alive. Ghosts, dreams, impersonators, and metaphors are outside physical attendance under B-03.
- `revivalAndNoonLife` checks the recorded dawn day 8 restoration time, living state at restoration and noon, and the strict order between them, supporting C04-OK-05. T-02 also directly states that life continues through day 10.

C04-OK-03 is a documentary comparison of story time and narration time. C04-OK-04 is a documentary comparison of speech attribution and authoritative world fact. Neither is assigned a Lean proof: arithmetic on encoded labels would not verify the words, attribution, or narrative perspective.

## Limits and assumptions

The proofs are checks of a source-linked bounded model, not authentication of documents or a general theorem about death. There is no permanent-death axiom; the model explicitly contains restoration. It says nothing about other characters, dates outside days 1–10, Ivo's missing location, key storage, or aesthetic quality. Natural-number labels are adequate because every relevant date and phase is nonnegative. Data transcription, interpretation, and source precedence remain human review obligations. The model contains no custom axioms or inconsistent witness statements and does not promote Mira's quoted claim to a world fact. This author has not conducted an independent semantic review of their own model.

## Execution repair

The initial build attempted `decide` before unfolding the custom proposition definitions and failed to synthesize decidability. Its actual source and failure logs are preserved under `attempts/initial-build/`. The repaired proofs explicitly simplify the pure predicate definitions and exact numeral comparisons. This changed proof elaboration only; model definitions and target propositions were unchanged. Successful current checks are recorded in proof-results.json and logs/.
