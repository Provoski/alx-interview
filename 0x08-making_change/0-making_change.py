#!/usr/bin/python3
"""0-making_change.py module"""


def makeChange(coins, total):
    """
    makeChange - determine the fewest number of coins needed
    to meet a given amount total.
    args:
        coin - list of the values of the coins in your possession
        total - tolat number of coin
    return - fewwlest number of coin needed
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
