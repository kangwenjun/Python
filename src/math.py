#! /usr/bin/env python
# coding=utf-8

import math

#abs 用于整数，浮点数，复数
print("abs(-1): ", abs(-1))
print("abs(-1.0): ", abs(-1.0))
print("abs(complex(1, 0)): ", abs(complex(1, 0)))

#max
print("max(1, 1.2): ", max(1, 1.2))
print("max([1, 3, 4, 7.9]: ", max([1, 3, 4, 7.9]))

#min
print("min(1, 3, 7): ", min(1, 3, 7))
print("min([1, 9, 8]: ", min([1, 9, 8]))

#math.fabs 用于整数，浮点数
print("math.fabs(-1): ", math.fabs(-1))
print("math.fabs(-1.0): ", math.fabs(-1.0))

#math.ceil 向上取整
print("math.ceil(math.pi): ", math.ceil(math.pi))
print("math.ceil(-46.9): ", math.ceil(-46.9))

#math.floor 向下整数
print("math.floor(math.pi): ", math.floor(math.pi))
print("math.floor(-46.9): ", math.floor(-46.9))

#round
print("round(3.1415926, 2): ", round(3.1415926, 2))
print("round(3.1415926, 3): ", round(3.1415926, 3))

#pow
print("pow(2, 2): ", pow(2, 2)) #内置方法:参数当作整数 即等价于2**2,并返回整数
print("math.pow(2, 2): ", math.pow(2, 2))  #参数当作浮点数 即等价于2.0**2,并返回整数
print("pow(1.2, 2): ", pow(1.2, 2)) #1.44

#math.exp 等价于e^x
print("math.exp(1): ", math.exp(1))
print("math.exp(2): ", math.exp(2))
print("math.e**1: ", math.e**1)
print("math.e**2: ", math.e**2)

#math.log x>0 返回x的自然对数 e^result = x
print("math.log(math.e): ", math.log(math.e))
print("math.log(math.exp(2)): ", math.log(math.exp(2)))

#math.log10
print("math.log10(10**1): ", math.log10(10**1))
print("math.log10(10**2): ", math.log10(10**2))

#math.modf 返回整数部分和小数部分
tupple = math.modf(math.pi)
print(tupple)
print(tupple[0]) #小数部分:浮点数
print(tupple[1]) #整数部分:浮点数

#math.sqrt
print("math.sqrt(100): ", math.sqrt(100))
