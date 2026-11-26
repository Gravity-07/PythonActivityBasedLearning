# 07. Student Marks Matrix Analysis

## Problem statement
Store marks of multiple students across multiple subjects and calculate student totals, averages, subject averages, and the top-performing student.

## Objectives
Use nested lists, nested loops, row-wise and column-wise calculations, and conditional statements.

## Assumptions
Marks are whole numbers from 0 to 100. Every student has marks for the same number of subjects. At least one student and one subject are entered.

## Algorithm
1. Read student and subject counts. 2. Read marks into a nested list. 3. Validate each mark. 4. Calculate each student's total and average. 5. Calculate each subject's average. 6. Identify the student with the highest total. 7. Display report.

## Flowchart
```text
Start → Read dimensions → Input marks matrix → Validate marks → Calculate row totals/averages → Calculate column averages → Find top student → Display → End
```

## Pseudocode
```text
INPUT student_count, subject_count\nmarks = empty nested list\nFOR each student:\n  row = empty list\n  FOR each subject: INPUT mark; validate; append\n  append row to marks\nFOR each row: calculate total and average\nFOR each subject column: calculate average\nFIND index with highest total\nPRINT report
```

## Python source code
See `marks_matrix.py` in this folder. Run it with:

```bash
python marks_matrix.py
```

## Test cases
Example matrix: [[80, 70, 90], [60, 75, 65]]\nExpected totals: 240 and 200. Student averages: 80.00 and 66.67. Subject averages: 70.00, 72.50, 77.50. Top student: Student 1.

## Sample output
Run the program and enter the values from the test cases above. The program prints the calculated result in the terminal. A real output screenshot can be captured after running it in IDLE, VS Code, or a terminal.

## Conclusion
The project demonstrates nested-list storage and both row-wise and column-wise matrix analysis.
