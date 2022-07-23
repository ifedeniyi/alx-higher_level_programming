#!/usr/bin/python3
"""The `student` module

Defines one class, `Student`.
"""


class Student:
    """Student class

    Args:
        first_name
        last_name
        age

    Attributes:
        first_name
        last_name
        age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves the dictionary representation of a Student instance."""

        return self.__dict__
