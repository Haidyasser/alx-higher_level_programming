#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initializes the data."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Returns the current square area."""
    def area(self):
        return self.__size ** 2
