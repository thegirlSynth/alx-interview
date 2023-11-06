#!/usr/bin/env python3
"""
Solves the N-Queens Problem as described in the README.md
"""


import sys


if len(sys.argv) != 2:
    print("Usage: nQueens N")
    exit(1)

try:
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)
except ValueError:
    print("N must be a number")
    exit(1)


def create_board(num):
    """
    Creates the required chessboard according to the specified size
    """
    chessboard = []
    for _ in range(num):
        row = []
        for _ in range(num):
            row.append(0)
        chessboard.append(row)

    return chessboard


def check_diagonal_threat(board, row, col):
    pass


def check_vertical_threat(board, row, col):
    pass


def check_horizontal_threat(board, row, col):
    pass


def place_queen(N):
    chess_board = create_board(N)

    for board in chess_board:  # output test
        print(board)

    # check_diagonal_threat(board, row, col)
    # check_vertical_threat(board, row, col)
    # check_horizontal_threat(board, row, col)


# is_threat = True
place_queen(int(sys.argv[1]))
