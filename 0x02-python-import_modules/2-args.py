#!/usr/bin/python3
import sys
if __name__ == "__main__":
    cnt = len(sys.argv)
    print("{} argument".format(cnt - 1), end="")
    if cnt == 1:
        print("s.")
    elif cnt == 2:
        print(":")
        print("1: {}".format(sys.argv[1]))
    else:
        print("s:")
        for i in range(1, cnt):
            print("{}: {}".format(i, sys.argv[i]))
