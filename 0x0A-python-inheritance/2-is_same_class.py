#!/usr/bin/python3
"""This is the `2-is_same_class` module.

The `2-is_same_class` module supplies one function, `is_same_class()`.
"""


def is_same_class(obj, a_class):
    """check if `obj` is an exact instance of `a_class`.

    Args:
        obj: object to check instance of
        a_class: class to perform check against

    Returns:
        bool: True if `obj` is instance of `a_class`, False otherwise
    """

    return type(obj) is a_class
