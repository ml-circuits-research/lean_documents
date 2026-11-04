# Model correspondence and limits

The model audits the selected report's eighteen claim groups for the synthetic North Channel incidents A/B/C, October 26-28, 2030. Report assertions are not evidence. Source text and native originals were reviewed before formal conclusions. All original material remains retained, including imperfect OCR and the append-only reviewed alternatives. The author compared original DOCX XML rules R01-R08, rendered PDF clauses M01-M06 and scan pages A01-A04; acceptance hashes are in extraction-review.json. Reviewed scans correct AQ markers, @5:@@ and @5:3@ to A markers, 05:00 and 05:30. No original is overwritten. A retained partial extraction state is explicitly acknowledged; material C containment quotations are readable and reviewed, while their substantive disagreement persists.

## UTC and versions

`utc localMinute offsetMinute` implements R02 as exact integer subtraction. Origin is October 27 00:00 UTC. T01 maps warning 01:30 +02:00 to90-120=-30 (October26 23:30), accepted detection 02:00 +02:00 to120-120=0, and delivered acknowledgement02:12 +02:00 to132-120=12. T02 containment03:20 +01:00 becomes200-60=140. T04 B detection04:10 +01:00 becomes250-60=190, acknowledgement04:45 +01:00 becomes285-60=225. T05 C detection01:50 +02:00 becomes110-120=-10. Independent executed Python fixed-offset datetime conversions agree with manual subtraction in visual-review/time-transcription.log. No geographical timezone/DST inference is used.

`revision` chooses1 for negative accepted detection offsets and2 at/after0 (R06). It uses accepted detection, never raw warning. `qualifyingDetection`, `elapsedInterval`, `acknowledgementTimely`, `aRevision` and `cRevision` respectively support C01,C02,C03,C13,C14. `timely start delivered allowance` checks start≤delivered≤start+allowance, respecting inclusive deadlines and preventing negative response durations from qualifying. Concrete incident records provide non-vacuity; C's authoritative detection is not discarded because its separate containment evidence conflicts.

## Pauses and containment

`Pause` stores approval minute, interval start/end and explicit external-dependency flag from T03. pause1=(25,30,60,true); pause2=(65,70,110,true). `validPause` checks dependency, approval strictly before start, and entire interval within A detection-to-containment. T03 separately states written commander approval, dependency identification and effectiveness. `approvedPausesCapped` checks both valid intervals, nonoverlap, their70-minute sum and45-minute allowed deduction. No general algorithm for overlapping intervals is claimed: these two concrete intervals are proven nonoverlapping, so addition is justified. `pauseCap` maps revision1→60 and revision2→45 per R04. `excludedA` is min(raw70,cap45); `activeA=elapsed140-excluded45=95`. `activeInterval` supports C04, `containmentLate` C05, and `approvedPausesCapped` C06. A five-minute breach of containment does not alter its separately timely twelve-minute acknowledgement.

## Scoped maintenance

`effectiveStart` requires priority2, matching operation and detection in the half-open window [begin,end) before returning the window end; otherwise it returns accepted detection. R07/M02 supply these conjuncts. `noMaintenanceForA` supports C07 with P1 priority, even under a hypothetical matching-operation flag; M01/T01 independently say A is not the scoped P2 indexing event. Maintenance is never added to containment pauses, and R03/R05 leave A acknowledgement/escalation clocks unchanged.

For B, T04 and M03 affirm P2 and the M-B identifier. Window MB27 is170≤minute<200 (02:50–03:20); detection190 lies inside. `startB=200` while historical detection remains190. `bAcknowledgement` supports C08:225-200=25≤30. `bRawVersusEffective` supports C09:225-190=35 is true but not the operative SLA comparison. M04's earlier coordinator contact is not silently promoted to delivered human acknowledgement. No other window is imported; M05's window completeness is not monitoring completeness.

## Role-specific escalation

N01 gives technical queue8 and delivered11; the ten-minute duty fails by1. N02 gives commander delivered22; its twenty-minute duty fails by2. `technicalLate` and `commanderLate` support C10/C11. No earlier delivered role notification exists under the explicit N01/N02/N04 register coverage, so these are bounded event failures rather than generic absence arguments. Queue success, informal awareness and subsequent commander action do not substitute for earlier delivered notifications.

T02 positively records continuous noncontainment from0 to140, represented as `uncontainedA t := 0≤t∧t<140`. This is a source fact, not inferred from telemetry silence or assumed state persistence. `executiveTimely` supports C12: at60 the trigger holds, delivered72 is12 minutes later and≤75. It neither cures the earlier late notifications nor inherits their lateness (N05). Notification clocks never subtract containment pauses.

## Conflict and observation gaps

`Testimony` records incident identifier, proposition minute, polarity and retraction. elise=(C encoded3,300,true,false) and pavel=(3,300,false,false) transcribe reviewed A01-A03. Pavel's explicit denial of full isolation at05:00 is the exact negation of Elise's assertion; the later05:20 endpoint does not describe another proposition or timezone. `cConflict` supports C15 by equality of event coordinates, opposing recorded polarity and no retractions. T05/A03/A04 supply absence of authoritative containment, priority or correction. The model never assumes both inconsistent world propositions, nor treats authentic signatures as proof of truth. Identity authenticity is stipulated only within the synthetic dossier.

`MonitoringWorld` separates gap samples, listed alarms in certified periods and actual gap exfiltration. `gapUnderdetermined` constructs both Boolean event values while preserving no retained gap samples and no listed alarms outside the gap. It is auxiliary for C16/C17. G01's gap is [01:10,01:40); G02 explicitly disclaims sensor completeness for all exfiltration even outside it; G03 ties outage to collector storage, not a transfer event; G04 says another capture is not supplied. These sources justify leaving event unconstrained. The proof is not a simulation or evidence that either event outcome actually occurred. The supported report claims concern non-entailment/support gaps, not proof of exfiltration absence or presence. Source completeness for notification/window records does not migrate to this event domain.

C18 is supported as an attributed-opinion and missing-metric statement under R08/F05. The underlying adjectives remain nonformal; no invented scoring function or Lean target is supplied.

## Execution and independence

Proof-results.json and logs preserve actual Lean version, compilation, requested target checks and dependency axiom audits. Kernel success verifies encoded source transcriptions and reasoning, not source authenticity or semantic completeness. This author performed semantic self-review but no independent reviewer has rederived the run; semantic-review.md states that limitation. No external kernel implementation is claimed. All work remains in this distinct repository tmp/ directory.

First execution note: Lean rejected the reserved keyword `matches` as a parameter name. It was renamed `operationMatches` without changing the rule or targets. The first failed result and build log are retained separately; subsequent proof-results.json records the actual rerun.

Executed final result: Lean4.24.0 passed 33 theorem/target checks. Axiom union: []. All requested direct and auxiliary targets were checked against their exact declared types.
