#!/usr/bin/python3
"""The `rectangle` module

It defines one class, `Rectangle(Base).`
"""
from models.base import Base


class Rectangle(Base):
    """A `Rectangle` class to create rectangle objects.

    Args:
        width (int): the width of the `Rectangle` instance
        height (int): the height of the `Rectangle` instance
        x (int, optional): x-coordinate
        y (int, optional): y-coordinate
        id (int, optional): the id for an instance of the `Rectangle` instance
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """The width property of the `Rectangle` instance."""

        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        """The height property of the `Rectangle` instance."""

        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        """"""

        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        """"""

        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
