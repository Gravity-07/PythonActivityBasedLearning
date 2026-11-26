# 06. Warehouse Inventory Reconciliation

## Problem statement
Compare opening stock, received stock, dispatched stock, and recorded closing stock for multiple products to find discrepancies and replenishment needs.

## Objectives
Practise lists, loops, arithmetic, and conditional statements.

## Assumptions
All quantities are whole numbers and non-negative. Expected closing stock = opening + received - dispatched. Reorder level is entered for each product.

## Algorithm
1. Read product count. 2. For each product, read quantities and reorder level. 3. Validate values. 4. Calculate expected stock and discrepancy. 5. Calculate replenishment quantity if below reorder level. 6. Display report.

## Flowchart
```text
Start → Read product count → Loop products → Input stock data → Validate → Calculate expected stock → Compare with recorded stock → Calculate reorder need → Report → End
```

## Pseudocode
```text
INPUT count\nFOR each product:\n  INPUT name, opening, received, dispatched, recorded, reorder_level\n  expected = opening + received - dispatched\n  discrepancy = recorded - expected\n  replenishment = max(0, reorder_level - recorded)\n  PRINT values and status
```

## Python source code
See `inventory_reconciliation.py` in this folder. Run it with:

```bash
python inventory_reconciliation.py
```

## Test cases
| Product | Opening | In | Out | Recorded | Reorder | Expected discrepancy | Replenishment |\n|---|---:|---:|---:|---:|---:|---:|---:|\n| Pen | 100 | 50 | 30 | 120 | 150 | 0 | 30 |\n| Book | 40 | 10 | 20 | 25 | 50 | -5 | 25 |

## Sample output
Run the program and enter the values from the test cases above. The program prints the calculated result in the terminal. A real output screenshot can be captured after running it in IDLE, VS Code, or a terminal.

## Conclusion
The program reconciles stock records and calculates the quantity needed to restore inventory to its reorder level.
