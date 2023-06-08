#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if len(sys.argv) - 1 != 3:
    exit(1)
a = int(sys.argv[1])
b = int(sys.argv[3])
if __name__ == "__main__":
    if len(sys.argv) - 1 != 3:
        exit(1)
    else:
        if sys.argv[2] == "+":
            print("{} {} {} = {}".format(a, sys.argv[2], b, add(a, b)))
        elif sys.argv[2] == "-":
            print("{} {} {} = {}".format(a, sys.argv[2], b,  sub(a, b)))
        elif sys.argv[2] == "*":
            print("{} {} {} = {}".format(a, sys.argv[2], b,  mul(a, b)))
        elif sys.argv[2] == "/":
            print("{} {} {} = {}".format(a, sys.argv[2], b,  div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
