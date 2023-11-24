#!/usr/bin/python3
"""
makeChange solves the problem described in the README.md
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """
    coins.sort(reverse=True)

    def makeChangeRecursive(coins, total, index):
        if total == 0:
            return 0
        if index == len(coins):
            return float("inf")

        minCoins = float("inf")
        for i in range(index, len(coins)):
            if coins[i] <= total:
                res = makeChangeRecursive(coins, total - coins[i], i)
                minCoins = min(minCoins, res + 1)

        return minCoins

    minCoins = makeChangeRecursive(coins, total, 0)
    return minCoins if minCoins <= total else -1
