def minimum_classes(conducted, attended, target):
    if conducted <= 0:
        raise ValueError("Conducted classes must be greater than zero.")
    if attended < 0 or attended > conducted:
        raise ValueError("Attended classes must be between 0 and conducted.")
    if target < 0 or target > 100:
        raise ValueError("Target must be between 0 and 100.")

    current_percentage = attended / conducted * 100
    future = 0
    while (attended + future) / (conducted + future) * 100 < target:
        future += 1
    return current_percentage, future


def main():
    try:
        conducted = int(input("Total classes conducted: "))
        attended = int(input("Classes attended: "))
        target = float(input("Required attendance percentage: "))
        current, future = minimum_classes(conducted, attended, target)

        print(f"Current attendance: {current:.2f}%")
        if future == 0:
            print("The student already meets the requirement.")
        else:
            print("Minimum additional consecutive classes to attend:", future)
    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
