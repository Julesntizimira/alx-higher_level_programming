#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    _list = my_list[:]
    if idx < 0:
        return _list
    if idx >= len(my_list):
        return _list
    else:
        _list[idx] = element
        return _list
