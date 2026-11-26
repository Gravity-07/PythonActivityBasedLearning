# 09. Monthly Calendar Generator

## Problem statement
Generate a text calendar for a month using its number of days and the weekday on which the month starts.

## Objectives
Use nested loops, counters, conditional statements, and formatted strings to generate a pattern-like layout.

## Assumptions
The user supplies a valid month name, a day count from 28 to 31, and a starting weekday where Monday is 0 and Sunday is 6. Leap-year validation is outside this exercise.

## Algorithm
1. Read month name, day count, and starting weekday. 2. Validate values. 3. Print weekday headings. 4. Print leading spaces for the starting weekday. 5. Print day numbers, starting a new row after Sunday.

## Flowchart
```text
Start → Input month/days/start weekday → Validate → Print heading → Print leading blanks → Loop day numbers → New week after Sunday → End
```

## Pseudocode
```text
INPUT month, days, start_day\nVALIDATE 28 <= days <= 31 AND 0 <= start_day <= 6\nPRINT weekday headings\nPRINT start_day blank cells\nFOR day from 1 to days:\n  PRINT day in fixed-width cell\n  IF (start_day + day) MOD 7 = 0: PRINT newline\nPRINT newline
```

## Python source code
See `calendar_generator.py` in this folder. Run it with:

```bash
python calendar_generator.py
```

## Test cases
Input: month=April, days=30, starting weekday=2 (Wednesday). Expected: 1 appears under Wednesday and 30 under Thursday.

## Sample output
Run the program and enter the values from the test cases above. The program prints the calculated result in the terminal. A real output screenshot can be captured after running it in IDLE, VS Code, or a terminal.

## Conclusion
The program uses loops and alignment spaces to generate a simple monthly calendar.
