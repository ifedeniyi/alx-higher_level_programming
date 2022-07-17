#!/usr/bin/python3
"""Not sure what this does yet... stay tuned."""


def add_integer(a, b=98):
    """Returns the addition of two integers `a` and `b`.

    Args:
        a (int): First operand in addition operarion.
        b (:obj:`int`, optional): Second operand in addition operation.

    Returns:
        (int) Result of adding `a` and `b`.
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
