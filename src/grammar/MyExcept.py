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
	
class MyException(Exception):
	def __init__(self, value, message):
		self.value = value
		self.message = message
	def __str__(self):
		return "value:{0}, message:{1}".format(self.value, self.message)

try:
	raise MyException(2, "MyException")
except MyException as e:
	print(e.__str__())