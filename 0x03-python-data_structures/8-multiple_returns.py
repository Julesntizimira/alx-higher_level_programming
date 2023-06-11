#!/usr/bin/python3
def multiple_returns(sentence):
    my_list = []
    my_list.append(len(sentence))
    if len(sentence) == 0:
        my_list.append(None)
    else:
        my_list.append(sentence[0])
    my_tuple = tuple(i for i in my_list)
