#!/usr/bin/python3
''' module 2-is_same_class
    defines one function is_same_class()
'''


def is_same_class(obj, a_class):
    ''' returns True if the object is exactly
        an instance of the specified class
        False otherwise
    '''
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    return False
