#!/usr/bin/python3
"""
Minimum Operations - Check README.md for detailed explanation of the problem.
"""


def minOperations(n):
    """
    This is the second version of the solution.
    As the first one was not very efficient in handling large numbers,
    there was a need to refactor the function.

    This approach is to compute the prime factors of n,
    and then return a sum of those factors.
    """

    if n <= 1:
        return 0

    factors_list = prime_factors(n)
    return sum(factors_list)


def prime_factors(n, divisor=2):
    # Base case
    if n == 1:
        return []

    factors = []

    # Find the smallest prime divisor of n
    while n % divisor != 0:
        divisor += 1

    # Append the prime factor to the list
    factors.append(divisor)

    # Recursively find the prime factors of the remaining part
    factors.extend(prime_factors(n // divisor, divisor))

    return factors
