#!/usr/bin/python3
"""Module 101-add_attribute.

Checks if an attribute can be added to an object.
"""


def add_attribute(obj, key, value):
    """Checks if `key` of `value` can be added to `obj`.

    Args:
        - obj: object to add the attribute to
        - key: name of the attribute
        - value: value of the attribute to add
    """

    if not hasattr(obj, '__slots__') and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(obj, '__slots__') and not hasattr(obj, key):
        raise TypeError("can't add new attribute")

    setattr(obj, key, value)
