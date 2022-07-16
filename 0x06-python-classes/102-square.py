#!/usr/bin/python3
"""Interesting class."""


class Square:
    """A class of squares and stuff.

    Args:
        size

    Attributes:
        size (:obj:`int`, optional): size of `Square` instance
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """int: Size of the square

        Note:
            Setter raises a TypeError if `value` is not type `int`,
            and if `value < 0`.
        """

        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Compute the area of the square instance.

        Returns:
            (int) The area of the square
        """

        return self.__size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __le__(self, other):
        return self.area() <= other.area()
