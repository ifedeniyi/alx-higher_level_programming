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
    """Divides all emalents of a matrix `matrix` by int `div`.

    Args:
        matrix (:obj:`list` of :obj:`list`): Matrix to transform.
        div (int): Int to divide `matrix` elements by.

    Returns:
        (:obj:`list` of :obj:`list`): Transformed matrix.
    """

    return list(map(lambda x: list(map(lambda y: y // div, x)), matrix))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
