# Your testing code
from src.my_math import add_numbers, subtract_numbers, multiply_numbers

def test1():
	res = add_numbers(222,3)
	assert res == 225

def test2():
	res = subtract_numbers(54,3)
	assert res == 51

def test3():
	res = multiply_numbers(21,30)
	assert res == 630



