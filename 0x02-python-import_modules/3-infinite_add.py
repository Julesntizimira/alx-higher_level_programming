#!/usr/bin/python3
import sys
sum = 0
if __name__ == "__main__":
    for i in sys.argv:
        if i != sys.argv[0]:
            sum = sum + int(i)
    print("{}".format(sum))
