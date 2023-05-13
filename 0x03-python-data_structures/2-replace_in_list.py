#!/usr/bin/python3


def def replace_in_list(mylist, idx, element):
    if idx < 0:
        return mylist
    if idx >= len(mylist):
        return mylist
    mylist[idx] = element
    return mylist
