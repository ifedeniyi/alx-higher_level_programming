#!/usr/bin/python3
"""The `6-load_from_json_file` module.

It defines one function, `load_from_json_file()`.
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”.

    Args:
        filename (string): file to write to
    """

    with open(filename) as f:
        return json.loads(f.read())
