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
    """
    Checks if a queen is a diagonal threat to another queen
    """
    for i in range(row):
        if abs(row - i) == abs(col - board[row][i]):
            return True
    return False


def check_vertical_threat(board, row, col):
    """
    Checks if a queen is a vertical threat to another queen
    """

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
    chess_board[0][0] = 1
    # chess_board[3][0] = 1
    # chess_board[2][2] = 1
    # chess_board[1][3] = 1

    for board in chess_board:  # output test
        print(board)
    # print(len(chess_board))

    # Check if the queen is being placed in a threatened position
    is_threat = check_diagonal_threat(chess_board, 2, 1)
    if not is_threat:
        print("I'm here 1")
        is_threat = check_vertical_threat(chess_board, 2, 1)
    if not is_threat:
        print("I'm here 2")
        is_threat = check_horizontal_threat(chess_board, 2, 1)

    return is_threat


val = place_queen(int(sys.argv[1]))
print(val)
