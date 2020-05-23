#! /usr/bin/env python
# coding=utf-8

for n in range(2, 10) :
	for x in range(2, n) :
		if n % x == 0 :
			print(n, " 等于 ", x, "*", n//x)
			break #跳过for之else
	else :
		print(n, " 是质数")