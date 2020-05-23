#! /usr/bin/env python
# coding=utf-8

import math

print('\n----------------str and repr----------------')
print("str:\t", str("str"))
print("repr-str:\t", repr("str")) #产生一个解释器易读的表达形式
print("repr-tuple:\t", repr((1, 2, 3)))
print("repr-list:\t", repr([1, 2, 3]))
print("repr-set:\t", repr({1, 2, 3}))
print("repr-dict:\t", repr({1:1,2:2, 3:3}))
print("repr-any-other:\t", repr("repr\t\n"))
print("repr-any-other:\t", repr(1))
print("repr-any-other:\t", repr(1.3))
print("repr-any-other:\t", repr(1+2j))
print("type(repr(1)):\t", type(repr(1)))
print("type(repr({1, 2, 3})):\t", type(repr({1, 2, 3})))

print('\n----------------format----------------')
print("{}$, {}kg".format(2, 3))
print("{0}$, {1}kg".format(2, 3)) #占位符
print("{price}$, {weight}kg".format(price=2, weight=3)) #关键字

print("ascii-{!a}".format("china"))
print("str-{!s}".format("china"))
print("repr-{!r}".format("china"))

print("pi:{0:.3f}".format(math.pi))
print("price:{0:5}".format(5))

table = {'Baidu': 1, 'kangwenjun': 2, 'Taobao': 3}
print("Baidu:{0[Baidu]:d}, kangwenjun:{0[kangwenjun]:d}, {0[Taobao]:d}".format(table))

print('\n----------------%----------------')
print("pi:%5.3f" % math.pi) # % is discarding