# Independent timestamp and arithmetic verification

Python datetime.fromisoformat interpreted the supplied literal numeric offsets; astimezone(UTC) and subtraction from October 27 00:00 UTC were executed independently of Lean. No geographic timezone or external daylight-saving schedule was used.

| Supplied timestamp | UTC | Minute offset |
| --- | --- | ---: |
| 2030-10-27T01:30+02:00 | 2030-10-26T23:30:00+00:00 | -30 |
| 2030-10-27T02:00+02:00 | 2030-10-27T00:00:00+00:00 | 0 |
| 2030-10-27T02:12+02:00 | 2030-10-27T00:12:00+00:00 | 12 |
| 2030-10-27T03:20+01:00 | 2030-10-27T02:20:00+00:00 | 140 |
| 2030-10-27T04:10+01:00 | 2030-10-27T03:10:00+00:00 | 190 |
| 2030-10-27T04:45+01:00 | 2030-10-27T03:45:00+00:00 | 225 |
| 2030-10-27T01:50+02:00 | 2030-10-26T23:50:00+00:00 | -10 |

A elapsed: 140 - 0 = 140 minutes.
Pause intervals: 60-30 = 30 and 110-70 = 40; disjoint sum 70; revision 2 deduction min(70,45)=45; active 140-45=95.
A acknowledgement: 12-0=12 <=15.
MB-27 interval [170,200); B detection190; deferred start200; delivery225; effective25<=30 while raw35>30.
A notification deliveries: technical11>10; commander22>20; executive trigger60 with containment140>60, delivery72; 72-60=12<=15.
C accepted detection offset -10 selects revision1; A raw warning-30 does not replace qualifying detection0.
