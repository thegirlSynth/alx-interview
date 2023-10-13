#!/usr/bin/python3
"""
Minimum Operations - Check README.md for detailed explanation of the problem.
"""


def minOperations(n):
    """
    This solution uses a recursive call to the function minOperations.

    Since performing this operation:
      when n = 2, minimum number of operations(min_num) = 2;
      when n = 3, min_num = 3;
      when n = 5, min_num = 5;
      when n = 7, min_num = 7;

    If you can break down a number into its factors, you can add up the min_num
    of each factor and their total will equal the minimum number required for
    the number to solve this problem successfully.
    """

    # Base Case
    if n <= 1:
        return 0

    min_num = 0
    factors = [2, 3, 5, 7]
    for num in factors:
        if n % num == 0:
            n = n // num
            min_num = num + minOperations(n)
            break

    return min_num
