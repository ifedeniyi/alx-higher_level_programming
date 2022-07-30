#!/usr/bin/python3
"""The `rectangle` module

It defines one class, `Rectangle()`,
which sub-classes the `Base()` class.`
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

    Attributes:
        width (int): the width of the `Rectangle` instance
        height (int): the height of the `Rectangle` instance
        x (int): x-coordinate
        y (int): y-coordinate
        id (int): the id for an instance of the `Rectangle` instance
    """

    field_names = ["id", "width", "height", "x", "y"]

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The width property of the `Rectangle` instance.

        Raises:
            TypeError: if `width` is not an int
            ValueError: if `width` <= 0
        """

        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """The height property of the `Rectangle` instance.

        Raises:
            TypeError: if `height` is not an int
            ValueError: if `height` <= 0
        """

        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """The x-coordinate of the `Rectangle` instance.

        Raises:
            TypeError: if `x` is not an int
            ValueError: if `x` < 0
        """

        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """The y-coordinate of the `Rectangle` instance.

        Raises:
            TypeError: if `y` is not an int
            ValueError: if `y` < 0
        """

        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of a `Rectangle` instance.
        """

        return self.width * self.height

    def display(self):
        """Prints to stdout the `Rectangle` instance with the character `#`,
        applying `x` and `y` offsets as necesssary.
        """

        print('\n' * self.y, end='')
        for _ in range(self.height):
            print(' ' * self.x, end='')
            for _ in range(self.width):
                print("#", end='')
            print('')

    def update(self, *args, **kwargs):
        """Updates a `Rectangle` instance dynamically."""

        argc = len(args)
        kwargc = len(kwargs)

        if argc > 0:
            self.id = args[0]
            if argc > 1:
                self.width = args[1]
                if argc > 2:
                    self.height = args[2]
                    if argc > 3:
                        self.x = args[3]
                        if argc > 4:
                            self.y = args[4]
        elif kwargc > 0:
            for k, v in kwargs.items():
                try:
                    if self.__getattribute__(k) is not None:
                        self.__setattr__(k, int(v) if str.isalnum(v) else v)
                except Exception as e:
                    print(e)
                    pass

    def to_dictionary(self):
        """Returns the dictionary representation of a `Rectangle`."""

        attrs = ["x", "y", "id", "height", "width"]
        return {x: self.__getattribute__(x) for x in attrs}

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
