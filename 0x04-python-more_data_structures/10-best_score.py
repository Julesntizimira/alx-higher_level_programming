#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        my_list = sorted(a_dictionary)
        _max = a_dictionary[my_list[0]]
        s = ''
        for i in my_list:
            if a_dictionary[i] > _max:
                _max = a_dictionary[i]
                s = i
        return s
