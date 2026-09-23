import art


def find_highest_bidder(bidding_record):
    """Return the winner and highest bid from the bidding record."""

    highest_bid = 0
    winner = ""

    for bidder, bid_amount in bidding_record.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    return winner, highest_bid


def get_bid():
    """Get and validate a positive bid amount from the user."""

    while True:
        try:
            bid = int(input("What is your bid?: $"))

            if bid <= 0:
                print("Please enter a bid greater than $0.")
                continue

            return bid

        except ValueError:
            print("Please enter a valid whole number.")


def get_yes_no(prompt):
    """Get a valid yes/no response from the user."""

    while True:
        response = input(prompt).lower().strip()

        if response in ("yes", "no"):
            return response

        print("Please type 'yes' or 'no'.")


def main():
    print(art.logo)

    bids = {}

    while True:
        name = input("What is your name?: ").strip()

        while not name:
            print("Name cannot be empty.")
            name = input("What is your name?: ").strip()

      
        bids[name] = get_bid()

        should_continue = get_yes_no(
            "Are there any other bidders? Type 'yes' or 'no'.\n"
        )

        if should_continue == "no":
            break

        # Clear the previous bidder's information from the screen.
        print("\n" * 30)

    winner, highest_bid = find_highest_bidder(bids)

    print("\n" * 2)
    print("****************************")
    print("       AUCTION RESULTS")
    print("****************************")
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
    print("****************************")


if __name__ == "__main__":
    main()
