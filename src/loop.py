#! /usr/bin/env python
# coding=utf-8

print('\n----------------while ... else----------------')
n = 0
while n < 10 :
	#print("n:", n++)
	print(n, end=",")
	n += 1
else :
	print("%d\nwhile ... else\n" % n)
	
print('\n----------------for ... else----------------')
for x in ["C", "C++", "Perl", "Python"] :
	print(x, end=",")
else :
	print("Go\nfor ... else\n")
	
print('\n----------------range----------------')
print("range(5):\t", range(5))
for x in range(5) :
	print(x, end=" ")
else :
	print("\n", end="")
	
for x in range(5, 8) :
	print(x, end=" ")
else :
	print("\n", end="")
	
for x in range(5, 10, 2) :
	print(x, end=" ")
else :
	print("\n", end="")

print('\n----------------range and len----------------')
ls = ['Google', 'Baidu', 'kangwenjun', 'Taobao', 'QQ']
for x in range(len(ls)) :
	print(ls[x], end=" ")
else :
	print("\n", end="")
	
print('\n----------------pass----------------')
class MyEmptyClass :
	pass
print("while True :\n\tpass #ctrl+c")
# 导致打印中止，除非ctrl+c
#while True :
#	pass #键盘中断 ctrl+c