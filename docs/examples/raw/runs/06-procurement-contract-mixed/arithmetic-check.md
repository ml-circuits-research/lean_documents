# Independently executed arithmetic checks

Python datetime date arithmetic in UTC and fractions.Fraction were run separately from the Lean implementation.

| Timestamp UTC | Minute offset from June 1 |
| --- | ---: |
| 2029-05-31T23:59 | -1 |
| 2029-06-01T00:00 | 0 |
| 2029-06-15T17:00 | 21180 |
| 2029-06-15T17:01 | 21181 |
| 2029-06-15T17:10 | 21190 |
| 2029-06-22T09:45 | 30825 |
| 2029-06-22T10:00 | 30840 |
| 2029-06-24T10:00 | 33720 |

June 3 through June 20: date difference 17, inclusive position 18; day 18 lies inside the first-through-thirtieth-date window.
P-13 exact converted euros: 9999999/400; exact ten-thousandths: 249999975; final rounded cents: 2500000.
P-14 exact euros: 12499997/500; exact ten-thousandths: 249999940; final rounded cents: 2499999.
P-11/P-12 normalized cents: 1240000 + 1260000 = 2500000.
E-19 review interval: June 24 10:00 minus June 22 10:00 = 2880 minutes = 48 hours.
