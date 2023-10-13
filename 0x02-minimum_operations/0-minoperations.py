#!/usr/bin/python3
"""
Minimum Operations - Check README.md for detailed explanation of the problem.
"""


def minOperations(n):
    """
    This is the second version of the solution.
    As the first one was not very efficient in handling large numbers,
    there was a need to refactor the function.

    This approach uses a function find_factors to find all the factors of n,
    and then uses is_prime to find the ones that are prime numbers.

    In other words, the prime factors of n are first computed, and a sum
    of those factors are returned.
    """
    factors_list = find_factors(n)

    prime_factors = []
    for item in factors_list:
        if is_prime(item):
            prime_factors.append(item)

    return sum(prime_factors)


def find_factors(n):
    factors = []  # Initialize an empty list to store the factors

    # Loop through numbers from 1 to the square root of n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)  # i is a factor
            factors.append(n // i)  # n // i is also a factor

    return factors


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
