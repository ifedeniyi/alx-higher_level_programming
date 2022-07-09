#!/usr/bin/python3

def roman_to_int(roman_string):
    final_int = 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if roman_string is None or type(roman_string) != str:
        return 0

    for i, v in enumerate(roman_string):
        if i is len(roman_string) - 1:
            final_int += roman_dict[v]
            continue

        if roman_dict[v] >= roman_dict[roman_string[i+1]]:
            final_int += roman_dict[v]
            continue
        else:
            final_int += (-1 * roman_dict[v])
            continue

    return final_int
