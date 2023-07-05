#!/usr/bin/python3
''' this 0-rectangle module
    defines class Rectangle
'''


class Rectangle:
    '''
    class Rectangle
    defines two property width and height
    '''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        ''' init method, constructor method
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = Rectangle.print_symbol

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
                s += f"{self.print_symbol}"
            if i != self.__height - 1:
                s += '\n'
        return s

    def __repr__(self):
        ''' return a string representation of the rectangle
            to be able to recreate a new instance
            by using eval()
        '''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        ''' called when you delete the class instance
        '''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' returns the biggest rectangle based on the area
            rect_1 must be an instance of Rectangle
            rect_2 must be an instance of Rectangle
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
