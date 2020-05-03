#! /usr/bin/env python
# coding=utf-8

ls = [1, 2, 3, 4]
it = iter(ls) # 第一步，创建迭代器
for x in it : # 第二步，使用next(it)
#	print(next(it), end=" ")# 重复使用next(it)
	print(x, end=" ")
else :
	print("\n", end="")
	
# 完整的迭代器使用流程
class MyNumbers:	# 第一步，实现迭代器类
	def __init__(self):
		self.val = 1
	
	def __iter__(self):
		self.val = 1
		return self #必须
		
	def __next__(self):
		if self.val < 10:
			x = self.val
			self.val += 1
			return x
		else:
			raise StopIteration #StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况
		
tmp = MyNumbers()
it = iter(tmp)# 第二步，创建迭代器
for x in it: # 第二步，使用next(it)，并捕获StopIteration和结束迭代
	print(x, end=" ")