#!/usr/bin/python3
"""Defines a `MyInt` class which sub-classes the `int` class."""


class MyInt(int):
    """Sub-classes the `int` class and Inverts the
        equality comparision of two integers."""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
