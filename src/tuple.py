#! /usr/bin/env python
# coding=utf-8

print('\n----------------special tuple----------------')
print("(1):\t", type((1)))
print("(1,):\t", type((1,)))
print("():\t", type(()))

print('\n----------------all----------------')
print('("kang", "wen", "jun")', ("kang", "wen", "jun"))
print('("kang", "wen", "jun")[:]:\t', ("kang", "wen", "jun")[:])
print('("kang", "wen", "jun")[0:]:\t', ("kang", "wen", "jun")[0:])
print('("kang", "wen", "jun")[-1::-1]:\t', ("kang", "wen", "jun")[-1::-1])

print('\n----------------some----------------')
print('("kang", "wen", "jun")[0]:\t', ("kang", "wen", "jun")[0])
print('("kang", "wen", "jun")[0:-1]:\t', ("kang", "wen", "jun")[0:-1])
print('("kang", "wen", "jun")[0::2]:\t', ("kang", "wen", "jun")[0::2])

print('\n----------------joint----------------')
print('("kang", "wen", "jun")+("kang", "wen", "jun"):\t', ("kang", "wen", "jun")+("kang", "wen", "jun"))
print('("kang", "wen", "jun")*2:\t', ("kang", "wen", "jun")*2)

print('\n----------------iterater----------------')
print('"kang" in ("kang", "wen", "jun"):\t', "kang" in ("kang", "wen", "jun"))
for x in ("kang", "wen", "jun") :
	print('tuple-for:\t', x)
	
print('\n----------------operator----------------')
print('len(("kang", "wen", "jun")):\t', len(("kang", "wen", "jun")))
print('max((3, 1, 7, 5, 9)):\t', max((3, 1, 7, 5, 9)))
print('min((3, 1, 7, 5, 9)):\t', min((3, 1, 7, 5, 9)))
print('type(tuple([1,2,3])):\t', type(tuple([1,2,3])))
print('type(tuple((1,2,3))):\t', type(tuple((1,2,3))))
print('type(tuple({1, 2, 3})):\t', type(tuple({1,2,3})))
print('type(tuple({1:"Chinese", 2:"American", 3:"Italian"})):\t', type(tuple({1:"Chinese", 2:"American", 3:"Italian"})))
print('tuple({1:"Chinese", 2:"American", 3:"Italian"}):\t', tuple({1:"Chinese", 2:"American", 3:"Italian"}))

print('\n----------------other----------------')
tup = (1, 1.2, "name", 1+2j)
del tup #释放内存


#tup[0:2] = () #tuple不可以修改
