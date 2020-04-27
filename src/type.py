#! /usr/bin/env python
# coding=utf-8

lVal = 2
fVal = 2.0
bVal = True
cVal = 2+1j
print(type(lVal))
print(type(fVal))
print(type(bVal))
print(type(cVal))

print(isinstance(lVal, int))
print(isinstance(fVal, float))
print(isinstance(bVal, bool))
print(isinstance(cVal, complex))
print(type(lVal) == int)

lVal = 2.0
print(isinstance(lVal, float))