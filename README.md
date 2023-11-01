# Hangman Game

This is a simple Hangman game implemented in Python. Players can guess letters to uncover a hidden word. The game provides a menu for starting the game and offers visual feedback on the progress. If you correctly guess all the letters before running out of attempts, you win the game.

## Getting Started

### Prerequisites

Make sure you have Python installed on your computer.

### Installation

1. Clone the repository to your local machine or download the code as a ZIP file and extract it.
2. Make sure you have a `palabras.txt` file in the same directory with a list of words, one word per line, in uppercase letters. You can customize this file with your own list of words.

## Running the Game

1. Open your terminal or command prompt.
2. Navigate to the directory where the game files are located.
3. Run the game by executing the following command:

   ```python hangman.py```

4. Follow the on-screen instructions to play the game. You can start the game by entering '1' and then press Enter.

## Gameplay

1. You will be presented with a hidden word represented by underscores, e.g., "_ _ _ _ _".

2. Enter a letter and press Enter to make a guess. You can only enter one letter at a time.

3. If your letter is in the word, it will be revealed in its correct positions. If not, you will lose an attempt.

4. Continue guessing letters until you either guess the entire word correctly or run out of attempts.

5. If you guess the word, you win the game, and the word is revealed.

6. If you run out of attempts, you lose the game.

7. You can replay the game or exit the program when prompted.

## Customization

You can customize the list of words in the `palabras.txt` file to make the game more challenging or tailored to your preferences.

## Author

Alejandro Vargas

## Acknowledgments

This Hangman game is a simple yet fun project that demonstrates Python programming and interactive console-based games. It can be a great way to improve your coding skills and have fun at the same time. Feel free to modify and enhance the game as you see fit!
