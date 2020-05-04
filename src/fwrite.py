#! /usr/bin/env python
# coding=utf-8

f = open("py.txt", "w")
size = f.write("data:www.kangwenjun\n")
f.write("size:{0}".format(size))
f.close()

with open("py.txt", "w") as f:
	size = f.write("data:www.kangwenjun\n")
	f.write("size:{0}".format(size))