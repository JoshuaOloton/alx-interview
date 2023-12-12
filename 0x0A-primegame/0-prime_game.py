#!/usr/bin/python3
"""
Module: Game of choosing Prime numbers
"""


def is_prime(num):
    """
    Check if a given number is prime.

    Parameters:
    - num (int): The number to check for primality.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            return False
    return True


def get_primes(n):
    """
    Get a list of prime numbers up to a given number.

    Parameters:
    - n (int): The upper limit for generating prime numbers.

    Returns:
    - list: A list of prime numbers up to n.
    """
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def optimal_move(nums):
    """
    Determine the optimal move for a player given a set of numbers.

    Parameters:
    - nums (list): The set of numbers to choose from.

    Returns:
    - list: The set of numbers after the optimal move is made.
    """
    primes = get_primes(max(nums))
    for prime in primes:
        if any(num % prime == 0 for num in nums):
            return [num for num in nums if num % prime != 0]
    return []


def isWinner(x, nums):
    """
    Determine the winner of each round in a game played by Maria and Ben.

    Parameters:
    - x (int): The number of rounds.
    - nums (list): An array of n for each round.

    Returns:
    - str or None: The name of the player that won the most rounds.
                  Returns "Maria" or "Ben" if there is a clear winner.
                  Returns None if the winner cannot be determined.
    """

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        rounds = [i for i in range(1, n + 1)]
        maria_turn = True

        while rounds:
            if maria_turn:
                moves = optimal_move(rounds)
                if moves:
                    rounds = moves
                    maria_turn = not maria_turn
                    continue
                else:
                    ben_wins += 1
                    break
            else:
                moves = optimal_move(rounds)
                if moves:
                    rounds = moves
                    maria_turn = not maria_turn
                    continue
                else:
                    maria_wins += 1
                    break

    if maria_wins < ben_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    return None
