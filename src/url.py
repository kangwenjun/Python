#! /usr/bin/env python
# coding=utf-8

from urllib.requese import urlopen

for line in urlopen("www.baidu.com"):
	line = line.decode("utf-8")
	print(line)