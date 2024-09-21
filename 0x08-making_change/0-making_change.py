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

    # If total is zero or less, no coins are needed
    if total <= 0:
        return 0

    # Initialize an array to store the fewest number of coins
    # for each amount up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins are needed to make a total of 0

    # Loop through all the amounts from 1 to total
    for i in range(1, total + 1):
        # Check each coin
        for coin in coins:
            if coin <= i:  # If the coin can be used (i.e., it's less than
                # or equal to the current amount)
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be achieved
    return dp[total] if dp[total] != float('inf') else -1
