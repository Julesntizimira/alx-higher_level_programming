#!/usr/bin/python3
'''this is 101-lazy_matrix_mul module
it defines on function lazy_matrix_mul(), for example
>>> print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
[[ 7 10]
 [15 22]]
'''

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    '''multiply two matrix
       return product matrix
    '''
    return np.matmul(m_a, m_b)
