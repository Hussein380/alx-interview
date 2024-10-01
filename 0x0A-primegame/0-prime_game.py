#!/usr/bin/python3


def sieve_of_eratosthenes(limit):
    """Generate a list of prime numbers up to a given limit using the Sieve of
    Eratosthenes."""

    # Create a list to track the prime status of each number from 0 to limit
    is_prime = [True] * (limit + 1)

    # Mark 0 and 1 as not prime
    is_prime[0], is_prime[1] = False, False

    # Start checking for primes from 2
    current_prime = 2

    # Continue until current_prime squared exceeds the limit
    while current_prime * current_prime <= limit:

        # If current_prime is still marked as prime
        if is_prime[current_prime]:

            # Mark all multiples of current_prime as non-prime
            for multiple in range(current_prime * current_prime, limit + 1,
                                  current_prime):
                is_prime[multiple] = False

        # Move to the next number
        current_prime += 1

    # Return a list of all numbers that are marked as prime
    return [number for number in range(limit + 1) if is_prime[number]]


def is_winner(num_rounds, rounds):
    """Determine the winner of the prime game based on the number of rounds
    and values of n."""

    # Find the maximum value of n from the input rounds
    max_n = max(rounds)

    # Get all prime numbers up to the maximum n
    prime_numbers = sieve_of_eratosthenes(max_n)

    # Initialize win counters for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Process each round of the game
    for n in rounds:
        # Create a list to track available numbers from 1 to n
        available_numbers = [True] * (n + 1)

        # Start with Maria's turn (0 for Maria, 1 for Ben)
        current_turn = 0

        # Check each prime number
        for prime in prime_numbers:

            # Break if the prime exceeds the current n
            if prime > n:
                break

            # If the prime number is still available
            if available_numbers[prime]:

                # Player removes the prime and its multiples
                for multiple in range(prime, n + 1, prime):
                    available_numbers[multiple] = False  # Mark as removed

                # Switch turns: if it was Maria's turn, it's now Ben's
                current_turn = 1 - current_turn

        # Determine the winner of the round
        if current_turn == 0:
            maria_wins += 1
        else:  # If it's Ben's turn, Maria can't move and Ben wins
            ben_wins += 1

    # Determine the overall winner based on win counts
    if maria_wins > ben_wins:
        return "Maria"  # Maria wins more rounds
    elif ben_wins > maria_wins:
        return "Ben"  # Ben wins more rounds
    else:
        return None  # If they have the same number of wins
