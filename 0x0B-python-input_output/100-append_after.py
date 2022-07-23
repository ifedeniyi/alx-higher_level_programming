#!/usr/bin/python3
"""`append_after` module"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line
        containing a specific string"""

    with open(filename, 'r+') as f:
        lines = f.readlines()
        dup_lines = []

        for line in lines:
            dup_lines.append(line)

            if line.find(search_string) >= 0:
                dup_lines.append(new_string)
                continue

        f.seek(0)
        f.writelines(dup_lines)
