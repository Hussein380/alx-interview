#!/usr/bin/python3
import sys


def solve_nqueens(n):
    board = [-1] * n  # Initialize the board with no queens placed

    def is_safe(row, col):
        # Check if it's safe to place a queen at (row, col)
        for i in range(row):
            # Check the same column
            if board[i] == col:
                return False
            # Check the same diagonal (upward and downward)
            if board[i] - i == col - row:
                return False
            if board[i] + i == col + row:
                return False
        return True

    def print_solution():
        # Print the current board configuration
        solution = [[i, board[i]] for i in range(n)]
        print(solution)

    def backtrack(row):
        if row == n:
            print_solution()
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)  # Start the backtracking process from the first row


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
