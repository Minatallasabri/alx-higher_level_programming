#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for m in i:
            if m != i[-1]:
                print("{:d}".format(m), end=" ")
        else:
            print("{:d}".format(m), end="")
        print()
