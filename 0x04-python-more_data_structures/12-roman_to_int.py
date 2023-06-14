#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    if isinstance(roman_string, str) is False:
        return None
    sum = 0
    dict1 = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    for i in range(-1, (len(roman_string) * -1) - 1, -1):
        if dict1[roman_string[i]] < dict1[roman_string[i + 1]] and i != -1:
            sum -= dict1[roman_string[i]]
        else:
            sum += dict1[roman_string[i]]
    return sum
