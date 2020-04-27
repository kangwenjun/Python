#! /usr/bin/env python
# coding=utf-8

str="www.kangwenjun.com";

print(str);
print(str[4]); #char
print(str[4:]); #第一点之后
print(str[4:-4]); #两点之间
print(str[4:14]); #两点之间
print(str[4:14:3]); #两点之间,间隔为3个字节的组合
print(str[4:-4] * 2); #两点之间,两次,即重复一次

desc= \
"""

	c/c++
	python
	java
"""

str += desc;

print(str);

print('Hello\tWorld!');
print(r'Hello\tWorld!'); #不发生转义