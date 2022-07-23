#!/usr/bin/python3
"""The Ppascal's triangle module

Defines one function, `pascal_triangle()`.
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
        the Pascal’s triangle"""

    col = []

    if n <= 0:
        return result

    for i in range(n):
        row = []

        if i == 0:
            col.append([1])
            continue

        prev = col[-1]

        # prev -> [1, 2, 1] -> len = 3
        for j in range(len(prev) + 1):
            if j == 0:
                row.append(1)
                continue

            if j == len(prev):
                row.append(1)
                break

            result = prev[j] + prev[j - 1]
            row.append(result)

        col.append(row)

    return col
