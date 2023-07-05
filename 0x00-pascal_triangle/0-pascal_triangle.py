#!/usr/bin/python3
"""
pascal_triangle function
"""


def pascal_triangle(n):
    if n <= 0:
        return []
    total = [[1], [1, 1]]
    for i in range(n-2):
        current = total[len(total)-1]
        new_list = [1]
        for j in range(1, len(current)):
            new_list.append(current[j] + current[j-1])
            if j == len(current) - 1:
                new_list.append(1)
                total.append(new_list)

    return total
