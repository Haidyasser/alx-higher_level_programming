#!/usr/bin/python3
"""Module for matrix_divided method."""

def matrix_divided(matrix, div):
	"""Divides all elements of a matrix and returns a new matrix."""
	if type(matrix) is not list:
		raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
	for r in matrix:
		if(type(r) is not list):
			raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
		for c in r:
			if not isinstance(c, (int, float)):
				raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
	
	sz = len(matrix[0])
	for r in matrix:
		if len(r) != sz:
			raise TypeError("Each row of the matrix must have the same size")
		
	if not isinstance(div, (int, float)):
		raise TypeError("div must be a number")
	if div == 0:
		raise ZeroDivisionError("division by zero")
	return [[round(c / div, 2) for c in r] for r in matrix]
