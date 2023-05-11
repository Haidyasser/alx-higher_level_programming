#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    op = ['+', '-', '*', '/']
    op_func = [add, sub, mul, div]
    print(f"{a} {op[0]} {b} = {op_func[0](a, b)}")
    print(f"{a} {op[1]} {b} = {op_func[1](a, b)}")
    print(f"{a} {op[2]} {b} = {op_func[2](a, b)}")
    print(f"{a} {op[3]} {b} = {op_func[3](a, b)}")
