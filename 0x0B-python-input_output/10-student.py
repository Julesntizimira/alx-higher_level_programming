#!/usr/bin/python3
'''Defines a class Student.'''


class Student:
    """
    class Student that defines a student
    """

    def __init__(self, first_name, last_name, age):
        ''' init methode or constructor '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        dic = {}
        if type(attrs) is list:
            for element in attrs:
                if type(element) is not str:
                    break
                if hasattr(self, element):
                    dic[element] = getattr(self, element)
            return dic

        return self.__dict__
