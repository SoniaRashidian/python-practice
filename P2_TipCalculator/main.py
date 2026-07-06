def get_float(prompt):
    """Safely get a floating-point number from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("❌ Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


def get_int(prompt):
    """Safely get an integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("❌ Please enter a number greater than zero.")
            else:
                return value
        except ValueError:
            print("❌ Invalid input. Please enter an integer.")


def calculate_tip():
    print("\n" + "=" * 40)
    print("        💰 TIP CALCULATOR")
    print("=" * 40)

    total_bill = get_float("Enter the total bill ($): ")
    tip_percent = get_float("Enter tip percentage (%): ")
    people = get_int("Number of people splitting the bill: ")

    tip_amount = total_bill * tip_percent / 100
    total_with_tip = total_bill + tip_amount
    amount_per_person = total_with_tip / people

    print("\n-------- BILL SUMMARY --------")
    print(f"Original Bill : ${total_bill:.2f}")
    print(f"Tip ({tip_percent:.1f}%) : ${tip_amount:.2f}")
    print(f"Total Bill    : ${total_with_tip:.2f}")
    print(f"People        : {people}")
    print("------------------------------")
    print(f"Each person pays: ${amount_per_person:.2f}")
    print("------------------------------")


print("Welcome to the Advanced Tip Calculator!")

while True:
    calculate_tip()

    again = input("\nCalculate another bill? (y/n): ").strip().lower()

    if again != "y":
        print("\nThank you for using the Tip Calculator! 👋")
        break
