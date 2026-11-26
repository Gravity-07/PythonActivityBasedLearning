# 05. ATM Transaction Sequence Simulation

## Problem statement
Simulate a sequence of deposits and withdrawals, maintain the account balance, reject invalid transactions, and summarize accepted transactions.

## Objectives
Use loops, lists, tuples, conditional statements, and arithmetic operators.

## Assumptions
Opening balance is non-negative. Transactions are entered as D for deposit or W for withdrawal. Amounts must be positive. A single withdrawal cannot exceed ₹10,000 or the available balance.

## Algorithm
1. Read opening balance and number of transactions. 2. Repeat for each transaction. 3. Validate type and amount. 4. Accept valid deposits. 5. Accept withdrawals only within balance and limit. 6. Store transaction outcomes. 7. Print summary.

## Flowchart
```text
Start → Input opening balance/count → Loop transactions → Valid type and amount? → Deposit or withdrawal rules → Update balance or reject → Store result → Print summary → End
```

## Pseudocode
```text
INPUT balance, count\nFOR each transaction:\n  INPUT type, amount\n  IF amount <= 0: reject\n  ELSE IF type = D: balance += amount; accepted\n  ELSE IF type = W AND amount <= 10000 AND amount <= balance: balance -= amount; accepted\n  ELSE: reject\nPRINT transaction list, accepted count, rejected count, balance
```

## Python source code
See `atm_simulation.py` in this folder. Run it with:

```bash
python atm_simulation.py
```

## Test cases
| Opening balance | Transactions | Expected closing balance |\n|---:|---|---:|\n| 5000 | D 1000; W 2000 | 4000 |\n| 500 | W 700 | 500 (withdrawal rejected) |

## Sample output
Run the program and enter the values from the test cases above. The program prints the calculated result in the terminal. A real output screenshot can be captured after running it in IDLE, VS Code, or a terminal.

## Conclusion
The simulation demonstrates transaction validation, sequential balance updates, and tuple-based transaction records.
