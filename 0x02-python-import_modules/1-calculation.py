#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    op = ['+', '-', '*', '/']
    op_func = [add, sub, mul, div]
    for i in range(4):
        print(str(a) + ' ' + op[i] + ' ', end='')
        print(str(b) + ' = ' + str(op_func[i](a, b)))
