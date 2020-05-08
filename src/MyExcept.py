#! /usr/bin/env python
# coding=utf-8

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