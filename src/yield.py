#! /usr/bin/env python
# coding=utf-8

import sys

def fibonacci(n):
	a, b, c = 0, 1, 0
	while True:
		if c > n:
			return #raise StopIteration
		yield a #返回值a,包含yield的函数只能用作迭代器--生成器函数
		a, b = b, a+b
		c += 1
	
it = fibonacci(10)
for x in it:
	print(x, end=" ")
else:
	print("\n", end="")
	
it = fibonacci(10)
while True:
	try:
		print(next(it), end=" ")
	except StopIteration:
		print("\n", end="")
		break
		#sys.exit()
