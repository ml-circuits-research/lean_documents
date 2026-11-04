# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

[Semantic correspondence review](semantic-review.md)

Extraction inventory: 9 documents; 1 pending, partial or blocked. See [ingestion details](ingestion.json) and [coverage](coverage.md).

## C07-C01

### Exact report claim

`input/report.md#C07-C01`

> **C07-C01.** A's qualifying detection was 00:00 UTC on October 27, after the separate raw warning at 23:30 UTC on October 26. Sources: R01, R02, T01.

### Verification question

Is A qualifying detection 00:00 UTC after its separate raw warning?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0004`

> North Channel Observatory operates a synthetic coastal data service. This playbook governs incidents A, B, and C from October 26 through October 28, 2030. A qualifying detection is the first incident classification accepted by the incident coordinator, not an untriaged sensor signal, an email draft, a queue entry, or an invoice from a monitoring provider. Acknowledgement is a delivered human acknowledgement identifying the incident and taking responsibility for response. Containment is an authoritative confirmation that the specified incident path has been isolated; planning an isolation or signing a checklist without completing the isolation is not containment. The source files distinguish authoritative event records from attributed witness claims. The playbook contains no rule making every signed statement an infallible world fact.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0006`

> All elapsed durations must be calculated on a single UTC timeline. Each timestamp bearing a numerical timezone offset is interpreted literally using that offset: UTC equals the printed local clock time minus the printed offset. The offset is fixed for that event even when nearby events display another offset. No outside daylight-saving calendar is needed or permitted to replace an explicit offset. The October dates were selected to make careless subtraction of local clock labels tempting. Exact minute timestamps denote exact instants, rather than intervals of possible occurrence. A deadline expressed as within N minutes is inclusive, so an action at exactly the deadline is timely. All clock changes, windows, and pauses relevant to the assessed incidents are explicitly recorded in the supplied sources.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

### Rules

- R01 uses coordinator-accepted classification, not raw untriaged warning; R02 subtracts each explicit offset.

### Assumptions

- The supplied synthetic records accurately transcribe the named incidents and scoped authoritative events; source authenticity outside the stipulated scenario is not independently certified.
- Timestamps are exact instants. Use their explicit numerical offsets and inclusive deadlines, without importing an external daylight-saving calendar.

### Reasoning

- 1. T01 distinguishes raw warning 01:30 +02:00 from accepted P1 detection 02:00 +02:00.
- 2. Subtracting120 minutes gives prior-day23:30 (offset-30) and October 27 00:00 (offset0).
- 3. Classification remains accepted and uncorrected; the earlier signal cannot replace it as detection.

### Limits

- The conclusion is limited to the specified incident, event, rule and October 26-28, 2030 domain; no broader operational or historical certification follows.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.qualifyingDetection` in module `Audit` (supports): `Audit.warningA = -30 ∧ Audit.detectionA = 0 ∧ Audit.warningA < Audit.detectionA`.
  [Model](models/Audit.lean) · [Executed check](checks/Target017.lean) · [Actual proof log](logs/target-017.log)

### Recommendation

Retain the qualified finding and its stated scope.

## C07-C02

### Exact report claim

`input/report.md#C07-C02`

> **C07-C02.** A's detection-to-containment interval is 140 elapsed minutes: 02:00 +02:00 is 00:00 UTC, while 03:20 +01:00 is 02:20 UTC. Sources: R02, T01, T02, F01.

### Verification question

Is A detection-to-containment duration140 minutes after explicit-offset conversion?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0006`

> All elapsed durations must be calculated on a single UTC timeline. Each timestamp bearing a numerical timezone offset is interpreted literally using that offset: UTC equals the printed local clock time minus the printed offset. The offset is fixed for that event even when nearby events display another offset. No outside daylight-saving calendar is needed or permitted to replace an explicit offset. The October dates were selected to make careless subtraction of local clock labels tempting. Exact minute timestamps denote exact instants, rather than intervals of possible occurrence. A deadline expressed as within N minutes is inclusive, so an action at exactly the deadline is timely. All clock changes, windows, and pauses relevant to the assessed incidents are explicitly recorded in the supplied sources.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T02`

> ## [T02]
> 
> Authoritative containment confirmation for A occurred at 2030-10-27 03:20 +01:00, equivalent to 02:20 UTC. The containment team then confirmed the affected security path was isolated. A remained uncontained continuously from qualifying detection until this confirmation; this positive incident-state record is independent of whether the monitoring sensors were continuously available. The source therefore establishes that A was still uncontained at 01:00 UTC, the potential executive escalation trigger. Subtracting the printed local labels 03:20 and 02:00 without accounting for their different offsets would not measure the elapsed response interval. No earlier containment event, partial containment accepted as full, or backdated correction exists in this authoritative A record.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 873, "end_character": 1667, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/review-correspondence.md](input/sources/review-correspondence.md) — `F01`

> ## [F01]
> 
> The response analyst's draft timeline converts A's detection from 02:00 +02:00 to 00:00 UTC and its containment from 03:20 +01:00 to 02:20 UTC. The elapsed interval is therefore one hundred forty minutes. An early margin calculation obtained eighty minutes by subtracting the two printed local labels; the analyst struck it out after noticing the different offsets. This arithmetic note corroborates the timestamp conversion rule rather than establishing a new clock convention. The relevant distinction is between explicit offsets, not an assumption about how a particular country's daylight-saving schedule normally works on that date.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 816, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "2c1cfb5fe6479718615cf4b6445b281ef66b534d4d017c05b46addbf4d27544a", "artifact_directory": "extraction/D00009/attempt-5oieugsr"}`.

### Rules

- UTC equals local clock minus that event offset; local labels with different offsets cannot be directly subtracted.

### Assumptions

- The supplied synthetic records accurately transcribe the named incidents and scoped authoritative events; source authenticity outside the stipulated scenario is not independently certified.
- Timestamps are exact instants. Use their explicit numerical offsets and inclusive deadlines, without importing an external daylight-saving calendar.

### Reasoning

- 1. 02:00 +02:00 converts to00:00 UTC; 03:20 +01:00 converts to02:20 UTC.
- 2. The common UTC axis is0 to140 minutes, hence140 elapsed minutes.
- 3. F01 corroborates and retracts the tempting80-minute local-label subtraction; T02 supplies authoritative full containment.

### Limits

- The conclusion is limited to the specified incident, event, rule and October 26-28, 2030 domain; no broader operational or historical certification follows.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.elapsedInterval` in module `Audit` (supports): `Audit.detectionA = 0 ∧ Audit.containmentA = 140 ∧ Audit.elapsedA = 140`.
  [Model](models/Audit.lean) · [Executed check](checks/Target018.lean) · [Actual proof log](logs/target-018.log)

### Recommendation

Retain the qualified finding and its stated scope.

## C07-C03

### Exact report claim

`input/report.md#C07-C03`

> **C07-C03.** A's delivered acknowledgement at 00:12 UTC was twelve minutes after detection and met the fifteen-minute P1 requirement. Sources: R03, T01.

### Verification question

Was A delivered acknowledgement timely under the P1 fifteen-minute duty?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0004`

> North Channel Observatory operates a synthetic coastal data service. This playbook governs incidents A, B, and C from October 26 through October 28, 2030. A qualifying detection is the first incident classification accepted by the incident coordinator, not an untriaged sensor signal, an email draft, a queue entry, or an invoice from a monitoring provider. Acknowledgement is a delivered human acknowledgement identifying the incident and taking responsibility for response. Containment is an authoritative confirmation that the specified incident path has been isolated; planning an isolation or signing a checklist without completing the isolation is not containment. The source files distinguish authoritative event records from attributed witness claims. The playbook contains no rule making every signed statement an infallible world fact.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0006`

> All elapsed durations must be calculated on a single UTC timeline. Each timestamp bearing a numerical timezone offset is interpreted literally using that offset: UTC equals the printed local clock time minus the printed offset. The offset is fixed for that event even when nearby events display another offset. No outside daylight-saving calendar is needed or permitted to replace an explicit offset. The October dates were selected to make careless subtraction of local clock labels tempting. Exact minute timestamps denote exact instants, rather than intervals of possible occurrence. A deadline expressed as within N minutes is inclusive, so an action at exactly the deadline is timely. All clock changes, windows, and pauses relevant to the assessed incidents are explicitly recorded in the supplied sources.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0008`

> Priority P1 requires acknowledgement within fifteen elapsed minutes after qualifying detection and containment within ninety active-response minutes after that detection. Priority P2 requires acknowledgement within thirty elapsed minutes after its effective response-clock start, with the maintenance deferral defined in M02 as the only applicable modification. The P1 acknowledgement clock is never paused or deferred. For a P1 containment clock, approved containment pauses may exclude elapsed time under R04. A pause does not alter the detection timestamp, acknowledgement clock, or escalation clock. No SLA in this dossier treats an unapproved pause request as an approved interruption, and no pause can exclude time before its approved beginning or after actual containment.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[8]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

### Rules

- R03 requires delivered human acknowledgement within 15 elapsed minutes, with no pause or maintenance deferral.

### Assumptions

- The supplied synthetic records accurately transcribe the named incidents and scoped authoritative events; source authenticity outside the stipulated scenario is not independently certified.
- Timestamps are exact instants. Use their explicit numerical offsets and inclusive deadlines, without importing an external daylight-saving calendar.

### Reasoning

- 1. T01 records a delivered human acknowledgement taking responsibility at 02:12 +02:00=00:12 UTC.
- 2. It is12 minutes after qualifying detection at 00:00, no later than00:15.
- 3. The model checks both exact interval and inclusive timely predicate; this outcome does not settle containment or escalation.

### Limits

- The conclusion is limited to the specified incident, event, rule and October 26-28, 2030 domain; no broader operational or historical certification follows.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.acknowledgementTimely` in module `Audit` (supports): `Audit.acknowledgementA - Audit.detectionA = 12 ∧ Audit.timely Audit.detectionA Audit.acknowledgementA 15`.
  [Model](models/Audit.lean) · [Executed check](checks/Target019.lean) · [Actual proof log](logs/target-019.log)

### Recommendation

Retain the qualified finding and its stated scope.

## C07-C04

### Exact report claim

`input/report.md#C07-C04`

> **C07-C04.** A's active-response containment interval was ninety-five minutes: 140 elapsed minutes minus the revision 2 cap of forty-five excluded minutes. Sources: R04, R06, T01, T02, T03, F02.

### Verification question

Does A active-response containment time equal140 minus45, or95 minutes?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0010`

> A valid containment pause must identify an external dependency blocking containment, be approved in writing by the incident commander before the pause begins, and specify a beginning and end. Approved pauses exclude only their actual overlap with the detection-to-containment interval. Nonoverlapping approved intervals can be added; overlapping intervals would be unioned so a minute is never excluded twice. Revision 1 caps the total excluded time at sixty minutes for an incident. Revision 2 caps the total at forty-five minutes. The cap applies to the combined excluded duration, not independently to each approved pause. Active-response time equals total elapsed detection-to-containment time minus the smaller of the approved overlapping duration and the applicable combined cap. Approval of a longer pause interval does not waive that cap.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[10]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0014`

> Revision 2 takes effect at 2030-10-27 00:00 UTC for incidents whose qualifying detection occurs at or after that instant. Incidents detected earlier retain revision 1 throughout their response, even when containment, handover, or evidence collection occurs after the boundary. A raw warning signal before midnight does not grandfather an incident whose accepted qualifying detection occurs at midnight. The revision change affects the containment-pause cap only; the acknowledgement, maintenance, and escalation rules reproduced here apply to both versions. A dashboard displaying the currently published revision does not amend an incident's detection event or its retained version. Exact receipt at the boundary belongs to revision 2.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[14]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T02`

> ## [T02]
> 
> Authoritative containment confirmation for A occurred at 2030-10-27 03:20 +01:00, equivalent to 02:20 UTC. The containment team then confirmed the affected security path was isolated. A remained uncontained continuously from qualifying detection until this confirmation; this positive incident-state record is independent of whether the monitoring sensors were continuously available. The source therefore establishes that A was still uncontained at 01:00 UTC, the potential executive escalation trigger. Subtracting the printed local labels 03:20 and 02:00 without accounting for their different offsets would not measure the elapsed response interval. No earlier containment event, partial containment accepted as full, or backdated correction exists in this authoritative A record.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 873, "end_character": 1667, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T03`

> ## [T03]
> 
> Commander approval PA-A1 was granted at 00:25 UTC for an external credential dependency blocking A containment from 00:30 through 01:00 UTC. Commander approval PA-A2 was granted at 01:05 UTC for an external routing dependency blocking A containment from 01:10 through 01:50 UTC. Each approval preceded its pause beginning, identified the dependency, and was effective for the stated interval. The pauses are nonoverlapping and both lie entirely between detection and authoritative containment. Their raw durations are thirty and forty minutes. Both approvals expressly remain subject to the combined cap in the applicable playbook revision. They do not waive, restart, or pause any escalation or acknowledgement clock.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1686, "end_character": 2414, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/review-correspondence.md](input/sources/review-correspondence.md) — `F02`

> ## [F02]
> 
> The analyst adds A's approved nonoverlapping pause durations, thirty plus forty, obtaining seventy raw approved minutes. Because A's accepted qualifying detection is exactly the revision 2 boundary, only forty-five minutes are excluded from the containment metric. The resulting active-response interval is ninety-five minutes, which exceeds the ninety-minute P1 allowance by five minutes. This calculation treats approval validity and combined exclusion cap as separate questions. Both pauses can be validly approved even though their full combined duration is not deductible. Replacing the cap with sixty minutes would improperly apply revision 1 to A.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 835, "end_character": 1499, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "2c1cfb5fe6479718615cf4b6445b281ef66b534d4d017c05b46addbf4d27544a", "artifact_directory": "extraction/D00009/attempt-5oieugsr"}`.

### Rules

- R04 deducts min(approved overlap, applicable combined cap); R06 gives boundary detection revision 2 cap45.

### Assumptions

- The supplied synthetic records accurately transcribe the named incidents and scoped authoritative events; source authenticity outside the stipulated scenario is not independently certified.
- Timestamps are exact instants. Use their explicit numerical offsets and inclusive deadlines, without importing an external daylight-saving calendar.

### Reasoning

- 1. T03 supplies nonoverlapping fully overlapping approved pauses30–60 and70–110, totaling30+40=70 minutes.
- 2. A detection is exactly revision 2 boundary, so exclusion is min(70,45)=45.
- 3. T02 gives140 elapsed minutes; active response=140-45=95, as F02 corroborates.

### Limits

- The conclusion is limited to the specified incident, event, rule and October 26-28, 2030 domain; no broader operational or historical certification follows.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.activeInterval` in module `Audit` (supports): `Audit.elapsedA = 140 ∧ Audit.excludedA = 45 ∧ Audit.activeA = 95`.
  [Model](models/Audit.lean) · [Executed check](checks/Target020.lean) · [Actual proof log](logs/target-020.log)

### Recommendation

Retain the qualified finding and its stated scope.

## C07-C05

### Exact report claim

`input/report.md#C07-C05`

> **C07-C05.** A exceeded the ninety-minute containment allowance by five active-response minutes, despite its timely acknowledgement. Sources: R03, R04, R06, T01, T02, T03, F02.

### Verification question

Does A exceed90-minute containment allowance by 5 despite timely acknowledgement?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0008`

> Priority P1 requires acknowledgement within fifteen elapsed minutes after qualifying detection and containment within ninety active-response minutes after that detection. Priority P2 requires acknowledgement within thirty elapsed minutes after its effective response-clock start, with the maintenance deferral defined in M02 as the only applicable modification. The P1 acknowledgement clock is never paused or deferred. For a P1 containment clock, approved containment pauses may exclude elapsed time under R04. A pause does not alter the detection timestamp, acknowledgement clock, or escalation clock. No SLA in this dossier treats an unapproved pause request as an approved interruption, and no pause can exclude time before its approved beginning or after actual containment.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[8]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0010`

> A valid containment pause must identify an external dependency blocking containment, be approved in writing by the incident commander before the pause begins, and specify a beginning and end. Approved pauses exclude only their actual overlap with the detection-to-containment interval. Nonoverlapping approved intervals can be added; overlapping intervals would be unioned so a minute is never excluded twice. Revision 1 caps the total excluded time at sixty minutes for an incident. Revision 2 caps the total at forty-five minutes. The cap applies to the combined excluded duration, not independently to each approved pause. Active-response time equals total elapsed detection-to-containment time minus the smaller of the approved overlapping duration and the applicable combined cap. Approval of a longer pause interval does not waive that cap.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[10]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0014`

> Revision 2 takes effect at 2030-10-27 00:00 UTC for incidents whose qualifying detection occurs at or after that instant. Incidents detected earlier retain revision 1 throughout their response, even when containment, handover, or evidence collection occurs after the boundary. A raw warning signal before midnight does not grandfather an incident whose accepted qualifying detection occurs at midnight. The revision change affects the containment-pause cap only; the acknowledgement, maintenance, and escalation rules reproduced here apply to both versions. A dashboard displaying the currently published revision does not amend an incident's detection event or its retained version. Exact receipt at the boundary belongs to revision 2.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[14]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T02`

> ## [T02]
> 
> Authoritative containment confirmation for A occurred at 2030-10-27 03:20 +01:00, equivalent to 02:20 UTC. The containment team then confirmed the affected security path was isolated. A remained uncontained continuously from qualifying detection until this confirmation; this positive incident-state record is independent of whether the monitoring sensors were continuously available. The source therefore establishes that A was still uncontained at 01:00 UTC, the potential executive escalation trigger. Subtracting the printed local labels 03:20 and 02:00 without accounting for their different offsets would not measure the elapsed response interval. No earlier containment event, partial containment accepted as full, or backdated correction exists in this authoritative A record.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 873, "end_character": 1667, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T03`

> ## [T03]
> 
> Commander approval PA-A1 was granted at 00:25 UTC for an external credential dependency blocking A containment from 00:30 through 01:00 UTC. Commander approval PA-A2 was granted at 01:05 UTC for an external routing dependency blocking A containment from 01:10 through 01:50 UTC. Each approval preceded its pause beginning, identified the dependency, and was effective for the stated interval. The pauses are nonoverlapping and both lie entirely between detection and authoritative containment. Their raw durations are thirty and forty minutes. Both approvals expressly remain subject to the combined cap in the applicable playbook revision. They do not waive, restart, or pause any escalation or acknowledgement clock.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1686, "end_character": 2414, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/review-correspondence.md](input/sources/review-correspondence.md) — `F02`

> ## [F02]
> 
> The analyst adds A's approved nonoverlapping pause durations, thirty plus forty, obtaining seventy raw approved minutes. Because A's accepted qualifying detection is exactly the revision 2 boundary, only forty-five minutes are excluded from the containment metric. The resulting active-response interval is ninety-five minutes, which exceeds the ninety-minute P1 allowance by five minutes. This calculation treats approval validity and combined exclusion cap as separate questions. Both pauses can be validly approved even though their full combined duration is not deductible. Replacing the cap with sixty minutes would improperly apply revision 1 to A.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 835, "end_character": 1499, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "2c1cfb5fe6479718615cf4b6445b281ef66b534d4d017c05b46addbf4d27544a", "artifact_directory": "extraction/D00009/attempt-5oieugsr"}`.

### Rules

- P1 containment allowance90 active minutes is independent of15-minute acknowledgement duty.

### Assumptions

- The supplied synthetic records accurately transcribe the named incidents and scoped authoritative events; source authenticity outside the stipulated scenario is not independently certified.
- Timestamps are exact instants. Use their explicit numerical offsets and inclusive deadlines, without importing an external daylight-saving calendar.

### Reasoning

- 1. 140 elapsed minus45 permitted exclusion gives95 active minutes.
- 2. 95 is greater than90 by 5, so containment fails its own allowance.
- 3. Acknowledgement at 12 remains timely. Success in one duty does not cancel failure in the other.

### Limits

- The conclusion is limited to the specified incident, event, rule and October 26-28, 2030 domain; no broader operational or historical certification follows.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.containmentLate` in module `Audit` (supports): `90 < Audit.activeA ∧ Audit.activeA - 90 = 5 ∧ Audit.timely Audit.detectionA Audit.acknowledgementA 15`.
  [Model](models/Audit.lean) · [Executed check](checks/Target021.lean) · [Actual proof log](logs/target-021.log)

### Recommendation

Retain the qualified finding and its stated scope.

## C07-C06

### Exact report claim

`input/report.md#C07-C06`

> **C07-C06.** Both A pauses were approved before they began, but only forty-five of their seventy combined minutes are deductible under the applicable cap. Sources: R04, R06, T03.

### Verification question

Were both pauses validly approved even though the full70 minutes cannot be excluded?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0010`

> A valid containment pause must identify an external dependency blocking containment, be approved in writing by the incident commander before the pause begins, and specify a beginning and end. Approved pauses exclude only their actual overlap with the detection-to-containment interval. Nonoverlapping approved intervals can be added; overlapping intervals would be unioned so a minute is never excluded twice. Revision 1 caps the total excluded time at sixty minutes for an incident. Revision 2 caps the total at forty-five minutes. The cap applies to the combined excluded duration, not independently to each approved pause. Active-response time equals total elapsed detection-to-containment time minus the smaller of the approved overlapping duration and the applicable combined cap. Approval of a longer pause interval does not waive that cap.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[10]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0014`

> Revision 2 takes effect at 2030-10-27 00:00 UTC for incidents whose qualifying detection occurs at or after that instant. Incidents detected earlier retain revision 1 throughout their response, even when containment, handover, or evidence collection occurs after the boundary. A raw warning signal before midnight does not grandfather an incident whose accepted qualifying detection occurs at midnight. The revision change affects the containment-pause cap only; the acknowledgement, maintenance, and escalation rules reproduced here apply to both versions. A dashboard displaying the currently published revision does not amend an incident's detection event or its retained version. Exact receipt at the boundary belongs to revision 2.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[14]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T02`

> ## [T02]
> 
> Authoritative containment confirmation for A occurred at 2030-10-27 03:20 +01:00, equivalent to 02:20 UTC. The containment team then confirmed the affected security path was isolated. A remained uncontained continuously from qualifying detection until this confirmation; this positive incident-state record is independent of whether the monitoring sensors were continuously available. The source therefore establishes that A was still uncontained at 01:00 UTC, the potential executive escalation trigger. Subtracting the printed local labels 03:20 and 02:00 without accounting for their different offsets would not measure the elapsed response interval. No earlier containment event, partial containment accepted as full, or backdated correction exists in this authoritative A record.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 873, "end_character": 1667, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T03`

> ## [T03]
> 
> Commander approval PA-A1 was granted at 00:25 UTC for an external credential dependency blocking A containment from 00:30 through 01:00 UTC. Commander approval PA-A2 was granted at 01:05 UTC for an external routing dependency blocking A containment from 01:10 through 01:50 UTC. Each approval preceded its pause beginning, identified the dependency, and was effective for the stated interval. The pauses are nonoverlapping and both lie entirely between detection and authoritative containment. Their raw durations are thirty and forty minutes. Both approvals expressly remain subject to the combined cap in the applicable playbook revision. They do not waive, restart, or pause any escalation or acknowledgement clock.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1686, "end_character": 2414, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

### Rules

- External-dependency pauses require prior written commander approval and bounded overlap; combined cap is not per-pause.

### Assumptions

- The supplied synthetic records accurately transcribe the named incidents and scoped authoritative events; source authenticity outside the stipulated scenario is not independently certified.
- Timestamps are exact instants. Use their explicit numerical offsets and inclusive deadlines, without importing an external daylight-saving calendar.

### Reasoning

- 1. PA-A1 approval00:25 precedes00:30 start; PA-A2 approval01:05 precedes01:10 start. Both specify blocking external dependencies and finite ends.
- 2. Intervals00:30–01:00 and01:10–01:50 do not overlap and lie inside00:00–02:20; durations30 and40 sum70.
- 3. Approval validity and deductibility are separate: revision 2 still caps combined exclusion at 45.

### Limits

- The conclusion is limited to the specified incident, event, rule and October 26-28, 2030 domain; no broader operational or historical certification follows.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.approvedPausesCapped` in module `Audit` (supports): `Audit.validPause Audit.pause1 ∧ Audit.validPause Audit.pause2 ∧ Audit.pause1.ends ≤ Audit.pause2.starts ∧ Audit.pauseMinutes = 70 ∧ Audit.excludedA = 45`.
  [Model](models/Audit.lean) · [Executed check](checks/Target022.lean) · [Actual proof log](logs/target-022.log)

### Recommendation

Retain the qualified finding and its stated scope.

## C07-C07

### Exact report claim

`input/report.md#C07-C07`

> **C07-C07.** MA-27 does not defer A's P1 response clocks; the maintenance exception applies only to its specified P2 operation and does not replace approved containment-pause rules. Sources: R03, R07, M01, M02, T01.

### Verification question

Does MA27 leave A P1 clocks unchanged despite shared infrastructure?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0008`

> Priority P1 requires acknowledgement within fifteen elapsed minutes after qualifying detection and containment within ninety active-response minutes after that detection. Priority P2 requires acknowledgement within thirty elapsed minutes after its effective response-clock start, with the maintenance deferral defined in M02 as the only applicable modification. The P1 acknowledgement clock is never paused or deferred. For a P1 containment clock, approved containment pauses may exclude elapsed time under R04. A pause does not alter the detection timestamp, acknowledgement clock, or escalation clock. No SLA in this dossier treats an unapproved pause request as an approved interruption, and no pause can exclude time before its approved beginning or after actual containment.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[8]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0016`

> An expressly scoped maintenance window may defer the effective P2 acknowledgement-clock start as stated in M02. Priority P1 overrides that deferral. A maintenance window is not itself a containment-pause approval, and its duration cannot be added to an approved external-dependency pause. Where maintenance and a qualifying incident overlap, the analyst must first identify the incident's priority and the maintenance operation's authorized scope. A general statement that maintenance was underway somewhere in the service is insufficient. Unless the relevant clause says otherwise, a window beginning is included and its ending is excluded when deciding whether a detection occurred inside the window. The end timestamp is nevertheless the start of a deferred clock.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[16]", "paragraph_index_in_story": 16, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/maintenance-authorization.pdf.md](input/sources/maintenance-authorization.pdf.md) — `pdf-page-0002`

> [M01]
> Maintenance authorization MA-27 permits controlled software work on the south archive
> cluster during the half-open UTC interval [2030-10-27 00:00, 2030-10-27 03:00). Its named
> operation is image-index rebuild, and it authorizes expected priority P2 indexing alarms
> only. The authorization explicitly excludes priority P1 security incidents, loss of
> containment, and any assumption that a security incident can wait until maintenance ends.
> Although incident A shares some infrastructure with this cluster, its P1 classification
> remains controlling. The maintenance operator is not authorized to change an incident’s
> priority merely to obtain a deferred response clock. No evidence in the packet records a
> valid priority reclassification of A.

Original: [input/originals/D00005.pdf](input/originals/D00005.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00005.pdf", "original_sha256": "33a2eb21bd3e2d3bc1bc3ee643f5694f958f4d55570d1067685bf2a9a9f5d730", "artifact_directory": "extraction/D00005/attempt-ljh5wni_"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/maintenance-authorization.pdf.md](input/sources/maintenance-authorization.pdf.md) — `pdf-page-0003`

> [M02]
> For a P2 incident within the explicitly named maintenance operation, a qualifying detection
> occurring inside its authorized half-open window receives an effective acknowledgement-clock
> start at the window end. A detection outside the window receives no such deferral. The
> thirty-minute P2 acknowledgement allowance then runs from that effective start, inclusive at
> its deadline. This is a specific adjustment to an acknowledgement clock, not a declaration
> that the incident did not exist until the window ended. It does not change the accepted
> detection record, allow a missed acknowledgement before an already-ended window to be
> excused, or add time to a P1 containment limit. The incident and maintenance identifiers
> must match the authorized operation.

Original: [input/originals/D00005.pdf](input/originals/D00005.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 3, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0003.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00005.pdf", "original_sha256": "33a2eb21bd3e2d3bc1bc3ee643f5694f958f4d55570d1067685bf2a9a9f5d730", "artifact_directory": "extraction/D00005/attempt-ljh5wni_"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/maintenance-authorization.pdf.md](input/sources/maintenance-authorization.pdf.md) — `pdf-page-0006`

> [M05]
> The maintenance package is complete for MA-27 and MB-27 window beginnings, endings,
> authorized operations, and priority restrictions. It includes no other window relevant to
> incidents A, B, or C during the assessment interval. This window completeness does not make
> the monitoring data complete and does not certify incident containment. The two
> authorizations have different scopes despite overlapping calendar dates and a shared service
> operator. MA-27 cannot be transferred to B simply because it ends near B’s window, and MB-27
> cannot excuse a P1 action for A. A document reference bearing only the word maintenance,
> without the operation identifier and time interval, is not sufficient to select the proper
> clause.

Original: [input/originals/D00005.pdf](input/originals/D00005.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 6, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0006.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00005.pdf", "original_sha256": "33a2eb21bd3e2d3bc1bc3ee643f5694f958f4d55570d1067685bf2a9a9f5d730", "artifact_directory": "extraction/D00005/attempt-ljh5wni_"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/maintenance-authorization.pdf.md](input/sources/maintenance-authorization.pdf.md) — `pdf-page-0007`

> [M06]
> An operations margin note says that analysts sometimes refer informally to the maintenance
> interval as a quiet period. The signed authorization expressly states that this phrase has
> no additional technical meaning. It does not suspend emergency notifications, authorize
> silent handling of security incidents, or establish that all customer traffic was absent.
> The signed priority restriction and effective-clock clauses take precedence over this
> informal shorthand. There is no clause requiring a reviewer to infer a favorable outcome
> whenever work was planned. The purpose of the package is to specify exactly which response-
> clock exception is authorized and to prevent unrelated windows or priorities from being
> combined.

Original: [input/originals/D00005.pdf](input/originals/D00005.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 7, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0007.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00005.pdf", "original_sha256": "33a2eb21bd3e2d3bc1bc3ee643f5694f958f4d55570d1067685bf2a9a9f5d730", "artifact_directory": "extraction/D00005/attempt-ljh5wni_"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

### Rules

- P1 overrides maintenance deferral. M01 restricts MA27 to named P2 indexing operation; R07 separates maintenance from approved dependency pauses.

### Assumptions

- The supplied synthetic records accurately transcribe the named incidents and scoped authoritative events; source authenticity outside the stipulated scenario is not independently certified.
- Timestamps are exact instants. Use their explicit numerical offsets and inclusive deadlines, without importing an external daylight-saving calendar.

### Reasoning

- 1. T01 accepts A as P1 security incident, expressly not the expected indexing warning.
- 2. M01 explicitly excludes P1 security incidents even though A shares infrastructure; no valid reclassification exists.
- 3. The effective-start model returns actual detection for P1 even if a scope-match flag were true. The source restriction independently prevents adding maintenance duration to containment pauses.

### Limits

- The conclusion is limited to the specified incident, event, rule and October 26-28, 2030 domain; no broader operational or historical certification follows.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.noMaintenanceForA` in module `Audit` (supports): `Audit.effectiveStart 1 false Audit.detectionA 0 180 = Audit.detectionA ∧ Audit.effectiveStart 1 true Audit.detectionA 0 180 = Audit.detectionA`.
  [Model](models/Audit.lean) · [Executed check](checks/Target023.lean) · [Actual proof log](logs/target-023.log)

### Recommendation

Retain the qualified finding and its stated scope.

## C07-C08

### Exact report claim

`input/report.md#C07-C08`

> **C07-C08.** B's effective acknowledgement-clock start was MB-27's 03:20 UTC end, making the 03:45 acknowledgement twenty-five minutes later and timely. Sources: R03, M02, M03, M04, T04, F03.

### Verification question

Is B effective acknowledgement start MB27 end03:20, producing timely25-minute response?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0008`

> Priority P1 requires acknowledgement within fifteen elapsed minutes after qualifying detection and containment within ninety active-response minutes after that detection. Priority P2 requires acknowledgement within thirty elapsed minutes after its effective response-clock start, with the maintenance deferral defined in M02 as the only applicable modification. The P1 acknowledgement clock is never paused or deferred. For a P1 containment clock, approved containment pauses may exclude elapsed time under R04. A pause does not alter the detection timestamp, acknowledgement clock, or escalation clock. No SLA in this dossier treats an unapproved pause request as an approved interruption, and no pause can exclude time before its approved beginning or after actual containment.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[8]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0016`

> An expressly scoped maintenance window may defer the effective P2 acknowledgement-clock start as stated in M02. Priority P1 overrides that deferral. A maintenance window is not itself a containment-pause approval, and its duration cannot be added to an approved external-dependency pause. Where maintenance and a qualifying incident overlap, the analyst must first identify the incident's priority and the maintenance operation's authorized scope. A general statement that maintenance was underway somewhere in the service is insufficient. Unless the relevant clause says otherwise, a window beginning is included and its ending is excluded when deciding whether a detection occurred inside the window. The end timestamp is nevertheless the start of a deferred clock.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[16]", "paragraph_index_in_story": 16, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/maintenance-authorization.pdf.md](input/sources/maintenance-authorization.pdf.md) — `pdf-page-0003`

> [M02]
> For a P2 incident within the explicitly named maintenance operation, a qualifying detection
> occurring inside its authorized half-open window receives an effective acknowledgement-clock
> start at the window end. A detection outside the window receives no such deferral. The
> thirty-minute P2 acknowledgement allowance then runs from that effective start, inclusive at
> its deadline. This is a specific adjustment to an acknowledgement clock, not a declaration
> that the incident did not exist until the window ended. It does not change the accepted
> detection record, allow a missed acknowledgement before an already-ended window to be
> excused, or add time to a P1 containment limit. The incident and maintenance identifiers
> must match the authorized operation.

Original: [input/originals/D00005.pdf](input/originals/D00005.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 3, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0003.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00005.pdf", "original_sha256": "33a2eb21bd3e2d3bc1bc3ee643f5694f958f4d55570d1067685bf2a9a9f5d730", "artifact_directory": "extraction/D00005/attempt-ljh5wni_"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/maintenance-authorization.pdf.md](input/sources/maintenance-authorization.pdf.md) — `pdf-page-0004`

> [M03]
> A separate authorization MB-27 covers operation M-B, a planned metadata migration affecting
> the west archive service, during [2030-10-27 02:50 UTC, 2030-10-27 03:20 UTC). Incident B is
> explicitly classified P2 and tied to M-B by both the accepted incident record and the
> maintenance operator’s completion certificate. Its accepted qualifying detection is
> 2030-10-27 04:10 +01:00, which is 03:10 UTC. This instant is strictly after the window
> begins and strictly before it ends. No unplanned extension, early termination, different
> timezone, or retroactive cancellation is recorded. The maintenance operation completed at
> the authorized 03:20 UTC end.

Original: [input/originals/D00005.pdf](input/originals/D00005.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 4, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0004.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00005.pdf", "original_sha256": "33a2eb21bd3e2d3bc1bc3ee643f5694f958f4d55570d1067685bf2a9a9f5d730", "artifact_directory": "extraction/D00005/attempt-ljh5wni_"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/maintenance-authorization.pdf.md](input/sources/maintenance-authorization.pdf.md) — `pdf-page-0005`

> [M04]
> The completion certificate states that the operator knew of B during the maintenance period
> and informed the coordinator. That contact is not the human acknowledgement specified by the
> playbook, which was delivered later and is recorded in the incident timeline. The
> authorization does not characterize B as a false alarm or remove it from the incident
> register. An analyst must therefore retain its accepted detection timestamp, use the
> specific permitted deferred clock start, and compare the actual delivered acknowledgement
> against the resulting deadline. Counting from the original detection while ignoring the
> authorized deferral would apply the wrong effective clock, even though that original
> detection remains a true event.

Original: [input/originals/D00005.pdf](input/originals/D00005.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 5, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0005.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00005.pdf", "original_sha256": "33a2eb21bd3e2d3bc1bc3ee643f5694f958f4d55570d1067685bf2a9a9f5d730", "artifact_directory": "extraction/D00005/attempt-ljh5wni_"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T04`

> ## [T04]
> 
> Incident B's accepted qualifying detection is 2030-10-27 04:10 +01:00, or 03:10 UTC. Its P2 classification and M-B operation identifier match MB-27. A delivered human acknowledgement identifying B and taking responsibility occurred at 2030-10-27 04:45 +01:00, or 03:45 UTC. No containment pause is claimed for B, and there is no P1 classification or changed maintenance scope in the supplied record. The raw elapsed interval from detection to acknowledgement is thirty-five minutes. The effective P2 acknowledgement interval must nevertheless be determined using the authorized maintenance exception, rather than treating raw elapsed time as the only possible response metric.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2433, "end_character": 3119, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/review-correspondence.md](input/sources/review-correspondence.md) — `F03`

> ## [F03]
> 
> For B, the review note retains 03:10 UTC as actual qualifying detection but uses 03:20 UTC, the authorized MB-27 window end, as the effective acknowledgement-clock start. Delivered acknowledgement at 03:45 UTC is twenty-five minutes after that start, within the thirty-minute allowance. The note explains that a thirty-five-minute raw detection-to-acknowledgement interval is not inherently a failure when an express scoped deferral applies. The same note explicitly rejects applying any maintenance deferral to A because A is priority P1. It does not claim that the existence of planned work alone establishes any other incident's compliance.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1518, "end_character": 2171, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "2c1cfb5fe6479718615cf4b6445b281ef66b534d4d017c05b46addbf4d27544a", "artifact_directory": "extraction/D00009/attempt-5oieugsr"}`.

### Rules

- Matching P2 detection inside [02:50,03:20) uses window end as effective start; allowance30 minutes inclusive.

### Assumptions

- The supplied synthetic records accurately transcribe the named incidents and scoped authoritative events; source authenticity outside the stipulated scenario is not independently certified.
- Timestamps are exact instants. Use their explicit numerical offsets and inclusive deadlines, without importing an external daylight-saving calendar.

### Reasoning

- 1. T04/M03 identify B as P2 and operation M-B matching MB27. Its03:10 detection is inside170≤190<200 minutes from origin.
- 2. M02 therefore selects03:20 (200), without changing historical detection. M04 says earlier operator contact was not the required acknowledgement.
- 3. Delivered03:45 (225) is25 minutes after effective start, before 03:50 deadline.

### Limits

- The conclusion is limited to the specified incident, event, rule and October 26-28, 2030 domain; no broader operational or historical certification follows.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.bAcknowledgement` in module `Audit` (supports): `Audit.startB = 200 ∧ Audit.acknowledgementB - Audit.startB = 25 ∧ Audit.timely Audit.startB Audit.acknowledgementB 30`.
  [Model](models/Audit.lean) · [Executed check](checks/Target024.lean) · [Actual proof log](logs/target-024.log)

### Recommendation

Retain the qualified finding and its stated scope.

## C07-C09

### Exact report claim

`input/report.md#C07-C09`

> **C07-C09.** B's raw detection-to-acknowledgement duration was thirty-five minutes, but that duration does not establish a violation because the authorized effective-clock duration was twenty-five minutes. Sources: R03, M02, M03, T04, F03.

### Verification question

Does the35-minute raw B interval fail to establish a violation under the authorized clock?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0008`

> Priority P1 requires acknowledgement within fifteen elapsed minutes after qualifying detection and containment within ninety active-response minutes after that detection. Priority P2 requires acknowledgement within thirty elapsed minutes after its effective response-clock start, with the maintenance deferral defined in M02 as the only applicable modification. The P1 acknowledgement clock is never paused or deferred. For a P1 containment clock, approved containment pauses may exclude elapsed time under R04. A pause does not alter the detection timestamp, acknowledgement clock, or escalation clock. No SLA in this dossier treats an unapproved pause request as an approved interruption, and no pause can exclude time before its approved beginning or after actual containment.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[8]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/maintenance-authorization.pdf.md](input/sources/maintenance-authorization.pdf.md) — `pdf-page-0003`

> [M02]
> For a P2 incident within the explicitly named maintenance operation, a qualifying detection
> occurring inside its authorized half-open window receives an effective acknowledgement-clock
> start at the window end. A detection outside the window receives no such deferral. The
> thirty-minute P2 acknowledgement allowance then runs from that effective start, inclusive at
> its deadline. This is a specific adjustment to an acknowledgement clock, not a declaration
> that the incident did not exist until the window ended. It does not change the accepted
> detection record, allow a missed acknowledgement before an already-ended window to be
> excused, or add time to a P1 containment limit. The incident and maintenance identifiers
> must match the authorized operation.

Original: [input/originals/D00005.pdf](input/originals/D00005.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 3, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0003.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00005.pdf", "original_sha256": "33a2eb21bd3e2d3bc1bc3ee643f5694f958f4d55570d1067685bf2a9a9f5d730", "artifact_directory": "extraction/D00005/attempt-ljh5wni_"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/maintenance-authorization.pdf.md](input/sources/maintenance-authorization.pdf.md) — `pdf-page-0004`

> [M03]
> A separate authorization MB-27 covers operation M-B, a planned metadata migration affecting
> the west archive service, during [2030-10-27 02:50 UTC, 2030-10-27 03:20 UTC). Incident B is
> explicitly classified P2 and tied to M-B by both the accepted incident record and the
> maintenance operator’s completion certificate. Its accepted qualifying detection is
> 2030-10-27 04:10 +01:00, which is 03:10 UTC. This instant is strictly after the window
> begins and strictly before it ends. No unplanned extension, early termination, different
> timezone, or retroactive cancellation is recorded. The maintenance operation completed at
> the authorized 03:20 UTC end.

Original: [input/originals/D00005.pdf](input/originals/D00005.pdf); extraction: poppler-bbox-layout.
Coordinates: `{"kind": "pdf", "page": 4, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0004.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00005.pdf", "original_sha256": "33a2eb21bd3e2d3bc1bc3ee643f5694f958f4d55570d1067685bf2a9a9f5d730", "artifact_directory": "extraction/D00005/attempt-ljh5wni_"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T04`

> ## [T04]
> 
> Incident B's accepted qualifying detection is 2030-10-27 04:10 +01:00, or 03:10 UTC. Its P2 classification and M-B operation identifier match MB-27. A delivered human acknowledgement identifying B and taking responsibility occurred at 2030-10-27 04:45 +01:00, or 03:45 UTC. No containment pause is claimed for B, and there is no P1 classification or changed maintenance scope in the supplied record. The raw elapsed interval from detection to acknowledgement is thirty-five minutes. The effective P2 acknowledgement interval must nevertheless be determined using the authorized maintenance exception, rather than treating raw elapsed time as the only possible response metric.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2433, "end_character": 3119, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/review-correspondence.md](input/sources/review-correspondence.md) — `F03`

> ## [F03]
> 
> For B, the review note retains 03:10 UTC as actual qualifying detection but uses 03:20 UTC, the authorized MB-27 window end, as the effective acknowledgement-clock start. Delivered acknowledgement at 03:45 UTC is twenty-five minutes after that start, within the thirty-minute allowance. The note explains that a thirty-five-minute raw detection-to-acknowledgement interval is not inherently a failure when an express scoped deferral applies. The same note explicitly rejects applying any maintenance deferral to A because A is priority P1. It does not claim that the existence of planned work alone establishes any other incident's compliance.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1518, "end_character": 2171, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "2c1cfb5fe6479718615cf4b6445b281ef66b534d4d017c05b46addbf4d27544a", "artifact_directory": "extraction/D00009/attempt-5oieugsr"}`.

### Rules

- Use the expressly modified effective P2 clock; actual detection remains a distinct historical event.

### Assumptions

- The supplied synthetic records accurately transcribe the named incidents and scoped authoritative events; source authenticity outside the stipulated scenario is not independently certified.
- Timestamps are exact instants. Use their explicit numerical offsets and inclusive deadlines, without importing an external daylight-saving calendar.

### Reasoning

- 1. 03:45 minus03:10 is35 minutes, so the raw duration in the report is correct.
- 2. M02/M03 authorize start 03:20 for this matched P2 incident, making operative duration25.
- 3. 25≤30 proves this acknowledgement timely. Comparing raw35 to30 would omit an applicable exception, not reveal a breach.

### Limits

- The conclusion is limited to the specified incident, event, rule and October 26-28, 2030 domain; no broader operational or historical certification follows.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.bRawVersusEffective` in module `Audit` (supports): `Audit.acknowledgementB - Audit.detectionB = 35 ∧ Audit.acknowledgementB - Audit.startB = 25 ∧ Audit.timely Audit.startB Audit.acknowledgementB 30`.
  [Model](models/Audit.lean) · [Executed check](checks/Target025.lean) · [Actual proof log](logs/target-025.log)

### Recommendation

Retain the qualified finding and its stated scope.

## C07-C10

### Exact report claim

`input/report.md#C07-C10`

> **C07-C10.** A's technical-lead notification was queued at 00:08 but delivered at 00:11 UTC, one minute after the ten-minute delivered-notification deadline. Sources: R05, N01.

### Verification question

Is A technical-lead notification late by one delivered-notification minute despite timely queueing?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0012`

> The escalation procedure contains three distinct duties for a P1 incident. The technical lead must receive a notification no later than ten elapsed minutes after qualifying detection. The incident commander must receive a notification no later than twenty elapsed minutes after qualifying detection. If the incident remains uncontained sixty elapsed minutes after detection, an executive duty officer must receive a notification no later than fifteen minutes after that trigger, giving a latest time of detection plus seventy-five minutes. All escalation clocks use ordinary elapsed UTC time without containment-pause exclusions. Queue submission, draft completion, attempted dialing, and successful delivery are different events. A notification satisfies the duty only on confirmed delivery to the required role, not merely when queued.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[12]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/notification-register.md](input/sources/notification-register.md) — `N01`

> ## [N01]
> 
> The notification register is complete for A's technical-lead, incident-commander, and executive-duty-officer notifications from 00:00 through 02:30 UTC on October 27. It separately records queue and delivered timestamps. Technical-lead notification TL-A was queued at 00:08 UTC and delivered to the required technical lead at 00:11 UTC. A receipt token confirms delivery. No earlier delivered notification to that role occurred. An automated display highlights the queue timestamp in green because queueing succeeded; that color is not a representation that the playbook's delivered-notification deadline was satisfied. The recipient role and incident identifier are unambiguous.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 159, "end_character": 848, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "bd983f6678e1509ba7b890bfc8662a6a08ad071f1bb1cde800416784867c4050", "artifact_directory": "extraction/D00007/attempt-q2dt7g4i"}`.

- [input/sources/notification-register.md](input/sources/notification-register.md) — `N04`

> ## [N04]
> 
> The register covers notifications to the three specified roles, not all internal chat messages or conversations. The playbook duties concern delivered role-specific notifications, so unrelated informal awareness does not satisfy them. The register's explicit statements that no earlier deliveries occurred support bounded absence reasoning for those exact duties and interval. They do not imply that no person knew of the incident, that no containment work occurred, or that no customer communication was sent. The handover records that the executive message arrived before A's authoritative containment, consistent with the incident remaining active after the escalation trigger.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2235, "end_character": 2925, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "bd983f6678e1509ba7b890bfc8662a6a08ad071f1bb1cde800416784867c4050", "artifact_directory": "extraction/D00007/attempt-q2dt7g4i"}`.

### Rules

- R05 counts confirmed delivery to required role, not queue entry; N01 closes earlier role-delivery events in00:00–02:30.

### Assumptions

- The supplied synthetic records accurately transcribe the named incidents and scoped authoritative events; source authenticity outside the stipulated scenario is not independently certified.
- Timestamps are exact instants. Use their explicit numerical offsets and inclusive deadlines, without importing an external daylight-saving calendar.

### Reasoning

- 1. Detection00:00 gives technical-lead deadline 00:10.
- 2. N01 separately records queue 00:08 and confirmed delivery 00:11, with no earlier delivered notification.
- 3. The green queue indicator is not a timeliness finding.11>10 gives one-minute lateness.

### Limits

- The conclusion is limited to the specified incident, event, rule and October 26-28, 2030 domain; no broader operational or historical certification follows.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.technicalLate` in module `Audit` (supports): `Audit.technicalQueued = 8 ∧ Audit.technicalDelivered = 11 ∧ ¬ Audit.timely Audit.detectionA Audit.technicalDelivered 10 ∧ Audit.technicalDelivered - (Audit.detectionA + 10) = 1`.
  [Model](models/Audit.lean) · [Executed check](checks/Target026.lean) · [Actual proof log](logs/target-026.log)

### Recommendation

Retain the qualified finding and its stated scope.

## C07-C11

### Exact report claim

`input/report.md#C07-C11`

> **C07-C11.** A's commander notification arrived at 00:22 UTC, two minutes after its unpaused twenty-minute deadline; containment pauses do not alter escalation deadlines. Sources: R04, R05, N02.

### Verification question

Was A commander notification two minutes late under its unpaused escalation clock?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0010`

> A valid containment pause must identify an external dependency blocking containment, be approved in writing by the incident commander before the pause begins, and specify a beginning and end. Approved pauses exclude only their actual overlap with the detection-to-containment interval. Nonoverlapping approved intervals can be added; overlapping intervals would be unioned so a minute is never excluded twice. Revision 1 caps the total excluded time at sixty minutes for an incident. Revision 2 caps the total at forty-five minutes. The cap applies to the combined excluded duration, not independently to each approved pause. Active-response time equals total elapsed detection-to-containment time minus the smaller of the approved overlapping duration and the applicable combined cap. Approval of a longer pause interval does not waive that cap.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[10]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0012`

> The escalation procedure contains three distinct duties for a P1 incident. The technical lead must receive a notification no later than ten elapsed minutes after qualifying detection. The incident commander must receive a notification no later than twenty elapsed minutes after qualifying detection. If the incident remains uncontained sixty elapsed minutes after detection, an executive duty officer must receive a notification no later than fifteen minutes after that trigger, giving a latest time of detection plus seventy-five minutes. All escalation clocks use ordinary elapsed UTC time without containment-pause exclusions. Queue submission, draft completion, attempted dialing, and successful delivery are different events. A notification satisfies the duty only on confirmed delivery to the required role, not merely when queued.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[12]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/notification-register.md](input/sources/notification-register.md) — `N02`

> ## [N02]
> 
> Incident-commander notification IC-A was queued at 00:18 UTC and delivered to the incident commander at 00:22 UTC. No earlier delivered commander notification occurred in the complete coverage. The later fact that the commander validly approved containment pauses does not retroactively move the first notification earlier. Executive-duty-officer notification EX-A was delivered at 01:12 UTC. Its message explicitly states that the incident remained uncontained at the sixty-minute mark and requests executive coordination. This message is not a reclassification, a containment event, or an approval to disregard previous escalation delays.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 867, "end_character": 1517, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "bd983f6678e1509ba7b890bfc8662a6a08ad071f1bb1cde800416784867c4050", "artifact_directory": "extraction/D00007/attempt-q2dt7g4i"}`.

- [input/sources/notification-register.md](input/sources/notification-register.md) — `N03`

> ## [N03]
> 
> The shift handover at 01:30 UTC repeats that approved containment pauses affect only the containment metric and are capped under the applicable revision. The outgoing operator wrote an informal calculation using seventy excluded minutes, then marked it provisional pending the revision check. That provisional number appears in a working column, not an approved policy amendment. The handover also notes that the notification console defaults to sorting by queue time, so exported rows must be read with their field names. This presentation detail explains how a report could mistake 00:08 for delivery without establishing that such a mistake is a valid interpretation.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1536, "end_character": 2216, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "bd983f6678e1509ba7b890bfc8662a6a08ad071f1bb1cde800416784867c4050", "artifact_directory": "extraction/D00007/attempt-q2dt7g4i"}`.

- [input/sources/notification-register.md](input/sources/notification-register.md) — `N04`

> ## [N04]
> 
> The register covers notifications to the three specified roles, not all internal chat messages or conversations. The playbook duties concern delivered role-specific notifications, so unrelated informal awareness does not satisfy them. The register's explicit statements that no earlier deliveries occurred support bounded absence reasoning for those exact duties and interval. They do not imply that no person knew of the incident, that no containment work occurred, or that no customer communication was sent. The handover records that the executive message arrived before A's authoritative containment, consistent with the incident remaining active after the escalation trigger.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2235, "end_character": 2925, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "bd983f6678e1509ba7b890bfc8662a6a08ad071f1bb1cde800416784867c4050", "artifact_directory": "extraction/D00007/attempt-q2dt7g4i"}`.

### Rules

- Escalation uses elapsed UTC without containment exclusions. N02/N04 provide bounded no-earlier-delivery facts.

### Assumptions

- The supplied synthetic records accurately transcribe the named incidents and scoped authoritative events; source authenticity outside the stipulated scenario is not independently certified.
- Timestamps are exact instants. Use their explicit numerical offsets and inclusive deadlines, without importing an external daylight-saving calendar.

### Reasoning

- 1. Detection00:00 gives commander deadline 00:20; delivery occurred00:22, not merely queue 00:18.
- 2. 22-20=2 minutes late. No earlier commander delivery occurred in the complete role-specific register.
- 3. Subsequent valid pause approvals neither backdate notification nor alter this deadline.

### Limits

- The conclusion is limited to the specified incident, event, rule and October 26-28, 2030 domain; no broader operational or historical certification follows.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.commanderLate` in module `Audit` (supports): `¬ Audit.timely Audit.detectionA Audit.commanderDelivered 20 ∧ Audit.commanderDelivered - (Audit.detectionA + 20) = 2`.
  [Model](models/Audit.lean) · [Executed check](checks/Target027.lean) · [Actual proof log](logs/target-027.log)

### Recommendation

Retain the qualified finding and its stated scope.

## C07-C12

### Exact report claim

`input/report.md#C07-C12`

> **C07-C12.** A was still uncontained at the 01:00 UTC executive trigger, and the 01:12 executive delivery met the 01:15 deadline despite earlier escalation delays. Sources: R05, T02, N02.

### Verification question

Did the executive duty trigger and then receive timely delivery independently of earlier late stages?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0012`

> The escalation procedure contains three distinct duties for a P1 incident. The technical lead must receive a notification no later than ten elapsed minutes after qualifying detection. The incident commander must receive a notification no later than twenty elapsed minutes after qualifying detection. If the incident remains uncontained sixty elapsed minutes after detection, an executive duty officer must receive a notification no later than fifteen minutes after that trigger, giving a latest time of detection plus seventy-five minutes. All escalation clocks use ordinary elapsed UTC time without containment-pause exclusions. Queue submission, draft completion, attempted dialing, and successful delivery are different events. A notification satisfies the duty only on confirmed delivery to the required role, not merely when queued.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[12]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T02`

> ## [T02]
> 
> Authoritative containment confirmation for A occurred at 2030-10-27 03:20 +01:00, equivalent to 02:20 UTC. The containment team then confirmed the affected security path was isolated. A remained uncontained continuously from qualifying detection until this confirmation; this positive incident-state record is independent of whether the monitoring sensors were continuously available. The source therefore establishes that A was still uncontained at 01:00 UTC, the potential executive escalation trigger. Subtracting the printed local labels 03:20 and 02:00 without accounting for their different offsets would not measure the elapsed response interval. No earlier containment event, partial containment accepted as full, or backdated correction exists in this authoritative A record.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 873, "end_character": 1667, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/notification-register.md](input/sources/notification-register.md) — `N02`

> ## [N02]
> 
> Incident-commander notification IC-A was queued at 00:18 UTC and delivered to the incident commander at 00:22 UTC. No earlier delivered commander notification occurred in the complete coverage. The later fact that the commander validly approved containment pauses does not retroactively move the first notification earlier. Executive-duty-officer notification EX-A was delivered at 01:12 UTC. Its message explicitly states that the incident remained uncontained at the sixty-minute mark and requests executive coordination. This message is not a reclassification, a containment event, or an approval to disregard previous escalation delays.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 867, "end_character": 1517, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "bd983f6678e1509ba7b890bfc8662a6a08ad071f1bb1cde800416784867c4050", "artifact_directory": "extraction/D00007/attempt-q2dt7g4i"}`.

- [input/sources/notification-register.md](input/sources/notification-register.md) — `N05`

> ## [N05]
> 
> A later operations summary says all relevant people were eventually informed. That broad statement is compatible with the exact delivered timestamps and does not settle whether each notification was timely. The procedure intentionally contains multiple steps rather than one aggregate requirement to tell someone. A single timely executive message cannot erase late technical-lead or commander notifications. Conversely, late early-stage notifications do not make a separately timely executive delivery late. The report must distinguish the duties by recipient, trigger, limit, and delivery event to avoid collapsing a mixed operational record into an unsupported all-compliant or all-failed summary.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 2944, "end_character": 3654, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "bd983f6678e1509ba7b890bfc8662a6a08ad071f1bb1cde800416784867c4050", "artifact_directory": "extraction/D00007/attempt-q2dt7g4i"}`.

- [input/sources/review-correspondence.md](input/sources/review-correspondence.md) — `F04`

> ## [F04]
> 
> The review coordinator lists the three A escalation results separately for discussion. The technical-lead delivery happened eleven minutes after detection; the commander delivery happened twenty-two minutes after detection. The executive trigger occurred at 01:00 UTC because A remained uncontained, and the executive delivery followed twelve minutes later at 01:12. The coordinator asks for corrective process discussion but makes no claim that one timely stage cancels another stage's delay. The underlying register is the evidence of events; this correspondence is a calculation and interpretation aid, not an authoritative alteration of delivered timestamps.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2190, "end_character": 2862, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "2c1cfb5fe6479718615cf4b6445b281ef66b534d4d017c05b46addbf4d27544a", "artifact_directory": "extraction/D00009/attempt-5oieugsr"}`.

### Rules

- R05 triggers executive duty if uncontained at detection+60; delivery due within 15 further elapsed minutes.

### Assumptions

- The supplied synthetic records accurately transcribe the named incidents and scoped authoritative events; source authenticity outside the stipulated scenario is not independently certified.
- Timestamps are exact instants. Use their explicit numerical offsets and inclusive deadlines, without importing an external daylight-saving calendar.

### Reasoning

- 1. T02 positively certifies A uncontained continuously from00:00 until 02:20; therefore it was uncontained at 01:00. This is not inferred from missing telemetry.
- 2. N02 gives executive delivery 01:12,12 minutes after trigger and before 01:15 deadline.
- 3. This stage is timely. N05 explicitly prevents treating it as curing earlier delays, or treating earlier delays as making this stage late.

### Limits

- The conclusion is limited to the specified incident, event, rule and October 26-28, 2030 domain; no broader operational or historical certification follows.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.executiveTimely` in module `Audit` (supports): `Audit.uncontainedA 60 ∧ Audit.executiveDelivered = 72 ∧ Audit.executiveDelivered - 60 = 12 ∧ Audit.timely 60 Audit.executiveDelivered 15`.
  [Model](models/Audit.lean) · [Executed check](checks/Target028.lean) · [Actual proof log](logs/target-028.log)

### Recommendation

Retain the qualified finding and its stated scope.

## C07-C13

### Exact report claim

`input/report.md#C07-C13`

> **C07-C13.** A uses revision 2 because accepted qualifying detection occurred exactly at its effective boundary; the earlier untriaged warning does not grandfather it. Sources: R01, R06, T01.

### Verification question

Does A use revision 2 despite raw warning before midnight?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0004`

> North Channel Observatory operates a synthetic coastal data service. This playbook governs incidents A, B, and C from October 26 through October 28, 2030. A qualifying detection is the first incident classification accepted by the incident coordinator, not an untriaged sensor signal, an email draft, a queue entry, or an invoice from a monitoring provider. Acknowledgement is a delivered human acknowledgement identifying the incident and taking responsibility for response. Containment is an authoritative confirmation that the specified incident path has been isolated; planning an isolation or signing a checklist without completing the isolation is not containment. The source files distinguish authoritative event records from attributed witness claims. The playbook contains no rule making every signed statement an infallible world fact.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0014`

> Revision 2 takes effect at 2030-10-27 00:00 UTC for incidents whose qualifying detection occurs at or after that instant. Incidents detected earlier retain revision 1 throughout their response, even when containment, handover, or evidence collection occurs after the boundary. A raw warning signal before midnight does not grandfather an incident whose accepted qualifying detection occurs at midnight. The revision change affects the containment-pause cap only; the acknowledgement, maintenance, and escalation rules reproduced here apply to both versions. A dashboard displaying the currently published revision does not amend an incident's detection event or its retained version. Exact receipt at the boundary belongs to revision 2.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[14]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

### Rules

- R06 includes exact boundary and keys version to accepted qualifying detection, not warning or current dashboard.

### Assumptions

- The supplied synthetic records accurately transcribe the named incidents and scoped authoritative events; source authenticity outside the stipulated scenario is not independently certified.
- Timestamps are exact instants. Use their explicit numerical offsets and inclusive deadlines, without importing an external daylight-saving calendar.

### Reasoning

- 1. Raw warning is23:30 October 26; accepted qualifying detection is00:00 October 27.
- 2. The latter equals revision 2 effective boundary, which expressly belongs to revision 2.
- 3. No correction or withdrawal changes that accepted detection. The earlier warning does not invoke revision 1 cap.

### Limits

- The conclusion is limited to the specified incident, event, rule and October 26-28, 2030 domain; no broader operational or historical certification follows.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.aRevision` in module `Audit` (supports): `Audit.revision Audit.detectionA = 2 ∧ Audit.warningA < 0 ∧ Audit.detectionA = 0`.
  [Model](models/Audit.lean) · [Executed check](checks/Target029.lean) · [Actual proof log](logs/target-029.log)

### Recommendation

Retain the qualified finding and its stated scope.

## C07-C14

### Exact report claim

`input/report.md#C07-C14`

> **C07-C14.** C retains revision 1 because its accepted detection was 23:50 UTC on October 26; later actions do not change that retained version. Sources: R06, T05.

### Verification question

Does C retain revision 1 from its accepted detection ten minutes before boundary?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0006`

> All elapsed durations must be calculated on a single UTC timeline. Each timestamp bearing a numerical timezone offset is interpreted literally using that offset: UTC equals the printed local clock time minus the printed offset. The offset is fixed for that event even when nearby events display another offset. No outside daylight-saving calendar is needed or permitted to replace an explicit offset. The October dates were selected to make careless subtraction of local clock labels tempting. Exact minute timestamps denote exact instants, rather than intervals of possible occurrence. A deadline expressed as within N minutes is inclusive, so an action at exactly the deadline is timely. All clock changes, windows, and pauses relevant to the assessed incidents are explicitly recorded in the supplied sources.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0014`

> Revision 2 takes effect at 2030-10-27 00:00 UTC for incidents whose qualifying detection occurs at or after that instant. Incidents detected earlier retain revision 1 throughout their response, even when containment, handover, or evidence collection occurs after the boundary. A raw warning signal before midnight does not grandfather an incident whose accepted qualifying detection occurs at midnight. The revision change affects the containment-pause cap only; the acknowledgement, maintenance, and escalation rules reproduced here apply to both versions. A dashboard displaying the currently published revision does not amend an incident's detection event or its retained version. Exact receipt at the boundary belongs to revision 2.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[14]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T05`

> ## [T05]
> 
> Incident C was accepted as P1 at 2030-10-27 01:50 +02:00, equivalent to 2030-10-26 23:50 UTC. Later actions occurred on October 27, but the qualifying detection timestamp is authoritative and unchanged. The accepted register deliberately contains no authoritative containment timestamp for C. Instead, the shift packet contains the two signed, inconsistent containment attestations reproduced in the scanned attestation source. This is unlike A, whose containment is authoritatively recorded in T02. No rule permits borrowing A's authoritative-record status for C or treating C's latest available testimony as automatically controlling because its document appears later in the transferred packet.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 3138, "end_character": 3845, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/containment-attestations.scan.pdf.md](input/sources/containment-attestations.scan.pdf.md) — `pdf-page-0005-reviewed-0001`

> [A04]
> The packet includes an administrative cover note confirming that both statements were
> received intact. It does not assert that containment occurred at either proposed time
> and does not establish the earliest possible time of isolation. The incident register
> deliberately leaves C containment uncertified, while retaining C's accepted detection
> before the revision boundary. That detection is not disputed by either signatory. The
> conflict therefore affects the selected containment proposition, not every
> independent fact about C. These scan pages are generated synthetic documents with
> printed signature labels; no real person's handwriting, personal data, or operational
> network identifiers are used.

Original: [input/originals/D00003.pdf](input/originals/D00003.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 5, "origin": {"format": "pdf", "page": 5, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0005-raster.png", "tsv_artifact": "pdf-page-0005.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.75592513265306, "minimum_word_confidence": 62.61581, "confidence_threshold": 85.0, "low_confidence_words": 1, "word_count": 98, "original": "input/originals/D00003.pdf", "original_sha256": "0ac923e297094632a74ab4ab8cf60709989191d75b35d5d29d2820007cbde0d0", "artifact_directory": "extraction/D00003/attempt-m917c19h", "source_anchor": "pdf-page-0005", "root_source_anchor": "pdf-page-0005", "reviewer": "audit_02m", "reason": "Visually inspected original scan raster in full; corrected semantic marker and OCR zero substitutions at 05:00 or 05:30 where present, preserving opposing testimony and all qualifiers.", "reviewed_at": "2026-11-04T15:13:41.005369+00:00", "transcription_snapshot": "input/manual-transcriptions/D00003/88f7763d0ec10b10cfbc90b82a9857fe4d8abdb2e5ba545eef5bc49b897e29bd.txt", "transcription_file_sha256": "b2aeda24d7bc3b6ac37312eb77e12f59e768ce78a5a939bc3e8ec815f01c113f", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

### Rules

- Earlier accepted detections retain revision 1 throughout response; later evidence/containment cannot change the governing version.

### Assumptions

- The supplied synthetic records accurately transcribe the named incidents and scoped authoritative events; source authenticity outside the stipulated scenario is not independently certified.
- Timestamps are exact instants. Use their explicit numerical offsets and inclusive deadlines, without importing an external daylight-saving calendar.

### Reasoning

- 1. 01:50 +02:00 converts to23:50 October 26, minute-10 on the origin axis.
- 2. That is before the00:00 revision 2 boundary; revision 1 applies.
- 3. T05 and A04 agree that detection is authoritative and undisputed, although C containment is not certified. The containment conflict does not erase this independent fact.

### Limits

- The conclusion is limited to the specified incident, event, rule and October 26-28, 2030 domain; no broader operational or historical certification follows.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.cRevision` in module `Audit` (supports): `Audit.detectionC = -10 ∧ Audit.revision Audit.detectionC = 1`.
  [Model](models/Audit.lean) · [Executed check](checks/Target030.lean) · [Actual proof log](logs/target-030.log)

### Recommendation

Retain the qualified finding and its stated scope.

## C07-C15

### Exact report claim

`input/report.md#C07-C15`

> **C07-C15.** The supplied C attestations conflict about complete isolation at 05:00 UTC; no unretracted statement has authority to settle the point over the other. Sources: T05, A01, A02, A03, A04.

### Verification question

Do authentic C attestations conflict without a source authorized to settle them?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0004`

> North Channel Observatory operates a synthetic coastal data service. This playbook governs incidents A, B, and C from October 26 through October 28, 2030. A qualifying detection is the first incident classification accepted by the incident coordinator, not an untriaged sensor signal, an email draft, a queue entry, or an invoice from a monitoring provider. Acknowledgement is a delivered human acknowledgement identifying the incident and taking responsibility for response. Containment is an authoritative confirmation that the specified incident path has been isolated; planning an isolation or signing a checklist without completing the isolation is not containment. The source files distinguish authoritative event records from attributed witness claims. The playbook contains no rule making every signed statement an infallible world fact.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0018`

> Monitoring evidence has its own completeness boundaries. A certified monitoring extract can establish that specified sensors reported no listed alarms during the certified observation periods. It does not prove that no underlying exfiltration occurred unless a supplied rule makes the sensors complete for that event type and period. Missing telemetry cannot by itself prove either successful exfiltration or its absence. Signed conflicting statements about containment remain attributed evidence unless authoritative records or an adopted resolution settle the point. The playbook defines timeliness, roles, pauses, and windows but supplies no objective criterion for judging that an overall response was professionally managed, emotionally reassuring, or exemplary. Those broader judgments require additional standards and argument.
> 

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[18]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T05`

> ## [T05]
> 
> Incident C was accepted as P1 at 2030-10-27 01:50 +02:00, equivalent to 2030-10-26 23:50 UTC. Later actions occurred on October 27, but the qualifying detection timestamp is authoritative and unchanged. The accepted register deliberately contains no authoritative containment timestamp for C. Instead, the shift packet contains the two signed, inconsistent containment attestations reproduced in the scanned attestation source. This is unlike A, whose containment is authoritatively recorded in T02. No rule permits borrowing A's authoritative-record status for C or treating C's latest available testimony as automatically controlling because its document appears later in the transferred packet.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 3138, "end_character": 3845, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/containment-attestations.scan.pdf.md](input/sources/containment-attestations.scan.pdf.md) — `pdf-page-0002-reviewed-0001`

> [A01]
> Containment operator Elise Stone signed a statement at 2030-10-27 05:10 UTC:
> "Incident C was fully isolated at exactly 05:00 UTC. I completed the final network-
> path isolation then, and no C path remained live after that instant." Her statement
> identifies complete containment, not an intermediate mitigation or intended future
> action. It concerns incident C, rather than incident A, and uses UTC explicitly. The
> signature is authentic within this synthetic dossier. The scan preserves her
> attributed words but contains no independently certified network trace proving the
> isolation event.

Original: [input/originals/D00003.pdf](input/originals/D00003.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 2, "origin": {"format": "pdf", "page": 2, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0002-raster.png", "tsv_artifact": "pdf-page-0002.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.01026661363636, "minimum_word_confidence": 63.257053, "confidence_threshold": 85.0, "low_confidence_words": 3, "word_count": 88, "original": "input/originals/D00003.pdf", "original_sha256": "0ac923e297094632a74ab4ab8cf60709989191d75b35d5d29d2820007cbde0d0", "artifact_directory": "extraction/D00003/attempt-m917c19h", "source_anchor": "pdf-page-0002", "root_source_anchor": "pdf-page-0002", "reviewer": "audit_02m", "reason": "Visually inspected original scan raster in full; corrected semantic marker and OCR zero substitutions at 05:00 or 05:30 where present, preserving opposing testimony and all qualifiers.", "reviewed_at": "2026-11-04T15:13:40.604190+00:00", "transcription_snapshot": "input/manual-transcriptions/D00003/f2c73ff169fa72a87f8a86ce29319fba80b81b376e3a4b6229800b78686ff70a.txt", "transcription_file_sha256": "d32b06511c768dc992b931b57c025274bfb0e77499964cb3cba12fd384ffe69e", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/containment-attestations.scan.pdf.md](input/sources/containment-attestations.scan.pdf.md) — `pdf-page-0003-reviewed-0001`

> [A02]
> Security observer Pavel Hart signed a statement at 2030-10-27 05:30 UTC: "Incident C
> was not fully isolated at 05:00 UTC. A C network path remained live at 05:00 and
> continued live until 05:20 UTC." Pavel's statement directly denies the same complete-
> isolation proposition Elise asserts. He is not describing an unrelated service, a
> different timezone, or an event merely adjacent to 05:00. His signature is also
> authentic within the synthetic dossier. He refers to a console observation but
> supplies no exported trace that the mandate makes authoritative over the other signed
> statement.

Original: [input/originals/D00003.pdf](input/originals/D00003.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 3, "origin": {"format": "pdf", "page": 3, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0003-raster.png", "tsv_artifact": "pdf-page-0003.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 93.65185876344086, "minimum_word_confidence": 49.620968, "confidence_threshold": 85.0, "low_confidence_words": 5, "word_count": 93, "original": "input/originals/D00003.pdf", "original_sha256": "0ac923e297094632a74ab4ab8cf60709989191d75b35d5d29d2820007cbde0d0", "artifact_directory": "extraction/D00003/attempt-m917c19h", "source_anchor": "pdf-page-0003", "root_source_anchor": "pdf-page-0003", "reviewer": "audit_02m", "reason": "Visually inspected original scan raster in full; corrected semantic marker and OCR zero substitutions at 05:00 or 05:30 where present, preserving opposing testimony and all qualifiers.", "reviewed_at": "2026-11-04T15:13:40.737741+00:00", "transcription_snapshot": "input/manual-transcriptions/D00003/74d057c1ffd7a573949b5264432bbf95d0ac166f21a1a683072c9f16d09c7d65.txt", "transcription_file_sha256": "e8660b78d23b6e7da20e9a1f81677c45deb3de9df025e357af9b99f0cc41ca1f", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/containment-attestations.scan.pdf.md](input/sources/containment-attestations.scan.pdf.md) — `pdf-page-0004-reviewed-0001`

> [A03]
> The two signatories have not retracted their attestations. No signed correction,
> adjudication, authoritative C containment record, or evidence-priority rule resolving
> the conflict is supplied. A later signing time alone does not make Pavel's statement
> an authorized correction of Elise's. Likewise, Elise's role as containment operator
> does not make her account infallible under the playbook. The packet's authenticity
> stipulation concerns the identity of the signatories and integrity of the text, not
> the historical truth of every assertion. A reviewer must preserve both attributed
> positions rather than accept both as unconditional facts or silently discard the less
> convenient account.

Original: [input/originals/D00003.pdf](input/originals/D00003.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 4, "origin": {"format": "pdf", "page": 4, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0004-raster.png", "tsv_artifact": "pdf-page-0004.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.55065942857144, "minimum_word_confidence": 71.014496, "confidence_threshold": 85.0, "low_confidence_words": 1, "word_count": 98, "original": "input/originals/D00003.pdf", "original_sha256": "0ac923e297094632a74ab4ab8cf60709989191d75b35d5d29d2820007cbde0d0", "artifact_directory": "extraction/D00003/attempt-m917c19h", "source_anchor": "pdf-page-0004", "root_source_anchor": "pdf-page-0004", "reviewer": "audit_02m", "reason": "Visually inspected original scan raster in full; corrected semantic marker and OCR zero substitutions at 05:00 or 05:30 where present, preserving opposing testimony and all qualifiers.", "reviewed_at": "2026-11-04T15:13:40.869589+00:00", "transcription_snapshot": "input/manual-transcriptions/D00003/653097fa4c7e85eb684393bda9dd0a3959fec379a0851eefccc17e303dbea4da.txt", "transcription_file_sha256": "3cd2223066b90c450f6320f6735834f622d46f3d4bb084bc3f84f9078d16b979", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

- [input/sources/containment-attestations.scan.pdf.md](input/sources/containment-attestations.scan.pdf.md) — `pdf-page-0005-reviewed-0001`

> [A04]
> The packet includes an administrative cover note confirming that both statements were
> received intact. It does not assert that containment occurred at either proposed time
> and does not establish the earliest possible time of isolation. The incident register
> deliberately leaves C containment uncertified, while retaining C's accepted detection
> before the revision boundary. That detection is not disputed by either signatory. The
> conflict therefore affects the selected containment proposition, not every
> independent fact about C. These scan pages are generated synthetic documents with
> printed signature labels; no real person's handwriting, personal data, or operational
> network identifiers are used.

Original: [input/originals/D00003.pdf](input/originals/D00003.pdf); extraction: manual-transcription.
Coordinates: `{"kind": "ocr", "page": 5, "origin": {"format": "pdf", "page": 5, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0005-raster.png", "tsv_artifact": "pdf-page-0005.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.75592513265306, "minimum_word_confidence": 62.61581, "confidence_threshold": 85.0, "low_confidence_words": 1, "word_count": 98, "original": "input/originals/D00003.pdf", "original_sha256": "0ac923e297094632a74ab4ab8cf60709989191d75b35d5d29d2820007cbde0d0", "artifact_directory": "extraction/D00003/attempt-m917c19h", "source_anchor": "pdf-page-0005", "root_source_anchor": "pdf-page-0005", "reviewer": "audit_02m", "reason": "Visually inspected original scan raster in full; corrected semantic marker and OCR zero substitutions at 05:00 or 05:30 where present, preserving opposing testimony and all qualifiers.", "reviewed_at": "2026-11-04T15:13:41.005369+00:00", "transcription_snapshot": "input/manual-transcriptions/D00003/88f7763d0ec10b10cfbc90b82a9857fe4d8abdb2e5ba545eef5bc49b897e29bd.txt", "transcription_file_sha256": "b2aeda24d7bc3b6ac37312eb77e12f59e768ce78a5a939bc3e8ec815f01c113f", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

### Rules

- Authentic signatures identify speakers, not automatic world truth. Retain both assertions unless authorized resolution or authoritative record exists.

### Assumptions

- The supplied synthetic records accurately transcribe the named incidents and scoped authoritative events; source authenticity outside the stipulated scenario is not independently certified.
- Timestamps are exact instants. Use their explicit numerical offsets and inclusive deadlines, without importing an external daylight-saving calendar.

### Reasoning

- 1. Visually reviewed A01 has Elise asserting full C isolation exactly 05:00; A02 has Pavel explicitly denying full isolation at 05:00 and saying a path stayed live until 05:20.
- 2. Their incident, timezone and event instant match. The model records one proposition with opposite attributed polarity, not two contradictory global facts.
- 3. A03 says neither statement was retracted and no correction, priority rule or authoritative C record resolves them. Later signing05:30 and operator role do not create precedence.
- 4. A04 cover note merely confirms intact receipt. T05 intentionally lacks authoritative containment, so the report accurately identifies unresolved conflict.

### Limits

- The conclusion is limited to the specified incident, event, rule and October 26-28, 2030 domain; no broader operational or historical certification follows.
- The meta-claim of conflict is supported; actual C containment at 05:00 remains disputed. No formal conclusion about its true isolation time is asserted.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.cConflict` in module `Audit` (supports): `Audit.elise.incident = Audit.pavel.incident ∧ Audit.elise.minute = Audit.pavel.minute ∧ Audit.elise.fullyIsolated ≠ Audit.pavel.fullyIsolated ∧ Audit.elise.retracted = false ∧ Audit.pavel.retracted = false`.
  [Model](models/Audit.lean) · [Executed check](checks/Target031.lean) · [Actual proof log](logs/target-031.log)

### Recommendation

Retain the qualified finding and its stated scope.

## C07-C16

### Exact report claim

`input/report.md#C07-C16`

> **C07-C16.** The supplied monitoring evidence does not determine whether exfiltration occurred during the 01:10–01:40 UTC gap; absence of retained telemetry is not a negative event record. Sources: R08, G01, G02, G03, G04.

### Verification question

Does the01:10–01:40 telemetry gap leave exfiltration unknown instead of proving absence?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0018`

> Monitoring evidence has its own completeness boundaries. A certified monitoring extract can establish that specified sensors reported no listed alarms during the certified observation periods. It does not prove that no underlying exfiltration occurred unless a supplied rule makes the sensors complete for that event type and period. Missing telemetry cannot by itself prove either successful exfiltration or its absence. Signed conflicting statements about containment remain attributed evidence unless authoritative records or an adopted resolution settle the point. The playbook defines timeliness, roles, pauses, and windows but supplies no objective criterion for judging that an overall response was professionally managed, emotionally reassuring, or exemplary. Those broader judgments require additional standards and argument.
> 

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[18]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T02`

> ## [T02]
> 
> Authoritative containment confirmation for A occurred at 2030-10-27 03:20 +01:00, equivalent to 02:20 UTC. The containment team then confirmed the affected security path was isolated. A remained uncontained continuously from qualifying detection until this confirmation; this positive incident-state record is independent of whether the monitoring sensors were continuously available. The source therefore establishes that A was still uncontained at 01:00 UTC, the potential executive escalation trigger. Subtracting the printed local labels 03:20 and 02:00 without accounting for their different offsets would not measure the elapsed response interval. No earlier containment event, partial containment accepted as full, or backdated correction exists in this authoritative A record.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 873, "end_character": 1667, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-pjjy7nug"}`.

- [input/sources/monitoring-coverage.md](input/sources/monitoring-coverage.md) — `G01`

> ## [G01]
> 
> The monitoring package certifies collection from A's egress sensors during [00:00, 01:10) UTC and [01:40, 02:30] UTC on October 27. It explicitly does not cover [01:10, 01:40) UTC because the collector's storage service was unavailable. Boundary brackets describe the certified collection intervals, not assumptions about attacker behavior. The retained records show no listed exfiltration alarms during the certified periods. There are no retained samples from the thirty-minute gap. The package contains no reconstruction of those missing samples, no redundant complete sensor stream, and no statement that silence from the collector proves absence of network activity.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 166, "end_character": 847, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "1ce800a888704355cbfe2e1478cc7111aa84695beb40b6bf419bfba6d11b2c1c", "artifact_directory": "extraction/D00006/attempt-dv_w766o"}`.

- [input/sources/monitoring-coverage.md](input/sources/monitoring-coverage.md) — `G02`

> ## [G02]
> 
> The sensor design note says the listed alarms detect particular signatures and traffic thresholds. It expressly declines to assert that every possible exfiltration would produce an alarm, even when collection is functioning. Thus the observation “no listed alarms in retained samples” is narrower than “no exfiltration occurred.” During the collection gap, even the narrower alarm observation lacks samples. The operational incident state in T02 remains independently documented: A was uncontained until 02:20 UTC. Being uncontained does not itself prove that data were taken, and becoming contained does not establish a complete retrospective history of earlier data movement.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 866, "end_character": 1553, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "1ce800a888704355cbfe2e1478cc7111aa84695beb40b6bf419bfba6d11b2c1c", "artifact_directory": "extraction/D00006/attempt-dv_w766o"}`.

- [input/sources/monitoring-coverage.md](input/sources/monitoring-coverage.md) — `G03`

> ## [G03]
> 
> A storage support ticket attributes the telemetry outage to a collector volume reaching its configured capacity. The ticket concerns the observation system and does not identify who, if anyone, initiated exfiltration. It does not allege that a malicious actor caused the storage condition, and no source connects the volume event to a successful transfer of protected records. A missing observational period can justify requesting additional evidence or marking a support gap. It cannot supply the absent positive premise for a report that asserts exfiltration, nor the absent complete negative evidence for a report that rules exfiltration out.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1572, "end_character": 2227, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "1ce800a888704355cbfe2e1478cc7111aa84695beb40b6bf419bfba6d11b2c1c", "artifact_directory": "extraction/D00006/attempt-dv_w766o"}`.

- [input/sources/monitoring-coverage.md](input/sources/monitoring-coverage.md) — `G04`

> ## [G04]
> 
> The security liaison requested a packet capture from a separate network appliance for the gap. The response says that archive was not transferred with this dossier. The package inventory is complete for supplied monitoring files only. It says nothing about whether another team possesses a usable capture, whether the capture would reveal an event, or whether collection was complete at that appliance. No report may fill this uncertainty by inventing a favorable or unfavorable result. A future authenticated capture might narrow the uncertainty, but the present finite evidence neither confirms nor denies exfiltration during the missing period.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2246, "end_character": 2903, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "1ce800a888704355cbfe2e1478cc7111aa84695beb40b6bf419bfba6d11b2c1c", "artifact_directory": "extraction/D00006/attempt-dv_w766o"}`.

### Rules

- R08 separates observations from events; negative alarm observations require sensor completeness before implying no exfiltration, which G02 expressly withholds.

### Assumptions

- The supplied synthetic records accurately transcribe the named incidents and scoped authoritative events; source authenticity outside the stipulated scenario is not independently certified.
- Timestamps are exact instants. Use their explicit numerical offsets and inclusive deadlines, without importing an external daylight-saving calendar.

### Reasoning

- 1. G01 provides no samples in half-open[01:10,01:40); no-alarm observations apply only to certified intervals outside it.
- 2. G02 denies completeness even when collection works, and uncontained incident state does not itself decide data transfer.
- 3. G04 says separate capture was not transferred and its contents/completeness cannot be invented.
- 4. The auxiliary model allows event=true and false while retaining missing gap samples and no listed alarms outside the gap. Thus exfiltration absence is not established.

### Limits

- The conclusion is limited to the specified incident, event, rule and October 26-28, 2030 domain; no broader operational or historical certification follows.
- The hypothetical worlds establish a missing-premise distinction, not actual exfiltration or non-exfiltration.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **auxiliary**.

### Formal evidence

- `Audit.gapUnderdetermined` in module `Audit` (auxiliary): `∀ event : Bool, ∃ w : Audit.MonitoringWorld, w.retainedGapSamples = false ∧ w.listedAlarmsOutsideGap = false ∧ w.exfiltrationInGap = event`.
  [Model](models/Audit.lean) · [Executed check](checks/Target032.lean) · [Actual proof log](logs/target-032.log)

### Recommendation

Obtain authenticated gap-period capture and its sensor/event coverage before deciding occurrence.

## C07-C17

### Exact report claim

`input/report.md#C07-C17`

> **C07-C17.** The same monitoring gap also does not establish exfiltration: the storage outage and missing samples supply no positive transfer event, so an assertion of occurrence would lack support. Sources: R08, G01, G02, G03, G04.

### Verification question

Does the same monitoring gap also fail to establish exfiltration occurrence?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0018`

> Monitoring evidence has its own completeness boundaries. A certified monitoring extract can establish that specified sensors reported no listed alarms during the certified observation periods. It does not prove that no underlying exfiltration occurred unless a supplied rule makes the sensors complete for that event type and period. Missing telemetry cannot by itself prove either successful exfiltration or its absence. Signed conflicting statements about containment remain attributed evidence unless authoritative records or an adopted resolution settle the point. The playbook defines timeliness, roles, pauses, and windows but supplies no objective criterion for judging that an overall response was professionally managed, emotionally reassuring, or exemplary. Those broader judgments require additional standards and argument.
> 

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[18]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/monitoring-coverage.md](input/sources/monitoring-coverage.md) — `G01`

> ## [G01]
> 
> The monitoring package certifies collection from A's egress sensors during [00:00, 01:10) UTC and [01:40, 02:30] UTC on October 27. It explicitly does not cover [01:10, 01:40) UTC because the collector's storage service was unavailable. Boundary brackets describe the certified collection intervals, not assumptions about attacker behavior. The retained records show no listed exfiltration alarms during the certified periods. There are no retained samples from the thirty-minute gap. The package contains no reconstruction of those missing samples, no redundant complete sensor stream, and no statement that silence from the collector proves absence of network activity.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 166, "end_character": 847, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "1ce800a888704355cbfe2e1478cc7111aa84695beb40b6bf419bfba6d11b2c1c", "artifact_directory": "extraction/D00006/attempt-dv_w766o"}`.

- [input/sources/monitoring-coverage.md](input/sources/monitoring-coverage.md) — `G02`

> ## [G02]
> 
> The sensor design note says the listed alarms detect particular signatures and traffic thresholds. It expressly declines to assert that every possible exfiltration would produce an alarm, even when collection is functioning. Thus the observation “no listed alarms in retained samples” is narrower than “no exfiltration occurred.” During the collection gap, even the narrower alarm observation lacks samples. The operational incident state in T02 remains independently documented: A was uncontained until 02:20 UTC. Being uncontained does not itself prove that data were taken, and becoming contained does not establish a complete retrospective history of earlier data movement.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 866, "end_character": 1553, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "1ce800a888704355cbfe2e1478cc7111aa84695beb40b6bf419bfba6d11b2c1c", "artifact_directory": "extraction/D00006/attempt-dv_w766o"}`.

- [input/sources/monitoring-coverage.md](input/sources/monitoring-coverage.md) — `G03`

> ## [G03]
> 
> A storage support ticket attributes the telemetry outage to a collector volume reaching its configured capacity. The ticket concerns the observation system and does not identify who, if anyone, initiated exfiltration. It does not allege that a malicious actor caused the storage condition, and no source connects the volume event to a successful transfer of protected records. A missing observational period can justify requesting additional evidence or marking a support gap. It cannot supply the absent positive premise for a report that asserts exfiltration, nor the absent complete negative evidence for a report that rules exfiltration out.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1572, "end_character": 2227, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "1ce800a888704355cbfe2e1478cc7111aa84695beb40b6bf419bfba6d11b2c1c", "artifact_directory": "extraction/D00006/attempt-dv_w766o"}`.

- [input/sources/monitoring-coverage.md](input/sources/monitoring-coverage.md) — `G04`

> ## [G04]
> 
> The security liaison requested a packet capture from a separate network appliance for the gap. The response says that archive was not transferred with this dossier. The package inventory is complete for supplied monitoring files only. It says nothing about whether another team possesses a usable capture, whether the capture would reveal an event, or whether collection was complete at that appliance. No report may fill this uncertainty by inventing a favorable or unfavorable result. A future authenticated capture might narrow the uncertainty, but the present finite evidence neither confirms nor denies exfiltration during the missing period.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2246, "end_character": 2903, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "1ce800a888704355cbfe2e1478cc7111aa84695beb40b6bf419bfba6d11b2c1c", "artifact_directory": "extraction/D00006/attempt-dv_w766o"}`.

### Rules

- Observation-system failure is not a positive event premise; missing evidence cannot be assigned an unfavorable event value.

### Assumptions

- The supplied synthetic records accurately transcribe the named incidents and scoped authoritative events; source authenticity outside the stipulated scenario is not independently certified.
- Timestamps are exact instants. Use their explicit numerical offsets and inclusive deadlines, without importing an external daylight-saving calendar.

### Reasoning

- 1. G03 attributes the outage to storage capacity and identifies no attacker or protected-record transfer.
- 2. G01 supplies no gap samples and G04 supplies no transferred independent capture.
- 3. The same evidence permits a hypothetical no-exfiltration completion as well as an exfiltration completion. Therefore neither polarity follows; the report correctly identifies occurrence as unsupported rather than false.

### Limits

- The conclusion is limited to the specified incident, event, rule and October 26-28, 2030 domain; no broader operational or historical certification follows.
- A support gap does not refute the underlying exfiltration proposition. No positive or complete negative event record is supplied.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **auxiliary**.

### Formal evidence

- `Audit.gapUnderdetermined` in module `Audit` (auxiliary): `∀ event : Bool, ∃ w : Audit.MonitoringWorld, w.retainedGapSamples = false ∧ w.listedAlarmsOutsideGap = false ∧ w.exfiltrationInGap = event`.
  [Model](models/Audit.lean) · [Executed check](checks/Target032.lean) · [Actual proof log](logs/target-032.log)

### Recommendation

Retain the support-gap finding and seek direct scoped transfer evidence.

## C07-C18

### Exact report claim

`input/report.md#C07-C18`

> **C07-C18.** The manager's description of the response as professionally managed and reassuring is an attributed opinion; the supplied playbook does not define a formal criterion for that overall judgment. Sources: R08, F05.

### Verification question

Does the report correctly separate the management adjectives from formally defined timeliness criteria?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0018`

> Monitoring evidence has its own completeness boundaries. A certified monitoring extract can establish that specified sensors reported no listed alarms during the certified observation periods. It does not prove that no underlying exfiltration occurred unless a supplied rule makes the sensors complete for that event type and period. Missing telemetry cannot by itself prove either successful exfiltration or its absence. Signed conflicting statements about containment remain attributed evidence unless authoritative records or an adopted resolution settle the point. The playbook defines timeliness, roles, pauses, and windows but supplies no objective criterion for judging that an overall response was professionally managed, emotionally reassuring, or exemplary. Those broader judgments require additional standards and argument.
> 

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[18]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-u6jv2_lo"}`.

- [input/sources/review-correspondence.md](input/sources/review-correspondence.md) — `F05`

> ## [F05]
> 
> A manager describes the response in an email as “professionally managed and reassuring.” A shift employee calls the early escalation delays avoidable. Neither provides an agreed scoring rubric, weighting of outcomes, or definition of professional management. Those views can be included as attributed opinions, but the objective timeliness record alone does not determine every broader evaluative adjective. The correspondence also distinguishes the unresolved C containment disagreement from the separate missing A monitoring period. One is conflicting testimony about a specific event; the other is unavailable observational evidence, and neither should be compressed into a claim that every supplied incident fact is unreliable.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 2881, "end_character": 3622, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "2c1cfb5fe6479718615cf4b6445b281ef66b534d4d017c05b46addbf4d27544a", "artifact_directory": "extraction/D00009/attempt-5oieugsr"}`.

### Rules

- R08 supplies no objective criterion for professionally managed or reassuring; attribution does not make evaluative content a mathematical consequence.

### Assumptions

- The supplied synthetic records accurately transcribe the named incidents and scoped authoritative events; source authenticity outside the stipulated scenario is not independently certified.
- Timestamps are exact instants. Use their explicit numerical offsets and inclusive deadlines, without importing an external daylight-saving calendar.

### Reasoning

- 1. F05 attributes the favorable phrase to a manager and also records an employee opinion that early delays were avoidable.
- 2. Neither supplies a rubric, outcome weighting or definition for the overall adjective.
- 3. The report qualified meta-claim is supported. Underlying management merits remain nonformal and are not assigned a Lean target.

### Limits

- The conclusion is limited to the specified incident, event, rule and October 26-28, 2030 domain; no broader operational or historical certification follows.
- No verdict is given on whether the response deserved the adjectives.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Retain attribution; specify an evaluative framework before assessing the broader judgment.
