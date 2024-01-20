#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """a function that prints a text with 2 new lines after each of these"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for c in text:
        print(c, end="")
        if c == '.' or c == '?' or c == ':':
            print("\n")
