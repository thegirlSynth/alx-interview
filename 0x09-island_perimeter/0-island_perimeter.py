#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    SOlves the island perimeter problem
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell contributes 4 to the perimeter

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Deduct 2 if the cell above is land
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Deduct 2 if the cell to the left is land

    return perimeter
