#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tmp = []
    for i in range(max(len(tuple_a), len(tuple_b), 2)) and len(tmp) < 2:
        e = 0
        if i < len(tuple_a):
            e += tuple_a[i]
        if i < len(tuple_b):
            e += tuple_b[i]
        tmp.append(e)
    return tuple(tmp)
