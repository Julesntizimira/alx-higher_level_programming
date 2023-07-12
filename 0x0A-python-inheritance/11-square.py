#!/usr/bin/python3
''' defines Square class that inherit from triangle
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' inherit from class Rectangle
    '''
    def __init__(self, size):
        '''constructor'''
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        '''returns square area '''
        return self.__size * self.__size

    def __str__(self):
        ''' return string representation of square'''
        return "[Square] {}/{}".format(self.__size, self.__size)
