#!/usr/bin/python3
"""The Ppascal's triangle module

Defines one function, `pascal_triangle()`.
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
        the Pascal’s triangle"""

    if n <= 0:
        return []

    col = [[1]]

    while len(col) != n:
        prev = col[-1]
        row = [1]

        for i in range(len(prev) - 1):
            row.append(prev[i] + prev[i+1])

        row.append(1)
        col.append(row)

    return col
