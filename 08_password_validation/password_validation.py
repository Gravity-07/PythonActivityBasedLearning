def validate_password(password):
    failures = []

    if len(password) < 8:
        failures.append("At least 8 characters are required.")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        else:
            has_special = True

    if not has_upper:
        failures.append("At least one uppercase letter is required.")
    if not has_lower:
        failures.append("At least one lowercase letter is required.")
    if not has_digit:
        failures.append("At least one digit is required.")
    if not has_special:
        failures.append("At least one special character is required.")
    if "password" in password.lower():
        failures.append("The word 'password' is not allowed.")

    repeated = False
    for index in range(len(password) - 2):
        if password[index] == password[index + 1] == password[index + 2]:
            repeated = True
            break
    if repeated:
        failures.append("Three identical consecutive characters are not allowed.")

    return failures


def main():
    password = input("Enter a sample password to validate: ")
    failures = validate_password(password)

    if len(failures) == 0:
        print("Result: Password meets this educational policy.")
    else:
        print("Result: Password does not meet the policy.")
        for failure in failures:
            print("-", failure)


if __name__ == "__main__":
    main()
