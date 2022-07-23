#!/usr/bin/python3
"""The `4-from_json_string` module.

It defines one function, `from_json_string()`.
"""
import json


def from_json_string(my_obj):
    """Deserializes to a python object from JSON string

    Args:
        my_obj (string): string to deserialize

    Returns:
        :obj:`object`: deserialized object
    """

    return json.loads(my_obj)
