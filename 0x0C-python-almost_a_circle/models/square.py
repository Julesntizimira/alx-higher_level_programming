#!/usr/bin/python3
''' define class square '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' inherits from Rectangle '''
    def __init__(self, size, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''return string represantation of Square'''
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        '''Get/set square size'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''assigns attributes'''
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''dictionary represantation of an instance of class Square'''
        dict1 = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return dict1
