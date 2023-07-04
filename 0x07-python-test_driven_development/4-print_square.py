#!/usr/bin/python3
''' this is 4-print_square module
this module contains one method print_square(), for example
>>> print_square(5)
#####
#####
#####
#####
#####
'''


def print_square(size):
    ''' prints a square with the character #.
    '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
