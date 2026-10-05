```python
"""
Number Guessing Game

A command-line game in which the player tries to guess
a randomly generated number between 1 and 100.
"""

from random import randint


# Game configuration
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
MIN_NUMBER = 1
MAX_NUMBER = 100

LOGO = r"""
 _   _                 _               
| \ | |_   _ _ __ ___ | |__   ___ _ __ 
|  \| | | | | '_ ` _ \| '_ \ / _ \ '__|
| |\  | |_| | | | | | | |_) |  __/ |   
|_| \_|\__,_|_| |_| |_|_.__/ \___|_|   

"""


def set_difficulty():
    """Ask the player to select a difficulty and return attempts."""
    while True:
        level = input(
            "Choose a difficulty. Type 'easy' or 'hard': "
        ).strip().lower()

        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("Invalid choice. Please enter 'easy' or 'hard'.")


def get_guess():
    """Get a valid integer guess between 1 and 100."""
    while True:
        try:
            guess = int(input("Make a guess: "))

            if MIN_NUMBER <= guess <= MAX_NUMBER:
                return guess

            print(
                f"Please enter a number between "
                f"{MIN_NUMBER} and {MAX_NUMBER}."
            )

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def check_answer(user_guess, actual_answer):
    """Compare the guess with the answer and provide a hint."""
    if user_guess > actual_answer:
        print("Too high.")
        return False

    elif user_guess < actual_answer:
        print("Too low.")
        return False

    else:
        print(f"You got it! The answer was {actual_answer}.")
        return True


def play_round():
    """Run one round of the Number Guessing Game."""
    answer = randint(MIN_NUMBER, MAX_NUMBER)
    turns = set_difficulty()

    print(
        f"\nYou have {turns} attempts to guess "
        f"the number."
    )

    while turns > 0:
        guess = get_guess()

        if check_answer(guess, answer):
            print("Congratulations! You win!")
            return

        turns -= 1

        if turns > 0:
            print(
                f"You have {turns} "
                f"{'attempt' if turns == 1 else 'attempts'} remaining."
            )
            print("Guess again.")
        else:
            print("You've run out of guesses. You lose.")
            print(f"The correct answer was {answer}.")


def game():
    """Start the game and allow the player to replay."""
    print(LOGO)
    print("Welcome to the Number Guessing Game!")
    print(
        f"I'm thinking of a number between "
        f"{MIN_NUMBER} and {MAX_NUMBER}."
    )

    while True:
        play_round()

        while True:
            play_again = input(
                "\nWould you like to play again? (yes/no): "
            ).strip().lower()

            if play_again in ("yes", "y"):
                print("\n" + "-" * 40 + "\n")
                break

            elif play_again in ("no", "n"):
                print("Thanks for playing. Goodbye!")
                return

            else:
                print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    game()
```
