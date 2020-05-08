#! /usr/bin/env python
# coding=utf-8

try:
	1/0
except ZeroDivisionError:
	print("ZeroDivisionError")
else:
	print("other error")
finally:
	print("excuted anyway")