#!/usr/bin/env python3
"""The `square` module

It defines one class, `Square(),
which sub-classes the `Rectangle()` class.`
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A `Square` class to create square objects.

    Args:
        size (int): the size of the `Square` instance
        x (int, optional): x-coordinate
        y (int, optional): y-coordinate
        id (int, optional): the id for an instance of the `Rectangle` instance

    Attributes:
        width (int): the width of the `Rectangle` instance
        height (int): the height of the `Rectangle` instance
        x (int): x-coordinate
        y (int): y-coordinate
        id (int): the id for an instance of the `Rectangle` instance
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)