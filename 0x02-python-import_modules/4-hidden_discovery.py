#!/usr/bin/python38
import hidden_4

def print_names():
	for name in dir(hidden_4):
		if name.startswith("__"):
			print(name)

if __name__ == '__main__':
    print_names()
