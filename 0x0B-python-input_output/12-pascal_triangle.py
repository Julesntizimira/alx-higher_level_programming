#!/usr/bin/python3
'''Defines pascal_triangle() function.'''


def pascal_triangle(n):
    '''returns a list of lists of integers
       representing the Pascal's triangle of n
    '''
    if n <= 0:
        return []

    trs = [[1]]
    while len(trs) != n:
        tr = trs[-1]
        temp = [1]
        for i in range(len(tr) - 1):
            temp.append(tr[i] + tr[i + 1])
        temp.append(1)
        trs.append(tmp)
    return trs
