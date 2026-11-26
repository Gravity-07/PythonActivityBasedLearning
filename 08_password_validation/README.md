# 08. Password Policy Validation

## Problem statement
Check sample passwords against a simple policy covering minimum length, uppercase, lowercase, digit, special character, repeated characters, and a prohibited substring.

## Objectives
Practise strings, loops, conditionals, and Boolean variables.

## Assumptions
Minimum length is 8. At least one uppercase letter, lowercase letter, digit, and special character is required. Three identical consecutive characters are not allowed. The substring 'password' is prohibited without regard to case. This is an educational validator, not a complete security system.

## Algorithm
1. Read a password. 2. Check length and character categories using a loop. 3. Check repeated consecutive characters. 4. Check prohibited substring. 5. Display every failed rule and final status.

## Flowchart
```text
Start → Input password → Check length → Scan characters → Check repetition → Check prohibited word → Any failures? → Print result → End
```

## Pseudocode
```text
INPUT password\nfailures = empty list\nCHECK length >= 8\nSET category flags false\nFOR each character: update uppercase/lowercase/digit/special flags\nCHECK all flags\nCHECK for three consecutive same characters\nCHECK 'password' not in lowercase password\nIF failures empty: PRINT valid ELSE PRINT each failure
```

## Python source code
See `password_validation.py` in this folder. Run it with:

```bash
python password_validation.py
```

## Test cases
| Sample | Expected result |\n|---|---|\n| Abcdef1! | Valid |\n| abc12345 | Invalid: uppercase and special character missing |\n| Password1! | Invalid: prohibited substring |\n| AAAabc1! | Invalid: three repeated consecutive characters |

## Sample output
Run the program and enter the values from the test cases above. The program prints the calculated result in the terminal. A real output screenshot can be captured after running it in IDLE, VS Code, or a terminal.

## Conclusion
The validator uses basic string operations and loops to report which password rules are not satisfied.
