# Evidence-backed claim audit

Lean checks the encoded propositions, not source authenticity, extraction accuracy, completeness, legal authority, or the adequacy of the model. Source filters are defensive checks, not a sandbox for hostile Lean code.

Technical verification: executed successfully using Lean (version 4.24.0, x86_64-unknown-linux-gnu, commit 797c613eb9b6d4ec95db23e3e00af9ac6657f24b, Release)

[Proof results](proof-results.json) · [Input manifest](input/manifest.json)

[Semantic correspondence review](semantic-review.md)

Extraction inventory: 9 documents; 1 pending, partial or blocked. See [ingestion details](ingestion.json) and [coverage](coverage.md).

## C07-01

### Exact report claim

`input/report.md#C07-01`

> **C07-01.** A's qualifying detection was at 00:00 UTC on October 27, 2030. Sources: R01, R02, T01.

### Verification question

Was A qualifying detection exactly October 27 00:00 UTC, distinguishing accepted classification from the earlier raw warning?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0004`

> North Channel Observatory operates a synthetic coastal data service. This playbook governs incidents A, B, and C from October 26 through October 28, 2030. A qualifying detection is the first incident classification accepted by the incident coordinator, not an untriaged sensor signal, an email draft, a queue entry, or an invoice from a monitoring provider. Acknowledgement is a delivered human acknowledgement identifying the incident and taking responsibility for response. Containment is an authoritative confirmation that the specified incident path has been isolated; planning an isolation or signing a checklist without completing the isolation is not containment. The source files distinguish authoritative event records from attributed witness claims. The playbook contains no rule making every signed statement an infallible world fact.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0006`

> All elapsed durations must be calculated on a single UTC timeline. Each timestamp bearing a numerical timezone offset is interpreted literally using that offset: UTC equals the printed local clock time minus the printed offset. The offset is fixed for that event even when nearby events display another offset. No outside daylight-saving calendar is needed or permitted to replace an explicit offset. The October dates were selected to make careless subtraction of local clock labels tempting. Exact minute timestamps denote exact instants, rather than intervals of possible occurrence. A deadline expressed as within N minutes is inclusive, so an action at exactly the deadline is timely. All clock changes, windows, and pauses relevant to the assessed incidents are explicitly recorded in the supplied sources.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

### Rules

- R01 defines qualifying detection as the coordinator-accepted classification. R02 converts UTC as local time minus the explicit numerical offset.

### Assumptions

- Apply only the supplied synthetic playbook and its expressly authoritative event records for A/B/C during October 26-28, 2030. Exact minutes and numerical offsets are literal; no external timezone convention is assumed.
- Material native-source text was inspected against original PDF pages or DOCX XML; independent datetime calculations are retained in arithmetic-check.md. This is source-to-model transcription, not live operational authentication.

### Reasoning

- 1. T01 separately records raw warning at 01:30 +02:00 and accepted P1 detection at 02:00 +02:00.
- 2. The accepted timestamp converts to 00:00 UTC on October 27. The raw warning converts to October 26 23:30 and cannot replace it.
- 3. The report exactly identifies the accepted-detection instant; the checked conversion supports it.

### Limits

- This establishes the supplied accepted event, not an independently measured earliest sensor anomaly.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim01` in module `Audit` (supports): `Audit.aDetection = 0`.
  [Model](models/Audit.lean) · [Executed check](checks/Target017.lean) · [Actual proof log](logs/target-017.log)

### Recommendation

Retain the detection timestamp and keep the raw warning in a separate field.

## C07-02

### Exact report claim

`input/report.md#C07-02`

> **C07-02.** Only eighty minutes elapsed between A's qualifying detection at local 02:00 and containment at local 03:20. Sources: R02, T01, T02, F01.

### Verification question

Is actual UTC elapsed time from A accepted local 02:00 +02:00 detection to local 03:20 +01:00 containment eighty minutes?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0006`

> All elapsed durations must be calculated on a single UTC timeline. Each timestamp bearing a numerical timezone offset is interpreted literally using that offset: UTC equals the printed local clock time minus the printed offset. The offset is fixed for that event even when nearby events display another offset. No outside daylight-saving calendar is needed or permitted to replace an explicit offset. The October dates were selected to make careless subtraction of local clock labels tempting. Exact minute timestamps denote exact instants, rather than intervals of possible occurrence. A deadline expressed as within N minutes is inclusive, so an action at exactly the deadline is timely. All clock changes, windows, and pauses relevant to the assessed incidents are explicitly recorded in the supplied sources.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T02`

> ## [T02]
> 
> Authoritative containment confirmation for A occurred at 2030-10-27 03:20 +01:00, equivalent to 02:20 UTC. The containment team then confirmed the affected security path was isolated. A remained uncontained continuously from qualifying detection until this confirmation; this positive incident-state record is independent of whether the monitoring sensors were continuously available. The source therefore establishes that A was still uncontained at 01:00 UTC, the potential executive escalation trigger. Subtracting the printed local labels 03:20 and 02:00 without accounting for their different offsets would not measure the elapsed response interval. No earlier containment event, partial containment accepted as full, or backdated correction exists in this authoritative A record.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 873, "end_character": 1667, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

- [input/sources/review-correspondence.md](input/sources/review-correspondence.md) — `F01`

> ## [F01]
> 
> The response analyst's draft timeline converts A's detection from 02:00 +02:00 to 00:00 UTC and its containment from 03:20 +01:00 to 02:20 UTC. The elapsed interval is therefore one hundred forty minutes. An early margin calculation obtained eighty minutes by subtracting the two printed local labels; the analyst struck it out after noticing the different offsets. This arithmetic note corroborates the timestamp conversion rule rather than establishing a new clock convention. The relevant distinction is between explicit offsets, not an assumption about how a particular country's daylight-saving schedule normally works on that date.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 816, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "2c1cfb5fe6479718615cf4b6445b281ef66b534d4d017c05b46addbf4d27544a", "artifact_directory": "extraction/D00009/attempt-lohr3nkf"}`.

### Rules

- R02 requires one UTC timeline and each event's explicit offset; printed local labels with different offsets cannot be subtracted as one clock.

### Assumptions

- Apply only the supplied synthetic playbook and its expressly authoritative event records for A/B/C during October 26-28, 2030. Exact minutes and numerical offsets are literal; no external timezone convention is assumed.
- Material native-source text was inspected against original PDF pages or DOCX XML; independent datetime calculations are retained in arithmetic-check.md. This is source-to-model transcription, not live operational authentication.

### Reasoning

- 1. Detection converts to 00:00 UTC while containment converts to 02:20 UTC, using +02:00 and +01:00 respectively.
- 2. Elapsed time is 140 minutes, not the 80-minute difference of the local labels. F01 records that local-label calculation as struck out.
- 3. The exact 80-minute elapsed assertion is contradicted by the supplied timestamps and mandatory conversion rule.

### Limits

- This is raw elapsed time before permitted containment exclusions; active-response duration is a separate quantity.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim02` in module `Audit` (refutes): `Audit.aElapsed = 140 ∧ Audit.aElapsed ≠ 80`.
  [Model](models/Audit.lean) · [Executed check](checks/Target018.lean) · [Actual proof log](logs/target-018.log)

### Recommendation

Correct elapsed time to 140 minutes and show both explicit-offset conversions.

## C07-03

### Exact report claim

`input/report.md#C07-03`

> **C07-03.** A's delivered human acknowledgement was timely under the fifteen-minute P1 allowance. Sources: R03, T01.

### Verification question

Did the actual delivered human acknowledgement of A satisfy the inclusive fifteen-minute P1 deadline after accepted detection?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0004`

> North Channel Observatory operates a synthetic coastal data service. This playbook governs incidents A, B, and C from October 26 through October 28, 2030. A qualifying detection is the first incident classification accepted by the incident coordinator, not an untriaged sensor signal, an email draft, a queue entry, or an invoice from a monitoring provider. Acknowledgement is a delivered human acknowledgement identifying the incident and taking responsibility for response. Containment is an authoritative confirmation that the specified incident path has been isolated; planning an isolation or signing a checklist without completing the isolation is not containment. The source files distinguish authoritative event records from attributed witness claims. The playbook contains no rule making every signed statement an infallible world fact.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0006`

> All elapsed durations must be calculated on a single UTC timeline. Each timestamp bearing a numerical timezone offset is interpreted literally using that offset: UTC equals the printed local clock time minus the printed offset. The offset is fixed for that event even when nearby events display another offset. No outside daylight-saving calendar is needed or permitted to replace an explicit offset. The October dates were selected to make careless subtraction of local clock labels tempting. Exact minute timestamps denote exact instants, rather than intervals of possible occurrence. A deadline expressed as within N minutes is inclusive, so an action at exactly the deadline is timely. All clock changes, windows, and pauses relevant to the assessed incidents are explicitly recorded in the supplied sources.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0008`

> Priority P1 requires acknowledgement within fifteen elapsed minutes after qualifying detection and containment within ninety active-response minutes after that detection. Priority P2 requires acknowledgement within thirty elapsed minutes after its effective response-clock start, with the maintenance deferral defined in M02 as the only applicable modification. The P1 acknowledgement clock is never paused or deferred. For a P1 containment clock, approved containment pauses may exclude elapsed time under R04. A pause does not alter the detection timestamp, acknowledgement clock, or escalation clock. No SLA in this dossier treats an unapproved pause request as an approved interruption, and no pause can exclude time before its approved beginning or after actual containment.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[8]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

### Rules

- R01 requires delivered human acknowledgement accepting responsibility; R03 allows 15 elapsed minutes for P1 without pauses or deferral.

### Assumptions

- Apply only the supplied synthetic playbook and its expressly authoritative event records for A/B/C during October 26-28, 2030. Exact minutes and numerical offsets are literal; no external timezone convention is assumed.
- Material native-source text was inspected against original PDF pages or DOCX XML; independent datetime calculations are retained in arithmetic-check.md. This is source-to-model transcription, not live operational authentication.

### Reasoning

- 1. T01 records accepted detection 00:00 UTC and a delivered human acknowledgement taking responsibility at 00:12 UTC.
- 2. Twelve elapsed minutes is within the inclusive fifteen-minute allowance.
- 3. The support is an actual delivered acknowledgement, not queueing or informal awareness.

### Limits

- This says nothing by itself about containment or separate escalation duties.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim03` in module `Audit` (supports): `Audit.aAcknowledgement - Audit.aDetection = 12 ∧ Audit.aAcknowledgement ≤ Audit.aDetection + 15`.
  [Model](models/Audit.lean) · [Executed check](checks/Target019.lean) · [Actual proof log](logs/target-019.log)

### Recommendation

Retain the timely acknowledgement finding separately from other duties.

## C07-04

### Exact report claim

`input/report.md#C07-04`

> **C07-04.** A's active-response containment interval was eighty minutes after permissible pause exclusions. Sources: R04, R06, T01, T02, T03, F02.

### Verification question

After valid pause overlap and the applicable combined revision cap, was A active containment time eighty minutes?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0006`

> All elapsed durations must be calculated on a single UTC timeline. Each timestamp bearing a numerical timezone offset is interpreted literally using that offset: UTC equals the printed local clock time minus the printed offset. The offset is fixed for that event even when nearby events display another offset. No outside daylight-saving calendar is needed or permitted to replace an explicit offset. The October dates were selected to make careless subtraction of local clock labels tempting. Exact minute timestamps denote exact instants, rather than intervals of possible occurrence. A deadline expressed as within N minutes is inclusive, so an action at exactly the deadline is timely. All clock changes, windows, and pauses relevant to the assessed incidents are explicitly recorded in the supplied sources.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0010`

> A valid containment pause must identify an external dependency blocking containment, be approved in writing by the incident commander before the pause begins, and specify a beginning and end. Approved pauses exclude only their actual overlap with the detection-to-containment interval. Nonoverlapping approved intervals can be added; overlapping intervals would be unioned so a minute is never excluded twice. Revision 1 caps the total excluded time at sixty minutes for an incident. Revision 2 caps the total at forty-five minutes. The cap applies to the combined excluded duration, not independently to each approved pause. Active-response time equals total elapsed detection-to-containment time minus the smaller of the approved overlapping duration and the applicable combined cap. Approval of a longer pause interval does not waive that cap.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[10]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0014`

> Revision 2 takes effect at 2030-10-27 00:00 UTC for incidents whose qualifying detection occurs at or after that instant. Incidents detected earlier retain revision 1 throughout their response, even when containment, handover, or evidence collection occurs after the boundary. A raw warning signal before midnight does not grandfather an incident whose accepted qualifying detection occurs at midnight. The revision change affects the containment-pause cap only; the acknowledgement, maintenance, and escalation rules reproduced here apply to both versions. A dashboard displaying the currently published revision does not amend an incident's detection event or its retained version. Exact receipt at the boundary belongs to revision 2.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[14]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T02`

> ## [T02]
> 
> Authoritative containment confirmation for A occurred at 2030-10-27 03:20 +01:00, equivalent to 02:20 UTC. The containment team then confirmed the affected security path was isolated. A remained uncontained continuously from qualifying detection until this confirmation; this positive incident-state record is independent of whether the monitoring sensors were continuously available. The source therefore establishes that A was still uncontained at 01:00 UTC, the potential executive escalation trigger. Subtracting the printed local labels 03:20 and 02:00 without accounting for their different offsets would not measure the elapsed response interval. No earlier containment event, partial containment accepted as full, or backdated correction exists in this authoritative A record.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 873, "end_character": 1667, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T03`

> ## [T03]
> 
> Commander approval PA-A1 was granted at 00:25 UTC for an external credential dependency blocking A containment from 00:30 through 01:00 UTC. Commander approval PA-A2 was granted at 01:05 UTC for an external routing dependency blocking A containment from 01:10 through 01:50 UTC. Each approval preceded its pause beginning, identified the dependency, and was effective for the stated interval. The pauses are nonoverlapping and both lie entirely between detection and authoritative containment. Their raw durations are thirty and forty minutes. Both approvals expressly remain subject to the combined cap in the applicable playbook revision. They do not waive, restart, or pause any escalation or acknowledgement clock.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1686, "end_character": 2414, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

- [input/sources/review-correspondence.md](input/sources/review-correspondence.md) — `F02`

> ## [F02]
> 
> The analyst adds A's approved nonoverlapping pause durations, thirty plus forty, obtaining seventy raw approved minutes. Because A's accepted qualifying detection is exactly the revision 2 boundary, only forty-five minutes are excluded from the containment metric. The resulting active-response interval is ninety-five minutes, which exceeds the ninety-minute P1 allowance by five minutes. This calculation treats approval validity and combined exclusion cap as separate questions. Both pauses can be validly approved even though their full combined duration is not deductible. Replacing the cap with sixty minutes would improperly apply revision 1 to A.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 835, "end_character": 1499, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "2c1cfb5fe6479718615cf4b6445b281ef66b534d4d017c05b46addbf4d27544a", "artifact_directory": "extraction/D00009/attempt-lohr3nkf"}`.

### Rules

- R04 deducts min(total approved overlapping pause duration, applicable combined cap). R06 assigns revision 2 to accepted detection exactly at the boundary; its cap is 45.

### Assumptions

- Apply only the supplied synthetic playbook and its expressly authoritative event records for A/B/C during October 26-28, 2030. Exact minutes and numerical offsets are literal; no external timezone convention is assumed.
- Material native-source text was inspected against original PDF pages or DOCX XML; independent datetime calculations are retained in arithmetic-check.md. This is source-to-model transcription, not live operational authentication.

### Reasoning

- 1. A actual UTC elapsed interval is 140 minutes. T03 establishes valid nonoverlapping pauses of 30 and 40 minutes entirely within that interval.
- 2. Their raw sum 70 is capped at 45 because accepted detection 0 selects revision 2. Active time is 140-45=95.
- 3. Eighty would result from improperly deducting the old 60-minute revision 1 cap. The actual prescribed metric is 95, refuting the report value.

### Limits

- Both pause approvals can be valid while their combined full duration remains nondeductible.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim04` in module `Audit` (refutes): `Audit.activeA = 95 ∧ Audit.activeA ≠ 80`.
  [Model](models/Audit.lean) · [Executed check](checks/Target020.lean) · [Actual proof log](logs/target-020.log)

### Recommendation

Replace eighty with ninety-five active-response minutes and identify the revision 2 combined cap.

## C07-05

### Exact report claim

`input/report.md#C07-05`

> **C07-05.** A met the ninety-minute active-response containment SLA. Sources: R03, R04, R06, T01, T02, T03, F02.

### Verification question

Did A meet its inclusive ninety-minute active-response containment SLA after the permissible capped deduction?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0008`

> Priority P1 requires acknowledgement within fifteen elapsed minutes after qualifying detection and containment within ninety active-response minutes after that detection. Priority P2 requires acknowledgement within thirty elapsed minutes after its effective response-clock start, with the maintenance deferral defined in M02 as the only applicable modification. The P1 acknowledgement clock is never paused or deferred. For a P1 containment clock, approved containment pauses may exclude elapsed time under R04. A pause does not alter the detection timestamp, acknowledgement clock, or escalation clock. No SLA in this dossier treats an unapproved pause request as an approved interruption, and no pause can exclude time before its approved beginning or after actual containment.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[8]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0010`

> A valid containment pause must identify an external dependency blocking containment, be approved in writing by the incident commander before the pause begins, and specify a beginning and end. Approved pauses exclude only their actual overlap with the detection-to-containment interval. Nonoverlapping approved intervals can be added; overlapping intervals would be unioned so a minute is never excluded twice. Revision 1 caps the total excluded time at sixty minutes for an incident. Revision 2 caps the total at forty-five minutes. The cap applies to the combined excluded duration, not independently to each approved pause. Active-response time equals total elapsed detection-to-containment time minus the smaller of the approved overlapping duration and the applicable combined cap. Approval of a longer pause interval does not waive that cap.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[10]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0014`

> Revision 2 takes effect at 2030-10-27 00:00 UTC for incidents whose qualifying detection occurs at or after that instant. Incidents detected earlier retain revision 1 throughout their response, even when containment, handover, or evidence collection occurs after the boundary. A raw warning signal before midnight does not grandfather an incident whose accepted qualifying detection occurs at midnight. The revision change affects the containment-pause cap only; the acknowledgement, maintenance, and escalation rules reproduced here apply to both versions. A dashboard displaying the currently published revision does not amend an incident's detection event or its retained version. Exact receipt at the boundary belongs to revision 2.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[14]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T02`

> ## [T02]
> 
> Authoritative containment confirmation for A occurred at 2030-10-27 03:20 +01:00, equivalent to 02:20 UTC. The containment team then confirmed the affected security path was isolated. A remained uncontained continuously from qualifying detection until this confirmation; this positive incident-state record is independent of whether the monitoring sensors were continuously available. The source therefore establishes that A was still uncontained at 01:00 UTC, the potential executive escalation trigger. Subtracting the printed local labels 03:20 and 02:00 without accounting for their different offsets would not measure the elapsed response interval. No earlier containment event, partial containment accepted as full, or backdated correction exists in this authoritative A record.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 873, "end_character": 1667, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T03`

> ## [T03]
> 
> Commander approval PA-A1 was granted at 00:25 UTC for an external credential dependency blocking A containment from 00:30 through 01:00 UTC. Commander approval PA-A2 was granted at 01:05 UTC for an external routing dependency blocking A containment from 01:10 through 01:50 UTC. Each approval preceded its pause beginning, identified the dependency, and was effective for the stated interval. The pauses are nonoverlapping and both lie entirely between detection and authoritative containment. Their raw durations are thirty and forty minutes. Both approvals expressly remain subject to the combined cap in the applicable playbook revision. They do not waive, restart, or pause any escalation or acknowledgement clock.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1686, "end_character": 2414, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

- [input/sources/review-correspondence.md](input/sources/review-correspondence.md) — `F02`

> ## [F02]
> 
> The analyst adds A's approved nonoverlapping pause durations, thirty plus forty, obtaining seventy raw approved minutes. Because A's accepted qualifying detection is exactly the revision 2 boundary, only forty-five minutes are excluded from the containment metric. The resulting active-response interval is ninety-five minutes, which exceeds the ninety-minute P1 allowance by five minutes. This calculation treats approval validity and combined exclusion cap as separate questions. Both pauses can be validly approved even though their full combined duration is not deductible. Replacing the cap with sixty minutes would improperly apply revision 1 to A.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 835, "end_character": 1499, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "2c1cfb5fe6479718615cf4b6445b281ef66b534d4d017c05b46addbf4d27544a", "artifact_directory": "extraction/D00009/attempt-lohr3nkf"}`.

### Rules

- R03 allows 90 active minutes; R04/R06 require 140 elapsed minus min(70,45), not uncapped or revision 1 deductions.

### Assumptions

- Apply only the supplied synthetic playbook and its expressly authoritative event records for A/B/C during October 26-28, 2030. Exact minutes and numerical offsets are literal; no external timezone convention is assumed.
- Material native-source text was inspected against original PDF pages or DOCX XML; independent datetime calculations are retained in arithmetic-check.md. This is source-to-model transcription, not live operational authentication.

### Reasoning

- 1. Actual active time is 95 minutes after both valid pauses and the combined 45-minute cap.
- 2. Ninety-five exceeds the inclusive 90-minute limit by 5.
- 3. The reported SLA success is directly refuted by the correctly computed metric, regardless of A's timely acknowledgement.

### Limits

- This is a five-minute containment-SLA failure under the fictional playbook, not a verdict on every aspect of response quality.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim05` in module `Audit` (refutes): `¬ (Audit.activeA ≤ 90) ∧ Audit.activeA - 90 = 5`.
  [Model](models/Audit.lean) · [Executed check](checks/Target021.lean) · [Actual proof log](logs/target-021.log)

### Recommendation

Record a five-minute containment breach and retain separate outcomes for acknowledgement/escalation.

## C07-06

### Exact report claim

`input/report.md#C07-06`

> **C07-06.** All seventy approved pause minutes may be excluded from A's containment clock because each pause was approved before it began. Sources: R04, R06, T03.

### Verification question

Does approval of both A pause intervals before their starts permit deduction of all seventy minutes despite the applicable combined cap?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0010`

> A valid containment pause must identify an external dependency blocking containment, be approved in writing by the incident commander before the pause begins, and specify a beginning and end. Approved pauses exclude only their actual overlap with the detection-to-containment interval. Nonoverlapping approved intervals can be added; overlapping intervals would be unioned so a minute is never excluded twice. Revision 1 caps the total excluded time at sixty minutes for an incident. Revision 2 caps the total at forty-five minutes. The cap applies to the combined excluded duration, not independently to each approved pause. Active-response time equals total elapsed detection-to-containment time minus the smaller of the approved overlapping duration and the applicable combined cap. Approval of a longer pause interval does not waive that cap.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[10]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0014`

> Revision 2 takes effect at 2030-10-27 00:00 UTC for incidents whose qualifying detection occurs at or after that instant. Incidents detected earlier retain revision 1 throughout their response, even when containment, handover, or evidence collection occurs after the boundary. A raw warning signal before midnight does not grandfather an incident whose accepted qualifying detection occurs at midnight. The revision change affects the containment-pause cap only; the acknowledgement, maintenance, and escalation rules reproduced here apply to both versions. A dashboard displaying the currently published revision does not amend an incident's detection event or its retained version. Exact receipt at the boundary belongs to revision 2.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[14]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T02`

> ## [T02]
> 
> Authoritative containment confirmation for A occurred at 2030-10-27 03:20 +01:00, equivalent to 02:20 UTC. The containment team then confirmed the affected security path was isolated. A remained uncontained continuously from qualifying detection until this confirmation; this positive incident-state record is independent of whether the monitoring sensors were continuously available. The source therefore establishes that A was still uncontained at 01:00 UTC, the potential executive escalation trigger. Subtracting the printed local labels 03:20 and 02:00 without accounting for their different offsets would not measure the elapsed response interval. No earlier containment event, partial containment accepted as full, or backdated correction exists in this authoritative A record.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 873, "end_character": 1667, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T03`

> ## [T03]
> 
> Commander approval PA-A1 was granted at 00:25 UTC for an external credential dependency blocking A containment from 00:30 through 01:00 UTC. Commander approval PA-A2 was granted at 01:05 UTC for an external routing dependency blocking A containment from 01:10 through 01:50 UTC. Each approval preceded its pause beginning, identified the dependency, and was effective for the stated interval. The pauses are nonoverlapping and both lie entirely between detection and authoritative containment. Their raw durations are thirty and forty minutes. Both approvals expressly remain subject to the combined cap in the applicable playbook revision. They do not waive, restart, or pause any escalation or acknowledgement clock.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1686, "end_character": 2414, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

- [input/sources/notification-register.md](input/sources/notification-register.md) — `N03`

> ## [N03]
> 
> The shift handover at 01:30 UTC repeats that approved containment pauses affect only the containment metric and are capped under the applicable revision. The outgoing operator wrote an informal calculation using seventy excluded minutes, then marked it provisional pending the revision check. That provisional number appears in a working column, not an approved policy amendment. The handover also notes that the notification console defaults to sorting by queue time, so exported rows must be read with their field names. This presentation detail explains how a report could mistake 00:08 for delivery without establishing that such a mistake is a valid interpretation.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1536, "end_character": 2216, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "bd983f6678e1509ba7b890bfc8662a6a08ad071f1bb1cde800416784867c4050", "artifact_directory": "extraction/D00007/attempt-8jbmjlgm"}`.

### Rules

- Valid advance commander approval and eligible overlap are necessary but do not waive R04 combined cap; revision 2 cap 45 applies to the total, not each interval independently.

### Assumptions

- Apply only the supplied synthetic playbook and its expressly authoritative event records for A/B/C during October 26-28, 2030. Exact minutes and numerical offsets are literal; no external timezone convention is assumed.
- Material native-source text was inspected against original PDF pages or DOCX XML; independent datetime calculations are retained in arithmetic-check.md. This is source-to-model transcription, not live operational authentication.

### Reasoning

- 1. Approvals at 00:25 and 01:05 precede starts 00:30 and 01:10; documented external dependencies and interval endpoints satisfy approval/overlap requirements.
- 2. Durations 30 and 40 are disjoint and both within detection-to-containment, giving 70 raw approved minutes.
- 3. R04 still limits combined exclusion to 45. The report's approval-validity premise is true but its full-deduction conclusion is false; N03 calls the uncapped 70 calculation provisional.

### Limits

- No conclusion invalidates the pause approvals themselves or permits subtracting the cap from unrelated clocks.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim06` in module `Audit` (refutes): `Audit.pauseConditions = true ∧ Audit.rawPauseA = 70 ∧ Audit.excludedA = 45 ∧ Audit.excludedA < Audit.rawPauseA`.
  [Model](models/Audit.lean) · [Executed check](checks/Target022.lean) · [Actual proof log](logs/target-022.log)

### Recommendation

Distinguish 70 approved minutes from 45 deductible minutes.

## C07-07

### Exact report claim

`input/report.md#C07-07`

> **C07-07.** A's response clock begins at 03:00 UTC because its detection occurred during MA-27 maintenance. Sources: R03, R07, M01, M02, T01.

### Verification question

Does A P1 security classification allow MA-27 maintenance to defer its response-clock start from accepted detection 00:00 to 03:00 UTC?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0008`

> Priority P1 requires acknowledgement within fifteen elapsed minutes after qualifying detection and containment within ninety active-response minutes after that detection. Priority P2 requires acknowledgement within thirty elapsed minutes after its effective response-clock start, with the maintenance deferral defined in M02 as the only applicable modification. The P1 acknowledgement clock is never paused or deferred. For a P1 containment clock, approved containment pauses may exclude elapsed time under R04. A pause does not alter the detection timestamp, acknowledgement clock, or escalation clock. No SLA in this dossier treats an unapproved pause request as an approved interruption, and no pause can exclude time before its approved beginning or after actual containment.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[8]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0016`

> An expressly scoped maintenance window may defer the effective P2 acknowledgement-clock start as stated in M02. Priority P1 overrides that deferral. A maintenance window is not itself a containment-pause approval, and its duration cannot be added to an approved external-dependency pause. Where maintenance and a qualifying incident overlap, the analyst must first identify the incident's priority and the maintenance operation's authorized scope. A general statement that maintenance was underway somewhere in the service is insufficient. Unless the relevant clause says otherwise, a window beginning is included and its ending is excluded when deciding whether a detection occurred inside the window. The end timestamp is nevertheless the start of a deferred clock.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[16]", "paragraph_index_in_story": 16, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

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
Coordinates: `{"kind": "pdf", "page": 2, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0002.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00005.pdf", "original_sha256": "33a2eb21bd3e2d3bc1bc3ee643f5694f958f4d55570d1067685bf2a9a9f5d730", "artifact_directory": "extraction/D00005/attempt-pv6z1bf3"}`.

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
Coordinates: `{"kind": "pdf", "page": 3, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0003.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00005.pdf", "original_sha256": "33a2eb21bd3e2d3bc1bc3ee643f5694f958f4d55570d1067685bf2a9a9f5d730", "artifact_directory": "extraction/D00005/attempt-pv6z1bf3"}`.

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
Coordinates: `{"kind": "pdf", "page": 6, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0006.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00005.pdf", "original_sha256": "33a2eb21bd3e2d3bc1bc3ee643f5694f958f4d55570d1067685bf2a9a9f5d730", "artifact_directory": "extraction/D00005/attempt-pv6z1bf3"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

### Rules

- R07 gives P1 precedence over maintenance deferral. M01 covers named P2 indexing alarms only; M02 defers only a matching P2 acknowledgement clock.

### Assumptions

- Apply only the supplied synthetic playbook and its expressly authoritative event records for A/B/C during October 26-28, 2030. Exact minutes and numerical offsets are literal; no external timezone convention is assumed.
- Material native-source text was inspected against original PDF pages or DOCX XML; independent datetime calculations are retained in arithmetic-check.md. This is source-to-model transcription, not live operational authentication.

### Reasoning

- 1. A detection lies temporally within MA-27 [00:00,03:00), but T01 identifies a P1 security incident, not its named expected P2 indexing operation.
- 2. Thus both the priority and operational-scope requirements for deferral fail. Shared infrastructure alone is insufficient.
- 3. A acknowledgement and containment clocks retain actual detection 00:00; only separately valid containment exclusions affect the latter metric. The asserted 03:00 clock start is refuted.

### Limits

- This does not deny the maintenance work or its possible scoped P2 effects; it denies transferring that exception to A.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim07` in module `Audit` (refutes): `Audit.aEffectiveStart = 0 ∧ Audit.aEffectiveStart ≠ 180`.
  [Model](models/Audit.lean) · [Executed check](checks/Target023.lean) · [Actual proof log](logs/target-023.log)

### Recommendation

Use A accepted detection 00:00 and preserve MA-27 scope restrictions.

## C07-08

### Exact report claim

`input/report.md#C07-08`

> **C07-08.** B's delivered acknowledgement at 03:45 UTC was timely under the authorized maintenance deferral. Sources: R03, M02, M03, M04, T04, F03.

### Verification question

Did B delivered acknowledgement 03:45 satisfy its inclusive 30-minute allowance after the authorized MB-27 deferral?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0004`

> North Channel Observatory operates a synthetic coastal data service. This playbook governs incidents A, B, and C from October 26 through October 28, 2030. A qualifying detection is the first incident classification accepted by the incident coordinator, not an untriaged sensor signal, an email draft, a queue entry, or an invoice from a monitoring provider. Acknowledgement is a delivered human acknowledgement identifying the incident and taking responsibility for response. Containment is an authoritative confirmation that the specified incident path has been isolated; planning an isolation or signing a checklist without completing the isolation is not containment. The source files distinguish authoritative event records from attributed witness claims. The playbook contains no rule making every signed statement an infallible world fact.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0008`

> Priority P1 requires acknowledgement within fifteen elapsed minutes after qualifying detection and containment within ninety active-response minutes after that detection. Priority P2 requires acknowledgement within thirty elapsed minutes after its effective response-clock start, with the maintenance deferral defined in M02 as the only applicable modification. The P1 acknowledgement clock is never paused or deferred. For a P1 containment clock, approved containment pauses may exclude elapsed time under R04. A pause does not alter the detection timestamp, acknowledgement clock, or escalation clock. No SLA in this dossier treats an unapproved pause request as an approved interruption, and no pause can exclude time before its approved beginning or after actual containment.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[8]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0016`

> An expressly scoped maintenance window may defer the effective P2 acknowledgement-clock start as stated in M02. Priority P1 overrides that deferral. A maintenance window is not itself a containment-pause approval, and its duration cannot be added to an approved external-dependency pause. Where maintenance and a qualifying incident overlap, the analyst must first identify the incident's priority and the maintenance operation's authorized scope. A general statement that maintenance was underway somewhere in the service is insufficient. Unless the relevant clause says otherwise, a window beginning is included and its ending is excluded when deciding whether a detection occurred inside the window. The end timestamp is nevertheless the start of a deferred clock.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[16]", "paragraph_index_in_story": 16, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

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
Coordinates: `{"kind": "pdf", "page": 3, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0003.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00005.pdf", "original_sha256": "33a2eb21bd3e2d3bc1bc3ee643f5694f958f4d55570d1067685bf2a9a9f5d730", "artifact_directory": "extraction/D00005/attempt-pv6z1bf3"}`.

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
Coordinates: `{"kind": "pdf", "page": 4, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0004.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00005.pdf", "original_sha256": "33a2eb21bd3e2d3bc1bc3ee643f5694f958f4d55570d1067685bf2a9a9f5d730", "artifact_directory": "extraction/D00005/attempt-pv6z1bf3"}`.

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
Coordinates: `{"kind": "pdf", "page": 5, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0005.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00005.pdf", "original_sha256": "33a2eb21bd3e2d3bc1bc3ee643f5694f958f4d55570d1067685bf2a9a9f5d730", "artifact_directory": "extraction/D00005/attempt-pv6z1bf3"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T04`

> ## [T04]
> 
> Incident B's accepted qualifying detection is 2030-10-27 04:10 +01:00, or 03:10 UTC. Its P2 classification and M-B operation identifier match MB-27. A delivered human acknowledgement identifying B and taking responsibility occurred at 2030-10-27 04:45 +01:00, or 03:45 UTC. No containment pause is claimed for B, and there is no P1 classification or changed maintenance scope in the supplied record. The raw elapsed interval from detection to acknowledgement is thirty-five minutes. The effective P2 acknowledgement interval must nevertheless be determined using the authorized maintenance exception, rather than treating raw elapsed time as the only possible response metric.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2433, "end_character": 3119, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

- [input/sources/review-correspondence.md](input/sources/review-correspondence.md) — `F03`

> ## [F03]
> 
> For B, the review note retains 03:10 UTC as actual qualifying detection but uses 03:20 UTC, the authorized MB-27 window end, as the effective acknowledgement-clock start. Delivered acknowledgement at 03:45 UTC is twenty-five minutes after that start, within the thirty-minute allowance. The note explains that a thirty-five-minute raw detection-to-acknowledgement interval is not inherently a failure when an express scoped deferral applies. The same note explicitly rejects applying any maintenance deferral to A because A is priority P1. It does not claim that the existence of planned work alone establishes any other incident's compliance.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1518, "end_character": 2171, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "2c1cfb5fe6479718615cf4b6445b281ef66b534d4d017c05b46addbf4d27544a", "artifact_directory": "extraction/D00009/attempt-lohr3nkf"}`.

### Rules

- M02 defers the clock for a matching P2 detection inside the half-open authorized window to that window's end; allowance 30 then runs inclusively.

### Assumptions

- Apply only the supplied synthetic playbook and its expressly authoritative event records for A/B/C during October 26-28, 2030. Exact minutes and numerical offsets are literal; no external timezone convention is assumed.
- Material native-source text was inspected against original PDF pages or DOCX XML; independent datetime calculations are retained in arithmetic-check.md. This is source-to-model transcription, not live operational authentication.

### Reasoning

- 1. T04/M03 identify B as P2 operationM-B, with actual accepted detection 03:10 inside MB-27 [02:50,03:20).
- 2. Effective acknowledgement start is 03:20, while actual detection remains 03:10. The delivered responsibility-taking acknowledgement is 03:45.
- 3. The effective interval is 25 minutes, within 30; operator earlier contact is not substituted for the actual acknowledgement.

### Limits

- The exception changes one acknowledgement metric, not B existence/detection or any P1 duty.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim08` in module `Audit` (supports): `(170 : Int) ≤ Audit.bDetection ∧ Audit.bDetection < 200 ∧ Audit.bEffectiveStart = 200 ∧ Audit.bAcknowledgement - Audit.bEffectiveStart = 25 ∧ Audit.bAcknowledgement ≤ Audit.bEffectiveStart + 30`.
  [Model](models/Audit.lean) · [Executed check](checks/Target024.lean) · [Actual proof log](logs/target-024.log)

### Recommendation

Retain the result with actual detection 03:10, effective start 03:20 and deadline 03:50 stated separately.

## C07-09

### Exact report claim

`input/report.md#C07-09`

> **C07-09.** B violated its thirty-minute acknowledgement allowance because thirty-five minutes elapsed after its original detection. Sources: R03, M02, M03, T04, F03.

### Verification question

Does the true 35-minute raw B detection-to-acknowledgement interval establish a 30-minute allowance violation when MB-27 deferral applies?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0008`

> Priority P1 requires acknowledgement within fifteen elapsed minutes after qualifying detection and containment within ninety active-response minutes after that detection. Priority P2 requires acknowledgement within thirty elapsed minutes after its effective response-clock start, with the maintenance deferral defined in M02 as the only applicable modification. The P1 acknowledgement clock is never paused or deferred. For a P1 containment clock, approved containment pauses may exclude elapsed time under R04. A pause does not alter the detection timestamp, acknowledgement clock, or escalation clock. No SLA in this dossier treats an unapproved pause request as an approved interruption, and no pause can exclude time before its approved beginning or after actual containment.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[8]", "paragraph_index_in_story": 8, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

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
Coordinates: `{"kind": "pdf", "page": 3, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0003.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00005.pdf", "original_sha256": "33a2eb21bd3e2d3bc1bc3ee643f5694f958f4d55570d1067685bf2a9a9f5d730", "artifact_directory": "extraction/D00005/attempt-pv6z1bf3"}`.

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
Coordinates: `{"kind": "pdf", "page": 4, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0004.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00005.pdf", "original_sha256": "33a2eb21bd3e2d3bc1bc3ee643f5694f958f4d55570d1067685bf2a9a9f5d730", "artifact_directory": "extraction/D00005/attempt-pv6z1bf3"}`.

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
Coordinates: `{"kind": "pdf", "page": 5, "page_width_points": 612.0, "page_height_points": 792.0, "coordinate_unit": "PDF points; origin at top-left", "text_reconstruction": "Words in Poppler line order, joined by one space; lines joined by newline.", "bbox_artifact": "pdf-page-0005.bbox.xhtml", "total_pages": 7, "original": "input/originals/D00005.pdf", "original_sha256": "33a2eb21bd3e2d3bc1bc3ee643f5694f958f4d55570d1067685bf2a9a9f5d730", "artifact_directory": "extraction/D00005/attempt-pv6z1bf3"}`.

Extraction uncertainty: PDF word coordinates and text are converter outputs; visual reading order, tables, and typography require source inspection.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T04`

> ## [T04]
> 
> Incident B's accepted qualifying detection is 2030-10-27 04:10 +01:00, or 03:10 UTC. Its P2 classification and M-B operation identifier match MB-27. A delivered human acknowledgement identifying B and taking responsibility occurred at 2030-10-27 04:45 +01:00, or 03:45 UTC. No containment pause is claimed for B, and there is no P1 classification or changed maintenance scope in the supplied record. The raw elapsed interval from detection to acknowledgement is thirty-five minutes. The effective P2 acknowledgement interval must nevertheless be determined using the authorized maintenance exception, rather than treating raw elapsed time as the only possible response metric.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2433, "end_character": 3119, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

- [input/sources/review-correspondence.md](input/sources/review-correspondence.md) — `F03`

> ## [F03]
> 
> For B, the review note retains 03:10 UTC as actual qualifying detection but uses 03:20 UTC, the authorized MB-27 window end, as the effective acknowledgement-clock start. Delivered acknowledgement at 03:45 UTC is twenty-five minutes after that start, within the thirty-minute allowance. The note explains that a thirty-five-minute raw detection-to-acknowledgement interval is not inherently a failure when an express scoped deferral applies. The same note explicitly rejects applying any maintenance deferral to A because A is priority P1. It does not claim that the existence of planned work alone establishes any other incident's compliance.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1518, "end_character": 2171, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "2c1cfb5fe6479718615cf4b6445b281ef66b534d4d017c05b46addbf4d27544a", "artifact_directory": "extraction/D00009/attempt-lohr3nkf"}`.

### Rules

- The applicable P2 allowance runs from the authorized effective start, not necessarily actual detection.

### Assumptions

- Apply only the supplied synthetic playbook and its expressly authoritative event records for A/B/C during October 26-28, 2030. Exact minutes and numerical offsets are literal; no external timezone convention is assumed.
- Material native-source text was inspected against original PDF pages or DOCX XML; independent datetime calculations are retained in arithmetic-check.md. This is source-to-model transcription, not live operational authentication.

### Reasoning

- 1. Raw 03:10-to 03:45 elapsed time is 35 minutes; that numerical premise is true.
- 2. The matching P2 maintenance rule shifts effective start to 03:20, yielding 25 minutes and a 03:50 deadline.
- 3. Actual 03:45 acknowledgement is timely, so the claimed violation is refuted because it applies the wrong clock.

### Limits

- A raw interval exceeding 30 is not automatically late in this explicitly scoped exception; no general maintenance exemption follows.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim09` in module `Audit` (refutes): `Audit.bAcknowledgement - Audit.bDetection = 35 ∧ Audit.bAcknowledgement ≤ Audit.bEffectiveStart + 30`.
  [Model](models/Audit.lean) · [Executed check](checks/Target025.lean) · [Actual proof log](logs/target-025.log)

### Recommendation

Replace violation with timely acknowledgement under the authorized 25-minute effective interval.

## C07-10

### Exact report claim

`input/report.md#C07-10`

> **C07-10.** A's technical-lead notification met the ten-minute deadline because it was queued at 00:08 UTC. Sources: R05, N01.

### Verification question

Did queueing A technical-lead notice at 00:08 satisfy the delivered-notification duty by 00:10?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0012`

> The escalation procedure contains three distinct duties for a P1 incident. The technical lead must receive a notification no later than ten elapsed minutes after qualifying detection. The incident commander must receive a notification no later than twenty elapsed minutes after qualifying detection. If the incident remains uncontained sixty elapsed minutes after detection, an executive duty officer must receive a notification no later than fifteen minutes after that trigger, giving a latest time of detection plus seventy-five minutes. All escalation clocks use ordinary elapsed UTC time without containment-pause exclusions. Queue submission, draft completion, attempted dialing, and successful delivery are different events. A notification satisfies the duty only on confirmed delivery to the required role, not merely when queued.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[12]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/notification-register.md](input/sources/notification-register.md) — `N01`

> ## [N01]
> 
> The notification register is complete for A's technical-lead, incident-commander, and executive-duty-officer notifications from 00:00 through 02:30 UTC on October 27. It separately records queue and delivered timestamps. Technical-lead notification TL-A was queued at 00:08 UTC and delivered to the required technical lead at 00:11 UTC. A receipt token confirms delivery. No earlier delivered notification to that role occurred. An automated display highlights the queue timestamp in green because queueing succeeded; that color is not a representation that the playbook's delivered-notification deadline was satisfied. The recipient role and incident identifier are unambiguous.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 159, "end_character": 848, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "bd983f6678e1509ba7b890bfc8662a6a08ad071f1bb1cde800416784867c4050", "artifact_directory": "extraction/D00007/attempt-8jbmjlgm"}`.

- [input/sources/notification-register.md](input/sources/notification-register.md) — `N04`

> ## [N04]
> 
> The register covers notifications to the three specified roles, not all internal chat messages or conversations. The playbook duties concern delivered role-specific notifications, so unrelated informal awareness does not satisfy them. The register's explicit statements that no earlier deliveries occurred support bounded absence reasoning for those exact duties and interval. They do not imply that no person knew of the incident, that no containment work occurred, or that no customer communication was sent. The handover records that the executive message arrived before A's authoritative containment, consistent with the incident remaining active after the escalation trigger.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2235, "end_character": 2925, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "bd983f6678e1509ba7b890bfc8662a6a08ad071f1bb1cde800416784867c4050", "artifact_directory": "extraction/D00007/attempt-8jbmjlgm"}`.

- [input/sources/notification-register.md](input/sources/notification-register.md) — `N03`

> ## [N03]
> 
> The shift handover at 01:30 UTC repeats that approved containment pauses affect only the containment metric and are capped under the applicable revision. The outgoing operator wrote an informal calculation using seventy excluded minutes, then marked it provisional pending the revision check. That provisional number appears in a working column, not an approved policy amendment. The handover also notes that the notification console defaults to sorting by queue time, so exported rows must be read with their field names. This presentation detail explains how a report could mistake 00:08 for delivery without establishing that such a mistake is a valid interpretation.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1536, "end_character": 2216, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "bd983f6678e1509ba7b890bfc8662a6a08ad071f1bb1cde800416784867c4050", "artifact_directory": "extraction/D00007/attempt-8jbmjlgm"}`.

### Rules

- R05 counts confirmed delivery to the required role; queue submission is a different event. N01 covers all such deliveries and explicitly excludes any earlier one.

### Assumptions

- Apply only the supplied synthetic playbook and its expressly authoritative event records for A/B/C during October 26-28, 2030. Exact minutes and numerical offsets are literal; no external timezone convention is assumed.
- Material native-source text was inspected against original PDF pages or DOCX XML; independent datetime calculations are retained in arithmetic-check.md. This is source-to-model transcription, not live operational authentication.

### Reasoning

- 1. N01 records queue 00:08 but actual technical-lead delivery 00:11 with a receipt token.
- 2. The required deadline is accepted detection 00:00 plus 10 minutes, inclusive. Actual first delivery is one minute late.
- 3. Queue success or its green console display cannot substitute for delivery, so the report's timely conclusion is refuted while its queue timestamp remains true.

### Limits

- The bounded no-earlier-delivery statement concerns this role/incident and covered interval, not all informal awareness.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim10` in module `Audit` (refutes): `Audit.technical.queued ≤ Audit.aDetection + 10 ∧ ¬ (Audit.technical.delivered ≤ Audit.aDetection + 10) ∧ Audit.technical.delivered = 11`.
  [Model](models/Audit.lean) · [Executed check](checks/Target026.lean) · [Actual proof log](logs/target-026.log)

### Recommendation

Record technical-lead delivery one minute late and label queue and delivery fields separately.

## C07-11

### Exact report claim

`input/report.md#C07-11`

> **C07-11.** A's commander notification met its twenty-minute deadline after subtracting the approved containment pauses. Sources: R04, R05, N02.

### Verification question

Can containment-pause deductions make A commander notification at 00:22 timely against the 20-minute escalation deadline?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0010`

> A valid containment pause must identify an external dependency blocking containment, be approved in writing by the incident commander before the pause begins, and specify a beginning and end. Approved pauses exclude only their actual overlap with the detection-to-containment interval. Nonoverlapping approved intervals can be added; overlapping intervals would be unioned so a minute is never excluded twice. Revision 1 caps the total excluded time at sixty minutes for an incident. Revision 2 caps the total at forty-five minutes. The cap applies to the combined excluded duration, not independently to each approved pause. Active-response time equals total elapsed detection-to-containment time minus the smaller of the approved overlapping duration and the applicable combined cap. Approval of a longer pause interval does not waive that cap.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[10]", "paragraph_index_in_story": 10, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0012`

> The escalation procedure contains three distinct duties for a P1 incident. The technical lead must receive a notification no later than ten elapsed minutes after qualifying detection. The incident commander must receive a notification no later than twenty elapsed minutes after qualifying detection. If the incident remains uncontained sixty elapsed minutes after detection, an executive duty officer must receive a notification no later than fifteen minutes after that trigger, giving a latest time of detection plus seventy-five minutes. All escalation clocks use ordinary elapsed UTC time without containment-pause exclusions. Queue submission, draft completion, attempted dialing, and successful delivery are different events. A notification satisfies the duty only on confirmed delivery to the required role, not merely when queued.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[12]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/notification-register.md](input/sources/notification-register.md) — `N02`

> ## [N02]
> 
> Incident-commander notification IC-A was queued at 00:18 UTC and delivered to the incident commander at 00:22 UTC. No earlier delivered commander notification occurred in the complete coverage. The later fact that the commander validly approved containment pauses does not retroactively move the first notification earlier. Executive-duty-officer notification EX-A was delivered at 01:12 UTC. Its message explicitly states that the incident remained uncontained at the sixty-minute mark and requests executive coordination. This message is not a reclassification, a containment event, or an approval to disregard previous escalation delays.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 867, "end_character": 1517, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "bd983f6678e1509ba7b890bfc8662a6a08ad071f1bb1cde800416784867c4050", "artifact_directory": "extraction/D00007/attempt-8jbmjlgm"}`.

- [input/sources/notification-register.md](input/sources/notification-register.md) — `N03`

> ## [N03]
> 
> The shift handover at 01:30 UTC repeats that approved containment pauses affect only the containment metric and are capped under the applicable revision. The outgoing operator wrote an informal calculation using seventy excluded minutes, then marked it provisional pending the revision check. That provisional number appears in a working column, not an approved policy amendment. The handover also notes that the notification console defaults to sorting by queue time, so exported rows must be read with their field names. This presentation detail explains how a report could mistake 00:08 for delivery without establishing that such a mistake is a valid interpretation.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1536, "end_character": 2216, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "bd983f6678e1509ba7b890bfc8662a6a08ad071f1bb1cde800416784867c4050", "artifact_directory": "extraction/D00007/attempt-8jbmjlgm"}`.

- [input/sources/notification-register.md](input/sources/notification-register.md) — `N04`

> ## [N04]
> 
> The register covers notifications to the three specified roles, not all internal chat messages or conversations. The playbook duties concern delivered role-specific notifications, so unrelated informal awareness does not satisfy them. The register's explicit statements that no earlier deliveries occurred support bounded absence reasoning for those exact duties and interval. They do not imply that no person knew of the incident, that no containment work occurred, or that no customer communication was sent. The handover records that the executive message arrived before A's authoritative containment, consistent with the incident remaining active after the escalation trigger.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2235, "end_character": 2925, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "bd983f6678e1509ba7b890bfc8662a6a08ad071f1bb1cde800416784867c4050", "artifact_directory": "extraction/D00007/attempt-8jbmjlgm"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T03`

> ## [T03]
> 
> Commander approval PA-A1 was granted at 00:25 UTC for an external credential dependency blocking A containment from 00:30 through 01:00 UTC. Commander approval PA-A2 was granted at 01:05 UTC for an external routing dependency blocking A containment from 01:10 through 01:50 UTC. Each approval preceded its pause beginning, identified the dependency, and was effective for the stated interval. The pauses are nonoverlapping and both lie entirely between detection and authoritative containment. Their raw durations are thirty and forty minutes. Both approvals expressly remain subject to the combined cap in the applicable playbook revision. They do not waive, restart, or pause any escalation or acknowledgement clock.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1686, "end_character": 2414, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

### Rules

- R05 escalation clocks use ordinary elapsed UTC time without containment-pause exclusions. R04 pauses affect containment only.

### Assumptions

- Apply only the supplied synthetic playbook and its expressly authoritative event records for A/B/C during October 26-28, 2030. Exact minutes and numerical offsets are literal; no external timezone convention is assumed.
- Material native-source text was inspected against original PDF pages or DOCX XML; independent datetime calculations are retained in arithmetic-check.md. This is source-to-model transcription, not live operational authentication.

### Reasoning

- 1. N02 records first commander delivery 00:22 and explicitly excludes earlier delivery; the inclusive deadline is 00:20.
- 2. No containment pause deduction applies to this clock. In any case the first approved pause begins 00:30, after this delivery.
- 3. The notification is two minutes late. Later commander approvals do not retroactively alter its delivery, and the report's subtraction rule is inapplicable.

### Limits

- This does not invalidate the commander's separate later pause approvals or determine other recipients' timeliness.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim11` in module `Audit` (refutes): `Audit.commander.delivered = 22 ∧ ¬ (Audit.commander.delivered ≤ Audit.aDetection + 20)`.
  [Model](models/Audit.lean) · [Executed check](checks/Target027.lean) · [Actual proof log](logs/target-027.log)

### Recommendation

Record the two-minute commander escalation delay without containment exclusions.

## C07-12

### Exact report claim

`input/report.md#C07-12`

> **C07-12.** A's executive-duty-officer notification was timely once the sixty-minute uncontained trigger occurred. Sources: R05, T02, N02.

### Verification question

Did the sixty-minute uncontained trigger actually occur for A, and was executive notification delivered within the following inclusive 15 minutes?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0012`

> The escalation procedure contains three distinct duties for a P1 incident. The technical lead must receive a notification no later than ten elapsed minutes after qualifying detection. The incident commander must receive a notification no later than twenty elapsed minutes after qualifying detection. If the incident remains uncontained sixty elapsed minutes after detection, an executive duty officer must receive a notification no later than fifteen minutes after that trigger, giving a latest time of detection plus seventy-five minutes. All escalation clocks use ordinary elapsed UTC time without containment-pause exclusions. Queue submission, draft completion, attempted dialing, and successful delivery are different events. A notification satisfies the duty only on confirmed delivery to the required role, not merely when queued.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[12]", "paragraph_index_in_story": 12, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T02`

> ## [T02]
> 
> Authoritative containment confirmation for A occurred at 2030-10-27 03:20 +01:00, equivalent to 02:20 UTC. The containment team then confirmed the affected security path was isolated. A remained uncontained continuously from qualifying detection until this confirmation; this positive incident-state record is independent of whether the monitoring sensors were continuously available. The source therefore establishes that A was still uncontained at 01:00 UTC, the potential executive escalation trigger. Subtracting the printed local labels 03:20 and 02:00 without accounting for their different offsets would not measure the elapsed response interval. No earlier containment event, partial containment accepted as full, or backdated correction exists in this authoritative A record.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 873, "end_character": 1667, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

- [input/sources/notification-register.md](input/sources/notification-register.md) — `N02`

> ## [N02]
> 
> Incident-commander notification IC-A was queued at 00:18 UTC and delivered to the incident commander at 00:22 UTC. No earlier delivered commander notification occurred in the complete coverage. The later fact that the commander validly approved containment pauses does not retroactively move the first notification earlier. Executive-duty-officer notification EX-A was delivered at 01:12 UTC. Its message explicitly states that the incident remained uncontained at the sixty-minute mark and requests executive coordination. This message is not a reclassification, a containment event, or an approval to disregard previous escalation delays.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 867, "end_character": 1517, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "bd983f6678e1509ba7b890bfc8662a6a08ad071f1bb1cde800416784867c4050", "artifact_directory": "extraction/D00007/attempt-8jbmjlgm"}`.

- [input/sources/notification-register.md](input/sources/notification-register.md) — `N04`

> ## [N04]
> 
> The register covers notifications to the three specified roles, not all internal chat messages or conversations. The playbook duties concern delivered role-specific notifications, so unrelated informal awareness does not satisfy them. The register's explicit statements that no earlier deliveries occurred support bounded absence reasoning for those exact duties and interval. They do not imply that no person knew of the incident, that no containment work occurred, or that no customer communication was sent. The handover records that the executive message arrived before A's authoritative containment, consistent with the incident remaining active after the escalation trigger.

Original: [input/originals/D00007.md](input/originals/D00007.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2235, "end_character": 2925, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00007.md", "original_sha256": "bd983f6678e1509ba7b890bfc8662a6a08ad071f1bb1cde800416784867c4050", "artifact_directory": "extraction/D00007/attempt-8jbmjlgm"}`.

- [input/sources/review-correspondence.md](input/sources/review-correspondence.md) — `F04`

> ## [F04]
> 
> The review coordinator lists the three A escalation results separately for discussion. The technical-lead delivery happened eleven minutes after detection; the commander delivery happened twenty-two minutes after detection. The executive trigger occurred at 01:00 UTC because A remained uncontained, and the executive delivery followed twelve minutes later at 01:12. The coordinator asks for corrective process discussion but makes no claim that one timely stage cancels another stage's delay. The underlying register is the evidence of events; this correspondence is a calculation and interpretation aid, not an authoritative alteration of delivered timestamps.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2190, "end_character": 2862, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "2c1cfb5fe6479718615cf4b6445b281ef66b534d4d017c05b46addbf4d27544a", "artifact_directory": "extraction/D00009/attempt-lohr3nkf"}`.

### Rules

- R05 triggers executive duty only if still uncontained 60 elapsed minutes after detection, then requires delivery within 15 minutes. No pause deductions apply.

### Assumptions

- Apply only the supplied synthetic playbook and its expressly authoritative event records for A/B/C during October 26-28, 2030. Exact minutes and numerical offsets are literal; no external timezone convention is assumed.
- Material native-source text was inspected against original PDF pages or DOCX XML; independent datetime calculations are retained in arithmetic-check.md. This is source-to-model transcription, not live operational authentication.

### Reasoning

- 1. T02 positively and authoritatively records A continuously uncontained until 02:20, so it was uncontained at 01:00; this is not an inference from missing telemetry.
- 2. The executive trigger is 01:00 and deadline 01:15. N02 gives actual executive-role delivery 01:12.
- 3. Twelve minutes after a real trigger is timely. This separate success neither erases nor inherits earlier technical/commander lateness.

### Limits

- This proves the particular triggered duty and delivery comparison, not blanket compliance of all escalations.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim12` in module `Audit` (supports): `Audit.aUncontainedAt (Audit.aDetection + 60) = true ∧ Audit.executiveDelivery - (Audit.aDetection + 60) = 12 ∧ Audit.executiveDelivery ≤ Audit.aDetection + 75`.
  [Model](models/Audit.lean) · [Executed check](checks/Target028.lean) · [Actual proof log](logs/target-028.log)

### Recommendation

Retain as a separate timely executive stage with the positive uncontained-state evidence.

## C07-13

### Exact report claim

`input/report.md#C07-13`

> **C07-13.** Revision 1 governs A because its raw warning arrived before the revision 2 boundary. Sources: R01, R06, T01.

### Verification question

Does A raw warning before midnight select revision 1 despite coordinator-accepted qualifying detection exactly at the revision 2 boundary?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0004`

> North Channel Observatory operates a synthetic coastal data service. This playbook governs incidents A, B, and C from October 26 through October 28, 2030. A qualifying detection is the first incident classification accepted by the incident coordinator, not an untriaged sensor signal, an email draft, a queue entry, or an invoice from a monitoring provider. Acknowledgement is a delivered human acknowledgement identifying the incident and taking responsibility for response. Containment is an authoritative confirmation that the specified incident path has been isolated; planning an isolation or signing a checklist without completing the isolation is not containment. The source files distinguish authoritative event records from attributed witness claims. The playbook contains no rule making every signed statement an infallible world fact.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0014`

> Revision 2 takes effect at 2030-10-27 00:00 UTC for incidents whose qualifying detection occurs at or after that instant. Incidents detected earlier retain revision 1 throughout their response, even when containment, handover, or evidence collection occurs after the boundary. A raw warning signal before midnight does not grandfather an incident whose accepted qualifying detection occurs at midnight. The revision change affects the containment-pause cap only; the acknowledgement, maintenance, and escalation rules reproduced here apply to both versions. A dashboard displaying the currently published revision does not amend an incident's detection event or its retained version. Exact receipt at the boundary belongs to revision 2.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[14]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T01`

> ## [T01]
> 
> Incident A generated a raw untriaged warning at 2030-10-27 01:30 +02:00, equivalent to 2030-10-26 23:30 UTC. The coordinator accepted its qualifying detection as priority P1 at 2030-10-27 02:00 +02:00, equivalent to 00:00 UTC on October 27. The accepted classification concerns a security incident in the south archive cluster, not an expected indexing warning under MA-27. A delivered human acknowledgement accepting responsibility occurred at 2030-10-27 02:12 +02:00, equivalent to 00:12 UTC. These are separate event fields, all exact to the minute. The raw warning is not itself the qualifying detection, and the classification record has not been corrected or withdrawn.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 169, "end_character": 854, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

### Rules

- R01 distinguishes raw signal from accepted detection; R06 explicitly rejects grandfathering from an earlier raw warning and includes the boundary in revision 2.

### Assumptions

- Apply only the supplied synthetic playbook and its expressly authoritative event records for A/B/C during October 26-28, 2030. Exact minutes and numerical offsets are literal; no external timezone convention is assumed.
- Material native-source text was inspected against original PDF pages or DOCX XML; independent datetime calculations are retained in arithmetic-check.md. This is source-to-model transcription, not live operational authentication.

### Reasoning

- 1. The raw warning converts to October 26 23:30, before transition, but remains untriaged.
- 2. The accepted qualifying detection is October 27 00:00 and is unchanged.
- 3. Revision 2 governs A. The report substitutes the wrong event for version selection and is refuted, despite correctly noting the earlier warning.

### Limits

- The revision change affects the pause cap only; acknowledgement, maintenance and escalation rules here apply to both versions.

### Result

Semantic state: **refuted**; argument status: **invalid_inference**; formal status: **refuted**.

### Formal evidence

- `Audit.claim13` in module `Audit` (refutes): `Audit.aRaw = -30 ∧ Audit.aDetection = 0 ∧ Audit.revision Audit.aDetection = 2 ∧ Audit.revision Audit.aDetection ≠ 1`.
  [Model](models/Audit.lean) · [Executed check](checks/Target029.lean) · [Actual proof log](logs/target-029.log)

### Recommendation

Use revision 2 for A and preserve separate warning/detection fields.

## C07-14

### Exact report claim

`input/report.md#C07-14`

> **C07-14.** C retains revision 1 even though its later response activities occurred on October 27. Sources: R06, T05.

### Verification question

Does C accepted detection before the boundary retain revision 1 despite later response activity on October 27?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0006`

> All elapsed durations must be calculated on a single UTC timeline. Each timestamp bearing a numerical timezone offset is interpreted literally using that offset: UTC equals the printed local clock time minus the printed offset. The offset is fixed for that event even when nearby events display another offset. No outside daylight-saving calendar is needed or permitted to replace an explicit offset. The October dates were selected to make careless subtraction of local clock labels tempting. Exact minute timestamps denote exact instants, rather than intervals of possible occurrence. A deadline expressed as within N minutes is inclusive, so an action at exactly the deadline is timely. All clock changes, windows, and pauses relevant to the assessed incidents are explicitly recorded in the supplied sources.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[6]", "paragraph_index_in_story": 6, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0014`

> Revision 2 takes effect at 2030-10-27 00:00 UTC for incidents whose qualifying detection occurs at or after that instant. Incidents detected earlier retain revision 1 throughout their response, even when containment, handover, or evidence collection occurs after the boundary. A raw warning signal before midnight does not grandfather an incident whose accepted qualifying detection occurs at midnight. The revision change affects the containment-pause cap only; the acknowledgement, maintenance, and escalation rules reproduced here apply to both versions. A dashboard displaying the currently published revision does not amend an incident's detection event or its retained version. Exact receipt at the boundary belongs to revision 2.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[14]", "paragraph_index_in_story": 14, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T05`

> ## [T05]
> 
> Incident C was accepted as P1 at 2030-10-27 01:50 +02:00, equivalent to 2030-10-26 23:50 UTC. Later actions occurred on October 27, but the qualifying detection timestamp is authoritative and unchanged. The accepted register deliberately contains no authoritative containment timestamp for C. Instead, the shift packet contains the two signed, inconsistent containment attestations reproduced in the scanned attestation source. This is unlike A, whose containment is authoritatively recorded in T02. No rule permits borrowing A's authoritative-record status for C or treating C's latest available testimony as automatically controlling because its document appears later in the transferred packet.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 3138, "end_character": 3845, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

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
Coordinates: `{"kind": "ocr", "page": 5, "origin": {"format": "pdf", "page": 5, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0005-raster.png", "tsv_artifact": "pdf-page-0005.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.75592513265306, "minimum_word_confidence": 62.61581, "confidence_threshold": 85.0, "low_confidence_words": 1, "word_count": 98, "original": "input/originals/D00003.pdf", "original_sha256": "0ac923e297094632a74ab4ab8cf60709989191d75b35d5d29d2820007cbde0d0", "artifact_directory": "extraction/D00003/attempt-mh9id4cw", "source_anchor": "pdf-page-0005", "root_source_anchor": "pdf-page-0005", "reviewer": "audit_01m", "reason": "Actually inspected original preserved scan page 5 with view_image. Corrected visible A04 marker and, where present, 05:00 isolation / 05:30 signature times misrecognized with @ characters; page-3 quote punctuation restored to visible straight quote. All material statement polarity and scope compared to the original; original OCR retained.", "reviewed_at": "2026-11-04T15:07:15.940033+00:00", "transcription_snapshot": "input/manual-transcriptions/D00003/88f7763d0ec10b10cfbc90b82a9857fe4d8abdb2e5ba545eef5bc49b897e29bd.txt", "transcription_file_sha256": "b2aeda24d7bc3b6ac37312eb77e12f59e768ce78a5a939bc3e8ec815f01c113f", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

### Rules

- R06 retains the revision selected by qualifying detection throughout response; later activity does not reselect it.

### Assumptions

- Apply only the supplied synthetic playbook and its expressly authoritative event records for A/B/C during October 26-28, 2030. Exact minutes and numerical offsets are literal; no external timezone convention is assumed.
- Material native-source text was inspected against original PDF pages or DOCX XML; independent datetime calculations are retained in arithmetic-check.md. This is source-to-model transcription, not live operational authentication.

### Reasoning

- 1. T05 accepted detection 01:50 +02:00 converts to October 26 23:50 UTC, ten minutes before boundary.
- 2. R06 therefore retains revision 1 for C even after midnight activities. A04 confirms neither signatory disputes that accepted detection.
- 3. Unresolved C containment time does not undermine this independent, authoritative detection/version result.

### Limits

- No C containment time, containment-SLA compliance or actual isolation event is thereby established.

### Result

Semantic state: **supported**; argument status: **sufficient**; formal status: **proved**.

### Formal evidence

- `Audit.claim14` in module `Audit` (supports): `Audit.cDetection = -10 ∧ Audit.revision Audit.cDetection = 1`.
  [Model](models/Audit.lean) · [Executed check](checks/Target030.lean) · [Actual proof log](logs/target-030.log)

### Recommendation

Retain revision 1 and keep the containment dispute separate.

## C07-15

### Exact report claim

`input/report.md#C07-15`

> **C07-15.** Incident C was fully isolated at exactly 05:00 UTC on October 27. Sources: T05, A01, A02, A03, A04.

### Verification question

What supports and denies complete C isolation exactly October 27 05:00 UTC, given authentic but unreconciled attestations and no authoritative C containment record?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0004`

> North Channel Observatory operates a synthetic coastal data service. This playbook governs incidents A, B, and C from October 26 through October 28, 2030. A qualifying detection is the first incident classification accepted by the incident coordinator, not an untriaged sensor signal, an email draft, a queue entry, or an invoice from a monitoring provider. Acknowledgement is a delivered human acknowledgement identifying the incident and taking responsibility for response. Containment is an authoritative confirmation that the specified incident path has been isolated; planning an isolation or signing a checklist without completing the isolation is not containment. The source files distinguish authoritative event records from attributed witness claims. The playbook contains no rule making every signed statement an infallible world fact.

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[4]", "paragraph_index_in_story": 4, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0018`

> Monitoring evidence has its own completeness boundaries. A certified monitoring extract can establish that specified sensors reported no listed alarms during the certified observation periods. It does not prove that no underlying exfiltration occurred unless a supplied rule makes the sensors complete for that event type and period. Missing telemetry cannot by itself prove either successful exfiltration or its absence. Signed conflicting statements about containment remain attributed evidence unless authoritative records or an adopted resolution settle the point. The playbook defines timeliness, roles, pauses, and windows but supplies no objective criterion for judging that an overall response was professionally managed, emotionally reassuring, or exemplary. Those broader judgments require additional standards and argument.
> 

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[18]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T05`

> ## [T05]
> 
> Incident C was accepted as P1 at 2030-10-27 01:50 +02:00, equivalent to 2030-10-26 23:50 UTC. Later actions occurred on October 27, but the qualifying detection timestamp is authoritative and unchanged. The accepted register deliberately contains no authoritative containment timestamp for C. Instead, the shift packet contains the two signed, inconsistent containment attestations reproduced in the scanned attestation source. This is unlike A, whose containment is authoritatively recorded in T02. No rule permits borrowing A's authoritative-record status for C or treating C's latest available testimony as automatically controlling because its document appears later in the transferred packet.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 3138, "end_character": 3845, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

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
Coordinates: `{"kind": "ocr", "page": 2, "origin": {"format": "pdf", "page": 2, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0002-raster.png", "tsv_artifact": "pdf-page-0002.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.01026661363636, "minimum_word_confidence": 63.257053, "confidence_threshold": 85.0, "low_confidence_words": 3, "word_count": 88, "original": "input/originals/D00003.pdf", "original_sha256": "0ac923e297094632a74ab4ab8cf60709989191d75b35d5d29d2820007cbde0d0", "artifact_directory": "extraction/D00003/attempt-mh9id4cw", "source_anchor": "pdf-page-0002", "root_source_anchor": "pdf-page-0002", "reviewer": "audit_01m", "reason": "Actually inspected original preserved scan page 2 with view_image. Corrected visible A01 marker and, where present, 05:00 isolation / 05:30 signature times misrecognized with @ characters; page-3 quote punctuation restored to visible straight quote. All material statement polarity and scope compared to the original; original OCR retained.", "reviewed_at": "2026-11-04T15:07:15.637716+00:00", "transcription_snapshot": "input/manual-transcriptions/D00003/f2c73ff169fa72a87f8a86ce29319fba80b81b376e3a4b6229800b78686ff70a.txt", "transcription_file_sha256": "d32b06511c768dc992b931b57c025274bfb0e77499964cb3cba12fd384ffe69e", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

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
Coordinates: `{"kind": "ocr", "page": 3, "origin": {"format": "pdf", "page": 3, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0003-raster.png", "tsv_artifact": "pdf-page-0003.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 93.65185876344086, "minimum_word_confidence": 49.620968, "confidence_threshold": 85.0, "low_confidence_words": 5, "word_count": 93, "original": "input/originals/D00003.pdf", "original_sha256": "0ac923e297094632a74ab4ab8cf60709989191d75b35d5d29d2820007cbde0d0", "artifact_directory": "extraction/D00003/attempt-mh9id4cw", "source_anchor": "pdf-page-0003", "root_source_anchor": "pdf-page-0003", "reviewer": "audit_01m", "reason": "Actually inspected original preserved scan page 3 with view_image. Corrected visible A02 marker and, where present, 05:00 isolation / 05:30 signature times misrecognized with @ characters; page-3 quote punctuation restored to visible straight quote. All material statement polarity and scope compared to the original; original OCR retained.", "reviewed_at": "2026-11-04T15:07:15.738294+00:00", "transcription_snapshot": "input/manual-transcriptions/D00003/74d057c1ffd7a573949b5264432bbf95d0ac166f21a1a683072c9f16d09c7d65.txt", "transcription_file_sha256": "e8660b78d23b6e7da20e9a1f81677c45deb3de9df025e357af9b99f0cc41ca1f", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

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
Coordinates: `{"kind": "ocr", "page": 4, "origin": {"format": "pdf", "page": 4, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0004-raster.png", "tsv_artifact": "pdf-page-0004.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.55065942857144, "minimum_word_confidence": 71.014496, "confidence_threshold": 85.0, "low_confidence_words": 1, "word_count": 98, "original": "input/originals/D00003.pdf", "original_sha256": "0ac923e297094632a74ab4ab8cf60709989191d75b35d5d29d2820007cbde0d0", "artifact_directory": "extraction/D00003/attempt-mh9id4cw", "source_anchor": "pdf-page-0004", "root_source_anchor": "pdf-page-0004", "reviewer": "audit_01m", "reason": "Actually inspected original preserved scan page 4 with view_image. Corrected visible A03 marker and, where present, 05:00 isolation / 05:30 signature times misrecognized with @ characters; page-3 quote punctuation restored to visible straight quote. All material statement polarity and scope compared to the original; original OCR retained.", "reviewed_at": "2026-11-04T15:07:15.838428+00:00", "transcription_snapshot": "input/manual-transcriptions/D00003/653097fa4c7e85eb684393bda9dd0a3959fec379a0851eefccc17e303dbea4da.txt", "transcription_file_sha256": "3cd2223066b90c450f6320f6735834f622d46f3d4bb084bc3f84f9078d16b979", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

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
Coordinates: `{"kind": "ocr", "page": 5, "origin": {"format": "pdf", "page": 5, "raster_dpi": 200, "pixel_to_pdf_points": "coordinate * 72 / 200", "total_pages": 5}, "coordinate_unit": "raster pixels; origin at top-left; bbox = left, top, width, height", "image_artifact": "pdf-page-0005-raster.png", "tsv_artifact": "pdf-page-0005.tsv", "ocr_language": "eng", "ocr_page_segmentation_mode": 3, "mean_word_confidence": 95.75592513265306, "minimum_word_confidence": 62.61581, "confidence_threshold": 85.0, "low_confidence_words": 1, "word_count": 98, "original": "input/originals/D00003.pdf", "original_sha256": "0ac923e297094632a74ab4ab8cf60709989191d75b35d5d29d2820007cbde0d0", "artifact_directory": "extraction/D00003/attempt-mh9id4cw", "source_anchor": "pdf-page-0005", "root_source_anchor": "pdf-page-0005", "reviewer": "audit_01m", "reason": "Actually inspected original preserved scan page 5 with view_image. Corrected visible A04 marker and, where present, 05:00 isolation / 05:30 signature times misrecognized with @ characters; page-3 quote punctuation restored to visible straight quote. All material statement polarity and scope compared to the original; original OCR retained.", "reviewed_at": "2026-11-04T15:07:15.940033+00:00", "transcription_snapshot": "input/manual-transcriptions/D00003/88f7763d0ec10b10cfbc90b82a9857fe4d8abdb2e5ba545eef5bc49b897e29bd.txt", "transcription_file_sha256": "b2aeda24d7bc3b6ac37312eb77e12f59e768ce78a5a939bc3e8ec815f01c113f", "transcription_normalization": "UTF-8 BOM and outer whitespace removed from indexed quotation only; original authored bytes retained.", "coordinate_interpretation": "Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording."}`.

Extraction uncertainty: Manual transcription is a reviewer-attributed interpretation of the original source, not machine-certified textual fidelity or source authenticity. Inherited coordinates identify the original passage; inherited OCR words and confidence describe the uncorrected extraction, not the manually transcribed wording.

### Rules

- Signed testimony is not an infallible world fact. No source priority, later-signature override, role-based infallibility or authoritative resolution is supplied.

### Assumptions

- Original scan pages were actually viewed and controlled reviewed-0001 transcriptions preserve source hashes and original OCR.
- Authenticity establishes attribution only; T05 authoritative detection must not be mistaken for authoritative containment.

### Reasoning

- 1. A01 visually verified text has Elise Stone affirm full isolation at exactly 05:00 with no path live afterward.
- 2. A02 visually verified text has Pavel Hart explicitly deny full isolation at 05:00 and assert a C path remained live until 05:20. The same incident, UTC instant and complete-isolation proposition are at issue.
- 3. A03 stipulates authentic signatures but no retraction, adjudication or priority rule. T05 deliberately provides no authoritative containment timestamp; A04 merely acknowledges receipt of statements.
- 4. The evidence state is both supporting and denying testimony. The auxiliary theorem records attributions without proving contradictory world facts or selecting a historical isolation time.

### Limits

- Visual correction of OCR resolves the transcribed 05:00/05:30 characters, not the witness dispute. Authenticity is stipulated within the dossier, not independently cryptographically tested by this audit.

### Result

Semantic state: **both**; argument status: **disputed**; formal status: **auxiliary**.

### Formal evidence

- `Audit.claim15Conflict` in module `Audit` (auxiliary): `Audit.eliseAffirmsIsolation0500 = true ∧ Audit.pavelDeniesIsolation0500 = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target031.lean) · [Actual proof log](logs/target-031.log)

### Recommendation

Display both attributed accounts and seek an authoritative trace or adopted resolution; do not settle the event by signing order.

## C07-16

### Exact report claim

`input/report.md#C07-16`

> **C07-16.** No exfiltration occurred during A's 01:10–01:40 UTC monitoring gap. Sources: R08, G01, G02, G03, G04.

### Verification question

Does the supplied evidence rule out all A exfiltration during the missing 01:10-01:40 UTC monitoring period?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0018`

> Monitoring evidence has its own completeness boundaries. A certified monitoring extract can establish that specified sensors reported no listed alarms during the certified observation periods. It does not prove that no underlying exfiltration occurred unless a supplied rule makes the sensors complete for that event type and period. Missing telemetry cannot by itself prove either successful exfiltration or its absence. Signed conflicting statements about containment remain attributed evidence unless authoritative records or an adopted resolution settle the point. The playbook defines timeliness, roles, pauses, and windows but supplies no objective criterion for judging that an overall response was professionally managed, emotionally reassuring, or exemplary. Those broader judgments require additional standards and argument.
> 

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[18]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/monitoring-coverage.md](input/sources/monitoring-coverage.md) — `G01`

> ## [G01]
> 
> The monitoring package certifies collection from A's egress sensors during [00:00, 01:10) UTC and [01:40, 02:30] UTC on October 27. It explicitly does not cover [01:10, 01:40) UTC because the collector's storage service was unavailable. Boundary brackets describe the certified collection intervals, not assumptions about attacker behavior. The retained records show no listed exfiltration alarms during the certified periods. There are no retained samples from the thirty-minute gap. The package contains no reconstruction of those missing samples, no redundant complete sensor stream, and no statement that silence from the collector proves absence of network activity.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 166, "end_character": 847, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "1ce800a888704355cbfe2e1478cc7111aa84695beb40b6bf419bfba6d11b2c1c", "artifact_directory": "extraction/D00006/attempt-csn4b669"}`.

- [input/sources/monitoring-coverage.md](input/sources/monitoring-coverage.md) — `G02`

> ## [G02]
> 
> The sensor design note says the listed alarms detect particular signatures and traffic thresholds. It expressly declines to assert that every possible exfiltration would produce an alarm, even when collection is functioning. Thus the observation “no listed alarms in retained samples” is narrower than “no exfiltration occurred.” During the collection gap, even the narrower alarm observation lacks samples. The operational incident state in T02 remains independently documented: A was uncontained until 02:20 UTC. Being uncontained does not itself prove that data were taken, and becoming contained does not establish a complete retrospective history of earlier data movement.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 866, "end_character": 1553, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "1ce800a888704355cbfe2e1478cc7111aa84695beb40b6bf419bfba6d11b2c1c", "artifact_directory": "extraction/D00006/attempt-csn4b669"}`.

- [input/sources/monitoring-coverage.md](input/sources/monitoring-coverage.md) — `G03`

> ## [G03]
> 
> A storage support ticket attributes the telemetry outage to a collector volume reaching its configured capacity. The ticket concerns the observation system and does not identify who, if anyone, initiated exfiltration. It does not allege that a malicious actor caused the storage condition, and no source connects the volume event to a successful transfer of protected records. A missing observational period can justify requesting additional evidence or marking a support gap. It cannot supply the absent positive premise for a report that asserts exfiltration, nor the absent complete negative evidence for a report that rules exfiltration out.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1572, "end_character": 2227, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "1ce800a888704355cbfe2e1478cc7111aa84695beb40b6bf419bfba6d11b2c1c", "artifact_directory": "extraction/D00006/attempt-csn4b669"}`.

- [input/sources/monitoring-coverage.md](input/sources/monitoring-coverage.md) — `G04`

> ## [G04]
> 
> The security liaison requested a packet capture from a separate network appliance for the gap. The response says that archive was not transferred with this dossier. The package inventory is complete for supplied monitoring files only. It says nothing about whether another team possesses a usable capture, whether the capture would reveal an event, or whether collection was complete at that appliance. No report may fill this uncertainty by inventing a favorable or unfavorable result. A future authenticated capture might narrow the uncertainty, but the present finite evidence neither confirms nor denies exfiltration during the missing period.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2246, "end_character": 2903, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "1ce800a888704355cbfe2e1478cc7111aa84695beb40b6bf419bfba6d11b2c1c", "artifact_directory": "extraction/D00006/attempt-csn4b669"}`.

- [input/sources/incident-timeline.md](input/sources/incident-timeline.md) — `T02`

> ## [T02]
> 
> Authoritative containment confirmation for A occurred at 2030-10-27 03:20 +01:00, equivalent to 02:20 UTC. The containment team then confirmed the affected security path was isolated. A remained uncontained continuously from qualifying detection until this confirmation; this positive incident-state record is independent of whether the monitoring sensors were continuously available. The source therefore establishes that A was still uncontained at 01:00 UTC, the potential executive escalation trigger. Subtracting the printed local labels 03:20 and 02:00 without accounting for their different offsets would not measure the elapsed response interval. No earlier containment event, partial containment accepted as full, or backdated correction exists in this authoritative A record.

Original: [input/originals/D00004.md](input/originals/D00004.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 873, "end_character": 1667, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00004.md", "original_sha256": "3c7f7f4ffa277289e9f0968044dcee0bb3ada7d8c2c09aa68e34ecae77fa730e", "artifact_directory": "extraction/D00004/attempt-xm33ric1"}`.

### Rules

- Missing samples cannot establish event absence; even retained no-listed-alarm observations are not complete detection of every possible exfiltration under G02.

### Assumptions

- No missing sample is assigned a fabricated value; hypothetical event alternatives preserve all supplied observation limitations.

### Reasoning

- 1. G01 certifies collection outside the gap and explicitly supplies no samples within [01:10,01:40).
- 2. G02 limits sensor signatures/thresholds; G04 supplies no redundant complete capture. Thus there is neither complete negative evidence for the gap nor a rule connecting alarm silence to no exfiltration.
- 3. T02 uncontained state is independently established but does not prove either event polarity. The storage ticket describes collector capacity, not attacker behavior.
- 4. Compatible hypothetical histories share missing gap samples and no listed retained alarms while differing on exfiltration. The negative report claim is insufficiently supported, not refuted by invented positive evidence.

### Limits

- The model demonstrates non-entailment only. Actual exfiltration remains unknown, including from ordinary absence of alarms in functioning but incomplete sensors.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **auxiliary**.

### Formal evidence

- `Audit.gapAlternatives` in module `Audit` (auxiliary): `Audit.possibleNoExfiltration.gapSamplesAvailable = false ∧ Audit.possibleExfiltration.gapSamplesAvailable = false ∧ Audit.possibleNoExfiltration.retainedListedAlarms = false ∧ Audit.possibleExfiltration.retainedListedAlarms = false ∧ Audit.possibleNoExfiltration.exfiltrationDuringGap = false ∧ Audit.possibleExfiltration.exfiltrationDuringGap = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target032.lean) · [Actual proof log](logs/target-032.log)

### Recommendation

Report the monitoring support gap and obtain a properly scoped capture or other event-complete evidence before asserting no exfiltration.

## C07-17

### Exact report claim

`input/report.md#C07-17`

> **C07-17.** Exfiltration occurred during A's 01:10–01:40 UTC monitoring gap because the collector has no records for that period. Sources: R08, G01, G02, G03, G04.

### Verification question

Does absence of collector records establish positive exfiltration during A's 01:10-01:40 gap?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0018`

> Monitoring evidence has its own completeness boundaries. A certified monitoring extract can establish that specified sensors reported no listed alarms during the certified observation periods. It does not prove that no underlying exfiltration occurred unless a supplied rule makes the sensors complete for that event type and period. Missing telemetry cannot by itself prove either successful exfiltration or its absence. Signed conflicting statements about containment remain attributed evidence unless authoritative records or an adopted resolution settle the point. The playbook defines timeliness, roles, pauses, and windows but supplies no objective criterion for judging that an overall response was professionally managed, emotionally reassuring, or exemplary. Those broader judgments require additional standards and argument.
> 

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[18]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/monitoring-coverage.md](input/sources/monitoring-coverage.md) — `G01`

> ## [G01]
> 
> The monitoring package certifies collection from A's egress sensors during [00:00, 01:10) UTC and [01:40, 02:30] UTC on October 27. It explicitly does not cover [01:10, 01:40) UTC because the collector's storage service was unavailable. Boundary brackets describe the certified collection intervals, not assumptions about attacker behavior. The retained records show no listed exfiltration alarms during the certified periods. There are no retained samples from the thirty-minute gap. The package contains no reconstruction of those missing samples, no redundant complete sensor stream, and no statement that silence from the collector proves absence of network activity.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 6, "end_line": 8, "start_character": 166, "end_character": 847, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "1ce800a888704355cbfe2e1478cc7111aa84695beb40b6bf419bfba6d11b2c1c", "artifact_directory": "extraction/D00006/attempt-csn4b669"}`.

- [input/sources/monitoring-coverage.md](input/sources/monitoring-coverage.md) — `G02`

> ## [G02]
> 
> The sensor design note says the listed alarms detect particular signatures and traffic thresholds. It expressly declines to assert that every possible exfiltration would produce an alarm, even when collection is functioning. Thus the observation “no listed alarms in retained samples” is narrower than “no exfiltration occurred.” During the collection gap, even the narrower alarm observation lacks samples. The operational incident state in T02 remains independently documented: A was uncontained until 02:20 UTC. Being uncontained does not itself prove that data were taken, and becoming contained does not establish a complete retrospective history of earlier data movement.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 11, "end_line": 13, "start_character": 866, "end_character": 1553, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "1ce800a888704355cbfe2e1478cc7111aa84695beb40b6bf419bfba6d11b2c1c", "artifact_directory": "extraction/D00006/attempt-csn4b669"}`.

- [input/sources/monitoring-coverage.md](input/sources/monitoring-coverage.md) — `G03`

> ## [G03]
> 
> A storage support ticket attributes the telemetry outage to a collector volume reaching its configured capacity. The ticket concerns the observation system and does not identify who, if anyone, initiated exfiltration. It does not allege that a malicious actor caused the storage condition, and no source connects the volume event to a successful transfer of protected records. A missing observational period can justify requesting additional evidence or marking a support gap. It cannot supply the absent positive premise for a report that asserts exfiltration, nor the absent complete negative evidence for a report that rules exfiltration out.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 16, "end_line": 18, "start_character": 1572, "end_character": 2227, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "1ce800a888704355cbfe2e1478cc7111aa84695beb40b6bf419bfba6d11b2c1c", "artifact_directory": "extraction/D00006/attempt-csn4b669"}`.

- [input/sources/monitoring-coverage.md](input/sources/monitoring-coverage.md) — `G04`

> ## [G04]
> 
> The security liaison requested a packet capture from a separate network appliance for the gap. The response says that archive was not transferred with this dossier. The package inventory is complete for supplied monitoring files only. It says nothing about whether another team possesses a usable capture, whether the capture would reveal an event, or whether collection was complete at that appliance. No report may fill this uncertainty by inventing a favorable or unfavorable result. A future authenticated capture might narrow the uncertainty, but the present finite evidence neither confirms nor denies exfiltration during the missing period.

Original: [input/originals/D00006.md](input/originals/D00006.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 21, "end_line": 23, "start_character": 2246, "end_character": 2903, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00006.md", "original_sha256": "1ce800a888704355cbfe2e1478cc7111aa84695beb40b6bf419bfba6d11b2c1c", "artifact_directory": "extraction/D00006/attempt-csn4b669"}`.

### Rules

- Unavailable observation is not positive event evidence; G03 expressly attributes storage outage without identifying malicious action or successful protected-data transfer.

### Assumptions

- The hypothetical alternatives are explanatory countermodels, not claims about unseen capture contents or actual attacker behavior.

### Reasoning

- 1. The collector lacks samples because its storage service was unavailable; the support ticket gives configured capacity as the observation-system cause.
- 2. No supplied source connects that outage to an attacker or an exfiltration event. The absent separate capture is also unknown, not an incriminating result.
- 3. A no-exfiltration history is compatible with the same gap, as is an exfiltration history. The auxiliary witness therefore blocks the claimed causal/evidential inference while leaving actual occurrence undetermined.

### Limits

- This does not prove that exfiltration did not occur. It identifies the missing positive event premise rather than substituting a favorable invented history.

### Result

Semantic state: **undetermined**; argument status: **insufficient_support**; formal status: **auxiliary**.

### Formal evidence

- `Audit.gapAlternatives` in module `Audit` (auxiliary): `Audit.possibleNoExfiltration.gapSamplesAvailable = false ∧ Audit.possibleExfiltration.gapSamplesAvailable = false ∧ Audit.possibleNoExfiltration.retainedListedAlarms = false ∧ Audit.possibleExfiltration.retainedListedAlarms = false ∧ Audit.possibleNoExfiltration.exfiltrationDuringGap = false ∧ Audit.possibleExfiltration.exfiltrationDuringGap = true`.
  [Model](models/Audit.lean) · [Executed check](checks/Target032.lean) · [Actual proof log](logs/target-032.log)

### Recommendation

Remove the positive event conclusion unless separate transfer evidence is obtained; retain the collection failure as its own documented finding.

## C07-18

### Exact report claim

`input/report.md#C07-18`

> **C07-18.** The overall incident response was professionally managed and reassuring. Sources: R08, F05.

### Verification question

Do the playbook or supplied opinions define criteria sufficient to judge the overall response professionally managed and reassuring?

### Source evidence

- [input/sources/response-playbook.docx.md](input/sources/response-playbook.docx.md) — `docx-p-0018`

> Monitoring evidence has its own completeness boundaries. A certified monitoring extract can establish that specified sensors reported no listed alarms during the certified observation periods. It does not prove that no underlying exfiltration occurred unless a supplied rule makes the sensors complete for that event type and period. Missing telemetry cannot by itself prove either successful exfiltration or its absence. Signed conflicting statements about containment remain attributed evidence unless authoritative records or an adopted resolution settle the point. The playbook defines timeliness, roles, pauses, and windows but supplies no objective criterion for judging that an overall response was professionally managed, emotionally reassuring, or exemplary. Those broader judgments require additional standards and argument.
> 

Original: [input/originals/D00008.docx](input/originals/D00008.docx); extraction: docx-xml.
Coordinates: `{"kind": "docx", "member": "word/document.xml", "xml_path": "/w:document/w:body/w:p[18]", "paragraph_index_in_story": 18, "story": "document", "raw_xml_artifact": "docx-xml/document.xml", "footnote_ids": [], "endnote_ids": [], "comment_ids": [], "original": "input/originals/D00008.docx", "original_sha256": "ea807f0cc7df7f30f991cbe5c74617b2537d0156212ca5f973925be279f78eae", "artifact_directory": "extraction/D00008/attempt-9rjd_lb_"}`.

- [input/sources/review-correspondence.md](input/sources/review-correspondence.md) — `F05`

> ## [F05]
> 
> A manager describes the response in an email as “professionally managed and reassuring.” A shift employee calls the early escalation delays avoidable. Neither provides an agreed scoring rubric, weighting of outcomes, or definition of professional management. Those views can be included as attributed opinions, but the objective timeliness record alone does not determine every broader evaluative adjective. The correspondence also distinguishes the unresolved C containment disagreement from the separate missing A monitoring period. One is conflicting testimony about a specific event; the other is unavailable observational evidence, and neither should be compressed into a claim that every supplied incident fact is unreliable.

Original: [input/originals/D00009.md](input/originals/D00009.md); extraction: utf8.
Coordinates: `{"kind": "text", "start_line": 26, "end_line": 28, "start_character": 2881, "end_character": 3622, "coordinate_unit": "Unicode code points after UTF-8 BOM removal", "original": "input/originals/D00009.md", "original_sha256": "2c1cfb5fe6479718615cf4b6445b281ef66b534d4d017c05b46addbf4d27544a", "artifact_directory": "extraction/D00009/attempt-lohr3nkf"}`.

### Rules

- R08 provides no operational standard for professional management or emotional reassurance. Objective timing metrics do not define every broader evaluative adjective.

### Assumptions

- No external incident-response standard or unstated utility/comfort metric is imported.

### Reasoning

- 1. F05 supplies a manager opinion using the report adjectives and another employee opinion about avoidable delays, but neither an agreed rubric or outcome weighting.
- 2. The documented mixed timeliness record, C testimony conflict and A monitoring gap address distinct objective/evidential questions rather than a complete management-quality criterion.
- 3. Both qualitative components remain nonformal under this mandate. No formal proof of either favorable evaluation or its negation is justified.

### Limits

- This is undefined evaluation, not a finding that the response was unprofessional or unreassuring. Attributed opinions can be preserved as opinions.

### Result

Semantic state: **not_applicable**; argument status: **nonformal**; formal status: **not_attempted**.

### Formal evidence

No formal proof requested for this finding.

### Recommendation

Attribute the manager's wording or supply an agreed rubric and argument before assessing the qualitative conclusion.
