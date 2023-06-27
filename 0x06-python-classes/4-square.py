#!/usr/bin/python3
'''Define a squre class'''


class Square:
    '''class square that defines a square'''
    def __init__(self,  size=0):
        '''constructor'''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        '''getter property'''
        return(self.__size)

    @size.setter
    def size(self, value):
        '''setter property'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''Public instance method'''
        return self.__size ** 2
