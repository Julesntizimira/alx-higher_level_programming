#!/usr/bin/python3
'''This is the 0-add_integer module
The 0-add_integer module supplies one function, add_integer().  For example,
>>> add_integer(10, 5)
15
'''


def add_integer(a, b=98):
    ''' add two integers
        return a + b
    '''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    ''' Raise Exception if a or b are not int or float type'''
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    ''' Raise Exception if a or b are not int or float type'''
    a = int(a)
    b = int(b)
    ''' cast types to int '''
    return a + b
