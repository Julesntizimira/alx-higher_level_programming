#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict1 = a_dictionary.copy()
    for i in dict1:
        dict1[i] *= 2
    return dict1
