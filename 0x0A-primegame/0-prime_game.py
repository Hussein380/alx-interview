#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def is_winner(rounds, nums):
    """Determine the overall winner after a series of rounds.

    Args:
        rounds (int): The number of rounds to play.
        nums (list): A list of integers representing the upper limit (n)
        for each round.

    Returns:
        str: Name of the player who won the most rounds, or None if it's a
        tie or invalid input.
    """

    # Check if the number of rounds is valid or if nums is None
    if rounds <= 0 or nums is None:
        return None

    # Ensure the number of rounds matches the length of nums
    if rounds != len(nums):
        return None

    # Initialize win counters for both players
    ben_wins = 0
    maria_wins = 0

    # Create a list to track prime numbers and their multiples
    max_num = sorted(nums)[-1]  # Get the maximum value in nums
    prime_tracker = [1 for _ in range(max_num + 1)]  # 1 indicates a prime
    prime_tracker[0], prime_tracker[1] = 0, 0  # 0 and 1 are not prime number

    # Mark non-prime numbers using the Sieve of Eratosthenes method
    for current_num in range(2, len(prime_tracker)):
        remove_multiples(prime_tracker, current_num)

    # Count wins based on the sums of prime_tracker
    for num in nums:
        if sum(prime_tracker[0:num + 1]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner based on win counts
    if ben_wins > maria_wins:
        return "Ben"
    if maria_wins > ben_wins:
        return "Maria"
    return None


def remove_multiples(prime_list, prime):
    """Remove multiples of the given prime from the list.

    Args:
        prime_list (list): A list where multiples of primes will be marked as
        not prime.
        prime (int): The current prime number whose multiples are to be rmv
    """

    # Iterate over the list to remove multiples of the prime number
    for multiple in range(2, len(prime_list)):
        try:
            prime_list[multiple * prime] = 0  # Mark as not prime
        except (ValueError, IndexError):
            break  # Exit if we go out of bounds
