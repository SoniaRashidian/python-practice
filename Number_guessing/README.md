# Number Guessing Game

The player guesses a randomly generated number between 1 and 100 and receives hints after each incorrect guess.

The game features two difficulty levels, input validation, an attempt counter, and the option to replay multiple rounds.

## Project Overview

The Number Guessing Game is a simple interactive Python application designed to practice fundamental programming concepts, including functions, loops, conditional statements, exception handling, and random number generation.

At the beginning of each round, the program generates a random number. The player selects a difficulty level and tries to guess the correct number within the allowed attempts.

The game provides feedback indicating whether each guess is too high or too low, helping the player narrow down the answer.

## Game Rules

The objective is to guess a randomly generated number between 1 and 100.

| Difficulty | Allowed Attempts |
| ---------- | ---------------: |
| Easy       |               10 |
| Hard       |                5 |

### How to Play

1. Start the game.
2. Select a difficulty level: `easy` or `hard`.
3. Enter a number between 1 and 100.
4. Receive a hint:

   * **Too high:** Your guess is greater than the answer.
   * **Too low:** Your guess is less than the answer.
5. Continue guessing until you find the correct number or run out of attempts.
6. Choose whether to play another round.

Invalid entries do not consume attempts.


