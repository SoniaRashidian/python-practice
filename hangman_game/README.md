# Hangman Game

Python code for the classic **Hangman word-guessing game**.

The player attempts to guess a randomly selected word one letter at a time. Each incorrect guess reduces the number of remaining lives, while correctly guessed letters are revealed in the word.

This project was developed as a Python programming practice project to strengthen understanding of **loops, conditionals, functions, collections, user input, random selection, and modular Python files**.

## 🎮 How the Game Works

1. A random word is selected from the word list.
2. The word is initially displayed as underscores.
3. The player guesses one letter at a time.
4. Correct guesses reveal the corresponding letters.
5. Incorrect guesses reduce the player's remaining lives.
6. The Hangman illustration changes according to the number of lives remaining.
7. The player wins by revealing the entire word before running out of lives.
8. The player loses when all six lives are used.

## 📁 Project Structure

```text
hangman-game/
│
├── main.py             # Main game logic
├── hangman_art.py      # Hangman logo and visual stages
├── hangman_words.py    # Word list used by the game
├── README.md           # Project documentation
└── .gitignore          # Git configuration
```


## 📷 Example Gameplay

```text
**************************** 6/6 LIVES LEFT ****************************
Word to guess: _ _ _ _ _

Guess a letter: a

Word to guess: _ a _ _ _

**************************** 6/6 LIVES LEFT ****************************
Guess a letter: z

You guessed 'z', that's not in the word. You lose a life.
```

