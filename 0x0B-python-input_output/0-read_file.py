#!/usr/bin/python3
"""The `0-read_file` module.

It defines one function, `read_file()`.
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (:obj:`str`, optional)
    """

    with open(filename) as f:
        for line in f:
            print(line, end='')
