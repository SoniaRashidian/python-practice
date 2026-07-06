import time


def slow_print(text):
    """Print text with a small delay for a storytelling effect."""
    print(text)
    time.sleep(1)


def get_choice(question, options):
    """
    Ask the user a question until a valid answer is given.
    """
    while True:
        choice = input(question).strip().lower()
        if choice in options:
            return choice
        print(f"❌ Invalid choice. Please choose: {', '.join(options)}")


def game_over(reason):
    print("\n" + "=" * 45)
    print(f"💀 {reason}")
    print("GAME OVER")
    print("=" * 45)


def victory():
    print("\n" + "=" * 45)
    print("🏆 Congratulations!")
    print("You found the hidden treasure!")
    print("YOU WIN!")
    print("=" * 45)


def play_game():
    print("=" * 45)
    print("🏝️ TREASURE ISLAND")
    print("=" * 45)
    print("Your mission is to find the treasure.\n")

    direction = get_choice(
        "You arrive at a crossroads.\nGo Left or Right? ",
        ["left", "right"]
    )

    if direction == "right":
        game_over("You fell into a deep hole.")
        return

    slow_print("\nYou continue walking...")

    lake = get_choice(
        "\nYou reach a lake.\nWait for a boat or Swim? ",
        ["wait", "swim"]
    )

    if lake == "swim":
        game_over("A giant trout attacked you.")
        return

    slow_print("\nThe boat safely takes you to the island...")

    door = get_choice(
        "\nThree doors stand before you.\nChoose Red, Blue, or Yellow: ",
        ["red", "blue", "yellow"]
    )

    if door == "red":
        game_over("The room is full of fire.")
    elif door == "blue":
        game_over("Wild beasts were waiting inside.")
    else:
        victory()


print("Welcome to Treasure Island!\n")

while True:
    play_game()

    again = input("\nPlay again? (y/n): ").lower()

    if again != "y":
        print("\nThanks for playing! 👋")
        break
