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

    def to_json(self, attrs=None):
        """Retrieves the dictionary representation of a Student instance,
            only including elements in `attrs` if present.

        Args:
            attrs (:obj:`list`, optional) : list to filter against

        Returns;
            :obj:`dict`: dictionary representation of `Student` instance
        """

        if type(attrs) is list:
            return dict(filter(
                lambda el: el[0] in attrs, self.__dict__.items()))

        return self.__dict__
