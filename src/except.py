#! /usr/bin/env python
# coding=utf-8

import sys
ls = [1, 2, 3, 4]
it = iter(ls)
while True :
	try :
		print(next(it), end=" ")
	except StopIteration :
		sys.exit()