#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    op = ['+', '-', '*', '/']
    opr = [add, sub, mul, div]
    for i in range(4):
        print("{} {} {} = {}".format(a, op[i], b, opr[i](a, b)))
