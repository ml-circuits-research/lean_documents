<a id="docx-p-0001"></a>
[V1-01] SYNTHETIC H-7 SPECIFICATION, REVISION 1. This document concerns the fictional Heliostat H-7 demonstration controller. It is not an actual safety standard and supplies no real-world safety advice. Revision 1 applies to tests executed before 1 June 2033 unless an explicitly approved profile says otherwise. The finite demonstration concerns measured trip delay under stated laboratory conditions. It does not certify lifetime reliability, mechanical protection, network security, or population defect rates. A report should identify the proposition actually tested rather than replace it with an undefined claim that the whole design is safe. The table below defines exact synthetic limits for this bounded exercise.

<a id="docx-p-0002"></a>
[V1-02] HISTORICAL ACCEPTANCE TABLE. The NORMAL temperature interval includes both endpoints. A missing authorized route outside that interval is not a zero threshold and does not imply a physical failure. Three repeated runs must be valid and belong to the same unit and profile. Values copied from another serial number do not complete a missing run. The supply condition belongs to applicability rather than to an independent exemption from other prerequisites.

<a id="docx-table-0001-r0001-c0001-p0001"></a>
Profile

<a id="docx-table-0001-r0001-c0002-p0001"></a>
Environment

<a id="docx-table-0001-r0001-c0003-p0001"></a>
Maximum delay

<a id="docx-table-0001-r0001-c0004-p0001"></a>
Valid runs

<a id="docx-table-0001-r0001-c0005-p0001"></a>
Other conditions

<a id="docx-table-0001-r0002-c0001-p0001"></a>
NORMAL

<a id="docx-table-0001-r0002-c0002-p0001"></a>
10 through 30 degrees Celsius inclusive

<a id="docx-table-0001-r0002-c0003-p0001"></a>
120 milliseconds

<a id="docx-table-0001-r0002-c0004-p0001"></a>
3 per unit

<a id="docx-table-0001-r0002-c0005-p0001"></a>
Both channels measured; 24 volts nominal

<a id="docx-table-0001-r0003-c0001-p0001"></a>
COLD

<a id="docx-table-0001-r0003-c0002-p0001"></a>
Below 10 degrees Celsius

<a id="docx-table-0001-r0003-c0003-p0001"></a>
No authorized criterion in revision 1

<a id="docx-table-0001-r0003-c0004-p0001"></a>
Not specified

<a id="docx-table-0001-r0003-c0005-p0001"></a>
No qualification route supplied

<a id="docx-table-0001-r0004-c0001-p0001"></a>
HOT

<a id="docx-table-0001-r0004-c0002-p0001"></a>
Above 30 degrees Celsius

<a id="docx-table-0001-r0004-c0003-p0001"></a>
No authorized criterion in revision 1

<a id="docx-table-0001-r0004-c0004-p0001"></a>
Not specified

<a id="docx-table-0001-r0004-c0005-p0001"></a>
No qualification route supplied

<a id="docx-p-0023"></a>
[V1-03] IMPLICATION DIRECTION. Three valid NORMAL runs within the applicable limit are sufficient for the narrowly defined delay demonstration. They are not stated necessary for every conceivable alternative assurance method. Full release additionally requires current calibration, both sensor channels measured, closure of required fault injections, and an authorized release signature. Passing a delay subrequirement alone is therefore insufficient for full release. The specification intentionally distinguishes a sufficient route to one predicate from a conjunction of prerequisites for another predicate. An audit must not reverse an implication merely because its converse sounds plausible or because no alternative route is described in this packet.

<a id="docx-p-0024"></a>
[V1-04] DATA HANDLING. A run aborted before acquisition supplies no delay measurement. A blank cell means unavailable evidence unless a signed explanatory note explicitly gives another meaning. It is not zero. An operator may invalidate a trace after discovering synchronization loss; the invalidation accompanies the printed value. Each extraction should retain unit identity, run date, profile, environment, validity, instrument, measured channels, and observed value. Comparing a column of numbers without those fields can apply the wrong revision or count invalid evidence. Missing measurements should be reported as concrete support gaps, not silently replaced by favorable numbers from a neighboring row.

<a id="docx-p-0025"></a>
[V1-05] HISTORICAL L01 RECORD. Unit L01 was tested on 20 May 2033 at 20 degrees Celsius. Its three valid delays were 110, 115, and 118 milliseconds. Both channels were measured using instrument K1, which was current for that date. These observations establish the historical delay demonstration under the 120-millisecond threshold. No fault-injection closure or final release signature for L01 is supplied here. A later tighter rule does not retroactively change the applicable threshold unless an operative transition clause explicitly requires reassessment. Historical acceptance and present authorization should remain separate questions, even when a later report discusses them together.
