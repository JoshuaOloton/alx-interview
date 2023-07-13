#!/usr/bin/python3
"""
This module contains a function that calculates the minimum number
of operations needed to result in exactly n 'H' characters in a file,
using only the 'Copy All' and 'Paste' operations.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to result in
    exactly n 'H' characters in a file.

    :param n: The desired number of 'H' characters in the file.
    :type n: int
    :return: The minimum number of operations needed to achieve n
    'H' characters in the file.
    :rtype: int
    """
    if n < 1:
        return 0
    i = 2
    num_operations = 0
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            num_operations += i
    if n > 1:
        num_operations += n
    return num_operations
