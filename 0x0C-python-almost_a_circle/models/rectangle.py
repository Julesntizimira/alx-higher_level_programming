#!/usr/bin/python3
''' defines class Rectangle '''
from models.base import Base


class Rectangle(Base):
    ''' inherits from Base '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''
        self.integerValidator('width', width)
        self.__width = width
        self.integerValidator('height', height)
        self.__height = height
        self.integerValidator('x', x)
        self.__x = x
        self.integerValidator('y', y)
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''Get/set Rectangle Width'''
        return self.__width

    @width.setter
    def width(self, value):
        self.integerValidator('width', value)
        self.__width = value

    @property
    def height(self):
        '''Get/set Rectangle Height'''
        return self.__height

    @height.setter
    def height(self, value):
        self.integerValidator('height', value)
        self.__height = value

    @property
    def x(self):
        '''Get/set x'''
        return self.__x

    @x.setter
    def x(self, value):
        self.integerValidator('x', value)
        self.__x = value

    @property
    def y(self):
        '''Get/set y'''
        return self.__y

    @y.setter
    def y(self, value):
        self.integerValidator('y', value)
        self.__y = value

    def integerValidator(self, name, value):
        ''' integer validator '''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if name == 'x' or name == 'y':
            if value < 0:
                raise ValueError(f"{name} must be >= 0")
        else:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")

    def area(self):
        '''return the area of a rectangle'''
        return self.__width * self.__height

    def display(self):
        '''prints in stdout the Rectangle instance with the character #'''
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        '''print string represantation of an instance'''
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def display(self):
        ''' to print in stdout the Rectangle instance
            with the character # by taking care of x and y
        '''
        for z in range(self.__y):
            print("")
        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        '''
            Updates the arguments in the class
        '''
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        '''return dictionary represantation of an instance'''
        dict1 = {'x' : self.__x, 'y' : self.__y, 'id': self.id, 'height': self.__height, 'width': self.__width}
        return dict1
