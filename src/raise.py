#! /usr/bin/env python
# coding=utf-8

try:
	raise ZeroDivisionError
except ZeroDivisionError:
	print("ZeroDivisionError")
else:
	print("other error")
finally:
	print("excuted anyway")