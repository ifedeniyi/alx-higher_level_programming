#!/usr/bin/python3
"""Defines a class `Rectangle`."""

Bg = __import__("7-base_geometry").BaseGeometry


class Rectangle(Bg):
    """Constructs a rectangle object.

    Args:
        width (int)
        height (int)
    """

    def __init__(self, width, height):
        super().integer_validator('width', width)
        super().integer_validator('height', height)

        self.__width = width
        self.__height = height
