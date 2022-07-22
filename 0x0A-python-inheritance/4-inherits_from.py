#!/usr/bin/python3
"""This is the `4-inherits_from` module.

The `4-inherits_from` module supplies one function, `inherits_from()`.
"""


def inherits_from(obj, a_class):
    """check if `obj` is instance of `a_class`.

    Args:
        obj: object to check instance of
        a_class: class to perform check against

    Returns:
        bool: True if `obj` is exact instance of `a_class`, False otherwise
    """

    if type(obj) == a_class:
        return
    return isinstance(obj, a_class)
