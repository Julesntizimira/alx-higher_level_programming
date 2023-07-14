#!/usr/bin/python3
'''Defines a class Student.'''


class Student:
    '''Represent a student.'''
    def __init__(self, first_name, last_name, age):
        ''' initialise a new insatance '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''retrieves a dictionary
           representation of a Student instance

           If attrs is a list of strings, only attribute
           names contained in this list must be retrieved.
           Otherwise, all attributes must be retrieved
        '''
        dic = {}
        if type(attrs) is list:
            for element in attrs:
                if type(element) is not str:
                    break
                if hasattr(self, element):
                    dic[element] = getattr(self, element)
            return dic

        return self.__dict__
