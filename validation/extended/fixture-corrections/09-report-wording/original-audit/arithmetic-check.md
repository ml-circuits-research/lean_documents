# Independent civil-calendar and arithmetic checks

Python datetime subtraction on the supplied civil-date timeline; origin2033-06-01 00:00. No timezone is assumed.

| Timestamp | Minute offset |
| --- | ---: |
| 2033-05-20T00:00 | -17280 |
| 2033-05-20T23:59 | -15841 |
| 2033-06-01T23:59 | 1439 |
| 2033-06-02T09:00 | 1980 |
| 2033-06-03T00:00 | 2880 |
| 2033-06-03T23:59 | 4319 |
| 2033-06-04T18:00 | 5400 |
| 2033-06-05T00:00 | 5760 |
| 2033-06-30T23:59 | 43199 |

L01: values=[110, 115, 118]; maximum=118; all within 120: True; limit-minus-maximum=2.

N01: values=[92, 95, 99]; maximum=99; all within 100: True; limit-minus-maximum=1.

N02: values=[90, 97, 101]; maximum=101; all within 100: False; limit-minus-maximum=-1.

E17: values=[104, 108, 106]; maximum=108; all within 110: True; limit-minus-maximum=2.

C01: values=[142, 145, 149]; maximum=149; all within 150: True; limit-minus-maximum=1.
