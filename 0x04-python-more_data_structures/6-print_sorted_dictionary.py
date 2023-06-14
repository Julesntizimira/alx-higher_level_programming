#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_list = sorted(a_dictionary)
    for i in my_list:
        print("{}: {}".format(i, a_dictionary[i]))
