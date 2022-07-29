#!/usr/bin/python3
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
        self.size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """The size property of the `Square` instance.

        Raises:
            TypeError: if `size` is not an int
            ValueError: if `size` <= 0
        """

        return self.width

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates a `Square` instance dynamically."""

        argc = len(args)
        kwargc = len(kwargs)

        if argc > 0:
            self.id = args[0]
            if argc > 1:
                self.width = args[1]
                self.height = args[1]
                if argc > 2:
                    self.x = args[2]
                    if argc > 3:
                        self.y = args[3]

        elif kwargc > 0:
            for k, v in kwargs.items():
                try:
                    if self.__getattribute__(k) is not None:
                        self.__setattr__(k, v)
                except Exception:
                    pass

    def to_dictionary(self):
        """Returns the dictionary representation of a `Square`."""

        attrs = ["id", "x", "size", "y"]
        return {x: self.__getattribute__(x) for x in attrs}
