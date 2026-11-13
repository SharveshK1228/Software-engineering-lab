# Static analysis findings

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Dynamic `eval` | Security (high) | 43-51 | Evaluated user supplied text as Python, allowing arbitrary code execution. | Replaced with parsing of two integer operands and a supported `<=` comparison. |
| SQL string interpolation | Security (high) | 27-30 | Programme names were interpolated into SQL, enabling SQL injection and breaking on quotes. | Used parameterized SQL and validated input. |
| Hard-coded studio password | Security (medium) | Original 6 | A credential was stored in source and was unused. | Removed the secret from the program. |
| Incorrect aggregate on delete | Correctness (medium) | Original 57-58 | Removing a slot did not update `booked_minutes`, so later results could be wrong. | Removed the stale aggregate and query the database for current schedule data. |
| Missing input validation | Reliability | 25-36 | Invalid hours, durations, or empty names could enter the schedule. | Added explicit validation and clear `ValueError`s. |
| Naming and formatting | Style | throughout | Non-PEP 8 names, one-line conditional and missing module/function docs. | Renamed helpers and applied consistent formatting and docstrings. |
