#! /usr/bin/env python
# coding=utf-8

empty = {}
print("empty:\t", empty)

student = {"Tom":"23", "Tim":21, "Jack":"China"}
print(student)
print(student.keys())
print(student.values())
student.clear()
print(student.keys())
print(student.values())

name = "kang"
age = 32
dict = {}
dict[name] = age #关键字必须为不可变类型
print(dict)