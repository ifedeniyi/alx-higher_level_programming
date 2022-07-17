#!/usr/bin/python3
"""This is the `2-matrix_divided` module.

The `2-matrix_divided` module supplies one function, `matrix_divided()`

Example:
    >>> matrix_divided = __import__("2-matrix_divided").matrix_divided
    >>> new_matrix = matrix_divided([[2, 4], [6, 8]], 2)
    >>> print(new_matrix)
    [[1, 2], [3, 4]]
"""


def matrix_divided(matrix, div):
    """Divides all elements of `matrix` by `div`.

    Args:
        matrix (:obj:`int` of :obj:`list` of :obj:`list`): Matrix to transform.
        div (int): Int to divide `matrix` elements by.

    Returns:
        (:obj:`float` of :obj:`list` of :obj:`list`): Transformed matrix.
    """

    row_len = 0
    new_arr = []
    type_err = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(type_err)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        if type(i) is not list:
            raise TypeError(type_err)
        else:
            row_len = row_len if row_len != 0 else len(i)

        if len(i) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        new_arr.append([])

        for j in i:
            if type(j) not in [int, float]:
                raise TypeError(type_err)
            new_arr[-1].append(round(j / div, 2))

    return new_arr
