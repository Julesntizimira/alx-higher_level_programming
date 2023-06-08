#!/usr/bin/python3
from sys import argv
number = 0
if __name__ == "__main__":
    if len(argv) - 1 == 0:
        print("{} arguments.".format(number))
    else:
        if len(argv) - 1 == 1:
            print("{} argument:".format(len(argv) - 1))
        else:
            print("{} arguments:".format(len(argv) - 1))
        for i in argv:
            if number != 0:
                print("{}: {}".format(number, i))
            number = number + 1
