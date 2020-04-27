#! /usr/bin/env python
# coding=utf-8

student = {'Tom', 'Jim', 'Mary', "Tom", "Jack", "Rose"}
print("student:\t", student) #集合自动去重

empty = set()
print("empty:\t", empty)

all = {1, 1.2, True, "name"}
print("all:\t", all)

#成员测试
if "Rose" in student :
	print("Rose 在集合中")
else :
	print("Rose 不在集合中")
	
a = set("abcfefdsg")
b = set("sdfaerkej")
print("a:\t", a)
print("b:\t", b)
print("a-b:\t", a-b) #在集合a当中，集合b没有的元素
print("b-a:\t", b-a)
print("a|b:\t", a|b)
print("a&b:\t", a&b)
print("a^b:\t", a^b)