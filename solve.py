import time
import sys

def print_rules():
    print("Welcome to the Sudoku!")
    print("Rules of Sudoku:")
    print("1. Each row must contain the numbers 1 to 9 without repetition.")
    print("2. Each column must contain the numbers 1 to 9 without repetition.")
    print("3. Each 3x3 sub-grid must contain the numbers 1 to 9 without repetition.")
    print("Let's solve the puzzle step by step!")
    time.sleep(10)

def read_sudoku_from_file(file_path):
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                row = [int(num) for num in line.split()]
                if len(row) != 9:
                    raise ValueError(f"Invalid row length: {len(row)}. Each row must have 9 numbers.")
                grid.append(row)
    if len(grid) != 9:
        raise ValueError(f"Invalid grid size: {len(grid)} rows. Expected 9 rows.")
    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
    print("\n")

def write_grid_to_file(grid, file_path):
    with open(file_path, 'w') as file:
        for row in grid:
            file.write(" ".join(str(num) for num in row) + "\n")

def is_valid_move(grid, row, col, num):
    # Check row
    if num in grid[row]:
        return False

    # Check column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num
                        print(f"Placed {num} at ({row+1}, {col+1})")
                        print_grid(grid)
                        time.sleep(0.5)

                        if solve_sudoku(grid):
                            return True
                        # Undo the move
                        grid[row][col] = 0
                        print(f"Backtracked at ({row+1}, {col+1})")
                        print_grid(grid)
                        time.sleep(0.5)

                return False
    return True

def main():
    file_path = "puzzle.txt"
    solved_file_path = "solved_puzzle.txt"

    # Redirect stdout to the file
    with open(solved_file_path, 'w') as file:
        sys.stdout = file

        print_rules()

        sudoku_grid = read_sudoku_from_file(file_path)
        print("Initial Sudoku Grid:")
        print_grid(sudoku_grid)

        print("Solving the puzzle step by step...\n")
        if solve_sudoku(sudoku_grid):
            print("Puzzle solved successfully!")
            print("Solved Sudoku Grid:")
            print_grid(sudoku_grid)
        else:
            print("No solution exists for the given Sudoku puzzle.")

    # Restore stdout
    sys.stdout = sys.__stdout__

    print(f"The output has been written to {solved_file_path}.")

if __name__ == "__main__":
    main()