# Maintenance authorizations and scope restrictions

All organizations, people, agreements, events, and rules in this source are synthetic.

## [M01]

Maintenance authorization MA-27 permits controlled software work on the south archive cluster during the half-open UTC interval [2030-10-27 00:00, 2030-10-27 03:00). Its named operation is image-index rebuild, and it authorizes expected priority P2 indexing alarms only. The authorization explicitly excludes priority P1 security incidents, loss of containment, and any assumption that a security incident can wait until maintenance ends. Although incident A shares some infrastructure with this cluster, its P1 classification remains controlling. The maintenance operator is not authorized to change an incident's priority merely to obtain a deferred response clock. No evidence in the packet records a valid priority reclassification of A.

## [M02]

For a P2 incident within the explicitly named maintenance operation, a qualifying detection occurring inside its authorized half-open window receives an effective acknowledgement-clock start at the window end. A detection outside the window receives no such deferral. The thirty-minute P2 acknowledgement allowance then runs from that effective start, inclusive at its deadline. This is a specific adjustment to an acknowledgement clock, not a declaration that the incident did not exist until the window ended. It does not change the accepted detection record, allow a missed acknowledgement before an already-ended window to be excused, or add time to a P1 containment limit. The incident and maintenance identifiers must match the authorized operation.

## [M03]

A separate authorization MB-27 covers operation M-B, a planned metadata migration affecting the west archive service, during [2030-10-27 02:50 UTC, 2030-10-27 03:20 UTC). Incident B is explicitly classified P2 and tied to M-B by both the accepted incident record and the maintenance operator's completion certificate. Its accepted qualifying detection is 2030-10-27 04:10 +01:00, which is 03:10 UTC. This instant is strictly after the window begins and strictly before it ends. No unplanned extension, early termination, different timezone, or retroactive cancellation is recorded. The maintenance operation completed at the authorized 03:20 UTC end.

## [M04]

The completion certificate states that the operator knew of B during the maintenance period and informed the coordinator. That contact is not the human acknowledgement specified by the playbook, which was delivered later and is recorded in the incident timeline. The authorization does not characterize B as a false alarm or remove it from the incident register. An analyst must therefore retain its accepted detection timestamp, use the specific permitted deferred clock start, and compare the actual delivered acknowledgement against the resulting deadline. Counting from the original detection while ignoring the authorized deferral would apply the wrong effective clock, even though that original detection remains a true event.

## [M05]

The maintenance package is complete for MA-27 and MB-27 window beginnings, endings, authorized operations, and priority restrictions. It includes no other window relevant to incidents A, B, or C during the assessment interval. This window completeness does not make the monitoring data complete and does not certify incident containment. The two authorizations have different scopes despite overlapping calendar dates and a shared service operator. MA-27 cannot be transferred to B simply because it ends near B's window, and MB-27 cannot excuse a P1 action for A. A document reference bearing only the word maintenance, without the operation identifier and time interval, is not sufficient to select the proper clause.

## [M06]

An operations margin note says that analysts sometimes refer informally to the maintenance interval as a quiet period. The signed authorization expressly states that this phrase has no additional technical meaning. It does not suspend emergency notifications, authorize silent handling of security incidents, or establish that all customer traffic was absent. The signed priority restriction and effective-clock clauses take precedence over this informal shorthand. There is no clause requiring a reviewer to infer a favorable outcome whenever work was planned. The purpose of the package is to specify exactly which response-clock exception is authorized and to prevent unrelated windows or priorities from being combined.
