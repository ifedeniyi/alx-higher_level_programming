#!/usr/bin/python3
"""The `3-to_json_string` module.

It defines one function, `to_json_string()`.
"""
import json


def to_json_string(my_obj):
    """Serializes an object (string) to JSON

    Args:
        my_obj

    Returns:
        string: serialized JSON string
    """

    return json.dumps(my_obj)
