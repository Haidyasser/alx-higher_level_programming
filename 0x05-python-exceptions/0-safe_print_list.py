#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    cnt = 0
    try:
        for i in range(x):
            my_list[i]
        for i in range(x):
            print(my_list[i], end="")
        print("")
        return x
    except IndexError:
        cnt = 0
        for i in my_list:
            print(i, end="")
            cnt += 1
        print("")
        return cnt
