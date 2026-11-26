def main():
    try:
        balance = float(input("Opening balance (Rs.): "))
        count = int(input("Number of transactions: "))
        if balance < 0 or count < 0:
            raise ValueError("Balance and transaction count cannot be negative.")

        transactions = []
        accepted = 0
        rejected = 0

        for index in range(count):
            print(f"\\nTransaction {index + 1}")
            kind = input("Type (D=deposit, W=withdrawal): ").strip().upper()
            amount = float(input("Amount (Rs.): "))
            status = "REJECTED"

            if amount > 0 and kind == "D":
                balance += amount
                status = "ACCEPTED"
            elif amount > 0 and kind == "W":
                if amount <= 10000 and amount <= balance:
                    balance -= amount
                    status = "ACCEPTED"
            elif kind not in ("D", "W"):
                print("Unknown transaction type.")

            if status == "ACCEPTED":
                accepted += 1
            else:
                rejected += 1

            transactions.append((kind, amount, status, balance))
            print(status, "| Current balance: Rs.", f"{balance:.2f}")

        print("\\n========== ATM SUMMARY ==========")
        for number, (kind, amount, status, remaining) in enumerate(transactions, 1):
            print(f"{number}. {kind} Rs.{amount:.2f} - {status} - Balance Rs.{remaining:.2f}")
        print("Accepted transactions:", accepted)
        print("Rejected transactions:", rejected)
        print(f"Closing balance: Rs. {balance:.2f}")
    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
