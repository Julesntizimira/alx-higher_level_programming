#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for raw in matrix:
        for j in raw:
            print("{:d}".format(j), end=("" if j == raw[len(raw) - 1] else " "))
        print()
