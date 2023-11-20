#!/usr/bin/python3
"""
Solves the problem described in the README.md
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise
    """

    size = len(matrix)

    for row in range(size):
        for col in range(row, size):
            matrix[row][col], matrix[col][row] = (
                matrix[col][row],
                matrix[row][col],
            )  # noqa

    for row in matrix:
        row.reverse()
