# Sudoku Visualizer

A simple and interactive Sudoku game built with Python and Pygame.  
You can play Sudoku, enter your own numbers, solve the puzzle in real-time with a visual backtracking algorithm, and reset the board at any time.

---

## Features

- **Interactive Sudoku Board:** Click any cell and type numbers (1–9) to fill the board.
- **Real-Time Solver:** Press `Enter` to watch the board solve itself step by step using backtracking.
- **Reset:** Press `R` to reset the puzzle to its original state.
- **Win Detection:** The game detects when you have correctly completed the puzzle and displays a win message.
- **Instructions:** Brief instructions are shown for 2 seconds when the game starts.

---

## Controls

- **Click** a cell to select it.
- **Type 1–9** to fill the selected cell.
- **Press `Enter`** to auto-solve the puzzle visually.
- **Press `R`** to reset the puzzle.
- **Close** the window to exit.

---

## Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/)

---

## How to Run

1. Install Python and Pygame if you haven't already:
    ```sh
    pip install pygame
    ```
2. Download or clone this repository.
3. Run the main file:
    ```sh
    python main.py
    ```

---

## Customization

- You can change the initial puzzle by editing the `grid` variable in `main.py`.
- Adjust the solver speed by changing the `pygame.time.delay(50)` value in the `solver` function.

---

## Screenshot

![Sudoku Screenshot](Output_screenshot.png)

---

## License

This project is for educational and personal use.
