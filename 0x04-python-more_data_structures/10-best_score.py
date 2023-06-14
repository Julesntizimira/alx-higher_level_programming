#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        j = 0
        _max = 0
        s = ''
        for i in a_dictionary:
            if j == 0:
                    _max = a_dictionary[i]
                    j += 1
                    s = i
                    continue
            if a_dictionary[i] > _max:
                _max = a_dictionary[i]
                s = i
            j += 1
        return s
