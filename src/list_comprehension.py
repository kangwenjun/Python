#! /usr/bin/env python
# coding=utf-8

#list
print("list-[x**2 for x in range(10)]:\t", [x**2 for x in range(10)])
print("list-[x**2 for x in range(10) if x % 2]:\t", [x**2 for x in range(10) if x % 2])
print("list-[x*y for x in range(1, 10) if x % 2 for y in range(x, 10) if 0 == y % 2]", [x*y for x in range(1, 10) if x % 2 for y in range(x, 10) if 0 == y % 2])
print("list-[[x,x**2] for x in range(5)]", [[x,x**2] for x in range(5)])

print("set-{x for x in range(5)}:\t", {x for x in range(5)})
print("dict-{x:x**2 for x in range(5)}:\t", {x:x**2 for x in range(5)})
print("tuple((x for x in range(5)))", tuple((x for x in range(5)))) #与其他不同：推导式产生的不是元组而是迭代器

tup_it = (x for x in range(5))
print("iterator to tuple:\t", tuple(tup_it))
tup_it = (x for x in range(5))
for x in tup_it:
	print(x, end=" ")
else:
	print("\n", end="")

tup_it = (x for x in range(5))
while True:
	try:
		print(next(tup_it), end=" ")
	except StopIteration:
		print("\n", end="")
		break