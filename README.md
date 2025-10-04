# Project-2-Sudoku-Solver
Overview
This program is a step-by-step Sudoku solver. It reads a Sudoku puzzle from a puzzle file, solves it interactively while providing visual feedback, and writes the solved puzzle into the solved_puzzle text file. The program also follows the classic Sudoku rules to ensure a valid solution.

Features


Rules Display: Displays the rules of Sudoku to the user at the start.

Grid Input/Output:

Reads a Sudoku puzzle from a text file (puzzle.txt).
Outputs the solved puzzle to another text file (solved_puzzle.txt).



Step-by-Step Solution:

Displays the puzzle-solving process in a human-readable format, step by step.
Includes backtracking to ensure a valid solution.



Validation: Ensures every move adheres to Sudoku rules.


Requirements

Python 3.x
A text file containing the Sudoku puzzle (puzzle.txt).


Usage

Input File Format (puzzle.txt)
The puzzle should be a 9x9 grid of numbers, where:

Empty cells are represented by 0.
Numbers are separated by spaces.
Each row occupies a single line.

Example:

5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9

Steps to Run

Ensure the input file (puzzle.txt) is in the same directory as the script.
Run the script:

python sudoku_solver.py
The solving process and result will be written to solved_puzzle.txt.


Code Explanation


print_rules():

Displays the rules of Sudoku with a 10-second pause.



read_sudoku_from_file(file_path):

Reads the puzzle from a file and converts it into a 9x9 grid (list of lists).



print_grid(grid):

Prints the Sudoku grid to the console with . representing empty cells.



write_grid_to_file(grid, file_path):

Writes the grid to a file in a human-readable format.



is_valid_move(grid, row, col, num):

Validates whether placing num at (row, col) follows Sudoku rules.



solve_sudoku(grid):

Implements a backtracking algorithm to solve the Sudoku puzzle.
Provides real-time feedback during solving.



main():

Manages file I/O and coordinates the solving process.




Output


Real-Time Logs: Step-by-step actions are written to solved_puzzle.txt.

Solved Puzzle: The final solved grid is saved in solved_puzzle.txt if a solution exists. If not, a message indicating no solution is provided.


Notes

The solving process is slow for large or complex puzzles due to real-time logging and step-by-step visualization.
Ensure the input file adheres to the specified format; otherwise, the program may fail.


Example Output (solved_puzzle.txt)

Welcome to the Sudoku!
Rules of Sudoku:
1. Each row must contain the numbers 1 to 9 without repetition.
2. Each column must contain the numbers 1 to 9 without repetition.
3. Each 3x3 sub-grid must contain the numbers 1 to 9 without repetition.
Let's solve the puzzle step by step!

Initial Sudoku Grid:
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
...

Solving the puzzle step by step...
...

Puzzle solved successfully!
Solved Sudoku Grid:
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
...
