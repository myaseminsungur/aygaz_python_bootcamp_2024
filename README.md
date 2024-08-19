# Rock, Paper, Scissors Game

Welcome to the **Rock, Paper, Scissors Arena!** 🎉

This is a Python-based implementation of the classic game "Rock, Paper, Scissors." The game allows you to play against the computer in a series of rounds until one of you wins two rounds to become the champion.

## How to Play

1. **Game Introduction**: The game introduces itself, explaining the rules and setting up the excitement.
2. **Choices**: The player chooses between `rock`, `paper`, or `scissors`.
3. **Result**: The game compares the player's choice with the computer's random choice and displays the result of each round.
4. **Scoring**: The first to win two rounds becomes the winner of the game.
5. **Replay**: After a game ends, the player is asked if they want to play again. The computer may or may not agree to a rematch.

## Rules

- **Rock crushes Scissors**: Rock wins.
- **Scissors cut Paper**: Scissors win.
- **Paper wraps Rock**: Paper wins.
- If both choices are the same, the round is a draw.

## Code Overview

- **`game_intro()`**: Introduces the game and displays the rules.
- **`rps(player, computer)`**: Determines the winner of a round based on the player's and computer's choices.
- **`display_results()`**: Displays the result of each round, including the choices, the result, and the current score.
- **`tas_kagit_makas_YASEMIN_SUNGUR()`**: The main function that runs the game, handling user input, game logic, and replay functionality.

## Getting Started

### Prerequisites

- Python 3.x

### Running the Game

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/aygaz-python-bootcamp.git
2. Navigate to the project directory:
   cd aygaz-python-bootcamp
3. Run the game:
   python3 tas_kagit_makas_Yasemin_Sungur.py
