#!/usr/bin/python3
"""The `append_after` module."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line
        containing a specific string."""

    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)

        for line in lines:
            if search_string in line:
                f.write(line + new_string)
            else:
                f.write(line)
