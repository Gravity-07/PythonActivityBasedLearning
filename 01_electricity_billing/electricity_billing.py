def calculate_bill(units):
    if units < 0:
        raise ValueError("Units cannot be negative.")

    if units <= 100:
        energy_charge = units * 3
    elif units <= 200:
        energy_charge = 100 * 3 + (units - 100) * 5
    else:
        energy_charge = 100 * 3 + 100 * 5 + (units - 200) * 7

    fixed_charge = 50
    subtotal = energy_charge + fixed_charge
    rebate = subtotal * 0.05 if units <= 100 else 0
    total = subtotal - rebate
    return energy_charge, fixed_charge, rebate, total


def main():
    try:
        units = float(input("Enter electricity units consumed: "))
        energy, fixed, rebate, total = calculate_bill(units)
        print("\\n------ ELECTRICITY BILL ------")
        print(f"Units consumed : {units:.2f}")
        print(f"Energy charge  : Rs. {energy:.2f}")
        print(f"Fixed charge   : Rs. {fixed:.2f}")
        print(f"Rebate         : Rs. {rebate:.2f}")
        print(f"Total bill     : Rs. {total:.2f}")
    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
