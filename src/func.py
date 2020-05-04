#! /usr/bin/env python
# coding=utf-8

#必须参数
def ShowStr(str):
	print(str)
	
#关键字参数
def ShowNum(a, b=5, c=10):
	print("a=", a, "\tb=", b, "\tc=", c)
	
#默认参数
def ShowAge(age=23):
	print("age=%d" % age)
	
#可变参数--tuple
def PrintArgTuple(arg1, *vartuple):
	print("\narg tuple")
	print(arg1)
	print(vartuple, "\n")
	
#可变参数--dict
def PrintArgDict(arg1, **varDict):
	print("\narg dict")
	print(arg1)
	print(varDict, "\n")
	
#可变参数--中间星号*
def PrintAll(a, b=5, *vartuple, c):
	print("all kinds of args")
	print("a=", a)
	print("b=", b)
	print("c=", c)
	print("vartuple:", vartuple)
	
#匿名函数--lambda
sum = lambda arg1, arg2: arg1+arg2

#强制位置参数
def Func3_8(a, b, /, c, d, *, e, f):
	print("\n / for version3.8")
	print("a=", a)
	print("b=", b)
	print("c=", c)
	print("d=", d)
	print("e=", e)
	print("f=", f)
	

ShowStr("www.kangwenjun.com")
ShowNum(c=20, a=2)
ShowAge()#默认参数
PrintArgTuple("%d%c", 1, 2)
PrintArgDict("%d%c", name="Lucy", age=23)
PrintAll(3, c=7)
PrintAll(3, 2, 6, 1, 11, 111, c=8) #若要传可变参数，则需要按顺序
#PrintAll(3, 2, c=8, 6, 1, 11, 111) #错误
print("sum:\t", sum(2, 3))

#a, b不能使用关键字参数，只能使用位置参数
#c, d既可以用关键字参数，也可以用位置参数
#e, f只能用关键字参数
Func3_8(10, 20, 30, d=40, e=50, f=60) 
