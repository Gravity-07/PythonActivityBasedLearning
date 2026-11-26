# 02. Employee Payroll Calculator

## Problem statement
Compute an employee's gross salary from basic pay, allowances, overtime, and incentives, then calculate deductions and net salary.

## Objectives
Practise variables, arithmetic operators, input, conditionals, and formatted output.

## Assumptions
HRA is 20% of basic pay, DA is 10%, overtime is paid at ₹150 per hour, and incentives are entered directly. Deduction is 8% of gross salary. All inputs must be non-negative.

## Algorithm
1. Read employee details and pay components. 2. Validate numeric inputs. 3. Calculate HRA, DA, overtime pay, and gross salary. 4. Calculate deduction and net salary. 5. Print salary statement.

## Flowchart
```text
Start → Input employee/pay data → Validate → Calculate allowances and overtime → Gross salary → Deduction → Net salary → Print statement → End
```

## Pseudocode
```text
INPUT name, basic, overtime_hours, incentive\nIF any numeric input < 0: PRINT error\nELSE:\n  hra = basic * 0.20\n  da = basic * 0.10\n  overtime_pay = overtime_hours * 150\n  gross = basic + hra + da + overtime_pay + incentive\n  deduction = gross * 0.08\n  net = gross - deduction\n  PRINT salary statement
```

## Python source code
See `employee_payroll.py` in this folder. Run it with:

```bash
python employee_payroll.py
```

## Test cases
| Basic | OT hours | Incentive | Expected net (₹) |\n|---:|---:|---:|---:|\n| 20000 | 0 | 0 | 23920.00 |\n| 30000 | 5 | 1000 | 37490.00 |

## Sample output
Run the program and enter the values from the test cases above. The program prints the calculated result in the terminal. A real output screenshot can be captured after running it in IDLE, VS Code, or a terminal.

## Conclusion
The program calculates salary components and produces a clear net-pay statement.
