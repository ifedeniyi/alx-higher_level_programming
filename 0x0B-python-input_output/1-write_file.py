#!/usr/bin/python3
"""The `1-write_file` module.

It defines one function, `write_file()`.
"""


def write_file(filename="", text=""):
    """writes to a text file (UTF8) and returns the
        number of characters written.

    Args:
        filename (:obj:`str`, optional)
        text (:obj:`str`, optional)
    """

    with open(filename, 'w') as f:
        return f.write(text)
