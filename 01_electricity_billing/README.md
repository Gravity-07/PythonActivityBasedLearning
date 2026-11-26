# 01. Progressive Electricity Billing

## Problem statement
Calculate a household electricity bill using progressive consumption slabs, a fixed charge, and a rebate for low consumption.

## Objectives
Use variables, numeric data types, arithmetic, conditional statements, and functions to calculate a bill.

## Assumptions
Units are non-negative. Slab rates are ₹3.00 for the first 100 units, ₹5.00 for the next 100, and ₹7.00 above 200. Fixed charge is ₹50. A 5% rebate applies when usage is at most 100 units.

## Algorithm
1. Read units consumed. 2. Reject negative input. 3. Calculate each slab charge. 4. Add fixed charge. 5. Apply the rebate if eligible. 6. Display the itemized bill.

## Flowchart
```text
Start → Read units → Valid units? → Calculate slab charges → Add fixed charge → Rebate eligible? → Calculate final bill → Display → End
```

## Pseudocode
```text
INPUT units\nIF units < 0: PRINT error\nELSE:\n  CALCULATE slab charges\n  total = energy_charge + fixed_charge\n  IF units <= 100: total = total * 0.95\n  PRINT bill
```

## Python source code
See `electricity_billing.py` in this folder. Run it with:

```bash
python electricity_billing.py
```

## Test cases
| Units | Expected energy charge | Expected final bill (₹) |\n|---:|---:|---:|\n| 50 | 150 | 190.00 (after rebate) |\n| 150 | 550 | 600.00 |\n| 250 | 1150 | 1200.00 |

## Sample output
Run the program and enter the values from the test cases above. The program prints the calculated result in the terminal. A real output screenshot can be captured after running it in IDLE, VS Code, or a terminal.

## Conclusion
The program demonstrates progressive slab billing and a conditional rebate using basic Python constructs.
