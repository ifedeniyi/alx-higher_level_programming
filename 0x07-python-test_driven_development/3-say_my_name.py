#!/usr/bin/python3
"""This is the `3-say_my_name` module.

The `3-say_my_name` module supplies one function, `say_my_name()`.

Example:
    >>> say_my_name = __import__("3-say_my_name").say_my_name
    >>> say_my_name("Frank", "Sinatra")
    My name is Frank Sinatra
"""


def say_my_name(first_name, last_name=""):
    """Prints string containing `first_name` and `last_name`.

    Args:
        first_name (string)
        last_name (:obj:`string`, optional)

    Raises:
        TypeError: If either `first_name` or `last_name` are not strings
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
