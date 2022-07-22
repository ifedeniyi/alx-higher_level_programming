#!/usr/bin/python3
"""Defines a class, `BaseGeometry()`."""


class BaseGeometry:
    """Empty class"""

    def area(self):
        """empty function

        Raises:
            Exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate arguments

        Args:
            name
            value
        """

        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
