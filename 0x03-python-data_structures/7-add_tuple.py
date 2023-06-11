#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    my_list = []
    for i in range(2):
        my_list.append((0 if i >= len(tuple_a) else tuple_a[i]) +
                       (0 if i >= len(tuple_b) else tuple_b[i]))
    my_tuple = tuple(i for i in my_list)
    return my_tuple
