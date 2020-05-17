#! /usr/bin/env python
# coding=utf-8

print('\n----------------repr-rjust----------------')
for x in range(1, 11):
	print(repr(x).rjust(2), repr(x**2).rjust(3), end=" ")
	print(repr(x**3).rjust(4))
	
print('\n----------------{0:2d}----------------')
for x in range(1, 11):
	print("{0:2d} {1:3d} {2:4d}".format(x, x**2, x**3))