# Independently executed Gregorian conversion check

Python datetime with Gregorian UTC dates; origin 2028-02-20 00:00 UTC.

| Timestamp UTC | Day offset | Minute offset |
| --- | ---: | ---: |
| 2028-02-20T09:00 | 0 | 540 |
| 2028-02-29T23:59 | 9 | 14399 |
| 2028-03-01T00:00 | 10 | 14400 |
| 2028-03-01T08:00 | 10 | 14880 |
| 2028-03-01T08:30 | 10 | 14910 |
| 2028-03-01T08:45 | 10 | 14925 |
| 2028-03-01T17:00 | 10 | 15420 |
| 2028-03-08T17:00 | 17 | 25500 |
| 2028-03-10T17:00 | 19 | 28380 |
| 2028-03-10T17:01 | 19 | 28381 |
| 2028-03-02T10:00 | 11 | 16440 |
| 2028-03-12T16:00 | 21 | 31200 |
| 2028-03-15T00:00 | 24 | 34560 |

2028-02-20 + 10 calendar days, cutoff 17:00 UTC = 2028-03-01T17:00:00+00:00; offset 15420.

2028-02-29 + 10 calendar days, cutoff 17:00 UTC = 2028-03-10T17:00:00+00:00; offset 28380.

2028-03-01 + 7 calendar days, cutoff 17:00 UTC = 2028-03-08T17:00:00+00:00; offset 25500.

Additional independently computed mapping: 2028-03-02T11:00 UTC = 16500 minutes. March 11/12 17:00 values are auxiliary hypothetical due dates, not sourced actual deadlines.

Additional independently computed mapping: 2028-03-11T17:00 UTC = 29820 minutes. March 11/12 17:00 values are auxiliary hypothetical due dates, not sourced actual deadlines.

Additional independently computed mapping: 2028-03-12T17:00 UTC = 31260 minutes. March 11/12 17:00 values are auxiliary hypothetical due dates, not sourced actual deadlines.
