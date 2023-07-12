#!/usr/bin/python3
''' module 1-my_list
'''


class MyList(list):
    ''' class Mylist
        inherit from actual list
    '''
    def print_sorted(self):
        '''print sorted list'''
        self = list.sort(self)

    def __str__(self):
        '''return printable sorted list as a string'''
        j = 0
        s = '['
        for i in self:
            if j != 0:
                s += ', '
            i = str(i)
            s += i
            j += 1
        s = s + ']'
        return s
