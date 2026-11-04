# Evaluator-only incremental mutation scenario

Withhold this file during blind audits. This scenario is an unexecuted design expectation, not an actual validation result.

Copy dossier10 into a distinct retained repository tmp/ reproduction directory. Preserve baseline source bytes, manifests, and actual logs. Change the copied N57 exception start in sources/98-board-exception.md from09:00 to11:00 while retaining the10:00 release. Also change EX01's explanatory inside-window sentence to state that the release and approval precede the new window. Change the N57 operational reference from saying the exception governs the release to a neutral reference requiring applicability review, so the mutated snapshot does not accidentally contain contrary source assertions. Do not mutate the original fixture.

Recompute all changed source hashes and the copied corpus fingerprint, then audit both supplied report variants separately in new retained run directories. C10-OK-07 and C10-ERR-07 require re-evaluation because their exception premise changed. An unchanged report hash must not silently reuse baseline proof or evidence results. Record any additional dependencies discovered by the implementation. Preserve actual commands, output, exit status, and reviewed assumptions. This README claims no execution or result.
