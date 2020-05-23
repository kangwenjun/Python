#! /usr/bin/env python
# coding=utf-8

import builtins

#Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域
print('\n----------------Global----------------')
print(builtins)

print('\n----------------builtins----------------')
print(dir(builtins))

print('\n----------------enclosing----------------')
def outer():
	outer_count = 1 #闭包函数外的作用域
	def inner():
		inner_count = 2 #局部作用域
		print("inner_count:{0}, outer_count:{1}".format(inner_count, outer_count))
	inner() #调用闭包函数
	
outer()

#其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问
print('\n----------------local----------------')
if True:
	if_count = 3
while True:
	while_count = 4
	break
for x in [1, 2, 3]:
	for_count = 5
try:
	try_count = 6
finally:
	finally_count = 7
	
def ShowCount():
	local_count = 8
	print("if_count:\t", if_count)
	print("while_count:\t", while_count)
	print("for_count:\t", for_count)
	print("try_count:\t", try_count)
	print("finally_count:\t", finally_count)
	print("local_count:\t", local_count)
ShowCount()

try:
	print("local_count:\t", local_count)
except NameError:
	print("local_count must be used in function 'ShowCount'.")
	
print('\n----------------global 关键字----------------')
global_num = 1
print("used in global:\t", global_num)
def global_test():
	#global global_num = 123 #语法错误
	global global_num
	global_num = 123
	print("used in local:\t", global_num)
global_test()
print("used in global:\t", global_num)

print('\n----------------nonlocal 关键字----------------')
def nonlocal_test():
	nonlocal_num = 1
	print("used in nonlocal:\t", nonlocal_num)
	def inner():
		nonlocal nonlocal_num
		nonlocal_num = 123
		print("used in local:\t", nonlocal_num)
	inner()
	print("used in nonlocal:\t", nonlocal_num)
nonlocal_test()

print('\n----------------python解释器bug----------------')
try:
	bug = 1
	def test():
		bug = bug + 1
	test()
except UnboundLocalError:
	print("python bug")
