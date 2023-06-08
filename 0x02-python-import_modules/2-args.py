#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) - 1 == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        j = 0
        for i in sys.argv:
            if j != 0:
                print("{} : {}".format(j, i))
            j = j + 1
