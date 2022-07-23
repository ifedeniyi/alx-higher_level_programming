#!/usr/bin/python3
"""The `2-append_write` module.

It defines one function, `append_write()`.
"""


def append_write(filename="", text=""):
    """appends to a text file (UTF8) and returns the
        number of characters written.

    Args:
        filename (:obj:`str`, optional)
        text (:obj:`str`, optional)
    """

    with open(filename, 'a') as f:
        return f.write(text)
