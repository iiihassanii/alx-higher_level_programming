#!/usr/bin/python3
import sys
"""_summary_
        """


def nqueen(size, row):
    list_queen = []
    for row in range(size):
        col = row
        for col in range(size):
            board.append([row, col])

    print(notallow)
    print()
    board = []


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

size = sys.argv[1]
if isinstance(size, int):
    print("N must be a number")
    exit(1)

size = int(size)

if size < 4:
    print("N must be at least 4")
    exit(1)


for row in range(size):
    nqueen(size, row)
