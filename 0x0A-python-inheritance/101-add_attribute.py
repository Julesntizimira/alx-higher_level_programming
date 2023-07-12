#!/usr/bin/python3
''' defines class add_attribute'''


def add_attribute(MyClass, name, value):
    '''adds a new attribute to an object
        if it is possible
    '''
    if hasattr(MyClass, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(MyClass, name, value)
