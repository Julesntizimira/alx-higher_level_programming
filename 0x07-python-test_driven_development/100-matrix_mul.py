#!/usr/bin/python3
''' this is 100-matrix_mul module
this module defines matrix_mul() function
>>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
[[7, 10], [15, 22]]
'''


def matrix_mul(m_a, m_b):
    '''multiply two matrix
       return product matrix
    '''
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    length = len(m_a[0])
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(i) == 0:
            raise ValueError("m_a can't be empty")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
        if length != len(i):
            raise TypeError("each row of m_a must be of the same size")
    length = len(m_b[0])
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(i) == 0:
            raise ValueError("m_b can't be empty")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
        if length != len(i):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    m_b = [[raw[i] for raw in m_b] for i in range(len(m_b[0]))]
    new_matrix = []
    for i in range(len(m_a)):
        new_matrix.append([])
        for k in range(len(m_b)):
            sum = 0
            for j in range(len(m_a[i])):
                sum += m_a[i][j] * m_b[k][j]
            new_matrix[i].append(sum)
    return new_matrix
