#!/usr/bin/python3
''' defines class Rectangle that inherit from basegeometry
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' class Rectangle that inherits to BaseGeometry
    '''
    def __init__(self, width, height):
        '''constructor'''
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width
