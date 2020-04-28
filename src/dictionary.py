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

good = dict([("apple", 23), ("huawei", 98), ("lenovo", 100)])
print(good)

name = "kang"
age = 32
dict = {} #保留字"dict"被覆盖
dict[name] = age #关键字必须为不可变类型
print(dict)

#good = dict([("apple", 23), ("huawei", 98), ("lenovo", 100)]) #保留字"dict"已被覆盖，无法使用