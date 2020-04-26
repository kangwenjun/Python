#! /usr/bin/env python
# coding=utf-8

tuple = (1, 1.2, "name", 1+2j)
print(tuple)
print(tuple[0:])
print(tuple[-1::-1])

print(tuple[0])		#元素
print(tuple[0:1])	#元组，tuple

print(tuple[0:2])
print(tuple[0::2])

print(tuple*2)
print(tuple+tuple)

#tuple[0:2] = () #tuple不可以修改

empty = () #空元组
print(empty) 

one = (1,) #一个元素的元组
print(one)