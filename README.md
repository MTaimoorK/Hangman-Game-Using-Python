# Hangman Game

A simple Hangman game implemented in Python. The game randomly selects a word from a predefined list and allows the player to guess letters or the entire word.

## Files

- `word_list.py`: Contains a list of English words used in the game. It generates a random list of 100 words using the NLTK library.

- `hangman_game.py`: The main Hangman game script. It imports the `random_words` list from `word_list.py` and includes functions for playing the game, getting words, and displaying the Hangman stages.

## Requirements

- Python 3.x
- NLTK (Natural Language Toolkit) library (install using `pip install nltk`)

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/hangman-game.git
   cd hangman-game

## Gameplay:

- The game starts by randomly selecting a word from the list.
- You have to guess letters or the entire word within a limited number of tries (6 in this case).
- The Hangman stages are displayed as you make incorrect guesses.
- If you correctly guess the word or run out of tries, the game will provide the outcome.
