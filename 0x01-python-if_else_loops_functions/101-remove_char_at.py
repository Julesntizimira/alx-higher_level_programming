#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    s = ""
    for i in str:
        if i == str[n]:
            continue
        s = s + i
    return s
