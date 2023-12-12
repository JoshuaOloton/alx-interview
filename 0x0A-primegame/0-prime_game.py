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
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def primeNos(n):
    """
    Returns a list of prime numbers between 1 and n inclusive.

    Args:
        n (int): The upper boundary of the range (inclusive).
        The lower boundary is always 1.

    Returns:
        list: A list of prime numbers between 1 and n.

    Examples:
        >>> primeNos(10)
        [2, 3, 5, 7]

    Note:
        The function uses the is_prime helper
        function to identify prime numbers.
    """
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game for a
    given number of rounds and upper limits.

    Args:
        x (int): The number of rounds of the game.
        nums (list): A list of upper limits for each round.

    Returns:
        str or None: The name of the winner (Maria or Ben)
        or None if the winner cannot be determined.

    Raises:
        ValueError: If input arguments are invalid
        (x is None, nums is None, x is not positive, or nums is an empty list).
    """
    if x is None or nums is None or x <= 0 or nums == []:
        return None
    maria, ben = 0, 0
    for i in range(x):
        prime_numbers = primeNos(nums[i])
        if len(prime_numbers) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if maria < ben:
        return 'Ben'
    elif maria > ben:
        return 'Maria'
    return None
