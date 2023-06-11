#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = len(sentence),
    if len(sentence) == 0:
        my_tuple = my_tuple + None
    else:
        new_tuple = my_tuple + (sentence[0],)
    return new_tuple
