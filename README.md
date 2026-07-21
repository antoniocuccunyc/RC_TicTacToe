# RC_TicTacToe
 
A simple terminal-based Tic-Tac-Toe game written in Python, built as a practice project for the Recurse Center application.
 
## How it works
 
Two players take turns entering a number from 1-9 to place their mark on the board. The positions correspond to the grid like this:
 
```
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```
 
The game checks for a winner after every move (rows, columns, and diagonals) and detects a tie if the board fills up with no winner.
 
## Running it
 
Requires Python 3. From the project directory:
 
```bash
python3 main.py
```
 
Follow the prompts to enter your move each turn.
 
## Project structure
 
- `main.py` - all game logic: board display, win checking, input handling, and the main game loop.
