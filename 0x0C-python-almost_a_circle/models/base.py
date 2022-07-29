#!/usr/bin/python3
"""The `base` module.

It defines one class, `Base`.
"""


from ast import Dict
import json


class Base:
    """This class will be the “base” of all other classes in this project.
        The goal of it is to manage id attribute in all your future classes
        and to avoid duplicating the same code (by extension, same bugs)

        Args:
            id (:obj:`Any`, optional): The id for an instance of the
            `Base` class.

        Attributes:
            id (:obj:`Any`): The id for an instance of the `Base` class.
        """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of `list_dictionaries`."""

        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)
