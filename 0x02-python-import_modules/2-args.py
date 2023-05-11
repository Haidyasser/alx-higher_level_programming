#!/usr/bin/python3
import sys
if __name__ == "__main__":
    cnt = len(sys.argv)
    print("{} arguments".format(cnt - 1), end="")
    if cnt == 1:
        print(".")
    else:
        print(":")
        for i in range(1, cnt):
            print("{}: {}".format(i, sys.argv[i]))
