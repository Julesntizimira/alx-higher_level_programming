#!/usr/bin/python3
'''101-nqueens module
'''


import sys

def solve_nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens_helper(board, 0, solutions)

    for solution in solutions:
        print(solution)

def solve_nqueens_helper(board, col, solutions):
    N = len(board)
    if col == N:
        # Found a solution, add it to the list
        queens = []
        for c in range(N):
            for r in range(N):
                if board[r][c] == 1:
                    queens.append([r, c])
        solutions.append(queens)
        return

    for row in range(N):
        if is_safe(board, row, col):
            # Place the queen at (row, col)
            board[row][col] = 1

            # Recursively solve the subproblem
            solve_nqueens_helper(board, col + 1, solutions)

            # Remove the queen from (row, col) for backtracking
            board[row][col] = 0

def is_safe(board, row, col):
    N = len(board)

    # Check if there is a queen in the same row
    for c in range(col):
        if board[row][c] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    # Check if there is a queen in the lower left diagonal
    r, c = row, col
    while r < N and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1

    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]
    solve_nqueens(N)

