#!/usr/bin/python3
"""The `base` module.

It defines one class, `Base`.
"""
import csv
import json
import os
import turtle
import time
from random import randrange


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
    def reset_obj_count():
        """Reset the private class attribute `__nb_objects`."""

        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of `list_dictionaries`.

        Args:
            list_dictionaries (:obj:`dict` of `list`): a list of dictionaries.
        """

        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the object representation of `json_string`.

        Args:
            json_string (str): a JSON string representation of an object.
        """

        if json_string is None:
            return []

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of `list_objs` to a file.

        Args:
            list_objs (:obj:`Object` of `list`): a list of instances
            of the `Base` class or it's sub-classes.
        """

        with open('{}.json'.format(cls.__name__), 'w') as f:
            dict_list = []
            if list_objs is not None:
                for item in list_objs:
                    dict_list.append(item.to_dictionary())

            f.write(cls.to_json_string(dict_list))

    @classmethod
    def create(cls, **dictionary):
        """Dynamically initializes a new instance with
        values from `dictionary`.
        """

        inst = cls(*[1 for _ in dictionary])
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """Loads list of instance dictionaries from file,
        and converts to a list of instances.
        """

        if not os.path.exists("{}.json".format(cls.__name__)):
            return []

        with open("{}.json".format(cls.__name__), 'r') as f:
            dict_list = cls.from_json_string(f.read())
            return [cls.create(**d) for d in dict_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string representation of `list_objs` to a file.

        Args:
            list_objs (:obj:`Object` of `list`): a list of instances
            of the `Base` class or it's sub-classes.
        """

        with open('{}.csv'.format(cls.__name__), 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=cls.field_names)
            writer.writeheader()

            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads the CSV string representation of `list_objs` from a file,
        and converts it to a list of instances.
        """

        with open('{}.csv'.format(cls.__name__), newline='') as f:
            reader = csv.DictReader(f)

            return [cls.create(**row) for row in reader]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """A static method that opens a window and draws all the instances"""

        t = turtle.Turtle()
        t.color("beige")
        turtle.bgcolor("violet")
        t.shape("square")
        t.pensize(8)

        for i in (list_rectangles + list_squares):
            t.penup()
            t.setpos(0, 0)
            turtle.Screen().colormode(255)
            t.pencolor((randrange(255), randrange(255), randrange(255)))
            Base.draw_rect(t, i)
            time.sleep(1)
        time.sleep(5)

    @staticmethod
    def draw_rect(t, rect):
        """Helper method that draws a Rectangle
        or Square.
        """

        t.penup()
        t.setpos(rect.x, rect.y)
        t.pendown()
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
