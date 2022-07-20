#!/usr/bin/python3
""" Create a rectangle class """


class Rectangle:
    """Definition of class rectangle

    Args:
        width (:obj:`int`, optional): width of `Rectangle` instance
        height (:obj:`int`, optional): height of `Rectangle` instance

    Attributes:
        width (int): width of `Rectangle` instance
        height (int): height of `Rectangle` instance
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: Width of the rectangle

        Note:
            Setter raises a TypeError if `width` is not type `int`,
            and a ValueError if `width < 0`.
        """

        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """int: Height of the rectangle

        Note:
            Setter raises a TypeError if `value` is not type `int`,
            and a ValueError if `height < 0`.
        """

        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
