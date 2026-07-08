import random

# ASCII Art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = ["Rock", "Paper", "Scissors"]
images = [rock, paper, scissors]


def get_user_choice():
    """Get a valid choice from the user."""
    while True:
        try:
            choice = int(input("\nChoose:\n0 - Rock\n1 - Paper\n2 - Scissors\n\nYour choice: "))
            if choice in [0, 1, 2]:
                return choice
            else:
                print("❌ Please enter 0, 1, or 2.")
        except ValueError:
            print("❌ Please enter a valid number.")


def determine_winner(user, computer):
    """Return the result of one round."""
    if user == computer:
        return "tie"

    if (user == 0 and computer == 2) or \
       (user == 1 and computer == 0) or \
       (user == 2 and computer == 1):
        return "user"

    return "computer"


def display_choices(user, computer):
    print("\nYou chose:")
    print(images[user])

    print("Computer chose:")
    print(images[computer])


def play_game():
    user_score = 0
    computer_score = 0
    ties = 0

    print("=" * 45)
    print("🎮 ROCK • PAPER • SCISSORS")
    print("=" * 45)

    while True:
        user = get_user_choice()
        computer = random.randint(0, 2)

        display_choices(user, computer)

        result = determine_winner(user, computer)

        if result == "user":
            print("🎉 You win this round!")
            user_score += 1

        elif result == "computer":
            print("💻 Computer wins this round!")
            computer_score += 1

        else:
            print("🤝 It's a tie!")
            ties += 1

        print("\n----------- SCORE -----------")
        print(f"You       : {user_score}")
        print(f"Computer  : {computer_score}")
        print(f"Ties      : {ties}")
        print("-----------------------------")

        again = input("\nPlay another round? (y/n): ").lower()

        if again != "y":
            break

    print("\n========== FINAL SCORE ==========")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print(f"Ties: {ties}")

    if user_score > computer_score:
        print("\n🏆 Overall Winner: You!")

    elif computer_score > user_score:
        print("\n💻 Overall Winner: Computer!")

    else:
        print("\n🤝 Overall Result: Draw!")

    print("\nThanks for playing!")


play_game()
