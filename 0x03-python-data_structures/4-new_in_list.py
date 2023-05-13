#!/usr/bin/python3


def new_in_list(mylist, idx, element):
    nlist = mylist[::]
    if idx < 0 or idx >= len(mylist):
        return nlist
    nlist[idx] = element
    return nlist
