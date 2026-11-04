# Authoritative accepted incident timeline and pause approvals

All organizations, people, agreements, events, and rules in this source are synthetic.

<a id="T01"></a>
## [T01]

Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

<a id="T02"></a>
## [T02]

Authoritative containment confirmation for A occurred at 2030-10-27 03:20 +01:00, equivalent to 02:20 UTC. The containment team then confirmed the affected security path was isolated. A remained uncontained continuously from qualifying detection until this confirmation; this positive incident-state record is independent of whether the monitoring sensors were continuously available. The source therefore establishes that A was still uncontained at 01:00 UTC, the potential executive escalation trigger. Subtracting the printed local labels 03:20 and 02:00 without accounting for their different offsets would not measure the elapsed response interval. No earlier containment event, partial containment accepted as full, or backdated correction exists in this authoritative A record.

<a id="T03"></a>
## [T03]

Commander approval PA-A1 was granted at 00:25 UTC for an external credential dependency blocking A containment from 00:30 through 01:00 UTC. Commander approval PA-A2 was granted at 01:05 UTC for an external routing dependency blocking A containment from 01:10 through 01:50 UTC. Each approval preceded its pause beginning, identified the dependency, and was effective for the stated interval. The pauses are nonoverlapping and both lie entirely between detection and authoritative containment. Their raw durations are thirty and forty minutes. Both approvals expressly remain subject to the combined cap in the applicable playbook revision. They do not waive, restart, or pause any escalation or acknowledgement clock.

<a id="T04"></a>
## [T04]

Incident B's accepted qualifying detection is 2030-10-27 04:10 +01:00, or 03:10 UTC. Its P2 classification and M-B operation identifier match MB-27. A delivered human acknowledgement identifying B and taking responsibility occurred at 2030-10-27 04:45 +01:00, or 03:45 UTC. No containment pause is claimed for B, and there is no P1 classification or changed maintenance scope in the supplied record. The raw elapsed interval from detection to acknowledgement is thirty-five minutes. The effective P2 acknowledgement interval must nevertheless be determined using the authorized maintenance exception, rather than treating raw elapsed time as the only possible response metric.

<a id="T05"></a>
## [T05]

Incident C was accepted as P1 at 2030-10-27 01:50 +02:00, equivalent to 2030-10-26 23:50 UTC. Later actions occurred on October 27, but the qualifying detection timestamp is authoritative and unchanged. The accepted register deliberately contains no authoritative containment timestamp for C. Instead, the shift packet contains the two signed, inconsistent containment attestations reproduced in the scanned attestation source. This is unlike A, whose containment is authoritatively recorded in T02. No rule permits borrowing A's authoritative-record status for C or treating C's latest available testimony as automatically controlling because its document appears later in the transferred packet.
