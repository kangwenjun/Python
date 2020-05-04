#! /usr/bin/env python
# coding=utf-8

def fibonacci(n):
	ls = []
	a, b = 0, 1
	while b < n:
		ls.append(b)
		a, b = b, a+b
	return ls