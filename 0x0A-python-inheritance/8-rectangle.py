#!/usr/bin/python3
''' module 5-base_geometry
    defines a class BaseGeometry as super
    and subclass Rectangle
'''


class BaseGeometry:
    ''' class BaseGeometry
    '''
    def area(self):
        '''raises an Exception with
           the message area() is not implemented
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''  validates value '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    ''' class Rectangle that inherits to BaseGeometry
    '''
    def __init__(self, width, height):
        '''constructor'''
        super().integer_validator("height", height)
        self.__height = height
        super().integer_validator("width", width)
        self.__width = width
