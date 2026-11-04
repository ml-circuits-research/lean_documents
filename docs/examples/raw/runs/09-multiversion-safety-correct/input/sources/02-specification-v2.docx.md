<a id="docx-p-0001"></a>
[V2-01] SYNTHETIC H-7 SPECIFICATION, REVISION 2. Revision 2 takes effect at 00:00 on 1 June 2033 for newly executed tests. It supersedes revision 1 for that prospective scope. Historical tests retain their historical approved rules unless explicitly retested; no retroactive reassessment is required here. Test execution time determines the applicable revision, not report publication time, file modification time, or the order in which an auditor discovers files. Identical serial numbers may appear in different periods because a unit can be retested. Every conclusion must identify the actual event being judged rather than attach a timeless pass or fail label to a serial number.

<a id="docx-p-0002"></a>
[V2-02] CURRENT ACCEPTANCE TABLE. Every endpoint in the stated intervals is inclusive. A valid NORMAL delay of 100 milliseconds satisfies the numeric limit; 101 does not. The COLD route additionally requires a current cold-fixture certificate. There is no supplied HOT route, and no route below zero degrees. A table row cannot be applied without checking the environment and profile. The limits in this synthetic exercise are exact integer comparisons; realistic measurement error models are outside scope. The absence of an error model must not be filled by an invented uncertainty discount or an assumed rounding allowance.

<a id="docx-table-0001-r0001-c0001-p0001"></a>
Profile

<a id="docx-table-0001-r0001-c0002-p0001"></a>
Environment

<a id="docx-table-0001-r0001-c0003-p0001"></a>
Maximum delay

<a id="docx-table-0001-r0001-c0004-p0001"></a>
Valid runs

<a id="docx-table-0001-r0001-c0005-p0001"></a>
Additional conditions

<a id="docx-table-0001-r0002-c0001-p0001"></a>
NORMAL

<a id="docx-table-0001-r0002-c0002-p0001"></a>
10 through 30 degrees Celsius

<a id="docx-table-0001-r0002-c0003-p0001"></a>
100 milliseconds

<a id="docx-table-0001-r0002-c0004-p0001"></a>
3 per unit

<a id="docx-table-0001-r0002-c0005-p0001"></a>
Both channels measured

<a id="docx-table-0001-r0003-c0001-p0001"></a>
COLD

<a id="docx-table-0001-r0003-c0002-p0001"></a>
0 through 9 degrees Celsius

<a id="docx-table-0001-r0003-c0003-p0001"></a>
150 milliseconds

<a id="docx-table-0001-r0003-c0004-p0001"></a>
3 per unit

<a id="docx-table-0001-r0003-c0005-p0001"></a>
Both channels measured and cold-fixture certificate

<a id="docx-table-0001-r0004-c0001-p0001"></a>
HOT

<a id="docx-table-0001-r0004-c0002-p0001"></a>
Above 30 degrees Celsius

<a id="docx-table-0001-r0004-c0003-p0001"></a>
No authorized threshold

<a id="docx-table-0001-r0004-c0004-p0001"></a>
No route

<a id="docx-table-0001-r0004-c0005-p0001"></a>
No qualification supplied

<a id="docx-p-0023"></a>
[V2-03] RELEASE CONJUNCTION. The specified release route requires an applicable delay demonstration, current calibration at every contributing run, both sensor channels measured, closure of the required fault injections, and an authorized release signature. Each conjunct is necessary under this route. Their conjunction is sufficient only within the finite H-7 demonstration scope. A signature does not overwrite an explicit failed run. A favorable channel A result cannot establish an absent channel B result. An explicit recorded failure supplies a counterexample to a claim that all requirements passed; a missing measurement instead leaves a required argument unsupported. These evidentiary situations should not be collapsed into one generic negative verdict.

<a id="docx-p-0024"></a>
[V2-04] INCORPORATED EXCEPTION. Annex X changes the NORMAL delay threshold for one named serial number and a specific time interval. It changes no other requirement. In particular, it does not expand the temperature range, waive channel B measurement, make expired calibration current, close fault injections, or delegate release signing authority. The applicable general rule and exception must be combined before comparing observed delay. A general threshold alone is an incomplete rule set for a unit covered by an exception. Conversely, resemblance to the exempt unit does not extend an exception to other serial numbers or later dates.

<a id="docx-p-0025"></a>
[V2-05] VALIDITY AND TIME. A recorded clock synchronization failure invalidates the affected trace even if its printed delay is small. Repeated runs belong to their named unit and profile. Calibration is current only when the run timestamp is on or before the stated expiry instant. A renewal after a run is not retrospective unless an authorized statement explicitly says it is. The packet contains no such retrospective calibration statement. The analyst must distinguish an absent certificate from a certificate affirmatively showing expiry. Both may prevent an assurance argument, but only the latter supplies direct contrary evidence about calibration at the specific instant.

<a id="docx-p-0026"></a>
[V2-06] REVIEW UNIVERSE. The named units are L01, N01, N02, N03, E17, and C01; X99 is an invalid demonstration trace. These cases do not constitute a random sample of a production population. No statistical inference about all manufactured controllers is supplied. A universal statement about the named valid runs can be refuted by one in-scope explicit run above its applicable threshold. A universal statement about all temperatures requires additional defined criteria and observations. Preserve successful bounded demonstrations while identifying unsupported extensions. Every name, signature, instrument, and event here is synthetic, so no conclusion should be mistaken for certification of a real product.
