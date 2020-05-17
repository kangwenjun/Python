#! /usr/bin/env python
# coding=utf-8

'''
matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
'''
matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])

ls = []
for i in range(4):
	ls.append([row[i] for row in matrix])
print(ls)

ls = []
for i in range(4):
	tmp = []
	for row in matrix:
		tmp.append(row[i])
	ls.append(tmp)
print(ls)