#!/usr/bin/python3
"""Interesting class."""


class Square:
    """A class of squares and stuff.

    Args:
        size
        position

    Attributes:
        size (:obj:`int`, optional): size of `Square` instance
        position (:obj:`tuple` of :obj:`int`): Coordinates of `Square` instance
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """:obj:`tuple` of :obj:`int`: Coordinates for x and y axis.

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
        """Compute the area of the square instance.

        Returns:
            (int) The area of the square
        """

        return self.__size ** 2

    def my_print(self):
        """Prints representation of the square using `#'s`."""

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

    def __str__(self):
        square = []

        if self.__size == 0:
            return ''
        for _ in range(self.__position[1]):
            square.append('\n')
        for rows in range(self.__size):
            for _ in range(self.__position[0]):
                square.append(' ')
            for _ in range(self.__size):
                square.append('#')
            if rows != self.__size - 1:
                square.append('\n')
        return ''.join(square)
