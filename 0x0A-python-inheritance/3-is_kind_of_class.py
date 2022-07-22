#!/usr/bin/python3
"""This is the `3-is_kind_of_class` module.

The `3-is_kind_of_class` module supplies one function, `is_kind_of_class()`.
"""


def is_kind_of_class(obj, a_class):
    """check if `obj` is instance of `a_class`.

    Args:
        obj: object to check instance of
        a_class: class to perform check against

    Returns:
        bool: True if `obj` is exact instance of `a_class`, False otherwise
    """

    return isinstance(obj, a_class)
