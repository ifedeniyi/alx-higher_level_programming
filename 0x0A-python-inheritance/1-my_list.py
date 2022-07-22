#!/usr/bin/python3
"""The module `1-my_list`.

Defines a list sub-class, `MyList()`.
"""


class MyList(list):
    """Definition of a custom list subclass."""

    __sorted_list = []

    def print_sorted(self):
        """Sorts and prints a list in ascending order."""

        MyList.__sorted_list = self.copy()
        MyList.__sorted_list.sort()
        print(MyList.__sorted_list)
