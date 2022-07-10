#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    final_dict = {}

    for k, v in a_dictionary.items():
        if v == value:
            continue
        final_dict[k] = v
    
    a_dictionary.clear()
    a_dictionary.update(final_dict)
    return final_dict
