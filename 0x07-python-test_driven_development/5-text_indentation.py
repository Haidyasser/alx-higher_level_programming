#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """a function that prints a text with 2 new lines after each of these"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    # lines = text.split("\n")
    subline = ""
    for c in text:
        subline += c
        if c in ".?:\n":
            print(subline.strip() + ("\n" if c in ".?:" else ""))
            subline = ""
    print(subline.strip(), end="")
        