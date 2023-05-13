#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(i), end="")
            if j+1 != len(matrix[i]):
                print(" ", end="")
        if i+1 != len(matrix):
            print("")