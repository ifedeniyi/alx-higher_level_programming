#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    unique = list(i for i in set_1) + list(j for j in set_2)

    return set(unique)
