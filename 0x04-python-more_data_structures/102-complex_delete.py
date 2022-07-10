#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    final_dict = {}
    updated = False

    for k, v in a_dictionary.items():
        if v == value:
            updated = True
            continue
        final_dict[k] = v

    if updated:
        a_dictionary.clear()
        a_dictionary.update(final_dict)
        return final_dict

    return a_dictionary
