#!/usr/bin/python3
''' defines MyInt class'''


class MyInt(int):
    '''class MyInt inherit from int class of integers
    '''
    def __eq__(self, other):
        '''check equality
        '''
        if isinstance(other, MyInt):
            return self != other
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
