#!/usr/bin/python3

def no_c(my_string):
    final_str = ''
    for i in my_string:
        if ord(i) == 67 or ord(i) == 99:
            continue
        final_str += i

    return final_str
