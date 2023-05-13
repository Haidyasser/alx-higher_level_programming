#!/usr/bin/python3


def no_c(my_string):
    ans = ""
    for c in my_string:
        if c != 'c':
            ans += c
    return ans
