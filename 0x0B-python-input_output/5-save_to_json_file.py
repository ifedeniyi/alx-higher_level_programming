#!/usr/bin/python3
"""The `5-save_to_json_file` module.

It defines one function, `save_to_json_file()`.
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation

    Args:
        my_obj (:obj:`any`): object to serialize and write to file
        filename (string): file to write to
    """

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
