# Monitoring extracts, coverage gap, and signal limitations

All organizations, people, agreements, events, and rules in this source are synthetic.

<a id="G01"></a>
## [G01]

The monitoring package certifies collection from A's egress sensors during [00:00, 01:10) UTC and [01:40, 02:30] UTC on October 27. It explicitly does not cover [01:10, 01:40) UTC because the collector's storage service was unavailable. Boundary brackets describe the certified collection intervals, not assumptions about attacker behavior. The retained records show no listed exfiltration alarms during the certified periods. There are no retained samples from the thirty-minute gap. The package contains no reconstruction of those missing samples, no redundant complete sensor stream, and no statement that silence from the collector proves absence of network activity.

<a id="G02"></a>
## [G02]

The sensor design note says the listed alarms detect particular signatures and traffic thresholds. It expressly declines to assert that every possible exfiltration would produce an alarm, even when collection is functioning. Thus the observation “no listed alarms in retained samples” is narrower than “no exfiltration occurred.” During the collection gap, even the narrower alarm observation lacks samples. The operational incident state in T02 remains independently documented: A was uncontained until 02:20 UTC. Being uncontained does not itself prove that data were taken, and becoming contained does not establish a complete retrospective history of earlier data movement.

<a id="G03"></a>
## [G03]

A storage support ticket attributes the telemetry outage to a collector volume reaching its configured capacity. The ticket concerns the observation system and does not identify who, if anyone, initiated exfiltration. It does not allege that a malicious actor caused the storage condition, and no source connects the volume event to a successful transfer of protected records. A missing observational period can justify requesting additional evidence or marking a support gap. It cannot supply the absent positive premise for a report that asserts exfiltration, nor the absent complete negative evidence for a report that rules exfiltration out.

<a id="G04"></a>
## [G04]

The security liaison requested a packet capture from a separate network appliance for the gap. The response says that archive was not transferred with this dossier. The package inventory is complete for supplied monitoring files only. It says nothing about whether another team possesses a usable capture, whether the capture would reveal an event, or whether collection was complete at that appliance. No report may fill this uncertainty by inventing a favorable or unfavorable result. A future authenticated capture might narrow the uncertainty, but the present finite evidence neither confirms nor denies exfiltration during the missing period.
