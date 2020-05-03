#! /usr/bin/env python
# coding=utf-8

ls = [1, 2, 3, 4]
it = iter(ls) # 第一步，创建迭代器
for x in it : # 第二步，使用next(it)
#	print(next(it), end=" ")# 重复使用next(it)
	print(x, end=" ")
else :
	print("\n", end="")