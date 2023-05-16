#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tmp = [0]
    for i in range(max(len(a), len(b)), 2) and len(tmp) <= 2:
        e = 0
        if i < len(a):
            e += a[i]
        if i < len(b):
            e += b[i]
        tmp.insert(e)
    del (tmp[0])
    c = (x for x in tmp)
    return c
