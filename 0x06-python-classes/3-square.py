#!/usr/bin/python3
"""Exports a Square class."""


class Square:
    """Square class that does nothing yet

    Args:
        size (int): Size of square instance.
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Compute area of square.

        Returns:
            (int) Area of square instance.
        """

        return self.__size ** 2
