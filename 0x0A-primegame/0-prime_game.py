#!/usr/bin/python3
"""
Solves the problem described in the README
"""


def isWinner(x, nums):
    """
    Prime Game
    """

    maria = 0
    ben = 0

    if x > 0:
        for num in nums:
            winner = find_winner(num)
            if winner == "maria":
                maria += 1
            elif winner == "ben":
                ben += 1

    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"

    return None


def is_prime(num):
    """
    Determines if number is prime
    """

    if num < 2:
        return False

    for n in range(2, int(0.5**num) + 1):
        if num % n == 0:
            return False

    return True


def find_winner(n):
    """
    Decides who is the winner of each round
    """

    primes = [i for i in range(2, n + 1) if is_prime(i)]

    if len(primes) % 2 == 0:
        return "ben"
    return "maria"
