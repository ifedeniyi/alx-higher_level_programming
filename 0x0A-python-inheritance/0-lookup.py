#!/usr/bin/python3
"""The module `0-lookup`.

Defines one function, `lookup()`.
"""


def lookup(obj: object):
    """gets the list of available attributes and methods of an object.

    Args:
        obj (:obj:`object`): object to retreive attributes from.

    Returns:
        :obj:`list`: list of available attributes and methods of `obj`.
    """
    return dir(obj)
