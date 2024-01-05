#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""


import sys

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

def solve_nqueens(n):
    def can_place(pos, ocuppied_positions):
        for i in range(len(ocuppied_positions)):
            if ocuppied_positions[i] == pos or \
                ocuppied_positions[i] - i == pos - len(ocuppied_positions) or \
                ocuppied_positions[i] + i == pos + len(ocuppied_positions):
                return False
        return True

    def place_queen(n, ocuppied_positions):
        if len(ocuppied_positions) == n:
            result.append(ocuppied_positions)
            return
        for pos in range(n):
            if can_place(pos, ocuppied_positions):
                place_queen(n, ocuppied_positions + [pos])

    result = []
    place_queen(n, [])
    return result

for solution in solve_nqueens(n):
    print([[i, solution[i]] for i in range(n)])
