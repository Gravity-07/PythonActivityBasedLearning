def main():
    try:
        count = int(input("Number of products: "))
        if count <= 0:
            raise ValueError("Enter at least one product.")

        report = []
        for index in range(count):
            print(f"\\nProduct {index + 1}")
            name = input("Product name: ").strip()
            opening = int(input("Opening stock: "))
            received = int(input("Received quantity: "))
            dispatched = int(input("Dispatched quantity: "))
            recorded = int(input("Recorded closing stock: "))
            reorder = int(input("Reorder level: "))

            values = [opening, received, dispatched, recorded, reorder]
            if any(value < 0 for value in values):
                raise ValueError("Stock quantities cannot be negative.")

            expected = opening + received - dispatched
            if expected < 0:
                raise ValueError("Dispatched quantity cannot exceed available stock.")
            discrepancy = recorded - expected
            replenishment = max(0, reorder - recorded)
            report.append((name, expected, recorded, discrepancy, replenishment))

        print("\\n========== INVENTORY REPORT ==========")
        for name, expected, recorded, discrepancy, replenishment in report:
            print(f"Product: {name}")
            print(f"  Expected closing stock : {expected}")
            print(f"  Recorded closing stock : {recorded}")
            print(f"  Discrepancy             : {discrepancy}")
            print(f"  Replenishment required  : {replenishment}")
            print("  Status                  :", "MATCH" if discrepancy == 0 else "CHECK RECORD")
    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
