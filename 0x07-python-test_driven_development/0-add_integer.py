#!/usr/bin/python3
"""Defines a function `add_integer` that adds 2 integers.

Example:
    >>> add_integer = __import__('0-add_integer').add_integer
    >>> print(add_integer(1, 2))
"""


def add_integer(a, b=98):
    """Adds two integers `a` and `b`.

    Args:
        a (int): First operand in addition operarion.
        b (:obj:`int`, optional): Second operand in addition operation.

    Raises:
        TypeError: If either `a` or `b` are not valid integers.

    Returns:
        int: Sum of `a` and `b`.
    """

    allowed_types = [int, float]

    if type(a) not in allowed_types:
        raise TypeError("a must be an integer")
    if type(b) not in allowed_types:
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
