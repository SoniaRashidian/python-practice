import random

from hangman_art import logo, stages
from hangman_words import word_list


def display_word(chosen_word, guessed_letters):
    """Return the current state of the word with unguessed letters hidden."""
    return "".join(
        letter if letter in guessed_letters else "_"
        for letter in chosen_word
    )


def play_game():
    """Run one complete game of Hangman."""
    lives = 6
    chosen_word = random.choice(word_list)
    guessed_letters = set()

    print(logo)

    while lives > 0:
        print(f"\n{'*' * 12} {lives}/6 LIVES LEFT {'*' * 12}")

        current_display = display_word(chosen_word, guessed_letters)
        print(f"Word to guess: {current_display}")

        # Check whether the player has already guessed the letter
        while True:
            guess = input("Guess a letter: ").lower().strip()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
            elif guess in guessed_letters:
                print(f"You've already guessed '{guess}'.")
            else:
                break

        guessed_letters.add(guess)

        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed '{guess}', that's not in the word. You lose a life.")

        # Display the updated Hangman stage
        print(stages[lives])

        # Check for a win
        current_display = display_word(chosen_word, guessed_letters)

        if "_" not in current_display:
            print(f"\n{current_display}")
            print("**************************** YOU WIN ****************************")
            return

    # If the loop ends, the player has lost
    print(f"\nThe word was: {chosen_word}")
    print("**************************** YOU LOSE ****************************")


if __name__ == "__main__":
    play_game()
