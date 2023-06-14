#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    _list = []
    for i in a_dictionary:
        if a_dictionary.get(i) == value:
            _list.append(i)
    for i in _list:
        a_dictionary.pop(i)
    return a_dictionary
