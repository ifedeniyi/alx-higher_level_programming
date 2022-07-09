#!/usr/bin/python3

def best_score(a_dictionary):
    max_key = None
    max_val = 0

    if a_dictionary is None:
        return None

    for i in a_dictionary.keys():
        if a_dictionary.get(i) > max_val:
            max_key = i
            max_val = a_dictionary.get(i)

    return max_key
