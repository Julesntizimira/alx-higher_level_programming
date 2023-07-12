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
        super().__init__(size, size)
