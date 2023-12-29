#!/usr/bin/python3
"""
Module to determine the fewest number of coins needed
   to meet a given amount total"
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed
       to meet a given amount total

    Args:
        coins (list): A list of the coin denominations available.
        total (int): The amount to be made change for.

    Returns:
        int: The fewest number of coins needed to meet the total.

    Examples:
        >>> makeChange([1, 2, 25], 37)
        7
    """

    if total <= 0:
        return 0
    coins.sort(reverse=True)
    min_coins = 0
    for coin in coins:
        if total <= 0:
            break
        if total >= coin:
            min_coins += total // coin
            total = total % coin
    if total != 0:
        return -1
    return min_coins
