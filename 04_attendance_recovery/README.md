# 04. Attendance Recovery Calculator

## Problem statement
Calculate a student's current attendance and determine the minimum number of consecutive classes to attend to reach the required percentage.

## Objectives
Practise arithmetic, conditionals, loops, and input validation.

## Assumptions
Conducted classes must be positive; attended classes must be between zero and conducted classes. The target percentage is between 0 and 100. Future classes are all attended.

## Algorithm
1. Read conducted and attended classes. 2. Validate values. 3. Calculate current attendance. 4. If target is already reached, report zero. 5. Otherwise use a loop to find the smallest future class count that reaches target. 6. Display result.

## Flowchart
```text
Start → Input class counts and target → Validate → Calculate percentage → Target reached? → Yes: 0 classes / No: loop future classes until target reached → Display → End
```

## Pseudocode
```text
INPUT conducted, attended, target\nVALIDATE inputs\ncurrent = attended / conducted * 100\nfuture = 0\nWHILE (attended + future) / (conducted + future) * 100 < target:\n  future = future + 1\nPRINT current, future
```

## Python source code
See `attendance_recovery.py` in this folder. Run it with:

```bash
python attendance_recovery.py
```

## Test cases
| Conducted | Attended | Target | Expected future classes |\n|---:|---:|---:|---:|\n| 20 | 15 | 75 | 0 |\n| 20 | 12 | 75 | 12 |\n| 10 | 5 | 75 | 10 |

## Sample output
Run the program and enter the values from the test cases above. The program prints the calculated result in the terminal. A real output screenshot can be captured after running it in IDLE, VS Code, or a terminal.

## Conclusion
The program applies a loop to find the minimum future attendance needed to meet a percentage target.
