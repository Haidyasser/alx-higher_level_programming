#!/usr/bin/python3
import sys
if __name__ == "__main__":
    cnt = len(sys.argv)
    sum = 0
    for i in range(1, cnt):
        sum += int(sys.argv[i])
    print(sum)
