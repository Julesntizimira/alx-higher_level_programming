#!/usr/bin/python3
''' this is 3-say_my_name module
this module contains on method say_my_name(), for example
>>> say_my_name('jules', 'ntizimira')
My name is jules ntizimira
'''


def say_my_name(first_name, last_name=""):
    ''' prints My name is <first name> <last name>
    '''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
