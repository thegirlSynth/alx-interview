#!/usr/bin/python3
"""
Solves the problem described in the README
"""


def sieve_of_eratosthenes(n):
    """
    Determines if number is prime
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return [i for i in range(2, n + 1) if primes[i]]


def isWinner(x, nums):
    """
    Decides who is the winner of each round
    """
    maria = 0
    ben = 0

    if x > 0:
        primes = sieve_of_eratosthenes(max(nums))

        for num in nums:
            winner = "ben" if num in primes else "maria"
            if winner == "maria":
                maria += 1
            elif winner == "ben":
                ben += 1

    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"

    return None
