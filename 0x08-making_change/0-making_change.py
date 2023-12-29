#!/usr/bin/python3
"""
makeChange solves the problem described in the README.md
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    INF = float("inf")
    dp = [0] + [INF] * total

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != INF else -1
