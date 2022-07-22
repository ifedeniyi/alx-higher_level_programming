#!/usr/bin/python3
"""Defines a class `Square`."""

Rect = __import__("9-rectangle").Rectangle


class Square(Rect):
    """Constructs a Square object.

    Args:
        size (int)
    """

    def __init__(self, size):
        super().integer_validator('size', size)

        self.__size = size

    def area(self):
        """Compute area of square object"""

        return self.size ** 2
