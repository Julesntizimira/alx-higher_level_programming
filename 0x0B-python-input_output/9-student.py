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
        '''
        return self.__dict__
