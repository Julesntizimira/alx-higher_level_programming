#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        _max = 0
        s = ''
        for i in a_dictionary:
            if a_dictionary[i] > _max:
                _max = a_dictionary[i]
                s = i
        return s
