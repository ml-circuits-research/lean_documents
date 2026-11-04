# Model interpretation and trust boundary

`Audit.Operation` models only the four operations within the complete register R01. `start` is a recorded actual occurrence; its use is non-vacuous because R02-R05 assert starts. All approval/declaration/countersignature `none` values are explicit register absences, never missing C-105 records. Event roles are transcribed from the register labels: approvals and countersignatures are duty-manager actions; declarations are duty-officer actions. `activeIncident` records qualification and activity at start, which is independent of a declaration.

`standard` implements P02: an explicitly granted duty-manager approval exists strictly before actual start. A request is a separate `EventKind` and cannot count as an approval. `emergency` implements all P03 conjuncts: qualifying active incident, declaration strictly before start, and countersignature in the inclusive interval from start to start + 1440. `authorized` implements the exhaustive P01 disjunction. The policy version is P-17 revision 3 only. These are Boolean decisions of the finite model, whose equality to true or false expresses the target; they do not authenticate the records.

Origin is 2028-04-10 00:00 UTC. Integer minute offsets use the Gregorian UTC calendar and exact-minute B02 convention. A day has 1440 minutes in these timestamps. The following offsets were independently computed with Python datetime rather than copied from Lean:

| Timestamp UTC | Minute offset |
| --- | ---: |
| 2028-04-10T08:40 | 520 |
| 2028-04-10T09:00 | 540 |
| 2028-04-10T10:00 | 600 |
| 2028-04-10T10:05 | 605 |
| 2028-04-10T10:15 | 615 |
| 2028-04-11T10:15 | 2055 |
| 2028-04-10T11:30 | 690 |
| 2028-04-10T13:20 | 800 |
| 2028-04-11T09:00 | 1980 |

Source-to-data map: `c101` uses R02 approval 520 and start 540, incident false and absent exception events. `c102` uses R03 start 615, no standard approval, incident true, declaration 605, countersignature 2055. Its request at offset 600 is typed request and not included among granted approvals. `c103` uses R04 equal approval/start 690 and absent exception conditions. `c104` uses R05 start 800, absent approval, incident false and absent declaration/countersignature. No covered events beyond the cutoff are assumed. These particular emergency deadlines precede the cutoff.

Theorem-to-claim map: `claim01` directly supports PA-01 (strict ordering and standard path); `claim02` refutes both material PA-02 assertions (no standard path and request is not approval); `claim03` directly supports PA-03 with the exact 1440-minute endpoint; `claim04` refutes both PA-04 assertions; `claim05` supports actual C-104 start plus failure of both exhaustive paths in PA-05; `claim08` refutes PA-08 by the actual C-102 emergency path despite absent standard approval. This also identifies a counterexample to the proposed implication from absent standard approval to nonauthorization.

`HandoffWorld` is a two-variable projection for PA-06, not a record of actual C-105 facts. H01-H02 report missing transferred records and explicitly allow either actual approval state; R01 excludes C-105. `claim06Countermodels` is auxiliary: two assignments agree that the package lacks a register while disagreeing about approval before the proposed time. The witness-note conflict is unaffected by either assignment. The result demonstrates non-entailment, not actual approval or actual nonapproval. No claim about a complete hypothetical history is needed for this projection.

`miraAffirmsStart0900` transcribes A01 and `leonDeniesStart0900` transcribes A02 after applying H02 operation identity. `claim07Conflict` is auxiliary proof of simultaneous attributed positive and negative evidence for PA-07, not proof that a start and non-start both occurred. P04 supplies no priority rule. No actual C-105 start is modeled as a settled fact.

`handoffPackage` transcribes complete H01 contents as request plus the two A01-A02 notes. `claim10` directly supports PA-10 as finite package nonmembership only; it says nothing about North Quay's event history. Package item categories suffice because the only target is external-register presence, and H01 explicitly states its absence.

PA-09 has no proof: P04 separates prudence from authorization and supplies no prudence criterion. It is outside formal assessment. No operational definition is invented.

All theorem proofs use ordinary core decision procedures; there are no custom axioms, external solver results, or unknown-as-false conversions. Formal status becomes validated only when proof-results.json records successful execution. The independent reviewer must assess transcription and proposition fidelity. This author's model inspection and arithmetic verification are self-review only. Source authenticity, external law, actual unresolved C-105 history and source completeness beyond the stated scope remain outside every theorem.

# Executed validation and self-review

The actual helper check completed with status `passed` on 2026-11-04T13:44:15.530258+00:00. Lean reported version 4.24.0. Nine declared theorems and nine explicit finding-target type assertions passed (18 logged checks). All dependencies are axiom-free except `claim10`, which uses the permitted core `propext` axiom. Exact anchored quote matching and input hash validation passed. Actual commands, target types, axiom output and timestamps are retained in proof-results.json and logs/. No external independent kernel checker was run.

Self-review checked all four finite operation records against R02-R05, both emergency interval endpoints, the day conversion, both C-105 witness polarities, and package-only completeness. Independent semantic review remains pending with the coordinating reviewer.
