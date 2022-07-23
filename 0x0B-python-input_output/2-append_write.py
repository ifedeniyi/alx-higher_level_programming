#!/usr/bin/python3
"""The `2-append_file` module.

It defines one function, `append_file()`.
"""


def append_file(filename="", text=""):
    """appends to a text file (UTF8) and returns the
        number of characters written.

    Args:
        filename (:obj:`str`, optional)
        text (:obj:`str`, optional)
    """

    with open(filename, 'a') as f:
        return f.write(text)
