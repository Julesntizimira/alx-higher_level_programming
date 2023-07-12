#!/usr/bin/python3
''' module 1-my_list
'''


class MyList(list):
    ''' class Mylist
        inherit from actual list
    '''
    def print_sorted(self):
        '''print sorted list'''
        a = sorted(self)
        print(a)


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
