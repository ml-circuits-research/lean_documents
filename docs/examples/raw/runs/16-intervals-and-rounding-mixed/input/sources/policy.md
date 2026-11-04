# Harbor Relay settlement protocol SR-16

[P1] This synthetic protocol governs incident H16 and its November 2026 invoice. All times are integer minute offsets from 09:00 UTC on 2 November 2026. Pause intervals are half-open [start,end); a minute belongs to the interval exactly when start <= minute < end. The gross incident window is [0,180). Count each paused minute once using the union of approved in-scope intervals, clipped to the gross window. An interval of zero length contributes zero. Intervals marked other-case never pause H16.

[P2] The SLA limit is 140 chargeable minutes inclusive. Chargeable time is gross elapsed minutes minus distinct approved in-scope paused minutes. An incident meets the SLA exactly when chargeable time <= 140. For the explicit extension scenario only, restoration occurs at minute 181 and all listed pause intervals and scope flags remain unchanged. No automatic tolerance minute applies.

[P3] Monetary source amounts are signed integer mills: ten mills equal one cent. Round each invoice line separately to integer cents, choosing the nearest cent and resolving an exact half-cent tie away from zero. For a negative credit, round its absolute magnitude under the same rule and restore the negative sign. Sum the signed rounded lines; never round the unrounded invoice aggregate instead. The separate credit note is not an invoice line.

[P4] A historical rebate requires at least three SLA breaches during August through October 2026. An H16 decision in November cannot establish the earlier-quarter breach count. This protocol provides no definition, benchmark, or test for whether compensation is reasonable.
