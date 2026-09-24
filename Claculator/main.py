import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        raise ValueError("Cannot divide by zero.")
    return n1 / n2


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def get_number(prompt):
    """Get a valid number from the user."""

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_operation():
    """Get a valid mathematical operation from the user."""

    print("\nAvailable operations:")

    for symbol in OPERATIONS:
        print(symbol)

    while True:
        operation = input("Pick an operation: ").strip()

        if operation in OPERATIONS:
            return operation

        print("Please choose one of the available operations.")


def calculate(num1, num2, operation):
    """Perform the selected calculation."""

    try:
        return OPERATIONS[operation](num1, num2)
    except ValueError as error:
        print(error)
        return None


def calculator():
    """Run one complete calculator session."""

    print(art.logo)

    num1 = get_number("What is the first number?: ")

    while True:
        operation = get_operation()
        num2 = get_number("What is the next number?: ")

        answer = calculate(num1, num2, operation)

        if answer is None:
            continue

        print(f"\n{num1:g} {operation} {num2:g} = {answer:g}")

        choice = input(
            f"\nType 'y' to continue calculating with {answer:g}, "
            "or type 'n' to start a new calculation: "
        ).lower().strip()

        if choice == "y":
            num1 = answer
        else:
            break


def main():
    while True:
        calculator()

        choice = input(
            "\nType 'y' to start a new calculation, "
            "or type 'n' to exit: "
        ).lower().strip()

        if choice != "y":
            print("Goodbye!")
            break

        print("\n" * 20)


if __name__ == "__main__":
    main()
