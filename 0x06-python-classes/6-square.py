#!/usr/bin/python3
"""Exports a Square class."""


class Square:
    """Square class that does some things.

    Args:
        size (:obj:`int`, optional): Size of the square. Defaults to `0`.
        position (:obj:`tuple` of :obj:`int`, optional): Coordinates for
            x and y axis. Defaults to `(0, 0)`.

    Attributes:
        size (int): Size of the square.
        position (:obj:`tuple` of :obj:`int`): Coordinates for x and y axis.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: Size of the square.

        Note:
            Setter raises a TypeError if `size` is not an int,
                and raises a ValueError if `size < 0`
        """

        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        """:obj:`tuple` of :obj:`int`: coordinates for x and y axis.

        Note:
            Setter raises a TypeError if
                : `position` is not a tuple of length 2,
                : `position` elements are not positive integers
        """

        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[1] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Find the area of the square instance.

        Returns:
            (int) The area of the square.
        """

        return self.__size ** 2

    def my_print(self):
        """Prints representation of the square using `#'s`"""

        if self.__size > 0:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
