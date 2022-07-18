#!/usr/bin/python3
"""This is the `4-print_square` module.

The `4-print_square` module supplies one function, `print_square()`.

Example:
    >>> print_square = __import__("4-print_square").print_square
    >>> print_square(2)
    ##
    ##
"""


def print_square(size):
    """Prints a square with the character `#`.

    Args:
        size (int): Size of the square.

    Raises:
        TypeError: If `size` is not an int.
        ValueError: If `size` is less than 0.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print("")
