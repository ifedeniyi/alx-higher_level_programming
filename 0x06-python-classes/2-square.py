#!/usr/bin/python3
"""Exports Square class"""


class Square:
    """Square class doing nothing useful yet.

    Args:
        size (int): Size of a square instance.
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
