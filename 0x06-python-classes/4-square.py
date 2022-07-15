#!/usr/bin/python3
"""Exports the Square class"""


class Square:
    """Square class that does some things

    Arguments:
        size (int): Size of the square.
    """

    def __init__(self, size=0):
        self.size = size


    @property
    def size(self):
        """int: Size of the square."""

        return self.__size


    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


    def area(self):
        """Find the area of the square instance.

        Returns:
            (int) The area of the square.
        """

        return self.__size ** 2
