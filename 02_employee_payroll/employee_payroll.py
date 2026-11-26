def calculate_salary(basic, overtime_hours, incentive):
    if basic < 0 or overtime_hours < 0 or incentive < 0:
        raise ValueError("Salary inputs cannot be negative.")

    hra = basic * 0.20
    da = basic * 0.10
    overtime_pay = overtime_hours * 150
    gross = basic + hra + da + overtime_pay + incentive
    deduction = gross * 0.08
    net = gross - deduction
    return hra, da, overtime_pay, gross, deduction, net


def main():
    name = input("Enter employee name: ").strip()
    try:
        basic = float(input("Enter basic pay (Rs.): "))
        overtime_hours = float(input("Enter overtime hours: "))
        incentive = float(input("Enter incentive (Rs.): "))
        hra, da, overtime_pay, gross, deduction, net = calculate_salary(
            basic, overtime_hours, incentive
        )

        print("\\n========== SALARY STATEMENT ==========")
        print("Employee       :", name if name else "Not provided")
        print(f"Basic pay      : Rs. {basic:.2f}")
        print(f"HRA (20%)      : Rs. {hra:.2f}")
        print(f"DA (10%)       : Rs. {da:.2f}")
        print(f"Overtime pay   : Rs. {overtime_pay:.2f}")
        print(f"Incentive      : Rs. {incentive:.2f}")
        print(f"Gross salary   : Rs. {gross:.2f}")
        print(f"Deduction (8%) : Rs. {deduction:.2f}")
        print(f"Net salary     : Rs. {net:.2f}")
    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
