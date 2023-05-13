#!/usr/bin/python3
"""Module for printing integers of a list"""


def print_list_integer(my_list=[]):
    """Prints all integers of a list"""
    for i in my_list:
        print("{:d}".format(i))


if __name__ == "__main__":
    print_list_integer()
