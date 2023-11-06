#!/usr/bin/python3
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
    """
    Checks if a queen is a vertical threat to another queen
    """
    # Check each row of the chessboard for the given column

    for row_index in range(len(board)):
        if board[row_index][col]:
            if row_index != row:
                return True
    return False


def check_horizontal_threat(board, row, col):
    """
    Checks if a queen is a horizontal threat to another queen
    """

    chess_row = board[row]
    index = 0

    for index in range(len(chess_row)):
        if chess_row[index]:
            if chess_row[index] != col:
                return True
        index += 1
    return False


def backtrack():
    pass


def place_queen(N):
    chess_board = create_board(N)
    chess_board[3][0] = 1

    for board in chess_board:  # output test
        print(board)
    # print(len(chess_board))

    # is_threat = check_diagonal_threat(board, row, col)
    # is_threat = check_vertical_threat(chess_board, 3, 3)
    is_threat = check_horizontal_threat(chess_board, 3, 3)
    return is_threat


# is_threat = True
val = place_queen(int(sys.argv[1]))
print(val)
