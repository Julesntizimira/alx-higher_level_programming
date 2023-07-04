#!/usr/bin/python3
''' this is 5-text_indentation module
this module defines on function text_indentation(),
>>> text_indentation("hello?world")
hello?
<BLANKLINE>
world
'''


def text_indentation(text):
    ''' prints a text with 2 new lines
        after each of these characters: ., ? and :
    '''
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        print(i, end="")
        if i == '.' or i == '?' or i == ':':
            print('\n')
