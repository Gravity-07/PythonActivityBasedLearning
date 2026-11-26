# 03. Retail Billing with Discounts

## Problem statement
Generate an itemized retail bill for several products, applying category tax and a threshold-based discount.

## Objectives
Use lists, loops, strings, arithmetic, and conditional statements to process multiple products.

## Assumptions
Each product has a name, category, price, and quantity. Electronics tax is 18%; other categories have 5% tax. A 10% discount applies when the pre-tax subtotal is at least ₹2,000. Discount is applied before tax.

## Algorithm
1. Read number of products. 2. For each product, read details and validate. 3. Calculate line total and subtotal. 4. Apply threshold discount. 5. Calculate category taxes on discounted line values. 6. Print invoice.

## Flowchart
```text
Start → Read product count → Loop through products → Validate details → Calculate subtotal → Discount threshold? → Calculate tax → Print itemized invoice → End
```

## Pseudocode
```text
INPUT product_count\nsubtotal = 0; items = empty list\nREPEAT product_count times:\n  INPUT name, category, price, quantity\n  VALIDATE price and quantity\n  line = price * quantity\n  ADD item to items; subtotal += line\nIF subtotal >= 2000: discount_rate = 0.10 ELSE 0\ndiscount = subtotal * discount_rate\nFOR each item: discounted_line = line * (1-discount_rate)\n  tax_rate = 0.18 if category is electronics else 0.05\n  tax += discounted_line * tax_rate\nPRINT invoice and subtotal - discount + tax
```

## Python source code
See `retail_billing.py` in this folder. Run it with:

```bash
python retail_billing.py
```

## Test cases
| Products | Subtotal | Discount | Expected total (₹) |\n|---|---:|---:|---:|\n| Book: 2 × 100 | 200 | 0 | 210.00 |\n| Electronics: 1 × 2500 | 2500 | 250 | 2655.00 |

## Sample output
Run the program and enter the values from the test cases above. The program prints the calculated result in the terminal. A real output screenshot can be captured after running it in IDLE, VS Code, or a terminal.

## Conclusion
The program uses a list and loop to build an invoice and apply conditional discounts and category-specific taxes.
