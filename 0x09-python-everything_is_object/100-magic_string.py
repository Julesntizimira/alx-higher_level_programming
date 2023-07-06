#!/usr/bin/python3
def magic_string():
    magic_string.s = magic_string.s + 1 if hasattr(magic_string, "s") else 1
    return (('BestSchool' + ", ") * magic_string.s)[:-2]
