def main():
    month = input("Month name: ").strip()
    try:
        days = int(input("Number of days (28-31): "))
        start_day = int(input("Starting weekday (0=Mon, 6=Sun): "))

        if not 28 <= days <= 31:
            raise ValueError("Day count must be from 28 to 31.")
        if not 0 <= start_day <= 6:
            raise ValueError("Starting weekday must be from 0 to 6.")

        weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
        print(f"\\n        {month}")
        for weekday in weekdays:
            print(f"{weekday:>4}", end="")
        print()

        for blank in range(start_day):
            print("    ", end="")

        for day in range(1, days + 1):
            print(f"{day:4}", end="")
            if (start_day + day) % 7 == 0:
                print()
        print()
    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
