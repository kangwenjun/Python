#! /usr/bin/env python
# coding=utf-8

import sys

fbeg = 0
fcur = 1
fend = 2

f = open(sys.argv[0], "r")
print("isatty:", f.isatty())
print("file name:", f.name)
print("file no:", f.fileno())
f.seek(0, fend)
file_size = f.tell()

print('\n----------------read all file_size:{0}----------------'.format(file_size))
f.seek(0, fbeg)
print(f.read(-1))

print('\n----------------read line file_size:{0}----------------'.format(file_size))
f.seek(0, fbeg)
someline = f.readline()
print("\nreadline-type:", type(someline), "\n")
while "" != someline:
	print(someline)
	someline = f.readline()
	
print('\n----------------read lines-default file_size:{0}----------------'.format(file_size))
f.seek(0, fbeg)
print(f.readlines())

line_size = 10
print('\n----------------read lines-{line_size} file_size:{file_size}----------------'.format(line_size=line_size, file_size=file_size))
f.seek(0, fbeg)
someline = f.readlines(line_size) #list
print("\nreadlines-type:", type(someline), "\n")
while someline != []:
	print(someline)
	someline = f.readlines(line_size)

f.close()
