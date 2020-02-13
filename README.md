# Sudoku game in Python

This is a simple sudoku game made in Python. This repository includes a terminal version, a GUI version and a solving algorithm.

## How to download

1. Clone this repository using `git clone https://github.com/Louis-Navarro/sudoku.git` or download the `.zip` file. Then open a terminal window in the folder

2. Type `pip install -r requirements.txt` and ther press enter. This will install all the required modules

3. Done ! You can now play sudoku in the terminal or with a GUI and quickly solve sudoku grids !

## How does the algorithm works

The algorithm used is a backtracking algorithm:
Firstly, it will find a number that can fill the first square, then same for the second square etc...
If no number works in one of the squares, the algorithm searches for another number in the previous square and so one.

![Backtracking tree](https://camo.githubusercontent.com/3683f568b4f63fa8a90276a03de022f09fcb16d4/687474703a2f2f692e696d6775722e636f6d2f4b644572434f552e676966 "Backtracking algorithm example")

NB: This is not the actual program, this is an example of how the algorithm works.
