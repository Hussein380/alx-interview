#!/usr/bin/python3

"""Module containing the make_change function to solve the coin change
problem."""


def make_change(coins, total):
    """
    Determine the minimum number of coins needed to achieve the given
    total amount.

    Args:
    coins (list): A list of available coin denominations.
    total (int): The target amount to achieve.

    Returns:
    int: The fewest number of coins needed to meet the total.
         Returns 0 if the total is 0 or less.
         Returns -1 if it's not possible to meet the total with the
         available coins.
    """

    # If no coins are provided, return -1 (impossible to make change)
    if not coins or coins is None:
        return -1

    # If total is zero or less, no coins are needed
    if total <= 0:
        return 0

    # Initialize the count of coins used
    coin_count = 0

    # Sort coins in descending order for the greedy approach
    coins = sorted(coins, reverse=True)

    # Try to reduce the total by the largest coin value first
    for coin in coins:
        # Use as many of the current coin as possible
        while coin <= total:
            total -= coin
            coin_count += 1

        # If total reaches zero, return the number of coins used
        if total == 0:
            return coin_count

    # If we exit the loop and total is not zero, return -1
    return -1
