#!/usr/bin/python3


def element_at(mylist, idx):
    if idx < 0:
        return None
    if idx >= len(mylist):
        return None
    return mylist[idx]
