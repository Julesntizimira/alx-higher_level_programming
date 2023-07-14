#!/usr/bin/python3
'''Defines pascal_triangle() function.'''


def pascal_triangle(n):
    '''returns a list of lists of integers
       representing the Pascal's triangle of n
    '''
    if n <= 0:
        return []
    tri = [[1]]
    for i in range(n - 1):
        s_tria = []
        for j in range(i + 2):
            if j == 0:
                x = 0
                y = tri[i][j]
            elif j == i + 1:
                x = tri[i][j - 1]
                y = 0
            else:
                x = tri[i][j - 1]
                y = tri[i][j]
            s_tria.append(x + y)
        tri.append(s_tria)
    return tri
