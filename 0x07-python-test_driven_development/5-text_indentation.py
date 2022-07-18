#!/usr/bin/python3
"""The `5-text_indentation` module.

The `5-text_indentation` module supplies one function, `text_indentation`.

Example:
    >>> text_indentation = __import__("5-text_indentation").text_indentation
    >>> text_indentation("Zen of Python: lorem ipsum dolor")
    Zen of Python:
    <BLANKLINE>
    lorem ipsum dolor
"""


def text_indentation(text: str):
    """Prints a text with 2 new lines after each of these characters:
        `.`, `?` and `:`

    Args:
        text (str): String to format and print.

    Raises:
        TypeEerror: If `text` is not of type `str`.
    """

    i = 0

    if type(text) is not str:
        raise TypeError("text must be a string")

    while i < len(text):
        print(text[i], end='')

        if text[i] in ['.', '?', ':']:
            print('\n\n', end='')
            try:
                while(True):
                    if text[i+1] == ' ':
                        i += 1
                        continue
                    break

            except IndexError:
                break

        i += 1
