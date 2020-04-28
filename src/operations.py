#! /usr/bin/env python
# coding=utf-8

lVal = 4 /2 #浮点数
print(isinstance(lVal, float))

lVal = 2//3 #向下取整除法,但结果的类型与分子分母有关
print(isinstance(lVal, int))

print(9//4) #2
print(9//-4) #-3
print(9//4.0) #2.0
print(9.0//-4) #-3.0


lVal = 2; #求幂运算
print(lVal**3) #2的三次方
lVal **= 4
print(lVal) #2的四次方

if n := lVal + 3 : #海象运算符
	print(n)

#逻辑运算符 and or not
a = 10
b = 20
print("a and b:", a and b) #结果中断表达式结果
print("a or b:", a or b)#结果中断表达式结果
print("not a:", not a) #结果：True,False

#成员关系运算符 in		not in
list = [1, 2, 3,4]
lVal = list[0]
if lVal in list :
	print("lVal in list")
lVal = 5
if lVal not in list :
	print("lVal not in list")
	
#身份运算符 is   	is not
print(id(a) != id(b))
print(a is not b)

a = b = 30
print(id(a) == id(b)) #引用了相同的对象:常量"30"
print(a is b)


#is 和 == 的区别
list2 = list;
print("list2 is list: ", list2 is list) #引用了同一个对象
print(list2 == list) #值相等

list2 = list[:]
print("list2 is list: ", list2 is list) #引用了不同的对象
print(list2 == list)