#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    for i in str:
        if i == str[n]:
            continue
        s = s + i
    return str
