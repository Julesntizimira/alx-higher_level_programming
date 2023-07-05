#!/usr/bin/python3
''' this 0-rectangle module
    defines class Rectangle
'''


class Rectangle:
    '''
    class Rectangle
    defines two property width and height
    '''

    def __init__(self, width=0, height=0):
        ''' init method, constructor method
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' Get/set rectangle width
            width must be an integer
            width must be >= 0"
        '''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' Get/set rectangle height
            height must be an integer
            height must be >= 0"
        '''
        return self.__width

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' return Rectangle Area
        '''
        return (self.__width * self.__height)

    def perimeter(self):
        ''' return Rectangle Perimeter
            if width or height is equal to 0, perimeter is equal to 0
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        ''' return string object when use str()
        '''
        s = ''
        if self.__width == 0 or self.__height == 0:
            return s
        for i in range(self.__height):
            for j in range(self.__width):
                s += '#'
            if i != self.__height - 1:
                s += '\n'
        return s

    def __repr__(self):
        ''' return a string representation of the rectangle
            to be able to recreate a new instance
            by using eval()
        '''
        return "Rectangle({}, {})".format(self.__width, self.__height)
